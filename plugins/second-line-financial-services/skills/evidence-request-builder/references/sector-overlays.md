# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — evidence-request-builder

Loaded when `scope.sector_overlay_set` includes `banking` or when the test addresses a banking regulator's rule. Does not replace `references/source-anchors.md`; supplements it with bank-specific evidence-request conventions.

#### Request-list conventions banking testing programs apply

A bank consumer-compliance or operational-risk testing PBC list carries a few conventions beyond the methodology baseline:

- **System of record is named, not generic.** Loan origination system (LOS), customer-relationship-management system, deposit operations system, complaint-management system, BSA case-management system, IAM, AUS — name the system, not "internal database". The workpaper later relies on the same naming.
- **CSV asks name expected columns.** A LAR extract request, a transaction extract request, and a complaints extract request all carry the expected columns in the artifact description (FFIEC HMDA field labels, ACH transaction fields, complaints-data dictionary fields). "Send the LAR" without a column list is the request-shaping failure that triggers re-asks.
- **Reg-specific evidence has format conventions.** HMDA LAR extracts are CSV by FFIEC field labels; Reg E case files are PDF bundles per case ID; CIP / CDD evidence is per-customer packets; SAR-decision evidence carries the access-control posture without restating SAR content.
- **Reliance classification distinguishes vendor and management-prepared evidence.** AUS configuration extracts are vendor-supplied; quarterly LAR data-quality reconciliation logs are management-prepared. Both classifications drive workpaper reliance test notes.
- **Population reference ties the request to the sampling memo.** A request for "the LAR for sample IDs 1-60" or "the recertification packets for the privileged subset (full population) plus the 30-record stratified standard subset" is testable; a request for "the LAR" without a population reference is not.

#### Bank-supervisory anchors (load by reference; do not restate)

