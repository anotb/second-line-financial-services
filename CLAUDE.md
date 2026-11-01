# Repository guidance for Claude

This repository contains one Claude plugin for second-line financial-services workflows, at `plugins/second-line-financial-services/`. It is listed in Anthropic's directory from that folder, tracking `main`. Do not split it back into several plugins.

## Editing rules

- Keep plugin components at the plugin root. Only `plugin.json` belongs under `.claude-plugin/`.
- Managed-agent cookbooks are not in scope for the main path. Upstream-contribution cookbooks, if any, live under `managed-agent-cookbooks/<agent>/` and are excluded from the marketplace manifest.
- Do not recreate `plugins/vertical-plugins`.
- Prefer `skills/` over legacy `commands/` for new plugin actions.
- Keep each skill `description` to 120 characters or fewer, so all skills fit Claude Code's listing budget. Longer guidance goes in the skill's `## When to use` section.
- Raise `version` in `plugin.json` with every release, and don't reference files outside the plugin folder.
- After editing source skills, run `python3 scripts/check.py` and `python3 scripts/check-skill-content.py`.
- Keep examples public-source-derived and anonymous.
