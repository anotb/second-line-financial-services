# Payments-fintech sector overlay — exit-plan

When the scope flags payments or fintech (BaaS programs, payment processors, prepaid issuers, MSBs, digital-payment apps), load this overlay alongside `references/source-anchors.md`. Settlement-network access continuity and regulated-customer-notice clocks are the dominant exit-planning constraints.

## Operative supervisory frame

- **NACHA Operating Rules (current edition)** — Third-Party Sender registration, ODFI risk-management responsibilities, and termination notice posture [verify rule citations]. Paywalled; cite as "current edition; specific rules confirmed against the firm's licensed copy".
- **FedNow Service Operating Procedures and RTP Operating Rules** [verify exact citations and current editions] — settlement-network access continuity on a processor transition.
- **Card-network rules (Visa, Mastercard, Amex, Discover) — current editions** [paywalled]. BIN-sponsorship transition, account-range portability, dispute-history portability.
- **Reg E, 12 CFR Part 1005** — §1005.8 change-in-terms notification on EFT services; §1005.18 prepaid-account specific provisions including pre-acquisition notice for customer-impactful changes.
- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (December 2024) [verify Federal Register citation and current state]. Where applicable, exit planning at a covered participant must reflect the supervisory posture.
- **FinCEN MSB rules at 31 CFR Part 1022** — MSB registration continuity if the transition changes registered-entity status [verify §].
- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date] — operative for sponsor-bank programs; the program-end mechanics are the partner bank's responsibility.
- **FFIEC inter-agency joint statement on community-bank fintech due diligence** (August 27, 2021, FIL-59-2021) [verify exact title and date] — termination considerations in BaaS arrangements.

## Settlement-network access continuity

- **ACH processor transition** — RDFI / ODFI continuity through cutover; in-flight ACH file handling; return-and-NOC traffic re-routing; NACHA-rule compliance during the transition; same-day-ACH window handling.
- **RTP / FedNow transition** — service-provider routing changes; participant-ID continuity; idempotency-key handling across the seam; settlement-bank-of-record changes.
- **Card-network transition (BIN sponsorship change)** — BIN-portability requests where supported by the network; card-reissuance posture if BIN reassignment is required; dispute-history portability; PCI-DSS posture preserved through the cutover; chargeback continuity.
- **Wire / Fedwire transition** — Fedwire participant-ID continuity; correspondent-bank arrangement transition.
- **Settlement-bank transition (for prepaid issuers, payroll-card issuers, money transmitters)** — settlement-of-record change, customer funds movement, FBO-account handling.

## Customer-notice (payments-fintech)

- **Reg E §1005.8** change-in-terms — the operative clock for most customer-impactful changes on a consumer EFT service. Twenty-one days advance notice is the common anchor; pin to the operative rule on the day [verify current periods].
- **Reg E §1005.18** prepaid pre-acquisition disclosures — where the transition changes terms a prospective prepaid-customer would see at acquisition.
- **Card-issuer cardholder agreements** — agreement-amendment clocks under network rules and applicable consumer-protection statutes.
- **State money-transmitter customer-notice statutes** — where the transition affects remittance-customer terms or the regulated entity providing the service.

## BaaS program exits

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

## AI vendor mode in payments-fintech

When `ai_vendor=true`:

- **Fraud-decisioning model transition** — substitute model's diligence, validation, and Reg E-compliance posture (where AI denies a transaction or holds funds, customer-facing impact must remain auditable). Cross-link to `vendor-diligence` and `llm-vendor-evidence-review`.
- **AI-driven compliance-decisioning (KYC, sanctions, AML)** — substitute model's regulator-facing audit posture; transition-period dual-running for false-negative analysis.
- **Customer-facing AI (chatbot, support assistant)** — Reg E and CFPB UDAAP-equivalent posture on the substitute system.
- **CFPB larger-participants supervision** — where applicable, supervisory engagement on AI-vendor transitions affecting customer-facing decisions.

## Cross-link inside the plugin

- **`vendor-diligence` payments-fintech overlay** carries the diligence depth the exit plan consumes; the substitute processor's diligence pack is a precondition to transition.
- **`contract-gap-review` payments-fintech overlay** carries the BaaS clause set, the sponsor-bank-program agreement clauses, and the network-rule flow-down clauses.
- **`concentration-risk-review`**: BIN-sponsor, processor, KYC-vendor, and fraud-decision-vendor concentration drives substitute viability.

## Output-template additions for payments-fintech

- Settlement-network and rail named, with cutover-window posture as a named line under transition target options.
- Reg E §1005.8 / §1005.18 customer-notice clock as a named line.
- BIN-sponsorship transition mechanics as a named line for card-issuer transitions.
- BaaS program-end mechanics as a named section for sponsor-bank arrangements (FBO, end-customer reconciliation, deposit-insurance representation, sponsor-bank notice responsibility).
- CFPB larger-participants supervisory engagement posture (where applicable).

## Common pitfalls in payments-fintech exit planning

- Treating a processor exit as a vendor-only transition. Settlement-network access continuity is the dominant constraint and frequently dictates the timeline.
- Skipping the in-flight transaction handover. Returns, NOCs, chargebacks, and disputes have their own clocks that survive the vendor transition.
- Missing the Reg E §1005.8 (or §1005.18) advance-notice clock on a customer-impactful change.
- Treating BaaS program-end as the program-operator's problem. The sponsor bank carries customer-notice responsibility, deposit-insurance-representation responsibility, and end-customer reconciliation responsibility.
- Skipping the Joint Statement (July 2024) element checklist on sponsor-bank transitions.
- Treating BIN reassignment as routine. Card reissuance, dispute-history portability, and PCI-DSS posture must be planned.
- Missing CFPB larger-participants supervisory engagement on an in-scope digital-payment-app transition.
