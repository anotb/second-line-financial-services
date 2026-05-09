---
name: life-health-pricing-governance
description: |
  Drafts a second-line pricing-governance review of a US life or health rating change (new rate filing, refile, accelerated-underwriting model, rating-plan refresh, ML-driven rating factor, post-issue underwriting model) for a state DOI rate analyst's audience. The artifact carries a rate-filing summary, a rating-factor map, an unfair-discrimination analysis under NAIC Model #880, disparate-impact red flags under state DOI bulletins, AIS Program coverage against the NAIC AI Bulletin (December 2023), and documentation completeness against SR 11-7-equivalent expectations. The deliverable shape is a Word memo plus an Excel rating-factor map; SERFF-track and AU-track engagements use the same spine.

  Best for:
  - A life or health insurer is preparing or refreshing a rate filing and second-line wants the pricing-governance file before SERFF submission.
  - An accelerated-underwriting model or ML-driven rating factor has gone through development and second-line needs the unfair-discrimination and disparate-impact review before deployment.
  - A state DOI inquiry on rating factors, AI use, or unfair discrimination has arrived and the carrier is preparing the response file.
  - An internal audit or ORSA review is sampling pricing governance for life or health.

  Not the right tool when:
  - The product is P&C (different rate-regulation model and different unfair-discrimination posture; out of scope).
  - The exposure is fair-lending under ECOA / Reg B for a credit-insurance product underwritten via a bank channel (use `consumer-compliance-fair-lending/fair-lending-test-plan` with the insurance overlay).
  - The use case is claims AI rather than pricing or underwriting (use `ai-governance-model-risk/agentic-ai-controls` with the insurance overlay).
  - The work is reserving, IBNR, or solvency capital rather than pricing.
argument-hint: "[product type, states, change type, AU / ML components, source posture]"
---

# Life and health pricing governance

