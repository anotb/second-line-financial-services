# ai-governance-model-risk — Phase 1 audit memo

Date: 2026-05-06
Phase: 1 (per-plugin scoping)
Plan: `docs/plans/2026-05-06-rationalized-plugin-map.md`

## Plugin role

Flagship capability plugin. Houses the second-line workflows that produce the AI and model risk artifact set: intake, tier, AI Act triage, model card, validation plan, agentic controls, board pack, plus a four-skill GenAI expansion (prompt injection, RAG evaluation, GenAI pre-prod gate, LLM vendor evidence). Other capability plugins reference outputs from here (third-party-operational-resilience consumes intake fields when running an AI-vendor diligence; risk-reporting consumes pack outputs into the enterprise risk committee pack; compliance-testing consumes model cards and validation plans into control test work).

## v1 skill list (confirmed)

Eleven skills:

1. `ai-use-case-intake`
2. `ai-risk-tiering`
3. `ai-act-triage`
4. `model-card-builder`
5. `validation-plan`
6. `agentic-ai-controls`
7. `board-ai-risk-pack`
8. `prompt-injection-risk` (NEW)
9. `rag-evaluation-review` (NEW)
10. `genai-pre-prod-review` (NEW)
11. `llm-vendor-evidence-review` (NEW)

No disagreement with the v1 skill list. The shape is right and the four GenAI additions land where a senior practitioner would expect them. The GenAI expansion is the v1 differentiator for this plugin and for the repo's market positioning.

## Changes vs v0.2

Drops:

- `ai-vendor-review` — absorbed into `vendor-diligence` in `third-party-operational-resilience` as an AI-vendor scenario mode. The existing `skills/ai-vendor-review/` folder (`SKILL.md`, `templates/`) and any references that point at it are scheduled for removal in phase 3, after the absorbed scenario mode is in place in TPRM. Do not delete now: `vendor-diligence` does not yet have the AI mode and an interim period of no AI-vendor coverage is worse than a soon-to-be-removed legacy skill.

Adds (NEW):

- `prompt-injection-risk` — second-line review of prompt-injection threat surface for a GenAI deployment. Anchored to NIST AI 600-1 Manage 2.7, OWASP Top 10 for LLM Applications, MITRE ATLAS, NCSC AI guidelines, NYDFS October 2024 letter.
- `rag-evaluation-review` — second-line review of retrieval and grounding evaluation for RAG. Anchored to NIST AI 600-1 Measure 2.9 and Measure 1.1, SR 11-7 §V, OCC Bulletin 2026-13.
- `genai-pre-prod-review` — pre-prod gate for a GenAI use case. Anchored to SR 11-7 §III to V, OCC Bulletin 2026-13, NIST AI RMF and NIST AI 600-1, EU AI Act Articles 9, 13, 14, 26 where applicable.
- `llm-vendor-evidence-review` — review of foundation-model vendor evidence packs against firm criteria. Anchored to SR 11-7 §VI, NIST AI 600-1 Govern 6.x and Manage 3.x, ISO/IEC 42001:2023 §7.4 / §8.x, EU AI Act Articles 51 to 55 where applicable. Pattern-references public Anthropic, OpenAI, Google system cards as the form factor under review.

Sector overlay absorptions:

- `ai-act-triage` MUST carry sector overlays for insurance and capital markets (insurance-ai-act-triage absorbed into this skill; the capital-markets overlay is required because of MiFID II / SEC overlap analysis for in-scope use cases).
- `agentic-ai-controls` MUST carry the insurance overlay (claims-ai-controls absorbed into this skill).

These overlays are reference documents inside the relevant capability skill, per the strict-sector-overlay rule in the v1 plan.

## Plugin-level shared references plan

Stays plugin-level (reused by every skill or many skills):

- `references/source-map.md` — public-source map for the plugin. Trim to rows actually used by this plugin's eleven skills (today the file is a near-duplicate of `common/references/source-map.md`). Phase 2 prunes unused rows and adds the GenAI-specific anchors that are missing today (NIST AI 600-1, OWASP Top 10 for LLM Applications, MITRE ATLAS, NCSC AI guidelines, NYDFS October 2024 letter, public system-card pattern references).
- `references/policy-control-library.md` — baseline AI control taxonomy. Used by `agentic-ai-controls`, `validation-plan`, `genai-pre-prod-review`. Keep here and extend with GenAI-specific control families (input filtering, output filtering, retrieval source vetting, tool boundary, structured output enforcement, content provenance, refusal behaviour, foundation-model swap revalidation).
- `references/review-gates.md` — named review gates and confidence labels. Used by every skill. Keep here.

