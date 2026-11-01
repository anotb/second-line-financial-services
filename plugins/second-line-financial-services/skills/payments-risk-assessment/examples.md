# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## bnpl-program-annual-assessment

### Example: BNPL program operator preparing its annual risk assessment after a CFPB action wave

Public-source-derived. No named program operator. The shape mirrors a common pattern at a mid-stage BNPL program operator running on debit-card and ACH rails through two sponsor processors with a thirty-state US footprint, preparing its annual second-line risk assessment in the wake of the CFPB BNPL / Pay-in-Four Interpretive Rule (May 2024 — **nullified by Pub. L. 119-11 (May 9, 2025); historical only**), the larger-participant rule for digital consumer payment applications, and the BNPL-themed Supervisory Highlights cycles.

#### Input

- **Program operator role**: `bnpl-provider`. Pay-in-Four product structure on debit-card and ACH rails. Closed-end credit posture asserted by the firm; the CFPB Interpretive Rule on whether Pay-in-Four constitutes a credit-card-like product subject to Reg Z dispute-resolution provisions was **nullified by Pub. L. 119-11 (May 9, 2025); historical only.** Reg Z applicability now turns on the product structure under the regulatory text rather than the nullified interpretive rule.
- **Rails in scope**: card debit (settlement and dispute mechanics), ACH (repayment-pull mechanics), card credit (where the merchant settles via card credit; rare in the cohort), check (legacy rails for a small subset of the borrower book).
- **Segments in scope**: BNPL borrower (consumer); BNPL merchant (SMB).
- **Geographic footprint**: 30 US states. State-AG enforcement on BNPL fee disclosure has been active in CA, NY, and others; verify current state-AG actions on the analysis date.
- **Sponsor banks and processors**: two sponsor processors handling debit-card settlement and ACH origination; a single ledger provider; a fraud-decision vendor; a sanctions-screening vendor; a single dispute-management vendor.
- **Review trigger**: `annual-cycle` plus `larger-participant-rule-applicability` (the firm is at the threshold and is checking applicability under the December 2024 CFPB final rule).
- **Audience**: head of payments compliance and CCO; second-line is producing the artifact for the ERC and for the sponsor-bank operating committee at each of the two processors.
- **Source posture**: `public-plus-firm-policy-plus-system-of-record-evidence`. The firm has access to its ledger, dispute-management vendor extracts, and the sponsor-processor reporting feeds.
- **Engagement scope supplied**: institution = BNPL non-bank program operator; primary regulators = CFPB (direct under §1024 if larger-participant designation lands; otherwise indirect), state-AG offices in the 30-state footprint, FTC; persona = head of payments compliance; sector overlay = payments-fintech (sector flagship); cross-cutting overlays = conduct (default-on for consumer-facing program), cyber (default-on; processor and fraud-vendor stack), privacy (default-on; consumer NPI flows for fraud monitoring).

#### Output sketch

The skill produces a payments risk assessment. Headlines:

- **Program summary** — BNPL program operator on debit-card and ACH rails; two sponsor processors; ledger and vendor stack named by role; 30-state footprint; current-cycle borrower book and merchant book sized by segment.

- **§1033 status note** — firm is a data provider for consumer-account-style BNPL ledger data under the Personal Financial Data Rights Final Rule; verify the firm's tier and implementation date on the analysis date; the docket has been active.

- **MSB / MTL status note** — fact-pattern-specific. The firm asserts non-MSB posture under the Pay-in-Four credit configuration; verify against the FinCEN administrative-ruling library; the state-by-state MTL footprint is verified through NMLS for any state that treats BNPL as money transmission (state treatment varies; verify per state).

