# consumer-compliance-fair-lending — Phase 1 audit memo

Date: 2026-05-06
Phase: 1 (per-plugin scoping)
Plan: `docs/plans/2026-05-06-rationalized-plugin-map.md`

## Plugin role

Second-line review surface for consumer compliance and fair-lending work. Audience is consumer compliance officers, fair-lending and fair-housing leads, UDAAP review teams, marketing review teams, and complaint management leads, both inside regulated firms and inside advisory / consulting teams running the same work for those firms. Skills produce review artifacts, gap lists, and red flags for human decision; they do not approve loans, deny adverse-action notices, finalize fair-lending or UDAAP determinations, file 1071 data, or take down live marketing.

## v1 skill list (confirmed)

Six skills, all carried from v0.2:

1. `adverse-action-review`
2. `complaint-theme-analysis`
3. `fair-lending-test-plan`
4. `marketing-claim-review`
5. `section1071-readiness`
6. `udaap-risk-review`

No deletions. No renames. No additions.

## Changes vs v0.2

- No skill list changes.
- All six SKILL.md files are currently boilerplate (same seven-step procedure with name swapped). Phase 2 rewrites content per the spec sheets in this folder.
- Source anchors today are bare URLs without section references. Phase 2 must add section references to every anchor; URLs alone are insufficient under the v1 quality bar.
- Activation-tuned descriptions (Best for / Not the right tool when / Anchored to) are written in each spec sheet and replace the formulaic v0.2 frontmatter.
- Cross-cutting overlay decisions are reflected per the rationalized plugin map:
  - `adverse-action-review` adds `references/cross-cutting/privacy.md` (GLBA Safeguards on customer data used in adverse-action analytics; state-privacy implications evolve quickly, treated with `[verify state-specific scope]`).
  - `marketing-claim-review` adds `references/cross-cutting/privacy.md` (privacy-claim substantiation, AdChoices, dark-pattern privacy, CCPA / state-privacy interaction with marketing).
  - `udaap-risk-review` adds `references/cross-cutting/conduct.md` (UDAAP findings as the dominant conduct-risk signal; conduct-committee escalation).
  - `complaint-theme-analysis` adds `references/cross-cutting/conduct.md` (complaints as the canonical conduct-risk surveillance signal).

## AI-related guidance: skills that MUST cite the AI / algorithmic-discrimination authorities

AI-related cross-cutting is implicit in two skills and required in the SKILL.md and source-anchors:

- `adverse-action-review` — MUST cite CFPB Circular 2022-03 (May 26, 2022, on adverse action notification with complex algorithms) and CFPB Circular 2023-03 (September 19, 2023, on adverse action notices using AI / complex credit models — specific and accurate reasons), and the Joint Statement on Enforcement of Civil Rights, Fair Lending, Fair Housing, and Consumer Financial Protection Laws (CFPB / DOJ / FTC / EEOC, April 25, 2023). The "the model is too complex" defense is foreclosed; reasons must be specific and supported by the model.
- `fair-lending-test-plan` — MUST cite CFPB Circulars 2022-03 and 2023-03, the April 2023 Joint Statement, and HUD AI / algorithmic-underwriting guidance ([verify exact citation — HUD has issued multiple Office of Fair Housing communications post-2023]). Where any in-scope decision is AI / ML, the test plan must include less-discriminatory-alternative testing.

`marketing-claim-review` and `udaap-risk-review` reference the April 2023 Joint Statement when AI personalization, AI underwriting, AI-generated copy, or algorithmic targeting is in scope, but do not require it on every invocation. `complaint-theme-analysis` references the Joint Statement only where complaints surface algorithmic-discrimination patterns. `section1071-readiness` is not an AI-specific skill; AI references are not required.

## AI circular confidence

Confidence that the named AI circulars and the Joint Statement exist as cited:

