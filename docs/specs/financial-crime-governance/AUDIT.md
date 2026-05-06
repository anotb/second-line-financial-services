# financial-crime-governance — Phase 1 audit memo

Date: 2026-05-06
Phase: 1 (per-plugin scoping)
Plan: `docs/plans/2026-05-06-rationalized-plugin-map.md`

## Plugin role

The financial-crime-governance plugin is the second-line review layer over a firm's BSA/AML, sanctions, and adverse-media program. It produces review artifacts for qualified human approvers (BSA officer, sanctions officer, EDD committee, SAR review committee, model risk committee). It does not own, approve, file, rate, or close anything. Every skill spec sheet states this guardrail explicitly under "Not the right tool when".

The plugin is US-deep first. EU and UK overlays come in v1.1 as overlay reference docs inside the relevant skill (FATF, EBA AML guidelines, UK MLRs, UK OFSI sanctions). The US anchor set is FFIEC BSA/AML Examination Manual, FinCEN rules and advisories, OFAC framework and guidance, OCC/FRB/FDIC/NCUA joint statements, and SR 11-7 / OCC 2026-13 for the AML monitoring system as a model.

## v1 skill list (confirmed)

Six skills, all carried from v0.2:

1. `aml-model-monitoring`
2. `cdd-risk-review`
3. `edd-escalation-pack`
4. `negative-news-triage`
5. `sanctions-screening-qa`
6. `sar-decision-qa`

No deletions. No renames. No additions.

## Changes vs v0.2

- No skill changes inside this plugin.
- `edd-escalation-pack` adds a conduct cross-cutting overlay (`references/cross-cutting/conduct.md`). PEP and high-risk-customer profiles intersect with conduct risk in a way that produces material findings the EDD committee should see (foreign-procurement exposure, sales-practice exposure for private banking and wealth segments, vulnerable-customer overlap with high-risk profiles).
- `sanctions-screening-qa` adds a cyber cross-cutting overlay (`references/cross-cutting/cyber.md`). Decision and rationale below.
- All six SKILL.md files are currently boilerplate (the same seven-step template with names swapped). Phase 2 rewrites content per the spec sheets in this folder.
- Source anchors today are bare URLs without section references. Phase 2 must add section references (or `[verify section]` placeholders) to every anchor.
- Descriptions today are formulaic and list source URLs in one long sentence. Phase 2 fixes per spec-sheet activation-tuned descriptions.

## Decision: cyber overlay on sanctions-screening-qa — INCLUDE

Decision: include `references/cross-cutting/cyber.md` on `sanctions-screening-qa`.

Rationale:

- Sanctions evasion via cyber and tech is a documented, live regulator concern, not speculative. OFAC has published industry-specific sanctions compliance guidance for the virtual currency industry (October 15, 2021) [verify date]. OFAC has issued ransomware-related advisories that explicitly address sanctions exposure for facilitating ransomware payments to designated parties. FinCEN has parallel virtual-currency and ransomware advisories.
- The overlay anchors cleanly to public OFAC and FinCEN material. It does not require speculative criteria.
- The typologies are screening-evasion-specific (virtual currency obfuscation, mixers and chain-hopping, BIN sponsorship and prepaid abuse, deepfake / synthetic-identity defeat of name-and-DOB matching, decentralized finance and bridge exposure). They are not a generic cyber-controls list. This keeps the overlay tight to the screening-QA artifact.
- A practitioner second-line sanctions QA without a cyber-evasion lens would miss the most active class of OFAC enforcement themes of the last several years.

The overlay is scoped narrowly to evasion typologies. General cyber controls (NYDFS Part 500 program-level, SEC cyber 8-K disclosure) sit elsewhere in the repo and are not duplicated here.

## Plugin-level shared references plan

Stays plugin-level (used by every skill, foundational):

