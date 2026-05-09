# Banking sector overlay — control-sampling

Loaded when `scope.sector_overlay_set` includes `banking` or when the test addresses a banking-regulator rule. Does not replace `references/source-anchors.md`; supplements it with bank-specific population, stratification, and tolerable-rate conventions.

## Population definition conventions banking examiners expect

A bank consumer-compliance or operational-risk sampling memo read by an OCC, FDIC, FRB, CFPB, or NYDFS examiner carries conventions beyond the AU-C 530 baseline:

- **Populations are defined in items examiners can pull, not in source tables.** Originations during period (HMDA), accounts open during period (Reg DD), transactions executed during period (Reg E), error-resolution case files closed during period (Reg E §1005.11). Examiners walk the population definition first when they pull the sampling memo.
- **Population pulls carry the extract date and the run-by role.** Extracts run at different dates produce different populations. The memo names the extract date, the run-by role, and the reconciliation that supports the completeness assertion (LAR row count to the LOS originated-loan count within tolerance; deposit-account count to the daily new-account reporting feed; transaction count to the core-banking system control total).
- **Cut-off treatment is explicit.** Reg DD account-opening tests use account-opened-date cut-off; Reg E error-resolution tests use case-closed-date cut-off; HMDA tests use action-taken-date cut-off mapped to the FFIEC reporting-year boundary.

## Bank-supervisory anchors (load by reference; do not restate)

- **CFPB Compliance Management Review** examination procedures inside the **CFPB Supervision and Examination Manual** (current edition) [verify section labels for the testing-program component]. https://www.consumerfinance.gov/compliance/supervision-examinations/ .
- **OCC Comptroller's Handbook — Compliance Management Systems** [verify current edition and section labels]. https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/index-comptrollers-handbook.html .
- **OCC PPM 5310-3 — Bank Supervision Process** [verify exact PPM number and current effective date].
- **SR 08-8 — Compliance Risk Management Programs and Oversight at Large Banking Organizations with Complex Compliance Profiles** (Federal Reserve, October 16, 2008) [verify section labels for testing-program scope and population coverage]. https://www.federalreserve.gov/boarddocs/srletters/2008/sr0808.htm .
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for $50B+ covered banks; the testing program's sample-design discipline feeds the risk-governance framework and the board's third-line oversight [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-I/part-30 .

## Bank-control-area sampling notes

### HMDA / Reg C testing

- Reg C — 12 CFR Part 1003. §1003.4 data points, §1003.5 disclosure and reporting [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1003 .
- FFIEC HMDA Filing Instructions Guide (current edition) [verify edition year]. https://www.ffiec.gov/hmda/guide.htm .
- Sampling conventions: stratify by action-taken type (originated, approved-not-accepted, denied, withdrawn, incomplete, file-closed-for-incompleteness, purchased) and by rate-spread reportability. Statistical attribute samples typical at 95% confidence with tolerable rates set per firm methodology, often referencing the FFIEC HMDA re-submission thresholds as a benchmark for material data-integrity defects [verify FFIEC HMDA re-submission threshold guidance edition]. For the demographic firewall (Reg C §1003.4(a)(10)) the population is the system-access entitlement extract for the production environment; sample design follows the cyber overlay's IAM conventions.

### CRA testing

- CRA — 12 CFR Part 25 (OCC), Part 195 (former OTS, OCC), Part 228 (FRB Reg BB), Part 345 (FDIC) [verify current effective state given the 2023 final-rule litigation history]. https://www.federalreserve.gov/supervisionreg/regbbcg.htm .
- Sampling conventions: lending-test samples stratify by geography (assessment area, low- and moderate-income geography), borrower profile (LMI borrower), and product mix. Service-test and investment-test samples size against the qualified-investment register.

### Reg B / ECOA testing

- Reg B — 12 CFR Part 1002. §1002.4 general rules, §1002.6 evaluation, §1002.9 notifications, §1002.13 monitoring information [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1002 .
- Sampling conventions: adverse-action-notice-timing tests sample by application-decision date with stratification by product (mortgage, auto, credit card, small business), channel, and decisioning system. Spousal-signature tests sample by underwriting file with stratification by product and joint-account flag. Demographic-firewall tests sample monitoring-information access against the entitlement extract.

### Reg DD, Reg E, Reg Z testing

- Reg DD — 12 CFR Part 1030 (TISA disclosures, account fees) [verify subsection labels].
- Reg E — 12 CFR Part 1005 (electronic fund transfers, error resolution) [verify subsection labels including §1005.11 procedures and §1005.18 prepaid].
- Reg Z — 12 CFR Part 1026 (Truth in Lending) [verify subsection labels].
- Sampling conventions for error-resolution under Reg E §1005.11: population is case files closed in the period, stratified by transaction type (debit-card unauthorised, ACH error, prepaid, ATM), by case outcome (provisional credit issued, denied, reversed), and by case-aging (within 10 business days, 11-45 business days). Disclosure-content tests sample disclosure-delivery events with stratification by channel (in-branch, online, mobile, mail) and product subset.

### BSA/AML testing

- FFIEC BSA/AML Examination Manual (current edition) [verify last-revision date]. https://bsaaml.ffiec.gov/manual .
- 31 CFR Part 1010, 1020, 1022, 1023, 1024, 1025, 1026 (FinCEN AML rules by industry) [verify part references].
- Sampling conventions: CIP testing samples new-account-opening packets with stratification by channel (in-branch, online, third-party-introduced) and customer type (consumer, business, non-resident-alien). CDD/EDD testing samples customer profiles with stratification by customer risk tier (low, medium, high, prohibited). SAR-decision testing samples case files from the alert population with stratification by alert source (transaction monitoring, manual referral, regulator inquiry) and by alert disposition. Sanctions-screening tests typically carry a zero-tolerable rate for actual hits and a near-zero tolerable rate for false-negative testing on calibrated control sets.

### CFPB CMS exam-cycle sampling

- The CFPB CMS examination procedures embed testing-program review. Sampling-memo discipline matters for the CMS rating distinct from substantive control findings; a weak sampling memo is a CMS finding regardless of whether the control under test passed.

## Sponsor-bank / bank-fintech-arrangement sampling

When the test addresses a bank-fintech partnership or a sponsor-bank deposit program, the sampling memo carries:

- The **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date] frame: end-customer reconciliation populations are defined at the FBO subledger level with stratification by program (where the bank sponsors multiple fintech programs) and by reconciliation status (matched, unmatched-aged, unmatched-current). Deposit-insurance representation tests sample customer-facing communications with stratification by channel.
- **Bank Service Company Act, 12 USC §1867(c)**: examiner-access posture for the vendor systems the firm sampled from; cite when the population pull rests on a bank service provider.
- **U.S. Interagency Guidance on Third-Party Relationships: Risk Management** (FDIC / OCC / FRB, June 2023) [verify Federal Register citation]: ongoing-monitoring sampling cadence and the population coverage expectation for sponsor-bank programs.

## Audience and tone

A sampling memo drafted with an upcoming OCC, FRB, FDIC, or CFPB exam in mind reads heavier on population-completeness narrative, the criterion source for the tolerable rate, and the stratification rationale (more detail on the FFIEC manual sections that drive segment-specific risk weighting). A memo drafted for in-cycle internal QA reads operationally with the same evidence base. CFPB CMS-aligned reads carry the consumer-compliance-rating frame as a context signal for tolerable-rate setting.
