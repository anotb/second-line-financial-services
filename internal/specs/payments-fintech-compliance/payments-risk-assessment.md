# Spec sheet: payments-risk-assessment

Plugin: `sector-plugins/payments-fintech-compliance`
Status: v1 retained skill (sector-unique under strict overlay rule).
Phase: 1 (spec only; no SKILL.md content here).

## Why this is a sector-only skill

A payments risk assessment is structured by rail, by customer segment, and by geography in a way that the generic `risk-compliance-core/risk-assessment` and `compliance-testing/control-matrix` skills do not produce. The matrix is denominated in payment populations and rail-specific failure modes (ACH return-rate breaches, card-network fraud-rate program escalations, FedNow / RTP fraud holds, cross-border correspondent risk). The output is the artifact a sponsor-bank reviewer, an examiner, or an internal audit team expects to read at the start of a program review or annual cycle.

The capability skill it does not duplicate is `risk-compliance-core/risk-assessment` (generic enterprise-risk-assessment scaffolding). That one provides the primitives; this one produces the payments-flavoured artifact. Boundary: when the assessment scope is enterprise-wide and not payment-specific (e.g., AI risk, model risk, cyber-only, third-party-only), use the capability skill with the payments-fintech overlay reference. Use this skill when payments rails are the dominant axis.

## Activation-tuned description

```
Drafts a payments risk assessment denominated by rail, customer segment, and geography: fraud, AML / sanctions, operational resilience, third-party / sponsor-bank dependence, customer-harm / UDAAP exposure, and reporting controls. Output is a structured artifact suitable for a sponsor-bank annual review, a state MTL exam preparation file, an internal audit kickoff, or an enterprise risk committee read-out.

Best for:
- A program operator, sponsor-bank's program-management team, or money transmitter is running its annual or semi-annual payments risk assessment and second-line is owning the artifact.
- A new product, rail, or geography is being added and the team needs the delta-risk assessment.
- An exam letter or sponsor-bank annual review has asked for the rail-by-rail risk view and the team is preparing the response file.
- A processor consolidation, sponsor-bank change, or BIN-sponsor change has shifted the risk profile and the team needs to re-baseline.

Not the right tool when:
- The work is a controls inventory (use fintech-partner-controls).
- The work is incident-specific (use payment-operations-incident-review).
- The work is data-access permissioning under §1033 (use open-banking-data-controls).
- The work is enterprise-wide and not payments-specific (use risk-compliance-core/risk-assessment with the payments-fintech overlay).
- The work is BSA / AML model monitoring or sanctions screening QA in isolation (use financial-crime-governance/aml-model-monitoring or sanctions-screening-qa with the payments-fintech overlay).

Anchored to: NACHA Operating Rules (current edition); Reg E (12 CFR Part 1005); Reg II (12 CFR Part 235); FedNow Service Operating Procedures; RTP Operating Rules (current); FFIEC BSA/AML Examination Manual; FinCEN MSB rules at 31 CFR Part 1022; Interagency Guidance on Third-Party Relationships (June 2023); OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements (July 2024) [verify date]; CFPB Supervisory Highlights (current cycles); state Money Transmitter laws (Money Transmitter Modernization Act adoption status [verify state-by-state]); OFAC sanctions enforcement guidance.
```

## Source anchors (skill-specific)

Named US sources, with section references where stable.

- **NACHA Operating Rules (current edition):**
  - Article Two ODFI / RDFI obligations [verify article numbering].
  - Return-rate thresholds (administrative, overall, unauthorized) [verify current thresholds and effective dates].
  - Same Day ACH (settlement windows and dollar limits) [verify].
  - WEB Debit account-validation rule (effective March 19, 2021) [verify exact rule text].
  - Third-Party Sender registration and risk-management rules [verify rule citations].
