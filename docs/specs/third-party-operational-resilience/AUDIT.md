# third-party-operational-resilience — Phase 1 audit memo

Date: 2026-05-06
Phase: 1 (per-plugin scoping)
Plan: `docs/plans/2026-05-06-rationalized-plugin-map.md`

## Plugin role

Capability plugin for second-line third-party risk and operational-resilience work. Covers vendor lifecycle (diligence, contract, exit), portfolio (concentration), regulated-filing support (DORA register), and the testing programme that proves resilience claims (severe-but-plausible scenarios, exit testing). The plugin sits across US-deep (interagency guidance, FFIEC) and EU (DORA, EBA) source bases, with sector overlays for banking, insurance, capital markets, and payments-fintech. Cyber and privacy show up as cross-cutting overlays inside the skills that touch them, not as standalone plugins.

## v1 skill list (confirmed)

Seven skills, all carried from v0.2:

1. `concentration-risk-review`
2. `contract-gap-review`
3. `criticality-assessment`
4. `dora-register-builder`
5. `exit-plan`
6. `resilience-testing-pack`
7. `vendor-diligence` (now absorbs the AI-vendor scenario from the dropped `ai-vendor-review` skill in `ai-governance-model-risk`)

No skills added to this plugin in v1. The folder structure already matches the v1 list — no skill files to create or remove. The work in v1 is content (per-skill SKILL.md, references, templates, schemas, examples) and the description-discipline rewrite.

## Disagreements with the brief

None on the v1 list. Two notes for downstream phases:

- The `vendor-diligence` skill is now load-bearing. It absorbs AI-vendor diligence as a scenario, which is the right call (AI-vendor diligence is a vendor-diligence problem with cross-cutting AI considerations, not a separate workflow). The spec sheet treats AI-vendor mode as a conditional section (`ai_specific_findings` only populated when `ai_vendor=true`), keeps the cross-cutting cyber and privacy overlays in scope by default for AI vendors, and adds AI-specific common pitfalls. Phase 2 must keep the SKILL.md branch logic clean — one skill, one playbook, with an explicit AI-vendor branch — rather than two skills sharing a folder.
- The deeper question of "is the published evidence pack sufficient for our deployment context" lives downstream in `ai-governance-model-risk/llm-vendor-evidence-review`. `vendor-diligence` is the firm-side wrapper around the AI vendor as a third party; `llm-vendor-evidence-review` is the model-risk lens on the vendor's evidence pack. The boundary is documented in the `vendor-diligence` description ("Not the right tool when… use llm-vendor-evidence-review for that narrower question"). Phase 2 in `ai-governance-model-risk` must mirror the boundary from the other side.

## vendor-diligence absorption of the AI-vendor scenario — design notes

