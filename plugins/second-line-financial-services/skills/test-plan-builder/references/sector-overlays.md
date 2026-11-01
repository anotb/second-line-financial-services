# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — test-plan-builder

Loaded when `scope.sector_overlay_set` includes `banking` or when the test addresses a banking regulator's rule. Does not replace `references/source-anchors.md`; supplements it with bank-specific test-plan conventions.

#### Test-plan conventions banking examiners expect

A bank consumer-compliance or operational-risk test plan that an OCC, FDIC, FRB, CFPB, or NYDFS examiner will later read at exam carries a few conventions beyond the IIA / AU-C 300 baseline:

- **Risk-based prioritization is named, not assumed.** Bank-supervisory expectations on the testing program (under SR 08-8 [verify section] and the OCC CMS handbook [verify section]) are that the test plan ties scope to a risk-based rationale rather than a calendar habit. The plan restates the risk read (customer impact, financial impact, regulatory impact, prior-cycle history) that produced this cycle's scope.
- **Pre-fieldwork sign-off is a hard gate.** Examiners pull the test plan and the workpaper together. A test plan signed after evidence pulls began reads as a methodology weakness; the plan's reviewer-signoff date should precede the evidence-request fielding date.
- **Test plan and workpaper are the same contract.** Silent drift between executed procedures and planned procedures is a CMS finding; the plan documents what gets done so the workpaper later either matches or names the divergence with sign-off.
- **Population definition is restated, not inherited.** The plan restates how the population is defined (originations during the period, accounts open during the period, transactions executed, packets due), where the extract comes from, and the completeness check the workpaper will run against the extract. Examiners walk this first when they pull the workpaper.
- **Reviewer separation is structural.** Bank exam findings repeatedly cite preparer-and-reviewer-as-same-role as a CMS finding. The plan's sign-off block makes the separation obvious from planning time.

#### Bank-supervisory anchors (load by reference; do not restate)

- **CFPB Compliance Management Review** examination procedures inside the **CFPB Supervision and Examination Manual** (current edition) [verify section labels for the testing-program component]. https://www.consumerfinance.gov/compliance/supervision-examinations/ .
- **FFIEC Consumer Compliance Rating System** (Federal Register, 80 Fed. Reg. 67428, November 2, 2015) [verify Federal Register citation]. https://www.federalregister.gov/documents/2015/11/02/2015-27738/ffiec-consumer-compliance-rating-system [verify URL].
- **OCC Comptroller's Handbook — Compliance Management Systems** [verify current edition and section labels]. https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/index-comptrollers-handbook.html .
- **SR 08-8 — Compliance Risk Management Programs and Oversight at Large Banking Organizations with Complex Compliance Profiles** (Federal Reserve, October 16, 2008) [verify section labels for the testing-program planning expectations]. https://www.federalreserve.gov/boarddocs/srletters/2008/sr0808.htm .
- **OCC PPM 5310-3 — Bank Supervision Process** [verify exact PPM number and current effective date].
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for $50B+ covered banks [verify asset threshold and subsection labels]. The plan's risk-based-prioritization rationale and the reviewer-separation discipline both feed the heightened-standards posture. https://www.ecfr.gov/current/title-12/chapter-I/part-30 .

#### Bank-control-area test-plan notes

##### HMDA / Reg C testing

