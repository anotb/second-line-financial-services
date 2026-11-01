# Example: HMDA LAR data-integrity PBC list for the annual compliance-testing cycle

Public-source-derived. No named institution. The shape mirrors the evidence ask a compliance-testing pod fields ahead of an annual HMDA Loan Application Register data-integrity test.

## Input

- **Test cycle**: annual HMDA LAR data-integrity test, drafting the PBC list ahead of fieldwork.
- **Test plan reference**: pre-fieldwork test plan (test ID `TP-CMP-HMDA-2026-01`) with operating-effectiveness procedures defined: P1 reperformance of selected LAR data points against source documents per sample, P2 LAR-to-LOS reconciliation at the population level, P3 demographic-firewall reperformance.
- **Sampling memo reference**: `SM-CMP-HMDA-2026-01` from `control-sampling`. 60 LAR records, stratified by action-taken type.
- **Engagement scope supplied**: institution = state member bank; primary regulators = FRB, CFPB, state DFI; persona = compliance-testing manager (reviewer); source posture = public-plus-firm-policy-plus-evidence; sector overlay = banking; cross-cutting overlay = conduct (consumer-facing), privacy not loaded (no GLBA Safeguards touch).
- **Period under test**: calendar year LAR.

## Output sketch

The skill produces a PBC evidence request list. Headlines:

- **Header** — evidence request list ID `ER-CMP-HMDA-2026-01`, test ID `TP-CMP-HMDA-2026-01`, control ID for the HMDA data-integrity control, obligation IDs for Reg C 12 CFR 1003.4 [verify subsection] data points and 12 CFR 1003.5 [verify subsection] reporting, period covered (calendar year), preparer role (compliance-testing analyst), reviewer role (compliance-testing manager), source posture public-plus-firm-policy-plus-evidence, escalation path (testing manager, then chief compliance officer), confidence label high.
- **Request summary** — 12 requests, due-date span aligned to the four-week fieldwork window, owner roles spread across LAR preparer, loan-operations data-quality lead, demographic-firewall control owner, and AUS configuration owner.
- **Request rows (representative)**:
  - `R001` — control objective: LAR data-point completeness and accuracy per sample. Criterion source: Reg C §1003.4 [verify subsection] data-point definitions. Artifact: LAR record extract for the 60 sampled LEI-loan-IDs with all 110 reportable data points, format CSV with named columns matching the FFIEC HMDA Filing Instructions Guide [verify edition] field labels (no screenshots accepted). System of record: LAR generation system. Owner role: LAR preparer. Due date: fieldwork day 5. Reliance: original-system-output. Sensitivity: confidential (NPI on borrower fields). Status: open.
  - `R002` — control objective: source-document support for sampled LAR records. Criterion source: Reg C §1003.4 [verify subsection]. Artifact: underlying loan-application file per sample ID (URLA, AUS findings, rate-lock confirmation, settlement statement, lien-position evidence). Format PDF (one bundle per sample). System of record: loan origination system, document repository. Owner role: loan operations file-pull lead. Due date: fieldwork day 10. Reliance: original-system-output. Sensitivity: confidential. Status: open.
  - `R003` — control objective: AUS configuration evidence supporting the AUS findings reliance. Criterion source: firm AUS reliance policy section, FFIEC HMDA Filing Instructions Guide [verify edition]. Artifact: AUS configuration export covering the period's underwriting rule set. Format system-export (CSV or PDF as the AUS supports). System of record: AUS (vendor). Owner role: AUS configuration owner. Due date: fieldwork day 7. Reliance: vendor-supplied (drives reliance test note in the workpaper). Sensitivity: internal. Status: open.
  - `R004` — control objective: ECOA monitoring data flow integrity. Criterion source: Reg B §1002.13 [verify subsection]. Artifact: demographic-information form per sample plus the front-end-to-back-end flow log. Format PDF (forms) plus CSV (flow log). System of record: loan origination system, demographic data store. Owner role: demographic-firewall control owner. Due date: fieldwork day 8. Reliance: original-system-output. Sensitivity: confidential. Status: open.
  - `R005` — control objective: demographic firewall structural enforcement. Criterion source: Reg B §1002.5(b) [verify subsection], firm fair-lending policy section. Artifact: production-environment role-based access entitlement extract for any role with read-or-write access to demographic information at underwriting. Format system-export CSV. System of record: IAM (Okta, Azure AD, or named equivalent). Owner role: IAM operations lead. Due date: fieldwork day 5. Reliance: original-system-output. Sensitivity: internal. Status: open.
  - `R006` — control objective: rate-spread calculation queue integrity (repeat-issue area from prior cycle). Criterion source: Reg C §1003.4(a)(12) [verify subsection], FFIEC HMDA Filing Instructions Guide rate-spread methodology [verify edition]. Artifact: rate-spread calculation log for the period with input fields and output spread per sample. Format CSV. System of record: rate-spread calculation engine. Owner role: pricing operations lead. Due date: fieldwork day 7. Reliance: original-system-output. Sensitivity: internal. Status: open.
  - `R007` — control objective: LAR-to-LOS population reconciliation evidence. Criterion source: firm LAR data-quality policy section. Artifact: quarterly LAR data-quality reconciliation log for the period. Format PDF (signed by the data-quality lead). System of record: loan-operations reconciliation log. Owner role: loan-operations data-quality lead. Due date: fieldwork day 3. Reliance: management-prepared (drives completeness-and-accuracy check). Sensitivity: internal. Status: open.
  - `R008` — control objective: prior-cycle LAR resubmission evidence. Criterion source: FFIEC HMDA resubmission threshold guidance [verify FFIEC edition], firm HMDA resubmission policy section. Artifact: prior-year resubmission log including resubmitted records, the resubmission rationale, and the regulator-acknowledgement evidence (where applicable). Format PDF. System of record: regulatory-reporting log. Owner role: regulatory-reporting manager. Due date: fieldwork day 5. Reliance: original-system-output. Sensitivity: confidential. Status: open.
  - Additional rows (R009-R012) cover preapproval-program disclosures, lien-position evidence on selected samples, loan-officer credentials per sample, and the AUS findings export per sample.
