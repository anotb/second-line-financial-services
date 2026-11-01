# Status

Current release: **1.0.1**.

## What ships

- One plugin with 68 skills: 8 capability groups and 4 sector groups.
- Each skill is self-contained: `SKILL.md`, source-anchors, sector and cross-cutting overlays, default template, optional schema, worked examples.
- US-deep at this release; EU as overlay; UK as see-also.
- MIT licensed.

## Recent

- Pre-launch validation eval across capability skills and the two most-used agent workflows.
- Capability-skill fixes from the eval (`scoping` schema split, `sar-decision-qa` sample-roll-up template, `fair-lending-test-plan` per-test specification block, `dora-register-builder` capital-markets enrichment, `genai-pre-prod-review` conduct B2B trigger).
- New cross-cutting `ai-ethics` overlay shipped to five AI / model-risk skills.
- New cross-cutting `privacy` overlay at `dora-register-builder`.
- Standalone agent plugins held back pending a rebuild that adds a maker / checker loop with context-isolated subagent forking and a primary-plus-critic shape. See [ROADMAP.md](ROADMAP.md).

## Limitations

- Public-source-derived examples and references only. Not legal interpretation, firm policy, or regulatory advice.
- Some regulatory anchors evolve quickly. Refresh `references/source-anchors.md` per skill before production use.
- Standalone agent plugins are not in this release.
- No production MCP connectors. Only `docs/examples/mcp.example.json` placeholders.
- No firm-specific policy, risk taxonomy, issue-rating, control library, committee template, or legal interpretation. Skills consume firm overlays via `references/firm-overlay.md` when a firm installs one.

## What's next

See [ROADMAP.md](ROADMAP.md). [CHANGELOG.md](CHANGELOG.md) carries the per-release history.
