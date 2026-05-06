# Example: HMDA LAR data-integrity workpaper for the annual compliance-testing cycle

Public-source-derived. No named institution. The shape mirrors a common annual HMDA data-integrity test at a HMDA-reportable bank.

## Input

- **Test cycle**: annual HMDA LAR data-integrity test, drafting the testing workpaper from completed fieldwork.
- **Test plan reference**: pre-fieldwork test plan (test ID `TP-CMP-HMDA-2026-01`) identifies the population (LAR records for the calendar year), the sample size (60 records, stratified by action-taken type), and the procedures (re-perform of selected LAR fields against source documents; reconciliation of LAR to the loan-origination system extract; demographic-firewall control reperformance).
- **Engagement scope supplied**: institution = state member bank; primary regulators = FRB, CFPB, state DFI; persona = compliance-testing manager; source posture = public-plus-firm-policy-plus-evidence; sector overlay = banking; cross-cutting overlays = conduct (consumer-facing), with privacy not loaded as the test does not touch GLBA Safeguards.
- **Exception register supplied**: from `exception-analysis`, exception_register_id `ER-CMP-HMDA-2026-01`. Six classified exceptions: two transposition errors on dollar amounts (data-integrity, medium); three missing-data points (one rate spread, two lien position) (documentation, medium); one mismatched property-type code (data-integrity, low). No design exceptions.
- **Test plan tolerable rate**: 3% data-point error rate for HMDA-reportable fields, set per firm policy and benchmarked against FFIEC HMDA Filing Instructions Guide [verify edition] data-validation thresholds.

## Output sketch

The skill produces a testing workpaper. Headlines:

- **Header** — workpaper ID, test ID `TP-CMP-HMDA-2026-01`, control ID for the HMDA data-integrity control, obligation IDs for Reg C 12 CFR 1003.4 [verify subsection] data points and 12 CFR 1003.5 [verify subsection] reporting, period covered (calendar year), preparer role (compliance-testing analyst), reviewer role (compliance-testing manager — separate role), QA placeholder.
- **Scope and source posture** — annual HMDA testing cycle, 60-record sample of LAR records, source posture public-plus-firm-policy-plus-evidence, no scope changes from the test plan.
- **Source criteria** — Reg C §1003.4 (data points) [verify subsection] cited with specific data-point definitions for the tested fields (loan amount, action taken, rate spread, lien position, property type, demographic information). FFIEC HMDA Filing Instructions Guide [verify edition] cited as the field-validation logic anchor.
- **Walkthrough summary** — walkthrough conducted with the LAR preparer (role), the loan-operations data-quality lead (role), and the demographic-firewall control owner (role). Screens inspected: LOS underwriting-decision screen, LAR generation report, demographic-information data-flow. Walkthrough conclusion: design appears effective; the LOS-to-LAR pipeline supports per-field reperformance, the demographic firewall is structurally enforced through role-based system access.
- **Evidence inspected** — LAR extract per sample ID (system-of-record extract from the LAR generation system, extract date noted, completeness check against the LOS originated-loan count); underlying loan files per sample (URLA, AUS findings, rate-lock confirmation, settlement statement) (system-of-record, individually pulled by sample ID); demographic-firewall evidence (system-access entitlement extract for the production environment, attestation from the demographic-firewall control owner). Reliance test note on the LAR extract: completeness reconciled to the LOS count within tolerance; accuracy validated by sample re-extraction of three records cross-checked against the live LAR.
- **Procedures performed** — P1 reperformance of the data points listed in the test plan against source documents per sample (executed against all 60 samples; six exceptions surfaced); P2 LAR-to-LOS reconciliation at the population level (executed; reconciled within tolerance); P3 demographic-firewall reperformance (executed; no exceptions). All procedures executed as designed; no fieldwork additions.
- **Sample-level results** — table with 60 rows; six rows flagged with exception IDs into ER-CMP-HMDA-2026-01.
- **Exceptions identified** — summary by classification: 0 design, 0 operating, 3 documentation, 3 data-integrity. Summary by severity: 0 critical, 0 high, 5 medium, 1 low. Repeat-issue posture: two of the data-integrity exceptions reference a prior-cycle issue on the LOS-to-LAR pipeline. Tolerable rate 3%; observed deviation rate 10% on tested data points (six exceptions across multiple data points; weighted by data-point count, the field-level deviation rate is calculated rather than the record-level rate).
- **Aggregation and projection** — concentration commentary: exceptions concentrated in non-residential refinances, suggesting a segment-specific pipeline weakness rather than a systemic LOS-to-LAR break. Sample-design implication: stratification by action-taken type was adequate for the population overall but did not stratify by property type; future cycle should consider property-type stratification. Projection commentary: appropriate to project the data-point deviation rate to the segment-level population (non-residential refinances) at the field level; not appropriate to project to the full LAR population given the segment concentration.
- **Conclusion** — design effectiveness: effective (the LOS-to-LAR pipeline supports per-field reperformance and the demographic firewall is enforced through role-based access). Operating effectiveness: partially effective (observed deviation rate 10% on data points exceeds the 3% tolerable rate; concentration in non-residential refinances). Combined: not effective at the data-point level for the non-residential refinance segment; effective for the residential-refinance and home-purchase segments tested.
- **Issues elevated** — two issues handed to `risk-compliance-core/skills/issue-writeup`: a data-integrity issue on the rate-spread calculation queue (handoff ID I-2026-013, severity medium, repeat issue from prior cycle) and a documentation issue on lien-position capture at origination (handoff ID I-2026-014, severity medium).
- **Reviewer questions** — one reviewer question: whether the segment-level deviation rate warrants re-submission consideration under the FFIEC HMDA re-submission thresholds [verify FFIEC HMDA re-submission threshold guidance edition], routed to legal review and the head of regulatory affairs; not concluded in the workpaper.
- **Limitations and reliance** — period coverage limited to the calendar year; demographic-firewall testing covers the production environment as of the testing date and does not cover the prior period; reliance on the LOS-to-LAR pipeline integrity rests on the population-level reconciliation (P2) plus sample-level reperformance (P1); no reliance on prior testing.
- **Confidence label** — high (source posture public-plus-firm-policy-plus-evidence, sample size adequate for the segment-level conclusion, evidence inspected directly).

The workpaper stops at preparer sign-off.

## Why this scenario matters

- **Boundary check on conclusion language**: the workpaper concludes on control effectiveness, not on whether the firm violated Reg C. Re-submission consideration sits with legal review and the head of regulatory affairs.
- **Boundary check on exception-analysis handoff**: the workpaper consumes the classified exception register; it does not re-classify exceptions or invent severity beyond the register.
- **Boundary check on aggregation read**: observed deviation rate exceeds tolerable, but concentration analysis matters; the conclusion distinguishes segment-level from population-level performance.
- **Boundary check on issue-writeup handoff**: two issues are elevated with distinct handoff IDs, severities, and source exception IDs; the workpaper does not draft the issue narrative.
- **Boundary check on reviewer questions**: the FFIEC re-submission consideration is a reviewer question for legal and regulatory-affairs leadership, not a conclusion.

## Anchors

- Reg C — 12 CFR Part 1003 (HMDA).
- FFIEC HMDA Filing Instructions Guide (current edition) [verify edition].
- AICPA AU-C 230 (Audit Documentation).
- AICPA AU-C 530 (Audit Sampling), §A18-§A22 (evaluating sample results) [verify paragraph references].
- FFIEC IT Examination Handbook, Audit booklet.

See `references/source-anchors.md` and `references/sector-overlays/banking.md` for full citations.
