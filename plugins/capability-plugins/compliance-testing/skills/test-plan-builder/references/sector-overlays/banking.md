# Banking sector overlay — test-plan-builder

Loaded when `scope.sector_overlay_set` includes `banking` or when the test addresses a banking regulator's rule. Does not replace `references/source-anchors.md`; supplements it with bank-specific test-plan conventions.

## Test-plan conventions banking examiners expect

A bank consumer-compliance or operational-risk test plan that an OCC, FDIC, FRB, CFPB, or NYDFS examiner will later read at exam carries a few conventions beyond the IIA / AU-C 300 baseline:

- **Risk-based prioritization is named, not assumed.** Bank-supervisory expectations on the testing program (under SR 08-8 [verify section] and the OCC CMS handbook [verify section]) are that the test plan ties scope to a risk-based rationale rather than a calendar habit. The plan restates the risk read (customer impact, financial impact, regulatory impact, prior-cycle history) that produced this cycle's scope.
- **Pre-fieldwork sign-off is a hard gate.** Examiners pull the test plan and the workpaper together. A test plan signed after evidence pulls began reads as a methodology weakness; the plan's reviewer-signoff date should precede the evidence-request fielding date.
- **Test plan and workpaper are the same contract.** Silent drift between executed procedures and planned procedures is a CMS finding; the plan documents what gets done so the workpaper later either matches or names the divergence with sign-off.
- **Population definition is restated, not inherited.** The plan restates how the population is defined (originations during the period, accounts open during the period, transactions executed, packets due), where the extract comes from, and the completeness check the workpaper will run against the extract. Examiners walk this first when they pull the workpaper.
- **Reviewer separation is structural.** Bank exam findings repeatedly cite preparer-and-reviewer-as-same-role as a CMS finding. The plan's sign-off block makes the separation obvious from planning time.

## Bank-supervisory anchors (load by reference; do not restate)

- **CFPB Compliance Management Review** examination procedures inside the **CFPB Supervision and Examination Manual** (current edition) [verify section labels for the testing-program component]. https://www.consumerfinance.gov/compliance/supervision-examinations/ .
- **FFIEC Consumer Compliance Rating System** (Federal Register, 80 Fed. Reg. 67428, November 2, 2015) [verify Federal Register citation]. https://www.federalregister.gov/documents/2015/11/02/2015-27738/ffiec-consumer-compliance-rating-system [verify URL].
- **OCC Comptroller's Handbook — Compliance Management Systems** [verify current edition and section labels]. https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/index-comptrollers-handbook.html .
- **SR 08-8 — Compliance Risk Management Programs and Oversight at Large Banking Organizations with Complex Compliance Profiles** (Federal Reserve, October 16, 2008) [verify section labels for the testing-program planning expectations]. https://www.federalreserve.gov/boarddocs/srletters/2008/sr0808.htm .
- **OCC PPM 5310-3 — Bank Supervision Process** [verify exact PPM number and current effective date].
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for $50B+ covered banks [verify asset threshold and subsection labels]. The plan's risk-based-prioritization rationale and the reviewer-separation discipline both feed the heightened-standards posture. https://www.ecfr.gov/current/title-12/chapter-I/part-30 .

## Bank-control-area test-plan notes

### HMDA / Reg C testing

