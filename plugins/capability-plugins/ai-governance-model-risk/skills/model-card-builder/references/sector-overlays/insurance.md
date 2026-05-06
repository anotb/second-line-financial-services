# Insurance sector overlay for model-card-builder

When the engagement-scope record names sector `insurance`, this overlay adds insurance-specific fields and review demands to the card. Where there is conflict between the capability defaults and this overlay, the overlay governs the insurance-sector elements.

Source content in this overlay derives from the insurance lead's overlay snippets in the phase-1 spec sheets; mapped here into the model-card context. Cited and section-referenced anchors in `references/source-anchors.md`.

## What changes for insurance model cards

### 1. NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023) is the spine

The Bulletin sets out an AIS Program (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness). The model card is one of the documentation artifacts the AIS Program demands. The Bulletin is itself a model bulletin; state-by-state adoption is tracked by the NAIC AI Working Group adoption tracker. Card-writer flag: cite by jurisdiction, do not assert the Bulletin as binding without state adoption confirmation.

The card carries an AIS Program element-by-element status block (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness), each tied to evidence in the source trace. This is the insurance-specific addition that a state DOI rate analyst will recognise.

### 2. State DOI bulletins extend the bar in named jurisdictions

The card identifies the operating footprint and flags the strictest applicable state. Named bulletins to enumerate when in scope:

- Colorado Division of Insurance regulation implementing SB 21-169 — governance and risk management of External Consumer Data and Information Sources (ECDIS) and predictive models in life-insurance underwriting. ECDIS provenance is a card field when CO is in scope.
- New York DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024) — governance, fairness testing, disclosure, and consumer-recourse expectations.
- California DOI bulletin on AI use in insurance — broader than CO/NY in scope but informs disclosure posture.

### 3. Fairness vs unfair discrimination — vocabulary translation

Capability fairness vocabulary (disparate impact, AIR, demographic parity) and insurance unfair-discrimination vocabulary (NAIC Unfair Trade Practices Act Model #880) are not the same legal test. State insurance code allows actuarially justified rating differences that would be challenged under disparate-impact frameworks elsewhere; conversely, some state insurance code prohibitions reach uses of variables (e.g., credit-based insurance scores in some states) that disparate-impact analysis would not flag.

The card's fairness section uses both vocabularies when applicable, and includes a translation note. The sign-off question explicitly asks whether the test framing matches the regulator's test framing.

### 4. ECDIS-driven rating and underwriting

Where the model uses external consumer data and information sources (third-party data beyond traditional underwriting variables), the card carries:

- ECDIS provenance for each data source: provider, lineage, refresh, consumer-disclosure posture, consumer-recourse channel.
- Per-state ECDIS treatment: CO regulation imposes specific governance and disclosure on ECDIS use in life underwriting; other states may follow.
- HIPAA touch flag for any health-data ECDIS feed.

### 5. Insurance use-case categories

The card recognises which insurance-AI use case category applies; the controls and limitations sections differ across them:

- Accelerated underwriting (life, health): tier elevation; ECDIS likely; HIPAA likely; CO/NY DFS bulletins apply.
- Claims AI (FNOL triage, severity prediction, fraud-indicator scoring, claims chatbot): NAIC Model #880 unfair-claims-settlement standards apply regardless of decision technology; state UCSPA timing and notice obligations apply.
- Pricing / rating ML factors: state DOI rate filing and prior-approval regimes apply where the model touches filed rates; rate analyst is a card audience.
- Marketing AI (suitability, replacement risk for annuities): NAIC Model #275 [verify model number] for annuity suitability.
- Agent-AI co-pilots: producer-licensing reach; suitability and best-interest standards.
- Back-office AI (call-center summarisation, mailroom OCR): generally lower tier.

### 6. ORSA materiality and Holding Company filings

For an enterprise-material AI use case, NAIC ORSA (Model #505) inclusion is required; the card flags ORSA inclusion and cross-references the firm's ORSA Summary Report. Holding Company filings (Form B affiliated services, Form D affiliated transactions) under Model #440 / #450 [verify] apply where the AI is provided by an affiliate.

### 7. HIPAA scope check

Any insurance AI touching PHI (health-claims AI, life-and-health underwriting using prescription-history or medical data) requires a HIPAA Privacy and Security Rule cross-check; HIPAA business-associate-agreement posture is a card data-section field for any vendor handling PHI.

### 8. Producer licensing on consumer-facing AI

A consumer-facing AI that takes binding-equivalent actions (binding, quoting commitments, surrendering, paying claims) can trigger producer-licensing questions; flag for the licensing function. Card sign-off questions probe the boundary.

### 9. Vendor-AI accountability

NAIC Bulletin Dec 2023 holds the carrier accountable for vendor and third-party AI used on its policies. The card's data and controls sections name the vendor, the firm-side governance, and the firm-side monitoring; vendor self-attestations are recorded but do not substitute for firm-side evidence.

## Insurance-specific output template additions

- `card_metadata.ais_program_status` — element-by-element status block (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness).
- `card_metadata.state_doi_status` — per-state status (CO, NY, CA at minimum if in operating footprint).
- `card_metadata.orsa_inscope` — boolean.
- `card_metadata.hipaa_touch` — boolean; if true, BAA reference required for any PHI-handling vendor.
- `card_metadata.producer_licensing_posture` — for consumer-facing AI taking binding-equivalent actions.
- `data[].ecdis_provenance` — provider, lineage, refresh, consumer-disclosure posture, consumer-recourse channel.
- `fairness_results[].test_framing` — fairness / unfair-discrimination / both.
- `signoff_questions[]` — insurance-specific (AIS Program element status, state DOI strictest-applicable, ECDIS posture, ORSA fit, HIPAA touch, producer-licensing).

## Common pitfalls in insurance model cards

- Carrying generic fairness vocabulary into a rate-filing context; state DOI rate analysts use unfair-discrimination vocabulary.
- Treating the NAIC Bulletin as US-uniform; adoption is state-by-state and the Bulletin is itself non-binding until state adoption.
- Omitting ECDIS provenance for a life-underwriting model when CO or NY is in operating footprint.
- Missing HIPAA BAA reference for a vendor handling PHI.
- Treating claims AI as a pure technology question without the Model #880 fair-claims-settlement frame.
- Forgetting that the TPA's controls are the carrier's controls under NAIC Insurance Data Security Model Law (#668) §4.F when the model runs at a TPA.
- Treating the AIS Program elements as a checklist; the card is the evidence, the elements are the structure.
