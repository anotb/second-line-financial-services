# Payments-fintech sector overlay — contract-gap-review

When the engagement scope flags payments or fintech (sponsor-bank programs, BaaS platforms, money transmitters, MSBs, card-program operators, processors), load this overlay alongside `references/source-anchors.md`.

## Operative supervisory frame

- **Interagency Guidance on Third-Party Relationships: Risk Management** (OCC / FRB / FDIC, June 6, 2023) is the spine for any bank-side review of a fintech counterparty contract.
- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact date and title] is the operative document for sponsor-bank programs. The contract gap matrix on a BaaS or program-operator counterparty must cover: end-customer reconciliation responsibilities and frequency; FBO subledger ownership, access, and reconciliation; deposit-insurance representation review (and customer-facing FDIC framing); program-operator operational-resilience commitments; and the fourth-party register with change-notice mechanism. The 2023 RFI on bank-fintech arrangements is not the binding statement; phase-2 cite-checks must catch the conflation [verify which artifacts are operative on the date of analysis].
- **FFIEC inter-agency joint statement on community-bank fintech due diligence** (August 2023) [verify exact title]: where the firm is a community bank engaging a fintech, this statement carries an explicit contract-checklist.

## Vendor-type taxonomy

The matrix must identify the counterparty's role on each rail and across the program: sponsor bank, BaaS platform / program manager, processor (front-end, back-end, gateway), BIN sponsor, ledger provider, card-issuance vendor, KYC / CIP vendor, fraud-decision vendor, sanctions-screening vendor, dispute-management vendor, FedNow / RTP gateway, ACH originator, ACH Third-Party Sender. Each pulls a distinct contract-clause set.

## Network and rule-based contract clauses

- **NACHA Operating Rules (current edition)** Originator and Third-Party Sender agreements; Third-Party Sender registration and risk-management terms [verify rule citations]. The contract must reflect the rule-required terms, the warranties allocated by NACHA to each party, and the audit-cooperation expectations. Paywalled; cite as "current edition" and pin against the firm's licensed copy.

- **Card-network operating rules (Visa, Mastercard, Amex, Discover)**. Required terms in issuer-processor and acquirer-merchant contracts; chargeback rules; PCI compliance representations; data-handling commitments; brand-protection terms. Paywalled; cite as "current edition" and pin against the firm's licensed copy.

- **Reg E (12 CFR Part 1005)** §1005.6, §1005.11, §1005.18 — error-resolution and customer-liability allocation. The contract must support the firm's Reg E obligations end-to-end, including evidence handover, dispute-decision allocation, and prepaid-account rule reach where applicable.

- **Reg Z (12 CFR Part 1026)** for credit-products — billing-error and disclosure obligations the contract must support.

## Money transmission and MSB

- **FinCEN MSB rules at 31 CFR Part 1022** and registration requirements at 31 CFR §1022.380 (initial registration within 180 days; renewal every two years). The agent-of-MSB and Third-Party-Relationship contract has specific content expectations: AML-program responsibilities, monitoring, registration evidence, termination triggers tied to regulatory action. Note: 31 CFR §1010.380 is the separate BOI / Corporate Transparency Act reporting rule, not the MSB-registration cite.
- **State money-transmission licences**: the contract for a vendor that touches funds-flow may need to reflect per-state licensing posture, consumer-protection bond evidence, and complaint-handling chain.

## Larger-participant rule

- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (December 2024) [verify Federal Register citation and current state including any litigation or congressional review]. Where the firm or the vendor crosses the threshold, the contract may need to reflect CFPB supervision-cooperation expectations.

## Sponsor-bank-program-specific clause expansions

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

## Cross-link inside the plugin

- **`exit-plan` payments-fintech overlay** carries the funds-flow wind-down, the FBO-account close-out sequence, the customer-notice obligations, and the network-orderly-exit posture. The contract gap matrix should evidence the contract clauses that enable each of those exit steps.

## Common payments-fintech pitfalls

- Treating the standard generic clause set as sufficient for a BaaS program agreement. The standard set undercovers; the overlay adds the program-specific rows.
- Missing the customer-liability-allocation row. Reg E allocates liability to the bank; the contract must support the bank's recovery posture against the program operator.
- Confusing the 2023 RFI on bank-fintech arrangements with the July 2024 Joint Statement. The Joint Statement is the operative artifact; the RFI is informational.
- Treating "PCI compliance" as a single contract row. PCI obligations sit across data-handling, breach-notification, audit-cooperation, and remediation rows.
