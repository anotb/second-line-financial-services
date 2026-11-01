# Troubleshooting: rag-evaluation-review

Recurring defects from RAG evaluation reviews and how to address them. Read alongside the skill spec sheet's common-pitfalls list and the loaded sector and cross-cutting overlay common-pitfalls sections.

## "Corpus" recorded as a single name when it is actually multiple sources

The most common review defect. The use case documents its "compliance corpus" or "claims corpus" or "research corpus" as a single name; the actual implementation indexes three or four sources of varying provenance, freshness, and ownership. Rolling them up loses the freshness, provenance, and ownership signal.

Fix: per-source enumeration is non-optional. Each row in `corpus_fitness[]` names one source by its system of record, with its own freshness, provenance, sensitivity, and owner. If the use case document calls it one corpus and the implementation has three sources, the review records three rows and notes the documentation gap as a recommended action.

## Faithfulness reported as a single number with no segmentation

A single global faithfulness number above the threshold can hide systematic failure on a query class, a corpus, or a population segment. The headline number is comforting; the segment-level detail is the analytical work.

Fix: required segment-level reporting on at least query type and corpus for every grounding metric. Where the use case has a population dimension (customer segment, geography, line of business), add the population segmentation. The conduct overlay surfaces fairness segmentation as the load-bearing extension.

## Refusal-rate measured but no labelled out-of-scope set exists

Refusal rate without a labelled out-of-scope test set is meaningless; the metric measures the rate at which the assistant refuses, but without a known-correct refusal target the rate has no reference.

Fix: refusal-rate evaluation requires a labelled out-of-scope test set documented in `dataset_ref`. If the dataset is absent or vague, the entry routes to recommended actions. The labelled set carries multiple classes (firm-confidential, off-corpus questions, questions about the assistant itself, scope-violating queries) with per-class labels; per-class refusal rates are the right segmentation.

## Citation precision reported as 100% because every output contains a citation marker

Citation precision defined as "the output contains a citation marker" is meaningless; it measures formatting compliance, not whether the cited document supports the claim. This is a recurring failure mode; vendor-supplied citation-precision numbers are often defined this way.

Fix: citation precision must be defined as supports-the-claim, not contains-a-marker. The `metric_definition` field carries the definition explicitly. Method requires SME adjudication on a sample (typically a few hundred cases) where the SME judges whether the cited document section supports the claim, not whether a citation marker is present. Vendor-supplied citation-precision numbers are recorded at vendor-self-attestation confidence; firm-side SME-adjudicated numbers carry higher confidence.

## Mitigations listed without evidence and without test coverage

A mitigation entry without an evidence pointer is policy, not a control. A mitigation entry with `exercised_in_test = false` is asserted coverage, not demonstrated coverage.

Fix: each `mitigations[]` entry requires an evidence pointer (config link, test report, change record, or `[evidence needed]`). Each entry needs `exercised_in_test` set explicitly. Mitigations marked `[evidence needed]` or `exercised_in_test = false` route to recommended actions, not silently into the memo body.

## Residual risk recorded as "low" without basis

"Low" without a one-line basis is opinion. The residual-risk table requires likelihood, impact, and basis on every entry.

Fix: re-write each residual-risk entry with the basis populated. The basis names the controls that hold the likelihood down, the failure mode that drives the impact, and the assumption that fails first when the control set degrades. If the basis cannot be written, the rating is unsupported and routes to recommended actions for further analysis.

## Monitoring relies on user-feedback thumbs only

Thumbs feedback from end users is sentiment, not ground truth. A monitoring section that lists thumbs as the primary signal is a dashboard, not a control programme.

Fix: every `monitoring[]` entry requires a `ground_truth_pipeline` populated. The pipeline is one of: sampled adjudication against SME judgement, golden-set replay against a labelled ground-truth set, automated scoring with a calibrated method, or rule-based detection with periodic SME calibration. Thumbs feedback can supplement (as a downstream-acceptance signal alongside adjuster-edit rate or analyst-edit rate) but does not substitute.

## Stale-content answer treated as hallucination

A stale-content answer is a corpus-fitness failure (the corpus did not contain the current version) or a freshness-gate failure (the retriever returned a superseded version), not a grounding failure. Treating it as hallucination misses the framing and routes the residual-risk and recommended-action to the wrong owner.

Fix: stale-content answer is its own failure-mode row, with the freshness gate as the linked mitigation. The corpus-fitness section names the refresh cadence and the known lag. The mitigation includes the freshness gate (filter out versions superseded after the current effective date) where the use case can support that filter.

