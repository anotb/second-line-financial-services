# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — criticality-assessment

When the scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the banking-only criteria the generic capability skill does not own.

#### Operative supervisory frame

- **Interagency Guidance on Third-Party Relationships: Risk Management** (OCC Bulletin 2023-17, FRB SR 23-4, FDIC FIL-29-2023, June 6, 2023). Criticality is risk-based and proportionate. Activities that pose higher risk warrant more rigorous oversight; community-bank tailoring narrative in the guidance is the right anchor for smaller institutions.
- **OCC Bulletin 2013-29** is still cited in supervisory practice as the predecessor framing for "critical activities".
- **FFIEC Information Technology Examination Handbook — Outsourcing Technology Services and Business Continuity Management booklets** [verify current edition and section structure] for the BIA frame that drives the firm's recovery objectives.
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for covered banks ($50B+): the criticality call feeds the risk-governance framework and the board's third-party oversight. A `critical` call belongs on the risk-committee agenda regardless of vendor spend.

#### Candidate IBS for banks

Important business services at a bank typically include payments (retail, commercial, cards), deposit-account servicing, lending and loan-servicing, custody where in-scope, and credit-decisioning where the bank operates the model. The IBS list is the firm's, not a regulator's; the candidate list above tracks BCBS Principles for Operational Resilience (March 2021) and the supervisory expectations in interagency and PRA materials. Where an arrangement sits on the critical chain of any of these, the criticality call moves toward `critical`.

#### BaaS and bank-fintech-arrangement applicability

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. Where the arrangement is a fintech program operator or BaaS platform, the criticality call must read end-customer reconciliation, FBO subledger, deposit-insurance representation accuracy, and the program-operator's own resilience as inputs to the tier. A BaaS program that touches the deposit-servicing IBS is critical-by-default; flag any other read for explicit rationale.

#### Community-bank tailoring

- **FFIEC inter-agency joint statement on community-bank fintech due diligence** (August 2021, FIL-59-2021) [verify exact title]. Community banks may run a leaner criticality framework, but the IBS test still applies. The tier is set by impact on the IBS, not by the bank's size.

#### Examiner-reach lens

- **Bank Service Company Act, 12 USC §1867(c)**. Statutory examiner-access right over bank service providers. Not a criticality-tier driver on its own, but a reminder that any arrangement at the bank must preserve examiner access; surfaces in `vendor-diligence` and `contract-gap-review` downstream.

#### Cross-link inside the plugin

- **`vendor-diligence` banking overlay** consumes the `tier` and the named IBS to set diligence depth.
- **`exit-plan` banking overlay** consumes the `tier`, the supported IBS, and the customer-impact read to set transition mechanics, including FBO-account wind-down for BaaS arrangements.
- **`concentration-risk-review`** consumes the `concentration_considerations` flag to drive portfolio analysis on hyperscaler region, BaaS sponsor-bank reach, and core-banking vendor concentration.

#### AI vendor mode at a bank

When `ai_vendor=true` and the firm is a bank:

- **Joint interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026)** applies where the arrangement supplies a **traditional statistical, quantitative, or non-generative, non-agentic AI model** used in a credit, compliance, or fraud decision. The guidance is most relevant to banking organisations with total assets over $30B and is non-binding (does not set forth enforceable standards). For an in-scope traditional model, the criticality call considers model-risk impact alongside operational impact; an AI vendor on the credit-decisioning IBS path is rarely below `important`. Footnote 3 of the guidance text excludes generative and agentic AI from scope.
- **For GenAI or agentic AI vendors**, the model-risk lens routes to NIST AI 600-1 (Generative AI Profile), the NIST AI Risk Management Framework, the EU AI Act where the EU subsidiary is in scope, and the firm's AI-governance framework rather than to 2026-13. The criticality call still considers AI-specific impact (decisioning influence, customer harm modes, model-version-pin volatility), but the regulatory anchor is different.
- A `critical` AI-vendor call (traditional or GenAI/agentic) triggers parallel review by the model-risk function downstream; record the cross-link.

#### Output additions for banking

- IBS named explicitly and matched against the candidate list above.
- Recovery-objective gap (firm tolerance vs vendor commitment) called out as a finding line where present.
- BaaS or bank-fintech-arrangement applicability check included where the arrangement is a fintech program.

#### Common pitfalls in banking criticality calls

