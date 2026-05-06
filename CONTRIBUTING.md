# Contributing

## Add a new capability skill

1. Add a folder under `plugins/capability-plugins/<plugin>/skills/<skill-name>/`.
2. Add `SKILL.md` with frontmatter: `name`, `description`, and optional Claude Code fields such as `argument-hint`.
3. Add `templates/default-output.md`.
4. Update the plugin README if needed.
5. If a standalone agent should use the skill, add the source path to that agent's `skills.bundle.json`.
6. Run `python3 scripts/sync-agent-skills.py`.
7. Run `python3 scripts/check.py`.

## Add a new standalone agent

1. Create `plugins/agent-plugins/<agent-name>/`.
2. Add `.claude-plugin/plugin.json`.
3. Add `agents/<agent-name>.md` as the primary workflow agent.
4. Add at least three focused subagents under `agents/`.
5. Add `skills.bundle.json` and run the sync script.
6. Add the plugin to `.claude-plugin/marketplace.json`.
7. Run validation.

## Quality bar

- Use public or user-provided sources. Do not invent evidence.
- Include human-review gates for decisions, filings, approvals, and customer-impacting actions.
- Keep `SKILL.md` focused. Put long references in `references/`.
- Avoid named-institution examples unless the source is public and the repo maintainer has decided it is appropriate.