- One skill, one playbook, with an AI-vendor branch surfaced explicitly. Description includes AI vendor as a "Best for" trigger.
- Output template carries an AI-specific section (#14 in the named-section list) that is populated only when `ai_vendor=true`.
- Structured-output schema extends `vendor.schema.json` with an `ai_vendor` boolean and an `ai_specific_findings` object. The schema change is a phase 2 item; the spec sheet defines the field set.
- Two example scenarios in the spec sheet: one non-AI (cloud IaaS for a regional bank's core platform), one AI (foundation-model API for P&C insurer FNOL triage). This forces the SKILL.md to handle both cleanly in phase 2.
- Cyber and privacy overlays are in scope by default for AI vendors. The privacy overlay specifically calls out the prompt-as-customer-data problem.
- Common pitfalls include AI-specific items: published-system-card-as-substitute, training-data-retention-default, evaluation-coverage-on-deployed-system. These are the items that distinguish AI-vendor diligence from generic SaaS diligence and they need to be explicit so the skill does not collapse into a generic vendor checklist.

Confidence in the absorption design: high. The scenario is genuinely a vendor-diligence problem with AI overlays, not a separate workflow shape. The risk is description drift in phase 2 (the SKILL.md treating AI vendor as a side-note rather than a real branch). The two-example design and the named AI-specific section in the output template mitigate that risk.

## Plugin-level shared references plan

Stays plugin-level (used by every skill in this plugin):

- `references/source-map.md` — the public-source map. Trim to the rows actually used by this plugin's seven skills. Drop AI-governance, fair-lending, financial-crime, and risk-data-and-reporting rows that are not anchors here. Add: OCC Bulletin 2013-29, FFIEC IT Handbook (Outsourcing Technology Services and Business Continuity Management booklets), DORA Articles 28-30 specifically, EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02), NYDFS Part 500.11, NAIC Model Law on insurance outsourcing, BCBS Principles for Operational Resilience (March 2021), UK PRA SS2/21 and SS1/21 (UK overlay), FFIEC inter-agency cloud joint statement (April 2020), FFIEC inter-agency joint statement on community-bank fintech due diligence (August 2023), TIBER-EU framework reference for advanced testing.
- `references/policy-control-library.md` — keep the third-party-lifecycle and ICT-third-party-register rows. Drop rows for AI use-case intake, model risk tiering, control testing, risk reporting, cyber disclosure readiness, CDD and SAR governance, and small-business-lending data controls — those belong to other plugins. Add a baseline row on resilience testing (test methods, cadence, scenario types) to anchor `resilience-testing-pack`.
- `references/review-gates.md` — plugin-wide. Keep as-is in shape; phase 2 ensures every skill cites the named gates (scope, evidence, authority, impact, decision) and the confidence labels (high/medium/low/unknown).

Moves per-skill in phase 2:

- `references/output-templates.md` — currently houses obligation-map, control-test workpaper, executive risk pack outlines. None of these are this plugin's primitives. Remove from this plugin (the obligation-map and control-test artifacts belong to `risk-compliance-core` and `compliance-testing`; the executive-risk-pack outline belongs to `risk-reporting`). Phase 2 builds per-skill `templates/default-output.md` for each of the seven skills using the named-section lists in the spec sheets.
- `references/public-regulatory-scenarios.md` — currently a cross-plugin index. Repo-level, not plugin-level. Move to `common/references/` or `docs/` in phase 3.

Schemas:

- `schemas/vendor.schema.json` — keep here; primary use by `criticality-assessment`, `vendor-diligence`, `contract-gap-review`, `exit-plan`. Phase 2 extends the schema to carry the AI-vendor block and to align with the named-section structured-output fields in the spec sheets.
- `schemas/test-plan.schema.json` — used by `resilience-testing-pack` here and by `compliance-testing/control-test-workpaper` (different shape). Phase 3 should split these into two schemas (`schemas/resilience-test-plan.schema.json` here and a separate one in `compliance-testing`). Until then, leaving as-is is a structural concern, not a blocker.
- `schemas/ai-use-case.schema.json`, `obligation.schema.json`, `control.schema.json`, `issue.schema.json`, `risk-report.schema.json` — these belong to other capability plugins. Phase 3 moves them to their respective plugins (`ai-governance-model-risk`, `risk-compliance-core`, `risk-reporting`). Until then, borrowed schemas; do not extend them here.

Phase 3 also needs a register-of-information schema. The DORA register is structured data with a published ITS schema; phase 2 of `dora-register-builder` produces a structured artifact, and phase 3 should land a `schemas/dora-register.schema.json` aligned to the ITS tables (or split into per-table sub-schemas if simpler).

## Boundary call: vendor-diligence (this plugin) vs ai-vendor-review (deprecated)

`ai-vendor-review` was dropped from `ai-governance-model-risk` per the v1 plan. The replacement landing zone is split:

- The full firm-side AI-vendor-as-third-party diligence pack lives here, under `vendor-diligence`. This is the right home: it covers contract, exit, concentration, BCDR, cyber, privacy, and the AI-specific scenario fields together — i.e., the third-party-risk perimeter.
- The narrower model-risk-lens review of "is this published evidence pack sufficient for our deployment context" lives in `ai-governance-model-risk` as `llm-vendor-evidence-review`. This is not a duplicate; it is the model-risk function reviewing the evidence pack quality for an AI vendor whose third-party diligence has either already been done or will be informed by the evidence-quality finding.

Workflow: `vendor-diligence` triggers `llm-vendor-evidence-review` when the AI vendor is in scope and an evidence pack (system card, eval report, red-team summary) is provided. The `llm-vendor-evidence-review` output flows back into `vendor-diligence`'s `ai_specific_findings.eval_evidence_status` field and into the open-evidence-gaps section. Phase 2 in `ai-governance-model-risk` must lock the boundary from the other side; the `vendor-diligence` description in this plugin already does so.

Confidence in the boundary: high. The two skills do different work for different functions (third-party risk vs model risk) and chain cleanly. The risk is invocation drift (an agent invoking both for the same job and producing duplicate diligence). The activation-tuned descriptions in both spec sheets — "Not the right tool when…" — are the mitigation. Phase 3 should add a Phase-3 content-quality check that flags diligence packs where both skills appear to have produced overlapping content for the same arrangement.

## Structural concerns

1. The plugin manifest (`plugin.json`) currently lists the seven skills inline. Tighten the wording in phase 3 to match the v1 positioning (third-party-risk and operational-resilience capability plugin).
2. There is no `agents/` folder. Capability plugins do not require agents — that is the agent-plugins job. Confirmed correct. The `tprm-resilience-reviewer` agent plugin (when stood up) consumes these seven skills via the bundling pipeline.
3. There is no `examples/` folder under any of the seven skills. Phase 2 must create `examples/<scenario>.md` per skill (two scenarios per spec sheet). The two scenarios per skill are documented in this folder's spec sheets and serve as the contract.
4. None of the seven skills currently have a `references/` subfolder. Phase 2 creates `references/source-anchors.md` per skill, plus the sector-overlay files (all four sectors apply to every skill in this plugin) and the cross-cutting files (cyber and privacy for `vendor-diligence`, `contract-gap-review`, `exit-plan`, `resilience-testing-pack`).
5. The current `argument-hint` is the same generic string across all seven skills. Phase 2 rewrites per skill (e.g., `"[arrangement: vendor name, service, criticality, deployment context]"` for `vendor-diligence`).
6. The current `description` frontmatter is the v0.2 long-sentence form. Phase 2 replaces with the activation-tuned `Best for` / `Not the right tool when` / `Anchored to` shape per the spec sheets.
7. `[verify section]` and `[verify subarticle]` placeholders are used liberally across the spec sheets where exact section numbering is uncertain (especially DORA Article 28(2)/28(7)/28(8), Article 30(2)/(3), Article 24-26, EBA outsourcing-guidelines section numbers, FFIEC IT Handbook section numbering, NYDFS 500 sub-section numbering, ITS column codes for the DORA register). Phase 2 must resolve each placeholder against the published source. This is the largest single content-quality task for this plugin.
8. The DORA Register of Information ITS schema reference: the spec sheet for `dora-register-builder` indexes the register tables as `b_01` through `b_07` based on the public EBA preparation materials. The exact table identifiers and column codes in the adopted Commission Implementing Regulation must be verified in phase 2; the spec sheet flags this with `[verify ITS table number]` and `[verify ITS column codes]` throughout.

## Source-anchor confidence per skill

- `criticality-assessment` — high. Anchors are stable (interagency guidance June 2023, FFIEC BCM BIA, DORA Article 28, EBA outsourcing guidelines). Section-ref verification is the phase-2 task.
- `contract-gap-review` — high. Interagency contract-negotiation section, DORA Article 30(2)/(3), EBA outsourcing-agreement guideline, NYDFS 500.11. Phase 2 verifies subarticle numbering for DORA 30(2)/(3).
- `vendor-diligence` — high overall; medium on the AI-vendor sub-anchors. The non-AI anchors are stable. The AI-vendor sub-anchors (NIST AI RMF Generative profile NIST AI 600-1 subsections, ISO/IEC 42001 §7.4 and §8.4 cross-references, NAIC Model Bulletin 2023 third-party-AI section) need phase-2 verification against the published documents.
- `exit-plan` — high. DORA Article 28(8), EBA outsourcing-guidelines exit-strategy section, FFIEC BCM, interagency guidance termination. Phase 2 verifies the EBA exit-strategy section number.
- `concentration-risk-review` — high. DORA Article 29 is the named anchor; interagency guidance has the concentration framing in ongoing-monitoring and planning sections; FSB and BCBS papers as background. Phase 2 verifies DORA Article 29 subarticle structure.
- `resilience-testing-pack` — high. FFIEC BCM testing-and-exercise section, DORA Articles 24-26, BCBS principles. The TLPT references and TIBER-EU specifics need phase-2 verification.
- `dora-register-builder` — medium. The DORA Articles (28(3), 28(7)) are stable. The Commission Implementing Regulation adopting the ITS and the exact table-and-column codes (`b_01` through `b_07` as indexed in the spec) need careful verification in phase 2 against the published ITS. This is the single largest verification task in the plugin.

Phase 2 readiness: all seven spec sheets are present in this folder. Each contains the activation-tuned description, source anchors with section refs (or `[verify…]` placeholders), sector and cross-cutting overlay decisions, output template named sections, structured output fields, two example scenarios, and common pitfalls. Phase 2 subagents take the spec sheet as their contract.
