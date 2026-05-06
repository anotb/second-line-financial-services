#!/usr/bin/env python3
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / 'plugins' / 'agent-plugins'

for agent_dir in sorted(p for p in AGENTS.iterdir() if p.is_dir()):
    bundle = agent_dir / 'skills.bundle.json'
    if not bundle.exists():
        continue
    data = json.loads(bundle.read_text(encoding='utf-8'))
    skills_dir = agent_dir / 'skills'
    if skills_dir.exists():
        shutil.rmtree(skills_dir)
    skills_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for item in data.get('bundled_skills', []):
        source = (agent_dir / item['from']).resolve()
        if not source.exists():
            raise FileNotFoundError(f'{agent_dir.name}: missing source skill {source}')
        target = skills_dir / source.name
        shutil.copytree(source, target)
        count += 1
    print(f'synced {agent_dir.name}: {count} skills')
