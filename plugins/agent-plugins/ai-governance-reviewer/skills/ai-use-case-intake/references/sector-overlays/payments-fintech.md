# Payments-fintech sector overlay for ai-use-case-intake

When the scope record names sector `payments-fintech`, this overlay tells the intake what additional fields to capture, which named regulators belong on the regulatory-flags table, and which sponsor-bank and money-transmitter facts are load-bearing. Payments-fintech intakes break differently from bank intakes: the program operator may not be the supervised entity, but the AI runs in the program operator's stack, and both the operator and the sponsor bank carry the consequences.

Loaded by: `ai-use-case-intake/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`, or when the institution type is a fintech program operator, BaaS platform, money transmitter, MSB, processor, BIN sponsor, or sponsor bank reviewing a fintech-supplied AI use case.

## Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

## What changes for payments-fintech intake

### 1. Sponsor-bank arrangement is the dominant intake pattern

Most fintech AI use cases run inside a sponsor-bank program. The intake captures both sides:

- `vendor_dependencies`: sponsor bank named with role `sponsor_bank` and criticality `critical`. Where a BIN sponsor is separate, named separately.
- `regulatory_flags`: `OCC_2023_17_third_party` and `July_2024_bank_fintech` with routing to `ai-risk-tiering` and `vendor-diligence`. The basis names which side the firm is on (program operator or sponsor bank).
- An open question for `vendor-diligence`: the program operator's evidence flow up to the sponsor bank, and the sponsor bank's downstream visibility into the operator's AI.
- The intake records the rail-by-rail role (ACH, Same Day ACH, wire, FedNow, RTP, card debit / credit, check, cross-border) the AI use case touches; different rails have different irrevocability and customer-protection clocks.

### 2. Money transmitter and MSB framing

Where the program operator is itself a money transmitter or registered MSB, FinCEN MSB rules (31 CFR Part 1022) and state MTL regimes apply:

- `regulatory_flags`: `FinCEN_MSB` and state-by-state MTL flags as applicable, with routing to `ai-risk-tiering` and `validation-plan`.
- The intake captures NMLS posture state-by-state (which states the firm is licensed in for money transmission) and Money Transmitter Modernization Act adoption status [verify state-by-state adoption status as of date of analysis].
- An open question for downstream work: where the use case touches BSA/AML, CIP, SAR-filing, or sanctions screening, the intake routes to `aml-model-monitoring` (in financial-crime-governance) and to `sanctions-screening-qa`.

### 3. Reg E reach on consumer-facing payment errors

Where the use case touches consumer-payment error resolution (intake of error claims, dispute routing, denial generation) under Reg E (12 CFR Part 1005), the intake captures:

- `regulatory_flags`: `Reg_E` with the §1005.11 timing posture (10 / 45 / 90-day clocks) named in the basis. Routing to `validation-plan` and `udaap-risk-review` (in consumer-compliance-fair-lending).
- An open question: the program-agreement allocation of error-resolution operational ownership between sponsor bank and program operator.

### 4. NACHA Operating Rules where the firm acts as ODFI, RDFI, or Third-Party Sender

For ACH-related AI use cases, NACHA Operating Rules (current edition) apply [verify current rule citations]:

- `regulatory_flags`: `NACHA_Operating_Rules` with routing to `validation-plan`. The basis names the role (ODFI, RDFI, Third-Party Sender) and the relevant return-rate threshold (administrative-return, overall-return, unauthorized-return) [verify current thresholds].
- An open question for `validation-plan`: how is the use case's contribution to the firm's return-rate posture monitored against current NACHA thresholds.

### 5. Card-network rules

Where the use case touches card debit or credit rails:

- `vendor_dependencies`: BIN sponsor named with role and criticality.
- `regulatory_flags`: card-network rules referenced as "Visa Core Rules and Visa Product and Service Rules; Mastercard Rules — current edition; specific sections to be confirmed against the firm's licensed copy" because the rulebooks are not public.
- An open question for `vendor-diligence`: the BIN sponsor's chargeback-rights posture and fraud-rate program escalation handling for the use case.

### 6. Faster-payments and irrevocability

For FedNow, RTP, and Same Day ACH use cases:

- The intake captures the irrevocability posture (real-time settlement finality on FedNow / RTP means the fraud playbook is request-for-return-of-funds plus monitoring escalation, not chargeback).
- An open question for downstream work: the fraud-typology library covers faster-payments-specific patterns (mule patterns on instant-funded accounts, ISO 20022 message-field anomalies, irrevocability-driven typology shift).

### 7. CFPB direct supervision under §1024 larger-participant rule

The digital wallets and payment apps larger-participant rule (December 2024) [verify Federal Register citation, effective date, and current state including any litigation or congressional review] designates a covered cohort of non-bank firms for direct CFPB supervision:

- An applicability check belongs in the intake: is the firm in scope for the larger-participant rule.
- Where in scope, `regulatory_flags`: `CFPB_larger_participant` with routing to `ai-risk-tiering` and `udaap-risk-review`.

### 8. UDAAP themes specific to fintech

CFPB Supervisory Highlights and consent orders (2023-26) have signalled on fintech UDAAP themes [verify which actions are current as of date of analysis]:

- Account closures and account holds without adequate notice or recourse.
- Reg E error-resolution timing failures presented as UDAAP rather than as Reg E findings.
- Fee disclosure failures (junk-fee themes, surprise-fee patterns).
- Marketing-claim review for FDIC-insurance representation (post-Synapse-era).
- BNPL UDAAP themes.
- Dark-pattern risk in onboarding and product-selection flows.

For any AI use case that touches these themes, intake captures the regulatory flag and routes to `udaap-risk-review`.

## Payments-fintech-specific intake fields

In addition to the capability intake spine, the following payments-fintech-specific facts belong on the record when relevant:

- Sponsor-bank counterparty (or "no sponsor bank" if direct-licensed money transmitter).
- Rail-by-rail role for the use case (ACH / Same Day ACH / wire / FedNow / RTP / card debit / card credit / check / cross-border).
- NMLS state-by-state licensure posture if direct-licensed money transmitter.
- BIN sponsor counterparty if card rails are in scope.
- Larger-participant rule applicability.
- BSA/AML role (bank-side, fintech-side, or split via program agreement).

## Common pitfalls in payments-fintech intake

- Recording a fintech AI use case without the sponsor-bank dependency. The program operator may not be the supervised entity, but the bank-side risk is the bank's regardless.
- Treating "vendor concentration" as a single number; sponsor-bank, BIN-sponsor, and processor are three distinct concentration axes that fail differently.
- Missing the rail-specific Reg E §1005.11 clock on consumer-facing error-resolution AI; the clock does not stop because the AI is making the call.
- Missing the Money Transmitter Modernization Act state adoption check on a multi-state money-transmitter use case.
- Missing the larger-participant rule applicability on a digital-wallet or payment-app use case at scale; the rule changes the supervisory posture from indirect-via-sponsor to direct-CFPB.
- Treating FDIC-insurance representation framing as marketing detail rather than as a UDAAP and FDIC misrepresentation rule (12 CFR Part 328 Subpart B, May 2022) [verify exact citation] flag.
