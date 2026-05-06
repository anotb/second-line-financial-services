# rag-evaluation-review — Phase 1 spec sheet

Date: 2026-05-06
Plugin: ai-governance-model-risk
Phase: 1 (per-skill scoping; no SKILL.md content)
Status: NEW for v1 (GenAI expansion).

## Activation-tuned description

Reviews the retrieval and grounding evaluation for a RAG-based GenAI use case. Confirms the corpus is fit for purpose, retrieval quality is measured, grounding (faithfulness, citation precision, refusal on out-of-scope queries) is tested with named methods, and ongoing monitoring is in place. Output is a second-line memo on whether the RAG implementation can be relied on for the use case's intended purpose, with named gaps and owner actions.

Best for:
- A first-line owner has built a RAG system and second-line needs an evaluation review before pre-prod, expansion, or annual revalidation.
- A foundation-model swap or retrieval-stack change has happened and the grounding evaluation needs to be re-confirmed.
- An incident on hallucination or off-corpus answer has surfaced and the committee needs an updated grounding posture.

Not the right tool when:
- The system has no retrieval (use validation-plan with the GenAI testing block).
- The work is the prompt-injection threat surface review (use prompt-injection-risk; use both side by side for a RAG agent).
- The work is the corpus access-control review only (use the privacy and cyber overlays in vendor-diligence or genai-pre-prod-review).

Anchored to: NIST AI RMF Generative AI Profile (NIST AI 600-1) Measure 2.9 (information integrity), Measure 1.1 (hallucination/confabulation), Manage 4.1 (deployment monitoring); SR 11-7 §V (validation, with focus on data and outcomes analysis applied to RAG); OCC Bulletin 2026-13 (revised interagency model risk management guidance, 2026) [verify section]; ISO/IEC 42001:2023 §8.x (operational controls); EU AI Act Article 10 (data governance) where applicable.

## Source anchors

- NIST AI RMF Generative AI Profile (NIST AI 600-1) — Measure 1.1 (hallucination/confabulation), Measure 2.9 (information integrity, including provenance and verifiability), Manage 4.1 (deployment monitoring), Govern 6.1 (third-party considerations) [verify exact subcategory numbering].
- SR 11-7 §V — validation activities, with the data-review and outcomes-analysis pillars applied to retrieval corpora and grounding outputs.
- OCC Bulletin 2026-13 (revised interagency model risk guidance, 2026) [verify section] — refreshed validation expectations including AI/ML and GenAI inclusion.
- ISO/IEC 42001:2023 §8.1 (operational planning), §9.1 (monitoring, measurement).
- EU AI Act Article 10 (data and data governance) — for high-risk AI; informational where applicable.
- Industry practice on grounding evaluation frameworks (RAGAS-style metric families: faithfulness, answer relevance, context precision, context recall) — used at the conceptual level only; practitioner expectation is that any equivalent named framework or in-house equivalent is acceptable as long as the metric semantics are documented.
- NYDFS Industry Letter on Cybersecurity Risks Arising from AI (October 2024) — informational where corpus access controls are part of cyber overlay.

## Sector overlays needed

- `references/sector-overlays/banking.md` — RAG corpora typical of banking (CRM, policy library, AML alert narratives, client documents); regulator overlap with FFIEC IT booklet expectations on data integrity.
- `references/sector-overlays/insurance.md` — RAG corpora typical of insurance (claim files, policy documents, medical records under HIPAA); NAIC Model Bulletin alignment, state insurance fairness expectations on retrieval-driven decision support.
- `references/sector-overlays/capital-markets.md` — RAG corpora typical of capital markets (research notes, transcripts, regulatory filings); MAR / Reg AC adjacency on selective disclosure or biased retrieval.
- `references/sector-overlays/payments-fintech.md` — RAG corpora typical of fintech (terms-of-service documents, dispute evidence, sponsor-bank policies).

## Cross-cutting overlays

- `references/cross-cutting/cyber.md` — corpus access controls, retrieval-side authentication, prompt-injection adjacency to indirect injection through corpus content.
- `references/cross-cutting/privacy.md` — primary overlay. Corpus content with regulated NPI / PHI; minimisation, purpose limitation, retention.
- `references/cross-cutting/conduct.md` — fairness-of-retrieval (does retrieval surface representative content across populations); customer-facing accuracy.

Climate not applicable.

## Output template named sections