- Reg C — 12 CFR Part 1003. §1003.4 data points, §1003.5 disclosure and reporting [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1003 .
- FFIEC HMDA Filing Instructions Guide (current edition) [verify edition year]. https://www.ffiec.gov/hmda/guide.htm .
- Test-plan conventions: criteria section names the data-point definitions per tested field and the FFIEC field-validation logic; population is the LAR records for the period with extract from the LAR generation system; sample is typically stratified by action-taken type and rate-spread reportability; design procedures cover the LOS-to-LAR pipeline configuration and the demographic firewall; operating procedures cover per-field reperformance against source documents and population-level LAR-to-LOS reconciliation.

##### CRA testing

- CRA — 12 CFR Part 25 (OCC), Part 195 (former OTS, OCC), Part 228 (FRB Reg BB), Part 345 (FDIC) [verify current effective state given the 2023 final-rule litigation history]. https://www.federalreserve.gov/supervisionreg/regbbcg.htm .
- Test-plan conventions: lending-test plans carry geography distribution, borrower-profile distribution, and product-mix distribution as planned outputs; service-test and investment-test plans carry the qualified-investment register-review approach. The performance-context narrative is set out in the plan, not invented in the workpaper.

##### Reg B / ECOA testing

- Reg B — 12 CFR Part 1002. §1002.4 general rules, §1002.6 rules concerning evaluation, §1002.9 notifications, §1002.13 information for monitoring [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1002 .
- Test-plan conventions: adverse-action notice-timing tests reconcile application date to notice date by sample with the §1002.9 timing clock as the criterion; spousal-signature tests require reading the underwriting file rather than the front-end application; demographic-firewall tests require inspection of the production environment, not the test environment, and the plan names the production-access prerequisite.

##### Reg DD, Reg E, Reg Z testing

- Reg DD — 12 CFR Part 1030 (TISA disclosures, account fees) [verify subsection labels].
- Reg E — 12 CFR Part 1005 (electronic fund transfers, error resolution) [verify subsection labels including §1005.11 procedures and §1005.18 prepaid].
- Reg Z — 12 CFR Part 1026 (Truth in Lending) [verify subsection labels].
- Test-plan conventions: error-resolution test plans under §1005.11 walk the timeline by sample (notice date, investigation start, provisional credit by day 10 or day 5 for new accounts [verify §1005.11(c) timing], final determination, customer notice); pass criterion is 100% of sampled disputes within the procedural clock; fail criterion is any sampled item outside the clock without escalation evidence. Disclosure-content tests compare the production disclosure to the regulatory model with a redline procedure.

##### BSA/AML testing

- FFIEC BSA/AML Examination Manual (current edition) [verify last-revision date]. https://bsaaml.ffiec.gov/manual .
- 31 CFR Part 1010, 1020, 1022, 1023, 1024, 1025, 1026 (FinCEN AML rules by industry) [verify part references].
- Test-plan conventions: CIP plans cover new-account opening with the documented identification-and-verification step as the procedure; CDD/EDD plans cover the customer-due-diligence questionnaire and EDD enrichment evidence by sample; SAR-decision plans cover the case-management file from alert to disposition with timing checks against 31 CFR §1020.320 [verify subsection]. SAR content review is restricted to authorised reviewers; the plan names the access-control posture rather than restating SAR content.

##### CFPB CMS exam-cycle test plans

- The CFPB CMS examination procedures embed testing-program review against the four CMS pillars (board and management oversight, compliance program, response to consumer complaints, compliance audit). The plan distinguishes substantive-rule tests from CMS-program tests; findings on the testing program itself feed the CMS rating distinct from substantive control findings.

#### Sponsor-bank / bank-fintech-arrangement test plans

When the test addresses a bank-fintech partnership or a sponsor-bank deposit program, the plan carries:

- The **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date] frame: end-customer reconciliation testing, FBO subledger reconciliation, deposit-insurance representation review, and the fourth-party register all sit inside this frame.
- **Bank Service Company Act, 12 USC §1867(c)**: examiner-access posture for the vendor systems the firm relies on for evidence; the plan names reliance posture upfront.

#### Audience and tone

A test plan drafted with an upcoming OCC, FRB, FDIC, or CFPB exam in mind reads heavier on criteria (more verbatim from the regulation, more detail on FFIEC manual sections), heavier on the population-definition narrative, and heavier on the reviewer-questions block where the cycle anticipates examiner attention. A test plan drafted for in-cycle program coverage reads operationally with the same criteria base.

## capital-markets

### Capital-markets sector overlay — test-plan-builder

Loaded when `scope.sector_overlay_set` includes `capital-markets` or when the test addresses SEC, FINRA, NFA, or fund-board rules. Supplements `references/source-anchors.md`.

#### Test-plan conventions SEC and FINRA examiners expect

SEC Division of Examinations staff and FINRA examiners read CCO and supervisory-control test plans against compliance-program rule frames rather than safety-and-soundness frames. Three conventions matter:

- **Annual review framing carries the test plan.** Investment Advisers Act Rule 206(4)-7 and Investment Company Act Rule 38a-1(a)(4) are written around an annual review; test plans feed the annual review compendium. The plan restates the annual-review-period framing and identifies which annual-review element it covers.
- **Supervisory testing maps to FINRA 3120 and 3130.** Broker-dealer compliance test plans feed the FINRA 3120 supervisory-controls report and the FINRA 3130 CEO certification. The plan identifies which 3120 testing area the cycle covers and the certification cycle the test feeds.
- **Recordkeeping evidence treatment is regulated.** SEC Rule 17a-4 and FINRA Rule 4511 govern format, retention, and accessibility of the records the plan relies on. The plan does not invent a recordkeeping convention; it relies on the firm's records-management posture and notes any deficiency in evidence accessibility as a planning constraint distinct from the substantive test.

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
- **SEC Regulation Systems Compliance and Integrity (Reg SCI), 17 CFR §§242.1000-242.1007** [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-242 .

#### Capital-markets-control-area test-plan notes

##### Adviser annual compliance review (206(4)-7)

- Test-plan conventions: criteria section cites the firm's compliance manual section under test plus the corresponding Advisers Act rule; population is the activity in the named compliance area for the annual-review period; design procedures cover the policy-and-procedure adequacy review; operating procedures cover sample-based reperformance against the policy clock or the rule's substantive requirement.

##### Fund compliance program (38a-1)

- Test-plan conventions: 38a-1(a)(4) requires the fund to obtain certification from each material service provider that they have adopted and implemented compliance policies reasonably designed to prevent violations of federal securities laws. Test plans for service-provider adequacy carry service-provider attestation, on-site or remote diligence evidence, and any examination findings the service provider has disclosed. Cross-link to `vendor-diligence` and `dora-register-builder` (where DORA also applies).

##### Supervisory testing (FINRA 3110 / 3120 / 3130)

- Test-plan conventions: each tested supervisory procedure ties to a 3110 or 3120 area; the plan aggregation feeds the 3120 annual report; the firm's CEO certification under 3130 is the downstream consumer named in the plan.

##### Marketing rule (206(4)-1)

- Test-plan conventions: criteria section names the disseminated advertisement (cited by ad ID and date), the supporting evidence for performance claims and case studies, the Marketing Rule disclosures, and the firm's review-and-approval evidence. Testimonial and endorsement test plans cover compensation arrangements and required disclosures by sample.

##### Custody rule (206(4)-2)

- Test-plan conventions: custody test plans reconcile client-account positions and transactions against qualified-custodian records by sample; surprise-examination evidence is referenced by ID with the surprise-examiner's report carried as third-party-assurance evidence; sole authority over a private fund triggers audit-or-surprise-exam testing of the audit pathway.

##### Trade surveillance (best execution, market manipulation, manipulative-trading)

- Test-plan conventions: surveillance-alert test plans cover alert disposition by sample, with the alert criteria, the case file, and the disposition rationale named as expected evidence. Trade-reconstruction test plans cover the order-execution timeline by sample with NMS or fixed-income market-data references.

##### Reg SCI testing (where applicable)

- Test-plan conventions: SCI-system test plans cover the SCI policies and procedures, the SCI-system inventory, the SCI-event reporting evidence, and the SCI-event business-continuity testing per §242.1003 [verify subsection labels].

#### Reg S-P safeguards testing

- Reg S-P (as amended May 16, 2024) imposes incident-response, customer-notification, and service-provider-oversight obligations on broker-dealers, advisers, and investment companies [verify exact compliance dates by entity type]. Test-plan conventions: customer-notification timing test plans cite the regulatory clock; service-provider-oversight test plans cite the rule's diligence and ongoing-monitoring standards.

#### Audience and tone

A test plan drafted with an upcoming SEC Division of Examinations exam in mind reads heavier on annual-review framing, marketing-rule supporting evidence, and custody-rule reconciliations. A plan drafted for FINRA cycle exam preparation reads heavier on 3120 supervisory testing, 3110 supervisory-procedure design evidence, and Rule 4511 recordkeeping posture. A fund-board-facing plan reads heavier on 38a-1(a)(4) service-provider compliance-program-adequacy evidence with the fund-board reporting cycle as the deliverable consumer.

## insurance

### Insurance sector overlay — test-plan-builder

Loaded when `scope.sector_overlay_set` includes `insurance` or when the test addresses NAIC, state DOI, or insurance-specific federal rules. Supplements `references/source-anchors.md`.

#### Test-plan conventions insurance examiners expect

State DOI market-conduct examiners and NAIC accreditation reviewers read insurer test plans slightly differently from bank examiners. Two conventions matter most:

- **Statutory framework is the criterion, not the model.** State DOI examiners read against the state's adopted version of the NAIC model, not against the model itself. The plan cites the state-adopted citation (e.g., "N.Y. Ins. Law §X / 11 NYCRR §Y") with the NAIC model as a secondary reference. State-by-state adoption variance matters and the plan notes it where the test scope is multi-state.
- **Market-conduct sample design follows the NAIC Market Conduct Examiners Handbook** rather than AU-C 530 directly. The plan restates the sample-design rationale aligned to the Handbook's standards (file-review sample sizes, error-tolerance bands) and reconciles to AU-C 530 only where the firm's methodology has chosen it.

#### Insurance-supervisory anchors (load by reference; do not restate)

- **NAIC Annual Financial Reporting Model Regulation (Model Audit Rule, Model #205)** [verify section references for the internal-control testing-program documentation expectation]. https://content.naic.org/cipr-topics/topic-naic-model-laws-and-regulations [verify URL].
- **NAIC Market Conduct Examiners Handbook** (current edition) [verify section labels]. https://content.naic.org/cmte_d_mceh.htm [verify URL].
- **NAIC Insurance Holding Company System Regulatory Act (Model #440) and Holding Company Model Regulation (Model #450)** [verify model numbers]. Form B and Form D filings carry plan-relevant disclosure for affiliated-vendor testing.
- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number]. ORSA testing posture for insurer programs; the plan references the ORSA section under review.
- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers** (December 4, 2023) [verify state-by-state adoption status]. AIS Program testing covers governance, risk management, validation, third-party AI accountability, monitoring, documentation, transparency, fairness. https://content.naic.org/sites/default/files/inline-files/2023-12-04%20Model%20Bulletin_Adopted_0.pdf [verify URL].

#### Insurance-control-area test-plan notes

##### Underwriting and pricing testing

- Test-plan conventions: criteria section names rate-filing-versus-applied-rate reconciliation as the substantive criterion; population is the policies issued during the period; design procedures cover the rate-engine configuration and the underwriting-rule mapping; operating procedures cover applicant-attribute reconciliation against the rate manual or rule engine output by sample.
- Predictive-model testing under state DOI bulletins (Colorado SB 21-169 implementing regulation [verify section], NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting [verify circular number]) uses the bulletin's required testing artifacts as the criteria list (governance documentation, fairness testing, third-party-AI accountability evidence).

##### Claims handling testing

- Unfair Claims Settlement Practices Act state adoption [verify state citations], usually state-adopted versions of NAIC Model #900 [verify model number] or NAIC Model #902 [verify model number]. Test plan conventions: claims-handling test plans restate the acknowledgement-investigation-decision-payment timeline by sample with state-statutory clocks; the criteria section cites the state-adopted statute, not the NAIC model.

##### Producer licensing and appointment testing

- Test-plan conventions: licensing-status reconciliation against the state DOI register (NIPR / SBS) by sample; appointment-status testing against the state DOI register; commission-payment testing against the licensed-and-appointed status as of transaction date. Criteria cite the state-adopted producer licensing act.

##### Privacy and data-security testing

- NAIC Insurance Data Security Model Law (Model #668), §4.F third-party service-provider obligations [verify state-by-state adoption]. Plan conventions: criteria section names cybersecurity-program governance, incident-response testing, third-party-vendor diligence and monitoring evidence per the state-adopted version.
- NY DFS 23 NYCRR Part 500 applies to NY-licensed insurers as Covered Entities; cyber overlay applies in addition to insurance overlay where the firm holds a NY license.
- HIPAA Security Rule applies where the insurer is a covered entity (health, dental, vision); cyber and privacy overlays both load.

##### ORSA Summary Report testing

- Test-plan conventions: ORSA-relevant test plans read risk-identification, risk-assessment, risk-monitoring, and group capital-adequacy sections; sample-level evidence is by risk type rather than by transaction. The plan limitations section flags that the ORSA itself is a management report; the testing plan concludes on the underlying control effectiveness, not on ORSA content.

#### Multi-state and group-vs-entity scope

The plan is explicit about the legal entity under test and the states whose rules apply. A multi-state market-conduct test plan names primary state and concurrent states (where applicable under coordinated examinations). A group-level testing plan carries the holding-company structure and the parent-entity scope; the plan does not propose conclusions on legal-entity ICFR for non-tested entities.

#### Audience and tone

A test plan drafted with an upcoming state DOI market-conduct exam in mind reads heavier on state-statutory citations, sample-design rationale aligned to the NAIC Market Conduct Examiners Handbook, and limitations on the period and lines of business covered. A plan drafted for the NAIC AIS Program reads heavier on third-party-AI accountability, validation, and fairness-testing evidence per the model bulletin's adopted text in the firm's domiciliary state.

## payments-fintech

### Payments-fintech sector overlay — test-plan-builder

Loaded when `scope.sector_overlay_set` includes `payments-fintech` or when the test addresses NACHA, sponsor-bank, money-transmitter, prepaid, or larger-participant rules. Supplements `references/source-anchors.md`.

#### Test-plan conventions for payments and fintech testing

Payments and fintech test plans carry conventions that bank consumer-compliance test planning does not always anticipate:

- **Sponsor-bank arrangements load two sector overlays.** The fintech program tests against payments-fintech rules; the sponsor-bank arrangement tests against banking rules (Bank Service Company Act, the 2024 Joint Statement on bank-third-party deposit programs, end-customer reconciliation, deposit-insurance representation). Both overlays load and the plan names which controls sit on which side.
- **Reg E error-resolution case files are the operating-procedure unit.** The case file the firm produces in the ordinary course is the testing artifact under §1005.11. Compliance test plans for Reg E error-resolution sample case files for adherence to the procedure and the procedural clock.
- **NACHA Operating Rules are paywalled.** Cite as "current edition; specific sections to be confirmed against the firm's licensed copy" rather than restating rule text in the plan. The criteria section names the rule citation; the firm's licensed copy is the source of truth at fieldwork.
- **Larger-participant CFPB scope changes the criteria base.** Where the firm is a CFPB larger participant for digital consumer payment applications, CMS-aligned planning applies; the plan cites the larger-participant rule alongside the substantive rule under test. (The November 2024 final rule has been the subject of post-publication challenge and CFPB reconsideration since 2025 — verify current operative status before treating designation as firm.)

#### Payments-fintech-supervisory anchors (load by reference; do not restate)

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. Operative for sponsor-bank programs.
- **Reg E — 12 CFR Part 1005**, especially §1005.6 (consumer liability), §1005.7 (initial disclosures), §1005.8 (change-in-terms), §1005.10 (preauthorized transfers), §1005.11 (error resolution), §1005.18 (prepaid accounts) [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1005 .
- **NACHA Operating Rules (current edition)** Third-Party Sender risk-management rules and ODFI obligations [verify rule citations against the firm's licensed copy]. https://www.nacha.org/ .
- **FinCEN MSB rules at 31 CFR Part 1022** and registration requirements at 31 CFR §1010.380 [verify subsection labels]. https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1022 .
- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (November 21, 2024) — the rule has been the subject of post-publication challenge and CFPB reconsideration since 2025; verify current operative status before relying on designation. https://www.consumerfinance.gov/compliance/supervisory-guidance/ .
- **State money-transmitter rules** (state by state) — test plans cite the state-adopted statute citation, not the Money Transmission Modernization Act text [verify state citations].
- **Interagency Guidance on Third-Party Relationships: Risk Management** (FDIC / OCC / FRB, June 6, 2023) [verify section labels]. https://www.federalreserve.gov/supervisionreg/srletters/SR2304.htm .

#### Payments-fintech-control-area test-plan notes

##### Reg E error-resolution testing

- Test-plan conventions: criteria section cites §1005.11 and the firm's dispute-handling policy section; population is the Reg E disputes raised in the period; design procedures cover the dispute-management system workflow configuration (does the workflow enforce the day-10 or day-5 provisional-credit clock, the 45-day final-resolution clock, the customer-notice generation [verify §1005.11(c) / (d) timing]); operating procedures cover sample-based reperformance against the procedural clock with the case file as evidence per sample.
- Pass criterion: 100% of sampled disputes within the procedural clock with current evidence in the case file. Fail criterion: any sampled item outside the clock without escalation evidence.
- Prepaid-account test plans under §1005.18 carry additional disclosure-format and access-time provisions; the plan names the prepaid-program subset of the population.

##### Sponsor-bank end-customer reconciliation testing

- Test-plan conventions: end-customer reconciliation test plans read the sponsor-bank FBO subledger against the fintech program's customer ledger by sample (or by full reconciliation if the program's volume is small). Plan carries timing (daily, weekly, month-end), exception aging, and unmatched-balance treatment as procedure design.
- Deposit-insurance representation review is a separate test; the plan reads the firm's customer-facing communications (account-opening, T&Cs, marketing) against FDIC pass-through-deposit-insurance requirements [verify FDIC citation].

##### NACHA Third-Party Sender testing

- Test-plan conventions: TPS test plans cover risk-management evidence per the firm's licensed NACHA Rules copy, the ODFI agreement, the originator-due-diligence file by sample, the return-rate monitoring evidence, and the unauthorised-return investigation evidence. Cite the NACHA rule by edition and section without restating; rely on the firm's licensed copy.

##### BSA/AML for MSBs and fintechs

- Test-plan conventions: AML-program test plans cover CIP, CDD, and EDD evidence per the FFIEC BSA/AML Examination Manual and 31 CFR Part 1022 [verify part references]. Suspicious-activity test plans review case-management evidence with the same access-control posture as bank BSA testing (SAR content access restricted; the plan names the access control rather than restating SAR content).

##### Larger-participant CFPB scope (where applicable)

- Test-plan conventions: where the firm is a CFPB larger participant for digital consumer payment applications, CMS-aligned testing applies (verify operative status of the November 2024 designation rule on the engagement date). The plan cites the larger-participant rule alongside the substantive rule under test.

#### Audience and tone

A test plan drafted with an upcoming CFPB exam in mind reads heavier on UDAAP-relevant disclosures, error-resolution timing, and customer-impact framing. A plan drafted for a state money-transmitter exam reads heavier on the state-statute citation, customer-funds protection (segregation, permissible investments) testing, and the surety-bond or net-worth status. A plan drafted for sponsor-bank governance reads heavier on the bank-side and fintech-side control split with the bank service provider relationship explicit.