- **Not-applicable items**:
  - Pre-period LAR records — out of period; the LAR is calendar-year scoped.
  - Small-business loans — out of scope under HMDA; covered separately under the Section 1071 testing cycle (12 CFR Part 1002 Subpart B; **§1071 revised final rule, May 1, 2026: 1,000 covered transactions; effective June 30, 2026; compliance January 1, 2028** — supersedes the 2023 tiered schedule) under test plan `TP-CMP-1071-2026-01`.
  - SAR content for any sampled customer — restricted access; the LAR data-integrity test does not inspect SAR content. SAR-decision testing is a separate cycle with its own access-control posture.
- **Limitations** — the request list addresses the calendar year only; demographic-firewall evidence is point-in-time at the testing date and does not cover the prior period; reliance on vendor AUS configuration evidence carries a separate completeness check via R003.
- **Reviewer questions** — one reviewer question for pre-fielding sign-off: whether the demographic-firewall entitlement extract (R005) should also pull the test environment for comparison, given that the firm's demographic-firewall control has historically been tested only against production. Routed to the testing manager.
- **Confidence label** — high.

The list is a spreadsheet artifact; render it via the `xlsx` skill in `document-skills`.

## Why this scenario matters

- **Boundary check on artifact specificity** — every request names the artifact concretely (CSV with named columns, PDF bundle per sample, role-based entitlement extract for a specific role-set), not "all relevant LAR documents".
- **Boundary check on reliance classification** — vendor-supplied (AUS configuration) and management-prepared (data-quality reconciliation log) evidence are flagged so the workpaper applies the right reliance test.
- **Boundary check on the not-applicable section** — small-business loans, pre-period records, and SAR content are explicitly out, with the rationale and the separate cycle named where applicable. Avoids re-ask in next year's cycle.
- **Boundary check on criterion-per-row** — each row names a single criterion source (regulation section, policy section, or methodology). Where the criterion stack is complex, the request was split rather than collapsed.
- **Boundary check on format specificity** — CSV asks name expected columns; "screenshot" is not accepted on data-integrity tests.

## Anchors

- Reg C — 12 CFR Part 1003 (HMDA), §1003.4 data points and §1003.5 reporting.
- FFIEC HMDA Filing Instructions Guide (current edition) [verify edition].
- Reg B — 12 CFR Part 1002, §1002.5(b) and §1002.13 [verify subsections].
- AICPA AU-C 500, Audit Evidence [verify paragraph].
- IIA Standard on Identifying Information (current Global Internal Audit Standards mapping of prior IPPF 2310) [verify section].

See `references/source-anchors.md` and `references/sector-overlays/banking.md` for full citations.
