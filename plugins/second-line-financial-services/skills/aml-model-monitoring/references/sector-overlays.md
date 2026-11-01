# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — aml-model-monitoring

When the scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the bank-specific monitoring nuance the generic skill does not own.

#### Segmentation lines the QA expects

Banks typically segment customers along several axes that the monitoring system tunes against. The QA reads which axes the institution actually uses and whether the segmentation is documented and refreshed.

- **Customer type.** Retail, small-business, mid-market commercial, large commercial, private banking, correspondent banking, MSB customers, trust customers, cash-intensive-business customers. Each carries a distinct expected-activity profile and distinct typology exposure.
- **Product mix.** Deposit, ACH, wire (domestic / international), check, RDC, debit / prepaid card, credit, treasury services, trade finance, lockbox. Scenario coverage by product is read against the BSA/AML risk assessment.
- **Geography.** Branch footprint, customer-residence concentrations, counterparty geographies (especially for international wires and trade), sanctioned-jurisdiction exposure (covered separately by `sanctions-screening-qa`).
- **Channel.** Branch, online, mobile, treasury portal, intermediated (correspondent, sponsor program, broker-dealer).

A rated decision that "segmentation is appropriate" without naming the axes and showing the population and behaviour evidence underneath is a label, not a rated decision. The QA names the missing axis.

#### Bank-typical scenario families

The institution's scenario inventory typically covers, at minimum:

- **Structuring** (cash and monetary-instrument). Threshold-based aggregation across short windows.
- **Rapid movement of funds** (in-and-out velocity). Inbound-to-outbound matching across short windows.
- **Unusual-pattern scenarios** against the customer's expected-activity profile (volume, velocity, counterparty, geography deviation).
- **High-risk-counterparty scenarios** (transactions with high-risk geographies, MSBs, certain correspondent flows).
- **Cash-intensive-business scenarios** (CTR pattern, deposit composition, large-bill mix where evidenced).
- **Trade-based-money-laundering indicators** for commercial customers with international counterparties (over- and under-invoicing patterns, third-party-payment indicators, invoice-mismatch indicators).
- **Wire-typology scenarios** (rapid pass-through, third-party-account routing, nested-correspondent exposure).
- **ACH and check** typology scenarios (kiting, false-positive debit patterns, P2P misuse).

Coverage gaps against active FinCEN typology advisories (e.g., ransomware-related conversion typologies, fentanyl supply-chain typologies, elder-fraud typologies, BEC) are findings. The QA does not specify the new scenario; it surfaces the coverage gap and routes to the change-governance machinery.

#### Correspondent and private banking nuance

Correspondent-banking monitoring carries nested-activity exposure: the underlying customer-of-customer activity is the typology surface, and downstream payment data may be limited. The QA reads whether the monitoring scope on correspondent activity is calibrated to the foreign-financial-institution's risk profile (`31 CFR §1010.610` due diligence drives the segmentation), whether nested activity is in scope, and how the monitoring scope handles the data-availability constraint.

Private-banking monitoring under `31 CFR §1010.620` carries source-of-funds and source-of-wealth context that the monitoring scenarios should be calibrated against. Senior-foreign-political-figure accounts carry heightened scrutiny that the monitoring scope should reflect.

#### Cash-intensive-business specifics

For banks serving cash-intensive businesses, the QA reads:

- Whether the segmentation isolates cash-intensive customers (not just labels them).
- Whether expected-cash-volume profiles are quantified at the customer level, not at the segment level.
- Whether the monitoring scope distinguishes deposit composition (denomination mix, large-bill ratio) where the firm's program and the typology landscape support it.
- Whether the scenario set covers structuring, rapid-velocity, and CTR-pattern scenarios calibrated to the cash-intensive segment specifically.

#### Refresh cadence at a bank

Common bank patterns for segmentation refresh: annually for high-risk segments, every two to three years for medium-risk, on event for low-risk. The QA reads against the institution's program-defined cadence, not against an external default. Refresh-cycle adherence is a finding when the cycle is missed; the QA names the missed-cycle date and the segments affected.

