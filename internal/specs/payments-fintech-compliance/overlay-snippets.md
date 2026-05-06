# Payments-fintech overlay snippets

Plugin: `sector-plugins/payments-fintech-compliance`
Phase: 1 (overlay outlines that feed capability-skill spec sheets and v1 phase-2 content).

These outlines define what the payments-fintech overlay reference (`references/sector-overlays/payments-fintech.md`) must cover inside each named capability skill. They are the v1 home for sector flavor that does not warrant a standalone payments-fintech-only skill. The four sector-only skills (`fintech-partner-controls`, `open-banking-data-controls`, `payment-operations-incident-review`, `payments-risk-assessment`) carry the artifacts that the capability primitives cannot produce; these overlays carry the rest.

Audience: payments compliance officers, BSA officers at fintechs and MSBs, third-party payment risk teams at sponsor banks, BaaS oversight teams, payment operations compliance leads.

---

## third-party-operational-resilience / vendor-diligence

Purpose: when the capability vendor-diligence skill is run on a payments or fintech counterparty, the payments-fintech overlay tells the reviewer what is rail-specific, sponsor-bank-specific, and money-transmitter-specific, and which named guidance sets the bar.

- US-deep frame: Interagency Guidance on Third-Party Relationships (OCC / FRB / FDIC, June 6, 2023) is the spine for any bank-side review of a fintech counterparty. The lifecycle (planning, due diligence, contract, ongoing monitoring, termination) maps cleanly onto the capability template; the overlay should call out the risk-based application to fintech relationships, including subcontractors and fourth parties (the processor, ledger provider, KYC vendor, fraud-decision vendor are the usual fourth-party pyramid).
- OCC / FRB / FDIC Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services (July 25, 2024) [verify exact date and title] is the operative document for sponsor-bank programs. Diligence on a BaaS or program-operator counterparty must cover end-customer reconciliation, FBO subledger posture, deposit-insurance representation review, customer-facing FDIC framing, and operational resilience of the program operator. The 2023 RFI on bank-fintech arrangements is not the binding statement; phase 2 cite-checks must catch this conflation [verify which artifacts are operative on the date of analysis].
- Vendor-type taxonomy specific to payments-fintech: sponsor bank, BaaS platform, processor (front-end, back-end, gateway), program manager, BIN sponsor, ledger provider, card-issuance vendor, KYC / CIP vendor, fraud-decision vendor, sanctions-screening vendor, dispute-management vendor, FedNow / RTP gateway, ACH originator-of-record vendor (the Third-Party Sender), and aggregator / developer-portal vendor. Each pulls a different rule set into the diligence checklist.
- NACHA Operating Rules (current edition) Third-Party Sender registration and risk-management rules [verify rule citations] apply to any counterparty acting as a Third-Party Sender on the firm's ODFI authority. Diligence must include the registration status, the Originator agreements the Third-Party Sender holds, and the return-rate-monitoring posture against current NACHA thresholds (administrative-return, overall-return, unauthorized-return) [verify current thresholds].
- FinCEN MSB rules (31 CFR Part 1022) where the counterparty is itself a money transmitter or registered MSB: registration on file, written AML program, CIP applicability, SAR-filing posture, and any FinCEN administrative ruling fact-patterns relevant to the configuration [verify on a fact-specific basis rather than asserting categorically]. Diligence on a money transmitter counterparty must verify NMLS status state-by-state and Money Transmitter Modernization Act adoption posture in the firm's footprint [verify state-by-state adoption status as of the date of analysis].
- Card-network conceptual citations: Visa Core Rules and Visa Product and Service Rules; Mastercard Rules. BIN sponsor accountability for chargeback rights, fraud-rate program escalations, and program-level reporting. Mark all card-network citations as "current edition; specific sections to be confirmed against the firm's licensed copy" because the rulebooks are not public.
- Reg E (12 CFR Part 1005) §1005.6, §1005.11, §1005.18 obligations the program operator owes downstream to consumers must be evidenced in the diligence even where the depository is the bank. The program agreement nearly always pushes operational ownership of error intake to the fintech, and the diligence has to capture that allocation.
- Cyber and resilience layer pulled in from `cross-cutting/cyber.md`: NYDFS Part 500 where the counterparty is a covered entity, GLBA Safeguards Rule passed through the program agreement, FFIEC IT booklets used by sponsor-bank examiners, sponsor-bank breach-notification chain.
- Output-template additions for payments-fintech vendor-diligence: rail-by-rail counterparty role; sponsor-bank and BIN-sponsor identification; MSB / MTL state-by-state licensing matrix; NACHA Third-Party Sender posture; subcontractor / fourth-party register; FBO subledger reconciliation evidence; deposit-insurance representation review.

