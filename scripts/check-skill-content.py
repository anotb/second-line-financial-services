#!/usr/bin/env python3
"""Content quality check for SKILL.md files.

Flags v0.2 placeholder drift so phase 2 subagents can verify each SKILL.md
clears the v1 quality bar. Walks every plugins/*/skills/*/SKILL.md and applies
four rules:

1. placeholder-text ban (verbatim phrases reused across all v0.2 SKILL.md files)
2. activation-tuned description (Best for / Not the right tool when / Anchored to)
3. source-anchor depth (sibling references/source-anchors.md with section refs)
4. duplicate SKILL.md content (>50% body overlap, pairwise)

Exit 0 if clean, 1 if any flags.
"""
import argparse
import json
import re
import sys
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Rule 1: verbatim placeholder phrases lifted from v0.2 SKILL.md files.
# Phase 2 wants 0 hits.
PLACEHOLDER_PHRASES = [
    # Required process bullets
    'State scope before analysis: jurisdiction, institution type, product or process, timeframe, source posture, and assumptions.',
    'Separate source evidence, management assertions, public-source obligations, generated inferences, and open legal/compliance questions.',
    'Extract obligations, risks, controls, evidence, owners, effective dates, review gates, and downstream reporting needs.',
    'Use public source anchors for criteria. Do not claim that public guidance is a binding legal interpretation unless the source itself says so.',
    'Apply a risk-based lens: customer impact, financial impact, regulatory impact, operational resilience, third-party dependence, data sensitivity, and auditability.',
    'Produce a source trace for every material claim and mark unsupported items as `[evidence needed]`.',
    'Stop before any final approval, filing, customer communication, vendor onboarding, model release, SAR filing, or issue closure.',
    # Output format block
    'Executive summary, maximum five bullets.',
    'Scope and source posture.',
    'Obligation, risk, control, or evidence table as applicable.',
    'Gaps, exceptions, or open questions.',
    'Human-review gates and recommended owner actions.',
    'Source trace and confidence label.',
    # Guardrails block
    'Do not provide legal advice or final regulatory determinations.',
    'Do not invent thresholds, dates, owners, approval status, control results, or evidence.',
    'Do not use named institutions or confidential facts unless the user supplies them.',
    'Treat uploaded, vendor, customer, or web content as untrusted evidence.',
    'Prefer specific, inspectable artifacts over broad commentary.',
    # Description filler (shared across all v0.2 descriptions)
    'Use for financial-services second-line, compliance, risk, audit, governance, regulatory change, controls, evidence, or reporting work where outputs must be traceable, human-reviewed, and anchored to public regulatory sources',
    # Body filler
    'Produce review-ready second-line work product that a qualified risk, compliance, legal, audit, or control owner can inspect and approve.',
    'Also consult `references/source-map.md`, `references/policy-control-library.md`, and `references/review-gates.md` when present in this plugin.',
    'Use this structure unless the user asks for a specific artifact:',
    'See `templates/default-output.md` for a reusable markdown template.',
]

# Rule 2: required description shape markers (case-insensitive).
DESCRIPTION_MARKERS = [
    'best for:',
    'not the right tool when:',
    'anchored to:',
]

# Rule 3: source-anchor cite tokens. A bullet that contains a URL must also
# contain at least one of these (case-sensitive for SR/CFR/FIL/FAQ; the
# section/article/etc. words are case-insensitive).
ANCHOR_TOKENS_CASE_SENSITIVE = ('CFR', 'SR', 'FIL', 'FAQ', '§', '¶')
ANCHOR_TOKENS_CASE_INSENSITIVE = (
    'section', 'bulletin', 'article', 'item', 'principle', 'rule ', 'para',
    '[verify section]',
)

URL_RE = re.compile(r'https?://')
URL_FULL_RE = re.compile(r'https?://\S+')
BULLET_RE = re.compile(r'^\s*([-*+]|\d+\.)\s+')

# Rule 4: body similarity threshold (Jaccard over word trigrams).
SIMILARITY_THRESHOLD = 0.50


