# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — exit-plan

When the scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the banking-only frame the generic capability skill does not own.

#### Operative supervisory frame

- **Interagency Guidance on Third-Party Relationships: Risk Management** (June 6, 2023) termination expectations are the spine. Apply on a risk-based basis; community-bank tailoring narrative is the right anchor for smaller institutions.
- **OCC Bulletin 2013-29** is still cited as the predecessor framing in supervisory practice; treat as supplemental.
- **FFIEC IT Examination Handbook — Outsourcing Technology Services and Business Continuity Management booklets** are examiner-facing detail. Pin the current edition for both.
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for $50B+ covered banks: the exit plan and its testing posture feed the risk-governance framework and the board's third-party oversight. The board should see the exit-plan testing cadence and outcomes for critical and important arrangements.
- **FRB SR 12-17 consolidated supervision framework** for BHCs: where the vendor sits across legal entities or supports a consolidated activity, the exit plan reflects the BHC view, not just the depository view.

#### Banking-only termination clause anchor

- **Bank Service Company Act, 12 USC §1867(c)** — examiner-access right continues through wind-down. The contract must preserve regulator examination access and audit rights into the transition window; the plan must show the actual evidence-preservation choreography (which logs, by whom, with what retention) so that an examiner asking after cutover can still get the records.

#### Customer-notice anchors (banking)

- **Reg DD, 12 CFR §1030.5** — change-in-terms notification on deposit accounts. Drives the customer-notice clock for any transition that changes the customer experience on a deposit account (statement format, fee structure, IVR or app behaviour, account-number reformatting).
- **Reg E, 12 CFR §1005.8** — change-in-terms notification on consumer-EFT services (debit, bill-pay, electronic transfers). Where the transition changes terms governing EFT services, the longer of the two clocks usually controls.
- **Reg Z, 12 CFR §1026.9** — change-in-terms on open-end consumer credit accounts where applicable [verify subsection].

#### FBO-account wind-down (sponsor-bank arrangements)

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. Where the exit-plan covers a fintech program operator or BaaS platform, specific elements:
  - End-customer reconciliation through the cutover with a per-customer ledger reconciliation.
  - FBO subledger validation against the bank's GL, with the seam dated.
  - Deposit-insurance representation: the customer-facing FDIC framing must remain accurate through and after the transition.
  - Customer-notice: program-end notice to end-customers is a sponsor-bank responsibility that cannot be delegated only to the program operator.
  - Fourth-party register: processor, KYC vendor, fraud-decision vendor, ledger provider all in the transition scope.

#### OCC Heightened Standards considerations

- For $50B+ covered banks, the exit plan and its test history feed the risk-governance framework. The independent risk-management function must see the plan; the board sees the testing cadence and outcomes for critical arrangements.
- Material vendor changes are commonly inside the firm's risk-appetite policy and need RAS-aligned reporting on transition.

#### AI vendor mode at a bank

When `ai_vendor=true` and the firm is a bank:

- **Joint interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026)** applies where the vendor supplies a **traditional statistical, quantitative, or non-generative, non-agentic AI model** used in a credit, compliance, or fraud decision. The guidance is most relevant to banking organisations with total assets over $30B and is non-binding (does not set forth enforceable standards). For an in-scope traditional model, exit planning must address model-risk continuity (substitute model evaluation, transition-period decisioning posture, model-risk-committee approval of the substitute). Footnote 3 of the guidance text excludes generative and agentic AI from scope.
- **For GenAI or agentic AI vendors**, the model-risk continuity lens routes to NIST AI 600-1 (Generative AI Profile), the NIST AI Risk Management Framework, the EU AI Act where the EU subsidiary is in scope, and the firm's AI-governance framework rather than to 2026-13. The transition-engineering work (prompt-template portability, RAG migration, model-version pin handling, guardrail and eval porting, agent-tool offboarding) sits in the AI-specific transition section of the plan; the regulatory anchor for the substitute's evaluation is the AI-governance frame.
- **Bank Service Company Act §1867(c)** examination access still applies on AI-vendor exit (traditional or GenAI). Audit logs, evaluation evidence, and incident-response records must be preserved through the transition.
- **OCC and FRB supervisory letters on AI use in banking** where applicable [verify specific letters relevant on the date of analysis].
- Cross-link to `llm-vendor-evidence-review` for the substitute model's evidence-pack review.

#### Cross-link inside the plugin

