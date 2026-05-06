# Payments-fintech sector overlay — criticality-assessment

When the engagement scope flags payments or fintech, load this overlay alongside `references/source-anchors.md`. It carries the payments-fintech-only criteria the generic capability skill does not own.

## Operative supervisory frame

- **NACHA Operating Rules (current edition)** Third-Party Sender registration and risk-management rules [verify rule citations]. Where the arrangement sits on the ACH path, the rules drive the criticality read.
- **FedNow Service Operating Procedures and RTP Operating Rules** [verify section and current editions]. Settlement-network access continuity for instant-payment rails.
- **Card-network rules (Visa, Mastercard, Amex, Discover) — current editions**. BIN-sponsorship arrangements; the BIN sponsor is critical by construction for any card program.
- **CFPB Reg E (12 CFR Part 1005)** §1005.6, §1005.11, §1005.18. Consumer-EFT and prepaid obligations affect customer-impact reads.
- **FinCEN MSB rules at 31 CFR Part 1022** and registration requirements at 31 CFR §1010.380 [verify §]. KYC/AML utilities and other compliance-rail arrangements get the criticality lens through MSB obligations.
- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (December 2024) [verify Federal Register citation and current state]. Where the firm or arrangement is in scope, supervisory exposure shapes the regulatory-impact read.

## Candidate IBS for payments-fintech entities

Important business services typically include payment authorisation and settlement, payment-network access (FedNow, RTP, ACH, card networks, wire), KYC/CIP and AML transaction monitoring, fraud detection and decisioning, customer ledger and reconciliation, settlement-account servicing, and dispute-and-chargeback handling. The IBS list is the firm's; the candidate list above tracks BCBS Principles for Operational Resilience (March 2021) translated into the payments-fintech setting.

## BaaS and sponsor-bank lens

- Where the firm is a fintech with a sponsor-bank relationship, the sponsor-bank arrangement is `critical` by construction for any deposit-product program.
- The sponsor-bank-side overlay is in `references/sector-overlays/banking.md`. Read both when the arrangement spans both perimeters; the firm-side criticality and the sponsor-side criticality may differ in scale but should align in tier.
- The 2024 interagency joint statement on bank deposit-product third-party arrangements [verify exact title and date] frames the BaaS criticality read.

## Cross-link inside the plugin

- **`vendor-diligence` payments-fintech overlay** consumes the `tier` and the named IBS to set diligence depth, including network-rule attestation and BSA-AML control attestation where applicable.
- **`exit-plan` payments-fintech overlay** consumes the `tier`, the supported IBS, and the customer-impact read to set transition mechanics, including settlement-network access continuity, BIN-sponsor transition, and Reg E and NACHA customer-notice posture.
- **`concentration-risk-review`** consumes the `concentration_considerations` flag for processor concentration, BIN-sponsor concentration, and KYC/AML-utility concentration.

## AI vendor mode at a payments-fintech entity

When `ai_vendor=true`:

- An AI vendor on the fraud-decisioning, AML-transaction-monitoring, or KYC-decisioning path is rarely below `important`. Fair-lending and UDAAP exposure shape the customer-impact and regulatory-impact reads.
- A `critical` AI-vendor call on a regulated decisioning path triggers parallel review by the model-risk and consumer-compliance functions; record the cross-link.

## Output additions for payments-fintech

- IBS named explicitly and matched against the candidate list above.
- Network-rule applicability check (NACHA, card networks, RTP, FedNow).
- BIN-sponsorship and sponsor-bank applicability check for fintech firms.
- BSA-AML-utility applicability check for KYC/AML and transaction-monitoring arrangements.

## Common pitfalls in payments-fintech criticality calls

- Setting tier without reading the network-rule perimeter. NACHA Third-Party Sender, card-network BIN-sponsor, and FedNow access carry tier-driving obligations regardless of vendor scale.
- Treating a sponsor-bank arrangement as a "partner" rather than a critical third-party arrangement. The sponsor bank sits on the deposit-product and BSA-AML chain.
- Missing the consumer-compliance lens. Reg E, NACHA, and card-network rules carry consumer-protection clocks that affect customer-impact and notification-trigger reads.
- Defaulting to the vendor's claimed RTO/RPO as the test. The firm's tolerance from the IBS impact analysis (often measured in minutes for instant-payment rails) is the test.
