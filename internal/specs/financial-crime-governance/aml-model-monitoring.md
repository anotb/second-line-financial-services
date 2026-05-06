# aml-model-monitoring — Phase 1 spec sheet

Date: 2026-05-06
Plugin: financial-crime-governance
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Reviews ongoing monitoring evidence for an AML transaction-monitoring system as a model under model risk management guidance. Covers data-quality controls, customer segmentation drift, scenario tuning evidence, threshold-change documentation, alert-volume and productivity trends, validation evidence, and below-the-line testing. Produces a second-line monitoring memo with material findings, evidence-needed items, and recommendations. Does not approve scenario changes, adjust thresholds, or sign off on validation conclusions.

Scope boundary: this skill covers AML-specific monitoring governance (segmentation, scenario tuning, alert quality, BTL testing, FFIEC SAR-side downstream effects). General model risk primitives (model definition, model inventory, validation framework, model-card structure, ongoing-monitoring expectations as a category) live in `ai-governance-model-risk`. When an AML monitoring system is being intaked, tiered, or papered as a model card, those skills lead and this one consumes their outputs.

Best for:
- Annual or quarterly second-line monitoring memo on a production AML transaction-monitoring system.
- Pre-validation review of monitoring evidence to scope what the next validation cycle should cover.
- Post-tuning review of a scenario or threshold change and the evidence supporting it.
- Pre-exam readiness review of monitoring documentation for the BSA/AML examination.

Not the right tool when:
- The work is the validation itself (scope: validation-plan in ai-governance-model-risk).
- The work is initial intake or tier classification of the AML system as a model (use ai-use-case-intake and ai-risk-tiering in ai-governance-model-risk).
- The work is QA over individual SAR decisions downstream of the alerts (use sar-decision-qa).
- The work is sanctions screening monitoring (use sanctions-screening-qa; sanctions has its own list-update, match-logic, and FP-rationale pattern).
- The decision is whether to approve a scenario change, threshold change, or validation conclusion. Skill produces review artifacts only; humans decide.

Anchored to: SR 11-7 / OCC 2011-12 (Supervisory Guidance on Model Risk Management, April 4, 2011), with revised interagency guidance OCC Bulletin 2026-13 [verify current section anchors] applying to AML transaction monitoring as a model; FFIEC BSA/AML Examination Manual sections on Suspicious Activity Reporting and on transaction monitoring expectations [verify section anchors]; FinCEN/Federal Banking Agencies Joint Statement on Innovation in BSA/AML Compliance (December 3, 2018); OCC, FRB, FDIC, NCUA Joint Statement on Risk-Focused BSA/AML Supervision (July 22, 2021).

## Source anchors

- SR 11-7 / OCC 2011-12 — Supervisory Guidance on Model Risk Management (April 4, 2011), §III (model development, implementation, and use), §IV (model validation), §V (governance, policies, and controls).
- OCC Bulletin 2026-13 — revised interagency model risk management guidance (2026): https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html [verify section anchors as repo references mature].
- FDIC FIL on revised interagency model risk management guidance, 2026: https://www.fdic.gov/news/financial-institution-letters/2026/agencies-revise-interagency-model-risk-management-guidance [verify section].
- FFIEC BSA/AML Examination Manual — Suspicious Activity Reporting section (covers transaction monitoring expectations): https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04 [verify section anchor for transaction-monitoring system expectations].
- FFIEC BSA/AML Examination Manual — BSA/AML Compliance Program section [verify section anchor for risk-based monitoring expectations].
- FinCEN/Federal Banking Agencies Joint Statement on Innovation in BSA/AML Compliance, December 3, 2018 — supervisory expectations on testing innovative approaches without supervisory criticism for self-identified weaknesses.
- OCC, FRB, FDIC, NCUA Joint Statement on Risk-Focused BSA/AML Supervision, July 22, 2021.
- Public AML transaction-monitoring enforcement actions and consent orders (used as pattern references, not as binding criteria) — anonymized in examples.

## Sector overlays needed

- `references/sector-overlays/banking.md` — bank-specific monitoring expectations (commercial vs. retail vs. private banking segmentation; correspondent-banking nested-activity monitoring; cash-intensive business monitoring).
- `references/sector-overlays/payments-fintech.md` — payments-specific scenarios (P2P fraud-AML overlap, MSB monitoring, third-party payment processor monitoring, sponsor-bank monitoring obligations); high-velocity, low-balance segmentation considerations.
- `references/sector-overlays/capital-markets.md` — broker-dealer and investment-adviser AML monitoring (manipulation-adjacent typologies, microcap concentration scenarios) [verify investment-adviser AML rule effective date]; mutual fund monitoring under 31 CFR 1024 [verify section].
- `references/sector-overlays/insurance.md` — covered-products monitoring (early surrender, large premium, single premium); narrow scope.

## Cross-cutting overlays

None at v1. Cyber typologies (ransomware, account takeover) live in the typology library and the FinCEN advisory references; not pulled out as a separate cross-cutting overlay for this skill.

## Output template named sections (mapped to SR 11-7 monitoring expectations and AML-specific elements)