- **`vendor-diligence` banking overlay** carries the diligence depth the exit plan consumes via the diligence record (subcontractors, data_access, residual_risk).
- **`contract-gap-review` banking overlay** carries the Bank Service Company Act clause set, the regulator-directed-termination clause expectation, and the BaaS deposit-insurance-representation clauses; the exit plan flags clause gaps and chains for the clause-by-clause read.
- **`concentration-risk-review`**: hyperscaler region, BaaS sponsor-bank reach, and core-banking vendor concentration drive the substitute-vendor viability read.
- **`resilience-testing-pack` banking overlay**: the exit-rehearsal scenario set sits inside the integrated test programme.

#### Output-template additions for banking

- Bank Service Company Act §1867(c) examination-access continuity posture as a named line under supervisory readiness.
- Reg DD §1030.5 and Reg E §1005.8 lead-time calculation as named entries under customer notice.
- Joint-statement element status under fourth-party dependencies for sponsor-bank arrangements.
- OCC Heightened Standards board-visibility status (only for $50B+ covered banks).

#### Common pitfalls in banking exit planning

- Treating the vendor's transition-assistance commitment as the plan. The clause is not the playbook.
- Skipping Bank Service Company Act §1867(c) preservation choreography. Examiner access continues through wind-down whether or not the contract says so.
- Missing the longer of the Reg DD and Reg E change-in-terms clocks on a transition that affects both services.
- Treating a sponsor-bank-program exit as a pure operational matter. End-customer reconciliation and deposit-insurance representation are bank-licensed responsibilities, not delegatable to the program operator.
- Skipping consolidated-supervision lens at a BHC.
- Treating an AI-vendor exit as just-another-vendor exit. The model-risk continuity and the substitute model's evaluation are part of the plan, not a separate workstream.

## capital-markets

### Capital-markets sector overlay — exit-plan

When the scope flags capital markets (advisers, broker-dealers, registered funds, asset managers), load this overlay alongside `references/source-anchors.md`. The bank-flavoured interagency-guidance termination frame is not the operative supervisory frame for SEC and FINRA registrants. Capital-markets exit plans for fund service-provider transitions are the most substantive sub-domain in this overlay.

#### Operative supervisory frame

- **Investment Advisers Act Rule 206(4)-7** — adviser compliance-program rule. Service-provider transitions must be reflected in the adviser's policies and procedures and in CCO oversight.
- **Investment Company Act Rule 38a-1(a)(4)** — fund compliance-program rule, including service-provider compliance-program-adequacy assessment for transfer agent, custodian, fund accountant, principal underwriter, valuation designee, pricing services. The fund CCO oversees; the fund board approves transitions of these critical service providers.
- **Investment Company Act §15** — investment advisory contracts; shareholder-vote thresholds and interim-contract authority on adviser or sub-adviser changes. **Rule 15a-4 interim contracts** carries the interim-period authority. Where the exit plan transitions an adviser or sub-adviser arrangement, ICA §15 and Rule 15a-4 are the operative spine.
- **Form N-CEN** — annual census report; service-provider-change disclosure for registered funds [verify the exact items that pick up service-provider changes].
- **FINRA Rule 3110 (supervision)** — for broker-dealers, supervisory continuity through vendor transitions.
- **Reg SCI — 17 CFR §242.1000 et seq.** — substitutability and BCDR posture for SCI entities; exit plans for SCI-system vendors must address Reg SCI substitutability expectations [verify subsection].

#### Books-and-records continuity

- **Investment Advisers Act Rule 204-2** — adviser books-and-records preservation continues through and after transition. Record formats, retention periods, and reproducibility-on-demand must survive cutover.
- **17 CFR §240.17a-4** — broker-dealer books-and-records preservation continues. The vendor's records that fall in the firm's 17a-4 scope must be returned in a format meeting the rule, including the preservation-medium requirements.
- **Rule 31a (under the Investment Company Act)** — fund records continuity.
- **Reg S-P (May 2024 amendments)** [verify exact compliance dates] — customer-information treatment on termination of a service-provider arrangement; service-provider written-contract elements including breach-notification carry through.

#### Fund service-provider transitions

This is the sub-domain where capital-markets exit planning carries the most weight. The named service providers under Rule 38a-1(a)(4) and the operative transition mechanics:

