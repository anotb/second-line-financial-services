# sar-decision-qa — Phase 1 spec sheet

Date: 2026-05-06
Plugin: financial-crime-governance
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Reviews a SAR / no-SAR decision file for completeness, defensibility, and alignment with the institution's SAR program and the FFIEC SAR manual expectations. Reviews the alert chronology, investigation steps performed, evidence considered, decision rationale, continuing-activity posture, and confidentiality controls. Produces a QA memo with material gaps, reviewer findings, and recommendations. Does not file, decline to file, amend, or close any SAR.

Best for:
- Second-line QA over a sample of closed alerts (filed and unfiled) within a defined lookback window.
- Targeted review of high-risk alert types (structuring, trade-based, layering, sanctions-adjacent, fraud-typology).
- Review of continuing-activity SAR cadence and 90-day continuing-review documentation.
- Pre-exam readiness review of SAR decision documentation against the FFIEC SAR section.

Not the right tool when:
- The work is alert-generation governance (transaction-monitoring scenario tuning, segmentation, threshold changes); use aml-model-monitoring.
- The work is the underlying CDD or EDD posture of the customer rather than the alert decision itself; use cdd-risk-review or edd-escalation-pack.
- The work is a single adverse media triage rather than a SAR decision; use negative-news-triage.
- The decision is whether to file, amend, or supplement the SAR. Skill produces QA artifacts only; humans decide.

Anchored to: FFIEC BSA/AML Examination Manual, Suspicious Activity Reporting section (current online manual): https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04 [verify section anchor]; 31 CFR 1020.320 (banks) and 31 CFR 1023.320 (broker-dealers) and parallel institution-specific SAR rules [verify section]; 31 USC 5318(g) statutory SAR authority and confidentiality rules; FinCEN SAR Filing Instructions (current FinCEN form and instructions, dated as-of); FinCEN advisories applicable to the typology under review (e.g., real estate, elder financial exploitation, ransomware) [verify advisory dates].

## Source anchors

- FFIEC BSA/AML Examination Manual — Suspicious Activity Reporting section: https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04 [verify section anchor]
- 31 CFR 1020.320 — Reports by banks of suspicious transactions [verify section].
- 31 CFR 1023.320 — Reports by brokers or dealers in securities of suspicious transactions [verify section].
- 31 CFR 1024.320, 1025.320, 1026.320, 1029.320, 1030.320 — parallel SAR rules for mutual funds, insurance companies, futures commission merchants, loan/finance companies, and housing GSEs [verify section as applicable].
- 31 USC 5318(g) — statutory SAR authority and confidentiality (no notification of subject permitted, with limited exceptions).
- FinCEN SAR Filing Instructions and current SAR form (BSA E-Filing) [verify current form version date].
- FinCEN advisories relevant to the typology: e.g., FIN-2014-A005 (real estate, since updated) [verify], FIN-2022-A001 (elder financial exploitation) [verify date], ransomware advisories [verify dates].
- OCC, FRB, FDIC, NCUA Joint Statement on Risk-Focused BSA/AML Supervision, July 22, 2021.
- FinCEN/Federal Banking Agencies Joint Statement on Innovation in BSA/AML Compliance, December 3, 2018.

## Sector overlays needed

- `references/sector-overlays/banking.md` — 31 CFR 1020.320 specifics; 30/60-day filing windows under SAR rules; continuing-activity 90-day reviews; common bank typologies (structuring, check kiting, ACH origination fraud, BIN attacks, elder exploitation).
- `references/sector-overlays/payments-fintech.md` — sponsor-bank SAR responsibility delineation; MSB SAR rules under 31 CFR 1022.320 [verify]; fintech-specific typologies (money muling, synthetic identity, P2P fraud).
- `references/sector-overlays/capital-markets.md` — 31 CFR 1023.320 (broker-dealers) and parallel rules for mutual funds and FCMs; market-manipulation, microcap, and prearranged-trading typologies.
- `references/sector-overlays/insurance.md` — 31 CFR 1025.320 [verify]; covered products only; early-surrender and unusual-funding typologies.

## Cross-cutting overlays

None at v1. Conduct overlap is real (insider-conduct typologies) but is more cleanly handled inside the typology library; cyber overlap (ransomware advisories, account-takeover) is captured in the typology references rather than as a cross-cutting overlay.

## Output template named sections

