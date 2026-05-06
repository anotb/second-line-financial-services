# Status

## Done

- Managed-agent cookbook scaffolding removed.
- Source taxonomy changed from vertical plugins to capability plugins plus sector overlays.
- Standalone agent plugins retained and expanded with focused plugin-shipped subagents.
- Public-source-derived examples added per skill under `plugins/<type>/<plugin>/skills/<skill>/examples/`.
- Shared policy, risk, control, source, review-gate, and output-template references added.
- JSON schemas added for obligations, controls, issues, AI use cases, vendors, test plans, and risk reports.
- Repository validation and public-content test scripts added and passing locally.
- Agent skill sync script added and used to bundle agent plugins.

## Not done

- Live `claude plugin validate` has not been run in Claude Code from this environment.
- No production MCP connectors are included. Only `.mcp.example.json` placeholders are provided.
- No firm-specific policy, risk taxonomy, issue-rating, control library, committee template, or legal interpretation is included.
- No confidential or named-institution examples are included.
- Golden conversation tests are represented as fixtures, expected-output files, and static content checks, not a live Claude evaluation harness.

## Known limitations

- Public-source-derived examples are useful for scaffolding and testing, but they are not substitutes for legal review or firm policy overlays.
- Some regulatory obligations evolve. Refresh `docs/source-map.md` and per-skill `references/source-anchors.md` before production use.
- Agent subagents are plugin-shipped Claude Code agents, not API-level delegation manifests.