- **Risk universe by rail**:
  - *Card debit* — top failure modes: chargeback-rate program escalation under the network monitoring program (Visa Dispute Monitoring Program / Mastercard Excessive Chargeback Merchant Compliance Program — paywalled, conceptual; verify program names and thresholds against the firm's licensed copy); Reg E §1005.6 unauthorised-transfer liability breach in the borrower-to-merchant repayment leg; Reg E §1005.11 dispute-timing failures (10 / 45 / 90-day windows). Residual risk: high. Top KRIs: chargeback-rate per merchant cohort; Reg E dispute-aging by stage.
  - *ACH (repayment-pull)* — top failure modes: unauthorised-return-rate breach against current NACHA threshold (R10, R11, R29, R51 codes; verify threshold and code list against the firm's licensed copy); WEB Debit account-validation rule failure (the rule effective March 19, 2021); administrative-return-rate breach. Residual risk: high. Top KRIs: unauthorised-return rate; account-validation coverage rate.
  - *Other rails* — summarised; not material to the borrower book.

- **Risk universe by segment**:
  - *BNPL borrower (consumer)* — top failure modes: fee disclosure (fee-vs-actual reconciliation against the firm's TILA-style or non-TILA disclosures; junk-fee themes per CFPB Circular series, verify current circular numbers); dispute-rights presentation (whether dispute language tracks the firm's actual dispute mechanics); Reg E §1005.11 timing failures presented as both Reg E findings and UDAAP findings; account-closure / hold UDAAP exposure where the borrower defaults trigger account hold beyond the contractual cure period. Residual risk: high. Top KRIs: dispute-timing-breach rate; complaint-volume vs CFPB Consumer Complaint Database benchmark; fee-disclosure reconciliation breach rate.
  - *BNPL merchant (SMB)* — top failure modes: chargeback-receipt timing on the merchant side; fee-disclosure on the merchant-side fee structure; merchant-categorisation accuracy (high-risk-vertical tagging). Residual risk: moderate. Top KRIs: merchant-side chargeback-rate; merchant-categorisation review cadence.

- **Risk universe by geography** — 30 state rows. CA row carries the CA DFPI under CCFPL applicability and active CA-AG enforcement on BNPL fee disclosure; NY row carries any NYDFS posture; each state row carries its own MTL / NMLS posture and MTMA adoption status. Default-to-USA is wrong; the operative obligations are state-by-state.

- **Concentration views**:
  - *Sponsor-bank* — n/a-as-banking-deposit; the BNPL construct does not run a sponsor-bank deposit relationship; the equivalent dependency is the sponsor-processor relationship. The assessment names the two sponsor processors explicitly.
  - *Processor* — top-N share by volume and value per rail; scenario impact under single-processor outage; current state is dual-processor for debit-card settlement, single-processor for ACH origination (a stretch on appetite given the unauthorised-return-rate risk).
  - *BIN-sponsor* — n/a (no card issuance in the cohort); BIN-sponsor row noted as not applicable.

- **Cross-cutting risks**:
  - *Customer-harm / UDAAP* — flagged red. Risk owner: CCO. Top KRIs: dispute-timing-breach rate; complaint-volume vs benchmark; fee-disclosure reconciliation breach rate. Deep-dive: `udaap-risk-review` with the payments-fintech overlay.
  - *Reporting / data quality* — yellow. Reg E §1005.11 dispute-timing data is the load-bearing report and the cadence has slipped vs the contractual SLA with the dispute-management vendor.
  - *Cyber* — yellow. Sponsor-processor SOC 2 Type II current at one processor; partial at the other (a Q2 audit period gap pending the next report).
  - *Fraud, AML / sanctions, operational resilience* — green-to-yellow per current cycle.

- **Risk-appetite posture** — red on the consumer-segment dispute-timing-breach KRI; yellow on the ACH unauthorised-return-rate KRI; yellow on the sponsor-processor concentration on ACH origination. Trigger conditions for red-to-amber escalation named.

- **KRI dictionary** — names each KRI with definition, source system, threshold (where set; `[evidence needed]` for the dispute-timing threshold which the firm has not formally set above the 10-day Reg E window), owner role, and cadence.

- **Recommended remediation portfolio** — Reg E §1005.11 dispute-timing reconciliation work plan; fee-disclosure refresh against current CFPB Circular guidance and the FDIC misrepresentation rule (where any FDIC framing appears); ACH unauthorised-return-rate sub-threshold programme; CFPB larger-participant-rule applicability check; second-processor evaluation for ACH origination redundancy.

- **Recommended disposition**: `accept-with-conditions`. Conditions: dispute-timing reconciliation evidenced before the next ERC cycle; fee-disclosure refresh evidenced before the next sponsor-processor annual review; CFPB larger-participant applicability decision in writing.

The assessment stops at the recommendation. The CCO and the head of payments compliance own sign-off; the sponsor-processor operating committees consume separately.

#### Why this scenario matters

- **Boundary check on UDAAP-as-cross-cutting**: the dispute-timing failures sit in both the consumer segment row and the cross-cutting UDAAP row; the assessment cannot collapse them.
- **Boundary check on default-to-USA geography**: the BNPL state regime is state-by-state and state-AG action is the live enforcement vector. A single "USA" geography row would miss the CA DFPI under CCFPL angle entirely.
- **Boundary check on concentration sub-tables**: the BNPL construct shifts the "sponsor-bank" axis to "sponsor-processor" but keeps the discipline of three separate views. BIN-sponsor is not applicable here and is named as not applicable, not omitted.
- **Boundary check on §1033**: the data-provider role under §1033 is operative for consumer-account-style BNPL ledger data; the implementation tier needs verification, not assumption.
- **Boundary check on the larger-participant rule**: the assessment names the applicability check as a remediation item rather than asserting the determination.

#### Anchors

- Reg E (12 CFR Part 1005) §1005.6, §1005.11.
- NACHA Operating Rules (current edition; paywalled; conceptual citation against firm's licensed copy) — return-rate thresholds, WEB Debit account-validation rule effective March 19, 2021, Third-Party Sender posture.
- Visa Core Rules and Mastercard Rules (current edition; paywalled; conceptual citation) — chargeback program escalation thresholds.
- CFPB Personal Financial Data Rights Final Rule under §1033 (October 22, 2024 — verify Federal Register citation and current docket status).
- CFPB final rule on larger participants of digital consumer payment applications (December 2024 — verify Federal Register citation and current state).
- CFPB BNPL / Pay-in-Four Interpretive Rule (May 2024) — **nullified by Pub. L. 119-11 (May 9, 2025); historical only.**
- CFPB Supervisory Highlights and Circular series (current cycles).
- FDIC misrepresentation rule, 12 CFR Part 328 Subpart B.
- State Money Transmitter Modernization Act adoption status via NMLS (state-by-state; verify on the analysis date).

See `references/source-anchors.md` for full citations and `references/sector-overlays.md#payments-fintech` for the rail-specific failure-mode menu.

## cross-border-remittance-rtp-corridor-add

### Example: Cross-border remittance fintech reassessing risk after adding RTP and a new corridor

Public-source-derived. No named program operator. The shape mirrors a common pattern at a cross-border remittance program operator, currently licensed in 25 US states under MTL via NMLS, that has just enabled RTP for the domestic legs of its remittance flows and added three new sending corridors (one of which is high-OFAC-risk-adjacent).

#### Input

- **Program operator role**: `cross-border-remittance-provider`. Money transmitter under state MTL in 25 states; FinCEN MSB-registered.
- **Rails in scope**: ACH and Same Day ACH (consumer funding); RTP (newly enabled for domestic-leg funding and for the US-side disbursement on receive corridors); wire (Fedwire / CHIPS for higher-value send corridors); cross-border correspondent (the substantive cross-border leg); virtual-currency on-ramp (for the on-ramp side of one new corridor; verify VASP counterparty configuration).
- **Segments in scope**: consumer remittance sender; consumer remittance receiver (US-side disbursement); a small business-to-consumer cohort.
- **Geographic footprint**: 25 US states; existing corridor countries plus three new corridors. One new corridor is high-OFAC-risk-adjacent (sanctioned-jurisdiction proximity; verify against current OFAC SDN, sectoral sanctions, and 50-Percent-Rule subsidiaries on the analysis date).
- **Sponsor banks and processors**: sponsor bank for USD funding flows; sanctions-screening vendor with corridor-by-corridor coverage; FX vendor and last-mile partner per receive corridor.
- **Review trigger**: `new-rail` (RTP enablement) + `new-corridor` (three corridors added). Combined as a delta-risk assessment that updates the prior annual baseline.
- **Audience**: BSA officer (primary); head of payments compliance; board risk committee for the OFAC-risk-adjacent corridor decision.
- **Source posture**: `public-plus-firm-policy-plus-system-of-record-evidence`. Firm has access to the sanctions-screening vendor portal, the sponsor-bank reporting feed, the FX-vendor reconciliation, and the corridor-by-corridor disbursement data.
- **Engagement scope supplied**: institution = state-licensed money transmitter (also FinCEN MSB-registered); primary regulators = FinCEN, OFAC, state DFI / DOB across the 25-state footprint via NMLS, CFPB (indirect on Reg E §1005.31 subpart B); persona = BSA officer; sector overlay = payments-fintech (sector flagship); cross-cutting overlays = cyber (default-on; vendor stack), conduct (default-on; consumer-facing), privacy (default-on).

#### Output sketch

The skill produces a delta-risk assessment that updates the prior annual baseline. Headlines:

- **Program summary** — money transmitter on cross-border remittance flows; named sponsor bank and vendor stack; 25-state US footprint; existing corridors plus three new (one high-OFAC-risk-adjacent); RTP newly enabled domestically.

- **§1033 status note** — firm is a data provider for consumer-account-style remittance ledger data; verify tier and implementation date.

- **MSB / MTL status note** — FinCEN MSB-registered (registration current; renewal date noted). State-by-state MTL via NMLS, 25-state footprint; MTMA adoption status varies; verify per state on the analysis date. Configuration-specific against FinCEN administrative-ruling library.

- **Risk universe by rail** (delta-focus on new and changed):
  - *RTP (newly enabled)* — top failure modes: settlement-finality irrevocability (no chargeback; recovery is request-for-return-of-funds under The Clearing House RTP Operating Rules — verify version and section against the firm's licensed copy); request-for-return-of-funds latency at the sponsor bank; ISO 20022 message-field anomalies (suspicious creditor account, suspicious end-to-end ID); 24/7/365 staffing posture for the operations and dispute teams. Residual risk: high (newly enabled). Top KRIs: request-for-return-of-funds aging; ISO 20022 anomaly-detection coverage; 24/7 staffing-coverage rate.
  - *Cross-border correspondent* — top failure modes: OFAC-screening latency on the new corridors (sanctions-screening vendor tuning lag); correspondent-bank de-risking on the OFAC-adjacent corridor; FX-disclosure timing under Reg E §1005.31 subpart B (pre-payment / post-payment disclosure; verify exact subpart B section and the firm's disclosure template). Residual risk: high on the OFAC-adjacent corridor, moderate elsewhere.
  - *ACH / Same Day ACH / wire* — unchanged from prior baseline; status line.
  - *Virtual-currency on-ramp* — top failure modes: Travel Rule applicability under 31 CFR §1010.410(f) at threshold (verify current threshold and FinCEN proposed-rule status); FinCEN CVC guidance applicability (FIN-2013-G001, FIN-2019-G001 — verify currency); VASP counterparty screening; chain-analytics vendor coverage; NYDFS BitLicense applicability under 23 NYCRR Part 200 if NY persons are in scope.

- **Risk universe by segment**:
  - *Consumer remittance sender* — top failure modes: Reg E §1005.31 subpart B disclosure-timing failures (the load-bearing failure mode for the new corridors); fee disclosure including FX-spread presentation; complaint volume on the new corridors. Residual risk: high.
  - *Consumer remittance receiver (US-side disbursement)* — top failure modes: Reg E §1005.6 unauthorised-transfer liability on the disbursement leg; account-takeover patterns on instant-funded inbound (heightened with RTP enablement); fee disclosure on receive-side fees. Residual risk: moderate-to-high.
  - *Business-to-consumer* — small cohort; top failure modes: AML-monitoring posture on B2C disbursement patterns. Residual risk: moderate.

- **Risk universe by geography**:
  - *25 US state rows* — each carries MTL via NMLS posture; MTMA adoption status per state (verify); state-AG enforcement on remittance fee disclosure where active; state breach-notification statutes for the cyber row.
  - *Corridor country rows* — existing corridors summarised; three new corridor rows in detail. The OFAC-adjacent corridor row carries: sending-side OFAC obligations (SDN list, sectoral sanctions, 50-Percent-Rule subsidiaries — verify against current); enhanced sanctions-screening cadence (real-time at message-field granularity, batch reconciliation daily); correspondent-bank reaffiliation status; receiving-side host-country obligations named at high level (the assessment does not substitute for local counsel).

- **Concentration views**:
  - *Sponsor-bank* — single sponsor bank for USD funding; scenario impact under sponsor exit named; standby-sponsor not pre-papered (a remediation item).
  - *Processor* — n/a-as-card; the equivalent for remittance is the sanctions-screening vendor and the FX vendor; named explicitly with corridor-by-corridor coverage.
  - *BIN-sponsor* — not applicable.

- **Cross-cutting risks**:
  - *AML / sanctions* — flagged red on the OFAC-adjacent corridor. Risk owner: BSA officer. Top KRIs: sanctions-hit-rate per corridor; sanctions-screening false-positive disposition aging; Travel Rule applicability log coverage. Deep-dives: `sanctions-screening-qa` and `aml-model-monitoring` with the payments-fintech overlay.
  - *Operational resilience* — yellow on RTP 24/7 staffing posture and on the request-for-return-of-funds latency.
  - *Customer-harm / UDAAP* — yellow on Reg E §1005.31 subpart B disclosure-timing on the new corridors.
  - *Cyber, fraud, reporting* — green-to-yellow per current cycle.

- **Risk-appetite posture** — red on the OFAC-adjacent corridor sanctions-hit-rate KRI; yellow on RTP 24/7 staffing; yellow on the Reg E §1005.31 disclosure-timing on new corridors. Trigger conditions named.

- **KRI dictionary** — RTP-specific KRIs (request-for-return-of-funds aging; ISO 20022 anomaly coverage; 24/7 staffing coverage); corridor-specific sanctions KRIs; Reg E §1005.31 disclosure-timing KRI.

- **Recommended remediation portfolio** — sanctions-screening-vendor tuning QA on the new corridors before volume scales; 24/7 staffing posture for RTP request-for-return-of-funds; Reg E §1005.31 disclosure-template review against the new corridors and the RTP-funded send paths; standby-sponsor pre-paper; state MTL filings for any state requiring notification of material change (MTMA adoption status drives the per-state filing path; verify per state); CSBS Multistate MSB Licensing Agreement Program coverage check.

- **Recommended disposition**: `accept-with-conditions`. Conditions: sanctions-screening tuning QA evidenced before volume scales on OFAC-adjacent corridor; RTP 24/7 staffing posture in place before next ERC; Reg E §1005.31 disclosure-template review evidenced; state MTL filings for material-change notifications complete.

The assessment stops at the recommendation. The BSA officer and the head of payments compliance own sign-off; the board risk committee consumes the OFAC-adjacent-corridor decision separately.

#### Why this scenario matters

- **Boundary check on faster-payments shift**: the RTP rail row cannot reuse the card-rail recovery template. Settlement-finality irrevocability and request-for-return-of-funds are the operative mechanics, not chargeback.
- **Boundary check on corridor-by-corridor geography**: the three new corridors get three rows, not one. The OFAC-adjacent corridor needs separate sanctions-screening and correspondent-bank treatment.
- **Boundary check on Reg E §1005.31 subpart B**: the remittance-transfer rule is its own beast. Asserting "this is a domestic Reg E lane" misses the cross-border subpart entirely.
- **Boundary check on Travel Rule and CVC**: the virtual-currency on-ramp on one corridor pulls the Travel Rule and FinCEN CVC guidance into the assessment; verify thresholds and guidance currency on the analysis date.
- **Boundary check on state MTL material-change notifications**: many state MTL regimes require notification of material change in business model (which a new rail or new corridor can be); MTMA adoption status varies; verify per state.
- **Boundary check on MSB-vs-not**: the firm is FinCEN MSB-registered (categorical fact, not a configuration question); the configuration question is which corridors and which CVC activity pull additional FinCEN obligations.

#### Anchors

- Reg E (12 CFR Part 1005) §1005.6, §1005.11, §1005.31 subpart B (remittance transfer rule).
- NACHA Operating Rules (current edition; paywalled; conceptual citation).
- The Clearing House RTP Operating Rules (current; verify version date and section).
- FedNow Service Operating Procedures (current; verify version date) — applicable on receive-side disbursement where FedNow is enabled.
- FinCEN MSB rules at 31 CFR Part 1022; FinCEN MSB registration at 31 CFR §1022.380; FinCEN Travel Rule at 31 CFR §1010.410(f); FinCEN CVC guidance FIN-2013-G001, FIN-2019-G001 (verify currency).
- OFAC 31 CFR Part 501; OFAC Compliance Commitments (May 2, 2019); OFAC SDN list and 50-Percent-Rule guidance.
- FFIEC BSA/AML Examination Manual.
- State Money Transmitter Modernization Act adoption status via NMLS (state-by-state; verify on the analysis date); CSBS Multistate MSB Licensing Agreement Program coverage.
- NYDFS 23 NYCRR Part 200 (BitLicense) for any NY-touching VC activity; NYDFS 23 NYCRR Part 500 §500.17(a) for cyber-event notification.

See `references/source-anchors.md` for full citations and `references/sector-overlays.md#payments-fintech` for the rail-specific and corridor-specific failure-mode menu.

## troubleshooting

### Troubleshooting: payments-risk-assessment

Recurring pitfalls. Read before drafting if the engagement looks unfamiliar; consult after drafting if the artifact does not feel right to a senior payments compliance reviewer.

#### Generic enterprise taxonomy with payments flavour dropped in

Symptom: the matrix has rows for "operational risk", "compliance risk", "credit risk" with payments-flavoured failure modes inside.

Why it fails: the artifact exists to be denominated in rails, segments, and geographies. Auditors and examiners cannot read a generic taxonomy as a payments risk assessment.

Fix: rebuild the matrix from rails, segments, and geographies first; the failure modes follow. The cross-cutting risks layer carries fraud, AML / sanctions, operational resilience, customer-harm / UDAAP, reporting, and cyber as a separate view.

#### Default-to-USA on the geography row

Symptom: a single "USA" row covering all 50 states.

Why it fails: the operative obligations are state-by-state. MTL via NMLS, MTMA adoption status, state UDAP regimes, state breach-notification statutes, and state-AG enforcement vary materially. CA DFPI under CCFPL is not the same as TX DOB; NY DFS is not the same as either.

Fix: one row per US state in scope. Where the state footprint is large (50 states), a state-grouping is acceptable for the rows that are genuinely homogeneous, but the heterogeneous states (CA, NY, TX, FL, IL, others by current enforcement posture) get their own rows.

#### Sponsor-bank-only concentration view

Symptom: a single "vendor concentration" line in the assessment.

Why it fails: sponsor-bank, processor, and BIN-sponsor concentration fail differently. A sponsor-bank exit leaves the program without rails and a depository; a processor outage cascades into customer-impact and Reg E §1005.11 timing; a BIN-sponsor exit leaves the card book without an issuer of record. A single line collapses the three failure modes.

Fix: three sub-tables. Each axis denominated in its own way (deposits / volume / customer count for sponsor-bank; volume and value per rail for processor; card volume and outstanding cards for BIN-sponsor). Cross-link to `concentration-risk-review` for the portfolio-level analysis; raise the flag here, do the analysis there.

#### Treating BNPL as a single rail

Symptom: a "BNPL" rail row in the matrix.

Why it fails: BNPL is not a rail. The operative rails are debit-card (settlement and dispute mechanics), ACH (repayment-pull mechanics), and sometimes card-credit. The risk profile shifts with the rail. A "BNPL" row hides the underlying rail-specific failure modes.

Fix: keep the rails as rails. Use a BNPL borrower segment row for the borrower-side risks and a BNPL merchant segment row for the merchant-side risks; cite the operative rails in those segment rows where the failure mode is rail-specific.

#### Missing the faster-payments irrevocability shift

Symptom: FedNow and RTP rows reuse the card-rail recovery template. Chargeback appears as a recovery mechanic.

Why it fails: settlement is final on receipt for FedNow and RTP. There is no chargeback. Recovery is request-for-return-of-funds plus monitoring escalation. The fraud-loss curve shifts forward; mule patterns on instant-funded inbound are heightened. The 24/7/365 staffing posture is operative, not optional.

Fix: rebuild the FedNow and RTP rows against the operative mechanics. Cite FedNow Service Operating Procedures and The Clearing House RTP Operating Rules (current; verify version) for the recovery mechanic.

#### Categorical MSB-vs-not assertion

Symptom: a sentence in the assessment that says "the firm is an MSB" or "the firm is not an MSB" without configuration-specific grounding.

Why it fails: MSB status is fact-pattern-specific against the FinCEN administrative-ruling library. Different configurations of the same product can fall on different sides of the line. A categorical assertion is an examiner-friendly target.

Fix: name the configuration as fact, the determination as a legal question that sits with counsel, and the operative posture (registration on file, written AML program, CIP applicability, SAR-filing chain) as evidence. The MSB / MTL status note in the artifact carries this discipline.

#### Skipping the cross-cutting UDAAP layer

Symptom: the matrix is "this is risk, not consumer compliance" and the UDAAP layer is omitted.

Why it fails: Reg E §1005.11 timing failures, account-closure / hold patterns, fee-disclosure failures, and FDIC-insurance representation are the highest-frequency examiner findings in this lane. The CFPB pursues both Reg E and UDAAP findings simultaneously. Omitting the UDAAP layer produces an assessment that the next CFPB Supervisory Highlights cycle will read as incomplete.

Fix: pull the conduct overlay (`references/cross-cutting.md#conduct`) in by default for any consumer-facing program. Read the theme list into the consumer segment row and into the cross-cutting UDAAP row. Cross-link to `udaap-risk-review` for the deep-dive.

#### Reg E §1005.31 subpart B treated as a domestic Reg E variant

Symptom: a cross-border remittance flow is read against Reg E §1005.6 / §1005.11 only.

Why it fails: the remittance transfer rule under Reg E §1005.31 subpart B has its own pre-payment and post-payment disclosure structure, its own error-resolution mechanics, and its own consumer-protection posture (verify exact subpart B section structure on the analysis date). A domestic Reg E read misses it.

Fix: where the program operates cross-border consumer remittance, read against Reg E §1005.31 subpart B. Cite the rule with the verify-section flag if the exact subpart structure is uncertain; do not invent.

#### Heat-map without supporting rows

Symptom: the deliverable is a colour-coded matrix with no underlying detail.

Why it fails: a heat-map without the supporting rows loses the auditability the artifact exists to provide. An examiner or sponsor-bank reviewer cannot trace the colour to a failure mode, control, or KRI.

Fix: heat-map summaries are appropriate for board and ERC audiences; the supporting matrix rows go in the appendix. The delivered artifact carries both.

#### Stale §1033 status note

Symptom: the §1033 status note is a generic paragraph that does not name the firm's tier or the implementation date.

Why it fails: the Personal Financial Data Rights Final Rule was finalised October 22, 2024 and the docket has been active. Tier dates and any compliance-date relief may have shifted. A generic note carries the citation but not the operational fact the firm needs.

Fix: name the firm's role under §1033 (data provider, data recipient, both, none) and the implementation tier date as of the analysis date. Verify the current docket status and date-stamp the citation.

#### Drafting against the "current edition" of NACHA without the disclaimer

Symptom: the artifact cites NACHA Operating Rules section numbers without the paywalled-disclaimer.

Why it fails: NACHA Operating Rules are paywalled. Section numbers and threshold values shift between editions. Without the disclaimer, the citation reads as if it were verified against the current edition when it cannot be (the firm holds the licensed copy; the assessment cites against it conceptually).

Fix: every NACHA citation carries the disclaimer "current edition; specific sections to be confirmed against the firm's licensed copy." Same pattern for Visa Core Rules, Visa Product and Service Rules, and Mastercard Rules.

#### The matrix is rail-by-rail but the rails are mislabeled

Symptom: a "Zelle" rail row, an "ACH push" rail row, a "wallet load" rail row.

Why it fails: Zelle is a P2P scheme that runs on top of underlying rails. ACH push is just ACH origination. Wallet load is the funding leg of a wallet program (debit card, ACH, or card-credit). Mislabeling the rails fragments the matrix and hides the operative rule set.

Fix: keep the rail row to the underlying rail (ACH, debit card, FedNow, RTP, etc.). Use the segment row to capture P2P consumer behaviour, wallet usage patterns, or scheme-specific risk. Cross-reference the scheme name in the segment row notes if helpful.

#### Engagement scope absent and not flagged

Symptom: the artifact reads as if a formal scope record were on file when it was not.

Why it fails: downstream skills key off the scope record (institution type, primary regulators, sector overlay set, persona, source posture). When scope was not formalised, the assessment must say so; otherwise downstream consumers (the concentration-risk-review skill, the exam-brief skill) cannot calibrate.

Fix: when the practitioner did not supply a formal scope record, ask the four questions (program-operator role, rails / segments / geographies in scope, review trigger, audience) and default to public posture if the practitioner declines. Note in the artifact that scope was not formalised; do not silently apply a default.
