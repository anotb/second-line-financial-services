# Example: Examiner-prep QA sweep on a portfolio of TPRM workpapers

Public-source-derived. No named institution. Mirrors the standard examiner-prep QA sweep done six weeks before a Federal Reserve targeted exam on third-party risk.

## Input

- **QA scope**: examiner-prep-sweep on 14 TPRM workpapers from the most recent testing cycle.
- **Trigger**: a Federal Reserve targeted exam on third-party risk is six weeks out. The second-line QA function is doing an examiner-prep sweep on the TPRM workpaper population the examiner is likely to sample.
- **Engagement scope supplied**: institution = mid-size bank holding company (large complex banking organisation under SR 08-8); primary regulators = FRB, OCC for the lead bank, plus state DFI; persona = QA reviewer (independent of the workpaper reviewers); source posture = public-plus-firm-policy-plus-evidence; sector overlays = banking and payments-fintech (the TPRM portfolio includes sponsor-bank fintech-program testing); cross-cutting overlays = cyber (TPRM portfolio includes vendor-IAM testing).
- **Inputs to the QA reviewer**: 14 completed TPRM workpapers, their underlying exception registers, the firm TPRM methodology, source-anchor file pointers (interagency TPRM guidance June 2023, joint statement on bank deposit arrangements July 2024, IIA Standard 1300, AICPA AU-C 230 / 530, FFIEC IT booklet).

## Output sketch

The skill produces an Excel workbook (per-workpaper QA tabs plus a portfolio summary tab) plus a Word QA memo. Headlines from the memo:

### Executive summary

- **Portfolio decision: 9 accept, 4 conditional-accept, 1 return-for-rework.** Aggregate severity across the 14 workpapers: 1 critical, 5 major, 14 minor.
- **Methodology drift across reviewers** is the dominant population-level finding; recommendation seed routes back to a methodology refresh before the next testing cycle, not just to per-workpaper rework.
- **Three workpapers have issue closure approval status flagged "not-approved"** pending rework; one has the underlying issue in `issue-writeup` already opened.

### QA scope

- 14 TPRM workpapers from the Q4 2025 testing cycle. Coverage: 6 critical-vendor monitoring workpapers, 4 SOC 2 reliance workpapers, 2 exit-plan-testing workpapers, 2 sponsor-bank deposit-program workpapers. Methodology references applied: AICPA AU-C 230 / 530, IIA Standard 1300 and 2340, interagency TPRM guidance June 2023, firm TPRM methodology.

### Population-level deficiency themes