---

## third-party-operational-resilience / exit-plan

Purpose: payments-rail wind-down adds rail-specific irrevocability, settlement-finality, and customer-transfer mechanics that the generic exit-plan skill does not own.

- Sponsor-bank termination is the dominant scenario. Program-agreement termination clauses, regulator-cooperation clauses, customer-data-portability clauses, and customer-notification timing have to be the centre of gravity. Anchored to Interagency Guidance on Third-Party Relationships (June 2023) and OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements (July 2024) [verify exact date].
- Rail-by-rail wind-down mechanics: ACH and Same Day ACH (settlement window cutovers; in-flight returns; ODFI re-papering with successor sponsor); wire (Fedwire / CHIPS counterparty handoff); FedNow and RTP (real-time settlement finality; in-flight requests-for-return-of-funds; ISO 20022 routing changes); card debit / credit (BIN re-sponsorship, processor re-platforming, chargeback in-flight transfer); check (where applicable; positive-pay file handoff); cross-border correspondent (correspondent-bank reaffiliation, OFAC re-screening of in-flight items).
- Customer-transfer mechanics: FBO subledger transfer to successor sponsor, in-flight Reg E §1005.11 claim transfer with the 10 / 45 / 90-day clock preserved, in-flight NACHA returns and reversals, in-flight card chargebacks, in-flight FedNow / RTP requests-for-return-of-funds. The clocks do not stop because the program is moving.
- Deposit-insurance representation handoff under the July 2024 joint statement: customer-facing FDIC framing must be re-papered for the successor sponsor, and the firm must evidence the change-control loop.
- State MTL and NMLS posture during a sponsor change: many state MTL regimes require notification of material change in sponsor or business model; NMLS filings have their own clocks [verify state-by-state].
- Subcontractor and fourth-party transfer: processor consents, ledger-provider consents, fraud-decision vendor re-papering, KYC / CIP vendor handoff if the data-residency posture changes.
- BSA / AML continuity: the SAR-filing chain, sanctions-screening cadence, and CIP records must remain unbroken; a transition gap is examiner red meat. Anchored to FFIEC BSA/AML Examination Manual; FinCEN MSB rules at 31 CFR Part 1022 where applicable.
- Output-template additions: rail-by-rail wind-down sequence with cutover dates, in-flight-item carry-over register, FBO-subledger reconciliation milestones, sponsor-bank notification log against program-agreement clauses, state MTL / NMLS notification log, customer-facing communication log (Reg E §1005.8(a) change-of-terms timing where applicable [verify]), successor-vendor onboarding evidence list.

---

## third-party-operational-resilience / concentration-risk-review

Purpose: payments-fintech concentration risk has three distinct axes that fail differently. The capability skill is rail-agnostic; the overlay names the axes and the failure modes.

- Sponsor-bank concentration: percentage of deposits / volume / customer count routed through each sponsor bank. Failure mode: a single sponsor bank exiting the program (consent-order-driven, business-decision-driven, or merger-driven) leaves the program operator without a depository and without rails. Mitigation patterns: dual-sponsor architecture, pre-papered standby sponsor, rail-redundancy posture per rail. Anchored to OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements (July 2024) [verify date] and to the wave of 2023-24 sponsor-bank consent orders touching BaaS reconciliation [verify which actions are current as of the date of analysis].
- Payments-processor concentration: percentage of volume / value through each processor on each rail. Failure mode: processor outage, processor consent-order, or processor pricing change cascades into customer-impact and Reg E §1005.11 timing. Mitigation: dual-processor architecture, rail-by-rail redundancy, in-flight migration capability. Cross-link to `payments-risk-assessment` rail rows.
- BIN sponsor concentration: percentage of card volume / outstanding cards under each BIN sponsor. Failure mode: BIN sponsor exit, network-rule change cascading through the BIN sponsor, fraud-rate program escalation at the BIN-sponsor level (Visa / Mastercard). Mitigation: dual-BIN posture, debit-vs-credit BIN separation, network-by-network coverage.
- Geographic concentration overlay: state MTL footprint concentration creates state-AG-action exposure; cross-border corridor concentration creates OFAC and correspondent-banking exposure. Anchored to state Money Transmitter Modernization Act adoption status [verify state-by-state] and OFAC sanctions enforcement guidance.
- KRI dictionary additions: top-N share for each axis, headroom-to-appetite, scenario-impact under single-counterparty exit, time-to-cutover for each rail under each axis.
- Output-template additions: three sub-tables (sponsor-bank, processor, BIN-sponsor) with top-N share, scenario impact, and recommended risk-appetite posture; geographic concentration callout; cross-link to `payments-risk-assessment` concentration views to avoid double-counting.
- Common pitfalls to capture: treating "vendor concentration" as a single metric (the three axes fail differently); benchmarking against the firm's own history rather than the rail's actual recovery time; missing the BIN-sponsor axis entirely because it is invisible to non-card teams.