- Setting tier on procurement category. "IT services" is not a tier; the IBS dependency sets the tier.
- Treating BaaS as a pass-through arrangement. The program operator sits on the deposit-servicing IBS path.
- Missing the consolidated-supervision lens at a BHC. Where the arrangement supports a consolidated activity, the criticality read should reflect the BHC view, not just the depository view.
- Allowing vendor commitment to set the recovery objective. Tolerance comes from the IBS impact analysis.

## capital-markets

### Capital-markets sector overlay — criticality-assessment

When the scope flags capital markets, load this overlay alongside `references/source-anchors.md`. It carries the capital-markets-only criteria the generic capability skill does not own.

#### Operative supervisory frame

- **Investment Advisers Act Rule 206(4)-7** — adviser compliance-program rule. The criticality call frames whether the arrangement supports an adviser-required function.
- **Investment Company Act Rule 38a-1(a)(4)** — fund compliance-program rule, including service-provider compliance-program-adequacy assessment for transfer agent, custodian, fund accountant, principal underwriter, valuation designee, pricing services. A vendor in any of these roles is at minimum `important`; many are `critical`.
- **FINRA Rule 3110 (supervision)** for broker-dealer arrangements that supervise registered persons or carry trade-and-order-handling responsibility.
- **Investment Advisers Act Rule 206(4)-2 (Custody Rule)** — qualified custodian arrangements; the custody chain is critical by construction.
- **Reg SCI — 17 CFR §242.1000 et seq.** Substitutability and BCDR posture for SCI entities; where the arrangement sits on an SCI system path the criticality call reflects the SCI obligations [verify subsection].
- **17 CFR Part 248 (Reg S-P) as amended May 16, 2024** [verify exact compliance dates] — customer-information-safeguarding obligations affect the data-scope and customer-impact reads.

#### Candidate IBS for capital-markets entities

Important business services typically include order management, execution and routing, clearing, settlement, custody, transfer-agency, fund-accounting, NAV calculation and pricing, market-data distribution where the firm operates an SCI system, regulatory-reporting (CAT, EBLM, Form 13F, ADV, N-CEN, N-PORT), and investor communications. The IBS list is the firm's; the candidate list above tracks BCBS Principles for Operational Resilience (March 2021) translated into the capital-markets setting and the named-service-provider construct under Rule 38a-1.

#### Fund-board lens

- For registered funds, the named-service-provider arrangements (transfer agent, custodian, fund accountant, principal underwriter, valuation designee, pricing services, sub-adviser) carry an explicit fund-board-oversight obligation under Rule 38a-1. The criticality call routes through the fund-board secretariat; an annual recertification cycle is the norm.
- **Investment Company Act §15** — investment advisory contracts; sub-adviser additions and replacements need shareholder vote or interim-contract authority under Rule 15a-4. The criticality call for a sub-adviser is `critical` by construction.

#### Cross-link inside the plugin

- **`vendor-diligence` capital-markets overlay** consumes the `tier` and the named IBS to set diligence depth, including 38a-1 service-provider compliance-program-adequacy where applicable.
- **`exit-plan` capital-markets overlay** consumes the `tier`, the supported IBS, and the customer-impact read to set transition mechanics, including books-and-records continuity (Rule 204-2, Rule 17a-4, Rule 31a) and fund-board notice timing.
- **`concentration-risk-review`** consumes the `concentration_considerations` flag for transfer-agent, custodian, fund-accountant, sub-adviser, and pricing-service concentration.

#### AI vendor mode at a capital-markets entity

When `ai_vendor=true`:

- An AI vendor on the order-management, execution-routing, NAV-calculation, or pricing path is rarely below `important`. Where the AI system reaches an SCI-system function, the SCI substitutability and BCDR obligations frame the criticality.
- An AI vendor supporting an adviser's investment process (research summarisation, factor extraction, signal generation) requires an explicit fiduciary lens; the criticality call must reflect adviser fiduciary accountability.
- A `critical` AI-vendor call triggers parallel review by the model-risk and AI governance functions; record the cross-link.

#### Output additions for capital markets

- IBS named explicitly and matched against the candidate list above.
- Named-service-provider-under-38a-1 check for any registered-fund arrangement.
- SCI-system-path applicability check for SCI entities.
- Sub-adviser interim-contract-authority check for adviser-arrangement scenarios.

#### Common pitfalls in capital-markets criticality calls

