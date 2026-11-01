# Anthropic convention review

## Observed current conventions

Public Anthropic financial-services materials use:

- A root marketplace manifest at `.claude-plugin/marketplace.json`.
- Self-contained agent plugins under `plugins/agent-plugins/<slug>/`.
- Source plugin bundles under `plugins/vertical-plugins/<slug>/`.
- Plugin manifests at `<plugin>/.claude-plugin/plugin.json`.
- Agents as markdown files under `<plugin>/agents/` with YAML frontmatter.
- Skills under `<plugin>/skills/<skill>/SKILL.md`.
- Skill copying into self-contained agent plugins so installing the agent brings the needed skills.

## Design decision in this repo

This repo deliberately does not use `plugins/vertical-plugins`. The word vertical usually means sector or institution type, while this repo's strongest content is horizontal second-line capability: AI governance, third-party risk, compliance testing, regulatory change, risk reporting, and financial crime governance.

The resulting taxonomy is:

- Capability skill groups for reusable second-line functions.
- Sector skill groups for banking, insurance, capital markets and asset management, and payments or fintech overlays.

All of them live in one plugin, `plugins/second-line-financial-services/`. The repo originally held 12 plugins, one per group. It merged them because one install and one directory listing are simpler for users and maintainers, and because Anthropic's directory takes one submission per folder.

Agents (planned for a later release): workflow agents in the same plugin that orchestrate its skills. See [ROADMAP.md](../ROADMAP.md) for the rebuild target.

## Subagent convention

When agents ship, each will include a primary workflow agent and focused worker subagents, following Claude Code's plugin agent pattern, where agents are specialized Markdown files under `agents/` with frontmatter for name, description, model, effort, max turns, and tool scoping.

## Commands convention

Current Claude Code documentation says skills and command files both create slash invocations, but skills are recommended for new plugins because they support supporting files and richer metadata. This repo therefore avoids legacy `commands/` for new content.

## Source links

- Anthropic financial-services repo: https://github.com/anthropics/financial-services
- Claude Code plugins: https://code.claude.com/docs/en/plugins
- Claude Code plugin reference: https://code.claude.com/docs/en/plugins-reference
- Claude Code skills: https://code.claude.com/docs/en/skills
- Claude Code subagents: https://code.claude.com/docs/en/sub-agents
