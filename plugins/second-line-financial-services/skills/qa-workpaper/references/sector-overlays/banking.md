# Banking sector overlay — qa-workpaper

Loaded when `scope.sector_overlay_set` includes `banking` or when the QA review covers a workpaper addressing a banking regulator's rule. Does not replace `references/source-anchors.md`; supplements it with bank-specific QA conventions. This is the heaviest overlay in the qa-workpaper file set: bank-supervisory expectations on independent QA over the testing program are explicit and recurring CMS findings.

## QA conventions banking examiners expect

A QA review note over a bank consumer-compliance, BSA/AML, or operational-risk testing workpaper carries a few conventions beyond the IIA / AICPA baseline:

- **Independent QA is structural, not advisory.** The CFPB CMS examination procedures, the OCC Comptroller's Handbook CMS module, and SR 08-8 read independent QA over the testing program as a CMS pillar. A workpaper that has not been QA-reviewed by an independent reviewer is a CMS finding distinct from any substantive control finding.
- **Reviewer-separation is a structural QA dimension.** Bank exam findings repeatedly cite preparer-and-reviewer-as-same-role and preparer-and-QA-as-same-role on the sign-off block. The QA review note checks the sign-off block first; same-role overlap is a critical deficiency that returns the workpaper.
- **Population definition and extract-integrity are QA scope items.** Examiners pull the workpaper, the population definition, and the extract integrity check together. The QA reviewer challenges whether the extract date is recorded, whether the run-by role is named, and whether the completeness check against an independent count is documented. Missing any of the three is a major deficiency.
- **Severity calibration ties to the firm's CMS rating implications.** Severity inflation in the workpaper distorts the testing-program output that feeds the CMS rating; severity deflation buries findings the examiner will surface anyway. The QA reviewer challenges severity against firm methodology floors and against analogous prior workpapers; both directions get pushback.
- **Conclusion language stays in second-line vocabulary.** Bank consumer-compliance workpapers occasionally drift into "the firm violated [Reg X]" framing. The QA reviewer rewrites to control-effectiveness language and routes the legal-violation question to legal counsel and the head of regulatory affairs separately.

## Bank-supervisory anchors (load by reference; do not restate)

- **CFPB Compliance Management Review** examination procedures inside the **CFPB Supervision and Examination Manual** (current edition) [verify section labels for the testing-program independent-QA component]. https://www.consumerfinance.gov/compliance/supervision-examinations/ .
- **OCC Comptroller's Handbook — Compliance Management Systems** [verify current edition and section labels for independent-QA expectations]. https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/index-comptrollers-handbook.html .
- **SR 08-8 — Compliance Risk Management Programs and Oversight at Large Banking Organizations with Complex Compliance Profiles** (Federal Reserve, October 16, 2008) [verify section labels for independent-review of testing work product]. https://www.federalreserve.gov/boarddocs/srletters/2008/sr0808.htm .
- **OCC PPM 5310-3 — Bank Supervision Process** [verify exact PPM number and current effective date].
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for $50B+ covered banks; independent-risk-management standards on testing-program QA feed the risk-governance framework and the board's third-line oversight [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-I/part-30 .
- **FFIEC Consumer Compliance Rating System** (Federal Register, 80 Fed. Reg. 67428, November 2, 2015) [verify Federal Register citation]. https://www.federalregister.gov/documents/2015/11/02/2015-27738/ffiec-consumer-compliance-rating-system [verify URL].

## Bank-control-area QA notes

### HMDA / Reg C testing — QA scope items

