# Repository guidance for Claude

This repository contains Claude Code plugins for second-line financial-services workflows.

## Editing rules

- Keep plugin components at the plugin root. Only `plugin.json` belongs under `.claude-plugin/`.
- Managed-agent cookbooks are not in scope for the main path. Upstream-contribution cookbooks, if any, live under `managed-agent-cookbooks/<agent>/` and are excluded from the marketplace manifest and from `scripts/sync-agent-skills.py`.
- Do not recreate `plugins/vertical-plugins`.
- Prefer `skills/` over legacy `commands/` for new plugin actions.
- Every standalone agent plugin needs a primary agent plus focused subagents under `agents/`.
- After editing source skills, run `python3 scripts/sync-agent-skills.py` and `python3 scripts/check.py`.
- Keep examples public-source-derived and anonymous.
