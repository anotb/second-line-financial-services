# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — sanctions-screening-qa

When the scope flags banking, load this overlay alongside `references/source-anchors.md`. Carries the bank-specific sanctions-screening frame the generic capability skill does not own.

#### Operative anchors

- **31 CFR Chapter V** — operative OFAC programs scoped to the bank's customer and counterparty population.
- **FFIEC BSA/AML Examination Manual — Office of Foreign Assets Control section** [verify section anchor] — examiner-facing detail on bank sanctions program elements.
- **OFAC Framework for Compliance Commitments** (May 2, 2019) — five-component frame the QA aligns findings to.

#### Bank-specific screening rails the QA examines

- **Customer screening at onboarding** against the operative list set; full-rescreen cycle; delta-rescreen against new designations between full cycles. The QA reads both cycles; a program that runs deltas only and never full-rescans drops dropped designations over time.
- **Wire screening** — incoming and outgoing, including correspondent / cover-payment activity. SWIFT field-level screening (50, 52, 56, 57, 59 and the 70 narrative field) and the institution's stripping-prevention controls. The QA reads field coverage and the policy on suppressed-or-incomplete originator information.
- **ACH screening** — outbound ACH against the operative list set; the QA reads the IAT-vs-domestic distinction and the screening posture on each.
- **Trade-finance screening** — letter-of-credit, documentary-collection, and trade-loan transactions screened against the list set and against the program's dual-use-goods and red-flag-jurisdiction controls. The QA reads the field coverage on the LC text (applicant, beneficiary, advising bank, confirming bank, vessels, ports, goods description).
- **Correspondent-banking nested-relationship exposure** — the bank's downstream-respondent exposure to sanctions-evasion through nested arrangements. The QA reads the program's nested-relationship documentation and the periodic re-attestation evidence from respondents.
- **Customer rescreen cycle** — the cadence (delta vs full re-scan), the post-list-event sweep, and the evidence trail.

#### Bank-specific 50 Percent Rule patterns

- Aggregate ownership across multiple SDN entities is the failure mode. A program reading single-owner ownership only misses aggregate-ownership cases.
- Chain-ownership reads (an SDN entity owns a parent that owns the customer) require the program to walk the chain; database-only reads on offshore corporate structures are a known gap.
- The QA reads the program's evidence basis (corporate registry, BO certification, commercial database, vendor analytics) and notes where database reads on opaque structures are not corroborated.

#### Bank-specific SSI and sectoral handling

The Russia-related sectoral programs (E.O. 13662 and successor authorities) and other sectoral programs require directive-specific logic (debt / equity tenor restrictions, prohibited service categories, restricted-securities handling). The QA reads whether the program implements directive-specific logic or collapses sectoral into SDN-style blocking.

#### List-update event cadence at a bank

- The OFAC publication date is the benchmark for response timing, not the bank's internal publication date.
- Post-event customer-base sweep evidence and post-event payment-rail re-scan evidence are separate reads. A bank that runs the customer sweep and not the rail-rescan misses in-flight transactions against the new designation.
- Cross-rail consistency check: a customer that hits on wire and clears on ACH within the same window without documentation is a `cross_rail_consistency` finding.

#### Cross-link inside the plugin

- **`cdd-risk-review`** carries the customer-segmentation and beneficial-ownership work. Where the screening QA flags a 50 Percent Rule aggregation gap, the CDD posture (especially the ownership prong on legal-entity customers) feeds the read; the QA cross-references rather than absorbing the CDD work.
- **`edd-escalation-pack`** carries EDD posture for high-risk customers (foreign correspondent, private banking, PEP). Sanctions-evasion exposure on these customer categories cross-references.
- **`aml-model-monitoring`** carries the screening-engine model governance (match-logic, threshold calibration, BTL testing). The QA notes whether model-risk coverage is current; it does not re-do tuning work.
- **`sar-decision-qa`** carries the SAR decision QA where a sanctions-adjacent alert escalates into an investigation that may produce a SAR.