- Reg C — 12 CFR Part 1003. §1003.4 data points, §1003.5 disclosure and reporting [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1003 .
- QA conventions: the QA reviewer re-performs a small subsample of the LAR-to-LOS reconciliation and the per-field reperformance to confirm the preparer's findings; QA challenges whether the field-level deviation rate calculation matches the FFIEC HMDA Filing Instructions Guide [verify edition] field-validation logic; QA challenges whether the segment concentration commentary is supported (e.g., non-residential refinances clustered) and whether the FFIEC HMDA re-submission threshold consideration was routed to legal review and the head of regulatory affairs as a reviewer question, not concluded in the workpaper.

### CRA testing — QA scope items

- CRA — 12 CFR Part 25 (OCC), Part 195 (former OTS, OCC), Part 228 (FRB Reg BB), Part 345 (FDIC) [verify current effective state given the 2023 final-rule litigation history]. https://www.federalreserve.gov/supervisionreg/regbbcg.htm .
- QA conventions: the QA reviewer challenges whether the lending-test workpaper carries the geography distribution, borrower-profile distribution, and product-mix distribution against the assessment-area definition; whether the qualified-investment register reconciles to the workpaper's investment-test sample; whether performance-context narrative was carried from the test plan rather than invented in the workpaper.

### Reg B / ECOA testing — QA scope items

- Reg B — 12 CFR Part 1002. §1002.4, §1002.6, §1002.9, §1002.13 [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1002 .
- QA conventions: the QA reviewer challenges whether adverse-action notice-timing testing reconciles application date to notice date by sample; whether spousal-signature testing reads the underwriting file (not just the front-end application); whether demographic-firewall testing reads the production environment (not the test environment). Production-versus-test environment evidence reliance is a recurring QA finding on Reg B workpapers.

### Reg DD, Reg E, Reg Z testing — QA scope items

- Reg DD — 12 CFR Part 1030; Reg E — 12 CFR Part 1005 (especially §1005.11 and §1005.18); Reg Z — 12 CFR Part 1026 [verify subsection labels].
- QA conventions: error-resolution workpapers under Reg E §1005.11 are walked by sample with QA re-perform of the timeline (notice date, investigation start, provisional credit, final determination, customer notice). Common QA findings: "investigation completed" rows without an evidence ID; severity rated medium where firm methodology floor for §1005.11(c) timing is high; conclusion language drifting toward "the bank did not comply with Reg E §1005.11(c)" instead of control-effectiveness framing. Disclosure-content workpapers carry a redline against the regulatory model; QA confirms the redline and the noted deviations.

### BSA/AML testing — QA scope items

- FFIEC BSA/AML Examination Manual (current edition) [verify last-revision date]. https://bsaaml.ffiec.gov/manual .
- 31 CFR Part 1010, 1020, 1022, 1023, 1024, 1025, 1026 (FinCEN AML rules by industry) [verify part references].
- QA conventions: CIP testing QA confirms new-account opening packet ties to the documented identification and verification step; CDD/EDD testing QA confirms the customer-due-diligence questionnaire and EDD enrichment evidence is sampled and reperformed; SAR-decision testing QA confirms the case-management file walks alert to disposition with timing checks against 31 CFR §1020.320. SAR content review is restricted to authorised reviewers; the QA reviewer does not restate SAR content in the QA review note and confirms the access-control posture on the underlying file is documented.

### CFPB CMS exam-cycle workpapers — QA scope items

- The QA review reads against the four CMS pillars (board and management oversight, compliance program, response to consumer complaints, compliance audit). The compliance-audit pillar carries the independent-QA requirement; a workpaper that has not been independently QA-reviewed creates a separate CMS finding from any substantive control finding. The QA reviewer flags this distinction in the review note where applicable.

## Sponsor-bank / bank-fintech-arrangement QA — examiner-prep sweep posture

A Federal Reserve, OCC, or FDIC targeted exam on third-party risk frequently arrives with six-to-eight-week notice. The second-line QA function is often called to do an examiner-prep sweep on the population of TPRM workpapers from the most recent testing cycle. The sweep posture differs from in-cycle QA:

- **Per-workpaper QA notes batched into one summary review.** The deliverable is a portfolio QA review with population-level deficiency themes plus per-workpaper notes.
- **Common deficiencies carried explicitly.** Vendor-supplied SOC 2 reports cited as evidence without the firm's reliance assessment documented; critical-vendor monitoring conclusions without evidence of the firm's KRI dashboard tie-out for that vendor; severity calibration on exit-plan-testing absence rated medium where firm methodology floor (and supervisory expectation) is high.
- **Issue closure approval status flagged separately from workpaper closure.** A workpaper accepted by QA does not close any open issue identified in the workpaper. The QA review note carries `issue_closure_approval` separately from `decision`.
- **Methodology-drift finding.** A population-level pattern (e.g., reviewer drift across workpapers in the cycle) is itself a finding worth documenting; the recommendation seed routes back to a methodology refresh before the next cycle, not to per-workpaper rework.

The frame:

- **Interagency Guidance on Third-Party Relationships: Risk Management** (FRB / FDIC / OCC, June 2023; 88 Fed. Reg. 37920, June 9, 2023) [verify section labels for ongoing-monitoring evidence and the firm's testing-and-review posture]. https://www.federalreserve.gov/supervisionreg/srletters/sr2304.htm .
- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. End-customer reconciliation, FBO subledger, deposit-insurance representation, and the fourth-party register all sit inside this frame.
- **Bank Service Company Act, 12 USC §1867(c)**: examiner-access posture for vendor systems the firm relied on for evidence; the QA reviewer confirms the workpaper named the BSCA-relied-on systems separately so the examiner can sequence the access request.

## Audience and tone

A QA review note drafted with an upcoming OCC, FRB, FDIC, or CFPB exam in mind reads heavier on independent-QA evidence (sign-off block, reviewer separation, QA reviewer role and date), heavier on extract-integrity dimensions, and heavier on conclusion-language hygiene. A QA note for in-cycle testing-program closure reads operationally with the same dimensions but lighter on the examiner-prep posture.