Moves per-skill in phase 2:

- `references/output-templates.md` — the current generic templates do not match the artifact-shape of the eleven skills. Phase 2 moves artifact-specific templates into each skill's `templates/default-output.md`. The plugin-level file is removed.
- `references/public-regulatory-scenarios.md` — repo-level index, not plugin-level. Move to `common/references/` or `docs/` in phase 3 alongside the same move for `risk-compliance-core`.

Schemas:

- `schemas/ai-use-case.schema.json` — primary owner of this schema. Other plugins reference it.
- The other six schemas in this plugin's `schemas/` folder (`control.schema.json`, `issue.schema.json`, `obligation.schema.json`, `risk-report.schema.json`, `test-plan.schema.json`, `vendor.schema.json`) are borrowed from other plugins. Phase 3 moves them to their owning plugins. Keep here meanwhile to avoid dangling references.

Phase 2 will add per-skill `references/source-anchors.md` for every skill. Sector overlays (`references/sector-overlays/<sector>.md`) are required for skills as listed in the spec sheets. Cross-cutting overlays (`references/cross-cutting/<cyber|privacy|conduct>.md`) are required as listed; climate is not applicable for this plugin.

## Specific call-outs

- `ai-vendor-review` removal scheduled for phase 3 (not now). Reason: TPRM `vendor-diligence` does not yet have the AI-vendor scenario mode. Removing the legacy skill before the absorbed mode lands creates a coverage gap. Phase 3 sequencing: (1) confirm the AI mode is in `vendor-diligence`'s phase-2 build, (2) update cross-references, (3) remove `skills/ai-vendor-review/` and prune any references to it.

- GenAI expansion is the v1 differentiator. The four new skills are the most regulator-active bucket for 2025-26 (NIST AI 600-1, NYDFS October 2024 letter, OCC and FRB supervisory letters, EU AI Act GPAI, ISO/IEC 42001 implementation pressure) and the most likely to drive plugin discovery. Phase 2 must hold the source-anchor bar on these four skills.

## Source-anchor depth — per-skill confidence

Solid:

- `ai-use-case-intake` — NIST AI RMF, ISO/IEC 42001, SR 11-7 §III all apply directly with named sections.
- `ai-risk-tiering` — SR 11-7 §IV and NIST AI RMF Map 5.1 / Measure 2.6 land directly. OCC 2026-13 is required and marked `[verify section]` for risk-rating language pending the published bulletin sweep.
- `ai-act-triage` — EU AI Act articles and annexes are explicit with cited articles. Risk: phasing dates and AI Office guidance evolving in 2025-26; spec sheet flags `[verify dates]` for the AI Pact and Q&A guidance.
- `model-card-builder` — SR 11-7 §V, NIST AI RMF, ISO/IEC 42001 §7.5 all direct. Public system cards used as pattern reference, not as facts copied.
- `validation-plan` — SR 11-7 §V three pillars are direct. NIST AI 600-1 Measure subcategories applied with `[verify exact numbering]` flags where the spec sheet lists specific Measure numbers.
- `board-ai-risk-pack` — SR 11-7 §II to III and NIST AI RMF Govern functions land directly. ISO/IEC 42001 §5.1 / §9.3 land directly.

Watch (flagged in the spec sheets, must hold the bar in phase 2):

- `agentic-ai-controls` — NIST AI 600-1 Manage 2.7 / 2.8 / 4.1 are right but the exact subcategory numbering needs verification at SKILL.md write time. MITRE ATLAS technique IDs flagged `[verify exact taxonomy]`. NCSC and OWASP versions flagged `[verify edition]`. The substantive coverage is sound; the precise citation is what needs the second pass.

Thinner (flag for phase 2 scrutiny):

