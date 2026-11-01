# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — contract-gap-review

When the scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the banking-only clause expectations the generic capability skill does not own.

#### Operative supervisory frame

- **Interagency Guidance on Third-Party Relationships: Risk Management** (OCC Bulletin 2023-17, FRB SR 23-4, FDIC FIL-29-2023, June 6, 2023). The contract-negotiation section is the spine of the banking gap matrix.
- **OCC Bulletin 2013-29** is still cited as the predecessor frame in supervisory practice. Where examiners reference it, treat as supplemental, not operative.
- **FFIEC IT Examination Handbook — Outsourcing Technology Services booklet** is the examiner-facing detail for technology-vendor contracts.
- **Comptroller's Handbook — Third-Party Relationships: Risk Management** [verify current edition] is the OCC examiner playbook for national banks and federal savings associations; the contract-issues section informs what an examiner expects to read in the matrix.
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for $50B+ covered banks: contract gap matrix outputs feed the risk-governance framework and the board's third-party oversight. The matrix for an important or critical vendor should be visible to the independent risk-management function.

#### Banking-only contract anchors

- **Bank Service Company Act, 12 USC §1867(c)** — statutory examiner-access right over bank service providers. The contract must preserve regulator examination access and audit rights into the vendor's records, systems, and personnel for the services performed for the bank. Banking-only clause expectation; flag any contract that lacks the clause as a `high`-severity finding regardless of vendor tier or other audit-rights language. The clause must include continuity through wind-down (the right survives termination for the records-retention period).

- **12 CFR Part 30 Appendix B (Interagency Guidelines Establishing Standards for Safeguarding Customer Information), III.D**. Service-provider arrangements: due diligence, contract requirements (information-security safeguards, monitoring), monitoring [verify subsection labels]. The contract clause cluster has a specific information-security floor here that pre-dates and is independent of the GLBA Safeguards Rule's FTC version.

#### Reg O lens

- **Reg O, 12 CFR Part 215** — diligence on a vendor whose principals are insiders (directors, executive officers, principal shareholders) of the partner bank, or affiliates thereof, must include the Reg O screen, and the contract must be at arms-length on terms substantially the same as those for comparable transactions with non-insiders. The contract gap matrix surfaces a `high`-severity finding where the contract reads as a related-party arrangement without the substantive Reg O substantiation.

#### BaaS and bank-fintech contract clauses

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC, OCC, FRB, July 25, 2024) [verify exact title and date]: where the contract is a sponsor-bank program agreement or BaaS platform agreement, the clause set expands to: end-customer-reconciliation responsibilities and frequency; FBO subledger ownership, access, and reconciliation; deposit-insurance representation review (and customer-facing FDIC framing); program-operator operational-resilience commitments; the fourth-party register and the change-notice mechanism; BSA/AML responsibility allocation; customer-liability allocation under Reg E and Reg DD; complaint-handling chain; data-portability on termination. The standard generic clause set undercovers BaaS; the overlay adds the program-specific rows.

- **OCC Bulletin on Bank-Fintech Arrangements** [verify bulletin number]: where present in the firm's source list, treat as supplemental detail.

- **FFIEC inter-agency joint statement on community-bank fintech due diligence** (August 2023) [verify exact title]: for community banks engaging fintech partners; carries an explicit contract-checklist that runs alongside the interagency guidance.

#### Reg E, Reg DD, and consumer-account close-out

- **Reg E (12 CFR Part 1005)** §1005.6, §1005.11, §1005.18 — error-resolution, customer-liability allocation, and prepaid-account rules. Contract must support the bank's ability to meet its Reg E obligations through the vendor's processes, including evidence handover for error-resolution determinations.
- **Reg DD (12 CFR Part 1030)** §1030.5 — change-in-terms and account-close-out customer-notification. Contract must support the bank's notification obligation on a vendor-driven account-close-out scenario.

#### Cross-link inside the plugin