- CFPB Circular 2022-03 (May 2022, adverse action with complex algorithms) — high confidence; widely cited and on the CFPB website.
- CFPB Circular 2023-03 (September 2023, adverse action accuracy with AI / complex models) — high confidence on existence and substance; phase 2 must verify the exact circular number and date because the bureau has issued several 2023 circulars on adverse action and the numbering / titling should be pinned. `[verify exact title and date]` markers are present in spec sheets where ambiguity exists.
- Joint Statement on Enforcement of Civil Rights, Fair Lending, Fair Housing, and Consumer Financial Protection Laws (CFPB / DOJ / FTC / EEOC, April 25, 2023) — high confidence; phase 2 confirms exact wording.
- HUD AI / algorithmic-underwriting guidance — medium confidence; HUD has published multiple Office of Fair Housing communications post-2023 and a 2024 letter on AI in tenant screening; phase 2 must pin the specific guidance applicable to credit / mortgage underwriting and use `[verify]` markers until pinned.
- Newer (2024-2025) CFPB AI circulars — assumed possible but not asserted; phase 2 sweep checks consumerfinance.gov/compliance/circulars for any newer items and adds them where relevant. Do not invent.

## Source-anchor confidence per skill

- `adverse-action-review` — high confidence on Reg B 1002.9 anchors (statutory and regulatory text is stable). Medium-high on CFPB Circulars (verify exact circular numbering as above). Medium on FCRA / Reg V 1022.74 cross-citations (stable but should be verified for current text).
- `complaint-theme-analysis` — high on Dodd-Frank §1031/1036 and the CFPB Complaint Database documentation. Medium on CFPB CMS Examination Procedures edition (phase 2 should pin the most recent edition). Medium on Supervisory Highlights (issue numbers and dates rotate).
- `fair-lending-test-plan` — high on ECOA / Reg B / FHA / HMDA statutory and regulatory anchors. Medium-high on Interagency Fair Lending Examination Procedures (FFIEC edition pinning). Medium on the CFPB Fair Lending Report (annual; needs current edition). Medium on HUD AI guidance.
- `marketing-claim-review` — high on Reg Z advertising rules (1026.16, 1026.24, 1026.40, 1026.60). Medium on MLA 32 CFR 232 mechanics. Medium on CFPB dark-pattern references (the bureau has discussed dark patterns in supervisory highlights and circulars; pin the named source in phase 2). Medium on AdChoices / DAA references (stable but evolving). Medium on FTC dark-patterns report (September 2022).
- `section1071-readiness` — high on the rule text (1002.103-114). Low-medium on the current effective compliance dates (court action and bureau response have moved them; phase 2 must pin the currently effective Tier dates and re-pin if they move again). Medium-high on the FIG (verify current edition).
- `udaap-risk-review` — high on Dodd-Frank §1031/1036 statutory text. Medium-high on the CFPB UDAAP Examination Manual (verify edition). Medium on the 2023 CFPB Policy Statement on Abusive Acts or Practices (verify exact title and date). Medium on the current set of UDAAP circulars (overdraft, junk fees, surprise representment, pay-to-pay) — these have been a focus area but the exact set in scope rotates.

`[verify ...]` markers are present in every spec sheet where confidence is below high.

## Plugin-level shared references plan

Stays plugin-level (used by every skill, foundational):

- `references/source-map.md` — public-source map. Plugin-wide. Trim to the rows actually used by this plugin's six skills (currently it duplicates `common/references/source-map.md` and contains many rows that are not consumer-compliance / fair-lending). Phase 2 prunes.
- `references/policy-control-library.md` — control patterns reused across skills (e.g., adverse action notice control, marketing review control, complaint management control, fair-lending testing control). Keep here and trim to consumer-compliance-relevant patterns.
- `references/review-gates.md` — named review gates and confidence labels. Plugin-wide. Keep here.

Moves per-skill in phase 2:

