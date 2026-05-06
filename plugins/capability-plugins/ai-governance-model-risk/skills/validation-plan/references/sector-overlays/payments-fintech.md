# Payments and fintech sector overlay for validation-plan

When the engagement-scope record names sector `payments-fintech`, this overlay adds payments- and fintech-specific scope items to the validation plan. Where there is conflict between the capability defaults and this overlay, the overlay governs the sector elements.

Loaded by: `validation-plan/SKILL.md` when `engagement_scope.sector_overlay_set` includes `payments-fintech`, or when the institution type implicates a money transmitter, payments processor, fintech program, sponsor-bank arrangement, prepaid issuer, BIN sponsor, or non-bank consumer-finance entity.

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for payments and fintech validation plans

### 1. Sponsor-bank model risk responsibility allocation

For sponsor-bank programs (a fintech offering deposit, lending, or card products through a sponsor-bank balance sheet), model risk responsibility is allocated by the bank-fintech contract and by the bank's own model risk policy. The plan carries:

- A statement of which legal entity owns the model (sponsor bank / fintech / shared) in plan metadata.
- A statement of which legal entity validates the model (typically the sponsor bank for any model that touches the bank's regulated activity).
- A statement of which regulator examines the model in practice (sponsor-bank's federal banking regulator typically, with CFPB reach for consumer products).
- The firm's posture on the OCC / FRB / FDIC interagency guidance on third-party relationships (June 2023) and the OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements (July 2024) [verify date].

Plan-writer flag: in a sponsor-bank arrangement, "the fintech built the model" is not a defence to bank-side validation expectations. The validation plan reads to the bank-side standard regardless of where the model was built.

### 2. Transaction-monitoring (TM) model validation under BSA/AML

For TM models in payments and money transmission, FinCEN expectations under the BSA, the FFIEC BSA/AML Examination Manual, and (for state-regulated money transmitters) state money-transmission examiners apply. The plan:

- Names the BSA officer or designee as a sign-off audience.
- Adds above-the-line / below-the-line testing in outcomes-analysis scope; this is the productivity test FFIEC examiners look for.
- Treats threshold tuning as a controls-scope validation item; threshold changes that materially shift alert volumes are change-management triggers and re-validation triggers in monitoring scope.
- Does not represent fraud-model performance metrics as AML-effectiveness evidence in outcomes-analysis; the two are doctrinally distinct.

For NY-licensed entities, NYDFS Part 504 senior-officer certification posture for TM models is a plan effective-challenge question.

### 3. Faster-payments-rail validation specifics

For models operating on FedNow, RTP, or Same Day ACH inbound, the irrevocability-driven typology shift changes the validation surface. The plan:

- Adds rail-by-rail outcomes-analysis cuts where the firm operates on multiple rails.
- Adds request-for-return-of-funds latency as a monitoring metric for FedNow / RTP fraud holds.
- Includes ISO 20022 message-field anomaly tests (suspicious creditor account, suspicious end-to-end ID) in outcomes-analysis scope where applicable.

### 4. Account-takeover (ATO) and fraud-model validation

For ATO detection, fraud-decline models, and step-up authentication models, the plan adds:

- Authentication-flow integration check in conceptual-soundness scope (which step, which decision boundary, which fallback path).
- False-positive vs false-negative trade-off explicitly in outcomes-analysis scope, with named owners for each side of the trade-off (fraud team vs customer-experience team).
- Reg E reach for unauthorised consumer transactions; the plan flags consumer-recourse for false declines as a controls-scope item.
- For card-program models, network rules (Visa, Mastercard, AmEx) apply; chargeback-rate program escalation (Visa fraud-monitoring program tiers, Mastercard equivalents) is a monitoring entry with re-validation trigger.

### 5. Onboarding-decisioning models and KYC/CIP

For models that influence onboarding (account-opening risk, KYC document review, identity-verification scoring), the plan carries:

- CIP and KYC integration check in conceptual-soundness scope; the model triages but does not substitute for the CIP rule (31 CFR 1020.220 for banks; 31 CFR 1010.230 for beneficial-ownership where applicable).
- Identity-verification vendor evidence enumerated in dependencies (vendor-supplied evaluation, plus firm-side validation).
- ECOA reach for onboarding implicating credit (e.g., card programs); UDAAP reach for deposit-only programs.

### 6. CFPB UDAAP and Reg E reach

For consumer-facing payments and fintech models, CFPB has authority under Dodd-Frank Title X for UDAAP and over Reg E (electronic fund transfers) and Reg DD (truth in savings) for deposit programs. The plan:

- Includes consumer-impact framing in any decision that affects a consumer transaction.
- Scopes Reg E error-resolution timing (10 / 45 / 90-day windows) where the model influences a consumer dispute.
- Adds complaint-rate drift to monitoring scope (CFPB complaint database plus internal feed; sponsor-bank-routed feed where applicable).
- Adds the larger-participant rule for digital wallets and payment apps (CFPB final rule, December 2024) [verify Federal Register citation, effective date, and current state including any litigation or congressional review] applicability check in plan metadata.

### 7. State money-transmission examination reach

For state-licensed money transmitters, state examiners (in many states the financial regulator) apply state-specific exam standards; multi-state CSBS-coordinated exams may apply. The plan flags state-licensure footprint and the strictest-applicable-state posture. NMLS posture and Money Transmitter Modernization Act adoption status [verify state-by-state] enter plan metadata.

### 8. NACHA Operating Rules — Third-Party Sender risk-management

For ODFIs, the plan's monitoring scope includes return-rate monitoring against current NACHA thresholds (administrative-return, overall-return, unauthorized-return) [verify current thresholds]. Where the firm acts as a Third-Party Sender on another ODFI's authority, registration status and Originator-agreement evidence are dependencies.

## Payments and fintech-specific output template additions

- `plan_metadata.legal_entity_type` — money transmitter / payments processor / sponsor-bank program / prepaid issuer / BIN sponsor / non-bank consumer-finance / fintech app.
- `plan_metadata.sponsor_bank_arrangement` — boolean; if true, sponsor-bank-side validator and federal banking regulator named.
- `plan_metadata.state_licensure_footprint` — list of states with money-transmission or other licences.
- `plan_metadata.network_rules_inscope` — boolean; if true, named networks (Visa, Mastercard, AmEx, ACH, FedNow, RTP) recorded.
- `plan_metadata.larger_participant_inscope` — boolean; CFPB digital-wallet larger-participant rule applicability.
- `data_review.scope_items[]` — CIP / KYC integration check for onboarding-decisioning models.
- `outcomes_analysis[]` — above-the-line / below-the-line testing for AML TM models; rail-by-rail outcomes for faster-payments models; chargeback-rate-program-tier monitoring for card-program models.
- `monitoring[]` — Reg E error-resolution-timing breach as re-validation trigger; complaint-rate drift; NACHA return-rate against current thresholds.
- `effective_challenge_questions[]` — payments-specific (sponsor-bank validator, BSA officer sign-off, NYDFS Part 504 certification, state money-transmission examiner posture, network-rule reach, larger-participant-rule applicability).

## Common pitfalls in payments and fintech validation plans

- Treating the fintech as the sole model owner when the sponsor bank inherits the model risk; bank examiners catch this in third-party reviews.
- Omitting BSA officer sign-off on a TM model; FFIEC manual expectation is clear.
- Reporting fraud-model performance as AML-effectiveness evidence in outcomes analysis; the two are doctrinally distinct.
- Missing Reg E error-resolution posture on a model that drives consumer transaction declines or holds.
- Treating state money-transmission exams as a footnote; state examiners regularly review TM models in money-transmission exams.
- Missing NYDFS Part 504 senior-officer certification posture for TM models in NY footprint.
- Asserting that vendor identity-verification scores are sufficient evidence of CIP compliance; CIP is the firm's regulatory obligation, not the vendor's.
- Treating faster-payments rails as ACH-with-shorter-windows; the irrevocability shift changes the typology surface and the validation tests should reflect that.
