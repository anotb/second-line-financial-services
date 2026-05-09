#!/usr/bin/env python3
"""Sync bundled skills into agent plugins.

Agent plugins are deferred from v1 to v1.x and live under
``internal/agent-plugins-deferred/`` (gitignored). This script targets that
internal location so local builds and the eventual v1.x revival can keep
the bundled-skill copies in sync. If the internal directory is absent, the
script no-ops cleanly.

Bundle ``from`` paths are repo-relative under ``plugins/``; legacy bundles
shipped them as ``../../capability-plugins/...`` from the old in-tree agent
location, which the resolver here normalises.
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / 'internal' / 'agent-plugins-deferred' / 'agent-plugins'
PLUGINS = ROOT / 'plugins'

if not AGENTS.exists():
    print(f'no agent plugins to sync (looked at {AGENTS.relative_to(ROOT)})')
    sys.exit(0)


def resolve_skill_source(agent_dir: Path, raw_from: str) -> Path:
    candidate = (agent_dir / raw_from).resolve()
    if candidate.exists():
        return candidate
    for prefix in ('../../', '../'):
        if raw_from.startswith(prefix):
            stripped = raw_from[len(prefix):]
            candidate = (PLUGINS / stripped).resolve()
            if candidate.exists():
                return candidate
    raise FileNotFoundError(
        f'{agent_dir.name}: cannot resolve bundled skill source {raw_from}'
    )


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
        source = resolve_skill_source(agent_dir, item['from'])
        target = skills_dir / source.name
        shutil.copytree(source, target)
        count += 1
    print(f'synced {agent_dir.name}: {count} skills')
