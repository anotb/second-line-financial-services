# Insurance sector overlay for ai-act-triage

When the scope record names sector `insurance`, this overlay adds insurance-specific scoping, named-bulletin reach, and parallel-regime reconciliation to the EU AI Act triage.

This overlay carries the substance of the deprecated `insurance-ai-act-triage` skill. A US carrier with EU operations or EU policyholders, an EU carrier in EU-only operations, and a reinsurer with EU cedents all use this overlay alongside the capability triage. Where there is conflict between the capability defaults and this overlay, the overlay governs the insurance-specific elements.

Loaded by: `ai-act-triage/SKILL.md` when `scope.sector_overlay_set` includes `insurance`, or when the institution type implicates an insurance entity (life, health, P&C, reinsurance, captive). Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for an insurance triage

### 1. Annex III(5)(c) is the spine for life and health

Annex III(5)(c) names "AI systems intended to be used for risk assessment and pricing in relation to natural persons in the case of life and health insurance" as a high-risk use case. This is the most direct route to high-risk classification for insurance work. The triage walks Annex III(5)(c) explicitly and records the row whether the answer is "applies" or "does not apply"; for example, a P&C pricing model is not in (5)(c), and the triage says so on the record.

Boundary cases the triage flags:

- Group health pricing: in scope of (5)(c) when the rating element falls on natural persons (group rating with individual experience-rating components).
- Reinsurance: typically not in scope of (5)(c) directly, because the cedent is a legal entity rather than a natural person; flag whether the reinsurance-pricing model uses individual-policy-level inputs that effectively price natural persons.
- Disability and long-term care: read as in scope of (5)(c) where the product is structured as health or life-equivalent.
- Annuity pricing: read on the facts; longevity-based annuity pricing falls in life; investment-only structures may not.

Article 6(3) derogation analysis is non-trivial for insurance pricing: the model is rarely a "narrow procedural task" or a "preparatory" output, because the price is the product. The triage records the derogation analysis explicitly and typically does not invoke it for pricing or risk-assessment use cases; flag the analysis to legal where invoked.

### 2. Claims AI is not automatically Annex III, but watch the boundary

Claims AI (FNOL triage, severity prediction, fraud-indicator scoring, claims-handling chatbots) is not directly named in Annex III. The triage records the walk and the conclusion. Boundary conditions to watch:

- Where a claims model determines or materially influences benefit payment (life or health benefits), an analysis under (5)(c) may apply by extension; flag to legal.
- Where the model influences fraud determinations that affect access to health benefits, GDPR Article 22 (automated decision-making affecting the data subject) reaches in addition to AI Act considerations.
- Where the claims chatbot generates output to natural persons, Article 50 transparency obligations apply (50(1) interaction-with-AI disclosure; 50(2) synthetic-content marking on outbound text).

### 3. NAIC Bulletin (December 2023) is the parallel US-side regime; the triage cross-walks

Even when the EU AI Act applies, the carrier's US-side AIS Program documentation under the NAIC Bulletin runs in parallel. The triage records the cross-walk so the firm does not duplicate work or miss a parallel obligation. The Bulletin is itself a model bulletin; state-by-state adoption is tracked via the NAIC AI Working Group adoption tracker. Cite by jurisdiction; do not assert the Bulletin as binding without state adoption confirmation.

The AIS Program elements (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness) map roughly to the EU obligations under Articles 9, 10, 11, 13, 14, 15, and 26. The mapping is not one-for-one; the triage carries a side-by-side block in the artifact for an in-scope insurance use case so the reviewer sees both lenses.

### 4. State DOI bulletins extend the bar in named jurisdictions

The triage names the strictest applicable state in the operating footprint and the relevant bulletin. Named bulletins to enumerate when in scope:

- Colorado Division of Insurance regulation implementing SB 21-169 — governance and risk management of External Consumer Data and Information Sources (ECDIS) and predictive models in life-insurance underwriting. ECDIS provenance is a triage-record field when CO is in scope.
- New York DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024) — governance, fairness testing, disclosure, and consumer-recourse expectations.
- California DOI bulletin on AI use in insurance — broader scoping than CO/NY; informs disclosure posture.

Where any of these bulletins apply alongside the EU AI Act triage, the artifact records both. The triage does not collapse the US-side and EU-side analyses; reviewers downstream need both lenses visible.

### 5. Insurance-AI use-case categories the triage explicitly recognises

The triage labels the use-case category up front because each category lights up different obligations:

- Accelerated underwriting (life and health): Annex III(5)(c) applies; ECDIS provenance is a triage field if external data is in the input set; HIPAA touch-flag set if PHI; CO/NY DFS bulletins apply.
- Claims AI (triage, FNOL, severity prediction, fraud-indicator scoring, claims chatbots): Annex III not directly; Article 50 applies for chatbots; NAIC Model #880 fair-claims-settlement frame applies regardless of decision technology.
- Pricing and rating ML factors and ECDIS use: Annex III(5)(c) for life and health; state DOI rate-filing regimes apply where the model touches filed rates.
- Marketing AI for product targeting: not Annex III; Article 50 sub-obligations may apply if synthetic content is generated; NAIC Model #275 [verify model number] for annuity-suitability and best-interest reach.
- Agent-facing AI (illustration generation, suitability triage): not Annex III; producer-licensing reach if the AI takes actions that constitute producer activity; suitability and best-interest standards apply.
- Back-office AI (call-center summarisation, mailroom OCR): typically minimal-risk under the AI Act; firm-side governance still applies.

### 6. Fairness vs unfair-discrimination terminology

EU AI Act Article 10 frames data governance and bias examination using the EU vocabulary (representativeness, errors, biases reasonably foreseeable). State DOI rate analysts and NAIC Bulletin reviewers use the unfair-discrimination test under Model #880 (actuarial justification, permitted versus prohibited rating factors). The triage uses both vocabularies when applicable and records a translation note. Sign-off questions probe whether the test framing matches the regulator's framing for each jurisdiction in the operating footprint.

### 7. HIPAA scope check

Any insurance AI touching PHI (health-claims AI, life-and-health underwriting using prescription-history or medical data) requires a HIPAA Privacy and Security Rule cross-check that the EU AI Act triage alone will not produce. The triage flags HIPAA touch and routes to the privacy team; for vendor-supplied AI handling PHI, BAA posture is a vendor-diligence item.

### 8. Producer licensing on consumer-facing AI

A consumer-facing AI that takes binding-equivalent actions (binding, quoting commitments, surrendering, paying claims) can trigger producer-licensing questions in US states; flag for the licensing function. Article 50 transparency applies in the EU for the AI-interaction surface; the licensing question is a separate, US-side workstream.

### 9. ORSA materiality

For an enterprise-material AI use case (often the case for accelerated underwriting at scale), NAIC ORSA (Model #505) inclusion is required on the US side. The triage flags ORSA inclusion; the EU-side equivalent for Solvency II governance is the ORSA-equivalent under EIOPA and the Central Bank of Ireland (or other EU NSAs); the artifact carries both flags.

### 10. Vendor-AI accountability

Both regimes hold the carrier accountable for vendor-supplied AI. Under the AI Act, the carrier is the deployer when the vendor is the provider; deployer obligations under Article 26 attach. Under the NAIC Bulletin, third-party AI accountability is one of the AIS Program elements. The triage names the vendor and the firm-side governance regardless of which regime is the lens.

## Insurance-specific output template additions

The triage artifact adds the following blocks when this overlay loads:

- A use-case category line at the top (accelerated underwriting / claims AI / pricing / marketing AI / agent-facing AI / back-office).
- AIS Program element-by-element status (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness), each tied to evidence.
- Per-state DOI bulletin status (CO, NY DFS, CA at minimum if in operating footprint; strictest applicable state flagged).
- ECDIS provenance for any external-consumer-data input.
- HIPAA touch flag and BAA pointer for any vendor handling PHI.
- Producer-licensing posture for consumer-facing AI taking binding-equivalent actions.
- ORSA inclusion flag (US side) and Solvency II-ORSA equivalent flag (EU side) where the use case is enterprise-material.
- AI Act <-> NAIC Bulletin cross-walk table for the in-scope obligations.
- AI Act <-> Solvency II governance reconciliation note where the EU subsidiary is in scope.

## Common pitfalls in insurance triages

- Skipping the Annex III(5)(c) walk for a P&C pricing model on the assumption that pricing AI is automatically high-risk; (5)(c) is life and health, not all insurance pricing.
- Treating claims AI as automatically high-risk because it is consumer-facing; the Annex III walk often returns "no row applies" for claims AI, with Article 50 being the operative obligation for chatbot surfaces.
- Treating the NAIC Bulletin as binding when state adoption has not occurred; cite by jurisdiction.
- Carrying generic fairness vocabulary into a state DOI rate-filing context; rate analysts use unfair-discrimination vocabulary under Model #880.
- Conflating the EU-side Article 27 FRIA with the GDPR DPIA; both may be required and they capture different elements.
- Missing ECDIS provenance for a life-underwriting model when CO or NY is in operating footprint.
- Treating EU AI Act high-risk as a US-side obligation by extension; the NAIC Bulletin is the US-side parallel and the obligations attach independently.
- Missing the vendor-AI accountability lens on both sides; the carrier remains accountable regardless of which regime the reviewer is reading.
