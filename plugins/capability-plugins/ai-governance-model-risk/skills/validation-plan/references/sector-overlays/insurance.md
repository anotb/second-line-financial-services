# Insurance sector overlay for validation-plan

When the scope record names sector `insurance`, this overlay adds insurance-specific scope items to the validation plan. Where there is conflict between the capability defaults and this overlay, the overlay governs the insurance-sector elements.

Source content derives from the insurance lead's overlay snippets and is mapped here into the validation-plan context. Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for insurance validation plans

### 1. NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023) is the spine

The Bulletin sets out an AIS Program (governance, risk management, testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness). The validation plan operationalises the testing-and-validation elements for an individual AI use case in a carrier setting. The Bulletin is itself a model bulletin; state-by-state adoption is tracked by the NAIC AI Working Group adoption tracker. Plan-writer flag: cite by jurisdiction, do not assert the Bulletin as binding without state adoption confirmation.

The plan carries an AIS Program element-by-element validation-coverage block in conceptual-soundness scope (testing, validation, third-party AI accountability, monitoring, documentation), tying each element to an outcomes-analysis or monitoring entry.

### 2. State DOI bulletins extend the bar in named jurisdictions

The plan identifies the operating footprint and aligns to the strictest applicable state. Named bulletins to enumerate when in scope:

- Colorado Division of Insurance regulation implementing SB 21-169 — governance and risk management of External Consumer Data and Information Sources (ECDIS) and predictive models in life-insurance underwriting. ECDIS provenance becomes a data-review scope item when CO is in footprint; unfair-discrimination testing is added to fairness scope.
- New York DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024) — governance, fairness testing, disclosure, and consumer-recourse expectations. NY-footprint plans add disparate-impact-style monitoring on top of the actuarial-justification test.
- California DOI bulletin on AI use in insurance — broader than CO/NY in scope but informs disclosure posture.

### 3. Fairness vs unfair-discrimination — vocabulary translation

Capability fairness vocabulary (disparate impact, AIR, demographic parity) and insurance unfair-discrimination vocabulary (NAIC Unfair Trade Practices Act Model #880) are not the same legal test. State insurance code permits actuarially justified rating differences that would be challenged under disparate-impact frameworks elsewhere; conversely, some state insurance code prohibitions reach uses of variables (e.g., credit-based insurance scores in some states) that disparate-impact analysis would not flag.

The plan's fairness scope uses both vocabularies when applicable. The success criterion for a rate-filing model includes the actuarial-justification test under state insurance code in addition to (or instead of) generic disparity ratios. An effective challenge question explicitly asks whether the test framing matches the regulator's test framing.

### 4. ECDIS-driven rating and underwriting

Where the model uses external consumer data and information sources (third-party data beyond traditional underwriting variables), the plan's data-review scope adds:

- ECDIS provenance for each data source: provider, lineage, refresh, consumer-disclosure posture, consumer-recourse channel.
- Per-state ECDIS treatment: CO regulation imposes specific governance and disclosure on ECDIS use in life underwriting; NY DFS Circular Letter has its own disclosure expectations.
- HIPAA touch flag for any health-data ECDIS feed (cross-link to `references/cross-cutting/privacy.md`).

### 5. Insurance use-case categories

The plan recognises which insurance-AI use case category applies; the outcomes-analysis and robustness scope differ across them:

- Accelerated underwriting (life, health): ECDIS-related tests; CO/NY DFS bulletin alignment; HIPAA-touch privacy overlay.
- Claims AI (FNOL triage, severity prediction, fraud-indicator scoring, claims chatbot): NAIC Model #880 unfair-claims-settlement standards apply regardless of decision technology; state UCSPA timing and notice obligations apply. Validation includes faithfulness, denial-letter quality, supervisor-override path testing.
- Pricing / rating ML factors: state DOI rate filing and prior-approval regimes apply where the model touches filed rates; rate analyst is a plan-acceptance audience.
- Marketing AI (suitability, replacement risk for annuities): NAIC Model #275 [verify model number] for annuity suitability.
- Agent-AI co-pilots: producer-licensing reach; suitability and best-interest standards.
- Back-office AI (call-center summarisation, mailroom OCR): generally lower tier; lighter validation.

### 6. ORSA materiality

For an enterprise-material AI use case, NAIC ORSA (Model #505) inclusion is required; the plan flags `orsa_inscope = true` and cross-references the firm's ORSA Summary Report. The plan's effective-challenge questions include an ORSA-fit question for tier-1 use cases.

### 7. HIPAA scope check

Any insurance AI touching PHI (health-claims AI, life-and-health underwriting using prescription-history or medical data) requires a HIPAA Privacy and Security Rule cross-check; HIPAA business-associate-agreement posture is a data-review scope item for any vendor handling PHI. Cross-link to `references/cross-cutting/privacy.md`.

### 8. Producer licensing on consumer-facing AI

A consumer-facing AI that takes binding-equivalent actions (binding, quoting commitments, surrendering, paying claims) can trigger producer-licensing questions; flag for the licensing function. Plan effective-challenge questions probe the boundary.

### 9. Vendor-AI accountability

NAIC Bulletin Dec 2023 holds the carrier accountable for vendor and third-party AI used on its policies. The plan's conceptual-soundness scope names the vendor evidence in scope (system card, evaluation report, red-team summary, contract addenda) and the firm-side rationale memo; vendor self-attestations are recorded but do not substitute for firm-side validation.

## Insurance-specific output template additions

- `plan_metadata.ais_program_coverage` — element-by-element validation-coverage block (testing, validation, third-party AI accountability, monitoring, documentation, transparency, fairness).
- `plan_metadata.state_doi_status` — per-state status (CO, NY, CA at minimum if in operating footprint).
- `plan_metadata.orsa_inscope` — boolean.
- `plan_metadata.hipaa_touch` — boolean; if true, BAA reference required for any PHI-handling vendor in `data_review`.
- `plan_metadata.producer_licensing_posture` — for consumer-facing AI taking binding-equivalent actions.
- `data_review.scope_items[]` — ECDIS provenance for each data source (provider, lineage, refresh, consumer-disclosure posture, consumer-recourse channel).
- `fairness_explainability[].dimension` — unfair-discrimination dimension under state insurance code (#880 vocabulary) in addition to or in place of generic fairness vocabulary.
- `effective_challenge_questions[]` — insurance-specific (AIS Program element coverage, state DOI strictest-applicable, ECDIS posture, ORSA fit, HIPAA touch, producer-licensing, claims-AI Model #880 fair-claims-settlement test framing).

## Common pitfalls in insurance validation plans

- Carrying generic fairness vocabulary into a rate-filing context; state DOI rate analysts use unfair-discrimination vocabulary and the actuarial-justification test.
- Treating the NAIC Bulletin as US-uniform; adoption is state-by-state and the Bulletin is itself non-binding until state adoption.
- Omitting ECDIS provenance for a life-underwriting model when CO or NY is in operating footprint.
- Missing HIPAA BAA reference for a vendor handling PHI in the data-review scope.
- Treating claims AI as a pure technology question without the Model #880 fair-claims-settlement frame; validation of a claims chatbot includes denial-letter quality and supervisor-override path testing, not just faithfulness.
- Forgetting that the TPA's controls are the carrier's controls under NAIC Insurance Data Security Model Law (#668) §4.F when the model runs at a TPA; the plan scopes the TPA's monitoring as in scope for the carrier's validation.
- Treating the AIS Program elements as a checklist rather than as scope coverage; the plan ties each element to a named outcomes-analysis or monitoring entry.