---

## financial-crime-governance / aml-model-monitoring

Purpose: MSB BSA monitoring and payment-channel-specific scenarios are not in the bank-flavored capability monitoring frame.

- US-deep frame: FFIEC BSA/AML Examination Manual sets the supervisory expectation, and FinCEN MSB rules (31 CFR Part 1022) set the program obligations for any program operator that is itself a money transmitter. The overlay must call out that MSB monitoring is not bank monitoring: CIP applicability is fact-specific, the SAR threshold is the same ($2,000 / $5,000 with bank-attempt knowledge — verify), but the typology library is payment-channel-shaped.
- Payment-channel-specific scenarios the monitoring model must cover: structuring across debit-card load-and-spend cycles; layering through P2P, wallet-to-wallet, and ACH-to-card flows; trade-based money laundering signals on cross-border remittance corridors; mule patterns on instant-funded accounts (FedNow, RTP, Same Day ACH inbound); BNPL repayment-pattern anomalies; payroll-on-demand abuse patterns; gig-economy disbursement-pattern anomalies; high-risk-merchant chargeback / refund laundering on card rails; gambling and high-risk-vertical funding patterns; sanctioned-jurisdiction proximity on cross-border corridors [verify which jurisdictions are sanctioned on the date of analysis against OFAC SDN and 50%-rule lists].
- ODFI / RDFI risk-monitoring posture under NACHA Operating Rules (current edition): the program operator owes upstream visibility into Originator behavior; return-rate monitoring against current NACHA thresholds (administrative-return, overall-return, unauthorized-return) is the proxy [verify current thresholds].
- Faster-payments-specific signals: FedNow and RTP fraud holds, ISO 20022 message-field anomalies (suspicious creditor account, suspicious end-to-end ID), velocity at the rail level vs at the customer level, irrevocability-driven typology shift (no chargeback path means the fraud playbook is request-for-return-of-funds plus monitoring escalation, not dispute).
- Sponsor-bank reliance posture: is the program operator running its own monitoring stack, relying on the sponsor bank, or running a hybrid? CFPB and prudential agencies expect the program operator to evidence its own line of sight into the typologies even where the SAR-filing happens at the sponsor.
- CFPB Circular series [verify specific circular numbers and dates relevant to AML / payments fraud as of the date of analysis] — supervisory signaling on payments-AML overlap with consumer-compliance.
- Output-template additions: payment-channel-by-channel typology coverage matrix; rail-specific KRI dictionary (return-rate, fraud-rate, sanctions-hit-rate per rail); MSB program-element status against 31 CFR Part 1022 if applicable; sponsor-bank reliance posture; cross-link to `sanctions-screening-qa` for the sanctions overlay.

---

## financial-crime-governance / sanctions-screening-qa

Purpose: cross-border payments, correspondent banking, and virtual-currency exposure are payments-fintech-specific sanctions-screening concerns.