- `references/source-map.md` — public-source map. Trim to rows actually relevant to this plugin's six skills (FFIEC manual sections, 31 CFR 1010.230, OFAC Framework, FinCEN advisories, SR 11-7 / OCC 2026-13). Remove rows that are foundational to other plugins (DORA, EU AI Act, BCBS 239, CFPB 1071) but not directly cited by any of these six skills.
- `references/policy-control-library.md` — baseline financial-crime control patterns (CIP controls, CDD pillars, sanctions screening configuration controls, SAR program controls, OFAC Framework five components mapped to control families). Keep here.
- `references/review-gates.md` — named review gates for financial-crime decisions (EDD committee gate, SAR review committee gate, sanctions release gate, model validation gate). Keep here.
- `references/output-templates.md` — current placeholder-grade. Phase 2 moves the artifact-specific outputs into each skill's `templates/default-output.md`. Plugin-level template stays only if it documents shared output conventions (executive summary length, source-trace format, confidence-label vocabulary).
- `references/public-regulatory-scenarios.md` — currently a cross-plugin index pointing at example scenarios. Same posture as in `risk-compliance-core/AUDIT.md`: this is a repo-level index, not a plugin-level reference. Phase 3 moves to `common/references/` or `docs/`.

Schemas (`schemas/`) currently include several borrowed schemas that belong to other capability plugins (`ai-use-case.schema.json`, `vendor.schema.json`, `test-plan.schema.json`, `risk-report.schema.json`, `obligation.schema.json`, `control.schema.json`). The financial-crime-governance plugin uses `issue.schema.json` directly. Phase 3 should:

- Keep `issue.schema.json` (used by every skill that surfaces material findings).
- Add three plugin-specific schemas in phase 2: `cdd-file.schema.json`, `alert-disposition.schema.json`, `sanctions-alert.schema.json`. Each spec sheet's structured-output-fields table is the contract.
- Remove or redirect the borrowed schemas to their owner plugins per the structural cleanup already noted in `risk-compliance-core/AUDIT.md`.

## Decision: aml-model-monitoring boundary call

`aml-model-monitoring` sits at the intersection of `financial-crime-governance` and `ai-governance-model-risk`. Both are correct homes for parts of the work.

Boundary, as adopted in the spec sheet:

- `ai-governance-model-risk` owns the model primitives: definition of "model", inventory, intake, tiering, model card, validation framework, ongoing-monitoring expectations as a category, governance and effective challenge. AML transaction-monitoring systems flow through those primitives the same way every other model does (intake → tiering → model card → validation → ongoing monitoring).
- `financial-crime-governance/aml-model-monitoring` owns the AML-specific monitoring governance artifact: data quality on AML feeds, customer segmentation drift, scenario inventory and tuning evidence, below-the-line testing, alert volume and productivity, threshold-change governance, and downstream effects into SAR decisioning.
- Skill scope explicitly excludes the validation deliverable itself (that is `validation-plan` in `ai-governance-model-risk`). It consumes validation evidence; it does not produce it.
- Skill scope explicitly excludes intake and tiering of the system as a model (those are `ai-use-case-intake` and `ai-risk-tiering` in `ai-governance-model-risk`).

Hand-off pattern: an AML monitoring system is intaked, tiered, and papered as a model in `ai-governance-model-risk`. It is then reviewed annually (or per cycle) in `financial-crime-governance/aml-model-monitoring`. Material findings here can trigger a re-tiering or re-validation in the model-risk plugin. Cross-references flow both ways via the inventory linkage in the structured output.

This is the right boundary because it lets a firm with strong central model risk management reuse the model primitives without re-implementing them inside a financial-crime silo, and lets a firm with strong financial-crime governance keep the AML-specific artifact close to the BSA/AML program.

## Source-anchor confidence per skill (phase 1 read)

