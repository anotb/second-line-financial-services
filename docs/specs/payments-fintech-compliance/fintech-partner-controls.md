# Spec sheet: fintech-partner-controls

Plugin: `sector-plugins/payments-fintech-compliance`
Status: v1 retained skill (sector-unique under strict overlay rule).
Phase: 1 (spec only; no SKILL.md content here).

## Why this is a sector-only skill

This skill sits on the fintech side of the bank-fintech relationship. The lens is the fintech program operator (or its second-line risk and compliance team) drafting and self-evidencing the controls a sponsor bank, a regulator, or an external assessor will look for. The capability skill it does not duplicate is `third-party-operational-resilience/vendor-diligence`, which is the bank-side lens (the bank evaluating the fintech). Different artifact, different audience, different evidence source.

There is also a near-neighbour skill in the banking sector overlay: `banking/bank-fintech-partnership-review`. That one is also bank-side (a sponsor bank doing principal-side oversight of its BaaS or fintech program). Boundary call below in the AUDIT memo.

The work here is sector-only because the controls inventory is payments-rail-specific (NACHA, card networks, FedNow / RTP, money-transmitter activity), the consumer-protection backbone is payments-specific (Reg E §1005.11 error resolution, Reg E §1005.6 unauthorized transfer liability, Reg DD where the deposit-like product wrapper applies), and the regulatory exposure flows through the sponsor-bank model, FBO-account mechanics, and the OCC / FRB / FDIC June 2023 Interagency Guidance on Third-Party Relationships plus the July 2023 Joint Statement on Bank-Fintech Arrangements [verify exact joint-statement date]. None of that is in scope for the generic capability vendor skill.

## Activation-tuned description

```
Drafts a fintech-side control inventory and self-evidence pack for a sponsor-bank or BaaS arrangement, mapped to Reg E error-resolution duties, NACHA Operating Rules obligations the program operator owes upstream, money-transmitter / MSB BSA posture where applicable, FBO-account mechanics, and the sponsor-bank oversight clauses in the underlying program agreement. Output is review-ready for the fintech's own second line and for production to the sponsor bank's third-party risk function.

Best for:
- A fintech, neobank, BaaS program, or wallet operator is preparing or refreshing its control pack for a sponsor-bank annual review, a sponsor-bank-led audit, or a state MTL exam.
- Compliance has been asked to self-evidence Reg E error-resolution timing (10/45/60-day windows), NACHA return handling, or unauthorized-transfer liability allocation between fintech and bank.
- A new payment rail (e.g., FedNow, RTP) or new product (e.g., debit-card program, instant payouts, secured card) is being added under the sponsor-bank's existing oversight envelope and the program operator needs the delta-control pack.
- An incoming sponsor bank, processor, or program manager has issued a control questionnaire (SIG, CAIQ-style, or bespoke) and the fintech's second line is preparing a defensible response.

Not the right tool when:
- The user is the sponsor bank itself doing principal-side oversight (use banking/bank-fintech-partnership-review, or third-party-operational-resilience/vendor-diligence with the payments-fintech overlay).
- The work is incident-specific (use payment-operations-incident-review).
- The work is a top-down rail-and-segment risk assessment rather than a controls inventory (use payments-risk-assessment).
- The work is data-access permissioning under §1033 / open finance (use open-banking-data-controls).
- The work is purely a UDAAP themes review of fintech marketing or fee disclosure (use consumer-compliance-fair-lending/udaap-risk-review with the payments-fintech overlay).

Anchored to: Interagency Guidance on Third-Party Relationships (OCC / FRB / FDIC, June 6, 2023); OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements (July 2023) [verify exact date]; Reg E (12 CFR Part 1005), in particular §1005.6 (unauthorized transfers), §1005.11 (error resolution), §1005.18 (prepaid accounts); Reg DD (12 CFR Part 1030); Reg II (12 CFR Part 235); NACHA Operating Rules (current edition) [verify article and section numbers per cited rule]; FinCEN MSB rules at 31 CFR Part 1022 where the program is a money transmitter; state Money Transmitter laws under the Money Transmitter Modernization Act framework as adopted state-by-state via NMLS [verify state-by-state adoption status]; CFPB Section 1033 Personal Financial Data Rights Final Rule (October 2024) where data-access duties touch the partner program [verify implementation tier and litigation status].
```

## Source anchors (skill-specific)

