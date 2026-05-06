# Conduct cross-cutting overlay for rag-evaluation-review

When the engagement-scope record flags `conduct` for a RAG evaluation review, this overlay adds the fairness-of-retrieval framing and the customer-facing accuracy framing. The conduct overlay loads where the use case has a population dimension (customer segment, geography, line of business) or where outputs flow into customer-facing communications.

Loaded by: `rag-evaluation-review/SKILL.md` when `engagement_scope.cross_cutting_set` includes `conduct`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- CFPB UDAAP framework (Dodd-Frank Act §1031 / §1036; CFPB Consumer Financial Protection Circulars on UDAAP) for consumer-facing communications generated or assisted by AI.
- Fair-lending framework: ECOA (15 USC §1691) and Regulation B (12 CFR Part 1002), Fair Housing Act (42 USC §3601 et seq.), and CFPB Circulars on AI in credit decisioning where the use case touches credit decisions or credit-adjacent decisions.
- SEC Marketing Rule (17 CFR §275.206(4)-1) and SEC fiduciary-standard / Reg BI framings for adviser-facing or broker-facing client-facing content.
- State unfair claims-settlement-practices acts and state insurance-fairness frameworks (e.g., Colorado Reg 10-1-1, Connecticut Insurance Department guidance) for retrieval-driven decision-support use cases in insurance.
- FINRA suitability framework for any sales-practice-adjacent use case in BD entities.
- General consumer protection: state UDAP regimes per residency.

## What changes when conduct is flagged

### Retrieval-quality and grounding evaluation gain a fairness segmentation

Where the use case has a population dimension, the segmentation requirement on retrieval-quality and grounding-evaluation metrics extends to fairness segmentation:

- Customer segment (mass-market, mass-affluent, private-banking; consumer, small-business, commercial; etc.) where the segmentation is relevant to the use case.
- Geography (state, urban/rural, where regional content access or regional product availability matters).
- Line of business (auto, life, disability, P&C in insurance; retail, commercial, treasury in banking).
- Protected-class proxies for fair-lending-adjacent use cases, with the proxy basis documented and the analysis approach aligned to the firm's fair-lending programme methodology.

A single global metric number on a customer-facing or decision-support use case is incomplete without the fairness segmentation.

### Customer-facing accuracy as a load-bearing failure-mode framing

The conduct framing for grounding-evaluation failure modes:

- Hallucination on a customer-facing communication is a UDAAP issue (deception by inaccurate statement) and a complaint-driver.
- Stale-content answer on a fee, rate, term, or product feature is a UDAAP issue (the customer is told something inconsistent with the current fact).
- Citation precision matters for any output where the customer might rely on the cited document; a wrong citation in a customer-facing communication is a UDAAP framing as well as a citation-quality framing.
- Refusal failure on out-of-scope (e.g., the assistant gives investment advice when the use case is operational support) creates suitability and Reg BI exposure for BD-affiliated use cases.

The grounding-evaluation thresholds for customer-facing or decision-support use cases are tighter than for analyst-facing or back-office use cases. The conduct overlay surfaces this in the recommended-actions section.

### Mitigations expand to include the conduct control set

Beyond the standard set:

- UDAAP-relevant output controls on customer-facing communications (deception, unfairness, abuse).
- Marketing Rule output controls for adviser-facing entities; books-and-records preservation per Rule 17a-4 / 204-2.
- Fair-lending output controls for credit-adjacent or credit-decisioning use cases; the fair-lending function signs off on the control specification.
- Suitability and Reg BI output controls for sales-practice-adjacent BD use cases.
- For insurance decision-support, state insurance-fairness output controls aligned to the AIS Program testing-and-validation expectations.

### Monitoring adds the conduct-tagged signal set

The baseline conduct signals to add when the overlay is flagged:

- Customer-complaint-rate and complaint-code drift as a downstream-acceptance signal; complaint codes mapping to RAG-output issues route to consumer compliance and to the AI risk committee.
- Fairness-segmented metric monitoring at a defined cadence (continuous for high-volume use cases, monthly or quarterly for low-volume), with drift alerting per segment.
- For decision-support use cases, disposition-rate fairness monitoring across protected-class proxies with annual reassessment at minimum.
- For insurance decision-support, alignment to the NAIC AIS Program monitoring elements per the loaded sector overlay.

### Reviewer-coordination considerations

- Consumer compliance is a named co-reviewer for any customer-facing use case.
- The fair-lending function is a named co-reviewer for any credit-adjacent or credit-decisioning use case.
- The CCO is a named co-acceptor for residual risk on UDAAP, Marketing Rule, and Reg BI framings.
- The chief actuary or the head of underwriting is a named co-reviewer for insurance decision-support use cases per the sector overlay.

## Recommended actions add the conduct-specific items

The standard conduct-tagged recommended-actions items the overlay surfaces:

- Confirm fairness-segmented evaluation is in place at the appropriate cadence.
- Confirm UDAAP-relevant output controls are documented and exercised for customer-facing communications.
- Confirm complaint-code mapping is in place to route RAG-output-related complaints to the AI risk committee.
- For credit-adjacent use cases, confirm the fair-lending function signs off on the residual-risk acceptance.
- For insurance decision-support, confirm the NAIC AIS Program documentation is current.

## Conduct-specific output additions

In the structured object (`schemas/rag-evaluation-review.schema.json`):

- `retrieval_quality[]` and `grounding_evaluation[]` entries with `segmentation` populated to include the fairness segmentation where the use case has a population dimension.
- `mitigations[]` entries with conduct-tagged owner (consumer compliance, fair-lending function, CCO).
- `monitoring[]` entries with conduct-tagged escalation path.
- `cross_cutting_overlay_notes.conduct` carries the conduct-specific fields: fairness-segmentation scope, UDAAP-relevant output-control scope, complaint-code routing, named co-reviewers per use-case framing.
- `recommended_actions[]` entries with conduct-tagged owner role.

## Common pitfalls in conduct-flagged RAG reviews

- Reporting a single faithfulness number on a customer-facing use case without the population dimension. A pass on the global number can hide systematic failure on a customer segment; the fairness segmentation surfaces it.
- Treating UDAAP framing as compliance background reading rather than as a load-bearing seam on the evaluation. UDAAP exposure is the load-bearing risk on customer-facing AI output; the residual-risk section carries it explicitly.
- Omitting the fair-lending function from the reviewer attestation when the use case touches credit decisions. Fair-lending sign-off is a co-acceptance, not a referral.
- Treating customer-complaint signals as customer-service operational data rather than as AI-quality leading indicators. Complaint-code mapping to RAG-output issues is the routing question.
- For insurance decision-support, asserting AIS Program documentation is current when the corpus or the metric set has changed. The NAIC AIS Program testing-and-validation element is current point-in-time and changes invalidate it.
- Setting grounding-evaluation thresholds at back-office levels for customer-facing use cases. Customer-facing thresholds are tighter; the recommended-action item names the threshold change.