## Per-customer or per-claim scoping asserted at the prompt layer rather than the retriever layer

Prompt-layer scoping is bypassable; an injected instruction in retrieved content can extract or reference data outside the intended scope. Retrieval-layer scoping is structural; the retriever cannot return content outside the scope by construction.

Fix: the review confirms the layer at which scoping is enforced. Prompt-layer-only scoping is a finding for any use case touching regulated personal data (NPI, PHI, MNPI). The recommended-action names the retrieval-platform owner and the implementation path.

## Retrieval-bias not assessed

Retrieval-bias is the canonical fairness question for RAG systems with a population dimension: does retrieval surface representative content across populations? The default behaviour of dense-vector retrievers can favour content that is well-represented in the training corpus, which can correlate with demographic attributes.

Fix: where the use case has a population dimension and the conduct overlay loads, retrieval-bias assessment is non-optional. Annual reassessment at minimum; continuous monitoring for high-volume customer-facing use cases. Method is documented in the firm's fair-lending or fairness-monitoring methodology; the residual-risk acceptance carries a basis.

## Foundation-model swap re-validation flag missing

For any architecture depending on a third-party foundation model, the standard recommended-action item that fires is the foundation-model swap re-validation flag in change management: an explicit re-run of this review on every vendor change-of-version notice. A vendor model swap can shift faithfulness, refusal behaviour, and citation patterns and invalidate the residual-risk view.

Fix: confirm the recommended-actions section includes the foundation-model swap re-validation item. If the foundation-model versioning posture is rolling-with-notice, additionally surface a recommended action to move to pinned versioning for tier-1 and tier-2 use cases.

## Vendor evaluation results presented as firm-side coverage

Vendor-supplied evaluation results test the vendor's foundation-model and the vendor's evaluation pipeline against the vendor's test set. They do not test the firm's prompt template, the firm's corpus, the firm's retrieval scoping, or the firm's intended-purpose-tied thresholds.

Fix: the metric entries record the source explicitly. Source-trace entries record vendor evidence at vendor-self-attestation confidence (typically low to medium). Recommended actions surface firm-internal evaluation gaps as `[evidence needed]` items.

## Cross-scope leakage treated as hallucination

Cross-scope leakage (cross-customer, cross-claim, cross-policy, cross-account) is a privacy event, not a model issue. Treating it as a hallucination misses the framing and routes the response posture to the wrong runbook.

Fix: cross-scope leakage is a separate failure-mode row with a privacy framing. A confirmed event triggers the privacy overlay's incident-response framing and the regulator-notification trigger evaluation. The mitigation set centres on retrieval-layer scoping; the monitoring set centres on rule-based detection plus SME spot-check.

## Adjacency to prompt-injection-risk not surfaced

Indirect injection through corpus content is the prompt-surface seam to a RAG system. This skill catalogues the grounding-side failure mode (off-corpus answer, citation fabrication driven by injected content); the focused threat-surface review lives in `prompt-injection-risk`.

Fix: confirm a `prompt-injection-risk` review is on file or in flight for the same use case. The recommended-actions section names the adjacency. The cyber overlay carries the framing.

## OCR-driven retrieval miss treated as an OCR engineering issue

OCR-driven retrieval miss on poor-scan documents (legacy medical records, scanned policy documents, handwritten notes) is a corpus-fitness issue, not just an OCR engineering question. Documents below the OCR confidence threshold are corpus-incomplete documents.

Fix: the OCR confidence gate is part of the corpus-fitness control set. Sub-threshold documents flag for human OCR review or re-processing before inclusion in retrieval. The monitoring section includes OCR confidence trend as a signal; ingestion-pass-rate drift is a leading indicator.

## Sector overlay loaded but the sector-specific seam not surfaced

Each sector overlay carries seams the RAG evaluation review tends to miss without the overlay (banking BSA officer involvement; insurance HIPAA minimum-necessary at retrieval; capital markets information-barrier enforcement at retrieval; payments-fintech sponsor-bank shared-responsibility allocation). Loading the overlay without surfacing the seam in the review is the failure mode.

Fix: re-read the loaded sector overlay against the review and confirm each named overlay-specific consideration is reflected in the corpus-fitness, mitigations, monitoring, or recommended-actions sections.

## Engagement scope not formalised

When the scope record is not supplied and the practitioner declines to formalise scope, the review still proceeds against a default public posture but should record the omission.

Fix: the review-metadata section notes that scope was not formalised; the recommended-actions section includes formalising scope as a low-or-medium-severity item; the source-trace confidence labels reflect the lack of formalised scope on items that would have been resolved by it.