Named US sources, with section references where stable. URL alone is not sufficient; phase 2 source-anchors.md must include cited excerpts.

- Interagency Guidance on Third-Party Relationships, Federal Register, OCC / FRB / FDIC, June 6, 2023 — full lifecycle expectations (planning, due diligence, contract, ongoing monitoring, termination), risk-based application to fintech relationships, and explicit treatment of subcontractors and fourth parties.
- OCC / FRB / FDIC Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services, July 25, 2024 [verify exact date and title] — sponsor-bank expectations for end-customer reconciliation, FBO-account ledgering, customer-facing disclosures about deposit-insurance posture, and operational resilience of the program operator.
- Reg E (12 CFR Part 1005):
  - §1005.6 — consumer liability for unauthorized EFTs (the 2-day / 60-day liability tiers); allocation between fintech and bank under the program agreement.
  - §1005.11 — error-resolution procedures, the 10-business-day investigation window, the 45-day extended window, the 90-day window for new accounts and POS / foreign-initiated transactions, provisional credit duties, and written notification timing.
  - §1005.18 — prepaid-account-specific overlays (registered vs unregistered accounts, error-resolution applicability, fee disclosure).
- Reg DD (12 CFR Part 1030) — APY disclosure, fee schedule, periodic statement obligations where the fintech surface presents a deposit-like product.
- Reg II (12 CFR Part 235) — debit-card interchange and routing; relevance is mostly bank-side, but program-operator processor configuration and merchant-routing posture are inspectable items.
- NACHA Operating Rules (current edition):
  - Article Two — ODFI / RDFI obligations; the program operator's role under the bank's ODFI status [verify article numbering against the current edition].
  - Same Day ACH provisions; WEB Debit account-validation rule (effective March 19, 2021) [verify exact rule text and section reference].
  - Return reason codes, return timeframes (R01-R85 family) [verify codes and timeframes]; ODFI return-rate thresholds (administrative-return rate, overall return rate, unauthorized-return rate) [verify current thresholds].
  - Risk-management rules including Third-Party Sender registration, Originator / Third-Party Sender risk monitoring [verify rule citations].
- FinCEN MSB rules (31 CFR Part 1022) — money transmitter registration, written AML program, Customer Identification Program (CIP) where applicable, SAR filing duties, currency transaction reporting; FinCEN administrative rulings on which fintech configurations constitute money transmission [verify the fact-pattern-specific rulings rather than asserting a categorical answer].
- State Money Transmitter laws — adoption status of the Money Transmitter Modernization Act (MTMA) and the Multistate MSB Licensing Agreement varies by state [verify state-by-state adoption status]; NMLS is the licensing system of record for most states.
- CFPB Personal Financial Data Rights Final Rule under §1033, October 2024 [verify Federal Register publication date and citation; verify litigation status and implementation timeline] — relevant where the partner program is a covered data provider or is contracting with one; further detail in `open-banking-data-controls`.
- Card network rules, conceptual level only:
  - Visa Core Rules and Visa Product and Service Rules — issuer / sponsor / program-manager allocations, chargeback-rights framework.
  - Mastercard Rules — equivalent allocations and chargeback framework.
  - Both: BIN sponsorship, dispute / chargeback timeframes, fraud-rate program escalations [verify thresholds; treat as conceptual citations].

Treat every external source as an anchor, not a substitute for legal interpretation. Date every citation in the output. Mark any rule citation that is non-public or paywalled (NACHA, card network rulebooks) as "current edition; specific sections to be confirmed against the firm's licensed copy."

## Sector overlays needed

Only `payments-fintech` (this is the sector skill).

## Cross-cutting overlays

- `cross-cutting/cyber.md` — required. NYDFS Part 500 where the program operator is a covered entity (or where the sponsor bank requires equivalent posture), GLBA Safeguards Rule expectations passed through the program agreement, FFIEC IT booklets used by sponsor-bank examiners, and the sponsor-bank breach-notification chain.
- `cross-cutting/privacy.md` — recommended. GLBA privacy notice posture, state privacy laws (CCPA / CPRA, CT / CO / VA / UT and the rest) for the customer-data flows, and the §1033 implications where data-access permissioning intersects with control design.
- `cross-cutting/conduct.md` — optional but useful. Fee disclosure, account-closure / hold UDAAP themes, dark-pattern risk in onboarding flows; cross-references to `consumer-compliance-fair-lending/udaap-risk-review` with the payments-fintech overlay.

