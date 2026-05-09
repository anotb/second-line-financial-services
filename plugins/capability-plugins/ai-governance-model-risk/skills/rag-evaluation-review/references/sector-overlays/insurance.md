# Insurance sector overlay for rag-evaluation-review

When the scope record names `insurance` as the sector, this overlay adds insurance-specific corpora considerations, mitigations, monitoring signals, and review-coordination expectations to the RAG evaluation review. Loaded by `rag-evaluation-review/SKILL.md` when `scope.sector_overlay_set` includes `insurance`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023), AIS Program elements including testing-and-validation, third-party AI accountability, and documentation; binding only to the extent state DOIs adopt it (the NAIC AI Working Group state-adoption tracker is the public reference).
- HIPAA Privacy and Security Rules (45 CFR Parts 160 and 164) where the corpus contains PHI. Minimum-necessary at the retrieval layer is the load-bearing privacy control.
- State Insurance Data Security Model Law (NAIC Model 668), as adopted by domiciliary states.
- State unfair claims-settlement-practices acts and state insurance-fairness frameworks (e.g., Colorado Reg 10-1-1 on AI-driven external consumer data in life insurance underwriting; Connecticut Insurance Department guidance) for retrieval-driven decision-support use cases.
- Where the insurer is a registered investment adviser, the SEC overlay applies; this overlay does not duplicate that framing.

## Corpora typical of insurance and the fitness considerations they raise

The recurring insurance RAG corpora and the fitness questions that bite:

- **Claim-file documents**: correspondence, medical records, prior summaries, adjuster notes, prior adjudication. Sensitivity is regulated-PHI for medical records; HIPAA minimum-necessary applies at retrieval. Per-claim scoping at the retriever is the load-bearing control. Provenance per document type is the corpus-fitness spine.

- **Policy documents (insurance policies)**: master policy wordings, endorsements, schedule pages, renewal letters. Sensitivity is confidential. Coverage gaps on legacy policy forms or jurisdiction-specific endorsements are common; coverage assessment by line of business and state is the right segmentation.

- **Underwriting content**: application data, third-party data feeds (motor vehicle records, prescription histories, credit-based insurance scoring inputs, ECDIS sources where applicable). Sensitivity ranges across confidential to regulated-PHI. State unfair-discrimination and state insurance-fairness frameworks apply where retrieval drives decision support; the conduct overlay carries the broader framing.

- **Medical records and clinical content**: clinical notes, lab reports, imaging reports, ICD-coded discharge summaries. Sensitivity is regulated-PHI; HIPAA minimum-necessary at retrieval is non-optional. OCR-driven retrieval is common on legacy medical records and the OCR confidence gate is load-bearing.

- **Loss-control and engineering reports (commercial lines)**: site inspection reports, loss-prevention recommendations, engineering surveys. Sensitivity is confidential. Provenance and retention-bound to the policy lifecycle.

- **Producer and broker correspondence**: emails, chat, meeting notes. Sensitivity is internal-to-confidential. Where the use case supports producer-facing assistants, conduct framing applies (producer training, suitability, sales-practice compliance).

## Mitigations the review should expect to see

Beyond the standard set:

- Per-claim or per-policy retrieval scoping enforced at the retriever (HIPAA minimum-necessary mapping).
- OCR confidence threshold for any document type ingested via OCR, with a defined re-OCR or human-review path for sub-threshold documents.
- PHI handling controls aligned to HIPAA Security Rule technical safeguards (encryption at rest and in transit, audit logging on retrieval, access controls).
- State insurance-fairness output filtering where the use case drives decision support; the conduct overlay carries the framing.
- NAIC AIS Program documentation linkage: the RAG evaluation review's grounding evaluation and monitoring sections feed the AIS Program testing-and-validation and monitoring elements.

## Monitoring signals the overlay adds

- Cross-claim or cross-policy leakage detection (rule-based detection on cross-scope ID surfaces in summary output); any confirmed event is a HIPAA-relevant incident and a privacy-overlay trigger.
- OCR confidence trend on PHI-containing documents; ingestion-pass-rate drift is a leading indicator of medical-record quality issues.
- Adjuster-edit rate or underwriter-edit rate as a downstream-acceptance signal; sustained increases indicate summary-quality drift.
- For decision-support use cases, fairness monitoring across protected-class proxies (segmentation of grounding-quality metrics by population), with annual reassessment at minimum.

## Review-coordination considerations

- The privacy officer is a named co-reviewer for any PHI-containing corpus.
- The chief actuary or the head of underwriting is a named co-reviewer for any decision-support use case where retrieval feeds rate-, premium-, or coverage-relevant outputs.
- The NAIC AIS Program coordinator (where the firm has formalised AIS Program governance) consumes the RAG evaluation review as input to the testing-and-validation and monitoring elements.
- For multi-state insurers, the review notes the domiciliary-state binding posture on the NAIC Model Bulletin and any state-specific AI guidance (e.g., Colorado, Connecticut, New York) that applies.

## Common pitfalls specific to insurance

- Asserting per-claim scoping at the prompt layer rather than the retriever layer for PHI corpora. The HIPAA minimum-necessary expectation is structural; prompt-layer scoping is bypassable.
- Treating OCR-driven retrieval miss as an OCR engineering issue rather than a corpus-fitness issue. The OCR confidence gate is part of the corpus-fitness control set; sub-threshold documents are corpus-incomplete documents.
- Reporting a single faithfulness number on a claims-summary use case spanning multiple lines of business (auto, life, disability, P&C). Segment-level reporting by line of business and claim type is required.
- Omitting the privacy officer from the reviewer attestation when the corpus contains PHI. The privacy officer co-signs the residual-risk acceptance.
- Not refreshing the retrieval-bias assessment with current policyholder demographic data ahead of annual revalidation for decision-support use cases. State insurance-fairness frameworks expect ongoing fairness monitoring, not a one-time baseline.
- Documenting the corpus as "claim file" without per-document-type provenance tagging. Medical records, correspondence, and adjuster notes carry different reliability postures; the corpus-fitness assessment loses the signal when they are rolled up.