- **Transfer agent transition** — shareholder-record continuity; SAR position reconciliation; tax-cost-basis and 1099 reporting continuity across the cutover; advance-notice to record holders; coordination with NSCC for fund-supermarket distribution; Form N-CEN update.
- **Custodian transition** — qualified-custodian status continuity under Rule 206(4)-2; surprise-audit posture across the cutover; account-statement delivery continuity; SLOA inventory reconciliation; sub-custody arrangements; fund-board notice and approval.
- **Fund accountant transition** — NAV calculation continuity and dual-running across the cutover; pricing-source continuity; tax-lot accounting; fund expense accruals; 1099 reporting; fund-board notice and approval.
- **Pricing-services transition** — methodology continuity; fair-valuation governance under **Rule 2a-5**; pricing-vendor diligence under Rule 38a-1(a)(4) for the substitute.
- **Sub-adviser transition** — ICA §15 shareholder-vote threshold; Rule 15a-4 interim-contract authority; portfolio-handover mechanics including in-flight trade settlement; soft-dollar and affiliated-broker conflict carry-over; Form ADV Part 2A Item 10 and Item 14 updates; fund-board approval.
- **Adviser transition** — full ICA §15 process; Rule 15a-4 interim contract; Form ADV-W on termination of the outgoing adviser if applicable; fund-board approval; shareholder vote.
- **Principal-underwriter transition** — selling-agreement re-papering; sales-load and 12b-1 fee continuity.
- **Valuation-designee transition** under Rule 2a-5 — fund-board oversight and approval.

#### Outsourced CCO transition

- Where the vendor is an outsourced CCO or compliance-service provider, the SEC's 2022 Risk Alert sets the bar [verify exact title and date]. Transition mechanics:
  - CCO-of-record handover with the seam dated.
  - Independence, resourcing, expertise, and access-to-information all re-evidenced on the substitute.
  - Reporting-line clarity to the adviser's senior management or the fund board re-established before the transition is effective.

#### Form ADV currency on transition

- **Form ADV Part 2A Item 10 and Item 14** — material-relationship disclosures must be updated on substantive vendor changes. Brochure amendment cycle is part of the customer-notice posture for advisers.

#### AI vendor mode for advisers and BDs

When `ai_vendor=true`:

- **SEC focus on AI / predictive analytics in adviser practices** — risk-alert and rulemaking activity has been ongoing; pin the current state on the date of analysis [verify].
- **Marketing Rule (Rule 206(4)-1)** — AI-generated marketing-content vendor transition must address content-retention and recordkeeping posture including the substitute model's marketing-content production.
- **Reg BI care obligation** for broker-dealers — AI-driven recommendation transitions must keep the BD's documentation of the care analysis intact.
- **Rule 204-2 books-and-records** — AI outputs supporting investment decisions must remain retrievable post-transition.
- Cross-link to `llm-vendor-evidence-review` for the substitute model's evidence-pack review.

#### Fund-board reach

- **Rule 38a-1(a)(4)** — fund-board notice or approval for material service-provider changes (custodian, transfer agent, fund accountant, sub-adviser, valuation designee, principal underwriter, pricing services).
- **ICA §15** — shareholder-vote thresholds for adviser and sub-adviser changes; Rule 15a-4 interim contracts carry the interim authority.
- The fund board's review of the substitute service-provider's compliance program is part of the transition; the exit plan carries the timing of board materials and the package contents.

#### Cross-link inside the plugin

- **`vendor-diligence` capital-markets overlay** carries the diligence depth the exit plan consumes; the substitute service-provider's diligence pack is a precondition to transition.
- **`contract-gap-review` capital-markets overlay** carries the Reg S-P clause set, the Custody Rule SLOA terms, the sub-adviser code-of-ethics clauses, and the Reg SCI terms; clause gaps surfaced here flag the exit-readiness gap.
- **`concentration-risk-review`** flags fund-administrator, custodian, and sub-adviser concentration that drives substitute-service-provider viability.

#### Output-template additions for capital markets

- Registration-class scoping line: adviser, BD, registered fund, dual-registrant, state-registered IA.
- Service-provider category against Rule 38a-1(a)(4) when the firm is a fund adviser or trustee.
- Custody Rule applicability check.
- Reg S-P treatment-of-customer-information posture as a named line.
- ICA §15 / Rule 15a-4 path as a named line for adviser or sub-adviser transitions.
- Form N-CEN update trigger as a named line.
- Form ADV Part 2A Item 10 / Item 14 amendment trigger as a named line.
- Fund-board notice and approval timing as a named line for fund service-provider transitions.

#### Common pitfalls in capital-markets exit planning

