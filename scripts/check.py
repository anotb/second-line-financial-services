#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r'^[a-z0-9][a-z0-9-]*[a-z0-9]$|^[a-z0-9]$')
errors = []

def err(msg):
    errors.append(msg)

def load_json(path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        err(f'{path}: invalid json: {exc}')
        return {}

def frontmatter(text):
    if not text.startswith('---\n'):
        return None
    end = text.find('\n---', 4)
    if end == -1:
        return None
    block = text[4:end]
    data = {}
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if ':' not in line:
            i += 1
            continue
        k, v = line.split(':', 1)
        k = k.strip()
        v = v.strip().strip('"')
        if v == '|' or v == '|-' or v == '>':
            # YAML literal/folded block scalar: gather following indented lines
            body = []
            j = i + 1
            while j < len(lines) and (lines[j].startswith(' ') or lines[j].startswith('\t') or lines[j] == ''):
                body.append(lines[j].lstrip())
                j += 1
            data[k] = '\n'.join(body).strip()
            i = j
            continue
        data[k] = v
        i += 1
    return data

def check_manifest(plugin_dir):
    manifest = plugin_dir / '.claude-plugin' / 'plugin.json'
    if not manifest.exists():
        err(f'{plugin_dir}: missing .claude-plugin/plugin.json')
        return
    data = load_json(manifest)
    name = data.get('name')
    if not name or not NAME_RE.match(name):
        err(f'{manifest}: plugin name must be kebab-case')
    if not data.get('version'):
        err(f'{manifest}: missing version')
    if not data.get('description'):
        err(f'{manifest}: missing description')

def check_skill(skill_dir):
    md = skill_dir / 'SKILL.md'
    if not md.exists():
        err(f'{skill_dir}: missing SKILL.md')
        return
    data = frontmatter(md.read_text(encoding='utf-8'))
    if data is None:
        err(f'{md}: missing YAML frontmatter')
        return
    name = data.get('name')
    desc = data.get('description')
    if name and not NAME_RE.match(name):
        err(f'{md}: invalid skill name {name}')
    if not desc or len(desc) < 80:
        err(f'{md}: description too short or missing')
    if not (skill_dir / 'templates' / 'default-output.md').exists():
        err(f'{skill_dir}: missing templates/default-output.md')

def check_agents(plugin_dir):
    agents_dir = plugin_dir / 'agents'
    if not agents_dir.exists():
        return
    agent_files = sorted(agents_dir.glob('*.md'))
    for md in agent_files:
        data = frontmatter(md.read_text(encoding='utf-8'))
        if data is None:
            err(f'{md}: missing agent frontmatter')
            continue
        for key in ('name', 'description', 'model', 'effort', 'maxTurns'):
            if not data.get(key):
                err(f'{md}: missing {key}')
        if data.get('name') and not NAME_RE.match(data.get('name')):
            err(f'{md}: invalid agent name {data.get("name")}')
    if 'agent-plugins' in str(plugin_dir) and len(agent_files) < 4:
        err(f'{plugin_dir}: agent plugin should include primary agent plus at least three focused subagents')

def check_marketplace():
    mp = ROOT / '.claude-plugin' / 'marketplace.json'
    if not mp.exists():
        err('missing .claude-plugin/marketplace.json')
        return
    data = load_json(mp)
    names = set()
    for plugin in data.get('plugins', []):
        name = plugin.get('name')
        source = plugin.get('source')
        if not name or not NAME_RE.match(name):
            err(f'marketplace plugin has invalid name: {name}')
        if name in names:
            err(f'marketplace duplicate plugin: {name}')
        names.add(name)
        if not source:
            err(f'marketplace plugin {name}: missing source')
        else:
            src = source[2:] if source.startswith('./') else source
            if not (ROOT / src).exists():
                err(f'marketplace source does not exist: {source}')

def check_no_removed_patterns():
    # Structural check: these legacy locations must not exist at the public root.
    # The Anthropic source repo layout pattern is mirrored at the root; v0.2-era
    # shared layers (root common/, examples/, tests/) live under internal/v0.2-archive/.
    banned_paths = ['managed-agent-cookbooks', 'plugins/vertical-plugins']
    for rel in banned_paths:
        if (ROOT / rel).exists():
            err(f'removed path still exists: {rel}')

def check_agent_skill_drift():
    for agent_dir in sorted((ROOT / 'plugins' / 'agent-plugins').iterdir()):
        if not agent_dir.is_dir():
            continue
        bundle = agent_dir / 'skills.bundle.json'
        if not bundle.exists():
            err(f'{agent_dir}: missing skills.bundle.json')
            continue
        data = load_json(bundle)
        for item in data.get('bundled_skills', []):
            src = (agent_dir / item['from']).resolve()
            dst = agent_dir / 'skills' / src.name
            if not src.exists():
                err(f'{agent_dir.name}: source skill missing {src}')
                continue
            if not dst.exists():
                err(f'{agent_dir.name}: bundled skill missing {dst}')
                continue
            src_text = (src / 'SKILL.md').read_text(encoding='utf-8')
            dst_text = (dst / 'SKILL.md').read_text(encoding='utf-8')
            if src_text != dst_text:
                err(f'{agent_dir.name}: bundled skill drift for {src.name}; run scripts/sync-agent-skills.py')

for base in [ROOT / 'plugins' / 'capability-plugins', ROOT / 'plugins' / 'sector-plugins', ROOT / 'plugins' / 'agent-plugins']:
    if not base.exists():
        err(f'missing {base}')
        continue
    for plugin_dir in sorted(p for p in base.iterdir() if p.is_dir()):
        check_manifest(plugin_dir)
        skills_dir = plugin_dir / 'skills'
        if skills_dir.exists():
            for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
                check_skill(skill_dir)
        check_agents(plugin_dir)

check_marketplace()
check_no_removed_patterns()
check_agent_skill_drift()

if errors:
    print('Validation failed:')
    for e in errors:
        print(f'- {e}')
    sys.exit(1)
print('Validation passed')