- Treating a "vendor" as outside the named-service-provider framework when the function it provides is actually a 38a-1 service. Transfer agency, fund accounting, and valuation are named services regardless of how the vendor describes itself.
- Skipping the SCI-system-path test for venues, market-makers, and clearing entities.
- Setting the tier without considering the fund-board oversight cadence. A `critical` call drives a different fund-board reporting line than an `important` call.
- Allowing vendor commitment to set the recovery objective. Tolerance comes from the IBS impact analysis and, for SCI entities, from the SCI BCDR obligations as well.

## insurance

### Insurance sector overlay — criticality-assessment

When the scope flags insurance, load this overlay alongside `references/source-anchors.md`. It carries the insurance-only criteria the generic capability skill does not own.

#### Operative supervisory frame

- **NAIC Insurance Data Security Model Law (Model #668), §4.F** third-party service-provider obligations including a risk-based criticality assessment.
- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number]. Critical outsourced functions belong in the ORSA Summary Report; a `critical` call here flows into the ORSA narrative.
- **NAIC Insurance Holding Company System Regulatory Act (Model #440)** [verify model number] and **Holding Company Model Regulation (Model #450)** [verify model number]. Where the arrangement is intragroup, Form B / Form D filings depend on the affiliated-vendor read; criticality call drives the disclosure shape.
- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers** (December 4, 2023). Carrier accountability for vendor and third-party AI; AIS Program elements (governance, risk management, testing, validation, third-party-AI accountability) inform the criticality read for AI vendors on a regulated decisioning path.

#### Candidate IBS for insurers

Important business services at an insurance carrier typically include claims handling and adjustment, policy administration (issuance, endorsements, renewals), underwriting, premium collection and reconciliation, policyholder communications and disclosures, and reserve and capital reporting. State guaranty-fund and policyholder-protection considerations weight the criticality call upward where the arrangement sits on the policyholder-facing path. The IBS list is the firm's; the candidate list above tracks BCBS Principles for Operational Resilience (March 2021) translated into the insurance setting.

#### State-by-state lens

- **State adoption tracker for the NAIC AI Bulletin** is the public reference; the operative state framework for an AI-driven life-insurance underwriting use case may include **Colorado SB 21-169 implementing regulation** (3 CCR 702-10 §1 [verify section]), the **NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting** (January 2024) [verify exact circular number], and similar state circulars.
- The criticality call considers the state-by-state adoption pattern where the arrangement supports a regulated decisioning path; an AI vendor on the underwriting-decisioning chain in a state with a published AI circular sits at `important` at minimum.

#### Cross-link inside the plugin

- **`vendor-diligence` insurance overlay** consumes the `tier` and the named IBS to set diligence depth, including AIS Program third-party-AI accountability where applicable.
- **`exit-plan` insurance overlay** consumes the `tier`, the supported IBS, and the customer-impact read to set transition mechanics, including policyholder-notice posture and policy-administration data portability.
- **`concentration-risk-review`** consumes the `concentration_considerations` flag for hyperscaler region, claims-TPA reach, and shared-policy-administration-platform concentration.

#### AI vendor mode at an insurer

When `ai_vendor=true` and the firm is an insurer:

- **NAIC AI Bulletin (December 2023)** AIS Program third-party-AI accountability frames the criticality call. An AI vendor on a regulated insurance-decisioning path (underwriting, pricing, claims-decisioning) is rarely below `important`.
- The carrier remains accountable for the AI vendor's decisions reaching policyholders. The criticality call must reflect that the carrier (not the vendor) is the regulated entity for fairness, transparency, and consumer-impact obligations.
- A `critical` AI-vendor call triggers parallel review by the AI governance function downstream; record the cross-link.

#### Output additions for insurance

- IBS named explicitly and matched against the candidate list above.
- ORSA-Summary-Report inclusion check for `critical` calls.
- Holding-company-act applicability check for intragroup arrangements.
- State-by-state lens for AI vendors on regulated decisioning paths.

#### Common pitfalls in insurance criticality calls

- Skipping the policyholder-facing-path test. A vendor that touches policyholder communications, claims, or premium collection sits closer to `critical` than the procurement category suggests.
- Treating an AI vendor as a "tooling" arrangement. Where the AI system reaches a regulated decision, the carrier accountability framework applies and the tier follows.
- Missing the holding-company-act lens for intragroup arrangements. An affiliate vendor still triggers the criticality call and the Form B / Form D filing read.
- Defaulting to the vendor's claimed RTO/RPO as the test. The firm's tolerance from the IBS impact analysis is the test; a state guaranty-fund event is a low-probability high-severity tail that must inform the tolerance.

## payments-fintech

### Payments-fintech sector overlay — criticality-assessment

When the scope flags payments or fintech, load this overlay alongside `references/source-anchors.md`. It carries the payments-fintech-only criteria the generic capability skill does not own.

#### Operative supervisory frame

- **NACHA Operating Rules (current edition)** Third-Party Sender registration and risk-management rules [verify rule citations]. Where the arrangement sits on the ACH path, the rules drive the criticality read.
- **FedNow Service Operating Procedures and RTP Operating Rules** [verify section and current editions]. Settlement-network access continuity for instant-payment rails.
- **Card-network rules (Visa, Mastercard, Amex, Discover) — current editions**. BIN-sponsorship arrangements; the BIN sponsor is critical by construction for any card program.
- **CFPB Reg E (12 CFR Part 1005)** §1005.6, §1005.11, §1005.18. Consumer-EFT and prepaid obligations affect customer-impact reads.
- **FinCEN MSB rules at 31 CFR Part 1022** and registration requirements at 31 CFR §1022.380. KYC/AML utilities and other compliance-rail arrangements get the criticality lens through MSB obligations. Note: 31 CFR §1010.380 is the separate BOI / Corporate Transparency Act rule, not the MSB-registration cite.
- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (December 2024) [verify Federal Register citation and current state]. Where the firm or arrangement is in scope, supervisory exposure shapes the regulatory-impact read.

#### Candidate IBS for payments-fintech entities

Important business services typically include payment authorisation and settlement, payment-network access (FedNow, RTP, ACH, card networks, wire), KYC/CIP and AML transaction monitoring, fraud detection and decisioning, customer ledger and reconciliation, settlement-account servicing, and dispute-and-chargeback handling. The IBS list is the firm's; the candidate list above tracks BCBS Principles for Operational Resilience (March 2021) translated into the payments-fintech setting.

#### BaaS and sponsor-bank lens

- Where the firm is a fintech with a sponsor-bank relationship, the sponsor-bank arrangement is `critical` by construction for any deposit-product program.
- The sponsor-bank-side overlay is in `references/sector-overlays.md#banking`. Read both when the arrangement spans both perimeters; the firm-side criticality and the sponsor-side criticality may differ in scale but should align in tier.
- The 2024 interagency joint statement on bank deposit-product third-party arrangements [verify exact title and date] frames the BaaS criticality read.

#### Cross-link inside the plugin

- **`vendor-diligence` payments-fintech overlay** consumes the `tier` and the named IBS to set diligence depth, including network-rule attestation and BSA-AML control attestation where applicable.
- **`exit-plan` payments-fintech overlay** consumes the `tier`, the supported IBS, and the customer-impact read to set transition mechanics, including settlement-network access continuity, BIN-sponsor transition, and Reg E and NACHA customer-notice posture.
- **`concentration-risk-review`** consumes the `concentration_considerations` flag for processor concentration, BIN-sponsor concentration, and KYC/AML-utility concentration.

#### AI vendor mode at a payments-fintech entity

When `ai_vendor=true`:

- An AI vendor on the fraud-decisioning, AML-transaction-monitoring, or KYC-decisioning path is rarely below `important`. Fair-lending and UDAAP exposure shape the customer-impact and regulatory-impact reads.
- A `critical` AI-vendor call on a regulated decisioning path triggers parallel review by the model-risk and consumer-compliance functions; record the cross-link.

#### Output additions for payments-fintech

- IBS named explicitly and matched against the candidate list above.
- Network-rule applicability check (NACHA, card networks, RTP, FedNow).
- BIN-sponsorship and sponsor-bank applicability check for fintech firms.
- BSA-AML-utility applicability check for KYC/AML and transaction-monitoring arrangements.

#### Common pitfalls in payments-fintech criticality calls

- Setting tier without reading the network-rule perimeter. NACHA Third-Party Sender, card-network BIN-sponsor, and FedNow access carry tier-driving obligations regardless of vendor scale.
- Treating a sponsor-bank arrangement as a "partner" rather than a critical third-party arrangement. The sponsor bank sits on the deposit-product and BSA-AML chain.
- Missing the consumer-compliance lens. Reg E, NACHA, and card-network rules carry consumer-protection clocks that affect customer-impact and notification-trigger reads.
- Defaulting to the vendor's claimed RTO/RPO as the test. The firm's tolerance from the IBS impact analysis (often measured in minutes for instant-payment rails) is the test.