- **Evidence-reliability (recurring across 8 of 14 workpapers).** Vendor-supplied SOC 2 reports cited as evidence without the firm's reliance assessment documented. The firm's reliance posture (CUEC review, complementary user entity controls posture, scope-period coverage versus the firm's testing period, qualified-opinion read) is missing from the evidence-inspected table on most workpapers.
- **Conclusion-support (recurring across 4 of 14 workpapers).** Workpapers concluding on critical-vendor monitoring as effective without any evidence of the firm's KRI dashboard for that vendor; the conclusion rests on the existence of a vendor-supplied report alone.
- **Severity calibration (recurring across 2 of 14 workpapers).** Two workpapers rate exit-plan-testing absence as medium; firm methodology floor (and supervisory expectation under interagency TPRM guidance June 2023) is high for critical vendors. Severity inflation requested.

### Deficiency findings (selected; full register in workbook Tab 3)

- **D1 (critical, conclusion-support).** Workpaper WP-2025-Q4-TPRM-007 (critical-vendor monitoring on a payment-processing vendor). Observation: workpaper concludes critical-vendor monitoring effective; no evidence of the firm's KRI dashboard tie-out for the vendor, no evidence of the firm's incident-tracking integration, no evidence of the firm's quarterly-review meeting minutes. Methodology reference: firm TPRM methodology, interagency TPRM guidance June 2023 [verify section]. Required action: return workpaper; redraft conclusion against the firm's actual monitoring evidence; if monitoring evidence is not produced, the conclusion rebases to not-effective and the issue elevates separately.
- **D2-D9 (major, evidence-reliability).** Eight workpapers cite vendor-supplied SOC 2 reports as evidence without firm reliance assessment. Required action per workpaper: add reliance assessment to evidence-inspected table; document CUEC posture and any unaddressed CUECs; document scope-period coverage versus firm testing period.
- **D10 (major, conclusion-support, paired with D2-D9).** Four workpapers conclude on critical-vendor monitoring without KRI dashboard evidence. Required action per workpaper: add KRI dashboard tie-out evidence or rebase conclusion.
- **D11-D12 (major, severity-calibration).** Two workpapers rate exit-plan-testing absence as medium; firm methodology floor is high. Required action: rebase severity to high; re-evaluate disposition (likely elevation to issue).
- **D13-D26 (minor, formatting and miscellaneous).** Fourteen minor deficiencies across the portfolio: missing population reconciliation totals, missing evidence reliance classification on case-management extracts, missing stratum-level breakdowns, scope-statement inconsistencies between test plan and workpaper.

### Sample re-perform results

- QA re-performed selected items across 6 workpapers (the higher-stakes critical-vendor monitoring and sponsor-bank deposit-program workpapers). Re-perform identified two divergences: one on a SOC 2 reliance workpaper (the SOC 2 report scope did not cover the firm's testing period; the workpaper relied on the report regardless), and one on a sponsor-bank end-customer reconciliation workpaper (the FBO subledger reconciliation evidence was sponsor-supplied; the firm did not independently verify).

### Severity calibration

- Two floor violations on exit-plan-testing absence (D11-D12). Methodology drift across reviewers is the underlying pattern; the methodology refresh recommendation seed routes the floor reaffirmation into the refresh.

### Conclusion support

- Aggregate: 9 of 14 workpapers carry supported conclusions (with minor noted); 4 carry partially-supported conclusions pending the rework items (D2-D10); 1 carries a not-supported conclusion (D1, return).

### Decision

| Workpaper ID | Decision | Rework items (if any) |
|---|---|---|
| WP-2025-Q4-TPRM-001 | accept | (minor noted) |
| WP-2025-Q4-TPRM-002 | accept | (minor noted) |
| WP-2025-Q4-TPRM-003 | conditional-accept | document SOC 2 reliance assessment; add CUEC posture |
| WP-2025-Q4-TPRM-004 | conditional-accept | document KRI dashboard tie-out for critical-vendor monitoring conclusion; add SOC 2 reliance assessment |
| WP-2025-Q4-TPRM-005 | accept | (minor noted) |
| WP-2025-Q4-TPRM-006 | conditional-accept | rebase exit-plan-testing severity to high; re-evaluate disposition |
| WP-2025-Q4-TPRM-007 | return-for-rework | redraft critical-vendor monitoring conclusion against actual monitoring evidence; if evidence not produced, rebase conclusion to not-effective and elevate issue |
| WP-2025-Q4-TPRM-008 | accept | (minor noted) |
| WP-2025-Q4-TPRM-009 | conditional-accept | document SOC 2 reliance assessment; add KRI dashboard tie-out |
| WP-2025-Q4-TPRM-010 | accept | (minor noted) |
| WP-2025-Q4-TPRM-011 | accept | (minor noted) |
| WP-2025-Q4-TPRM-012 | accept | (minor noted) |
| WP-2025-Q4-TPRM-013 | accept | (minor noted) |
| WP-2025-Q4-TPRM-014 | accept | (minor noted) |

- **Issue closure approval status**: 3 workpapers flagged not-approved pending rework (WP-007, WP-004, WP-009 — all on critical-vendor monitoring conclusions); 11 not-applicable.

### Reviewer questions

- Q1: does the methodology refresh sit before the next testing cycle, or does it sit inside the current cycle as a mid-cycle methodology amendment? — testing manager plus head of compliance testing.
- Q2: should the SOC 2 reliance posture be standardised in the testing template (defaulted to require CUEC posture documentation) or left to per-workpaper preparer discretion? — testing manager.
- Q3: who routes the WP-007 rework to the workpaper reviewer, and what is the closure timeline given the six-week exam window? — head of compliance testing.

### QA confidence label

- Medium overall. The population shows methodology drift across reviewers, suggesting a methodology refresh is needed before the next cycle. QA re-perform was completed on six of fourteen workpapers; full re-perform across the population was not feasible in the examiner-prep window.

## Why this scenario matters

- **Boundary check on examiner-prep posture.** The QA scope is examiner-prep-sweep, not in-cycle QA; the deliverable is a portfolio QA memo plus per-workpaper notes, not 14 separate full-review packs.
- **Boundary check on population-level themes.** The dominant finding (methodology drift) is a population-level pattern, not a per-workpaper deficiency. The recommendation seed routes to methodology refresh, not to per-workpaper rework alone.
- **Boundary check on issue closure approval.** Three workpapers are flagged not-approved for issue closure separately from the workpaper-decision column; QA decision and issue closure decision are distinct.
- **Boundary check on QA confidence labelling.** Medium confidence for the portfolio reflects re-perform coverage limits in the examiner-prep window, not a defect in the QA reviewer's work; the confidence label is honest about what the QA could and could not cover in the window.

## Anchors

- AICPA AU-C 230 (Audit Documentation).
- AICPA AU-C 530 (Audit Sampling) §A18-§A22 [verify paragraph references].
- IIA Standard 1300 [verify section labels] (QAIP) and Standard 2340 [verify section labels] (engagement supervision).
- Interagency Guidance on Third-Party Relationships: Risk Management (FRB / FDIC / OCC, June 2023).
- Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services (FDIC / OCC / FRB, July 25, 2024).
- FFIEC IT Examination Handbook (Audit booklet, April 2012).
- Banking sector overlay (this skill); payments-fintech sector overlay (this skill); cyber cross-cutting overlay (this skill).

See `references/source-anchors.md`, `references/sector-overlays/banking.md`, `references/sector-overlays/payments-fintech.md`, and `references/cross-cutting/cyber.md` for full citations.