- `cdd-risk-review` — high. FFIEC CDD section, FinCEN CDD Final Rule, 31 CFR 1010.230, FinCEN CIP rules, joint statements all stable. One `[verify]` flag: BOI reporting under 31 CFR 1010.380 given the CTA litigation timeline. Phase 2 must date the BOI status as-of and not assert it without grounding.
- `edd-escalation-pack` — high. FFIEC sections (PEP, private banking, correspondent), 31 CFR 1010.620 / 1010.610, FinCEN CDD Final Rule. Wolfsberg as public industry standard, not regulator. `[verify section]` flags on FFIEC online manual section anchors.
- `sar-decision-qa` — high. FFIEC SAR section, 31 CFR 1020.320 and parallels, 31 USC 5318(g), FinCEN form and advisories all stable. `[verify]` flags on specific FinCEN advisory dates and on parallel-rule citations for non-bank institution types.
- `aml-model-monitoring` — medium-high. SR 11-7 stable. OCC Bulletin 2026-13 and FDIC FIL anchors are the current revision in the repo's source map; section references inside `[verify]` until the revised guidance text is read against the spec. FFIEC SAR-section transaction-monitoring expectations are not a single named subsection; phase 2 must pin the exact anchor or flag.
- `sanctions-screening-qa` — high. OFAC Framework May 2019 stable; OFAC lists and 50 Percent Rule guidance stable; OFAC virtual currency and ransomware guidance dated and citable. `[verify]` flags on dated OFAC advisories where the version moves.
- `negative-news-triage` — medium. FFIEC manual covers ongoing CDD and adverse-information escalation but not as a single named "adverse media" section; phase 2 must pin the adverse-information anchor or flag. FinCEN CDD Final Rule fourth pillar covers ongoing monitoring and supports the artifact's existence. Wolfsberg is the cleanest public industry reference for the source-tier and identity-confidence concepts but is not a regulator anchor.

Across all six skills, every anchor has a public source. No invented regulatory facts. `[verify section]` placeholders are used wherever the section anchor is uncertain.

## Structural concerns

1. The current SKILL.md descriptions list source URLs in one long sentence — this is the formulaic v0.2 pattern. Phase 2 replaces with activation-tuned `Best for / Not the right tool when / Anchored to`.
2. The current `argument-hint` is the same generic string across all six skills. Phase 2 rewrites per skill (e.g., for `sar-decision-qa`: `"[alert file: alert chronology, investigation steps, disposition rationale]"`).
3. There is no `examples/` folder under any of the six skills. Phase 2 creates two example scenarios per skill per the spec sheets.
4. There is no `references/` subfolder under any of the six skills. Phase 2 creates `references/source-anchors.md` per skill plus the cross-cutting overlays for `edd-escalation-pack` (conduct) and `sanctions-screening-qa` (cyber).
5. Sector overlay folders are needed under every skill; phase 2 creates the four sector overlay files per skill where flagged in the spec sheet.
6. `schemas/` includes borrowed schemas from other plugins. Structural cleanup deferred to phase 3 per `risk-compliance-core/AUDIT.md`. Phase 2 adds three plugin-specific schemas (`cdd-file`, `alert-disposition`, `sanctions-alert`) tied to the structured-output-fields tables in this folder.
7. There is no `agents/` folder. Capability plugins do not require agents — that is the agent-plugins job. Confirmed correct.
8. Boundary with `ai-governance-model-risk` for `aml-model-monitoring` documented above. Phase 3 should add a one-line cross-reference inside both plugins' READMEs so practitioners arrive at the right artifact.

## Phase 2 readiness

All six skills have spec sheets in this folder:

- `aml-model-monitoring.md`
- `cdd-risk-review.md`
- `edd-escalation-pack.md`
- `negative-news-triage.md`
- `sanctions-screening-qa.md`
- `sar-decision-qa.md`

Each spec sheet contains: activation-tuned description; source anchors with section refs or `[verify]` placeholders; sector and cross-cutting overlay decisions; output template named sections; structured output fields; two public-source-derived example scenarios; common pitfalls. Phase 2 subagents take the spec sheet as their contract.