- Importing the bank-flavoured interagency-guidance frame as if it were operative for an adviser or BD. The capital-markets supervisory frame runs through Rule 206(4)-7, Rule 38a-1, ICA §15, FINRA Rule 3110, and Reg S-P, not through the June 2023 interagency guidance.
- Missing the fund-board notice / approval path for service-provider changes at a registered fund.
- Treating an outsourced-CCO transition as a routine vendor change. CCO-of-record handover is a compliance-program-design transition.
- Missing the Reg S-P (May 2024) treatment-of-customer-information clauses on a transition that pre-dates the amendments.
- Treating Rule 204-2, Rule 17a-4, and Rule 31a books-and-records continuity as a vendor problem. The firm remains responsible regardless of vendor transition.
- Skipping ICA §15 and Rule 15a-4 sequencing on adviser or sub-adviser transitions.
- Missing Reg SCI substitutability expectations on SCI-system vendor transitions.
- Missing fair-valuation-governance considerations under Rule 2a-5 on a pricing-vendor transition.

## insurance

### Insurance sector overlay — exit-plan

When the scope flags insurance, load this overlay alongside `references/source-anchors.md`. The bank-flavoured interagency-guidance termination frame is not the operative supervisory frame for state-regulated insurers.

#### Operative supervisory frame