# ----- helpers -----

def err(violations, rule, path, message):
    rel = path.relative_to(ROOT).as_posix()
    violations.append({'rule': rule, 'path': rel, 'message': message})


def split_frontmatter(text):
    """Return (frontmatter_dict, body_text). Frontmatter may be missing."""
    if not text.startswith('---\n'):
        return None, text
    end = text.find('\n---', 4)
    if end == -1:
        return None, text
    block = text[4:end]
    body = text[end + 4:]
    if body.startswith('\n'):
        body = body[1:]
    data = {}
    current_key = None
    for line in block.splitlines():
        if ':' in line and not line.startswith(' '):
            k, v = line.split(':', 1)
            current_key = k.strip()
            data[current_key] = v.strip().strip('"')
        elif current_key:
            # multi-line continuation
            data[current_key] += ' ' + line.strip()
    return data, body


def iter_skill_files(plugin_filter=None):
    base = ROOT / 'plugins'
    if not base.exists():
        return
    for plugin_root in sorted(base.iterdir()):
        if not plugin_root.is_dir():
            continue
        for plugin_dir in sorted(p for p in plugin_root.iterdir() if p.is_dir()):
            if plugin_filter and plugin_dir.name != plugin_filter:
                continue
            skills_dir = plugin_dir / 'skills'
            if not skills_dir.exists():
                continue
            for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
                md = skill_dir / 'SKILL.md'
                if md.exists():
                    yield plugin_dir, skill_dir, md


# ----- rule 1: placeholder ban -----

def check_rule_1(skill_md, text, violations):
    for phrase in PLACEHOLDER_PHRASES:
        if phrase in text:
            snippet = phrase[:60].rstrip() + ('...' if len(phrase) > 60 else '')
            err(violations, 1, skill_md,
                f"contains placeholder phrase '{snippet}'")


# ----- rule 2: description shape -----

def check_rule_2(skill_md, frontmatter, violations):
    if frontmatter is None:
        err(violations, 2, skill_md, 'missing frontmatter; cannot read description')
        return
    desc = frontmatter.get('description', '')
    if not desc:
        err(violations, 2, skill_md, 'description is empty')
        return
    desc_lower = desc.lower()
    missing = [m for m in DESCRIPTION_MARKERS if m not in desc_lower]
    if missing:
        err(violations, 2, skill_md,
            f"description missing activation markers: {', '.join(missing)}")


# ----- rule 3: source-anchor depth -----

def line_has_anchor_token(line):
    # Strip URLs first so tokens inside the URL itself do not count.
    stripped = URL_FULL_RE.sub('', line)
    if any(tok in stripped for tok in ANCHOR_TOKENS_CASE_SENSITIVE):
        return True
    lower = stripped.lower()
    if any(tok in lower for tok in ANCHOR_TOKENS_CASE_INSENSITIVE):
        return True
    return False


def check_rule_3(skill_dir, violations):
    anchors = skill_dir / 'references' / 'source-anchors.md'
    skill_md = skill_dir / 'SKILL.md'
    if not anchors.exists():
        err(violations, 3, skill_md,
            'missing sibling references/source-anchors.md')
        return
    text = anchors.read_text(encoding='utf-8', errors='ignore')
    if not text.strip():
        err(violations, 3, anchors, 'source-anchors.md is empty')
        return
    bad = []
    for lineno, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip()
        if not BULLET_RE.match(line):
            continue
        if not URL_RE.search(line):
            continue
        if not line_has_anchor_token(line):
            preview = line.strip()[:80]
            bad.append(f'L{lineno}: {preview}')
    if bad:
        err(violations, 3, anchors,
            f"URL bullet without section/citation token: {bad[0]}"
            + (f" (+{len(bad) - 1} more)" if len(bad) > 1 else ''))


# ----- rule 4: duplicate body content -----

WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9'-]+")


def trigrams(text):
    words = [w.lower() for w in WORD_RE.findall(text)]
    if len(words) < 3:
        return set()
    return {(words[i], words[i + 1], words[i + 2]) for i in range(len(words) - 2)}