Tuning cycle cadence varies; common patterns are annual full tuning or rolling scenario-by-scenario tuning over an 18-month cycle. The QA reads whether the cadence is documented and adhered to, and whether each scenario in the inventory has a last-tuned date inside the program's cadence.

#### BTL testing posture at a bank

Below-the-line testing samples activity that fell just below the alert threshold to detect under-tuning. The QA reads whether BTL is performed scenario by scenario, whether sample sizes are statistically defensible against the population, whether the escalation rate is documented, and whether sign-off ties to a named reviewer independent of the tuning team. BTL "performed" reported as a binary without sample size, escalation rate, or sign-off is a finding.

#### Productivity and SAR conversion definitions

The QA names the denominator in every productivity and SAR-conversion metric. Common definitions:

- **Productivity** = SARs filed / alerts generated for a scenario in window. Or = escalated investigations / alerts. The denominator differs by firm.
- **SAR conversion** = SARs filed / investigations opened. Or = SARs filed / alerts generated. The two read very differently.
- **False-positive rate** = closed-without-escalation alerts / alerts generated. Definitions vary by whether "closed without escalation" includes auto-closed, manually closed, or both.

A productivity figure reported without a denominator definition is not interpretable; the QA marks the metric as `[evidence needed]` until the definition is on file.

#### Bank-specific findings the QA is alert to

- Segmentation refresh overdue against firm policy.
- Scenarios in the inventory with no documented last-tuned date or with last-tuned-date older than the program cadence.
- BTL performed for some scenarios but not others, without rationale for the gaps.
- Threshold change records where the approval evidence post-dates the change effective date.
- Productivity declining quarter-over-quarter for a scenario without a documented tuning hypothesis or a remediation plan.
- Scenario coverage gaps against active FinCEN advisories that the BSA/AML risk assessment named as in-scope typologies.
- Data-quality issues outstanding across multiple monitoring cycles without remediation owner or target date.
- Validation findings outstanding past the remediation target date without documented re-baselining.

## capital-markets

### Capital markets sector overlay — aml-model-monitoring

When the scope flags capital markets, load this overlay alongside `references/source-anchors.md`. AML transaction-monitoring at broker-dealers, investment advisers, and registered funds reads differently from a deposit-bank context.

#### Operative-program read

- **Broker-dealer.** AML program under FINRA Rule 3310 implementing 31 USC 5318(h); CIP under `31 CFR §1023.220`; SAR filing under `31 CFR §1023.320`. [verify section labels.]
- **Investment adviser.** AML program rule under `31 CFR Chapter X` for investment advisers — effective dates and scope are evolving; date the read and verify the operative compliance date. [verify the exact compliance dates and scope coverage.]
- **Registered fund (mutual fund).** AML program under `31 CFR §1024.210`; CIP under `§1024.220`; SAR under `§1024.320`. [verify section labels.]
- **FCM / IB.** Parallel CFTC-regulated AML program. [verify section labels.]

#### Capital-markets-typical typologies the monitoring scope addresses

The typology surface differs from a deposit bank's. The QA reads whether the scenario inventory addresses:

- **Microcap manipulation patterns** at broker-dealers serving microcap and shell-company customers — pump-and-dump schemes, shell-company concentrations, free-stock distribution patterns. Public enforcement themes have repeatedly addressed broker-dealer monitoring of microcap and shell-company activity.
- **Penny-stock concentration** indicators (concentrated positions in low-priced stocks at customers without an investment-advisory relationship that justifies the position).
- **Wash-trading and matched-trade patterns** where the firm's surveillance does not already cover.
- **Anonymous-source funding patterns** (third-party-account funding, intermediated funding, layered-account funding).
- **Account-roll patterns** (repeated account-opening, funding, trading, withdrawal cycles across related accounts).
- **Pre-IPO and private-placement related-customer concentration patterns.**
- **Large-cash-equivalent inflows** (cashier's checks, money orders, wire blocks from third-party originators, virtual-currency conversions).

The line between AML monitoring and trade surveillance is artificial in capital markets; the QA reads the AML system's coverage of patterns that border on market-manipulation typologies and notes where hand-off to surveillance is documented.

#### Investment-adviser nuance

Investment advisers historically operated outside the AML program rule; the FinCEN final rule extends scope. The QA reads:

- Whether the adviser's monitoring system is in place at the operative compliance date.
- Whether the scope covers the adviser's customer base appropriately (separately-managed accounts, private funds, sub-advisory relationships).
- Whether reliance on a custodian or broker-dealer's monitoring is documented under the rule's reliance provisions and whether the adviser's residual monitoring scope is defined.

#### Registered fund nuance

Mutual funds typically rely on the transfer agent for transaction-level monitoring. The QA reads:

- Whether the fund's AML program documents the reliance on the transfer agent and the residual fund-board oversight.
- Whether the transfer agent's monitoring system meets the fund's program expectations.
- Whether large-redemption, short-hold-period, and unusual-pattern scenarios are covered for the fund's investor base.
- Whether broker-omnibus account monitoring is in scope (or relied on the broker), and how the reliance is documented.

#### Segmentation in a capital-markets context

Customer segmentation at a broker-dealer or adviser typically covers:

- Customer type (retail individual, retail joint, retirement, trust, entity, foreign individual, foreign entity, institutional, hedge fund, family office).
- Account type (cash, margin, advisory, custodial, IRA, 401(k), trust, omnibus).
- Funding source (linked-bank ACH, wire, journal from related account, certificate, cashier's check, third-party).
- Trading profile (buy-and-hold, active equities, options, fixed-income concentrate, microcap-active, ETF-only, structured product).

A capital-markets segmentation that does not isolate the microcap-active profile is missing the most-cited enforcement-theme axis.

#### Productivity and SAR conversion in a capital-markets context

Capital-markets SAR rates are typically lower per customer than at a deposit bank but the SARs filed often address larger-dollar or higher-typology cases. The QA reads denominators and trends, not absolute rates, and is alert to:

- Auto-closure rules in a capital-markets monitoring system (less common than in payments) — read for documented validation.
- Per-scenario productivity trend, especially for microcap and structuring scenarios.
- Cross-reference between AML SAR filings and trade-surveillance referrals — the same pattern hitting both is a healthy signal; one without the other can indicate scope mismatch.

#### Capital-markets-specific findings the QA is alert to

- Microcap or shell-company-customer concentration without scenario coverage.
- Investment-adviser AML program scope unclear or operative compliance date treated as undefined.
- Mutual-fund reliance on transfer-agent monitoring documented but not exercised (fund-board review of TA monitoring posture absent).
- Broker-dealer monitoring scope on omnibus customer accounts unaddressed.
- Cross-product monitoring (cash + securities + lending) at full-service broker-dealers absent — the scenarios run product-by-product and miss cross-product layering.
- Trade-surveillance / AML-monitoring boundary undocumented; cases drop between the two.

## insurance

### Insurance sector overlay — aml-model-monitoring

When the scope flags insurance, load this overlay alongside `references/source-anchors.md`. AML monitoring scope at insurance carriers is narrower than at banks, broker-dealers, or payments-fintech, but the lines that exist are well-defined.

#### Operative scope

- **Covered products under `31 CFR §1025`.** Permanent life with cash value, annuities with cash value, and other insurance products with investment features. P&C, term life without cash value, group products, and health are generally outside scope.
- **AML program rule for insurance companies issuing covered products.** Program elements parallel the SAR-eligible-institution AML program structure: independent testing, designated officer, training, internal policies and procedures. [verify section labels.]
- **SAR rule under `31 CFR §1025.320`.** [verify section labels.]

#### Insurance-typical typologies the monitoring scope addresses

The typology surface for insurance covered products is narrow but distinctive:

- **Early surrender** of a permanent life or annuity policy soon after purchase, especially with a willingness to absorb surrender charges — the cash value out is the typology, not the loss.
- **Large premium** payments that exceed the policyholder's documented income or wealth profile.
- **Single premium** purchases of cash-value products from sources or amounts that do not match the customer profile.
- **Third-party premium funding** (a third party paying premiums on a policy the third party does not own and has no documented insurable interest in).
- **Frequent loans or partial withdrawals** against policy cash value followed by repayment patterns suggestive of layering.
- **Free-look-period cancellation** patterns (purchase, free-look refund, repurchase) indicative of cash-value cycling.
- **Beneficiary changes** that move proceeds to high-risk parties or jurisdictions.
- **Policy assignments** to third parties, especially across jurisdictions.

#### Distribution-channel nuance

Insurance carriers distribute through agents, brokers, banks (covered-product sales at the bank channel), wirehouses, registered investment advisers, and direct channels. The QA reads:

- Whether monitoring scope captures activity originated through each channel and whether agent / broker channel data feeds are integrated.
- Whether bank-distributed covered-product activity is monitored at the carrier or at the bank or at both, and whether the boundary is documented.
- Whether agent-of-record changes and producer-driven patterns (one producer originating multiple early-surrender cases) are within scope.

#### Segmentation in an insurance context

Insurance segmentation is typically lighter than at a bank or broker-dealer because the population is less actively transacting. Common axes:

- Product type (universal life, variable life, fixed annuity, variable annuity, indexed annuity).
- Premium-payment pattern (single, periodic, flexible).
- Distribution channel.
- Producer / agent.
- Customer profile (individual, corporate-owned policy, trust-owned, institutional).

The QA reads whether the segmentation isolates corporate-owned and trust-owned policies (the beneficial-ownership read on these is harder than on individual policies) and whether agent-driven concentrations are visible.

#### Productivity and SAR conversion in an insurance context

Insurance SAR rates are very low per policy and trend lines need long windows to be informative. The QA reads:

- Whether the monitoring system is exercised at all in the review window (a common finding is that the system runs but no alerts are generated in long stretches; the QA reads whether that reflects low typology surface, under-tuning, or coverage gaps).
- Whether scenario coverage matches the carrier's product mix (a fixed-annuity-only carrier has a different typology surface than a variable-product carrier).
- Whether SAR filings tie to monitoring output or only to agent-or-customer-reported events.

#### Insurance-specific findings the QA is alert to

- Monitoring scope on covered products absent for a product the carrier issues.
- Distribution-channel data feed gaps (especially agent-channel-originated activity) outstanding.
- Beneficial-ownership read on corporate-owned and trust-owned policies absent.
- Agent-driven concentration patterns (one producer, repeated early-surrender or third-party-funded patterns) unmonitored.
- Free-look-cycling patterns absent from the scenario inventory.
- Cross-channel layering (bank channel + agent channel for the same customer) unaddressed where the carrier's data infrastructure could detect it.

## payments-fintech

### Payments and fintech sector overlay — aml-model-monitoring

When the scope flags payments-fintech, load this overlay alongside `references/source-anchors.md`. Sponsor-bank programs, money-transmitter licensees, P2P operators, prepaid issuers, third-party payment processors, and BaaS programs all carry monitoring nuance the generic skill does not own.

#### Operative-program read

Before reading the monitoring system, the QA confirms whose program is operative.

- **Sponsor-bank program.** A non-bank fintech operating under a sponsor-bank model carries monitoring obligations under the program contract; the sponsor's BSA officer holds program oversight, and the fintech's monitoring system must meet the sponsor's program-level requirements. The QA reads against the sponsor program first, then the fintech's operating procedures.
- **Money services business (MSB) licensee.** A registered MSB operates its own program under FinCEN's MSB rules; the QA reads against the MSB's BSA program directly.
- **Independent bank or credit union with a fintech-style product (P2P, faster payments, mobile-first deposits).** Read against the institution's own program.
- **Third-party payment processor sponsored by a bank.** TPPP carries CDD-on-merchant and monitoring obligations downstream of the sponsor bank's program; data feed integrity from the TPPP into the bank's monitoring system is its own line of inquiry.

A monitoring memo that does not name the operative program is unread. The QA states the operative-program designation in the scope section.

#### Segmentation in a payments-fintech context

Payments and fintech populations are typically high-volume, low-balance, and skew younger and more transient than a deposit bank's. Standard demographic-and-behaviour segmentation may misfire. The QA reads:

- Whether segmentation captures the customer-journey lifecycle (onboarding, activation, sustained use, dormant, churned, reactivated). Activation and reactivation cohorts behave very differently from sustained-use cohorts.
- Whether the segmentation captures channel and device signal (web vs mobile vs API; device-fingerprint stability; new-device-on-known-account events).
- Whether peer-network features (counterparty graph, repeated-counterparty patterns, social-graph-implied connections in P2P) are part of the segmentation, where the firm uses them.
- Whether prepaid and stored-value segments isolate by load source, load velocity, and spend velocity.

A segmentation refresh that re-clusters fintech customers on demographic axes alone is missing the most informative axis.

#### Payments-typical scenario families

Beyond the bank-typical scenarios, payments-fintech monitoring typically covers:

- **P2P fraud-AML overlap scenarios.** Account-takeover-driven P2P sends, push-payment-fraud receipt patterns, scam-victim payout patterns, mule-account receipt-and-forward patterns.
- **Velocity scenarios** calibrated to the firm's product mix (intraday velocity, day-over-day velocity, week-over-week velocity), with thresholds tuned to the high-volume, low-balance population.
- **Funding-source typology scenarios** (linked-account funding, prepaid funding, third-party-card funding, faster-payment funding) and the rapid-cash-out patterns that follow.
- **MSB-customer scenarios** for sponsor banks banking MSBs.
- **Cross-border remittance typology scenarios** for licensed money transmitters (corridor-specific patterns, structuring across recipients, recipient-graph patterns, hawala-type indicators).
- **Faster-payment typology scenarios** (instant-credit-revoke abuse, unauthorised-push-payment patterns).
- **Card-not-present and BIN-attack indicators** where the program scope includes card issuance.
- **Virtual-currency on-ramp / off-ramp scenarios** where the institution serves customers transacting with VASPs (overlap with `references/cross-cutting.md#cyber`).

#### Sponsor-bank program-level coverage

For sponsor banks, the QA reads the program-level monitoring across the BaaS or fintech-program portfolio:

- Whether the sponsor's monitoring system aggregates across program partners or runs partner-by-partner.
- Whether the monitoring scope covers programs with limited downstream visibility (the data-quality and data-feed integrity questions are foundational here).
- Whether program-partner-driven segmentation makes sense at the sponsor level (a single threshold across all partners rarely does).
- Whether sponsor-level reviews of partner monitoring posture are documented and dated.

#### Data quality at velocity

Payments and fintech systems run high transaction volumes through layered architectures (ledger, processor, card network, ACH operator, RTP, sponsor-bank rail). The QA reads:

- Whether data feeds from each layer are documented (source, refresh, completeness, identifiers).
- Whether deprecated identifiers, processor migrations, or rail changes are tracked and the monitoring system's mappings are refreshed.
- Whether the firm's data-quality controls flag stale or missing feeds before the monitoring run.
- Whether identifier-stability across the lifecycle (account, device, customer) is monitored.

A data-quality issue on a payments rail outstanding for two cycles is heavier than the same issue on a low-volume product, given the throughput.

#### Productivity and conversion in a payments-fintech context

Productivity and SAR-conversion metrics in payments populations skew differently than in a deposit bank. The QA names the denominator and reads the trend, not the absolute number. Per-customer SAR rates may be small and trend lines matter more than spot values.

Auto-closure thresholds (where the program closes alerts without analyst review based on rules) are a heightened concern in high-volume populations. The QA reads whether auto-closure rules are documented, validated, and re-tuned, and whether BTL covers the auto-closed population.

#### Payments-specific findings the QA is alert to

- Segmentation that re-clusters on demographics rather than on lifecycle, channel, device, or peer-network features.
- Velocity scenarios with thresholds carried over from a deposit-bank baseline without re-calibration to the high-volume, low-balance population.
- Auto-closure rules without documented validation or BTL coverage.
- Sponsor-bank program-level monitoring run partner-by-partner without aggregated-portfolio visibility, leaving cross-partner typologies unobserved.
- Data feed gaps from a payment rail (RTP, FedNow, card processor, ACH operator) outstanding without remediation owner or target date.
- Faster-payment scenarios absent or under-tuned where the institution's faster-payment volume is material.
- VASP-counterparty exposure unaddressed in the scenario inventory where the customer base shows VASP transaction patterns; cross-link to `references/cross-cutting.md#cyber`.