- US-deep frame: OFAC Compliance Commitments (May 2019) and 31 CFR Part 501 set the program structure; the OFAC SDN list, sectoral sanctions, and 50%-rule subsidiaries are the daily input. The overlay must call out the operational reality that sanctions screening on cross-border payments and correspondent flows is denominated in transaction volume, not customer count, and the QA program has to reflect that.
- Cross-border payment screening: corridor-by-corridor screening cadence, message-field coverage (originator, beneficiary, ordering institution, beneficiary institution, intermediary; ISO 20022 expanded fields for SWIFT-equivalent flows), false-positive disposition QA, true-positive escalation QA, batch vs real-time screening posture for FedNow / RTP cross-border edge cases [verify which faster-payments rails are in scope for cross-border on the date of analysis].
- Correspondent banking exposure: where the program operator is using a sponsor bank's correspondent relationships, the screening obligation is contractual through the program agreement and supervisory through the FFIEC BSA/AML manual chapter on correspondent accounts for foreign banks. The QA program has to evidence end-to-end coverage, not just front-door screening.
- Virtual currency exposure: FinCEN guidance on virtual currency (FIN-2013-G001, FIN-2019-G001) [verify currency of citations as of the date of analysis] applies where the program operator interacts with money services involving convertible virtual currency. Travel Rule applicability under 31 CFR §1010.410(f) for transmittals of $3,000 or more [verify current threshold]; FinCEN proposed rule changes on the threshold [verify status]. Screening posture on VASP counterparties; chain-analytics vendor evidence.
- Card-network sanctions posture: BIN-level controls, cross-border merchant screening, sanctioned-merchant blocking (Visa Core Rules and Mastercard Rules require issuer-level controls, conceptual citation only [verify against licensed copy]).
- Sanctions-screening vendor QA: false-positive rate baseline by corridor, true-positive aging, list-update latency, fuzzy-matching threshold posture, manual-review queue aging, audit-trail completeness. Anchored to OFAC Compliance Commitments and to public OFAC enforcement actions where vendor-tuning failures were the root cause [verify which actions are current as of the date of analysis].
- Sponsor-bank reliance posture: same as AML — running own stack vs relying on sponsor vs hybrid. The fintech program operator has to evidence its line of sight even if the OFAC-blocking-and-rejecting reports go through the sponsor.
- Output-template additions: corridor-by-corridor screening coverage matrix; virtual-currency-counterparty register (if applicable); Travel Rule applicability log; vendor-tuning evidence pack; sponsor-bank reliance posture; cross-link to `payments-risk-assessment` geography rows.

---

## consumer-compliance-fair-lending / udaap-risk-review

Purpose: fintech UDAAP enforcement themes are payment-channel-specific. The capability UDAAP skill is built around bank deposit and credit products; the overlay carries the fintech-specific themes the CFPB has been signalling on.

- Fintech UDAAP enforcement themes from CFPB Supervisory Highlights and consent orders (2023-26) [verify which actions are current as of the date of analysis]:
  - Account closures and account holds without adequate notice or recourse — the most-frequent fintech UDAAP theme. The overlay must list the named control families: notice timing, customer-recourse channel, complaint-routing-to-sponsor-bank loop, account-closure root-cause review.
  - Reg E error-resolution timing failures presented as UDAAP rather than as Reg E findings (the CFPB has been pursuing both lanes simultaneously) [verify].
  - Fee disclosure failures — junk-fee themes, surprise-fee patterns, NSF / overdraft framing on fintech accounts (CFPB Circular 2022-06 on unanticipated overdraft fees [verify circular number and date]; CFPB guidance on surprise overdraft and junk fees).
  - Marketing claim review for FDIC-insurance representation — the Synapse-era 2023-24 enforcement and prudential-agency statements mean any "FDIC-insured" framing on fintech surfaces must be re-papered to the pass-through caveats. Anchored to OCC / FRB / FDIC Joint Statement (July 2024) [verify date] and FDIC misrepresentation rule (12 CFR Part 328 Subpart B, May 2022) [verify exact citation].
  - BNPL UDAAP themes — fee disclosure, dispute-rights presentation, comparative-shopping framing. Anchored to CFPB BNPL market-monitoring report (September 2022) and any subsequent CFPB BNPL actions [verify].
  - Dark-pattern risk in onboarding and product-selection flows — CFPB Circular 2023-XX [verify which circulars address dark patterns directly]; FTC dark-pattern guidance.
  - Larger-participant rule for digital wallets and payment apps (CFPB final rule, December 2024) [verify Federal Register citation, effective date, and current state including any litigation or congressional review]. The rule brings designated non-bank larger participants into direct CFPB supervision and changes the UDAAP-review posture for in-scope fintechs.