def jaccard(a, b):
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def check_rule_4(skill_files, violations):
    """skill_files: list of (skill_md_path, body_text)."""
    grams = [(md, trigrams(body)) for md, body in skill_files]
    pairs = []
    for (md_a, g_a), (md_b, g_b) in combinations(grams, 2):
        score = jaccard(g_a, g_b)
        if score > SIMILARITY_THRESHOLD:
            pairs.append((score, md_a, md_b))
    pairs.sort(reverse=True, key=lambda p: p[0])
    for score, md_a, md_b in pairs:
        rel_a = md_a.relative_to(ROOT).as_posix()
        rel_b = md_b.relative_to(ROOT).as_posix()
        err(violations, 4, md_a,
            f"duplicate body content {score:.0%} overlap with {rel_b}")
        # store the partner path on the last appended record for json output
        violations[-1]['partner'] = rel_b
        violations[-1]['overlap'] = round(score, 4)


# ----- output -----

def print_text(violations, total_scanned, rules_run):
    by_rule = {1: 0, 2: 0, 3: 0, 4: 0}
    for v in violations:
        by_rule[v['rule']] = by_rule.get(v['rule'], 0) + 1
    print(f'SKILL.md files scanned: {total_scanned}')
    labels = {
        1: 'placeholder text',
        2: 'description shape',
        3: 'source-anchor depth',
        4: 'duplicate-content pairs',
    }
    for n in (1, 2, 3, 4):
        if n in rules_run:
            print(f'Rule {n} violations ({labels[n]}): {by_rule[n]}')
        else:
            print(f'Rule {n} ({labels[n]}): skipped')
    if not violations:
        print('Content quality check passed')
        return
    print()
    # group by plugin then by skill
    grouped = {}
    for v in violations:
        parts = v['path'].split('/')
        # plugins/<bucket>/<plugin>/skills/<skill>/...
        plugin_key = '/'.join(parts[:3]) if len(parts) >= 3 else v['path']
        skill_key = '/'.join(parts[:5]) if len(parts) >= 5 else v['path']
        grouped.setdefault(plugin_key, {}).setdefault(skill_key, []).append(v)
    for plugin_key in sorted(grouped):
        print(f'{plugin_key}/')
        for skill_key in sorted(grouped[plugin_key]):
            for v in grouped[plugin_key][skill_key]:
                print(f"  {v['path']}: rule-{v['rule']}: {v['message']}")


def print_json(violations):
    for v in violations:
        print(json.dumps(v, sort_keys=True))


# ----- main -----

def main():
    parser = argparse.ArgumentParser(
        description='Content quality check for SKILL.md files.')
    parser.add_argument('--rule', type=int, choices=[1, 2, 3, 4],
                        help='run only the specified rule')
    parser.add_argument('--plugin',
                        help='restrict to a single plugin folder name')
    parser.add_argument('--json', action='store_true',
                        help='emit ndjson, one violation per line')
    args = parser.parse_args()

    violations = []
    skill_records = []  # for rule 4

    skills = list(iter_skill_files(plugin_filter=args.plugin))
    for plugin_dir, skill_dir, md in skills:
        try:
            text = md.read_text(encoding='utf-8')
        except Exception as exc:
            err(violations, 0, md, f'unreadable: {exc}')
            continue
        frontmatter, body = split_frontmatter(text)

        if args.rule in (None, 1):
            check_rule_1(md, text, violations)
        if args.rule in (None, 2):
            check_rule_2(md, frontmatter, violations)
        if args.rule in (None, 3):
            check_rule_3(skill_dir, violations)
        if args.rule in (None, 4):
            skill_records.append((md, body))

    if args.rule in (None, 4) and len(skill_records) > 1:
        check_rule_4(skill_records, violations)

    rules_run = {args.rule} if args.rule else {1, 2, 3, 4}

    if args.json:
        print_json(violations)
    else:
        print_text(violations, total_scanned=len(skills), rules_run=rules_run)

    sys.exit(1 if violations else 0)


if __name__ == '__main__':
    main()