- **`exit-plan` banking overlay** carries the FBO-account wind-down sequence, the §1030.5 and §1005.8 customer-notification responsibilities, and §1867(c) examination-access continuity through wind-down. The contract gap matrix should evidence the contract clauses that enable each of those exit steps; the exit-plan workflow consumes the findings.
- **`vendor-diligence` banking overlay** carries the read-through on monitoring evidence; the contract gap matrix is the input on whether the contract gives the bank the rights to obtain that evidence.

#### Common banking pitfalls

- Treating "audit rights subject to reasonable cooperation" as satisfying Bank Service Company Act §1867(c). It does not. The §1867(c) clause must explicitly preserve regulator examination access; bilateral audit-cooperation language is a separate row.
- Missing the FBO subledger and end-customer-reconciliation clause set in a sponsor-bank program contract. The standard generic clause set undercovers BaaS; the overlay adds the program-specific rows.
- Treating "industry-standard SLA" as sufficient for a critical vendor at a $50B+ covered bank. Heightened Standards Appendix D requires the board's third-party oversight to read against the firm's tolerance, not the vendor's default.

## capital-markets

### Capital-markets sector overlay — contract-gap-review

When the scope flags capital markets (advisers, broker-dealers, registered funds, asset managers, SCI entities), load this overlay alongside `references/source-anchors.md`. The bank-flavoured interagency-guidance frame is not the operative supervisory frame for non-bank registrants; the contract clause set is built differently.

#### Operative supervisory frame

There is no single interagency third-party-contract bulletin for SEC and FINRA registrants. Contract expectations come through:

- **Investment Advisers Act Rule 206(4)-7** — adviser compliance-program rule. The adviser must have written policies and procedures reasonably designed to prevent violations; service-provider oversight requires contractual reach into evidence, monitoring, and incident-response cooperation. The matrix must surface the rows that enable the adviser's compliance-program oversight.

- **Investment Company Act Rule 38a-1(a)(4)** — fund compliance-program rule, including service-provider compliance-program-adequacy assessment for transfer agent, custodian, fund accountant, principal underwriter, valuation designee, pricing services. The fund CCO oversees; the contract must give the fund CCO information-access, certification, and incident-cooperation rights.

- **FINRA Rule 3110 (supervision)** — for broker-dealers, supervisory obligations extend to outsourced functions. The contract must support the BD's supervisory reach (records access, personnel-reach, exam-cooperation).

