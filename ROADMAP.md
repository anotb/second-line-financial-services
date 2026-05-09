# Roadmap

What's next, in rough priority order. See [STATUS.md](STATUS.md) for what's already landed and [internal/reviews/post-build-actions.md](internal/reviews/post-build-actions.md) for the consolidated action register.

## Near term

1. Run `claude plugin validate` against each plugin in the target Claude Code version. Live validation has not been run from the build environment.
2. Per-skill independent reviewer pass: drafting edits against the spec sheets in `internal/specs/`.
3. Resolve any remaining items in [internal/reviews/post-build-actions.md](internal/reviews/post-build-actions.md) flagged as open.

## v1.1

### Standalone agent plugins (deferred from v1)

Agent plugins (`ai-governance-reviewer`, `regulatory-change-analyst`, `third-party-risk-reviewer`, `controls-testing-analyst`, `risk-reporting-analyst`, `financial-crime-governance-reviewer`) are pulled from v1 and held under `internal/agent-plugins-deferred/` for the v1.x revival pass. The validation eval (8-case maker / checker run, [internal/eval-2026-05-09/synthesis/findings.md](internal/eval-2026-05-09/synthesis/findings.md)) found capability skills are practitioner-grade but the agent layer is half-built: subagent definitions are six-rule frontmatter stubs distinguished only by name, the writer subagent's tool scope and artifact shape miss program-level engagements, and primary agents under-prompt for the engagement-level moves (dual-entity, multi-regulator, shared-services, deliverable shape) that justify them.

The v1.x rebuild target:

- **Two-agent shape (primary + critic).** The critic role earned its keep in both eval cases (charter-type catches, agentic-ambiguity calls, dual-charter framing). Reader and writer roles were ceremony as built. v1.x ships primary plus a differentiated critic with role-specific operating rules; the primary absorbs reader and writer duties.
- **Genuine maker / checker loop with subagent forking.** v1.x targets actual context-isolated subagent forks for the critic pass rather than the in-context simulation pattern the v0 design assumed. Critic loads only the skill spec, the brief, and the maker artifact; primary loads everything else. The two contexts never see each other directly; the critic returns a structured challenge log the primary reconciles. Latency is the trade-off; signal quality is the gain.
- **Depend, do not bundle.** Agent plugins declare dependencies on the capability plugins whose skills they orchestrate (`risk-compliance-core` for `scoping`; `third-party-operational-resilience` for `vendor-diligence`; etc.). The v0 self-contained `skills.bundle.json` pattern duplicates content and creates drift; v1.x uses plugin manifest dependencies once the install machinery is verified.
- **Engagement-level scoping prompts.** Primaries name dual-entity and multi-regulator and shared-services and program-level-vs-artifact-shape as first-class scoping fields, not as inferred context.
- **Tool scopes match role.** Writer-equivalent roles get `Write`. Reader-equivalent roles do not. Validate before merge.
- **Live install eval.** Each agent ships with at least one golden conversation regression test exercising the maker / checker loop on a known-good brief.

When the agent revival lands, the marketplace manifest gets the 6 entries back and the top-level README rebuilds the agent table.

### Cross-cutting overlay rollouts

- `cross-cutting/ai-ethics.md` (new in v1) shipped to the 5 most load-bearing AI / model-risk skills (`genai-pre-prod-review`, `ai-use-case-intake`, `ai-risk-tiering`, `agentic-ai-controls`, `board-ai-risk-pack`). Roll out to the remaining 6 (`model-card-builder`, `validation-plan`, `ai-act-triage`, `llm-vendor-evidence-review`, `prompt-injection-risk`, `rag-evaluation-review`) in v1.1, with per-skill tailoring of the intro and pitfalls heading.
- `cross-cutting/privacy.md` (new in v1 for `dora-register-builder`) extends to `concentration-risk-review` and any other ops-resilience skill where ICT-arrangement personal-data flows are register-relevant.
- Conduct-overlay B2B-flow-through trigger (added in v1 to `genai-pre-prod-review/conduct.md`) propagates to the other 8 conduct overlay files in `ai-governance-model-risk` once a coordinated voice / structure pass is run.

### New skills

- `bsa-aml-ra-methodology` skill in `financial-crime-governance`. The eval surfaced the gap (FDIC RA-methodology supervisory finding had no skill anchor; makers built workstream scaffolding off FFIEC and cross-skill RA references). Ships as a standalone skill, mirrors the existing `cdd-risk-review` shape.

### Modular install (deferred from v1)

Analysis at [internal/research/modular-install-analysis-2026-05-09.md](internal/research/modular-install-analysis-2026-05-09.md). Two stages:

- **Stage 1, README install paths.** Replace the current Install section with Quick start (everything one-liner), Persona recipes (8 personas with copy-paste install blocks), and Layered install (core / capability / sector explanation). Surface the "sector overlays inside capability skills are free" point so users don't double-install. Pure docs change.
- **Stage 2, manifest dependencies.** Add `"dependencies": ["risk-compliance-core"]` to all 8 capability and 4 sector plugin manifests. Bare-name deps pull latest from same marketplace; versioned constraints (`^0.2`) require `claude plugin tag --push` discipline if adopted. Agent-plugin dependency declarations land alongside the v1.x agent revival.

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
- Cookbook layer for upstream PR candidates to `anthropics/financial-services` (initial candidates align with the agent revival above once the agents land).

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
- Subagent-name uniqueness across agent plugins (re-enabled when agents revive).
- Drift checks for copied references and schemas, not just skills.
- Schema additivity check: enforce the "additive changes only, never silent renames" prose currently documented across SKILL.md but not validated.
- Golden conversation regression tests for the 6 standalone agents (lands with the v1.x agent revival).
