# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — control-sampling

Loaded when `scope.sector_overlay_set` includes `banking` or when the test addresses a banking-regulator rule. Does not replace `references/source-anchors.md`; supplements it with bank-specific population, stratification, and tolerable-rate conventions.

#### Population definition conventions banking examiners expect

A bank consumer-compliance or operational-risk sampling memo read by an OCC, FDIC, FRB, CFPB, or NYDFS examiner carries conventions beyond the AU-C 530 baseline:

- **Populations are defined in items examiners can pull, not in source tables.** Originations during period (HMDA), accounts open during period (Reg DD), transactions executed during period (Reg E), error-resolution case files closed during period (Reg E §1005.11). Examiners walk the population definition first when they pull the sampling memo.
- **Population pulls carry the extract date and the run-by role.** Extracts run at different dates produce different populations. The memo names the extract date, the run-by role, and the reconciliation that supports the completeness assertion (LAR row count to the LOS originated-loan count within tolerance; deposit-account count to the daily new-account reporting feed; transaction count to the core-banking system control total).
- **Cut-off treatment is explicit.** Reg DD account-opening tests use account-opened-date cut-off; Reg E error-resolution tests use case-closed-date cut-off; HMDA tests use action-taken-date cut-off mapped to the FFIEC reporting-year boundary.

#### Bank-supervisory anchors (load by reference; do not restate)

