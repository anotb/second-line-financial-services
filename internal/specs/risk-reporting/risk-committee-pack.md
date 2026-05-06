# risk-committee-pack — spec sheet

Plugin: `risk-reporting`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Drafts an enterprise risk committee pack covering heat map, top risks, material risk events, KRI movement and breaches, issues and remediation status, forward-looking commentary, and decision items. Output is a named-section pack a CRO, board secretary, or risk committee chair can take into the meeting after qualified review.

Best for:
- Assembling the standing quarterly or monthly enterprise risk committee pack from upstream KRI feeds, issue logs, loss events, and management commentary.
- Refreshing a board-level risk pack ahead of a regulator-attended meeting (CCAR, SR 12-17 horizontal review, OCC Heightened Standards readiness check).
- Pulling a single committee view across credit, market, operational, compliance, financial-crime, model, third-party, cyber, and (where applicable) climate risk.

Not the right tool when:
- The pack is AI-committee-specific (use `ai-governance-model-risk/skills/board-ai-risk-pack`).
- The work is a single KRI commentary block (use `kri-commentary`).
- The work is an SEC cyber disclosure decision or 8-K Item 1.05 trigger analysis (use `cyber-disclosure-readiness`).
- The work is a management response to an MRA/MRIA or audit finding (use `management-response`).
- The underlying risk data lineage has not been established (the pack assumes BCBS 239 data is fit for purpose; if not, run `bcbs239-gap-assessment` first).

Anchored to: BCBS 239 (January 2013) Principles 7-11 (risk reporting practices); COSO ERM (2017) governance and reporting components; OCC Heightened Standards, 12 CFR Part 30 Appendix D (large-bank risk governance framework) [verify section]; FRB SR 12-17 (Consolidated Supervision Framework for Large Financial Institutions, December 2012); Dodd-Frank Section 165(b) risk committee requirements for very-large bank holding companies [verify current threshold]; SEC Climate Disclosure Rule (final March 2024) [verify current effectiveness — subject to litigation and stay history]; TCFD Recommendations (Final Report, June 2017; Implementing the Recommendations, October 2021) where the firm reports climate risk to the committee.

## Source anchors

Primary:
- BCBS 239 — Basel Committee, Principles for Effective Risk Data Aggregation and Risk Reporting, January 2013. Principles to cite: 7 (accuracy), 8 (comprehensiveness), 9 (clarity and usefulness), 10 (frequency), 11 (distribution). Use for: pack data-quality posture, the section on KRI movement and breaches, and the data-confidence label.
- COSO ERM 2017 — Enterprise Risk Management: Integrating with Strategy and Performance, June 2017. Components to cite: Governance and Culture, Strategy and Objective-Setting, Performance, Review and Revision, Information Communication and Reporting. Use for: pack architecture (top risks, heat map, performance against risk appetite, committee escalation).
- OCC Heightened Standards, 12 CFR Part 30 Appendix D. Sections to cite: II (Risk Governance Framework), III (Risk Appetite Statement), IV (Roles and Responsibilities of the Board) [verify section labels]. Use for: large-bank risk-committee pack expectations on RAS reporting, board challenge, and three-lines roles.
- FRB SR 12-17 — Consolidated Supervision Framework for Large Financial Institutions, December 2012. Use for: enhanced-prudential-supervision context, capital and liquidity governance reporting expectations.
- Dodd-Frank Section 165(b) — risk committee requirements for publicly traded BHCs above the size threshold and nonbank SIFIs. Use for: framing the committee charter scope. [verify current threshold given EGRRCPA 2018 amendments]

Cross-cutting overlays (climate is required for this skill):
- SEC Climate Disclosure Rule (Release Nos. 33-11275, 34-99678; final March 2024). [verify current effectiveness — the rule has been subject to legal challenges and stay actions; phase 2 must check current SEC posture before SKILL.md ships.] Sections to cite: Item 1500-1507 of Regulation S-K (climate-related disclosures, governance, risk management, targets and goals); Article 14 of Regulation S-X (financial-statement effects). Use for: the climate section of the committee pack, where applicable.
- TCFD Recommendations — Final Report, June 2017; Implementing the Recommendations, October 2021. Pillars: Governance, Strategy, Risk Management, Metrics and Targets. Use for: voluntary or international-firm climate reporting where SEC rule does not directly apply.
- FSB SCEAS / NGFS climate scenarios — short-term and long-term reference scenarios used by US and EU supervisors for climate scenario analysis reporting to the board. Use for: scenario commentary within the pack.

