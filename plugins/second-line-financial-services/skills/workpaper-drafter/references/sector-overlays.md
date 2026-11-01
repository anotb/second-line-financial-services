# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — workpaper-drafter

Loaded when `scope.sector_overlay_set` includes `banking` or when the test addresses a banking regulator's rule. Does not replace `references/source-anchors.md`; supplements it with bank-specific workpaper conventions.

#### Workpaper conventions banking examiners expect

A bank consumer-compliance or operational-risk testing workpaper read by an OCC, FDIC, FRB, CFPB, or NYDFS examiner carries a few conventions beyond the AU-C 230 baseline:

- **Test plan reference is binding.** Examiners pull the test plan and the workpaper together. Silent drift between them reads as a methodology weakness. Document scope changes with pre-fieldwork sign-off references.
- **Reviewer-separation evidence is structural.** Bank exam findings repeatedly cite preparer-and-reviewer-as-same-role as a CMS finding. The workpaper sign-off block makes the separation obvious.
- **Population definition is restated, not assumed.** The workpaper restates how the population was defined (originations during period, accounts open during period, transactions executed during period), where it was extracted from, and the completeness check on the extract. Examiners walk this first when they pull the workpaper.
- **Evidence reliance on system-of-record extracts requires the extract date and an integrity check.** Extracts run at different dates produce different populations; the workpaper names the extract date, the run-by role, and what the preparer did to confirm extract completeness against an independent count.

#### Bank-supervisory anchors (load by reference; do not restate)

- **CFPB Compliance Management Review** examination procedures inside the **CFPB Supervision and Examination Manual** (current edition) [verify section labels for the testing-program component]. https://www.consumerfinance.gov/compliance/supervision-examinations/ .
- **FFIEC Consumer Compliance Rating System** (Federal Register, 80 Fed. Reg. 67428, November 2, 2015) [verify Federal Register citation]. https://www.federalregister.gov/documents/2015/11/02/2015-27738/ffiec-consumer-compliance-rating-system [verify URL].
- **OCC Comptroller's Handbook — Compliance Management Systems** [verify current edition and section labels]. https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/index-comptrollers-handbook.html .
- **SR 08-8 — Compliance Risk Management Programs and Oversight at Large Banking Organizations with Complex Compliance Profiles** (Federal Reserve, October 16, 2008) [verify section labels for testing-program documentation]. https://www.federalreserve.gov/boarddocs/srletters/2008/sr0808.htm .
- **OCC PPM 5310-3 — Bank Supervision Process** [verify exact PPM number and current effective date].
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for $50B+ covered banks; testing-program outputs feed the risk-governance framework and the board's third-line oversight [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-I/part-30 .

#### Bank-control-area workpaper notes

##### HMDA / Reg C testing