- **Reg E (12 CFR Part 1005):** §1005.6 unauthorized-transfer liability, §1005.11 error-resolution timing, §1005.18 prepaid.
- **Reg II (12 CFR Part 235):** debit-card interchange and routing.
- **Reg DD (12 CFR Part 1030):** APY and fee disclosure for deposit-like products.
- **Reg Z (12 CFR Part 1026):** where a credit-side product (BNPL, secured card, charge card) is in scope.
- **FedNow Service Operating Procedures (current)** [verify version date]; **RTP Operating Rules (current)** [verify version date] — settlement finality, fraud-hold mechanics, ISO 20022 message-field handling.
- **FFIEC BSA/AML Examination Manual** — CDD, ongoing monitoring, SAR, CIP, and the MSB-specific overlay where applicable.
- **FinCEN MSB rules (31 CFR Part 1022)** — registration, written AML program, CIP where applicable, SAR filing duties; FinCEN administrative rulings on which fintech configurations constitute money transmission [verify fact-specific rulings rather than asserting categorically].
- **State Money Transmitter laws** — adoption of the **Money Transmitter Modernization Act (MTMA)** [verify state-by-state adoption status as of the engagement date]; NMLS as the licensing system of record; **Multistate MSB Licensing Agreement** as the multistate processing channel.
- **OFAC sanctions:** 31 CFR Part 501, OFAC Compliance Commitments framework (2019), Specially Designated Nationals list maintenance posture.
- **Interagency Guidance on Third-Party Relationships, OCC / FRB / FDIC, June 6, 2023** — risk-based application to fintech relationships, including subcontractor and fourth-party expectations.
- **OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements, July 2024** [verify exact date and title] — sponsor-bank concentration, end-customer reconciliation, FBO-account expectations.
- **CFPB Supervisory Highlights (current cycles)** [verify which issues are current as of the engagement date] — recurring fintech themes (Reg E timing, account closure / hold UDAAP, fee disclosure, junk-fees).
- **Card-network rules, conceptual level:** Visa Core Rules, Mastercard Rules; chargeback rights, fraud-rate program escalations, BIN sponsor accountability [verify; cite as conceptual].
- **CFPB enforcement actions, public consent orders** [verify which are current] — public source for fact patterns on Buy Now Pay Later, wallet apps, and fintech account-holds / fee-disclosure.

Treat every external source as an anchor, not a substitute for legal interpretation. Date every citation in the output. Mark NACHA, Visa, Mastercard, RTP citations as "current edition; specific sections to be confirmed against the firm's licensed copy."

## Sector overlays needed

Only `payments-fintech` (this is the sector skill).

## Cross-cutting overlays

- `cross-cutting/cyber.md` — required where the rails depend on processors, ledger providers, and fraud-decision vendors with cyber-incident exposure (most do). Tie-in to NYDFS Part 500 where applicable, GLBA Safeguards, FFIEC IT booklets, and the sponsor-bank cyber-notification chain.
- `cross-cutting/conduct.md` — required where the program operator faces UDAAP exposure on fee disclosure, account closure, holds, dispute / Reg E timing, or dark-pattern risk. Cross-reference `consumer-compliance-fair-lending/udaap-risk-review` with the payments-fintech overlay.
- `cross-cutting/privacy.md` — recommended where customer-data flows for fraud and AML monitoring create privacy and GLBA Safeguards exposure beyond the basic obligations.

## Output template named sections

The dispatch instructions specify the structured axes (by rail, by customer segment, by geography). The output is a matrix-shaped artifact, not a narrative.

1. Program summary (program operator role, sponsor banks, processors, BIN sponsor, geographic footprint, customer base size).
2. **Risk universe — by rail.** One row per rail in scope, with columns: inherent risk, top three failure modes (rail-specific: ACH unauthorized-return-rate breach, card-network fraud-rate program escalation, FedNow request-for-return latency, etc.), key controls, residual risk, top three KRIs, owner role.
3. **Risk universe — by customer segment.** One row per segment (e.g., consumer / SMB / gig worker / payroll-on-demand / SMB-merchant / cross-border-remittance / high-risk vertical), with columns: inherent risk, top failure modes (UDAAP / dispute / chargeback / AML / sanctions), key controls, residual risk, top KRIs, owner.
4. **Risk universe — by geography.** One row per US state or country in scope, with columns: licensing posture (MTL / NMLS, MSB, state DFI registration), top failure modes (state UDAP, state breach-notification, state cross-border remittance), key controls, residual risk, owner.
5. **Concentration views.** Three sub-tables: sponsor-bank concentration, processor concentration, BIN-sponsor concentration. Each sub-table reports top-N share, scenario impact, and recommended risk-appetite posture. Cross-reference `third-party-operational-resilience/concentration-risk-review` with the payments-fintech overlay.
6. **Cross-cutting risks.** Fraud, AML / sanctions, operational resilience, customer-harm / UDAAP, reporting / data quality, cyber. One row per topic with risk owner, top three KRIs, and reference to the deep-dive skill (e.g., `aml-model-monitoring`, `sanctions-screening-qa`, `udaap-risk-review`, `cyber-disclosure-readiness`).
7. **Risk-appetite posture.** For each top-quintile cell in the matrix above: green / yellow / red against firm appetite [evidence needed]; trigger conditions for red-to-amber escalation.
8. **KRIs and reporting cadence.** KRI dictionary, with definition, source system, threshold (where set), owner, reporting cadence (board / ERC / sponsor-bank operating committee).
9. **Recommended remediation portfolio.** Each item: risk reference, action, owner role, target date, evidence link.
10. **Open items and named follow-ups with owners.**
11. **Source citations with date.**

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `program_id` | string | Internal identifier. |
| `program_role` | enum (`fintech_program_operator`, `BaaS_platform`, `program_manager`, `wallet_operator`, `neobank`, `payments_processor`, `money_transmitter_only`, `other`) | Drives matrix scope. |
| `rail_rows` | array of object | Each: rail, inherent_risk, top_failure_modes (array), key_controls (array), residual_risk, kris (array), owner_role. |
| `segment_rows` | array of object | Each: segment, inherent_risk, top_failure_modes, key_controls, residual_risk, kris, owner_role. |
| `geography_rows` | array of object | Each: jurisdiction (US state or country), licensing_posture (object: MTL / NMLS / MSB / DFI), top_failure_modes, key_controls, residual_risk, kris, owner_role. |
| `concentration_views` | object | Each of `sponsor_bank`, `processor`, `bin_sponsor`: top_N_share, scenario_impact, appetite_posture. |
| `cross_cutting_risks` | array of object | Each: topic, risk_owner_role, top_kris, deep_dive_skill_reference. |
| `risk_appetite_posture` | array of object | Each: cell_reference (rail x segment x geography), status (green / yellow / red), trigger_conditions. |
| `kri_dictionary` | array of object | Each: kri_id, definition, source_system, threshold, owner_role, cadence. |
| `remediation_portfolio` | array of object | Each: risk_reference, action, owner_role, target_date, evidence_link. |
| `open_items` | array of object | Each: description, owner_role, target_date. |
| `gaps` | array of gap | Each: description, source citation with date, severity, owner_role, target_close_date. |
| `recommended_disposition` | enum (`baseline_accepted`, `accept_with_conditions`, `remediate_then_re_baseline`, `escalate`) | Second-line recommendation. |
| `source_citations` | array of citation | Each: source name, section reference, retrieval date, URL where public. |

