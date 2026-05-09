# Roadmap

What's next, in rough priority order. See [STATUS.md](STATUS.md) for what's already landed.

## Near term

1. Run `claude plugin validate` against each plugin in the target Claude Code version. Live validation has not been run from the build environment.
2. Close the `dora-register-builder` relabel inside `third-party-operational-resilience`.
3. Work through Phase 5 audit findings open in `internal/reviews/`.
4. Phase 3 schema relocation: move schemas borrowed across plugins for v1 to their owning plugins (per-skill schemas land under `<skill>/schemas/`).
5. Per-skill independent reviewer pass: drafting edits against the spec sheets in `internal/specs/`.

## v1.1

- Firm-overlay starter: a worked example `references/firm-overlay.md` showing how a firm threads policy taxonomy, role labels, system-of-record names, decision forums, and committee templates into the skills.
- Approved MCP connectors for GRC, policy, document management, ticketing, data lineage, model inventory, vendor inventory, and incident management systems. Today the repo ships only `.mcp.example.json` placeholders.
- EU overlay expansion across sector skills. UK still see-also.
- Cookbook layer for upstream PR candidates to `anthropics/financial-services` (initial candidates: `ai-governance-reviewer`, `regulatory-change-analyst`).
- Golden conversation tests for the six standalone agent workflows.

## Capability backlog

- Supervisory priority watchlist skills by regulator and sector.
- Policy-lifecycle workflows: annual review, attestation, exception handling, policy-control traceability.
- Data governance controls for AI, BCBS 239, regulatory reporting, and data-quality incidents.
- Operational-resilience scenario-test planner for severe but plausible scenarios (extends `resilience-testing-pack`).
- Issue-remediation validation and closure QA.

## Test backlog

- JSON Schema validation tests for every sample output (where the skill ships a schema).
- No-unsupported-claims lint for generated examples.
- Source-trace completeness tests.
- Subagent-name uniqueness across agent plugins.
- Drift checks for copied references and schemas, not just skills.