- **State insurance department oversight** — the operative regulatory relationship is state-by-state. The exit plan reflects the carrier's domiciliary regulator first, then material-state regulators where the transition affects in-force policyholders.
- **NAIC Insurance Holding Company System Regulatory Act (Model #440)** [verify model number] and **Holding Company Model Regulation (Model #450)** [verify model number]: where the vendor is an affiliate of the carrier, transition triggers Form B / Form D filings.
- **NAIC Insurance Data Security Model Law (Model #668), §4.F** — third-party service-provider obligations including transition data-handling. State-by-state adoption.
- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number] — critical outsourced functions sit in the ORSA. A vendor-transition affecting a critical outsourced function updates the ORSA Summary Report.

#### Policyholder-facing transitions

- **Policy administration platform exit** — the most common high-impact insurance vendor transition. Considerations:
  - Portability of policy administration data, in-force-policy schedules, billing histories, and claims-in-flight state.
  - Customer-facing change-of-servicer notice. Required content and timing vary by state and product line; pin to the operative state insurance code on the day [verify state-by-state].
  - Producer-channel notice where the producer relationship rides on the platform (commission accruals, agent-of-record tagging).
- **Claims TPA transition** — claims-handling continuity is policyholder-facing on the day. Considerations:
  - In-flight claim handover with the seam dated for state-of-record purposes.
  - Reserve continuity (case reserves and IBNR) across the cutover; actuarial sign-off on the substitute TPA's reserve methodology.
  - Reinsurance reporting continuity — ceded-reinsurance reporting must cover both legs of the transition.
  - Statutory unfair-claims-practices clocks continue to run during transition.
- **Pricing and underwriting vendor transition** — for life and health, ECDIS / predictive-model vendor transitions trigger:
  - **Colorado SB 21-169** governance considerations (3 CCR 702-10 §1 [verify section]) for life-insurance underwriting models.
  - **NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting** (January 2024) [verify exact circular number] considerations.
  - The substitute model's diligence and validation belong to model-risk management; chain to `vendor-diligence` and to `validation-plan` as appropriate.

#### Guaranty-fund and policyholder-protection considerations

- State guaranty associations protect policyholders on insolvency of a carrier; vendor exit at a healthy carrier does not trigger guaranty-fund mechanics, but the customer-facing communications must avoid implying an insolvency posture.
- Where the transition is driven by carrier financial distress, the state insurance department leads and the exit plan becomes a sub-plan of the broader resolution work.

#### Affiliate-vendor transition

- Where the vendor is an affiliate (Form B / Form D filings on the way in), termination requires Form D filings and may trigger state regulator review under the Holding Company Model Act.
- Affiliate cost-allocation arrangements and tax-sharing implications belong in the plan even when the operational migration is straightforward.

#### AI vendor mode at an insurer

When `ai_vendor=true` and the firm is an insurer:

- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers** (December 4, 2023). Carrier accountability for vendor and third-party AI continues through transition. The substitute vendor's AIS Program elements (governance, risk management, testing, validation, third-party-AI accountability, monitoring, documentation, transparency, fairness) are part of the substitute-vendor viability read.
- **State adoption tracker** — the NAIC AI Working Group adoption tracker is the public reference. Transition timing must respect any state-specific notification or filing on AI use changes [verify state-by-state].
- Cross-link to `llm-vendor-evidence-review` for the substitute model's evidence-pack review.
- For Annex III high-risk classification under the EU AI Act (insurance pricing and risk-assessment in life and health) where applicable, transition planning must address regulatory continuity for the substitute system [verify Annex III item number].

#### Cross-link inside the plugin

- **`vendor-diligence` insurance overlay** carries the diligence depth the exit plan consumes.
- **`contract-gap-review` insurance overlay** carries the NAIC Model #668 §4.F clause set and the affiliate-vendor termination clauses.
- **`concentration-risk-review`** flags claims-TPA, policy-administration-platform, and ECDIS-vendor concentration that drives substitute-vendor viability.

#### Output-template additions for insurance

- Domiciliary regulator and material-state regulator notification posture as a named line under regulator notice.
- Producer-channel notice as a named line under customer notice.
- ORSA-update trigger flag where the vendor supports a critical outsourced function.
- Form B / Form D filing trigger for affiliate-vendor termination.
- For claims TPA transitions, in-flight-claim handover with reserve-continuity and reinsurance-reporting lines.

#### Common pitfalls in insurance exit planning

- Treating insurance vendor exit as a bank-style transition. The state regulatory lens, the policyholder-facing notice considerations, and the affiliate-vendor filing path are insurance-specific.
- Skipping the producer-channel notice. The producer relationship is part of the transition impact on a policy-administration-platform exit.
- Missing the in-flight-claim handover seam on a TPA transition. State-of-record continuity for unfair-claims-practices clocks, reserves, and reinsurance reporting must be dated.
- Treating an ECDIS or pricing-model vendor exit as a routine vendor exit. State AI governance and model-risk continuity are part of the plan.
- Missing the ORSA-update trigger on transition of a critical outsourced function.

## payments-fintech

### Payments-fintech sector overlay — exit-plan

When the scope flags payments or fintech (BaaS programs, payment processors, prepaid issuers, MSBs, digital-payment apps), load this overlay alongside `references/source-anchors.md`. Settlement-network access continuity and regulated-customer-notice clocks are the dominant exit-planning constraints.

#### Operative supervisory frame

- **NACHA Operating Rules (current edition)** — Third-Party Sender registration, ODFI risk-management responsibilities, and termination notice posture [verify rule citations]. Paywalled; cite as "current edition; specific rules confirmed against the firm's licensed copy".
- **FedNow Service Operating Procedures and RTP Operating Rules** [verify exact citations and current editions] — settlement-network access continuity on a processor transition.
- **Card-network rules (Visa, Mastercard, Amex, Discover) — current editions** [paywalled]. BIN-sponsorship transition, account-range portability, dispute-history portability.
- **Reg E, 12 CFR Part 1005** — §1005.8 change-in-terms notification on EFT services; §1005.18 prepaid-account specific provisions including pre-acquisition notice for customer-impactful changes.
- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (December 2024) [verify Federal Register citation and current state]. Where applicable, exit planning at a covered participant must reflect the supervisory posture.
- **FinCEN MSB rules at 31 CFR Part 1022** — MSB registration continuity if the transition changes registered-entity status [verify §].
- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date] — operative for sponsor-bank programs; the program-end mechanics are the partner bank's responsibility.
- **FFIEC inter-agency joint statement on community-bank fintech due diligence** (August 27, 2021, FIL-59-2021) [verify exact title and date] — termination considerations in BaaS arrangements.

#### Settlement-network access continuity

- **ACH processor transition** — RDFI / ODFI continuity through cutover; in-flight ACH file handling; return-and-NOC traffic re-routing; NACHA-rule compliance during the transition; same-day-ACH window handling.
- **RTP / FedNow transition** — service-provider routing changes; participant-ID continuity; idempotency-key handling across the seam; settlement-bank-of-record changes.
- **Card-network transition (BIN sponsorship change)** — BIN-portability requests where supported by the network; card-reissuance posture if BIN reassignment is required; dispute-history portability; PCI-DSS posture preserved through the cutover; chargeback continuity.
- **Wire / Fedwire transition** — Fedwire participant-ID continuity; correspondent-bank arrangement transition.
- **Settlement-bank transition (for prepaid issuers, payroll-card issuers, money transmitters)** — settlement-of-record change, customer funds movement, FBO-account handling.

#### Customer-notice (payments-fintech)