#### Output-template additions for banking

- Wire-message field-coverage status as a named field.
- Correspondent-banking nested-relationship attestation status as a named field.
- Trade-finance field-coverage status as a named field where the bank has trade-finance activity.
- Customer-rescreen cycle posture (delta vs full) as a named field.

#### Common pitfalls in banking sanctions-screening QA

- Reading the FFIEC manual sections as binding rules rather than as examiner expectations layered on the OFAC programs.
- Treating wire-message screening as covering only the originator and beneficiary fields, missing intermediary-bank fields and the 70 narrative field where evasion language often sits.
- Letting the QA drift into a recommendation on a specific alert disposition; the QA reviews the program and the documentation, not the match-or-no-match call.
- Skipping the correspondent-banking nested-relationship read on a bank with material correspondent activity.
- Conflating SSI directive-specific prohibitions with SDN blocking treatment in the disposition pipeline.
- Reading delta-update timeliness without reading delta-vs-full reconciliation evidence; the program may be fast on deltas and still drop designations between full cycles.

## capital-markets

### Capital-markets sector overlay — sanctions-screening-qa

When the scope flags capital markets (broker-dealers, mutual funds, futures commission merchants, covered investment advisers), load this overlay alongside `references/source-anchors.md`.

#### Operative anchors

- **31 CFR Chapter V** — operative OFAC programs scoped to the firm's customer, counterparty, and securities population.
- **OFAC Framework for Compliance Commitments** (May 2, 2019).
- **FFIEC manual is not the operative examiner anchor for BDs and funds** — SEC examination staff and FINRA examiners are. The QA reads the BD's written supervisory procedures (WSPs) under **FINRA Rule 3110 (supervision)** and the fund's compliance program under **Investment Company Act Rule 38a-1**. The OFAC posture sits inside those frames.
- **FINRA Rule 3310** — AML compliance program for BDs. The OFAC obligation runs alongside.
- **SEC Division of Examinations risk alerts on AML / sanctions programs at advisers and BDs** [verify specific risk alerts current on the date of analysis].

#### Capital-markets-specific screening rails the QA examines

- **Customer screening** at onboarding, periodic refresh, and event-driven rescreen against the operative list set.
- **Counterparty screening** — for institutional accounts, the executing-broker / clearing-broker / custodian / issuer / underwriter populations.
- **Securities-related sanctions** — restricted-securities lists (NS-CMIC and successor authorities) require the program to screen the security itself, not only the customer. The QA reads whether the trading-system-side check is in place at order-entry, at allocation, and at settlement.
- **Microcap and offshore-issuer concentration** — pump-and-dump and shell-company-issuer patterns intersect sanctions screening when the issuer or beneficial owners touch designated parties.
- **Settlement-chain screening** — counterparty / agent / custodian screening at settlement, including DTC-mediated and cross-border settlement.
- **Mutual-fund screening** — transfer-agent-level screening of shareholders; allocation-time screening on omnibus accounts.
- **FCM screening** — futures-account screening; introducing-broker chain screening.

#### Restricted-securities-list handling

The Non-SDN Communist Chinese Military Companies (NS-CMIC) list and successor restricted-securities lists carry **transaction-level prohibitions on the security itself**, not on the customer. A screening program that reads only customer name against the list misses the transaction-prohibition limb.

- The QA reads whether the order-management system or the trading platform applies a security-level block on restricted securities.
- The QA reads the program's posture on divestment-window restrictions (the wind-down period for existing positions in newly-restricted securities) and the evidence trail.
- Custody-side handling of restricted positions is a separate read where the firm has custody capability.

#### Investment-adviser scope