1. Scope and review window (system, time window, regulator overlay)
2. Model identifier and inventory linkage (links to ai-governance-model-risk artifacts)
3. Data quality posture (completeness, timeliness, integrity controls; data-quality issues outstanding)
4. Customer segmentation
   a. Segmentation methodology and last-refresh date
   b. Segmentation drift evidence (population, behavior)
   c. Segmentation issues outstanding
5. Scenario inventory and tuning evidence
   a. Active scenarios in scope
   b. Tuning cycle, last-tuned date, methodology summary
   c. Below-the-line testing posture
6. Threshold-change governance (changes in window, approvals, post-change effect)
7. Alert volume and productivity trends (volume, productivity, SAR conversion, FP rate where defined)
8. Validation evidence (last validation date, scope, findings outstanding)
9. Issues and material findings (criterion-aligned)
10. Recommended human-review gates (validation triggers, tuning triggers, scope expansion)
11. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `system_id` | string | Canonical AML monitoring system identifier (link to model inventory). |
| `review_window` | object | Sub-fields: start_date, end_date, regulator_overlay (array). |
| `data_quality` | object | Sub-fields: completeness_status, timeliness_status, integrity_controls_documented, open_dq_issues (array). |
| `segmentation` | object | Sub-fields: methodology_summary, last_refresh_date, drift_indicators (array of metric, baseline, current, threshold), open_issues (array). |
| `scenarios` | array of objects | Scenario name, typology, last_tuned_date, btl_testing_posture, productivity_metric, sar_conversion_metric, open_issues. |
| `threshold_changes` | array of objects | Scenario, change_type, change_date, approval_evidence, post_change_effect. |
| `alert_volume_trend` | object | Sub-fields: time_series_summary, productivity_trend, sar_conversion_trend, fp_rate_trend (where defined). |
| `validation_evidence` | object | Sub-fields: last_validation_date, validation_scope, open_findings (array), validator_independence (bool). |
| `material_findings` | array of objects | Finding, criterion (SR 11-7 / OCC 2026-13 section, FFIEC manual section), severity, evidence pointer. |
| `recommended_gates` | array of objects | Gate name, criterion, required reviewer, stop condition. |
| `source_trace` | array of objects | Claim, source, confidence label. |

## Example scenarios (public-source-derived, anonymous)

1. Mid-size US bank, annual second-line monitoring memo on the production AML transaction-monitoring system. Review window: trailing 12 months. System covers retail deposit, commercial deposit, ACH, wire, and check products. Segmentation last refreshed 14 months ago. Active scenarios include structuring, rapid movement of funds, and unusual-pattern scenarios. Public criteria reference: SR 11-7 §III (development), §IV (validation), §V (governance); FFIEC SAR manual transaction-monitoring expectations. Findings: segmentation refresh cadence overdue against firm policy stating 12-month max; below-the-line testing performed for two of seven scenarios in window; alert productivity declining quarter-over-quarter for one scenario without a documented tuning hypothesis; data-quality issue on a deprecated wire-feed identifier outstanding for two cycles. Recommended gates: segmentation refresh prior to next tuning cycle; tuning hypothesis documentation gate before threshold change; data-quality issue closure before validation cycle.

2. Regional bank, post-tuning review of a structuring-scenario threshold change. Reviewer assesses the tuning evidence supporting a threshold tightening from prior baseline. Public criteria reference: SR 11-7 §III, §V; FFIEC SAR manual; FinCEN/agencies 2018 Joint Statement on Innovation. Findings: BTL testing performed at the prior threshold, sample size adequate; productivity uplift hypothesis stated and quantified; reviewer cannot independently reproduce the productivity calculation from the artifacts on file (calculation script not version-controlled); change approval recorded but approver independence from the tuning team not documented. Recommended gates: post-implementation review at 90 days; calculation reproducibility evidence; approver-independence documentation gate added to standard tuning workflow.

## Common pitfalls

1. AML transaction monitoring is treated as "rules", not as a model. Then SR 11-7 / OCC 2026-13 expectations on validation, governance, ongoing monitoring, and effective challenge do not get applied. Mitigation: skill explicitly cites model-risk-guidance criteria and asserts AML monitoring is in scope as a model.
2. Productivity and FP rate are reported without definition. Different denominators give different numbers. Mitigation: structured fields force a defined metric and a definitional pointer.
3. Below-the-line testing reported as "performed" without sample sizes, escalation rate, or sign-off. Mitigation: BTL posture field requires a structured posture entry, not a binary.
4. Segmentation drift assessed only against population (count of customers per segment) and not against behavior (transaction profile per segment). Population stable; behavior moved. Mitigation: drift_indicators field forces both.
5. Threshold-change approvals papered after the fact. Approval evidence pre-dates change date in some files; post-dates in others; signature on a meeting minute serves as approval. Mitigation: change_date and approval_evidence fields force the timeline.
6. Reviewer drifts into recommending a specific threshold or scenario change. Skill produces gates, not changes. Tuning, validation, and approvals are human decisions.
7. Scope creep into validation. The validation cycle is its own deliverable in ai-governance-model-risk. This skill consumes validation evidence; it does not produce it.