- **Reg E §1005.8** change-in-terms — the operative clock for most customer-impactful changes on a consumer EFT service. Twenty-one days advance notice is the common anchor; pin to the operative rule on the day [verify current periods].
- **Reg E §1005.18** prepaid pre-acquisition disclosures — where the transition changes terms a prospective prepaid-customer would see at acquisition.
- **Card-issuer cardholder agreements** — agreement-amendment clocks under network rules and applicable consumer-protection statutes.
- **State money-transmitter customer-notice statutes** — where the transition affects remittance-customer terms or the regulated entity providing the service.

#### BaaS program exits

This is the substantive sub-domain in payments-fintech. A BaaS program exit is a sponsor-bank, program-operator, and end-customer transition simultaneously.

- **Joint Statement on Banks' Arrangements with Third Parties (July 2024)** [verify title and date] elements that the exit plan must address:
  - End-customer reconciliation through the cutover with a per-customer ledger reconciliation.
  - FBO subledger validation against the bank's GL with the seam dated.
  - Deposit-insurance representation: the customer-facing FDIC framing must remain accurate; on program end, customer-facing materials cannot imply continuing FDIC pass-through where the substitute does not provide it.
  - Customer-notice on program end is the sponsor bank's responsibility, not delegable solely to the program operator.
  - Fourth-party register: processor, KYC vendor, fraud-decision vendor, ledger provider, card-issuer-processor, all in the transition scope.
- **End-customer outcomes**:
  - Customer fund availability through and after cutover.
  - Account-data return / portability, where the customer is moving to a successor program rather than exiting financial services.
  - Dispute-history continuity for in-flight Reg E disputes.
- **Program-operator residual obligations**:
  - Records preservation under any applicable bank-record-retention obligation.
  - Cooperation with sponsor-bank regulators including post-program supervisory inquiries.

#### AI vendor mode in payments-fintech

When `ai_vendor=true`:

- **Fraud-decisioning model transition** — substitute model's diligence, validation, and Reg E-compliance posture (where AI denies a transaction or holds funds, customer-facing impact must remain auditable). Cross-link to `vendor-diligence` and `llm-vendor-evidence-review`.
- **AI-driven compliance-decisioning (KYC, sanctions, AML)** — substitute model's regulator-facing audit posture; transition-period dual-running for false-negative analysis.
- **Customer-facing AI (chatbot, support assistant)** — Reg E and CFPB UDAAP-equivalent posture on the substitute system.
- **CFPB larger-participants supervision** — where applicable, supervisory engagement on AI-vendor transitions affecting customer-facing decisions.

#### Cross-link inside the plugin

- **`vendor-diligence` payments-fintech overlay** carries the diligence depth the exit plan consumes; the substitute processor's diligence pack is a precondition to transition.
- **`contract-gap-review` payments-fintech overlay** carries the BaaS clause set, the sponsor-bank-program agreement clauses, and the network-rule flow-down clauses.
- **`concentration-risk-review`**: BIN-sponsor, processor, KYC-vendor, and fraud-decision-vendor concentration drives substitute viability.

#### Output-template additions for payments-fintech

- Settlement-network and rail named, with cutover-window posture as a named line under transition target options.
- Reg E §1005.8 / §1005.18 customer-notice clock as a named line.
- BIN-sponsorship transition mechanics as a named line for card-issuer transitions.
- BaaS program-end mechanics as a named section for sponsor-bank arrangements (FBO, end-customer reconciliation, deposit-insurance representation, sponsor-bank notice responsibility).
- CFPB larger-participants supervisory engagement posture (where applicable).

#### Common pitfalls in payments-fintech exit planning

- Treating a processor exit as a vendor-only transition. Settlement-network access continuity is the dominant constraint and frequently dictates the timeline.
- Skipping the in-flight transaction handover. Returns, NOCs, chargebacks, and disputes have their own clocks that survive the vendor transition.
- Missing the Reg E §1005.8 (or §1005.18) advance-notice clock on a customer-impactful change.
- Treating BaaS program-end as the program-operator's problem. The sponsor bank carries customer-notice responsibility, deposit-insurance-representation responsibility, and end-customer reconciliation responsibility.
- Skipping the Joint Statement (July 2024) element checklist on sponsor-bank transitions.
- Treating BIN reassignment as routine. Card reissuance, dispute-history portability, and PCI-DSS posture must be planned.
- Missing CFPB larger-participants supervisory engagement on an in-scope digital-payment-app transition.