- **CFPB Compliance Management Review** examination procedures inside the **CFPB Supervision and Examination Manual** (current edition) [verify section labels for the testing-program component]. https://www.consumerfinance.gov/compliance/supervision-examinations/ .
- **OCC Comptroller's Handbook — Compliance Management Systems** [verify current edition and section labels]. https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/index-comptrollers-handbook.html .
- **OCC PPM 5310-3 — Bank Supervision Process** [verify exact PPM number and current effective date].
- **SR 08-8 — Compliance Risk Management Programs and Oversight at Large Banking Organizations with Complex Compliance Profiles** (Federal Reserve, October 16, 2008) [verify section labels for testing-program scope and population coverage]. https://www.federalreserve.gov/boarddocs/srletters/2008/sr0808.htm .
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for $50B+ covered banks; the testing program's sample-design discipline feeds the risk-governance framework and the board's third-line oversight [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-I/part-30 .

#### Bank-control-area sampling notes

##### HMDA / Reg C testing

- Reg C — 12 CFR Part 1003. §1003.4 data points, §1003.5 disclosure and reporting [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1003 .
- FFIEC HMDA Filing Instructions Guide (current edition) [verify edition year]. https://www.ffiec.gov/hmda/guide.htm .
- Sampling conventions: stratify by action-taken type (originated, approved-not-accepted, denied, withdrawn, incomplete, file-closed-for-incompleteness, purchased) and by rate-spread reportability. Statistical attribute samples typical at 95% confidence with tolerable rates set per firm methodology, often referencing the FFIEC HMDA re-submission thresholds as a benchmark for material data-integrity defects [verify FFIEC HMDA re-submission threshold guidance edition]. For the demographic firewall (Reg C §1003.4(a)(10)) the population is the system-access entitlement extract for the production environment; sample design follows the cyber overlay's IAM conventions.

##### CRA testing

- CRA — 12 CFR Part 25 (OCC), Part 195 (former OTS, OCC), Part 228 (FRB Reg BB), Part 345 (FDIC) [verify current effective state given the 2023 final-rule litigation history]. https://www.federalreserve.gov/supervisionreg/regbbcg.htm .
- Sampling conventions: lending-test samples stratify by geography (assessment area, low- and moderate-income geography), borrower profile (LMI borrower), and product mix. Service-test and investment-test samples size against the qualified-investment register.

##### Reg B / ECOA testing

- Reg B — 12 CFR Part 1002. §1002.4 general rules, §1002.6 evaluation, §1002.9 notifications, §1002.13 monitoring information [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1002 .
- Sampling conventions: adverse-action-notice-timing tests sample by application-decision date with stratification by product (mortgage, auto, credit card, small business), channel, and decisioning system. Spousal-signature tests sample by underwriting file with stratification by product and joint-account flag. Demographic-firewall tests sample monitoring-information access against the entitlement extract.

##### Reg DD, Reg E, Reg Z testing

- Reg DD — 12 CFR Part 1030 (TISA disclosures, account fees) [verify subsection labels].
- Reg E — 12 CFR Part 1005 (electronic fund transfers, error resolution) [verify subsection labels including §1005.11 procedures and §1005.18 prepaid].
- Reg Z — 12 CFR Part 1026 (Truth in Lending) [verify subsection labels].
- Sampling conventions for error-resolution under Reg E §1005.11: population is case files closed in the period, stratified by transaction type (debit-card unauthorised, ACH error, prepaid, ATM), by case outcome (provisional credit issued, denied, reversed), and by case-aging (within 10 business days, 11-45 business days). Disclosure-content tests sample disclosure-delivery events with stratification by channel (in-branch, online, mobile, mail) and product subset.

##### BSA/AML testing

- FFIEC BSA/AML Examination Manual (current edition) [verify last-revision date]. https://bsaaml.ffiec.gov/manual .
- 31 CFR Part 1010, 1020, 1022, 1023, 1024, 1025, 1026 (FinCEN AML rules by industry) [verify part references].
- Sampling conventions: CIP testing samples new-account-opening packets with stratification by channel (in-branch, online, third-party-introduced) and customer type (consumer, business, non-resident-alien). CDD/EDD testing samples customer profiles with stratification by customer risk tier (low, medium, high, prohibited). SAR-decision testing samples case files from the alert population with stratification by alert source (transaction monitoring, manual referral, regulator inquiry) and by alert disposition. Sanctions-screening tests typically carry a zero-tolerable rate for actual hits and a near-zero tolerable rate for false-negative testing on calibrated control sets.

##### CFPB CMS exam-cycle sampling

- The CFPB CMS examination procedures embed testing-program review. Sampling-memo discipline matters for the CMS rating distinct from substantive control findings; a weak sampling memo is a CMS finding regardless of whether the control under test passed.

#### Sponsor-bank / bank-fintech-arrangement sampling

When the test addresses a bank-fintech partnership or a sponsor-bank deposit program, the sampling memo carries:

- The **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date] frame: end-customer reconciliation populations are defined at the FBO subledger level with stratification by program (where the bank sponsors multiple fintech programs) and by reconciliation status (matched, unmatched-aged, unmatched-current). Deposit-insurance representation tests sample customer-facing communications with stratification by channel.
- **Bank Service Company Act, 12 USC §1867(c)**: examiner-access posture for the vendor systems the firm sampled from; cite when the population pull rests on a bank service provider.
- **U.S. Interagency Guidance on Third-Party Relationships: Risk Management** (FDIC / OCC / FRB, June 2023) [verify Federal Register citation]: ongoing-monitoring sampling cadence and the population coverage expectation for sponsor-bank programs.

#### Audience and tone

A sampling memo drafted with an upcoming OCC, FRB, FDIC, or CFPB exam in mind reads heavier on population-completeness narrative, the criterion source for the tolerable rate, and the stratification rationale (more detail on the FFIEC manual sections that drive segment-specific risk weighting). A memo drafted for in-cycle internal QA reads operationally with the same evidence base. CFPB CMS-aligned reads carry the consumer-compliance-rating frame as a context signal for tolerable-rate setting.

## capital-markets

### Capital-markets sector overlay — control-sampling

Loaded when `scope.sector_overlay_set` includes `capital-markets` or when the test addresses FINRA, SEC, MSRB, or CFTC rules for broker-dealers, investment advisers, registered funds, or futures commission merchants. Supplements `references/source-anchors.md` with capital-markets-specific population, stratification, and tolerable-rate conventions.

#### Population definition conventions capital-markets examiners expect

FINRA examiners, SEC OCIE/EXAMS reviewers, and adviser internal auditors carry conventions beyond the general sampling baseline:

- **Populations are defined by trading-day, account-day, or transaction-event.** Trades executed during period (broker-dealer best execution, suitability, Reg BI), accounts open during period (KYC, suitability profile freshness), customer communications sent during period (FINRA Rule 2210 communications), supervisory reviews completed during period (FINRA Rule 3110).
- **Recordkeeping populations under SEC 17a-4 / FINRA 4511 are large.** The memo defines the population in items the sample can draw from (records subject to a particular retention requirement) and reconciles to the books-and-records system control totals. WORM-storage populations carry the storage-system extract as the source of truth.
- **Adviser populations under Advisers Act Rule 206(4)-7 follow the firm's annual-review scope.** The annual review's risk-prioritisation drives the populations the sample targets across the year.

#### Capital-markets-supervisory anchors (load by reference; do not restate)

- **FINRA Rule 3120 — Supervisory Control System** [verify subsection labels]. The annual-report-on-supervisory-controls testing sits inside this frame. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3120 .
- **FINRA Rule 3130 — Annual Certification of Compliance and Supervisory Processes** [verify subsection labels]. CEO certification supported by CCO testing of supervisory processes; sampling-memo discipline drives the CCO's certification basis. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3130 .
- **FINRA Rule 3110 — Supervision** [verify subsection labels for required tests and verifications]. Supervisory-reviews populations sit here. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3110 .
- **FINRA Rule 2111 — Suitability** and **SEC Regulation Best Interest (17 CFR §240.15l-1)** [verify subsection labels for the Care, Conflict, Disclosure, and Compliance Obligations]. Suitability and Reg BI sampling pulls recommendations and customer profiles. https://www.finra.org/rules-guidance/rulebooks/finra-rules/2111 ; https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.15l-1 .
- **SEC Rule 17a-4 (17 CFR §240.17a-4)** and **FINRA Rule 4511 — General Requirements (Books and Records)** [verify subsection labels]. Recordkeeping populations and retention requirements drive the population-completeness basis for capital-markets sampling. https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.17a-4 ; https://www.finra.org/rules-guidance/rulebooks/finra-rules/4511 .
- **Investment Advisers Act Rule 206(4)-7** [verify subsection labels for the annual-review documentation expectation and the testing-program component]. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-7 .
- **SEC Rule 38a-1 (17 CFR §270.38a-1)** for registered investment companies — fund compliance program rule [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-270/section-270.38a-1 .

#### Capital-markets-control-area sampling notes

##### Suitability and Reg BI testing

- Sampling conventions: suitability and Reg BI testing samples recommendations made in the period with stratification by product complexity (mutual fund, ETF, structured product, options, alternative, fixed income), customer type (retail, institutional, accredited, high-net-worth), and registered representative experience. Care Obligation testing reads the recommendation against the customer profile; Conflict and Disclosure Obligation testing reads the supervisory documentation. Tolerable rates for high-complexity-with-retail-customer combinations are typically lower than firm baseline because customer-impact framing concentrates risk.

##### Trade-execution and best-execution testing

- Sampling conventions: best-execution testing samples trades executed in the period with stratification by venue, order type (market, limit, marketable limit), security type, and trade size. The population is trades subject to best-execution review per the firm's policy; the source of truth is the order-management or execution-management system extract.

##### Books-and-records testing

- Sampling conventions: 17a-4 / 4511 testing samples records subject to specific retention requirements with stratification by record category. WORM-storage testing reads the storage-system extract by sample with reperformance against the retention metadata. Tolerable rates for WORM-failure populations are typically zero per firm policy because the regulatory consequence is absolute.

##### Supervisory-review testing (3110)

- Sampling conventions: supervisory-review testing samples reviews completed in the period with stratification by review type (electronic communication review, trade exception review, customer-account review), reviewing principal, and reviewed-population subset. The population is reviews-the-firm-was-required-to-perform per the firm's WSPs; missing-review tests use the inverse population.

##### Communications-with-public testing (2210)

- Sampling conventions: 2210 testing samples communications sent in the period with stratification by communication type (retail, correspondence, institutional), distribution channel, and pre-use-approval status. Pre-use-approved communications carry a different population from filed-with-FINRA communications.

##### Adviser annual-review (206(4)-7) testing

- Sampling conventions: the annual-review scope dictates which control populations are sampled across the year. Custody-rule (Rule 206(4)-2) testing samples client accounts with stratification by custodian, account type, and asset count. Books-and-records testing under Rule 204-2 mirrors the broker-dealer 17a-4 conventions.

##### Fund 38a-1 testing

- Sampling conventions: fund compliance-program testing samples board reports, sub-adviser oversight evidence, valuation determinations, and proxy-voting records by sample. The population follows the fund's compliance-program scope under Rule 38a-1 [verify subsection].

#### Audience and tone

A sampling memo drafted with an upcoming FINRA examination in mind reads heavier on the FINRA rule citations, the supervisory-control frame (3120/3130), and the WSP-derived population definitions. A memo drafted with an upcoming SEC EXAMS visit in mind reads heavier on the Rule 206(4)-7 annual-review frame, the books-and-records retention matrices, and the customer-impact framing for retail products. A memo drafted for fund-board reporting reads heavier on the 38a-1 compliance-program frame and the custodian-by-custodian breakdown for custody-rule testing.

## insurance

### Insurance sector overlay — control-sampling

Loaded when `scope.sector_overlay_set` includes `insurance` or when the test addresses NAIC or state-DOI rules. Supplements `references/source-anchors.md` with insurance-specific population, stratification, and tolerable-rate conventions.

#### Population definition conventions insurance examiners expect

State DOI market-conduct examiners and NAIC-aligned internal auditors carry conventions beyond the general sampling baseline:

- **Populations are defined by transaction type and policy line.** Claims handled in the period (closed-without-payment, closed-with-payment, denied, reopened); underwriting decisions issued in the period (new business, renewal, declination, non-renewal, cancellation); complaints received in the period (DOI-routed, direct-to-carrier); policy forms in force during the period.
- **Multi-state populations stratify by state.** State-by-state variance in adopted statutes (UTPA, UCSPA, claims-handling clocks) drives stratification. Multi-state samples carry per-state buckets so per-state findings do not get lost in an aggregate read.
- **Population pulls reconcile to the policy administration system or claims management system control totals.** The memo names the system, the extract date, the cut-off treatment (claim-closed-date, policy-effective-date, complaint-received-date), and the reconciliation result.

#### Insurance-supervisory anchors (load by reference; do not restate)

- **NAIC Annual Financial Reporting Model Regulation (Model Audit Rule, Model #205)** [verify section references for ICFR-relevant sampling conventions and adoption status by state]. https://content.naic.org/cipr-topics/topic-naic-model-laws-and-regulations [verify URL].
- **NAIC Market Conduct Examiners Handbook** (current edition) [verify section labels for the standardised data calls, sampling conventions, and tolerable-rate conventions on claims, underwriting, complaint, and policy-form populations]. https://content.naic.org/cmte_d_mceh.htm [verify URL].
- **NAIC Unfair Trade Practices Act (Model #880)** and **Unfair Claims Settlement Practices Act (Model #900)** [verify model numbers and state-by-state adoption]. State-adopted versions carry the operative statutory citation.
- **NAIC Corporate Governance Annual Disclosure Model Act (Model #305)** and **Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model numbers and adoption status]. ORSA-relevant testing samples carry the risk-assessment-driven scope from the firm's ORSA filing.

#### Insurance-control-area sampling notes

##### Claims-handling testing

- Sampling conventions: claims-handling testing samples closed claims with stratification by claim type (auto bodily injury, auto property damage, homeowners, commercial liability, life, health, workers' comp), claim outcome (paid, denied, closed-without-payment, reopened), claim severity (by reserve at close), and claim aging (within 30 days, 31-90 days, over 90 days). State-statutory clock tests (acknowledgement within X days, decision within Y days, payment within Z days) sample by claim-state and apply the state-specific tolerable rate. Tolerable rates for unfair-claims-settlement-practices populations are typically zero or near-zero in firm methodology because the regulatory frame is enforcement-oriented.

##### Underwriting testing

- Sampling conventions: underwriting samples new-business and renewal decisions with stratification by product line, distribution channel (agent, broker, direct, MGA), state, and decision outcome. Rating-accuracy tests sample issued policies with stratification by rating territory, product, and rate-revision wave. Disparate-treatment testing under state-adopted ECOA-equivalents (where applicable) follows fair-lending stratification conventions.

##### Complaint-handling testing

- Sampling conventions: complaint testing samples received complaints with stratification by complaint source (DOI-routed, direct-to-carrier, social-media-escalation), complaint type (claim, underwriting, billing, sales-practices), and resolution status. DOI-routed complaints typically carry a separate read because the DOI-response timing is a regulator-facing population with a state-specific clock.

##### Policy-form testing

- Sampling conventions: policy-form-content testing samples policies issued in the period with stratification by product and state. Form-filing-status tests reconcile the policy-form library against the state-filed-form register; the population is forms in force during the period and stratification is by state.

##### Producer-licensing testing

- Sampling conventions: producer-licensing testing samples policies sold in the period with stratification by producer state, producer type (individual, agency), and product. The control population is policies-with-an-unlicensed-producer-event; tolerable rate is typically zero per state law.

#### ORSA-aligned sampling

When the test sits inside the ORSA risk-assessment scope:

- Population definition follows the ORSA-identified risk register; sampling targets controls mitigating the highest-rated risks per the ORSA filing. The memo references the ORSA filing year and the firm's risk-rating methodology.
- Tolerable rates for ORSA-relevant controls draw from firm methodology calibrated against the ORSA-identified risk appetite; the criterion source names the ORSA filing as well as the firm methodology.

#### Audience and tone

A sampling memo drafted with an upcoming state DOI market-conduct examination in mind reads heavier on the state-statutory clock citations, the per-state stratification rationale, and the standardised-data-call alignment from the NAIC Market Conduct Examiners Handbook. A memo drafted for the firm's actuarial or financial reporting context (Model #205-relevant) reads heavier on the ICFR-control-effectiveness frame. ORSA-aligned reads carry the risk-rating context as a stratification driver.

## payments-fintech

### Payments-fintech sector overlay — control-sampling

Loaded when `scope.sector_overlay_set` includes `payments-fintech` or when the test addresses NACHA, sponsor-bank, money-transmitter, prepaid, or larger-participant rules. Supplements `references/source-anchors.md` with payments-fintech-specific population, stratification, and tolerable-rate conventions.

#### Population definition conventions payments and fintech examiners expect

Payments and fintech testing populations carry conventions that bank consumer-compliance testing does not always anticipate:

- **Sponsor-bank arrangements load two sector overlays.** The fintech program tests against payments-fintech rules; the sponsor-bank arrangement tests against banking rules (Bank Service Company Act, Joint Statement on Bank-Third-Party Deposit Programs, end-customer reconciliation). Both overlays load and the sampling memo names which controls sit on which side, with separate populations where the controls are separable.
- **Reg E error-resolution case files are themselves the population.** Under §1005.11, the case file the firm produces in the ordinary course is the testing target; the population is case files closed in the period, stratified by case type and outcome.
- **NACHA-relevant populations include returns, originated entries, and exception cases.** Third-Party Sender testing samples ODFI-relationship evidence, originator due diligence files, return-rate monitoring evidence, and unauthorised-return investigation cases.
- **State money-transmitter testing carries per-state populations.** Customer-funds protection testing (segregation, permissible investments) samples by state-licensed entity and state.

#### Payments-fintech-supervisory anchors (load by reference; do not restate)

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. Operative for sponsor-bank programs.
- **U.S. Interagency Guidance on Third-Party Relationships: Risk Management** (FDIC / OCC / FRB, June 2023) [verify exact title and Federal Register citation]. Ongoing-monitoring sampling cadence and the population coverage expectation for sponsor-bank programs.
- **Reg E — 12 CFR Part 1005**, especially §1005.6 (consumer liability), §1005.7 (initial disclosures), §1005.8 (change-in-terms), §1005.10 (preauthorized transfers), §1005.11 (error resolution), §1005.18 (prepaid accounts) [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1005 .
- **Reg Z — 12 CFR Part 1026** billing-error procedures (§1026.13 for open-end credit) [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1026 .
- **NACHA Operating Rules (current edition)** Third-Party Sender risk-management rules and ODFI obligations [verify rule citations against the firm's licensed copy]. https://www.nacha.org/ .
- **FinCEN MSB rules at 31 CFR Part 1022** and registration requirements at 31 CFR §1010.380 [verify subsection labels]. https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1022 .
- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (November 21, 2024) — subject to post-publication challenge and CFPB reconsideration since 2025; verify current operative status before relying on designation. https://www.consumerfinance.gov/compliance/supervisory-guidance/ .
- **State money-transmitter rules** (state by state) — sampling memos carry the state-adopted statute citation, not the Money Transmission Modernization Act text [verify state citations].

#### Payments-fintech-control-area sampling notes

##### Reg E error-resolution sampling

- Sampling conventions: §1005.11 sampling pulls case files closed in the period with stratification by transaction type (debit-card unauthorised, ACH error, prepaid, ATM, P2P), case outcome (provisional credit issued, denied, reversed), case-aging (within 10 business days, 11-45 business days, beyond 45 days), and customer type (consumer, prepaid-account holder, business). Day-10 / day-5 provisional-credit timing under §1005.11(c) [verify timing] drives a separate stratum where the firm's policy clock is tighter than the regulatory minimum. Prepaid testing under §1005.18 carries additional disclosure-format and access-time testing populations.

##### Sponsor-bank end-customer reconciliation sampling

- Sampling conventions: end-customer reconciliation testing population is FBO subledger entries during the period with stratification by program (where the bank sponsors multiple fintech programs), reconciliation status (matched, unmatched-aged, unmatched-current), and entry type (deposit, withdrawal, fee, internal-transfer). Tolerable rates for unmatched-aged populations are typically zero or near-zero per firm methodology because customer-funds-segregation expectations are absolute.
- Deposit-insurance representation testing samples customer-facing communications (account-opening, T&Cs, marketing) with stratification by channel and program; the population is communications sent in the period.

##### NACHA Third-Party Sender sampling

- Sampling conventions: TPS testing samples ODFI-relationship evidence, originator due diligence files, return-rate monitoring evidence, and unauthorised-return investigation files. Stratification by originator, by return-code category, and by aging. Cite the NACHA rule by edition and section without restating; rely on the firm's licensed copy.

##### BSA/AML for MSBs and fintechs

- Sampling conventions: AML-program testing samples CIP, CDD, and EDD evidence per the FFIEC BSA/AML Examination Manual and 31 CFR Part 1022 [verify part references]. Stratification by customer risk tier, by onboarding channel, and by product. Suspicious-activity testing samples case-management files with the same access-control posture as bank BSA testing (SAR content access restricted; the memo names the access control without restating SAR content).

##### Money-transmitter customer-funds-protection testing

- Sampling conventions: customer-funds-protection testing samples permissible-investment positions and segregated-account balances against state-license obligations. The population is segregation positions held during the period; stratification by state and by investment type. Tolerable rates are typically zero per state law because the regulatory consequence is the license itself.

##### Larger-participant CFPB scope (where applicable)

- Sampling conventions: where the firm is a CFPB larger participant for digital consumer payment applications, CMS-aligned testing applies (verify operative status of the November 2024 designation rule on the engagement date). Sampling memos cite the larger-participant rule alongside the substantive rule under test, and the population definitions follow the digital-payment-application transaction set.

#### Audience and tone

A sampling memo drafted with an upcoming CFPB exam in mind reads heavier on UDAAP-relevant populations (disclosures, error-resolution, customer-impact framing in stratification), and the customer-impact-driven tolerable-rate setting for consumer-facing populations. A memo drafted for a state money-transmitter exam reads heavier on the state-statutory citations, the per-state customer-funds-protection populations, and the surety-bond or net-worth status as context. A memo drafted for sponsor-bank governance reads heavier on the bank-side and fintech-side population split, with the bank service provider relationship explicit in the source-of-truth narrative.