The artifact is the second-line pricing-governance file a state DOI rate analyst, an internal audit reviewer, or an ORSA examiner expects on a life or health rating change. It is not the actuarial memorandum (the actuarial work justifies the rate; this work justifies the governance over the actuaries and the model). It is not a model-validation report (validation is one input, not the deliverable). It is not an ECOA / Reg B fair-lending test plan (the statutory frame here is NAIC Model #880 unfair-discrimination plus state insurance code, not ECOA; the test, the permitted-vs-prohibited factor list, and the protected classes differ).

The shape is structured: rate-filing summary, rating-factor map, unfair-discrimination analysis applied factor-by-factor and to the rating plan as a whole, disparate-impact red flags under state DOI guidance (Colorado SB 21-169 implementing regulation, NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting January 2024, California DOI bulletin on AI use), AIS Program element-by-element coverage against the NAIC AI Bulletin December 2023, documentation-completeness against SR 11-7-equivalent expectations (state DOIs cite SR 11-7 / OCC 2026-13 as analogous model-risk expectation language for ML pricing models), state-DOI-bulletin alignment per state in the filing footprint, and a privacy and consumer-disclosure posture covering HIPAA where PHI is in scope and ECDIS consumer-recourse where ECDIS is in scope. ACA-pricing checks bolt on for individual or small-group health. Illustration checks under NAIC Model #582 bolt on where the change touches illustrated values. The artifact is a draft; the named approver — chief pricing actuary, chief risk officer, head of compliance, or the rate-filing committee — decides.

## Ask first

Settle these before drafting. Default and flag where the engagement does not yet have an answer.

- **What is the product type and which states are in scope.** Life, individual health, small-group health, large-group health, annuity, disability, LTC. The product drives which statutory frame applies (ACA pricing rules for individual / small-group health; #582 illustrations for life; #275 suitability for annuity transactions; HIPAA where the underwriting touches PHI). The state list drives the bulletin set: Colorado Regulation 10-1-1 (amended October 15, 2025) where Colorado is in scope; NY DFS Insurance Circular Letter No. 7 (2024) where New York is in scope; California DOI bulletin where California is in scope; the NAIC AI Working Group adoption tracker for the rest.
- **What is the change type.** New filing, refile, rate-level change, factor change, model change, accelerated-underwriting launch, AU change. Change type drives review depth and which sections of the artifact carry weight; an AU launch with ECDIS in the input set lights up CO and NY as load-bearing rows even if the rate level is unchanged.
- **What rating factors are in play and which are derived from ECDIS.** Each factor needs its statutory-permission status state-by-state and its interaction with prohibited bases under the relevant state insurance code; ECDIS-derived factors carry an additional provenance and consumer-recourse layer per CO regulation and NY DFS Circular Letter.
- **What AI / ML components are in the pricing or underwriting chain and who supplies them.** Vendor-supplied AI pulls third-party-AI-accountability obligations under the NAIC Bulletin December 2023; vendor self-attestations are not evidence.
- **What is the source posture.** Public-only, public-plus-firm-policy, public-plus-firm-policy-plus-evidence, connector-aware (rate-filing system, model inventory, vendor inventory, monitoring dashboards). Posture sets the evidence ask. Aspirational posture is not a posture.

When `scope` is supplied, consume it (`institution.type`, `institution.primary_regulators`, `sector_overlay_set`, `cross_cutting_overlay_set`, `persona.role`, `source_posture`); the sector overlay is always insurance for this skill. When it is not supplied, ask the questions and default to public posture if the practitioner declines. Note the absence in the artifact.

## How the file gets built

The body has the same spine across product types; sections light up or stay quiet based on scope.

The **rate-filing summary** is one page. Product, state(s), filing channel (SERFF tracking number where issued), effective date, rationale for change, prior approval status, named-role owners. The summary is the orientation any DOI rate analyst reads first; the rest of the file answers the questions the summary raises.

The **rating-factor map** is the centre of gravity, and the deliverable is a separate Excel workbook (one row per factor, columns for the statutory dimensions). Each row carries: factor name, source data, ECDIS flag (yes / no / vendor-derived), statutory-permission status by state in scope (permitted / prohibited / silent / requires-justification), interaction-with-prohibited-bases note (state insurance code lists protected classes; the test is per state, not federal), actuarial-justification reference (memorandum section), monitoring metric, and owner role. The map is the artifact a DOI rate analyst will read line-by-line; build it as the workbook, not as a markdown table buried in the memo.

The **unfair-discrimination analysis** under NAIC Model #880 applies the standard to each rating factor and to the rating plan as a whole. The Model #880 test is not ECOA disparate-treatment: actuarial justification matters, the permitted-vs-prohibited rating-factor list is state-defined, and the protected classes are defined by state insurance code. Carry the test explicitly. Where a factor is prohibited in one state and silent in another in the filing footprint, the artifact names the state-by-state divergence rather than collapsing to a federal answer.

The **disparate-impact red flags** section runs where state DOI guidance imports a disparate-impact-style monitoring expectation on top of #880. Colorado Regulation 10-1-1 (amended October 15, 2025) imposes a governance and risk-management duty on ECDIS and predictive models in life-insurance underwriting; verify the current scope on the analysis date. NY DFS Insurance Circular Letter No. 7 (2024) sets disclosure and consumer-recourse expectations for AI and ECDIS in life-insurance underwriting and pricing. California DOI bulletin on AI use imposes broader expectations across product lines. Where a factor is ECDIS-derived, run the proxy-variable risk check; where the model is ML-driven, run the monitoring-metric check; where consumer recourse is required, name the channel and the SLA.

The **AI / ML rating factor and accelerated-underwriting governance** section is the AIS Program cross-walk against the NAIC AI Bulletin December 2023. AIS Program elements: governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness. Each element gets a status row (in-place, partial, gap, not-applicable) with evidence pointer. Vendor-AI is not exempt; the carrier remains accountable. Where the carrier has not adopted an AIS Program at all, the artifact says so and points the gap at the regulatory-affairs lead, not the model-risk function.

The **documentation-completeness vs SR 11-7-equivalent expectations** section maps the model documentation, validation evidence, performance-monitoring plan, change-management process, and ongoing-monitoring metrics against the SR 11-7 / OCC 2026-13 model-risk expectation language. State DOIs cite this language as analogous, not directly applicable; the artifact treats it as a defensible benchmark and names the citation as analogous rather than binding. Carry the `[verify final OCC 2026-13 issuance date and bulletin number]` marker until the citation is confirmed.

The **state DOI bulletin alignment** section runs per state in the filing footprint. NAIC Model Bulletin adoption status; CO Regulation 10-1-1 (amended October 15, 2025) if Colorado is in scope; NY DFS Insurance Circular Letter No. 7 (2024) if NY is in scope; CA bulletin if CA is in scope; standard state DOI rate-filing checklist points (file completeness, actuarial certification, prior-approval status, market-conduct posture). Use the NAIC AI Working Group adoption tracker for current state-by-state status; do not freeze a state list in the artifact.

The **privacy and consumer-disclosure posture** section pulls HIPAA where PHI is in scope and the ECDIS consumer-recourse and adverse-information disclosure expectations from CO regulation and NY DFS Circular Letter. The conduct overlay layers fair-treatment language for the AU decline / referral flow. The privacy overlay carries the substantive PHI and ECDIS analysis.

**ACA-pricing checks** run where individual or small-group health is in scope. Community rating, age-band limits (3:1 for adults under federal default; tighter in some states), tobacco surcharge limits (1.5:1), geographic-rating-area compliance under 45 CFR §147.102. These are bright-line rules.

**Illustration checks** under NAIC Model #582 run where the change touches illustrated values for life products. Self-support and lapse-support tests; illustrated-vs-non-illustrated-vs-actual tracking; the actuarial certification chain.

The artifact closes with **gaps**, **open items and owners**, **recommended disposition** (`approve`, `approve-with-conditions`, `remediate-then-re-review`, `decline-and-rework`), and **source citations with date**.

## Quality bar

Every material claim cites a source from `references/source-anchors.md` (or a loaded overlay) by file path; unsupported claims are marked `[evidence needed]`. The unfair-discrimination test is Model #880 plus state insurance code, not ECOA / Reg B. The rating-factor map is a separate Excel workbook with state-by-state statutory-permission columns, not a single markdown table. ECDIS provenance is named for every factor that touches third-party consumer data. AIS Program element-by-element coverage runs against the NAIC AI Bulletin December 2023. SR 11-7-equivalent language is cited as analogous, not binding (OCC 2026-13 covers traditional models in the federal banking frame and excludes GenAI and agentic AI from scope; carry the same analogous-only posture for state DOIs). State-by-state divergence is named rather than collapsed to a federal answer. HIPAA layer applies wherever the underwriting or pricing touches PHI. ACA-pricing bright-line rules apply for individual / small-group health. Named institutions appear in narrative only when they are public defendants in a finalised state-DOI consent order or rate-filing rejection. The artifact is a draft and the named approver decides.

## Adaptation

File depth scales to the change type and the audience. A SERFF rate-level refile reads tighter than an AU launch with ECDIS in the input set. A board-risk-committee read-out collapses the rating-factor map to a heat-map appendix. A state-DOI-inquiry response file leads with the bulletin-alignment row for the inquiring state. An ORSA-driven internal review pulls the AIS Program section to the front. The Excel rating-factor map is required for any change touching a rating factor; it can be a single-row delta workbook for a factor change or a full grid for a refile.

## Sector and cross-cutting overlays

This skill is insurance-only. The sector overlay (`references/sector-overlays/insurance.md`) is required-on for every engagement run through this skill — it is the workflow itself, not extra flavour. Cross-cutting overlays load when the engagement implicates them.

- `cross-cutting/privacy.md` — required. HIPAA Privacy Rule (45 CFR Part 164 Subpart E) where pricing or underwriting touches PHI; state insurance-information-and-privacy frameworks; ECDIS consumer-disclosure and recourse expectations under NY DFS Circular Letter and Colorado regulation.
- `cross-cutting/conduct.md` — recommended. Consumer-fair-treatment lens on rating factors, the AU decline / referral flow, and life-and-health sales-practice expectations.
- Cyber overlay does not load at the pricing layer; cyber sits on `insurance-outsourcing-review` and on the AI-vendor diligence review.

## Pointers

- `references/source-anchors.md` — citations for the named anchors (Model #880, NAIC AI Bulletin December 2023, NY DFS Circular Letter January 2024, Colorado SB 21-169 implementing regulation, ACA pricing rules at 45 CFR Part 147, Model #582 illustrations, Model #275 suitability in annuity transactions, HIPAA Privacy Rule, Model #505 ORSA, SR 11-7 / OCC 2026-13 as analogous model-risk language, Solvency II as see-also for EU overlay).
- `references/sector-overlays/insurance.md` — the workflow itself: rating-factor permission posture, AU-and-ML governance under the NAIC AI Bulletin, the AIS Program cross-walk, the ECDIS provenance check, state-by-state bulletin variation.
- `references/cross-cutting/privacy.md`, `conduct.md` — cross-cutting flavour.
- `templates/default-output.md` — Word-memo content spec (named sections).
- `examples/` — public-source-derived: a life carrier launching AU with ECDIS in CO and NY; a small-group health refile with a vendor ML risk-adjustment input.
- `TROUBLESHOOTING.md` — recurring pitfalls (treating Model #880 as ECOA; letting the actuarial memo stand in for governance; skipping ECDIS provenance; missing ACA bright-lines on individual / small-group health; collapsing illustrations into rate filing).

The plugin-level shared references (`references/source-map.md`, `references/policy-control-library.md`, `references/public-regulatory-scenarios.md`) sit at the plugin root.

## Output

Default to drafting against `templates/default-output.md`. Render as Word, Excel, PowerPoint, or Markdown when the audience or workflow asks for it; the typical pair is a Word memo via the `docx` skill plus the rating-factor map as an Excel workbook via the `xlsx` skill (both in the `document-skills` plugin). The memo carries the narrative and analysis; the workbook carries the line-by-line factor map a DOI rate analyst will read.

Downstream consumers: `insurance-outsourcing-review` reads the vendor-AI accountability findings for any vendor in the pricing chain; `ai-governance-model-risk/ai-act-triage` (with the insurance overlay) reads the AU / ML triage lens; `risk-reporting/risk-committee-pack` (with the insurance overlay) reads the AIS Program status and the disposition row for the ORSA Summary Report build-out. The named approver — chief pricing actuary, CRO, head of compliance, or the rate-filing committee — decides; the file is a draft until that step.