Secondary (overlay only):
- FRB SR 95-51 (rating risk management at state member banks) [verify current applicability] — historical anchor for the four-element risk management framework.
- BCBS 239 Principles 1-6 (overarching governance and data aggregation) — referenced indirectly; deep treatment lives in `bcbs239-gap-assessment`.

## Sector overlays needed

- `banking.md` — Covers OCC Heightened Standards 12 CFR Part 30 Appendix D large-bank framework, FRB enhanced prudential standards under DFA 165, FFIEC IT-risk reporting expectations, and CRA / fair-lending reporting at the committee level when the BHC has consumer banking subsidiaries.
- `insurance.md` — Covers ORSA Summary Report (NAIC Model #505) [verify section] expectations for the enterprise risk view, NAIC Corporate Governance Annual Disclosure (Model #305) [verify], and state DOI risk-management reporting expectations.
- `capital-markets.md` — Covers SEC Rule 17h-1T / 17h-2T risk-assessment recordkeeping for broker-dealers [verify], FINRA 3120/3130 supervisory and CEO certification reporting, and CFTC risk-committee reporting expectations for FCMs and SDs.
- `payments-fintech.md` — Covers OCC fintech bank-partnership risk-reporting expectations (third-party concentration, BaaS risk roll-up) [verify] and CFPB supervisory reporting touchpoints for large nonbank money transmitters.

## Cross-cutting overlays needed

- `climate.md` — Required. The committee pack carries enterprise climate risk reporting where the firm is in scope of the SEC climate rule (large accelerated filers and accelerated filers, with phased-in compliance) [verify current effectiveness], EU CSRD as a non-US group company, or voluntary TCFD-aligned disclosure. Anchors: SEC Climate Disclosure Rule [verify current status], TCFD 2017 + 2021, FSB SCEAS, NGFS scenarios. The overlay covers heat-map placement of physical and transition risk, scenario analysis commentary, and the link between the committee pack and the 10-K climate disclosure.
- `cyber.md` — Optional. Cyber risk almost always appears in the committee pack but the depth lives in `cyber-disclosure-readiness`. Pull a brief from there into the committee section rather than re-anchoring full cyber sources. Anchors when included: NYDFS Part 500 §500.4(b) board reporting; SEC Reg S-K Item 106 governance disclosure.
- `privacy.md` — Not required at v1.
- `conduct.md` — Not required at v1; conduct findings appear via `management-response` and roll up into the issues section of the pack.

## Output template named sections

Top of artifact:
- Cover page: meeting date, committee name (e.g., Risk Committee of the Board, Enterprise Risk Committee), period covered, classification, document version
- Decision items requested (single page, named decisions, owners, recommended actions)
- Executive summary (5-7 bullets, CRO voice)

Body:
- Heat map by risk type (credit, market, liquidity, operational, compliance, financial crime, model, third-party, cyber, climate where applicable, strategic, reputational; current period rating, prior period rating, direction)
- Top risks (named risks driving each heat-map cell, with quantified exposure where available, key drivers, and ownership)
- Material risk events in the period (loss events above threshold, near-misses, control failures, regulatory actions, with date, root cause, impact, status)
- KRI movement and breaches (table of KRIs with thresholds, current value, prior value, RAG status, breach commentary; pulls from `kri-commentary`)
- Risk appetite status (RAS metrics, current value vs limit/trigger/tolerance, breaches, recalibration requests)
- Issues and remediation status (open MRAs, MRIAs, audit issues, regulatory exam findings, internal issues over threshold; ageing, owner, due date, slippage)
- Forward-looking commentary (emerging risks, regulatory horizon, scenario stress results, climate scenario commentary where applicable)
- Decision items (full detail of each decision requested, with options, recommended option, dissents, and required vote)

Tail:
- Appendix: data confidence and BCBS 239 posture (data lineage notes, known limitations, restatements)
- Appendix: source trace per material claim
- Appendix: glossary of risk taxonomy terms
- Sign-off block (CRO, committee chair, date, reviewer questions)

## Structured output fields

Schema: `schemas/risk-report.schema.json` (existing; extend in phase 2) plus a pack-level wrapper schema to be added.

Pack wrapper object:
- `pack_id`: string. Stable ID for this pack instance.
- `committee_name`: string. E.g., "Risk Committee of the Board".
- `meeting_date`: string. ISO date.
- `period_covered`: object. `start` (ISO date), `end` (ISO date).
- `classification`: enum. `internal`, `board-confidential`, `regulator-shareable`.
- `cro_summary_bullets`: array of strings. Maximum 7.
- `heat_map`: array of objects with `risk_type` (enum: credit / market / liquidity / operational / compliance / financial-crime / model / third-party / cyber / climate / strategic / reputational), `current_rating` (enum: low / moderate / elevated / high), `prior_rating` (same enum), `direction` (enum: improving / stable / deteriorating), `commentary` (string).
- `top_risks`: array of objects with `risk_id`, `risk_name`, `risk_type` (enum from heat_map), `exposure_quantified` (string or null), `key_drivers` (array of strings), `owner` (role, not person).
- `material_events`: array of objects with `event_id`, `event_date` (ISO date), `event_type` (enum: loss-event / near-miss / control-failure / regulatory-action / external-event), `description`, `gross_impact` (string or null), `net_impact` (string or null), `status` (enum: open / under-investigation / remediated / closed), `linked_issue_ids` (array).
- `kris`: array of `risk-report.schema.json` objects (extended with `risk_type` and `breach_age_days` fields in phase 2).
- `ras_status`: array of objects with `ras_metric`, `limit`, `trigger`, `tolerance`, `current_value`, `breach_status` (enum: within / at-trigger / breach), `commentary`.
- `issues_summary`: object with counts and ageing buckets for `mra` (Matter Requiring Attention), `mria` (Matter Requiring Immediate Attention), `audit`, `regulatory_exam`, `internal_high_severity`. Each bucket has `open_count`, `over_age_count`, `aged_over_days_threshold`.
- `forward_looking`: object with `emerging_risks` (array of strings), `regulatory_horizon` (array of strings), `scenario_results` (array of objects with `scenario_name`, `result_summary`, `breach_flag`).
- `climate_section`: object (optional, present when in scope). `governance_summary`, `physical_risk_summary`, `transition_risk_summary`, `scenarios_used` (array of strings; e.g., NGFS Net Zero 2050, NGFS Delayed Transition), `linked_10k_disclosure_section` (string or null).
- `decision_items`: array of objects with `decision_id`, `decision_requested`, `options` (array), `recommended_option`, `requested_vote_or_acknowledgement` (enum), `owner`.
- `data_confidence_label`: enum. `high` / `medium` / `low` / `unknown`.
- `bcbs239_known_limitations`: array of strings.
- `human_review_required`: boolean. Always true for v1.

Phase 2 should add to `risk-report.schema.json`:
- `risk_type` (enum, same values as heat_map.risk_type).
- `breach_age_days` (integer or null).
- `bcbs239_principle_refs` (array of strings).

## Example scenarios

### Scenario 1: Quarterly Risk Committee pack for a Category III BHC

Input: a Category III bank holding company under the FRB tailoring framework is preparing the Q2 risk committee pack. CRO has flagged operational risk and third-party concentration as deteriorating, model risk as stable but with two open MRAs from the most recent OCC continuous-monitoring letter, and climate as in-scope under TCFD-aligned voluntary disclosure (parent group reports under EU CSRD). Source posture: public-only anchors (BCBS 239, OCC Heightened Standards, TCFD) plus the firm's RAS and risk taxonomy.

Output emphasizes:
- Heat map shows operational and third-party at "elevated, deteriorating" with quantified loss-event count year-to-date; model at "moderate, stable" with the two MRAs flagged as decision items requesting an extended remediation date.
- KRI movement section pulls 14 KRIs from the upstream feed, with three RED breaches and one trigger-level alert. Each red KRI has a paragraph of commentary citing root cause, owner, and remediation status; commentary is generated by the `kri-commentary` skill and consumed here.
- Material risk events lists a single Tier 1 loss event (vendor outage in payments processing, 12-hour duration, customer-facing) with linked issue ID and current remediation status.
- Climate section is present but lean: TCFD-aligned governance and risk management subsections, NGFS Net Zero 2050 and Delayed Transition scenarios used, and a pointer to the parent group's CSRD-aligned 10-K equivalent disclosure section. Source-trace appendix flags that SEC climate disclosure rule current effectiveness is unresolved [verify] and the firm's posture is to continue voluntary TCFD reporting until SEC posture clarifies.
- Decision items: one extension request for the two model-risk MRAs, one approval request for a revised RAS metric on third-party concentration.
- Data confidence label: medium. Three of the 14 KRIs have known data-lineage gaps documented in the latest BCBS 239 self-assessment.
- Human review required: yes; the pack is a draft for the CRO and the Head of Risk Reporting before it goes to the committee secretary.

### Scenario 2: Annual board-pack refresh ahead of an OCC Heightened Standards horizontal review

Input: a covered bank under 12 CFR Part 30 Appendix D is preparing the annual committee pack ahead of a horizontal supervisory review. The pack must clearly demonstrate three-lines roles, board challenge of management's risk view, and the connection between the RAS and operating limits. Source posture: public-only anchors (12 CFR Part 30 Appendix D, OCC Comptroller's Handbook on Corporate and Risk Governance), plus the firm's risk-governance framework and RAS.

