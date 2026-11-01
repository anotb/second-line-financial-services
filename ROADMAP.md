# Roadmap

What's next, in rough priority order.

## Near term

1. Per-skill independent reviewer pass: drafting edits against the source spec for each skill.
2. Tighten `scripts/check-skill-content.py` Rule 3 (source-anchor depth): the rule fires per-bullet but anchors are split across `Citation:` / `Excerpt:` / `Link:` bullets, producing structural false positives. Either skip `Link:` bullets or evaluate the citation block as a unit.

## Next release

### Standalone agent plugins

Agent plugins (`ai-governance-reviewer`, `regulatory-change-analyst`, `third-party-risk-reviewer`, `controls-testing-analyst`, `risk-reporting-analyst`, `financial-crime-governance-reviewer`) are pulled from the current release pending a rebuild. A pre-launch validation eval found that capability skills are practitioner-grade but the agent layer is half-built: subagent definitions are frontmatter stubs distinguished only by name, the writer subagent's tool scope and artifact shape miss program-level engagements, and primary agents under-prompt for the engagement-level moves (dual-entity, multi-regulator, shared-services, deliverable shape) that justify them.

The rebuild target:

- **Two-agent shape (primary + critic).** The critic role earned its keep in eval (charter-type catches, agentic-ambiguity calls, dual-charter framing). Reader and writer roles were ceremony as built. The next iteration ships primary plus a differentiated critic with role-specific operating rules; the primary absorbs reader and writer duties.
- **Genuine maker / checker loop with subagent forking.** Targets actual context-isolated subagent forks for the critic pass rather than the in-context simulation pattern the prior design assumed. Critic loads only the skill spec, the brief, and the maker artifact; primary loads everything else. The two contexts never see each other directly; the critic returns a structured challenge log the primary reconciles. Latency is the trade-off; signal quality is the gain.
- **Depend, do not bundle.** Agent plugins declare dependencies on the capability plugins whose skills they orchestrate (`risk-compliance-core` for `scoping`; `third-party-operational-resilience` for `vendor-diligence`; etc.). The prior self-contained `skills.bundle.json` pattern duplicates content and creates drift; the rebuild uses plugin manifest dependencies once the install machinery is verified.
- **Engagement-level scoping prompts.** Primaries name dual-entity, multi-regulator, shared-services, and program-level-vs-artifact-shape as first-class scoping fields, not as inferred context.
- **Tool scopes match role.** Writer-equivalent roles get `Write`. Reader-equivalent roles do not. Validate before merge.
- **Live install eval.** Each agent ships with at least one golden conversation regression test exercising the maker / checker loop on a known-good brief.

When the agents land, the marketplace manifest gets the six entries back and the top-level README rebuilds the agent table.

### Cross-cutting overlay rollouts

- `cross-cutting/ai-ethics.md` shipped to five AI / model-risk skills (`genai-pre-prod-review`, `ai-use-case-intake`, `ai-risk-tiering`, `agentic-ai-controls`, `board-ai-risk-pack`). Extend to the remaining six (`model-card-builder`, `validation-plan`, `ai-act-triage`, `llm-vendor-evidence-review`, `prompt-injection-risk`, `rag-evaluation-review`), with per-skill tailoring of the intro and pitfalls heading.
- `cross-cutting/privacy.md` (currently on `dora-register-builder`) extends to `concentration-risk-review` and any other ops-resilience skill where ICT-arrangement personal-data flows are register-relevant.
- Conduct-overlay B2B-flow-through trigger (currently on `genai-pre-prod-review/conduct.md`) propagates to the other eight conduct overlay files in `ai-governance-model-risk`.

### New skills

- `bsa-aml-ra-methodology` skill in `financial-crime-governance`. Eval surfaced the gap (FDIC RA-methodology supervisory finding had no skill anchor; makers built workstream scaffolding off FFIEC and cross-skill RA references). Ships as a standalone skill, mirrors the existing `cdd-risk-review` shape.

### Modular install: README persona recipes

The plugin manifests already declare `risk-compliance-core` as a dependency, so installing any downstream plugin auto-pulls the foundation. The remaining work is on the README install section:

- Replace the current single install block with Quick start (everything one-liner), Persona recipes (8 personas with copy-paste install blocks), and Layered install (core / capability / sector explanation).
- Surface the "sector overlays inside capability skills are free" point so users don't double-install.
- Pure docs change.

Agent-plugin dependency declarations land alongside the agent rebuild.

### dora-register-builder full rebuild

- Schema rebuild against Commission Implementing Reg (EU) 2024/2956 (official ITS table / column codes, Annex labels, ICT-service-type taxonomy verbatim).
- R-tables, RT-tables, and relational tables alongside the B-tables in the official template.
- Internal-to-ITS service-type mapping table (currently held in the firm-overlay slot as a pointer; the actual code list the official Annex prescribes is not embedded).
- Examples body relabelling from "first-cycle build" framing to "preparation pass" framing.

### Schema dedup

Drop schemas a plugin's skills don't actually use, so each plugin only ships the generic schemas it needs. Plugin self-containment is preserved; the goal is removing unused copies, not relocating shared schemas.

### Other

- Firm-overlay starter: a worked example `references/firm-overlay.md` showing how a firm threads policy taxonomy, role labels, system-of-record names, decision forums, and committee templates into the skills.
- Approved MCP connectors for GRC, policy, document management, ticketing, data lineage, model inventory, vendor inventory, and incident management systems. Today the repo ships only `docs/examples/mcp.example.json` placeholders.
- EU overlay expansion across sector skills. UK still see-also.
- Cookbook layer for upstream PR candidates to `anthropics/financial-services` (initial candidates align with the agent rebuild above once the agents land).

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
- Golden conversation regression tests for the six standalone agents (lands with the agent rebuild).
