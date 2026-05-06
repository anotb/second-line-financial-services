# Insurance sector overlay for ai-use-case-intake

When the engagement-scope record names sector `insurance`, this overlay tells the intake what additional fields to capture, which named regulators belong on the regulatory-flags table, and which open questions tag to downstream insurance work. The carrier remains accountable for vendor and third-party AI used on its policies (NAIC Model Bulletin December 2023 third-party AI accountability); the intake captures the fields that accountability flows from.

Loaded by: `ai-use-case-intake/SKILL.md` when `engagement_scope.sector_overlay_set` includes `insurance`, or when the institution type is an insurer (carrier, reinsurer, MGA, MGU, captive) or insurance group.

## Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

## What changes for insurance intake

### 1. NAIC Bulletin on Use of AI Systems by Insurers (December 2023) — AIS Program spine

For insurers, the intake feeds the AIS Program (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness). Intake captures:

- `regulatory_flags`: `NAIC_Bulletin_AI_2023` with routing to `ai-risk-tiering`, `model-card-builder`, `validation-plan`. Note the state-by-state adoption status (the NAIC AI Working Group adoption tracker is the public reference for which states have adopted) in the basis line; the Bulletin is binding only where adopted.
- `decision_impact.customer_impact`: scored against the Bulletin's spine of "potential to harm consumers" — eligibility, premium, claims, coverage decisions read high; back-office reads lower.
- An open question for `model-card-builder`: which AIS Program elements need explicit coverage in the card.

### 2. Insurance use case categories the intake must explicitly recognise

Insurance AI clusters into categories with different regulatory weights. The intake purpose statement should name the category:

- Accelerated underwriting (life and health) — state DOI bulletin reach (CO SB 21-169, NY DFS Insurance Circular Letter January 2024, CA bulletin), HIPAA touch on health data, ECDIS provenance question.
- Claims AI (triage, FNOL, severity prediction, fraud-indicator scoring, claims-handling chatbots) — NAIC Model #880 fair-claims-settlement standards, state UCSPA reach, HIPAA touch on health-claims, UPL boundary on consumer-facing chatbots.
- Pricing / rating ML factors and ECDIS use — state DOI rate-filing reach, prohibited rating factor exposure, NAIC Model #880 unfair discrimination.
- Marketing AI for product targeting — TCPA reach where outbound communications, NAIC #275 [verify] suitability where annuities involved.
- Agent-facing AI (illustration generation, suitability triage) — producer-licensing question on consumer-facing actions, NAIC Suitability in Annuity Transactions Model Regulation [verify model number].
- Back-office AI (call-center summarisation, mailroom OCR, claims-letter drafting) — generally lower regulatory weight, but still in scope for the AIS Program if the insurer has adopted it.

### 3. State DOI bulletins on AI use

Each state-bulletin reach is a separate flag because each state has its own scoping (life-only in CO and NY DFS Circular; broader in NAIC Bulletin and CA bulletin) and consumer-recourse expectations:

- `regulatory_flags`: `CO_SB_21_169` (life-insurance underwriting using ECDIS or predictive models in CO), `NY_DFS_Circular_AI_2024` (life-insurance underwriting and pricing using AI and ECDIS in NY), CA bulletin where applicable. Routing to `ai-risk-tiering` and `model-card-builder`.
- The intake captures the operating footprint by state and lights up the bulletin flag where the use case is in the state's scope.

### 4. ECDIS data source provenance

Where the use case uses External Consumer Data and Information Sources (e.g., third-party clinical and prescription data, credit-related data outside FCRA, behavioural data), intake captures:

- `data_sources`: each ECDIS source named with provenance, lawful basis, and consumer-recourse channel.
- An open question for `model-card-builder` and `validation-plan`: ECDIS provenance evidence pack and bias-evaluation evidence framed against unfair discrimination (Model #880) terminology in addition to or in place of generic fairness terminology.

### 5. HIPAA touch on health data

Any insurance AI touching PHI (health-claims AI; life-and-health underwriting AI using prescription-history or medical data) requires a HIPAA cross-check:

- `data_sources`: PHI sources tagged `regulated_phi` with field-level tagging (medical history, prescription history, claims diagnoses) required.
- `regulatory_flags`: `HIPAA` with routing to `ai-risk-tiering` and `validation-plan`.
- Vendor BAA posture as a vendor-dependency note where any vendor handles PHI.

### 6. ORSA materiality

If the AI use case is enterprise-material under the carrier's ORSA materiality threshold, the use case belongs in the ORSA Summary Report under Model #505. Intake captures:

- An open question for `board-ai-risk-pack` (and a flag in the change plan): does the use case meet the firm's ORSA materiality threshold; if so, the use case feeds the ORSA Summary Report.

### 7. Producer licensing on consumer-facing actions

Any consumer-facing AI that takes actions on policies (binding, quoting commitments, surrendering, paying claims, agent-AI co-pilots that recommend) can trigger producer-licensing questions:

- An open question for the licensing function: does the use case cross into producer activity without licensing.
- Where the use case is consumer-facing claims AI, an additional UPL boundary check (does the chatbot cross into legal advice or coverage opinions).

### 8. Vendor-AI accountability

NAIC Bulletin December 2023 holds the carrier accountable for vendor and third-party AI used on its policies. Intake captures:

- `vendor_dependencies`: each AI vendor named with role and criticality, with the AIS Program third-party-AI elements as routing notes for `vendor-diligence`.
- A regulatory flag for `NAIC_Bulletin_AI_2023` third-party AI accountability with routing to `vendor-diligence`.

## Insurance-specific intake fields

In addition to the capability intake spine, the following insurance-specific facts belong on the record when relevant:

- Operating footprint by state (which DOI bulletins are in scope).
- AIS Program element coverage status (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness).
- ORSA-materiality posture.
- TPA / claims-administrator role where the AI runs at a TPA on the carrier's policies (NAIC Insurance Data Security Model Law #668 §4.F third-party service-provider obligations apply; the TPA's controls are the carrier's controls for §4.F purposes).
- HIPAA touch and BAA posture.
- ECDIS provenance for any data input the AI uses.

## Common pitfalls in insurance intake

- Treating the NAIC Bulletin as US-uniform when it is state-by-state in adoption.
- Recording an underwriting-AI use case with "fairness" framing only; insurance regulators use unfair discrimination under Model #880, which has a different test (actuarial justification matters; permitted vs prohibited rating factors are state-defined).
- Missing the ECDIS provenance question on a use case using third-party data inputs; CO and NY DFS Circular both turn on ECDIS-specific governance.
- Treating a TPA's AI as out-of-scope because the TPA runs it; the carrier remains accountable under the NAIC Bulletin and the Model #668 third-party service-provider obligations.
- Skipping the HIPAA flag on a life-underwriting AI that uses prescription-history data; the data category triggers the rule regardless of whether the carrier considers itself in the health business.
- Recording a consumer-facing claims chatbot as low decision-impact on the basis of "the human reviews the denial letter." Where the bot crosses into legal advice or coverage opinions, the UPL question is open and the decision-impact reads higher than the human-review point suggests.
