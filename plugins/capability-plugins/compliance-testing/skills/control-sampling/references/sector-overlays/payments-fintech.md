# Payments-fintech sector overlay — control-sampling

Loaded when `scope.sector_overlay_set` includes `payments-fintech` or when the test addresses NACHA, sponsor-bank, money-transmitter, prepaid, or larger-participant rules. Supplements `references/source-anchors.md` with payments-fintech-specific population, stratification, and tolerable-rate conventions.

## Population definition conventions payments and fintech examiners expect

Payments and fintech testing populations carry conventions that bank consumer-compliance testing does not always anticipate:

- **Sponsor-bank arrangements load two sector overlays.** The fintech program tests against payments-fintech rules; the sponsor-bank arrangement tests against banking rules (Bank Service Company Act, Joint Statement on Bank-Third-Party Deposit Programs, end-customer reconciliation). Both overlays load and the sampling memo names which controls sit on which side, with separate populations where the controls are separable.
- **Reg E error-resolution case files are themselves the population.** Under §1005.11, the case file the firm produces in the ordinary course is the testing target; the population is case files closed in the period, stratified by case type and outcome.
- **NACHA-relevant populations include returns, originated entries, and exception cases.** Third-Party Sender testing samples ODFI-relationship evidence, originator due diligence files, return-rate monitoring evidence, and unauthorised-return investigation cases.
- **State money-transmitter testing carries per-state populations.** Customer-funds protection testing (segregation, permissible investments) samples by state-licensed entity and state.

## Payments-fintech-supervisory anchors (load by reference; do not restate)

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. Operative for sponsor-bank programs.
- **U.S. Interagency Guidance on Third-Party Relationships: Risk Management** (FDIC / OCC / FRB, June 2023) [verify exact title and Federal Register citation]. Ongoing-monitoring sampling cadence and the population coverage expectation for sponsor-bank programs.
- **Reg E — 12 CFR Part 1005**, especially §1005.6 (consumer liability), §1005.7 (initial disclosures), §1005.8 (change-in-terms), §1005.10 (preauthorized transfers), §1005.11 (error resolution), §1005.18 (prepaid accounts) [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1005 .
- **Reg Z — 12 CFR Part 1026** billing-error procedures (§1026.13 for open-end credit) [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1026 .
- **NACHA Operating Rules (current edition)** Third-Party Sender risk-management rules and ODFI obligations [verify rule citations against the firm's licensed copy]. https://www.nacha.org/ .
- **FinCEN MSB rules at 31 CFR Part 1022** and registration requirements at 31 CFR §1010.380 [verify subsection labels]. https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1022 .
- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (December 2024) [verify Federal Register citation and current state including any litigation or congressional review]. https://www.consumerfinance.gov/compliance/supervisory-guidance/ [verify URL].
- **State money-transmitter rules** (state by state) — sampling memos carry the state-adopted statute citation, not the Money Transmission Modernization Act text [verify state citations].

## Payments-fintech-control-area sampling notes

### Reg E error-resolution sampling

- Sampling conventions: §1005.11 sampling pulls case files closed in the period with stratification by transaction type (debit-card unauthorised, ACH error, prepaid, ATM, P2P), case outcome (provisional credit issued, denied, reversed), case-aging (within 10 business days, 11-45 business days, beyond 45 days), and customer type (consumer, prepaid-account holder, business). Day-10 / day-5 provisional-credit timing under §1005.11(c) [verify timing] drives a separate stratum where the firm's policy clock is tighter than the regulatory minimum. Prepaid testing under §1005.18 carries additional disclosure-format and access-time testing populations.

### Sponsor-bank end-customer reconciliation sampling

- Sampling conventions: end-customer reconciliation testing population is FBO subledger entries during the period with stratification by program (where the bank sponsors multiple fintech programs), reconciliation status (matched, unmatched-aged, unmatched-current), and entry type (deposit, withdrawal, fee, internal-transfer). Tolerable rates for unmatched-aged populations are typically zero or near-zero per firm methodology because customer-funds-segregation expectations are absolute.
- Deposit-insurance representation testing samples customer-facing communications (account-opening, T&Cs, marketing) with stratification by channel and program; the population is communications sent in the period.

### NACHA Third-Party Sender sampling

- Sampling conventions: TPS testing samples ODFI-relationship evidence, originator due diligence files, return-rate monitoring evidence, and unauthorised-return investigation files. Stratification by originator, by return-code category, and by aging. Cite the NACHA rule by edition and section without restating; rely on the firm's licensed copy.

### BSA/AML for MSBs and fintechs

- Sampling conventions: AML-program testing samples CIP, CDD, and EDD evidence per the FFIEC BSA/AML Examination Manual and 31 CFR Part 1022 [verify part references]. Stratification by customer risk tier, by onboarding channel, and by product. Suspicious-activity testing samples case-management files with the same access-control posture as bank BSA testing (SAR content access restricted; the memo names the access control without restating SAR content).

### Money-transmitter customer-funds-protection testing

- Sampling conventions: customer-funds-protection testing samples permissible-investment positions and segregated-account balances against state-license obligations. The population is segregation positions held during the period; stratification by state and by investment type. Tolerable rates are typically zero per state law because the regulatory consequence is the license itself.

### Larger-participant CFPB scope (where applicable)

- Sampling conventions: where the firm is a CFPB larger participant for digital consumer payment applications, CMS-aligned testing applies. Sampling memos cite the larger-participant rule [verify Federal Register citation] alongside the substantive rule under test, and the population definitions follow the digital-payment-application transaction set.

## Audience and tone

A sampling memo drafted with an upcoming CFPB exam in mind reads heavier on UDAAP-relevant populations (disclosures, error-resolution, customer-impact framing in stratification), and the customer-impact-driven tolerable-rate setting for consumer-facing populations. A memo drafted for a state money-transmitter exam reads heavier on the state-statutory citations, the per-state customer-funds-protection populations, and the surety-bond or net-worth status as context. A memo drafted for sponsor-bank governance reads heavier on the bank-side and fintech-side population split, with the bank service provider relationship explicit in the source-of-truth narrative.