1. Alert summary (alert ID, scenario, generation date, alert type, monetary footprint)
2. Customer and account context (CDD posture, prior SAR history at customer level, related parties)
3. Investigation steps performed (with evidence pointers and dates)
4. Evidence considered (system-of-record extracts, public information, internal escalations)
5. Disposition (filed / not filed / closed with continuing review)
6. Decision rationale (typology citation, FinCEN advisory link if applicable, narrative coherence)
7. Confidentiality posture (notification controls, internal access controls, tipping-off considerations)
8. Continuing activity posture (90-day review cadence, prior SAR linkage)
9. QA reviewer findings (criteria-aligned)
10. Material gaps and evidence-needed items
11. Recommendation (no further action, re-open, escalate to SAR review committee, training feedback)
12. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `alert_id` | string | Canonical alert identifier (placeholder for sample). |
| `alert_type` | enum | `transaction_monitoring`, `referral_internal`, `referral_external`, `manual_detection`, `negative_news`, `sanctions_adjacent`, `other`. |
| `scenario_name` | string | Monitoring scenario or rule that generated the alert (null if non-system). |
| `monetary_footprint` | object | Sub-fields: aggregate_amount, currency, time_window, transaction_count. |
| `customer_id` | string | Customer identifier (placeholder). |
| `prior_sar_history` | array of objects | Prior SAR filings at customer / related-party level (count, dates, typologies; placeholder where unknown). |
| `investigation_steps` | array of objects | Step description, date, performer role, evidence pointer. |
| `disposition` | enum | `filed`, `not_filed_closed`, `closed_with_continuing_review`, `escalated_pending`. |
| `decision_rationale` | object | Sub-fields: typology, advisory_reference, narrative_summary, narrative_coherence_label. |
| `confidentiality_posture` | object | Sub-fields: tipping_off_risk_assessed (bool), internal_access_controls_documented (bool), notification_avoidance_controls (text). |
| `continuing_activity` | object | Sub-fields: prior_sar_link, last_continuing_review_date, next_review_due. |
| `qa_findings` | array of objects | Finding description, criterion violated, severity, evidence pointer. |
| `material_gaps` | array of strings | Each tagged with criterion. |
| `recommendation` | enum | `no_further_action`, `re_open_investigation`, `escalate_to_sar_review_committee`, `training_feedback`, `process_change_recommendation`. |
| `source_trace` | array of objects | Claim, source, confidence label. |

## Example scenarios (public-source-derived, anonymous)

1. Community bank, structuring typology. Alert generated by a structuring-detection scenario after a small-business customer makes nine cash deposits each just under the $10,000 CTR threshold within a rolling 14-day window across two branches. FFIEC SAR manual scenario reference: structuring is a long-standing typology; FinCEN guidance on structuring is well-documented. Investigation file shows: customer interviewed, no satisfactory explanation, deposits inconsistent with documented expected activity. Disposition: SAR filed. QA review focus: narrative coherence, citation to typology, completeness of structured fields on the SAR form, customer-related-party search completeness, evidence chain. QA finding: investigator did not document a search for related-party accounts at the institution; structured field for "structuring" present but the narrative is generic. Recommendation: training feedback to investigator group on related-party search documentation; no SAR amendment recommended (reviewer flags as a discussion item for the SAR review committee, not a directive).

2. Mid-size bank, account-takeover-adjacent typology drawing on a FinCEN ransomware advisory pattern. Alert generated by an unusual-pattern scenario on a commercial customer's outbound wires to a high-risk jurisdiction following a customer report of a suspected business-email-compromise event. Investigation file: customer's IT firm provided forensic summary; bank fraud unit recovered partial funds; outbound counterparty showed indicators consistent with public ransomware-advisory typology (FinCEN ransomware advisories) [verify advisory dates]. Disposition: SAR filed with cyber-related fields and 30-day filing window met. QA review focus: completeness of cyber-event indicators in structured SAR fields; alignment with applicable FinCEN cyber/ransomware advisory; tipping-off controls during the customer's recovery process; continuing-review setup. QA findings: cyber-event structured fields complete; advisory citation in narrative is generic; tipping-off controls during recovery were assessed informally and not documented. Recommendation: process-change recommendation on documentation of tipping-off assessments during fraud-recovery interactions.

## Common pitfalls

1. Disposition rationale narrates the decision in plain language but does not cite a typology or applicable FinCEN advisory. QA must distinguish narrative coherence from criteria-citation.
2. Continuing-activity 90-day reviews documented only when a follow-on SAR is filed. Reviews that conclude "no continuing activity" are not papered, leaving an evidence gap. Mitigation: QA tracks 90-day review cadence regardless of outcome.
3. Investigation steps recorded as a free-text paragraph with no dates, no performer roles, and no evidence pointers. Cannot be QA'd against the timeline. Mitigation: structured investigation_steps field forces dated, attributed entries.
4. Tipping-off / confidentiality assessment is treated as a tickbox at the program level rather than considered for each decision (especially fraud-recovery, EDD-overlap, and law-enforcement-liaison cases).
5. QA conflates the alert quality (which belongs to aml-model-monitoring) with the decision quality (which belongs here). Mitigation: scoping section explicitly states which questions are out of scope.
6. Reviewer drifts toward instructing a SAR amendment or filing. Skill produces QA findings and recommendations; SAR review committee or BSA officer files, amends, or declines.
7. "No further action" recommendation issued without reference to whether the customer is on an EDD or refresh trajectory. Mitigation: cross-reference to cdd-risk-review and edd-escalation-pack outputs where available.