- `prompt-injection-risk` — coverage is sound on NIST AI 600-1, OWASP, MITRE ATLAS, NCSC, NYDFS. The risk is that NIST AI 600-1 subcategory numbering, OWASP edition, and ATLAS technique IDs need verification at SKILL.md write time. There is no single named federal financial-services rule directly on prompt injection; the strongest financial-services anchor is NYDFS October 2024 plus NIST AI 600-1. Flag this in phase 2 so the SKILL.md does not over-claim binding regulator language.
- `rag-evaluation-review` — NIST AI 600-1 Measure 2.9 / 1.1 land. SR 11-7 §V applies by analogy. The metric framework references (RAGAS-style metric families) are industry practice, not regulator requirement; the spec sheet handles this correctly by treating them as conceptual references only. Flag for phase 2: do not present industry metric frameworks as regulatory requirements.
- `genai-pre-prod-review` — strongest source coverage of the four new skills (SR 11-7 §III to V, OCC 2026-13 [verify], NIST AI RMF, NIST AI 600-1, ISO/IEC 42001, EU AI Act Articles 9 / 13 / 14 / 26 where applicable). The pattern is a roll-up of upstream artifacts, so the source anchors come through the upstream skills.
- `llm-vendor-evidence-review` — SR 11-7 §VI, NIST AI 600-1 Govern 6.x / Manage 3.x, ISO/IEC 42001 §7.4 / §8.x land. EU AI Act Articles 51 to 55 are correct for GPAI but evolving (Code of Practice, AI Office practice, phasing). Public system cards used as pattern reference. Flag for phase 2: the EU AI Act Articles 51 to 55 references must use current language as of the SKILL.md write date.

## Structural concerns

1. Every existing `SKILL.md` in this plugin is the same generic seven-step boilerplate, with only the name and description swapped. Confirmed by reading all eight current SKILL.md files. Phase 2 must produce skill-specific content.
2. `description` frontmatter today is one long sentence listing source URLs, not the activation-tuned `Best for` / `Not the right tool when` / `Anchored to` shape. Phase 2 fixes this per the spec sheets.
3. `argument-hint` today is the same generic placeholder across all eight skills. Phase 2 rewrites per skill.
4. None of the eight existing skills have a `references/` subfolder. Phase 2 creates `references/source-anchors.md` per skill, plus the sector-overlay and cross-cutting overlay files listed in each spec sheet.
5. None of the eight existing skills have an `examples/` subfolder. Phase 2 creates `examples/<scenario>.md` (two scenarios per spec sheet).
6. `templates/` exists per skill today, with a generic template not matched to the artifact shape. Phase 2 replaces with artifact-specific named-section templates per the spec sheets.
7. Six of the seven schemas in `schemas/` belong to other plugins. Phase 3 moves them to their owners. The plugin's own schema (`ai-use-case.schema.json`) needs an extension for GenAI fields (foundation-model dependence, RAG architecture, autonomy level enum extended for `agentic_with_tool_use`).
8. README mentions `ai-vendor-review` in the inventory list; phase 3 removes that mention together with the legacy skill. README also needs to highlight the GenAI expansion as the v1 differentiator (handled separately in this phase 1 README update).
9. No `agents/` folder in this plugin. Capability plugins do not require agents — that work is handled in the standalone agent plugins in phase 3. Confirmed correct.

## Phase 2 readiness

All eleven skills have spec sheets in this folder:

- `ai-use-case-intake.md`
- `ai-risk-tiering.md`
- `ai-act-triage.md`
- `model-card-builder.md`
- `validation-plan.md`
- `agentic-ai-controls.md`
- `board-ai-risk-pack.md`
- `prompt-injection-risk.md`
- `rag-evaluation-review.md`
- `genai-pre-prod-review.md`
- `llm-vendor-evidence-review.md`

Each spec sheet contains the activation-tuned description, source anchors with section refs (or `[verify section]` placeholders), sector and cross-cutting overlay decisions, output template named sections, structured output fields, two example scenarios, and common pitfalls. Phase 2 subagents take the spec sheet as their contract.

The four GenAI spec sheets specifically call out where source-anchor depth needs verification at SKILL.md write time. Phase 2 must hold the bar there; this plugin is the v1 differentiator and will receive the heaviest scrutiny.