## Output template named sections

Practitioner headings on the default-output template:

1. Program summary (rails in scope, products, sponsor bank(s), processors, program manager, BIN sponsor, customer base, geographic footprint).
2. Regulatory perimeter (sponsor-bank charter type, fintech licensing posture: MTL state list, MSB FinCEN registration, state-by-state NMLS status, broker-dealer or other adjacent licenses if applicable).
3. Program-agreement control map (oversight clauses, audit rights, change-control rights, termination and exit, indemnification, regulatory-cooperation clauses, customer-data ownership clauses).
4. Reg E controls (§1005.6 unauthorized-transfer allocation; §1005.11 error-resolution timing 10/45/90-day windows; provisional credit posture; §1005.18 if prepaid; reconciliation of who-receives-the-claim between fintech and bank).
5. NACHA controls (ODFI / Third-Party Sender posture, return-rate monitoring against current thresholds, WEB Debit account-validation, Same Day ACH limits and risk holds, Originator agreements and ODFI sub-agreements; settlement reconciliation).
6. Card-network controls (chargeback intake and timing, fraud monitoring, Visa / Mastercard program-level reporting where applicable; BIN sponsor coordination).
7. Faster-payments controls (FedNow Service, RTP) — fraud holds, ISO 20022 message field handling, irrevocability posture, customer dispute pathway given the lack of Reg E coverage of certain real-time pull flows [verify].
8. FBO-account mechanics (subledger reconciliation cadence, escheatment, deposit-insurance pass-through requirements per the July 2024 joint statement, customer-facing FDIC representation review).
9. BSA / AML / sanctions controls (CIP, ongoing monitoring, SAR filing posture if MSB, sanctions-screening cadence, reliance on sponsor bank vs. fintech-direct posture, OFAC list updates).
10. Customer-protection controls (UDAAP-relevant fee disclosure, account-closure and hold procedures, complaint intake routing to sponsor bank, error-correction loops).
11. Cyber and resilience controls (incident escalation chain to sponsor bank within program-agreement timeframes, BCP / DR coverage, third-party / fourth-party register).
12. Subcontractor and fourth-party controls (processor, KYC vendor, fraud-decision vendor, card processor, ledger provider).
13. Self-evidence pack (artifact list cross-referenced to each controls section above; named owner role; evidence freshness).
14. Gaps, issues, and recommended remediation (each gap: source citation with date, severity, owner, target close date).
15. Open items and named follow-ups with owners.
16. Source citations with date.

## Structured output fields

Drafted for the schema author in phase 2.

| Field | Type | Purpose |
|---|---|---|
| `program_id` | string | Internal identifier for the partner program under review. |
| `program_role` | enum (`fintech_program_operator`, `BaaS_platform`, `program_manager`, `wallet_operator`, `neobank`, `payments_processor`, `other`) | Drives which control sections apply. |
| `rails_in_scope` | array of enum (`ACH`, `Same_Day_ACH`, `Wire`, `FedNow`, `RTP`, `Card_debit`, `Card_credit`, `Check`, `Cross_border_correspondent`, `Card_prepaid`) | Determines NACHA / card-network / faster-payments overlays. |
| `sponsor_banks` | array of object | Each: bank name (where public), charter type (national bank / state member / state non-member / state-chartered ILC / other), program agreement effective date, agreement type (BaaS / sponsor / processor). |
| `licensing_posture` | object | MTL state list with NMLS IDs (or `[verify]` flag), FinCEN MSB registration, broker-dealer / SEC / state adjacent licenses where applicable. |
| `program_agreement_findings` | array of finding | Each finding: clause, expectation (per Interagency TPRM and July 2024 joint statement), present / absent, severity. |
| `reg_e_findings` | array of finding | §1005.6 / §1005.11 / §1005.18 controls present / absent, with the timing and provisional-credit observations. |
| `nacha_findings` | array of finding | ODFI obligations, Third-Party Sender posture, return-rate thresholds, WEB Debit account-validation, Same Day ACH controls. |
| `card_network_findings` | array of finding | Visa / Mastercard chargeback timing, fraud thresholds, BIN sponsor coordination. |
| `faster_payments_findings` | array of finding | FedNow / RTP fraud-hold, ISO 20022 message integrity, dispute pathway posture. |
| `fbo_findings` | array of finding | Subledger reconciliation, escheatment, deposit-insurance pass-through, FDIC representation review. |
| `bsa_aml_findings` | array of finding | CIP, monitoring, SAR posture, sanctions screening, MSB obligations where applicable. |
| `udaap_findings` | array of finding | Fee disclosure, account-closure / hold practice, complaint routing. |
| `cyber_resilience_findings` | array of finding | Incident escalation cadence, BCP / DR posture, vendor inventory. |
| `subcontractor_inventory` | array of object | Each: vendor name (where public), function, criticality, evidence-of-oversight artifact. |
| `self_evidence_index` | array of object | Each: control reference, artifact name, owner role, last-refreshed date, freshness flag. |
| `gaps` | array of gap | Each: description, source citation with date, severity, owner, target close date. |
| `issues` | array of issue | Material issues elevated to risk register or audit. |
| `recommended_disposition` | enum (`ready_for_sponsor_bank_review`, `ready_with_conditions`, `remediate_then_re_review`, `not_ready`) | Second-line recommendation, not a decision. |
| `conditions` | array of string | Conditions attached to a ready-with-conditions disposition. |
| `open_items` | array of item | Each: description, owner, target date. |
| `source_citations` | array of citation | Each: source name, section / rule reference, retrieval date, URL where public; private-rulebook citations marked accordingly. |