- Reg E §1005.11 timing as a UDAAP signal: where error-resolution claims sit beyond the 10 / 45 / 90-day windows, examiners pursue both Reg E and UDAAP findings.
- Fee-disclosure-vs-actual reconciliation: the operative test is the disclosure language vs the actual flow on a per-product, per-cohort basis.
- Sponsor-bank UDAAP cross-pollination: a fintech UDAAP finding can flow upstream to the sponsor bank's CFPB or prudential-supervisory file under the bank-fintech-arrangements lens.
- Output-template additions: theme-by-theme control review (account-closure / hold; Reg E timing; fee disclosure; FDIC representation; BNPL; dark patterns); larger-participant rule applicability check; sponsor-bank UDAAP cross-pollination posture; complaint-data triangulation (CFPB Consumer Complaint Database, internal complaint data, sponsor-bank-routed complaint data).

---

## regulatory-change-management / exam-brief

Purpose: fintech exam-prep nuances under the sponsor-bank model and under direct CFPB supervision of larger non-bank participants are sufficiently different from bank exam-prep that the capability exam-brief must inherit a payments-fintech overlay.

- Two-track exam posture: most fintechs are not directly examined by a federal prudential agency, but they are examined indirectly through the sponsor bank's third-party-risk file, and increasingly directly by the CFPB under §1024 supervisory authority for larger participants and §1031 / §1036 enforcement authority more broadly. State exam-prep is a third track for any money transmitter (state DFI / DOB exams via NMLS). The overlay must lay out all three tracks and tell the brief which is operative.
- Sponsor-bank-led review (annual or off-cycle): the document-request playbook is the program-agreement clause set, the prior-year findings, the controls inventory, the FBO subledger reconciliation evidence, the Reg E / NACHA / card-network metrics, the deposit-insurance representation review, and the fourth-party register. Anchored to Interagency Guidance on Third-Party Relationships (June 2023) and OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements (July 2024) [verify date].
- CFPB direct supervision under §1024 larger-participant rules: the digital wallets and payment apps larger-participant rule (December 2024) [verify Federal Register citation, effective date, and current state including any litigation or congressional review] designates a covered cohort. The brief must check applicability and, where in scope, prepare the CFPB EXAMS-equivalent posture (entry conference, scope letter, document-request, exit conference, MRA / MRIA equivalents [verify CFPB-specific terminology]).
- State MTL exam-prep: state-by-state with significant variation; NMLS as the licensing system of record. The brief must check Money Transmitter Modernization Act adoption status [verify state-by-state] and any state-specific rules (e.g., NY DFS BitLicense for VC activity, CA DFPI rulemaking under the Money Transmission Act and California Consumer Financial Protection Law).
- CFPB Circular series [verify which circulars are current as of the date of analysis] — supervisory signaling that should be picked up in the brief: account-closure / hold, junk-fees, Reg E timing, BNPL, dark patterns, FDIC misrepresentation.
- FinCEN exam-prep where the program operator is an MSB: FFIEC BSA/AML Examination Manual chapters; FinCEN administrative-ruling library; SAR-filing posture and MSB registration evidence.
- Privilege posture: many fintech exam interactions go through the sponsor bank, with privilege complications (joint-defense, common-interest, work-product). The brief must flag privilege boundaries before any document goes outbound.
- Output-template additions: three-track scoping (sponsor-bank-led, CFPB-direct, state-MTL); larger-participant-rule applicability log; state-by-state NMLS posture; sponsor-bank coordination calendar; privilege-boundary log; cross-link to `fintech-partner-controls` self-evidence pack.

---

## Notes

- Each overlay-snippet outline above feeds two artefacts in phase 2: the payments-fintech overlay reference inside the relevant capability skill (`references/sector-overlays/payments-fintech.md`), and an explicit cross-link from the capability skill's `SKILL.md` so the reviewer is prompted to check the overlay when a payments-fintech use case is in scope.
- Where a citation is marked [verify], phase 2 should confirm the exact rule text, model number, Federal Register citation, effective date, and current state (including any litigation, withdrawal, or congressional review) before the citation goes into a SKILL.md. The payments-fintech regulatory pipeline has been unusually active in 2023-2026 (Interagency TPRM Guidance, joint statements on bank-fintech arrangements, §1033 final rule, larger-participant rule for digital wallets, MTMA state-by-state adoption); annual minimum re-validation.
- No invented regulatory facts. Public sources only. NACHA and card-network rulebook citations are paywalled and must be flagged as "current edition; specific sections to be confirmed against the firm's licensed copy."
