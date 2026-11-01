# Banking sector overlay — workpaper-drafter

Loaded when `scope.sector_overlay_set` includes `banking` or when the test addresses a banking regulator's rule. Does not replace `references/source-anchors.md`; supplements it with bank-specific workpaper conventions.

## Workpaper conventions banking examiners expect

A bank consumer-compliance or operational-risk testing workpaper read by an OCC, FDIC, FRB, CFPB, or NYDFS examiner carries a few conventions beyond the AU-C 230 baseline:

- **Test plan reference is binding.** Examiners pull the test plan and the workpaper together. Silent drift between them reads as a methodology weakness. Document scope changes with pre-fieldwork sign-off references.
- **Reviewer-separation evidence is structural.** Bank exam findings repeatedly cite preparer-and-reviewer-as-same-role as a CMS finding. The workpaper sign-off block makes the separation obvious.
- **Population definition is restated, not assumed.** The workpaper restates how the population was defined (originations during period, accounts open during period, transactions executed during period), where it was extracted from, and the completeness check on the extract. Examiners walk this first when they pull the workpaper.
- **Evidence reliance on system-of-record extracts requires the extract date and an integrity check.** Extracts run at different dates produce different populations; the workpaper names the extract date, the run-by role, and what the preparer did to confirm extract completeness against an independent count.

## Bank-supervisory anchors (load by reference; do not restate)

- **CFPB Compliance Management Review** examination procedures inside the **CFPB Supervision and Examination Manual** (current edition) [verify section labels for the testing-program component]. https://www.consumerfinance.gov/compliance/supervision-examinations/ .
- **FFIEC Consumer Compliance Rating System** (Federal Register, 80 Fed. Reg. 67428, November 2, 2015) [verify Federal Register citation]. https://www.federalregister.gov/documents/2015/11/02/2015-27738/ffiec-consumer-compliance-rating-system [verify URL].
- **OCC Comptroller's Handbook — Compliance Management Systems** [verify current edition and section labels]. https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/index-comptrollers-handbook.html .
- **SR 08-8 — Compliance Risk Management Programs and Oversight at Large Banking Organizations with Complex Compliance Profiles** (Federal Reserve, October 16, 2008) [verify section labels for testing-program documentation]. https://www.federalreserve.gov/boarddocs/srletters/2008/sr0808.htm .
- **OCC PPM 5310-3 — Bank Supervision Process** [verify exact PPM number and current effective date].
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for $50B+ covered banks; testing-program outputs feed the risk-governance framework and the board's third-line oversight [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-I/part-30 .

## Bank-control-area workpaper notes

### HMDA / Reg C testing

- Reg C — 12 CFR Part 1003. §1003.4 data points, §1003.5 disclosure and reporting [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1003 .
- FFIEC HMDA Filing Instructions Guide (current edition) [verify edition year]. https://www.ffiec.gov/hmda/guide.htm .
- Workpaper conventions: data-integrity tests reconcile LAR to the loan origination system extract by sample; the source criteria carry the data-point definition and the FFIEC field-validation logic. Sample design typically stratified by action-taken type and rate-spread reportability.

### CRA testing

- CRA — 12 CFR Part 25 (OCC), Part 195 (former OTS, OCC), Part 228 (FRB Reg BB), Part 345 (FDIC) [verify current effective state given the 2023 final-rule litigation history]. https://www.federalreserve.gov/supervisionreg/regbbcg.htm .
- Workpaper conventions: lending-test workpapers carry the geography distribution, borrower-profile distribution, and product-mix distribution. Service-test and investment-test workpapers carry the qualified-investment register. Performance-context narrative is set out in the test plan, not invented in the workpaper.

### Reg B / ECOA testing

- Reg B — 12 CFR Part 1002. §1002.4 general rules, §1002.6 rules concerning evaluation of applications, §1002.9 notifications, §1002.13 information for monitoring purposes [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1002 .
- Workpaper conventions: adverse-action notice-timing testing reconciles application date to notice date by sample; spousal-signature testing requires reading the underwriting file, not just the front-end application; demographic-firewall testing for monitoring information requires inspection of the production environment, not the test environment.

### Reg DD, Reg E, Reg Z testing

- Reg DD — 12 CFR Part 1030 (TISA disclosures, account fees) [verify subsection labels].
- Reg E — 12 CFR Part 1005 (electronic fund transfers, error resolution) [verify subsection labels including §1005.11 procedures and §1005.18 prepaid].
- Reg Z — 12 CFR Part 1026 (Truth in Lending) [verify subsection labels].
- Workpaper conventions: error-resolution workpapers under Reg E §1005.11 walk the timeline by sample (notice date, investigation start, provisional credit, final determination, customer notice). Disclosure-content workpapers compare the production disclosure to the regulatory model with a redline and note any deviations.

### BSA/AML testing

- FFIEC BSA/AML Examination Manual (current edition) [verify last-revision date]. https://bsaaml.ffiec.gov/manual .
- 31 CFR Part 1010, 1020, 1022, 1023, 1024, 1025, 1026 (FinCEN AML rules by industry) [verify part references].
- Workpaper conventions: CIP testing reconciles new-account opening packet to the documented identification and verification step; CDD/EDD testing reads the customer-due-diligence questionnaire and the EDD enrichment evidence; SAR-decision testing reviews the case-management file from alert to disposition with timing checks against 31 CFR §1020.320. SAR content review is restricted to authorised reviewers; the workpaper notes the access control on the underlying file rather than restating SAR content.

### CFPB CMS exam-cycle workpapers

- The CFPB CMS examination procedures embed testing-program review. The workpaper reads against the four CMS pillars (board and management oversight, compliance program, response to consumer complaints, compliance audit). Findings on the testing program itself feed the CMS rating, distinct from substantive control findings.

## Sponsor-bank / bank-fintech-arrangement testing

When the test addresses a bank-fintech partnership or a sponsor-bank deposit program, the workpaper carries:

- The **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date] frame: end-customer reconciliation testing, FBO subledger reconciliation, deposit-insurance representation review, and the fourth-party register all sit inside this frame.
- **Bank Service Company Act, 12 USC §1867(c)**: examiner-access posture for the vendor systems the firm relied on for evidence; cite when reliance evidence is from a bank service provider.
- **OCC, FDIC, FRB consent-order public materials** for sponsor-bank programs (cite by named order when public): used to anchor the regulatory expectation, not as a named-institution narrative.

## Audience and tone

A workpaper drafted with an upcoming OCC, FRB, FDIC, or CFPB exam in mind reads heavier on criteria (more verbatim from the regulation, more detail on FFIEC manual sections), heavier on limitations (period coverage, scope exclusions, reliance on prior testing), and heavier on the population-definition narrative. A workpaper drafted for in-cycle internal QA reads operationally with the same evidence base.