## Two example scenarios (public-source-derived, anonymous)

1. **BaaS program operator preparing for a sponsor-bank annual review after a public 2024 enforcement wave on bank-fintech reconciliation.** Public anchor: OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements (July 2024) [verify exact date]; Interagency TPRM Guidance, June 6, 2023; CFPB consent orders against fintech-adjacent program operators with respect to deposit-account misrepresentation and FBO-account reconciliation. Scenario: the program operator runs a checking-equivalent product across two sponsor banks, FBO subledger reconciliation cadence is daily but exception-resolution SLA is undocumented, customer-facing disclosure includes "FDIC-insured" framing without the pass-through caveats, and the recent migration to a new ledger provider has not been re-papered through the program-agreement change-control clause. Skill output: program-agreement gaps (change-control, FDIC representation review), reconciliation gap (exception-resolution SLA), and a self-evidence index showing the artifacts the sponsor bank's TPRM team will request.
2. **Mid-stage neobank adding FedNow-funded instant payouts under an existing sponsor-bank ACH agreement.** Public anchor: FedNow Service Operating Procedures (current); NACHA Operating Rules (current edition); Reg E §1005.11; Reg E provisional-credit applicability questions on real-time pull flows [verify]. Scenario: instant-payout product launches through the sponsor bank's FedNow participation, the program agreement does not name FedNow as an in-scope rail, fraud-hold parameters are set by the processor without fintech sign-off, customer-dispute flow defaults to the Reg E ACH path even where the underlying transfer is real-time and the rail's irrevocability posture differs. Skill output: program-agreement amendment gap (FedNow not named), fraud-hold parameter ownership gap, Reg E error-resolution gap on dispute routing, and a controls map for the new rail.

Both scenarios use only public sources. No named institutions are used as fact-specific examples; public CFPB and prudential-agency consent orders against fintech-adjacent program operators are the conceptual reference.

## Common pitfalls

- Drafting the artifact as a vendor questionnaire response rather than a self-evidence pack. Sponsor-bank TPRM teams want artifacts and owners, not narrative.
- Treating Reg E error-resolution as the bank's problem because the depository is the bank. The program agreement nearly always pushes operational ownership of error intake and triage to the fintech, which means the fintech has to evidence the §1005.11 timing.
- Asserting categorical money-transmitter status without checking the FinCEN administrative-ruling fact patterns and the state-by-state MTMA adoption. The right answer is configuration-specific.
- Using the same controls map for ACH and for FedNow / RTP. Real-time rails change the irrevocability posture, the dispute pathway, and the fraud-hold mechanics.
- Treating NACHA return-rate thresholds as static. They are revised; the firm's licensed copy is the source of truth and the artifact should say so.
- Conflating fintech-side controls with sponsor-bank-side controls. The bank's principal-side oversight obligations sit in `banking/bank-fintech-partnership-review`. Mixing the two muddies the audience and the audit trail.
- Skipping the FBO subledger / deposit-insurance representation review. Post-2024, this is the highest-frequency examiner finding in this lane.
- Citing the July 2023 RFI on bank-fintech arrangements as the binding statement when the operative document is the July 2024 joint statement [verify which artifacts are operative as of the date of analysis].