- **CFPB Compliance Management Review** examination procedures inside the **CFPB Supervision and Examination Manual** (current edition) [verify section labels for the testing-program component]. https://www.consumerfinance.gov/compliance/supervision-examinations/ .
- **OCC Comptroller's Handbook — Compliance Management Systems** [verify current edition and section labels]. https://www.occ.gov/publications-and-resources/publications/comptrollers-handbook/index-comptrollers-handbook.html .
- **SR 08-8 — Compliance Risk Management Programs and Oversight at Large Banking Organizations with Complex Compliance Profiles** (Federal Reserve, October 16, 2008) [verify section labels for testing-program documentation]. https://www.federalreserve.gov/boarddocs/srletters/2008/sr0808.htm .
- **OCC PPM 5310-3 — Bank Supervision Process** [verify exact PPM number and current effective date].
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for $50B+ covered banks [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-I/part-30 .
- **Bank Service Company Act, 12 USC §1867(c)** — examiner-access posture for bank service providers; cite when a request asks a bank service provider for evidence.

#### Bank-control-area request notes

##### HMDA / Reg C testing

- Reg C — 12 CFR Part 1003. §1003.4 data points, §1003.5 disclosure and reporting [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1003 .
- FFIEC HMDA Filing Instructions Guide (current edition) [verify edition year]. https://www.ffiec.gov/hmda/guide.htm .
- Request conventions: LAR record extracts are CSV with named columns matching FFIEC field labels; underlying loan files are per-sample PDF bundles (URLA, AUS findings, rate-lock confirmation, settlement statement, lien-position evidence); demographic-firewall evidence carries an IAM-extract scope (production, by role) plus the demographic-information form per sample. AUS configuration extracts are a separate request flagged vendor-supplied. Quarterly LAR data-quality reconciliation log is management-prepared and triggers the workpaper's completeness-and-accuracy check.

##### CRA testing

- CRA — 12 CFR Part 25 (OCC), Part 228 (FRB Reg BB), Part 345 (FDIC) [verify current effective state given the 2023 final-rule litigation history]. https://www.federalreserve.gov/supervisionreg/regbbcg.htm .
- Request conventions: lending-test evidence requests draw geographic distribution extracts, borrower-profile distribution extracts, and product-mix distribution extracts; service-test and investment-test requests draw the qualified-investment register and branch-distribution evidence. Performance-context narrative is set out in the test plan rather than requested as evidence.

##### Reg B / ECOA testing

- Reg B — 12 CFR Part 1002. §1002.4, §1002.5(b), §1002.6, §1002.9, §1002.13 [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1002 .
- Request conventions: adverse-action notice testing requests the underlying application file and the notice-issuance log per sample; spousal-signature testing requests the underwriting file (not just the front-end application) per sample; demographic-firewall testing requests the production-environment role-based access entitlement extract for any role with access to demographic information at underwriting (not the test environment).

##### Reg DD, Reg E, Reg Z testing

- Reg DD — 12 CFR Part 1030 [verify subsection labels].
- Reg E — 12 CFR Part 1005 [verify subsection labels including §1005.11 procedures and §1005.18 prepaid].
- Reg Z — 12 CFR Part 1026 [verify subsection labels].
- Request conventions: error-resolution case files are PDF bundles per case ID with the dispute-management-system case extract attached; disclosure-content testing requests the production disclosure (PDF) plus the regulatory model for redline; periodic-statement testing requests sample statements per account ID with the statement-generation log.

##### BSA/AML testing

- FFIEC BSA/AML Examination Manual (current edition) [verify last-revision date]. https://bsaaml.ffiec.gov/manual .
- 31 CFR Part 1010, 1020, 1022, 1023, 1024, 1025, 1026 (FinCEN AML rules by industry) [verify part references].
- 31 CFR §1010.230 (beneficial ownership for legal-entity customers) [verify subsection].
- Request conventions: CIP testing requests the new-account opening packet plus the documented identification-and-verification step per sample; CDD/EDD testing requests the customer-due-diligence questionnaire and the EDD enrichment evidence per sample; SAR-decision testing requests the case-management file from alert to disposition with timing checks against 31 CFR §1020.320 — SAR content access is restricted; the request notes the access-control posture rather than restating SAR content. Beneficial-ownership recertification testing requests the recertification form, certifier-attestation record, and any change-of-ownership trigger evidence per legal-entity sample.

##### Sponsor-bank arrangements

- When the test addresses a bank-fintech partnership or a sponsor-bank deposit program, the request list draws against the **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]: end-customer reconciliation evidence (FBO subledger versus fintech program ledger), deposit-insurance representation evidence (account-opening, T&Cs, marketing), and the fourth-party register evidence.
- Bank Service Company Act, 12 USC §1867(c) examiner-access posture is cited where the firm relies on the BSCA-covered contract to field a request to a bank service provider.

#### Audience and tone

A request list drafted ahead of an upcoming OCC, FRB, FDIC, or CFPB exam reads heavier on the regulator-acknowledgement evidence (resubmission logs, prior-cycle remediation evidence) and on the named system-of-record discipline. A request list drafted for in-cycle internal testing reads operationally with the same evidence base; the methodology bar is the same, only the rendering audience changes.

## capital-markets

### Capital-markets sector overlay — evidence-request-builder

Loaded when `scope.sector_overlay_set` includes `capital-markets` or when the test addresses FINRA, SEC, NFA, MSRB, or exchange rules. Supplements `references/source-anchors.md`.

#### Request-list conventions capital-markets testing programs apply

Broker-dealer, investment adviser, and asset-management testing PBC lists carry conventions distinct from bank consumer-compliance:

- **Order-blotter pulls are recordkeeping evidence, not transaction reports.** Order blotters under SEC Rule 17a-3 / 17a-4 and FINRA Rule 4511 are the source-of-record for order events. Requests for order-blotter extracts cite the rule and name the format the recordkeeping rule preserves (non-rewriteable form, audit-trail intact). Cite the rule rather than restating the recordkeeping format requirements.
- **Communications-supervision evidence carries an archive scope.** FINRA Rule 3110(b)(4) communications-review evidence requests cite the firm's communications archive (Smarsh, Global Relay, Bloomberg Vault, or named equivalent), the channel scope (email, IM, social media, voice where retained), and the supervisory-review-evidence format (review-completion log per supervisor, sample of reviewed items per supervisor).
- **Trade-surveillance evidence carries the surveillance-platform scope and the alert-disposition log.** Trade-surveillance testing requests the alert log per sample (alert ID, alert reason, surveillance rule fired, disposition rationale, disposer role, disposition date) plus the underlying order-event evidence per alerted order.
- **Adviser compliance-program evidence draws the annual-review file under Rule 206(4)-7.** The annual review under Rule 206(4)-7 is itself a workpaper; testing the annual-review process requests the annual-review file (scope memo, testing performed, findings, remediation tracking).
- **Books-and-records request format respects the recordkeeping rule.** Broker-dealer record requests respect SEC Rule 17a-4 preservation requirements; the format requested reflects the firm's recordkeeping practice (PDF copies acceptable for second-line testing; the underlying preservation in non-rewriteable form is the firm's compliance posture, not the testing posture).

#### Capital-markets-supervisory anchors (load by reference; do not restate)

- **FINRA Rule 3110 — Supervision** [verify subsection labels including §3110(a) supervisory system, §3110(b) written supervisory procedures, §3110(c) internal inspections, §3110(d) transaction review and investigation, §3110(e) qualifications of supervisors]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3110 .
- **FINRA Rule 3120 — Supervisory Control System** [verify subsection labels]. Annual report on supervisory controls. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3120 .
- **FINRA Rule 3130 — Annual Certification of Compliance and Supervisory Processes** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/3130 .
- **SEC Rule 17a-3 (17 CFR §240.17a-3)** — broker-dealer recordkeeping (records to be made). https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.17a-3 .
- **SEC Rule 17a-4 (17 CFR §240.17a-4)** — broker-dealer recordkeeping (records to be preserved). https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.17a-4 .
- **FINRA Rule 4511 — General Requirements (Books and Records)** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/4511 .
- **Investment Advisers Act Rule 206(4)-7** — adviser compliance-program rule [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-7 .
- **Investment Advisers Act Rule 204-2** — adviser books and records [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.204-2 .
- **SEC Marketing Rule (Rule 206(4)-1)** [verify subsection labels including testimonials, endorsements, and performance advertising provisions]. https://www.ecfr.gov/current/title-17/chapter-II/part-275/section-275.206(4)-1 .
- **SEC Regulation Best Interest (17 CFR §240.15l-1)** [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-240/section-240.15l-1 .
- **SEC Reg SCI (17 CFR §§242.1000-242.1007)** for SCI entities [verify subsection labels]. https://www.ecfr.gov/current/title-17/chapter-II/part-242 .

#### Capital-markets-control-area request notes

##### Communications-supervision testing (FINRA 3110(b)(4))

- Request conventions: communications-archive extract for the sampled supervisor-period (channel, message ID, sender, recipients, date, content) from the firm's archive (Smarsh, Global Relay, Bloomberg Vault, or named equivalent). Per-supervisor review-completion log with sample items reviewed and the review-evidence (lexicon-hit disposition, escalation evidence where applicable). Reliance test note covers the archive's completeness against the messaging platform.

##### Trade-surveillance testing

- Request conventions: alert log CSV for the sampled period per surveillance rule fired (alert ID, alert reason, fired rule, disposition rationale, disposer role, disposition date). Underlying order-event extract per alerted order (order entry, modification, execution, cancellation events with times). Surveillance-rule configuration extract for the period. Reliance test note distinguishes alert-disposition from supervisory-rule-tuning evidence.

##### Books-and-records testing (17a-3, 17a-4, 4511)

- Request conventions: per-sample record retrieval from the firm's preservation system (order tickets, customer-account documents, communications, supervisory records). Format respects the recordkeeping rule's preservation form; the request asks for a copy in PDF or system-export and the preservation format itself is evidenced separately by a recordkeeping-system attestation.

##### Adviser annual-review testing (206(4)-7)

- Request conventions: annual-review file from the firm's CCO (scope memo, testing performed by topic, findings register, remediation tracking, board or governance committee report). The annual review is itself a workpaper; the request asks for the annual-review file rather than evidencing the underlying activity for the second-line test.

##### Marketing-rule testing (206(4)-1)

- Request conventions: marketing-materials register CSV for the period with material ID, channel, intended audience, period live, and the supervisory-review evidence per material; per-sample material PDF; performance-advertising supporting evidence (calculation methodology, GIPS-compliance evidence where claimed, fee-and-expense net-or-gross posture). Testimonials and endorsements draw the disclosure evidence and the compensation arrangement evidence per Rule 206(4)-1 [verify subsection].

##### Supervisory-controls and annual-certification testing (3120, 3130)

- Request conventions: 3120 supervisory-controls report for the most recent year with supporting tests-and-verifications evidence. 3130 CEO certification with the underlying CCO testing-of-supervisory-processes evidence. The request list draws the certification cycle and the supporting tests; the testing this list serves is one input to the next 3130 cycle.

##### Reg SCI testing (where the firm is an SCI entity)

- Request conventions: SCI systems inventory; SCI-event log for the period with materiality-determination evidence; quarterly material-systems-changes report; annual SCI review; business-continuity / disaster-recovery testing evidence. SCI evidence is connector-aware where the firm has automated SCI inventory and event-management systems.

#### Audience and tone

A request list drafted ahead of an upcoming SEC OCIE / Examinations Division exam reads aligned to the SEC examination request-list shape (which the SEC publishes in its sample exam request-letter materials). A request list drafted ahead of a FINRA cycle exam reads aligned to FINRA's request-letter conventions. A request list for the firm's internal CCO-led periodic testing reads operationally with the same evidence shape; the methodology bar is the same, only the rendering audience changes.

## insurance

### Insurance sector overlay — evidence-request-builder

Loaded when `scope.sector_overlay_set` includes `insurance` or when the test addresses NAIC, state DOI, or federal insurance rules. Supplements `references/source-anchors.md`.

#### Request-list conventions insurance testing programs apply

Insurance testing PBC lists carry conventions distinct from bank consumer-compliance:

- **Claim-file and policy-file evidence is per-file PDF.** A claim-file ask is the full file (FNOL, adjuster notes, coverage analysis, payment record, denial letter where applicable, complaint correspondence where applicable) per claim ID. A policy-file ask is the underwriting file per policy ID (application, underwriter notes, rate calculation, supporting documentation, declaration page). System-of-record naming matters: claim-management system, policy-administration system, agency-management system.
- **Rate-filing testing requests the SERFF filing.** Rate-and-form-filing testing draws the actual SERFF (System for Electronic Rate and Form Filing) filing record per state-product, the supporting actuarial memorandum, and the state DOI approval order or disposition. SERFF tracking number is the natural request key.
- **Market-conduct evidence follows the NAIC Market Conduct Examiners Handbook conventions.** State DOI market-conduct examinations use standardised request-list shapes the NAIC handbook codifies; second-line testing programs in scope of upcoming market-conduct exams should align the request-list shape so the workpaper file reads against the examiner's expectation.
- **Complaint-handling evidence draws the consumer-complaint log plus per-complaint files.** Complaint logs are CSV exports from the complaint-management system with named columns (complaint ID, intake date, source, line of business, complaint type, resolution date, resolution outcome). Per-sample complaint files are PDF bundles.
- **Producer-licensing evidence draws state-licensing and appointment evidence.** Producer-licensing testing requests the licensing register (state, license type, effective date, appointment status) plus per-sample state license verification (NIPR or state DOI lookup).

#### Insurance-supervisory anchors (load by reference; do not restate)

- **NAIC Annual Financial Reporting Model Regulation (Model Audit Rule, Model #205)** [verify section references for the ICFR-relevant evidence-request conventions]. https://content.naic.org/cipr-topics/topic-naic-model-laws-and-regulations [verify URL].
- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number and section labels]. https://content.naic.org/cipr-topics/own-risk-and-solvency-assessment-orsa .
- **NAIC Market Conduct Examiners Handbook** (current edition) [verify section labels for state DOI market-conduct request conventions]. https://content.naic.org/cmte_d_mceh.htm [verify URL].
- **NAIC Insurance Data Security Model Law (Model #668)** [verify section labels for cybersecurity event-reporting and program-evidence requests]. https://content.naic.org/cipr-topics/insurance-data-security-model-law .
- **State unfair claims settlement practices statutes** (state by state) — testing requests carry the state-adopted statute citation; the NAIC Unfair Claims Settlement Practices Model Act (Model #900) [verify model number] is the methodology anchor where the state adopted the model.

#### Insurance-control-area request notes

##### Claims-handling testing (state UCSPA, NAIC Market Conduct Examiners Handbook)

- Request conventions: per-sample claim file PDF bundle (FNOL, adjuster notes, coverage analysis, payment record, denial letter where applicable, customer correspondence). Claim-handling timing requests the claim-system event log (intake date, acknowledgement date, decision date, payment date) per sample. Complaint-correspondence routing testing requests the complaint-management-system extract joined to the claim file by claim ID. Reliance test notes apply where the claim file is management-prepared at the adjuster level (subject to supervisor review trace).

##### Underwriting-file testing (NAIC Market Conduct Examiners Handbook)

- Request conventions: per-sample policy file PDF bundle (application, underwriter notes, rate calculation, supporting documentation, declaration page, any subsequent endorsements). Underwriting-decision testing also requests the underwriter-decision audit trail from the policy-administration system. Rating-tier-assignment testing requests the rating-engine input/output log per sample.

##### Rate-and-form-filing testing

- Request conventions: SERFF filing record per state-product (filing PDF, supporting documentation, actuarial memorandum, state DOI disposition or approval letter). State-by-state filing register is a CSV export from the firm's filing-tracking system (or from SERFF directly). Use-and-file states versus prior-approval states have different evidence shapes; the request list distinguishes by state.

##### Producer-licensing and appointment testing

- Request conventions: producer-licensing register CSV (NPN, name-as-licensed, state, license type, license effective and expiration dates, appointment status, line-of-authority) from the agency-management system; per-sample state license verification (NIPR or state DOI). Continuing-education compliance testing requests the producer's CE-credit register from the firm's CE-tracking system or from NAIC ProducerCheck.

##### Privacy and data-security testing under Model #668

- Request conventions: information-security program evidence (program documents, risk-assessment evidence, incident-response evidence, third-party assurance for vendors handling NPI). Cybersecurity event reporting requests the firm's event log for the period with the §4(B) [verify subsection] notification timing per event.

##### ORSA testing

- Request conventions: ORSA Summary Report draft for the period, ORSA risk-assessment supporting evidence, and the board-or-board-committee approval of the ORSA Summary Report. ORSA evidence is typically connector-aware reliance because the ORSA Summary Report itself is a privileged regulator-only filing and evidence access posture matters.

#### Audience and tone

A request list drafted ahead of an upcoming state DOI market-conduct exam reads aligned to the NAIC Market Conduct Examiners Handbook standardised data calls. A request list drafted for the firm's internal periodic testing of claim-handling reads operationally with the same evidence shape. Where the firm is multi-state, the request list distinguishes state-specific evidence (state-adopted statute citation) from federal-or-NAIC-model evidence.

## payments-fintech

### Payments-fintech sector overlay — evidence-request-builder

Loaded when `scope.sector_overlay_set` includes `payments-fintech` or when the test addresses NACHA, sponsor-bank, money-transmitter, prepaid, or larger-participant rules. Supplements `references/source-anchors.md`.

#### Request-list conventions payments-fintech testing programs apply

Payments and fintech testing PBC lists carry conventions distinct from bank consumer-compliance:

- **Sponsor-bank arrangements load two sector overlays.** The fintech program tests against payments-fintech rules; the sponsor-bank arrangement tests against banking rules (Bank Service Company Act, Joint Statement on Bank-Third-Party Deposit Programs, end-customer reconciliation, deposit-insurance representation). Both overlays load and the request list names which evidence sits on which side. Sponsor-bank-side requests cite the bank's BSCA-covered contract for examiner access.
- **Reg E case-file requests are per-case PDF bundles.** §1005.11 case files are the workpaper for Reg E error-resolution testing; request the case file (notice date, investigation evidence, provisional credit evidence, final determination, customer notice, any reversal) per sample case ID.
- **NACHA Operating Rules are paywalled.** Cite as "current edition; specific sections to be confirmed against the firm's licensed copy" rather than asking for rule text. Request the firm's compliance evidence against the NACHA rules (Third-Party Sender risk-management evidence, ODFI-warranty evidence, return-rate monitoring) drawing against the firm's licensed-copy sections.
- **Money-transmitter evidence carries state-by-state structure.** The request list lists per-state-licensed entity the licensing register, per-state surety bond or net-worth evidence, per-state customer-funds protection evidence (segregation, permissible investments), and per-state reporting evidence (call reports, MSB reports under FinCEN 31 CFR Part 1022).
- **Crypto and stablecoin evidence asks the source-of-record system explicitly.** Where the firm's evidence sits on-chain (wallet inventory, on-chain reserves attestation), the request cites the chain, the wallet address scope, and the block-height or snapshot date; off-chain evidence sits in the firm's exchange or custody system and the request names the system.

#### Payments-fintech-supervisory anchors (load by reference; do not restate)

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. Operative for sponsor-bank programs.
- **Interagency Guidance on Third-Party Relationships: Risk Management** (FDIC / OCC / FRB, June 6, 2023) [verify section labels]. Sponsor-bank oversight evidence requests sit inside this frame. https://www.federalreserve.gov/supervisionreg/srletters/SR2304.htm .
- **Reg E — 12 CFR Part 1005**, especially §1005.6 (consumer liability), §1005.7 (initial disclosures), §1005.10 (preauthorized transfers), §1005.11 (error resolution), §1005.18 (prepaid accounts) [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1005 .
- **NACHA Operating Rules (current edition)** [verify rule citations against the firm's licensed copy]. https://www.nacha.org/ .
- **FinCEN MSB rules at 31 CFR Part 1022** and registration requirements at 31 CFR §1010.380 [verify subsection labels]. https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1022 .
- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (November 21, 2024) — subject to post-publication challenge and CFPB reconsideration since 2025; verify current operative status before relying on designation. https://www.consumerfinance.gov/compliance/supervisory-guidance/ .
- **State money-transmitter rules** (state by state) — request lists carry the state-adopted statute citation, not the Money Transmission Modernization Act text [verify state citations].
- **OCC Bulletin 2008-12 — Risk Management Guidance on Payment Processors** [verify exact bulletin number] for bank-side processor-relationship testing.

#### Payments-fintech-control-area request notes

##### Reg E error-resolution testing (§1005.11)

- Request conventions: per-sample case file PDF bundle (notice date, investigation evidence, provisional credit evidence with timing, final determination, customer notice, any reversal). Dispute-management-system case extract per sample with case-event log (notice received, investigation start, provisional credit issued, final determination, customer notice, reversal where applicable). Reliance test note covers completeness of the case file against the dispute-management system. Prepaid-account testing under §1005.18 requests the prepaid-program subset of the population with the additional disclosure-format and access-time evidence.

##### Sponsor-bank end-customer reconciliation testing

- Request conventions: end-customer reconciliation evidence for the period — sponsor-bank FBO subledger extract joined to the fintech program's customer ledger by sample (or full-population reconciliation if program volume is small). Reconciliation cadence evidence (daily, weekly, month-end). Exception-aging and unmatched-balance treatment evidence. The request list distinguishes bank-side and fintech-side ownership of each evidence row.
- Deposit-insurance representation review requests the firm's customer-facing communications (account-opening, T&Cs, marketing) per the FDIC pass-through-deposit-insurance requirements [verify FDIC citation].
- Fourth-party register evidence is requested where the fintech program relies on subcontractors that the sponsor-bank's TPRM frame requires registering.

##### NACHA Third-Party Sender testing

- Request conventions: TPS testing requests risk-management evidence per the firm's licensed NACHA Rules copy, the ODFI agreement, the originator-due-diligence file by sample, the return-rate monitoring evidence, the unauthorised-return investigation evidence, and the OFAC screening evidence on originators. Cite the NACHA rule by edition and section without restating; rely on the firm's licensed copy.

##### BSA/AML testing for MSBs and fintechs

- Request conventions: AML-program testing requests CIP, CDD, and EDD evidence per sample under the FFIEC BSA/AML Examination Manual and 31 CFR Part 1022 [verify part references]. Suspicious-activity testing requests case-management evidence with the same access-control posture as bank BSA testing (SAR content access restricted; the request notes the access control without restating SAR content). Sanctions-screening testing requests the screening configuration, the alert log per sample, and the alert-disposition evidence.

##### State money-transmitter testing

- Request conventions: per-state-licensed entity, the licensing register, the surety-bond or net-worth evidence (per the state's standard), the customer-funds protection evidence (segregation accounts, permissible investments), the per-state reporting evidence (state-required call reports, customer-funds attestations), and the per-state customer-disclosure evidence. The request list groups by state because the criteria differ.

##### Crypto and stablecoin program testing

- Request conventions: wallet inventory (chain, wallet address, custodian role), proof-of-reserves attestation evidence (where the program represents a reserves position), customer asset segregation evidence, sanctions-screening at the wallet level, and the firm's travel-rule compliance evidence under FinCEN 31 CFR §1010.410(f) [verify subsection]. On-chain evidence cites the chain, the wallet address scope, and the snapshot block-height or date.

##### CFPB larger-participant scope (where applicable)

- Request conventions: where the firm is a CFPB larger participant for digital consumer payment applications, CMS-aligned testing applies (verify operative status of the November 2024 designation rule on the engagement date). The request list cites the larger-participant rule alongside the substantive rule under test (Reg E, UDAAP).

#### Audience and tone

A request list drafted ahead of an upcoming CFPB exam reads heavier on UDAAP-relevant evidence (call recordings, complaint files, marketing-claim review records). A request list drafted ahead of a state money-transmitter exam reads heavier on the state-specific licensing, surety-bond, customer-funds protection, and reporting evidence. A request list drafted ahead of a sponsor-bank-led oversight cycle reads heavier on the bank-side and fintech-side control split, with the bank service provider relationship explicit and the BSCA examiner-access posture cited where relevant.