- **SEC Division of Examinations Risk Alerts on outsourced CCO arrangements** (the SEC's 2022 Risk Alert is the most-cited; [verify exact title and date]). Where the vendor is an outsourced-CCO provider, the matrix has additional rows on conflicts, capacity, evidence-access, and termination on regulatory-action triggers.

#### Custody Rule

- **Investment Advisers Act Rule 206(4)-2** — where the vendor touches client assets, the contract must reflect qualified-custodian status, account-statement-delivery responsibilities, surprise-audit cooperation, and SLOA inventory access. Distinct contract-row set from generic safekeeping-services language.

#### Books-and-records and retention

- **17 CFR §§240.17a-3 and 240.17a-4 (BD books-and-records)** and **17 CFR §270.31a-2 (fund books-and-records)**: retention windows, form requirements (electronic-storage media, write-once-read-many or audit-trail equivalents under amended 17a-4), prompt-production-on-request. The contract must give the registrant the records, in the required form, within the timeframes the rules contemplate. The matrix surfaces a row for retention scope and form, a separate row for production-timing, and a separate row for media-format compliance.

#### Reg S-P (May 2024 amendments)

- **17 CFR Part 248 (Reg S-P) as amended May 2024** [verify exact compliance dates by entity type and size]: covered-institution safeguarding obligations, service-provider written-contract requirements, and breach-notification timing. The matrix must surface the Reg S-P contract-clause set, including the service-provider written-contract requirement and the upstream breach-notification clock that supports the covered institution's customer-notice obligation.

#### Reg SCI

- **Reg SCI (17 CFR §§242.1000-1007)** for SCI entities. The contract for an SCI-system-supporting vendor must include incident-notification (timing aligned with the SCI entity's Reg SCI obligations), BCP cooperation, change-management cooperation, and documentation access. The clause set is enhanced over the generic third-party-contract baseline.

#### Sub-adviser and best-execution arrangements

- **Sub-adviser oversight**: where a sub-adviser is the vendor, the contract must reflect the fund adviser's 38a-1 program reach, the code-of-ethics flow-down, soft-dollar and affiliated-broker conflicts disclosure, and termination triggers tied to compliance findings.
- **Best execution under Investment Advisers Act §206 fiduciary duty and FINRA Rule 5310** — where the vendor is an execution venue, ATS, or broker-dealer counterparty, the matrix overlaps with `best-execution-surveillance` (capital-markets sector skill). The contract must give the registrant the data and reporting that support the best-execution analysis.

#### Cross-link inside the plugin

- **`exit-plan` capital-markets overlay** carries the records-portability sequence under 17a-4 and 31a-2, the fund-board notification posture for a critical-fund-service-provider exit, and the SEC and state notification posture where applicable. The contract gap matrix should evidence the contract clauses that enable each of those exit steps.

#### Common capital-markets pitfalls

- Applying the bank-flavoured interagency-guidance contract checklist verbatim. The non-bank registrant's contract clause set comes through 206(4)-7, 38a-1, FINRA 3110, and the rule-specific contract reach (Custody Rule, books-and-records, Reg S-P, Reg SCI). The matrix must build off the right frame.
- Missing the books-and-records media-format row. Amended 17a-4 changed the acceptable-storage-media requirements; a contract written against the prior frame can be silent on the current requirement.
- Conflating fund-adviser oversight with sub-adviser oversight. The fund's 38a-1 reach into a sub-adviser is distinct from the adviser's 206(4)-7 reach into a service provider; the matrix must reflect the right rule for the right vendor.
- Treating the Reg S-P May 2024 service-provider contract requirement as already satisfied by the generic confidentiality clause. The amended rule has specific contract-content expectations; the matrix surfaces them as a distinct row.

## insurance

### Insurance sector overlay — contract-gap-review

When the scope flags insurance, load this overlay alongside `references/source-anchors.md`. The insurance overlay carries the clause expectations the bank-flavoured capability skill does not own.

#### Vendor and contract types specific to insurance

The matrix must recognise the insurance-specific contract population: managing general agent (MGA) agreement, managing general underwriter (MGU) agreement, third-party administrator (TPA) agreement, claims-administrator agreement, underwriting-bureau agreement, actuarial-services agreement, IT outsourcing agreement, AI / ML vendor agreement, ECDIS data-provider agreement, illustration-software-vendor agreement, reinsurance-services-vendor agreement (distinct from a reinsurance treaty itself). Each pulls a different model-law clause set into the matrix.

#### Operative model-law clause anchors

- **NAIC Insurance Data Security Model Law (Model #668), §4.F third-party service-provider obligations**: written-contract terms requiring information-security safeguards, monitoring, incident-response cooperation, and breach-notification chain. Distinct from federal interagency-guidance third-party expectations. State-by-state adoption; the NAIC adoption tracker is the public reference. Where adopted, the §4.F contract clauses are mandatory-by-source; absence is a `high`-severity finding.

- **NAIC Insurance Holding Company System Regulatory Act (Model #440)** [verify model number] and **Holding Company Model Regulation (Model #450)** [verify model number]: affiliate-services contracts (Form B, Form D) have prescribed content (cost-allocation methodology, term, termination, access to books and records by the domiciliary regulator). The contract gap matrix must evidence the prescribed clauses where the vendor is an affiliate.

- **NAIC Producer Licensing Model Act** [verify model number]: any vendor exercising binding or producer authority requires per-state producer licensing. The contract must reflect the per-state authorisation, including limitations on binding authority and termination triggers on licence loss.

- **NAIC Unfair Trade Practices Act (Model #880)** and the carrier's state-by-state unfair-claims-settlement-practices acts: where the vendor sits in a claims process, the contract must support the carrier's compliance with the acts (timing, customer-communication, fair-dealing standards). Pass-through accountability does not absolve the carrier; the contract clauses must enable the carrier's oversight.

- **State Department of Insurance bulletins** on specific outsourced functions where the carrier is licensed; pin the bulletins by state and date.

#### ORSA and ERM fit

- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number]: critical outsourced functions belong in the ORSA Summary Report. Contracts for ORSA-fit vendors must include the information-access clauses that enable the carrier to populate the ORSA narrative (operational-resilience evidence, sub-contractor footprint, exit posture).

#### AI vendor mode at an insurer

When `ai_vendor=true` and the firm is an insurer:

- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023)**: the carrier remains accountable for vendor and third-party AI used on its policies. The contract gap matrix must include rows for AIS-Program-aligned vendor obligations: governance access, validation evidence access, third-party-AI accountability flow-down, monitoring evidence access, documentation access, transparency to the carrier, fairness-testing cooperation. State-by-state adoption; consult the NAIC AI Working Group adoption tracker.

- **Colorado SB 21-169 implementing regulation** (3 CCR 702-10 §1 [verify section]) and parallel state regulations on ECDIS and predictive models in life-insurance underwriting: the contract must support governance, testing, validation, and consumer-recourse obligations the carrier holds. https://doi.colorado.gov/ [verify exact citation].

- **NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting** (January 2024) [verify exact circular number]: equivalent contract reach for NY-licensed life carriers.

#### Cross-link inside the plugin

- **`exit-plan` insurance overlay** carries the in-force-policy-servicing wind-down sequence, the regulator-notification posture for an outsourced critical function, and the Form D filing implications for an affiliate-services exit. The contract gap matrix should evidence the contract clauses that enable each of those exit steps.

#### Common insurance pitfalls

- Missing the §4.F clause set on a TPA or MGA contract because the federal interagency-guidance frame was applied alone. The federal frame does not cover §4.F third-party-service-provider contract terms.
- Missing the Form D clause set on an affiliate-services agreement. Affiliate-services contracts have prescribed content under Model #450; absence is a `high`-severity finding.
- Reading "AIS Program elements" as a single clause. The Bulletin lists multiple program elements; each translates into a distinct contract-row obligation on the vendor.
- Treating producer-licensing as procurement's problem. The contract must reflect per-state authorisation and the licence-loss termination trigger; it is a contract-row finding.

## payments-fintech

### Payments-fintech sector overlay — contract-gap-review

When the scope flags payments or fintech (sponsor-bank programs, BaaS platforms, money transmitters, MSBs, card-program operators, processors), load this overlay alongside `references/source-anchors.md`.

#### Operative supervisory frame

- **Interagency Guidance on Third-Party Relationships: Risk Management** (OCC / FRB / FDIC, June 6, 2023) is the spine for any bank-side review of a fintech counterparty contract.
- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact date and title] is the operative document for sponsor-bank programs. The contract gap matrix on a BaaS or program-operator counterparty must cover: end-customer reconciliation responsibilities and frequency; FBO subledger ownership, access, and reconciliation; deposit-insurance representation review (and customer-facing FDIC framing); program-operator operational-resilience commitments; and the fourth-party register with change-notice mechanism. The 2023 RFI on bank-fintech arrangements is not the binding statement; cite-checks must catch the conflation [verify which artifacts are operative on the date of analysis].
- **FFIEC inter-agency joint statement on community-bank fintech due diligence** (August 2023) [verify exact title]: where the firm is a community bank engaging a fintech, this statement carries an explicit contract-checklist.

#### Vendor-type taxonomy

The matrix must identify the counterparty's role on each rail and across the program: sponsor bank, BaaS platform / program manager, processor (front-end, back-end, gateway), BIN sponsor, ledger provider, card-issuance vendor, KYC / CIP vendor, fraud-decision vendor, sanctions-screening vendor, dispute-management vendor, FedNow / RTP gateway, ACH originator, ACH Third-Party Sender. Each pulls a distinct contract-clause set.

#### Network and rule-based contract clauses

- **NACHA Operating Rules (current edition)** Originator and Third-Party Sender agreements; Third-Party Sender registration and risk-management terms [verify rule citations]. The contract must reflect the rule-required terms, the warranties allocated by NACHA to each party, and the audit-cooperation expectations. Paywalled; cite as "current edition" and pin against the firm's licensed copy.

- **Card-network operating rules (Visa, Mastercard, Amex, Discover)**. Required terms in issuer-processor and acquirer-merchant contracts; chargeback rules; PCI compliance representations; data-handling commitments; brand-protection terms. Paywalled; cite as "current edition" and pin against the firm's licensed copy.

- **Reg E (12 CFR Part 1005)** §1005.6, §1005.11, §1005.18 — error-resolution and customer-liability allocation. The contract must support the firm's Reg E obligations end-to-end, including evidence handover, dispute-decision allocation, and prepaid-account rule reach where applicable.

- **Reg Z (12 CFR Part 1026)** for credit-products — billing-error and disclosure obligations the contract must support.

#### Money transmission and MSB

- **FinCEN MSB rules at 31 CFR Part 1022** and registration requirements at 31 CFR §1022.380 (initial registration within 180 days; renewal every two years). The agent-of-MSB and Third-Party-Relationship contract has specific content expectations: AML-program responsibilities, monitoring, registration evidence, termination triggers tied to regulatory action. Note: 31 CFR §1010.380 is the separate BOI / Corporate Transparency Act reporting rule, not the MSB-registration cite.
- **State money-transmission licences**: the contract for a vendor that touches funds-flow may need to reflect per-state licensing posture, consumer-protection bond evidence, and complaint-handling chain.

#### Larger-participant rule

- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (December 2024) [verify Federal Register citation and current state including any litigation or congressional review]. Where the firm or the vendor crosses the threshold, the contract may need to reflect CFPB supervision-cooperation expectations.

#### Sponsor-bank-program-specific clause expansions

When the contract is a sponsor-bank program agreement or BaaS platform agreement, the standard clause set expands to include:

- End-customer reconciliation responsibilities and frequency.
- FBO subledger ownership, access, and reconciliation cadence.
- Deposit-insurance representation review (and the customer-facing FDIC framing).
- Program-operator operational-resilience commitments including BCDR test evidence and impact-tolerance alignment.
- Fourth-party register and the change-notice mechanism.
- BSA / AML responsibility allocation including SAR-decision authority.
- Customer-liability allocation under Reg E and Reg DD.
- Complaint-handling chain (including CFPB complaint routing).
- Data-portability on termination (account-level, transaction-level, customer-record-level).
- Wind-down obligations protective of end-customers.

#### Cross-link inside the plugin

- **`exit-plan` payments-fintech overlay** carries the funds-flow wind-down, the FBO-account close-out sequence, the customer-notice obligations, and the network-orderly-exit posture. The contract gap matrix should evidence the contract clauses that enable each of those exit steps.

#### Common payments-fintech pitfalls

- Treating the standard generic clause set as sufficient for a BaaS program agreement. The standard set undercovers; the overlay adds the program-specific rows.
- Missing the customer-liability-allocation row. Reg E allocates liability to the bank; the contract must support the bank's recovery posture against the program operator.
- Confusing the 2023 RFI on bank-fintech arrangements with the July 2024 Joint Statement. The Joint Statement is the operative artifact; the RFI is informational.
- Treating "PCI compliance" as a single contract row. PCI obligations sit across data-handling, breach-notification, audit-cooperation, and remediation rows.