Until FinCEN's covered-investment-adviser AML rulemaking is fully operative for sanctions-program purposes, advisers' OFAC obligations apply through **OFAC's strict-liability frame** directly (every US person has to comply with OFAC), not through a stand-alone sanctions-program rule. The QA reads the adviser's program against the OFAC Framework five components (advisers can voluntarily align even where the FFIEC manual is not the operative anchor) and notes the rulemaking state on the date of analysis [verify current state of FinCEN IA AML rulemaking on the date of analysis].

#### Cross-link inside the plugin

- **`cdd-risk-review`** carries the BD's, fund's, or adviser's customer-segmentation work. Where the screening QA flags a 50 Percent Rule aggregation gap on legal-entity customers, the CDD posture feeds the read.
- **`aml-model-monitoring`** carries the screening-engine and surveillance-system model governance.
- **`sar-decision-qa`** carries the SAR-decision QA where a sanctions-adjacent alert at a BD escalates.

#### Cross-link to other plugins

- **`market-conduct-and-customer-outcomes/best-execution-surveillance`** [verify skill exists in current build] — where the sanctions alert sits adjacent to a market-manipulation pattern (e.g., microcap pump-and-dump linked to a sanctioned issuer), cross-reference rather than absorbing both lenses.
- **`vendor-diligence`** for transfer-agent, custodian, fund-accountant, and order-management-system vendor diligence.

#### Output-template additions for capital markets

- Restricted-securities-list handling status as a named field (`security-level-block`, `customer-only-screen`, `partial`, `not-applicable`).
- Settlement-chain screening posture as a named field where the firm has clearing or settlement capability.
- Transfer-agent screening posture as a named field for fund firms.
- Adviser-rule-state note as a dated field where the firm is a covered investment adviser.

#### Common pitfalls in capital-markets sanctions-screening QA

- Importing the FFIEC bank-flavoured frame as if it were operative for a BD or fund; the FFIEC manual informs but does not bind, and SEC / FINRA examiners are the primary audience.
- Reading restricted-securities-list compliance as a customer-screen exercise; the operative limb is a security-level transaction prohibition.
- Treating an investment-adviser-only firm as outside OFAC scope; OFAC is strict-liability and reaches every US person.
- Skipping the settlement-chain or transfer-agent screening read where the firm has those capabilities.
- Confusing CDD findings (which sit in `cdd-risk-review`) with sanctions-screening findings.
- Missing the divestment-window posture on newly-restricted securities (operational compliance with the wind-down period is a discrete read).

## insurance

### Insurance sector overlay — sanctions-screening-qa

When the scope flags insurance, load this overlay alongside `references/source-anchors.md`. The insurance overlay carries what the bank- and payments-flavoured frames do not.

#### Operative anchors

