# Roadmap

What's next, in rough priority order. See [STATUS.md](STATUS.md) for what's already landed and [internal/reviews/post-build-actions.md](internal/reviews/post-build-actions.md) for the consolidated action register.

## Near term

1. Run `claude plugin validate` against each plugin in the target Claude Code version. Live validation has not been run from the build environment.
2. Per-skill independent reviewer pass: drafting edits against the spec sheets in `internal/specs/`.
3. Resolve any remaining items in [internal/reviews/post-build-actions.md](internal/reviews/post-build-actions.md) flagged as open.

## v1.1

### Modular install (deferred from v1)

Analysis at [internal/research/modular-install-analysis-2026-05-09.md](internal/research/modular-install-analysis-2026-05-09.md). Two stages:

- **Stage 1, README install paths.** Replace the current Install section with Quick start (everything one-liner), Persona recipes (8 personas with copy-paste install blocks), and Layered install (core / capability / sector / agent explanation). Surface the "sector overlays inside capability skills are free" point so users don't double-install. Pure docs change.
- **Stage 2, manifest dependencies.** Add `"dependencies": ["risk-compliance-core"]` to all 8 capability and 4 sector plugin manifests. Skip agent plugins (already self-contained bundles). Bare-name deps pull latest from same marketplace; versioned constraints (`^0.2`) require `claude plugin tag --push` discipline if adopted.

### dora-register-builder full rebuild (deferred from v1)

Light relabel landed at commit d11e3b5. Full rebuild deferred:
- Schema rebuild against Commission Implementing Reg (EU) 2024/2956 (official ITS table / column codes, Annex labels, ICT-service-type taxonomy verbatim).
- R-tables, RT-tables, and relational tables alongside the B-tables in the official template.
- Internal-to-ITS service-type mapping table (currently held in the firm-overlay slot as a pointer; the actual code list the official Annex prescribes is not embedded).
- Examples body relabelling from "first-cycle build" framing to "preparation pass" framing.

### Schema dedup quick-win (replaces Phase 3 schema relocation)

Phase 3 schema relocation (move borrowed schemas to their owning plugins) was reconsidered after analysis showed plugin self-containment matters more than dedup for distribution; Anthropic's first-party FS plugins follow the same self-containing pattern. Replacement v1.1 plan: drop schemas a plugin's skills don't actually use, so each plugin only ships the generic schemas it needs. Lower blast radius than full relocation; same maintenance benefit.

### Other v1.1

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
- Schema additivity check: enforce the "additive changes only, never silent renames" prose currently documented across SKILL.md but not validated.