- `references/output-templates.md` — templates fragment per skill into `<skill>/templates/default-output.md` per the v1 anatomy. The current single output-templates file is generic and conflicts with the per-skill named-section templates in the spec sheets. Remove the generic file in phase 3 once per-skill templates are in place.
- `references/public-regulatory-scenarios.md` — repo-level index of public-source-derived scenarios. Move to `common/references/` or `docs/` per the same recommendation in `risk-compliance-core/AUDIT.md`. Until then, leave as-is and stop adding to it from skill content.

Schemas at plugin level today: `ai-use-case.schema.json`, `control.schema.json`, `issue.schema.json`, `obligation.schema.json`, `risk-report.schema.json`, `test-plan.schema.json`, `vendor.schema.json`. Most of these are borrowed from `risk-compliance-core` and other plugins. Phase 3 should:

- Move `ai-use-case.schema.json` to `ai-governance-model-risk` (not used by this plugin's six skills).
- Move `vendor.schema.json` to `third-party-operational-resilience` (not used by this plugin's six skills).
- Move `risk-report.schema.json` to `risk-reporting`.
- Move `test-plan.schema.json` to `compliance-testing`.
- Keep `obligation.schema.json`, `control.schema.json`, `issue.schema.json` (referenced by these skills' findings).
- Add new plugin-specific schemas in phase 2 per the structured-output fields enumerated in the spec sheets:
  - `adverse-action-review.schema.json`
  - `complaint-theme-analysis.schema.json`
  - `fair-lending-test-plan.schema.json`
  - `marketing-claim-review.schema.json`
  - `section1071-readiness.schema.json` (aligned to 12 CFR 1002.107 data points; `[verify schema completeness]`)
  - `udaap-risk-review.schema.json`

## Structural concerns

1. `plugin.json` description likely lists the six skills inline with the boilerplate description; phase 3 tightens to the v1 positioning (consumer compliance and fair-lending second-line review surface).
2. There is no `agents/` folder. Capability plugins do not require agents — that is the agent-plugins job. Confirmed correct.
3. None of the six skill folders have `references/`, `examples/`, or `schemas/` subfolders; they only have `templates/`. Phase 2 creates the per-skill anatomy:
   - `<skill>/references/source-anchors.md`
   - `<skill>/references/sector-overlays/*.md` per the spec sheet
   - `<skill>/references/cross-cutting/*.md` for the four skills that take cross-cutting overlays (privacy on adverse-action-review and marketing-claim-review; conduct on udaap-risk-review and complaint-theme-analysis)
   - `<skill>/templates/default-output.md` (named sections per the spec sheet, replacing whatever generic content lives there today)
   - `<skill>/schemas/<skill>.schema.json`
   - `<skill>/examples/<scenario>.md` (two scenarios per spec sheet)
4. The current `argument-hint` is the same generic string across all six skills. Phase 2 rewrites per skill (e.g., `"[notice population, decision data, model output, period]"` for adverse-action-review).
5. The current `description` frontmatter is malformed for activation purposes (long sentence with embedded URLs). Phase 2 replaces with the activation-tuned shape from each spec sheet.
6. `templates/` exists per skill but content is generic. Phase 2 replaces with the named-section template specific to the skill.
7. Section 1071 compliance dates are court-revised and moving. Phase 2 pins them at the time of writing and includes a refresh note.

## Phase 2 readiness

All six skills have spec sheets in this folder:

- `adverse-action-review.md`
- `complaint-theme-analysis.md`
- `fair-lending-test-plan.md`
- `marketing-claim-review.md`
- `section1071-readiness.md`
- `udaap-risk-review.md`

Each spec sheet contains the activation-tuned description (Best for / Not the right tool when / Anchored to), source anchors with section references and `[verify]` markers where applicable, sector and cross-cutting overlay decisions, output-template named sections, structured-output fields, two public-source-derived example scenarios, common pitfalls, and the mandatory guardrail. Phase 2 subagents take the spec sheet as their contract.
