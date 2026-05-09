# Payments-fintech sector overlay — vendor-diligence

When the scope flags payments or fintech (sponsor-bank programs, BaaS platforms, money transmitters, MSBs, card-program operators), load this overlay alongside `references/source-anchors.md`.

## Operative supervisory frame

- **Interagency Guidance on Third-Party Relationships: Risk Management** (OCC / FRB / FDIC, June 6, 2023) is the spine for any bank-side review of a fintech counterparty.
- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact date and title] is the operative document for sponsor-bank programs. Diligence on a BaaS or program-operator counterparty must cover end-customer reconciliation, FBO subledger posture, deposit-insurance representation review (and customer-facing FDIC framing), program-operator operational resilience, and the fourth-party register. The 2023 RFI on bank-fintech arrangements is not the binding statement; phase-2 cite-checks must catch the conflation [verify which artifacts are operative on the date of analysis].
- **FFIEC inter-agency joint statement on community-bank fintech due diligence** (August 2023) [verify exact title]: where the firm is a community bank engaging a fintech, this statement carries an explicit due-diligence checklist.

## Vendor-type taxonomy

The diligence must identify the counterparty's role on each rail and across the program:

- Sponsor bank
- BaaS platform / program manager
- Processor (front-end, back-end, gateway)
- BIN sponsor
- Ledger provider
- Card-issuance vendor
- KYC / CIP vendor
- Fraud-decision vendor
- Sanctions-screening vendor
- Dispute-management vendor
- FedNow / RTP gateway
- ACH originator-of-record vendor (Third-Party Sender)
- Aggregator / developer-portal vendor

Each pulls a different rule set into the diligence checklist.

## NACHA

- **NACHA Operating Rules (current edition)** Third-Party Sender registration and risk-management rules [verify rule citations]: any counterparty acting as a Third-Party Sender on the firm's ODFI authority must have registration on file, the underlying Originator agreements documented, and return-rate-monitoring posture against current NACHA thresholds (administrative-return, overall-return, unauthorized-return) [verify current thresholds]. NACHA citations are paywalled; mark as "current edition; specific sections to be confirmed against the firm's licensed copy."

## MSB / state money-transmitter licensing

- **FinCEN MSB rules at 31 CFR Part 1022** where the counterparty is itself a money transmitter: registration on file, written AML program, CIP applicability where applicable, SAR-filing posture.
- **State money-transmitter licensing**: NMLS status on a per-state basis. **Money Transmitter Modernization Act** adoption posture in the firm's footprint [verify state-by-state adoption status as of the date of analysis].
- **NY DFS BitLicense** (23 NYCRR Part 200) for virtual-currency activity in NY.
- **CA DFPI** rulemaking under the Money Transmission Act and California Consumer Financial Protection Law.

## Card networks

- **Visa Core Rules and Visa Product and Service Rules; Mastercard Rules** [verify against firm's licensed copy]: BIN sponsor accountability for chargeback rights, fraud-rate program escalations (Visa Fraud Monitoring Program and Mastercard Excessive Fraud Merchant program), and program-level reporting.
- Card-network rulebooks are paywalled. Mark all citations as "current edition; specific sections to be confirmed against the firm's licensed copy."

## Reg E reach

- **Reg E (12 CFR Part 1005)** §1005.6 (consumer-liability), §1005.11 (error-resolution), §1005.18 (prepaid-account additions): the program operator owes downstream Reg E posture to consumers even where the depository is the bank. The program agreement nearly always pushes operational ownership of error intake to the fintech, and the diligence has to capture that allocation. Examiners pursue both Reg E and UDAAP findings where the timing windows slip.

## Cyber and resilience layer

- **NYDFS 23 NYCRR Part 500** where the counterparty is a covered entity.
- **GLBA Safeguards Rule** passed through the program agreement.
- **FFIEC IT booklets** used by sponsor-bank examiners.

## CFPB direct supervision

- **CFPB §1024 larger-participant rules** for digital wallets and payment apps (December 2024) [verify Federal Register citation, effective date, and current state including any litigation or congressional review]. Where the fintech is a designated larger participant, the CFPB has direct supervisory and examination authority. The diligence pack must surface applicability and the fintech's CFPB-readiness posture as relevant to the firm's bank.
- **CFPB Circular series** on account closures and holds, junk-fees, dark patterns, FDIC misrepresentation, BNPL [verify which circulars are current as of the date of analysis].

## Cross-link inside the plugin

- **`exit-plan` payments-fintech overlay** carries rail-by-rail wind-down mechanics (ACH and Same Day ACH cutover, wire and FedNow / RTP settlement-finality posture, card BIN re-sponsorship, in-flight-item carry-over register, FBO subledger reconciliation).
- **`concentration-risk-review` payments-fintech overlay** carries the three-axis concentration view: sponsor-bank, processor, BIN-sponsor.
- **`contract-gap-review` payments-fintech overlay** carries the program-agreement clause set, NACHA Third-Party Sender clauses, deposit-insurance-representation clauses, and the Reg E error-handling allocation.

## AI vendor mode in payments

When `ai_vendor=true` and the counterparty is a payments / fintech vendor (commonly fraud-decision, CIP / KYC, dispute-decision, or customer-service AI):

- The bank-fintech-arrangement frame still applies; the AI overlay layers on top.
- Reg E §1005.11 timing applies regardless of who or what produced the decision.
- BSA / AML and sanctions diligence on AI vendors that influence transaction-monitoring or sanctions-screening outcomes: model-risk overlay applies via cross-link to model-risk skills.

## Output-template additions for payments-fintech

- Rail-by-rail counterparty role table.
- Sponsor-bank and BIN-sponsor identification.
- MSB / MTL state-by-state licensing matrix.
- NACHA Third-Party Sender posture line.
- Subcontractor / fourth-party register.
- FBO subledger reconciliation evidence status.
- Deposit-insurance representation review status.
- CFPB larger-participant applicability check.

## Common pitfalls in payments-fintech vendor diligence

- Treating a sponsor-bank program operator as a SaaS vendor and missing the program-agreement-driven obligation allocation (FBO posture, deposit-insurance representation, Reg E timing).
- Skipping the per-state NMLS check on a money-transmitter counterparty.
- Missing the NACHA Third-Party Sender registration question for ACH counterparties.
- Treating card-network rulebook citations as if they were public; they are paywalled.
- Conflating the 2023 RFI on bank-fintech arrangements with the binding July 2024 joint statement.
- Skipping the CFPB §1024 larger-participant applicability check on a digital-wallet or payment-app counterparty.
