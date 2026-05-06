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
    for line in block.splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            data[k.strip()] = v.strip().strip('"')
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
    # Structural check: these legacy/demo locations must not exist in this repo.
    # Documentation may mention the old Anthropic source layout for comparison.
    legacy_demo = 'fake' + '-bank'
    banned_paths = ['managed-agent-cookbooks', 'plugins/vertical-plugins', f'examples/{legacy_demo}']
    for rel in banned_paths:
        if (ROOT / rel).exists():
            err(f'removed path still exists: {rel}')

    # Content check: example paths should remain public-regulatory and should not
    # reintroduce synthetic named-institution sample folders.
    examples = ROOT / 'examples'
    if examples.exists():
        for path in examples.rglob('*'):
            rel = path.relative_to(ROOT).as_posix()
            if legacy_demo in rel:
                err(f'legacy fake example path still exists: {rel}')

def check_agent_skill_drift():
    for agent_dir in sorted((ROOT / 'plugins' / 'agent-plugins').iterdir()):
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

def check_public_examples():
    examples = ROOT / 'examples' / 'public-regulatory'
    if not examples.exists():
        err('missing examples/public-regulatory')
        return
    files = list(examples.rglob('*'))
    content_files = [p for p in files if p.is_file() and p.suffix.lower() in {'.md', '.yaml', '.yml', '.csv', '.json'}]
    if len(content_files) < 10:
        err('expected at least 10 public-regulatory example files')
    for path in content_files:
        text = path.read_text(encoding='utf-8', errors='ignore')
        if path.suffix == '.md' and ('Source anchors' not in text and 'source_anchor' not in text):
            err(f'{path}: public markdown example should include Source anchors')

def check_schemas():
    for schema in (ROOT / 'schemas').glob('*.schema.json'):
        data = load_json(schema)
        if '$schema' not in data or 'required' not in data:
            err(f'{schema}: schema missing $schema or required')

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
check_public_examples()
check_schemas()

if errors:
    print('Validation failed:')
    for e in errors:
        print(f'- {e}')
    sys.exit(1)
print('Validation passed')