- Reg C — 12 CFR Part 1003. §1003.4 data points, §1003.5 disclosure and reporting [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1003 .
- FFIEC HMDA Filing Instructions Guide (current edition) [verify edition year]. https://www.ffiec.gov/hmda/guide.htm .
- Test-plan conventions: criteria section names the data-point definitions per tested field and the FFIEC field-validation logic; population is the LAR records for the period with extract from the LAR generation system; sample is typically stratified by action-taken type and rate-spread reportability; design procedures cover the LOS-to-LAR pipeline configuration and the demographic firewall; operating procedures cover per-field reperformance against source documents and population-level LAR-to-LOS reconciliation.

### CRA testing

- CRA — 12 CFR Part 25 (OCC), Part 195 (former OTS, OCC), Part 228 (FRB Reg BB), Part 345 (FDIC) [verify current effective state given the 2023 final-rule litigation history]. https://www.federalreserve.gov/supervisionreg/regbbcg.htm .
- Test-plan conventions: lending-test plans carry geography distribution, borrower-profile distribution, and product-mix distribution as planned outputs; service-test and investment-test plans carry the qualified-investment register-review approach. The performance-context narrative is set out in the plan, not invented in the workpaper.

### Reg B / ECOA testing

- Reg B — 12 CFR Part 1002. §1002.4 general rules, §1002.6 rules concerning evaluation, §1002.9 notifications, §1002.13 information for monitoring [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1002 .
- Test-plan conventions: adverse-action notice-timing tests reconcile application date to notice date by sample with the §1002.9 timing clock as the criterion; spousal-signature tests require reading the underwriting file rather than the front-end application; demographic-firewall tests require inspection of the production environment, not the test environment, and the plan names the production-access prerequisite.

### Reg DD, Reg E, Reg Z testing

- Reg DD — 12 CFR Part 1030 (TISA disclosures, account fees) [verify subsection labels].
- Reg E — 12 CFR Part 1005 (electronic fund transfers, error resolution) [verify subsection labels including §1005.11 procedures and §1005.18 prepaid].
- Reg Z — 12 CFR Part 1026 (Truth in Lending) [verify subsection labels].
- Test-plan conventions: error-resolution test plans under §1005.11 walk the timeline by sample (notice date, investigation start, provisional credit by day 10 or day 5 for new accounts [verify §1005.11(c) timing], final determination, customer notice); pass criterion is 100% of sampled disputes within the procedural clock; fail criterion is any sampled item outside the clock without escalation evidence. Disclosure-content tests compare the production disclosure to the regulatory model with a redline procedure.

### BSA/AML testing

- FFIEC BSA/AML Examination Manual (current edition) [verify last-revision date]. https://bsaaml.ffiec.gov/manual .
- 31 CFR Part 1010, 1020, 1022, 1023, 1024, 1025, 1026 (FinCEN AML rules by industry) [verify part references].
- Test-plan conventions: CIP plans cover new-account opening with the documented identification-and-verification step as the procedure; CDD/EDD plans cover the customer-due-diligence questionnaire and EDD enrichment evidence by sample; SAR-decision plans cover the case-management file from alert to disposition with timing checks against 31 CFR §1020.320 [verify subsection]. SAR content review is restricted to authorised reviewers; the plan names the access-control posture rather than restating SAR content.

### CFPB CMS exam-cycle test plans

- The CFPB CMS examination procedures embed testing-program review against the four CMS pillars (board and management oversight, compliance program, response to consumer complaints, compliance audit). The plan distinguishes substantive-rule tests from CMS-program tests; findings on the testing program itself feed the CMS rating distinct from substantive control findings.

## Sponsor-bank / bank-fintech-arrangement test plans

When the test addresses a bank-fintech partnership or a sponsor-bank deposit program, the plan carries:

- The **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date] frame: end-customer reconciliation testing, FBO subledger reconciliation, deposit-insurance representation review, and the fourth-party register all sit inside this frame.
- **Bank Service Company Act, 12 USC §1867(c)**: examiner-access posture for the vendor systems the firm relies on for evidence; the plan names reliance posture upfront.

## Audience and tone

A test plan drafted with an upcoming OCC, FRB, FDIC, or CFPB exam in mind reads heavier on criteria (more verbatim from the regulation, more detail on FFIEC manual sections), heavier on the population-definition narrative, and heavier on the reviewer-questions block where the cycle anticipates examiner attention. A test plan drafted for in-cycle program coverage reads operationally with the same criteria base.
