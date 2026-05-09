# Payments-fintech sector overlay — resilience-testing-pack

When the scope flags payments-fintech, load this overlay alongside `references/source-anchors.md`. It carries the payments-and-fintech-only frame the generic capability skill does not own.

## Operative supervisory frame

- **Interagency Guidance on Third-Party Relationships: Risk Management** (June 6, 2023) ongoing-monitoring section [verify section]. Vendor-performance and contingency-plan testing for payments arrangements.
- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. For sponsor-bank arrangements, the testing pack covers end-customer reconciliation, FBO subledger validation, deposit-insurance-representation continuity, and program-operator-distress scenarios.
- **Joint statement on community-bank fintech due diligence** (FIL-59-2021, August 27, 2021) [verify exact title and date]. Community-bank-specific testing-of-fintech-vendor expectations [verify section].
- **NACHA Operating Rules (current edition)** Third-Party Sender risk-management rules [verify rule citations]. ACH-network testing-of-failover and customer-impact handling.
- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (December 2024) [verify Federal Register citation and current state including any litigation or congressional review]. Where the firm or the vendor is a larger-participant payments platform, supervisory expectations on resilience testing apply.
- **FedNow and RTP operating rules** [verify references for current versions] — instant-payment-rails failover testing.

## Payments-rails scenarios

Payments-fintech testing pack scenarios commonly include:

- Card-network connectivity loss (Visa, MasterCard, Amex, Discover; or interchange-network equivalents).
- ACH-rail outage (FedACH, EPN); NACHA Operating Rules failover posture.
- Instant-payment-rail outage (FedNow, RTP); failover to alternative rail or to scheduled-rail with customer-experience consequences.
- Card-issuing-processor outage (the firm's processor or a fourth-party processor on the BIN-sponsorship chain).
- BIN-sponsor-bank distress scenario (program-operator perspective) and program-operator-distress scenario (sponsor-bank perspective).
- Fraud-decisioning vendor outage during peak transaction volume.
- KYC vendor outage during peak onboarding volume.
- Hyperscaler-region failure on the firm's primary compute region (and the firm's reliance on a single region for the payments platform).
- Wallet-vendor or BIN-card-controls vendor outage.

## Sponsor-bank programme testing

For sponsor-bank-and-program-operator arrangements (BaaS):

- End-customer reconciliation rehearsal: the bank's GL against the program operator's FBO subledger, with the seam dated.
- FBO subledger validation against the bank's records.
- Deposit-insurance-representation continuity in a program-operator distress scenario.
- Customer-notice rehearsal under program-end conditions; the customer-notice obligation is a sponsor-bank responsibility.
- Fourth-party register exercised: processor, KYC vendor, fraud-decision vendor, ledger provider all in scope.

The sponsor bank designs and approves the testing pack for the program; the program operator participates. A program operator running its own pack independent of the sponsor bank has misallocated the responsibility.

## Customer-impact safety controls

For payments-rails tests that may surface real customer impact:

- Customer-impact-threshold safety control set against the firm's policy and the operative consumer-protection clock (Reg E §1005.6 unauthorised-EFT, §1005.11 error-resolution clocks for the affected service).
- Pre-positioned customer-comms templates including IVR, mobile-banking-app banner, and statement-message framing.
- Fraud-monitoring sensitivity adjusted during the test window to avoid false-positive cascades.
- Settlement-cycle awareness: an exercise that runs across a cutoff window has settlement-cycle implications that need pre-coordination.

## AI-vendor testing in payments-fintech

When `ai_in_scope=true`:

- Fraud-decisioning vendor model regression scenario (the most common AI-on-payments scenario).
- KYC vendor AI-driven document-verification regression.
- Generative-AI customer-support vendor outage (where the vendor sits on customer-facing dispute-handling paths).

## Cross-link inside the plugin

- **`vendor-diligence` payments-fintech overlay** carries the diligence depth the testing pack consumes.
- **`exit-plan` payments-fintech overlay** carries program-operator-distress and sponsor-bank-distress exit-rehearsal design.
- **`concentration-risk-review`** for the firm's BIN-sponsor exposure, processor concentration, hyperscaler-region exposure across the payments platform.
- **`contract-gap-review` payments-fintech overlay**: where a test surfaces a contract gap (joint-statement element coverage, NACHA Third-Party-Sender risk-management terms), chain to the contract-gap review.

## Output-template additions for payments-fintech

- Sponsor-bank-program element checklist under evidence-collection plan for BaaS arrangements.
- Settlement-cycle awareness line under safety controls for tests that may run across cutoff windows.
- Reg E error-resolution clock line under customer-impact safety controls.
- NACHA Operating Rules failover scenario where the firm has material ACH exposure.

## Common pitfalls in payments-fintech resilience testing

- Treating multi-rail architecture as a free failover posture without tested rail-to-rail cutover. Architecture is the hypothesis; the test is the evidence.
- Skipping settlement-cycle coordination on a test that runs across a cutoff window. The test becomes a real settlement event.
- Letting the fraud-monitoring system trigger on test traffic. Pre-coordinate to avoid false-positive cascades and customer-experience consequences.
- Treating sponsor-bank-program testing as the program operator's job. The sponsor bank designs and approves; the operator participates.
- Setting tolerance from the program operator's preference rather than from the sponsor bank's IBS-map tolerance. The bank is the regulated entity.
- Skipping fourth-party-processor scenarios where the BIN-sponsorship chain has multiple processors.
- Treating community-bank fintech-vendor testing as a check-the-box exercise; FIL-59-2021 [verify] expects substantive due-diligence and ongoing-monitoring including testing.