1. Use case reference and RAG architecture summary
2. Corpus fitness review (sources, freshness, coverage, sensitivity, provenance)
3. Retrieval quality evaluation (named metrics: context precision, context recall, retrieval latency; methods, datasets, results)
4. Grounding evaluation (named metrics: faithfulness, citation precision, answer relevance, refusal-rate on out-of-scope; methods, datasets, results)
5. Failure modes catalogued (hallucination, off-corpus answer, citation fabrication, stale-content answer, retrieval bias)
6. Mitigations in place (corpus curation, vetting, prompt design, refusal behaviour, citation enforcement, structured output)
7. Monitoring (sampling cadence, ground-truth pipeline, drift signals, owners)
8. Residual risk (named, with likelihood and impact framing, accepted-risk owners)
9. Recommended owner actions (gaps to close, deadlines)
10. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `use_case_id` | string | Links to intake record. |
| `architecture_summary` | object | Sub-fields: foundation_model, retriever_type, corpus_count, refresh_cadence. |
| `corpus_fitness` | array of objects | Each: corpus, source, freshness, coverage_assessment, sensitivity, provenance, owner. |
| `retrieval_quality` | array of objects | Each: metric (context_precision/context_recall/latency), method, dataset_ref, value, threshold, owner. |
| `grounding_evaluation` | array of objects | Each: metric (faithfulness/citation_precision/answer_relevance/refusal_rate), method, dataset_ref, value, threshold, owner. |
| `failure_modes` | array of objects | Each: failure_mode, frequency, example, mitigation. |
| `mitigations` | array of objects | Each: mitigation, type, evidence. |
| `monitoring` | array of objects | Each: signal, sampling_cadence, ground_truth_pipeline, owner, escalation_path. |
| `residual_risk` | array of objects | Each: risk, likelihood, impact, accepted_owner. |
| `recommended_actions` | array of objects | Each: gap, owner, deadline, severity. |
| `source_trace` | array of objects | Claim, source, evidence reference, confidence. |

## Example scenarios (public-source-derived, anonymous)

1. A US bank deploys a RAG-based assistant for compliance analysts that retrieves over the firm's internal compliance policy library and a vendor-supplied regulatory-text database. Review captures: corpus fitness (policy library refreshed quarterly with a known lag, vendor regulatory database updated weekly with provenance), retrieval quality (context precision and recall measured on a held-out analyst query set), grounding (faithfulness and citation-precision measured on the same set, refusal-rate on out-of-scope queries about firm-confidential matters), failure modes (stale-policy answer, citation fabrication, off-corpus answer drawing on foundation-model parametric knowledge), mitigations (citation-enforcement requires a corpus reference for any factual claim, refusal pattern for queries the assistant cannot ground), monitoring (weekly faithfulness sampling against ground truth, refusal-rate dashboard).

2. A regional life insurer's RAG-based claims summary assistant retrieves over claim file documents only (PHI), no external corpora. Review captures: corpus fitness (per-claim file scoped retrieval, retention bounded to claim lifecycle, provenance tagged per document), retrieval quality (context precision on adjuster query test set; recall less critical since over-retrieval is acceptable when filtered), grounding (faithfulness, citation-precision, refusal on cross-claim queries), failure modes (cross-claim leakage if scoping fails, OCR-driven retrieval miss on poor scans, hallucinated medical fact), mitigations (per-claim scope enforced at retriever, OCR confidence threshold, output-filter refusal of any cross-claim ID reference), monitoring (sampling of summaries against adjuster review, OCR-confidence trend, refusal-rate trend).

## Common pitfalls

1. The evaluation reports faithfulness as a single number with no segmentation across query type, corpus, or population. Hides systematic failure on a query class. Mitigation: required segment-level reporting on at least query type and corpus.
2. The "corpus" is documented as a single name without source detail. The corpus is actually three sources of varying provenance and freshness, and only one of them is curated. Mitigation: corpus fitness block requires per-source enumeration.
3. Refusal-rate is measured but no out-of-scope test set exists. The number is meaningless. Mitigation: refusal-rate evaluation requires a labelled out-of-scope test set documented in `dataset_ref`.
4. Citation precision is reported as 100% because every output contains a citation marker, regardless of whether the cited document supports the claim. Mitigation: citation precision must be defined as supports-the-claim, not contains-a-marker; documented method required.
5. Monitoring relies on user-feedback thumbs only. Insufficient signal. Mitigation: required ground-truth pipeline (sampled adjudication, golden-set replay, or equivalent) at a defined cadence.
