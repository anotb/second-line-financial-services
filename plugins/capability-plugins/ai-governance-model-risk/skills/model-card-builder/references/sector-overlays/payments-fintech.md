# Payments and fintech sector overlay for model-card-builder

When the scope record names sector `payments-fintech`, this overlay adds payments- and fintech-specific fields and review demands to the card. Where there is conflict between the capability defaults and this overlay, the overlay governs the sector elements.

Loaded by: `model-card-builder/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`, or when the institution type implicates a money transmitter, payments processor, fintech program, sponsor-bank arrangement, prepaid issuer, BIN sponsor, or non-bank consumer-finance entity.

Cited and section-referenced anchors in `references/source-anchors.md`.

## What changes for payments and fintech model cards

### 1. Sponsor-bank model risk responsibility allocation

For sponsor-bank programs (a fintech offering deposit, lending, or card products through a sponsor-bank balance sheet), the model risk responsibility is allocated by the bank-fintech contract and by the bank's own model risk policy. The card carries:

- A statement of which legal entity owns the model (sponsor bank / fintech / shared).
- A statement of which legal entity validates the model and signs the card (typically the sponsor bank for any model that touches the bank's regulated activity).
- A statement of which regulator examines the model in practice (sponsor-bank's federal banking regulator typically, with CFPB reach for consumer products).
- The firm's posture on the FDIC and OCC sponsor-bank oversight expectations (joint OCC/FRB/FDIC interagency guidance on third-party relationships, June 2023).

Card-writer flag: in a sponsor-bank arrangement, "the fintech built the model" is not a defence to bank-side documentation expectations.

### 2. Transaction-monitoring (TM) model risk overlap with BSA/AML

For TM models in payments and money-transmission, FinCEN expectations under the BSA, the FFIEC BSA/AML Examination Manual, and (for state-regulated money transmitters) state money-transmission examiners apply. The card carries:

- BSA officer or designee as a signoff reviewer.
- Threshold-tuning posture as a controls-section item; threshold changes that materially shift alert volumes are change-management triggers.
- The model's role in the SAR workflow without claiming the model files SARs (the firm files SARs; the model triages or scores).
- Above-the-line / below-the-line testing cadence and ownership.

### 3. Account-takeover (ATO) detection and fraud models

For ATO detection, fraud-decline models, and step-up authentication models, the card adds:

- The model's authentication-flow integration (which step, which decision boundary, which fallback path).
- The fraud-team and customer-experience trade-off statement (false-positive rate vs false-negative rate, with named owners for each).
- Reg E reach for unauthorised consumer transactions; the card flags the consumer-recourse channel for false declines.
- For card-program models, network rules (Visa, Mastercard, AmEx) apply in addition to regulatory expectations; the card flags network rule reach where applicable.

### 4. Onboarding-decisioning models and KYC/CIP

For models that influence onboarding (account-opening risk, KYC document review, identity-verification scoring), the card carries:

- CIP and KYC integration statement; the model triages but does not substitute for the CIP rule (31 CFR 1020.220 for banks; 31 CFR 1010.230 for beneficial-ownership where applicable).
- Adverse decisioning posture for ECOA reach where the onboarding implicates credit (e.g., card programs); for deposit-only programs, ECOA may not reach but consumer-protection (UDAAP) does.
- Identity-verification vendor evidence (vendor-supplied evaluation, plus firm-side validation).

### 5. CFPB UDAAP and Reg E reach

For consumer-facing payments and fintech models, the CFPB has authority under Dodd-Frank Title X for UDAAP and over consumer-protection rules including Reg E (electronic fund transfers) and Reg DD (truth in savings) for deposit programs. The card carries:

- Consumer-impact framing for any decision that affects a consumer transaction.
- Reg E error-resolution posture where the model influences a consumer dispute.
- Complaint-rate drift monitoring (CFPB complaint database plus internal feed).

### 6. State money-transmission examination reach

For state-licensed money transmitters, state examiners (in many states, the financial regulator) apply state-specific exam standards; multi-state Conference of State Bank Supervisors (CSBS) NMLS-coordinated exams may apply. The card flags state-licensure footprint and the strictest-applicable-state posture.

### 7. NYDFS Part 504 (transaction monitoring) and Part 500 (cyber)

For NY-licensed fintechs and DFS-regulated money transmitters, Part 504 imposes specific TM-program expectations including the senior-officer certification; the card flags NY footprint and the certification posture for TM models. NYDFS Part 500 cyber expectations apply across the operation.

## Payments and fintech-specific output template additions

- `card_metadata.legal_entity_type` — money transmitter / payments processor / sponsor-bank program / prepaid issuer / BIN sponsor / non-bank consumer-finance / fintech app.
- `card_metadata.sponsor_bank_arrangement` — boolean; if true, sponsor-bank-side validator and federal banking regulator named.
- `card_metadata.state_licensure_footprint` — list of states with money-transmission or other licences.
- `card_metadata.network_rules_inscope` — boolean; if true, named networks (Visa, Mastercard, AmEx, network ACH, RTP) recorded.
- `data[].cip_kyc_integration` — for onboarding-decisioning models.
- `controls[]` — Reg E error-resolution posture (consumer products); SAR-workflow integration (TM models); network-rule controls (card programs).
- `signoff_questions[]` — payments-specific (sponsor-bank validator, BSA officer signoff, NYDFS Part 504 certification, state money-transmission examiner posture, network-rule reach).

## Common pitfalls in payments and fintech model cards

- Treating the fintech as the sole model owner when the sponsor bank inherits the model risk; bank examiners catch this in third-party reviews.
- Omitting BSA officer signoff on a TM model; FFIEC manual expectation is clear.
- Reporting fraud-model performance as AML-effectiveness evidence; the two are doctrinally distinct.
- Missing Reg E error-resolution posture on a model that drives consumer transaction declines or holds.
- Treating state money-transmission exams as a footnote; state examiners regularly review TM models in money-transmission exams.
- Missing NYDFS Part 504 senior-officer certification posture for TM models in the NY footprint.
- Asserting that vendor identity-verification scores are sufficient evidence of CIP compliance; CIP is the firm's, not the vendor's, regulatory obligation.