- **31 CFR Chapter V** — operative OFAC programs scoped to the carrier's customer, beneficiary, producer, and counterparty population. Insurance carriers are US persons; OFAC is strict-liability and reaches every US person.
- **OFAC Framework for Compliance Commitments** (May 2, 2019).
- **31 USC §5318(h)** — AML program requirement for insurance companies (the operative AML compliance program rule). The OFAC sanctions program runs alongside; the QA reads against the carrier's written compliance program.
- **NAIC Insurance Data Security Model Law (Model #668)** [verify model number] — adjacent cybersecurity frame; intersects the sanctions screening pipeline at the IDV-and-onboarding layer.

#### Insurance-specific screening rails the QA examines

- **Customer screening at policy underwriting** — applicant, policy owner, payor (where different), insured (where different from owner) screened against the operative list set.
- **Beneficiary screening at claim** — beneficiary screened at claim notification and again at payment. Beneficiary-change events post-issuance are an event-driven rescreen trigger; a designation occurring after policy issue but before claim has to be picked up.
- **Producer (agent / broker) screening at appointment and at periodic re-attestation** — the producer is a counterparty; producer-perpetrated schemes and producer-distribution-chain exposure are real.
- **Premium-payment counterparty screening** — third-party premium payors, lender-funded payors (premium-financing), and foreign-jurisdiction wire payors are screened.
- **Reinsurance counterparty screening** — ceding and assuming counterparties (and retrocessionaires) are screened. Reinsurance treaty re-attestation cycles carry the periodic read.
- **Payee screening at payout** — claim payees, surrender payees, dividend payees, policy-loan disbursement payees.

#### Covered-products scoping interaction

The carrier's BSA / SAR program operates against covered products only (permanent life with cash value, annuities with cash value, certain other investment-type products). The carrier's **OFAC obligation does not stop at covered products** — OFAC is strict-liability and applies across all lines including P&C, term life, group, and health. The QA scopes carefully:

- The BSA / AML overlay applies to covered products.
- The OFAC sanctions screening obligation applies to all customer, beneficiary, producer, and counterparty populations regardless of product line.
- A program that scopes sanctions screening to covered products only has under-scoped its OFAC obligation; this is a foundational finding.

#### Beneficiary-at-claim posture

The beneficiary-at-claim screening is the most-often-overlooked rail in insurance sanctions screening. The lifecycle is:

- Beneficiary screened at policy issue.
- Beneficiary-change events post-issue trigger rescreen.
- Beneficiary screened at claim notification.
- Beneficiary screened again at payment (post-list-update events between notification and payment).

A program that screens at issue and again at claim only, without the change-event rescreen and the payment-time refresh, has gaps. The QA reads the lifecycle, not a single point in it.

#### Reinsurance counterparty exposure

Ceding and assuming reinsurance counterparties (and retrocessionaires) are counterparties for OFAC purposes. The QA reads:

- Treaty-level counterparty screening at execution and at periodic renewal.
- Facultative-level counterparty screening at placement.
- Retrocession-chain visibility (does the program know the retrocessionaires of its assuming counterparties).
- Run-off-portfolio counterparty rescreen on legacy treaties.

#### Producer accountability

The insurance distribution model means the **producer** is a counterparty whose appointment and conduct sit inside the program's sanctions risk. The QA reads:

- Producer-screening at appointment against the operative list set.
- Periodic producer re-attestation including sanctions-screening refresh.
- Producer-distribution-chain screening (sub-producers, MGAs, MGUs).
- Producer-driven scheme indicators (policies steered to designated counterparties, beneficiary patterns inconsistent with customer profile).

#### Cross-link inside the plugin

- **`cdd-risk-review`** carries the carrier's covered-product CDD work and the producer-due-diligence frame. Where the screening QA flags a 50 Percent Rule aggregation gap on a legal-entity policy owner, the CDD posture feeds the read.
- **`edd-escalation-pack`** carries EDD posture for high-risk customers (PEPs, foreign-jurisdiction premium funding, large face-amount contracts).
- **`sar-decision-qa`** carries the SAR-decision QA where a sanctions-adjacent alert escalates. Note that SAR rule scope is covered-products-only; OFAC scope is broader.

#### Cross-link to other plugins

- **`market-conduct-and-customer-outcomes`** plugin [verify skill availability in current build] — producer-perpetrated schemes overlap.
- **`vendor-diligence`** for TPA / claims-administrator / underwriting-bureau / IDV-vendor diligence where the alert source is a third-party system.

#### Output-template additions for insurance

- Beneficiary-at-claim screening lifecycle status as a named-field block (`issue`, `change-event`, `claim-notification`, `payment-time`).
- Producer-screening status as a named field (`appointment`, `periodic-re-attestation`, `sub-producer-chain`).
- Reinsurance-counterparty screening status as a named field (`treaty`, `facultative`, `retrocession-chain`, `run-off`).
- Covered-vs-non-covered scope read for the OFAC obligation as a named field (the BSA scope and the OFAC scope are different).
- Premium-financing counterparty screening status as a named field where the carrier has premium-finance volumes.

#### Common pitfalls in insurance sanctions-screening QA

- Scoping sanctions screening to covered products only; OFAC is strict-liability across all product lines.
- Screening at policy issue and at claim only, missing the change-event rescreen and the payment-time refresh on the beneficiary lifecycle.
- Treating producer screening as a one-time appointment exercise; periodic re-attestation and sub-producer-chain reads are part of the program.
- Skipping reinsurance-counterparty screening because the cessions are treated as "between sophisticated counterparties"; OFAC reaches every US person regardless of counterparty sophistication.
- Importing FFIEC bank-flavoured continuing-cycle reads where the carrier's program is structured around policy-cycle and claim-cycle events instead.
- Confusing carrier insolvency / financial-condition triggers with sanctions-screening triggers; those route through different supervisory channels.

## payments-fintech

### Payments-fintech sector overlay — sanctions-screening-qa

When the scope flags payments or fintech (sponsor-bank programs, BaaS platforms, money transmitters, MSBs, card-program operators, virtual-currency on-ramps), load this overlay alongside `references/source-anchors.md`. The overlay carries the payments-rail-specific and sponsor-bank-allocation reads the bank-flavoured frame does not.

#### Screening-responsibility allocation

The threshold question for a payments-fintech sanctions-screening QA is which entity owns the screening obligation on which activity. The allocation is documented in the sponsor-bank program agreement and is not optional QA scope.

- **Sponsor-bank arrangement (BaaS, program operator, fintech with bank in the chain)**: the sponsor bank typically holds the OFAC obligation for activity in the bank's accounts under the operative OFAC program(s). The fintech's program may detect, the sponsor bank reviews and decides. The QA reads the fintech's screening evidence, the handoff package to the sponsor bank, and confirms the bank-level read on the same activity is not double-counted or skipped.
- **Standalone MSB**: the MSB itself owns the OFAC obligation. Operative OFAC programs and the FFIEC OFAC section apply directly.
- **Money transmitter with multi-state licensure**: per-state requirements layer on top of the federal OFAC obligation; the QA notes the per-state population but reads against the federal anchor.
- **Dual-posture (MSB with sponsor-bank deposit account)**: both can apply to different segments of activity. The QA scopes which counterparty owns which screening read.

#### Payments-rail-specific screening

- **Real-time card screening** — authorization-time screening latency tradeoffs. The QA reads the program's posture on declines for sanctions hits at authorization time (the customer-experience pressure to clear false positives within milliseconds is real; the disposition evidence trail still has to exist).
- **ACH screening** — outbound and inbound; same-day ACH compresses the screening window. The QA reads the cycle and the suspended-batch handling.
- **Faster-payments rail screening** (e.g., RTP, FedNow) — sub-second authorization windows; the program's pre-screening (customer-level, counterparty-level) versus per-transaction screening posture. The QA reads the rail-specific operating window.
- **Wire screening (where the fintech has wire capability)** — same field-level reads as a bank.
- **Card-program screening** — BIN-sponsor allocation of screening responsibility, prepaid-card cardholder screening, and the cross-card / cross-program reconciliation evidence. Multi-card / cross-program activity is a known evasion vector.
- **Crypto on-ramp / off-ramp screening** — exchange-side and custodial-wallet screening; address-level designations; analytics-vendor governance. The cyber overlay engages.

#### Sponsor-bank screening responsibility

When the QA covers a fintech operating under a sponsor-bank model, the screening-responsibility allocation read is load-bearing:

- The drafted program (fintech's screening rules, fuzzy thresholds, exclusion lists).
- The investigation evidence (dated, attributed disposition decisions; evidence pointers).
- The handoff package to the sponsor bank (the alerts the fintech escalates; the rationale for non-escalated alerts; the periodic re-attestation to the sponsor bank).
- The sponsor bank's own screening read on the same activity (the QA reads whether the bank's read is independent or relies on the fintech's read; reliance has to be documented in the program agreement and tested).

A handoff package missing the periodic re-attestation, missing the rationale for non-escalated dispositions, or missing the sponsor-bank's independent-test evidence is a `process_change_recommendation` finding.

#### MSB screening considerations

- **31 CFR §1022.380** — MSB registration with FinCEN. Initial registration within 180 days of becoming an MSB; renewal every two years. Adjacent program-element check; an unregistered MSB has a foundational program defect that the screening QA notes by reference even though registration is outside the screening artifact. Not the BOI / CTA reporting rule at §1010.380, which is a separate obligation with its own legal status.
- **State money-transmitter license set** — per-state populations.
- **Bank Secrecy Act and OFAC dual obligations** — the MSB's program-level posture on BSA / OFAC convergence is the operative read.

#### Crypto on-ramp / off-ramp screening exposure

The FinCEN / OFAC convergence on virtual-currency activity is the dominant evasion vector at fintech and crypto-adjacent firms. The QA reads:

- **Address-level screening** against OFAC-designated addresses (mixers, sanctioned-jurisdiction-adjacent wallets). Name-only screening misses address-level designations.
- **Counterparty-attribution evidence** from blockchain-analytics vendors. Vendor outputs are vendor outputs; the QA cites the vendor and routes vendor-diligence to `vendor-diligence`.
- **Hop-distance posture** — does the program treat addresses one or two hops from sanctioned addresses as alert-generating, and on what evidence basis.
- **Chain-hopping and cross-chain bridges** — does the program have visibility across chains the customer base uses.
- **The cyber overlay (`references/cross-cutting.md#cyber`) carries the deeper read** on these typologies.

#### Cross-link inside the plugin

- **`cdd-risk-review`** carries the fintech's customer-segmentation and onboarding-CDD work. Sanctions findings on synthetic-identity, deepfake, or BO opacity feed back to CDD-program tuning.
- **`sar-decision-qa`** carries the SAR-decision QA. Sanctions-adjacent alerts that escalate to SAR cross-reference; convertible-virtual-currency typologies are the dominant overlap.
- **`aml-model-monitoring`** carries the screening-engine and analytics-vendor model-risk view. The QA notes whether model-risk coverage is current.

#### Cross-link to other plugins

- **`vendor-diligence`** carries the sponsor-bank, processor, BIN-sponsor, KYC-vendor, fraud-decision-vendor, sanctions-screening-vendor, and blockchain-analytics-vendor diligence. The screening QA cross-references vendor-diligence findings where a sub-processor's posture is material.
- **`llm-vendor-evidence-review`** carries the AI-vendor evidence-pack review for AI tooling in the screening or analytics pipeline.

#### Output-template additions for payments-fintech

- Screening-responsibility allocation as a named field (`sponsor-bank-screens`, `msb-screens`, `dual-posture`).
- Per-rail screening posture (`real-time-card`, `same-day-ach`, `faster-payments`, `wire`, `crypto-on-ramp`) as a named-field block with operating-window observations.
- Sponsor-bank handoff package status (`complete`, `partial`, `missing-non-escalated-rationale`, `missing-periodic-re-attestation`, `missing-bank-independent-test-evidence`, `other-gap`).
- Address-level screening capability status (loaded with the cyber overlay).

#### Common pitfalls in payments-fintech sanctions-screening QA

- Reviewing the fintech's screening as if the fintech were the obligor; missing the sponsor-bank screening-responsibility allocation read.
- Treating real-time rail latency pressure as a reason to lower disposition-evidence rigour; the disposition still has to be evidenced after the fact.
- Skipping the address-level screening read on programs with crypto on-ramp / off-ramp exposure (the cyber overlay engages).
- Reading the analytics-vendor output as a primary source (it is a vendor output; route vendor-diligence).
- Missing the cross-card / cross-program reconciliation read on multi-card programs (BIN-sponsor evasion vector).
- Importing bank-flavoured wire-message field reads to a fintech without wire capability; scope to the rails the program actually operates.