- Reg C — 12 CFR Part 1003. §1003.4 data points, §1003.5 disclosure and reporting [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1003 .
- FFIEC HMDA Filing Instructions Guide (current edition) [verify edition year]. https://www.ffiec.gov/hmda/guide.htm .
- Workpaper conventions: data-integrity tests reconcile LAR to the loan origination system extract by sample; the source criteria carry the data-point definition and the FFIEC field-validation logic. Sample design typically stratified by action-taken type and rate-spread reportability.

##### CRA testing

- CRA — 12 CFR Part 25 (OCC), Part 195 (former OTS, OCC), Part 228 (FRB Reg BB), Part 345 (FDIC) [verify current effective state given the 2023 final-rule litigation history]. https://www.federalreserve.gov/supervisionreg/regbbcg.htm .
- Workpaper conventions: lending-test workpapers carry the geography distribution, borrower-profile distribution, and product-mix distribution. Service-test and investment-test workpapers carry the qualified-investment register. Performance-context narrative is set out in the test plan, not invented in the workpaper.

##### Reg B / ECOA testing

- Reg B — 12 CFR Part 1002. §1002.4 general rules, §1002.6 rules concerning evaluation of applications, §1002.9 notifications, §1002.13 information for monitoring purposes [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1002 .
- Workpaper conventions: adverse-action notice-timing testing reconciles application date to notice date by sample; spousal-signature testing requires reading the underwriting file, not just the front-end application; demographic-firewall testing for monitoring information requires inspection of the production environment, not the test environment.

##### Reg DD, Reg E, Reg Z testing

- Reg DD — 12 CFR Part 1030 (TISA disclosures, account fees) [verify subsection labels].
- Reg E — 12 CFR Part 1005 (electronic fund transfers, error resolution) [verify subsection labels including §1005.11 procedures and §1005.18 prepaid].
- Reg Z — 12 CFR Part 1026 (Truth in Lending) [verify subsection labels].
- Workpaper conventions: error-resolution workpapers under Reg E §1005.11 walk the timeline by sample (notice date, investigation start, provisional credit, final determination, customer notice). Disclosure-content workpapers compare the production disclosure to the regulatory model with a redline and note any deviations.

##### BSA/AML testing

- FFIEC BSA/AML Examination Manual (current edition) [verify last-revision date]. https://bsaaml.ffiec.gov/manual .
- 31 CFR Part 1010, 1020, 1022, 1023, 1024, 1025, 1026 (FinCEN AML rules by industry) [verify part references].
- Workpaper conventions: CIP testing reconciles new-account opening packet to the documented identification and verification step; CDD/EDD testing reads the customer-due-diligence questionnaire and the EDD enrichment evidence; SAR-decision testing reviews the case-management file from alert to disposition with timing checks against 31 CFR §1020.320. SAR content review is restricted to authorised reviewers; the workpaper notes the access control on the underlying file rather than restating SAR content.

##### CFPB CMS exam-cycle workpapers

- The CFPB CMS examination procedures embed testing-program review. The workpaper reads against the four CMS pillars (board and management oversight, compliance program, response to consumer complaints, compliance audit). Findings on the testing program itself feed the CMS rating, distinct from substantive control findings.

#### Sponsor-bank / bank-fintech-arrangement testing

When the test addresses a bank-fintech partnership or a sponsor-bank deposit program, the workpaper carries:

- The **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date] frame: end-customer reconciliation testing, FBO subledger reconciliation, deposit-insurance representation review, and the fourth-party register all sit inside this frame.
- **Bank Service Company Act, 12 USC §1867(c)**: examiner-access posture for the vendor systems the firm relied on for evidence; cite when reliance evidence is from a bank service provider.
- **OCC, FDIC, FRB consent-order public materials** for sponsor-bank programs (cite by named order when public): used to anchor the regulatory expectation, not as a named-institution narrative.

#### Audience and tone

A workpaper drafted with an upcoming OCC, FRB, FDIC, or CFPB exam in mind reads heavier on criteria (more verbatim from the regulation, more detail on FFIEC manual sections), heavier on limitations (period coverage, scope exclusions, reliance on prior testing), and heavier on the population-definition narrative. A workpaper drafted for in-cycle internal QA reads operationally with the same evidence base.

## capital-markets

### Capital-markets sector overlay — workpaper-drafter

Loaded when `scope.sector_overlay_set` includes `capital-markets` or when the test addresses SEC, FINRA, NFA, or fund-board rules. Supplements `references/source-anchors.md`.

#### Workpaper conventions SEC and FINRA examiners expect

SEC Division of Examinations staff and FINRA examiners read CCO and supervisory-control testing workpapers against compliance-program rule frames rather than safety-and-soundness frames. Three conventions matter:

- **Annual review evidence carries the testing workpaper.** Investment Advisers Act Rule 206(4)-7 and Investment Company Act Rule 38a-1(a)(4) are written around an annual review; testing workpapers feed the annual review compendium. The workpaper restates the annual-review-period framing.
- **Supervisory testing is the FINRA 3120 / 3130 anchor.** Broker-dealer compliance testing workpapers feed the FINRA 3120 supervisory-controls report and the FINRA 3130 CEO certification. The workpaper identifies which 3120 testing area it covers and the certification cycle.
- **Recordkeeping evidence treatment is regulated.** SEC Rule 17a-4 and FINRA Rule 4511 govern format, retention, and accessibility of the records the workpaper relies on. The workpaper does not invent a recordkeeping convention; it relies on the firm's records-management posture and notes any deficiency in evidence accessibility as a control finding distinct from the substantive test.

#### Capital-markets-supervisory anchors (load by reference; do not restate)

- **Investment Advisers Act Rule 206(4)-7** — adviser compliance-program rule [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-7 .
- **Investment Company Act Rule 38a-1(a)(4)** — fund compliance-program rule, including service-provider compliance-program-adequacy assessment [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-270/section-270.38a-1 .
- **FINRA Rule 3110 — Supervision** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3110 .
- **FINRA Rule 3120 — Supervisory Control System** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3120 .
- **FINRA Rule 3130 — Annual Certification of Compliance and Supervisory Processes** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3130 .
- **SEC Rule 17a-4** — broker-dealer recordkeeping [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.17a-4 .
- **FINRA Rule 4511 — General Books and Records Requirements** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/4511 .
- **Investment Advisers Act Rule 206(4)-2 (Custody Rule)** [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-2 .
- **Investment Advisers Act Rule 206(4)-1 (Marketing Rule)** [verify subsection labels for advertisement testing]. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-1 .
- **17 CFR Part 248 (Reg S-P) as amended May 16, 2024** [verify exact compliance dates by entity type and size]. https://www.sec.gov/files/rules/final/2024/34-100155.pdf [verify URL].

#### Capital-markets-control-area workpaper notes

##### Adviser annual compliance review (206(4)-7)

- Workpaper conventions: annual-review testing covers each named compliance area in the firm's compliance manual; the workpaper aggregation reads observed deviation against the firm's compliance-policy tolerance and against the regulatory minimum where prescribed. The annual-review summary is itself a separate artifact (firm-side compliance report); the testing workpaper feeds it.

##### Fund compliance program (38a-1)

- Workpaper conventions: 38a-1(a)(4) requires the fund to obtain certification from each material service provider that they have adopted and implemented compliance policies reasonably designed to prevent violations of federal securities laws. Workpaper testing of service-provider adequacy reads service-provider attestation, on-site or remote diligence, and any examination findings the service provider has disclosed. Cross-link to `vendor-diligence` and `dora-register-builder` (where DORA also applies).

##### Supervisory testing (FINRA 3110 / 3120 / 3130)

- Workpaper conventions: supervisory testing is the firm-side compendium of FINRA-required testing. Each tested supervisory procedure ties to a 3110 or 3120 area. The workpaper aggregation feeds the 3120 annual report; the firm's CEO certification under 3130 is the downstream consumer.

##### Marketing rule (206(4)-1)

- Workpaper conventions: advertisement testing reads the disseminated advertisement (cited by ad ID and date), the supporting evidence for performance claims and case studies, the Marketing Rule disclosures, and the firm's review-and-approval evidence. Testimonial and endorsement testing covers compensation arrangements and required disclosures by sample.

##### Custody rule (206(4)-2)

- Workpaper conventions: custody testing reconciles client-account positions and transactions against qualified-custodian records by sample; surprise-examination evidence is referenced by ID, with the surprise-examiner's report carried as third-party-assurance evidence; sole authority over a private fund triggers audit-or-surprise-exam testing of the audit pathway.

##### Trade surveillance (best execution, market manipulation, manipulative-trading)

- Workpaper conventions: surveillance-alert testing reads alert disposition by sample, with the alert criteria, the case file, and the disposition rationale carried as evidence. Trade-reconstruction testing reads the order-execution timeline by sample with NMS or fixed-income market-data references.

#### Reg S-P safeguards testing

- Reg S-P (as amended May 16, 2024) imposes incident-response, customer-notification, and service-provider-oversight obligations on broker-dealers, advisers, and investment companies [verify exact compliance dates by entity type]. Workpaper conventions: customer-notification timing testing reads the incident timeline against the regulatory clock; service-provider-oversight testing reads diligence and ongoing-monitoring evidence per the rule's standards.

#### Audience and tone

A workpaper drafted with an upcoming SEC Division of Examinations exam in mind reads heavier on annual-review evidence, marketing-rule supporting evidence, and custody-rule reconciliations. A workpaper drafted for FINRA cycle exam preparation reads heavier on 3120 supervisory testing, 3110 supervisory-procedure design evidence, and Rule 4511 recordkeeping posture. A fund-board-facing workpaper reads heavier on 38a-1(a)(4) service-provider compliance-program-adequacy evidence with the fund-board reporting cycle as the deliverable consumer.

## insurance

### Insurance sector overlay — workpaper-drafter

Loaded when `scope.sector_overlay_set` includes `insurance` or when the test addresses NAIC, state DOI, or insurance-specific federal rules. Supplements `references/source-anchors.md`.

#### Workpaper conventions insurance examiners expect

State DOI market-conduct examiners and NAIC accreditation reviewers read insurer testing workpapers slightly differently from bank examiners. Two conventions matter most:

- **Statutory framework is the criterion, not the model.** State DOI examiners read against the state's adopted version of the NAIC model, not against the model itself. The workpaper cites the state-adopted citation (e.g., "N.Y. Ins. Law §X / 11 NYCRR §Y") with the NAIC model as a secondary reference. State-by-state adoption variance matters and the workpaper notes it where the test scope is multi-state.
- **Market-conduct sample design follows the NAIC Market Conduct Examiners Handbook** rather than AU-C 530 directly. The workpaper restates the sample-design rationale aligned to the Handbook's standards (file-review sample sizes, error-tolerance bands) and reconciles to AU-C 530 only where the firm's methodology has chosen it.

#### Insurance-supervisory anchors (load by reference; do not restate)

- **NAIC Annual Financial Reporting Model Regulation (Model Audit Rule, Model #205)** [verify section references]. ICFR-relevant testing documentation conventions and auditor-management coordination expectations. https://content.naic.org/cipr-topics/topic-naic-model-laws-and-regulations [verify URL].
- **NAIC Market Conduct Examiners Handbook** (current edition) [verify section labels]. https://content.naic.org/cmte_d_mceh.htm [verify URL].
- **NAIC Insurance Holding Company System Regulatory Act (Model #440) and Holding Company Model Regulation (Model #450)** [verify model numbers]. Form B and Form D filings carry workpaper-relevant disclosure for affiliated-vendor testing.
- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number]. ORSA Summary Report content is itself the subject of testing for material risk areas; the workpaper for ORSA-relevant testing references the ORSA section under review.
- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers** (December 4, 2023) [verify state-by-state adoption status]. AIS Program testing covers governance, risk management, validation, third-party AI accountability, monitoring, documentation, transparency, fairness. https://content.naic.org/sites/default/files/inline-files/2023-12-04%20Model%20Bulletin_Adopted_0.pdf [verify URL].

#### Insurance-control-area workpaper notes

##### Underwriting and pricing testing

- Workpaper conventions: rate-filing-versus-applied-rate reconciliation by sample; pricing model governance testing reads model-version-pin against the date of policy effective; underwriting-rule application testing reconciles applicant attributes against the rate manual or rule engine output.
- Predictive-model testing under state DOI bulletins (Colorado SB 21-169 implementing regulation [verify section], NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting [verify circular number]) reads against the bulletin's required testing artifacts (governance documentation, fairness testing, third-party-AI accountability evidence).

##### Claims handling testing

- Unfair Claims Settlement Practices Act state adoption [verify state citations], usually state-adopted versions of NAIC Model #900 [verify model number] or NAIC Model #902 [verify model number]. Testing reads acknowledgement timing, investigation timing, settlement timing, denial-letter content by sample.
- Workpaper conventions: claims-handling samples restate the acknowledgement-investigation-decision timeline by sample with state-statutory clocks; the criteria section cites the state-adopted statute, not the NAIC model.

##### Producer licensing and appointment testing

- Workpaper conventions: licensing-status reconciliation against the state DOI register (NIPR / SBS) by sample; appointment-status testing against the state DOI register; commission-payment testing against the licensed-and-appointed status as of transaction date.

##### Privacy and data-security testing

- NAIC Insurance Data Security Model Law (Model #668), §4.F third-party service-provider obligations [verify state-by-state adoption]. Testing reads cybersecurity-program governance, incident-response testing, third-party-vendor diligence and monitoring evidence.
- NY DFS 23 NYCRR Part 500 applies to NY-licensed insurers as Covered Entities; cyber overlay applies in addition to insurance overlay where the firm holds a NY license.
- HIPAA Security Rule applies where the insurer is a covered entity (health insurer, dental, vision); cyber and privacy overlays both load.

##### ORSA Summary Report testing

- Workpaper conventions: ORSA-relevant testing reads risk-identification, risk-assessment, risk-monitoring, and group capital-adequacy sections; sample-level evidence is by risk type rather than by transaction. The workpaper limitations section flags that the ORSA itself is a management report; the testing concludes on the underlying control effectiveness, not on ORSA content.

#### Multi-state and group-vs-entity scope

The workpaper is explicit about the legal entity under test and the states whose rules apply. A multi-state market-conduct test names primary state and concurrent states (where applicable under coordinated examinations). A group-level testing workpaper carries the holding-company structure and the parent-entity scope; the workpaper does not conclude on legal-entity ICFR for non-tested entities.

#### Audience and tone

A workpaper drafted with an upcoming state DOI market-conduct exam in mind reads heavier on state-statutory citations, sample-design rationale aligned to the NAIC Handbook, and limitations on the period and lines of business covered. A workpaper drafted for the NAIC AIS Program reads heavier on third-party-AI accountability, validation, and fairness-testing evidence per the model bulletin's adopted text in the firm's domiciliary state.

## payments-fintech

### Payments-fintech sector overlay — workpaper-drafter

Loaded when `scope.sector_overlay_set` includes `payments-fintech` or when the test addresses NACHA, sponsor-bank, money-transmitter, prepaid, or larger-participant rules. Supplements `references/source-anchors.md`.

#### Workpaper conventions for payments and fintech testing

Payments and fintech testing workpapers carry conventions that bank consumer-compliance testing does not always anticipate:

- **Sponsor-bank arrangements load two sector overlays.** The fintech program tests against payments-fintech rules; the sponsor-bank arrangement tests against banking rules (Bank Service Company Act, Joint Statement on Bank-Third-Party Deposit Programs, end-customer reconciliation, deposit-insurance representation). Both overlays load and the workpaper names which controls sit on which side.
- **Reg E error-resolution case files are themselves workpapers.** The case file the firm produces in the ordinary course is the testing artifact under §1005.11. Compliance-testing workpapers reading Reg E error-resolution sample case files for adherence to the procedure are reading workpapers-of-workpapers; cite by case ID and treat the case file as system-of-record evidence.
- **NACHA Operating Rules are paywalled.** Cite as "current edition; specific sections to be confirmed against the firm's licensed copy" rather than restating rule text in the workpaper. The criteria section names the rule citation; the firm's licensed copy is the source of truth.

#### Payments-fintech-supervisory anchors (load by reference; do not restate)

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. Operative for sponsor-bank programs.
- **Reg E — 12 CFR Part 1005**, especially §1005.6 (consumer liability), §1005.7 (initial disclosures), §1005.8 (change-in-terms), §1005.10 (preauthorized transfers), §1005.11 (error resolution), §1005.18 (prepaid accounts) [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1005 .
- **NACHA Operating Rules (current edition)** Third-Party Sender risk-management rules and ODFI obligations [verify rule citations against the firm's licensed copy]. https://www.nacha.org/ .
- **FinCEN MSB rules at 31 CFR Part 1022** and registration requirements at 31 CFR §1010.380 [verify subsection labels]. https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1022 .
- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (November 21, 2024) — subject to post-publication challenge and CFPB reconsideration since 2025; verify current operative status before relying on designation. https://www.consumerfinance.gov/compliance/supervisory-guidance/ .
- **State money-transmitter rules** (state by state) — testing workpapers carry the state-adopted statute citation, not the Money Transmission Modernization Act text [verify state citations].
- **OCC Bulletin 2008-12 — Risk Management Guidance on Payment Processors** [verify exact bulletin number] for bank-side processor-relationship testing.

#### Payments-fintech-control-area workpaper notes

##### Reg E error-resolution testing

- Workpaper conventions: §1005.11 procedures are tested by case sample. The workpaper reads notice date, investigation start, provisional credit (where applicable, by day 10 or day 5 for new accounts [verify §1005.11(c) timing]), final determination, customer notice, and any reversal-of-provisional-credit. The case file is treated as system-of-record evidence with reliance test note on completeness against the dispute-management system.
- Prepaid-account testing under §1005.18 carries additional disclosure-format and access-time provisions; the workpaper notes the prepaid-program subset of the population.

##### Sponsor-bank end-customer reconciliation testing

- Workpaper conventions: end-customer reconciliation testing reads the sponsor-bank FBO subledger against the fintech program's customer ledger by sample (or by full reconciliation if the program's volume is small). Reconciliation workpapers carry timing (daily, weekly, month-end), exception aging, and unmatched-balance treatment. The workpaper limitations section names the period covered; reconciliations rely on point-in-time extracts.
- Deposit-insurance representation review is a separate test; the workpaper reads the firm's customer-facing communications (account-opening, T&Cs, marketing) against FDIC pass-through-deposit-insurance requirements [verify FDIC citation].

##### NACHA Third-Party Sender testing

- Workpaper conventions: TPS testing reads risk-management evidence per the firm's licensed NACHA Rules copy, the ODFI agreement, the originator-due-diligence file by sample, the return-rate monitoring evidence, and the unauthorised-return investigation evidence. Cite the NACHA rule by edition and section without restating; rely on the firm's licensed copy.

##### BSA/AML for MSBs and fintechs

- Workpaper conventions: AML-program testing reads CIP, CDD, and EDD evidence per the FFIEC BSA/AML Examination Manual and 31 CFR Part 1022 [verify part references]. Suspicious-activity testing reviews case-management evidence with the same access-control posture as bank BSA testing (SAR content access restricted; the workpaper notes the access control without restating SAR content).

##### Larger-participant CFPB scope (where applicable)

- Workpaper conventions: where the firm is a CFPB larger participant for digital consumer payment applications, CMS-aligned testing applies (verify operative status of the November 2024 designation rule on the engagement date). The workpaper cites the larger-participant rule alongside the substantive rule under test.

#### Audience and tone

A workpaper drafted with an upcoming CFPB exam in mind reads heavier on UDAAP-relevant disclosures, error-resolution timing aggregation, and customer-impact framing. A workpaper drafted for a state money-transmitter exam reads heavier on the state-statute citation, the customer-funds protection (segregation, permissible investments) testing, and the surety-bond or net-worth status. A workpaper drafted for sponsor-bank governance reads heavier on the bank-side and fintech-side control split, with the bank service provider relationship explicit.