Output emphasizes:
- Cover page and executive summary cite the relevant heightened standards sections (II and III) [verify section labels] explicitly to demonstrate alignment.
- Heat map by risk type uses the firm's eight-category taxonomy mapped to the heightened-standards expected categories. Climate is included as a supporting risk under strategic, not as a standalone heat-map cell, with rationale documented.
- Risk appetite status section is the centrepiece. Each of 22 RAS metrics is reported with limit, trigger, tolerance, current value, and a column showing how the metric ladders to operating limits below.
- Forward-looking commentary covers the three regulatory items most likely to come up in the OCC review: the SEC climate disclosure rule status [verify], the BCBS 239 self-assessment refresh, and the FRB stress-test results.
- Source-trace appendix is exhaustive — every material claim links to the source system, the upstream KRI report, or the regulatory anchor.
- Data confidence label: high on credit, market, liquidity (data warehouse is examined annually); medium on operational and third-party (vendor data quality has known gaps); low on climate (scenario data is third-party-supplied with limited internal validation).
- Human review required: yes; the pack is a draft for the CRO, General Counsel, and Head of Regulatory Affairs before committee distribution.

## Common pitfalls

1. Treating the pack as a status report rather than a governance instrument. The pack exists to drive committee decisions. The "Decision items requested" section must be the first body section a committee member reads, and every decision must have named options, a recommendation, and a requested vote or acknowledgement. A pack with no decision items is a status update; the committee charter usually calls for both, but the decision section is the load-bearing one.
2. Heat map without movement. A static heat map is useless. Every cell must show prior-period rating and direction, and any deteriorating cell must be addressed in the top-risks section.
3. Climate as bolt-on. Where climate is in scope, it is part of the enterprise heat map (or, if not separately rated, explicitly mapped under strategic risk with documented rationale). Phase 2 must not allow a separate "Climate appendix" floating outside the risk taxonomy.
4. SEC climate rule overreach. Phase 2 SKILL.md and the climate cross-cutting overlay must explicitly flag that the SEC climate rule has been subject to legal challenges and stay actions; never assert current effectiveness without checking SEC's posture as of the report date. Default posture for the spec sheet: cite the rule with a [verify current effectiveness] flag and lean on TCFD for substantive content.
5. RAS metrics without linkage to operating limits. The committee owns the RAS. The pack must show how each RAS metric ladders down to first-line operating limits, otherwise the heightened-standards expectation that the board frame and oversee the RAS is not demonstrably met.
6. Issues section as a counter, not a manager. An open-issues section that just shows counts and ageing is insufficient under SR 12-17 and Heightened Standards. Each MRA / MRIA over a threshold age must have a named owner, a forward action, and a slippage commentary.
7. Confidence label gaming. The data confidence label is BCBS 239-anchored. If three KRIs have lineage gaps, the label is medium at best; phase 2 should reject "high" confidence labels when known limitations are non-empty.
8. Generic forward-looking commentary. "Emerging risks include cyber, AI, and climate" is filler. Phase 2 must require named, dated, regulator-anchored items (e.g., "FRB stress test 2026 hypothetical scenario published February 2026"; "expected NYDFS Part 500 amendment effective Q3 2026").