## Two example scenarios (public-source-derived, anonymous)

1. **Buy Now Pay Later program operator preparing its annual risk assessment after a CFPB action wave.** Public anchor: CFPB enforcement actions and Supervisory Highlights themes on BNPL [verify which are current, including any 2023-26 actions]; Reg E §1005.11 where the BNPL flow is run on debit-card rails; Reg Z applicability question for closed-end vs. open-end credit [verify how the firm has structured this]; UDAAP themes on fee disclosure and dispute timing. Scenario: the program operator runs BNPL across 2 sponsor processors and 30 US states, top failure modes by rail are debit-card chargeback timing and ACH unauthorized-return-rate breach, top failure modes by segment are SMB merchants and consumer dispute escalation, top failure modes by geography are states with active state-AG enforcement on BNPL fee disclosure (CA / NY / others). Skill output: matrix with rail / segment / geography rows, sponsor-processor concentration view, UDAAP cross-cutting risk callout, KRI dictionary with the dispute-timing KRI flagged red, and a remediation portfolio focused on Reg E timing reconciliation and fee disclosure refresh.
2. **Cross-border remittance fintech reassessing risk after adding RTP and a new corridor.** Public anchor: Reg E §1005.31 (remittance transfer rule subpart B) [verify exact citation and pre-payment / post-payment disclosure timing]; OFAC sanctions program; FFIEC BSA/AML manual; FinCEN MSB rules; state MTL adoption status [verify state-by-state]; RTP Operating Rules. Scenario: program operates in 25 states under MTL, adds three new sending corridors (one of which is high-OFAC-risk-adjacent), enables RTP for domestic legs, sponsor-bank-mediated USD funding, and top failure modes are sanctions-screening-vendor latency on the new corridors and Reg E §1005.31 disclosure-timing on RTP-funded sends. Skill output: rail rows (RTP, ACH, Wire, correspondent), segment rows (consumer / business-to-consumer / corridor-specific), geography rows (each US state plus each corridor country with sanctions-flag), processor concentration view, cross-cutting AML / sanctions deep-dive references, and a state MTL filing readiness gap.

Both scenarios use only public sources. CFPB Supervisory Highlights and public BNPL / remittance enforcement actions provide the conceptual fact patterns; no named institutions are used as fact-specific examples.

## Common pitfalls

- Starting from a generic enterprise-risk taxonomy and dropping payments-specific failure modes into it. The matrix has to be denominated in rails, segments, and geographies; the failure modes follow.
- Asserting a state's MTL posture without checking MTMA adoption and current NMLS status for that state on the engagement date. The right answer is state-by-state.
- Using a single "concentration risk" line. Sponsor-bank, processor, and BIN-sponsor concentration are three separate views and they fail differently.
- Skipping the cross-cutting UDAAP layer for "this is risk, not consumer compliance." Reg E timing failures, fee disclosure failures, and account-closure / hold practices are the highest-frequency examiner findings in this lane.
- Treating the BNPL flow as a single rail when it is debit-card or ACH or both depending on the cohort. The risk profile changes with the rail.
- Letting the geography row default to "USA" when state MTLs and state UDAP regimes are the operative obligations.
- Omitting cross-border and FX-specific failure modes for a remittance flow because the firm thinks of itself as "domestic with international corridors." The Reg E §1005 subpart B remittance-transfer rule is its own beast.
- Drafting the artifact as a heat-map without the supporting rows. A heat-map without the underlying matrix loses the auditability the artifact exists to provide.
