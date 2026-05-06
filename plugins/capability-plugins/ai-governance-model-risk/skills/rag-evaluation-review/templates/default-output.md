# RAG evaluation review: [use case name and version]

Starting structure for a second-line review of a RAG-based GenAI use case. Depth flexes with tier, lifecycle stage, and audience; the section list does not. A pre-prod gate review compresses production-monitoring evidence; an in-prod-periodic or post-incident review expands it. Items without evidence carry `[evidence needed]` and route to recommended actions, not silently into the memo.

The memo is a draft until the human reviewer attests.

---

## 1. Review metadata

- Reviewer role: [function, e.g. AI Governance Lead, MRMO, second-line model risk]
- Review stage: [pre-prod-gate / in-prod-periodic / post-incident / post-foundation-model-swap / post-retrieval-stack-change / annual-revalidation / exam-readiness]
- Review date: [YYYY-MM-DD]
- Engagement-scope ID (if `engagement-scoping` was run): [ID]
- Model card ID (links to `model-card-builder`): [ID]
- Validation plan ID (links to `validation-plan`): [ID]

---

## 2. Use case reference and RAG architecture summary

- Use case ID (links to `ai-use-case-intake`): [ID]
- Tier: [tier-1 / tier-2 / tier-3 / tier-4 / tier-unassigned, with reference to `ai-risk-tiering` output]
- Lifecycle stage: [development / pre-prod / prod / monitoring-only / retirement]
- Intended purpose: [stated purpose; the reliance assertion is judged against this]
- Foundation model: provider, name, version, version pinning posture (pinned, floating, rolling-with-notice, unknown)
- Retriever: type (dense-vector, sparse-bm25, hybrid, graph, structured-query, rerank-stack), embedding model, reranker
- Corpora: count of distinct corpora the retriever indexes (per-source enumeration in section 3)
- Refresh cadence summary: one line across corpora; per-corpus cadence in section 3
- Scoping rules: per-user, per-tenant, per-case retrieval scoping at the retriever layer

A short architecture diagram or pointer to the model card's system description is preferable to re-restating the system here.

---

## 3. Corpus fitness

Per-source enumeration. A "corpus" documented as a single name but actually three sources of varying provenance and freshness records as three rows.

| Corpus | Source (system of record) | Freshness | Coverage assessment | Sensitivity | Provenance | Owner | Access controls |
|---|---|---|---|---|---|---|---|
| [name] | [underlying source system, not just a label] | [refresh cadence, last refresh, known lag] | [fit against intended purpose; gaps named] | [public / internal / confidential / regulated-NPI / regulated-PHI / MNPI / privileged] | [tagged / untagged / partial; basis] | [function] | [retrieval-side enforcement; pointer to cyber overlay if applicable] |

Coverage assessment is the second-line judgement on whether the corpus actually answers the use case's intended question space. Naming a gap is more useful than asserting "comprehensive coverage".

---

## 4. Retrieval quality evaluation

Industry-practice metric families (the RAGAS-style families: context precision, context recall, retrieval latency) plus reranker lift and scoping correctness where applicable. Equivalent in-house metrics are acceptable provided the semantics are documented in `metric_definition`.

| Metric | Definition | Method (framework, version, judge basis) | Dataset ref | Segmentation | Result | Threshold | Evidence pointer | Owner |
|---|---|---|---|---|---|---|---|---|
| context_precision | [definition] | [method] | [dataset ID] | [segments reported, e.g. by query type, by corpus] | [headline value] | [acceptance threshold tied to intended purpose] | [pointer] | [function] |
| context_recall | | | | | | | | |
| retrieval_latency | | | | | | | | |
| rerank_lift (if applicable) | | | | | | | | |
| scoping_correctness (if applicable) | | | | | | | | |

A single number with no segmentation hides systematic failure on a query class. Required reporting at minimum: by query type, by corpus, and by population where the use case has a population dimension (customer segment, geography, line of business).

---

## 5. Grounding evaluation

Industry-practice metric families (the RAGAS-style families: faithfulness, answer relevance) plus citation precision and refusal rate on a labelled out-of-scope set. Equivalent in-house metrics acceptable provided the semantics are documented.

| Metric | Definition | Method (framework, version, judge basis) | Dataset ref | Segmentation | Result | Threshold | Evidence pointer | Owner |
|---|---|---|---|---|---|---|---|---|
| faithfulness | [definition] | [method] | [dataset ID] | [segments] | [value] | [threshold] | [pointer] | [function] |
| answer_relevance | | | | | | | | |
| citation_precision | [must be defined as supports-the-claim, not contains-a-marker] | | | | | | | |
| refusal_rate_on_out_of_scope | [requires labelled out-of-scope set] | | | | | | | |
| hallucination_rate (if measured) | | | | | | | | |
| stale_content_rate (if measured) | | | | | | | | |

Citation precision defined as "every output contains a citation marker" is meaningless; the metric must measure whether the cited document supports the claim. Refusal rate measured without a labelled out-of-scope test set is meaningless; if the dataset reference is absent or vague, the entry routes to recommended actions.

---

## 6. Failure modes catalogued

For each failure mode observed or anticipated:

| Failure mode | Frequency (rate, basis) | Example (anonymised, pattern) | Mitigation |
|---|---|---|---|
| hallucination | | | |
| off_corpus_answer | | | |
| citation_fabrication | | | |
| stale_content_answer | | | |
| retrieval_bias | | | |
| cross_scope_leakage | | | |
| ocr_or_parsing_miss (if applicable) | | | |
| refusal_failure_on_out_of_scope | | | |
| over_refusal_on_in_scope | | | |

Baseline set above; failure modes not applicable to the architecture record as "not applicable" rather than omitted. Frequency is a rate with a basis (sampled set, monitoring window) or `[evidence needed]`. The example is a pattern; specific facts that would identify a customer or transaction stay out.

---

## 7. Mitigations in place

For each mitigation:

| Mitigation | Type | Owner | Evidence pointer | Exercised in test? |
|---|---|---|---|---|
| [name] | [corpus_curation / source_vetting / retrieval_scoping / reranking / prompt_design / citation_enforcement / structured_output / refusal_behavior / human_in_the_loop_gate / freshness_gate / ocr_confidence_gate / output_filter / logging_and_monitoring] | [function] | [config link, test report, change record, or `[evidence needed]`] | [yes / no] |

A mitigation without an evidence pointer is policy, not a control. A mitigation listed but not exercised in any evaluation run is recorded with `exercised_in_test = no` and routed to recommended actions; do not treat it as coverage.

---

## 8. Monitoring

For each production signal:

| Signal | Sampling cadence | Ground-truth pipeline | Threshold | Owner | Escalation path |
|---|---|---|---|---|---|
| [name] | [continuous / daily / weekly / monthly / event-driven] | [sampled adjudication / golden-set replay / SME review / automated scoring] | [value, in firm policy units] | [function] | [named committee, officer, or process; CISO function for cyber-tagged signals] |

User-feedback thumbs alone is not a monitoring programme. A ground-truth pipeline at a defined cadence is required: sampled adjudication against SME judgement, golden-set replay, or an equivalent. Without it, the monitoring section is a dashboard, not a control.

The baseline signal set for a typical RAG system: faithfulness sampling against ground truth, citation-precision sampling, refusal-rate dashboard, retrieval-source audit, retrieval latency, foundation-model version monitoring, corpus refresh-cadence monitoring. For systems with PHI, NPI, or MNPI corpora, add cross-scope leakage detection. For systems with OCR-driven retrieval, add OCR confidence trend.

---

## 9. Residual risk

For each named residual risk:

| Risk | Likelihood | Impact | Basis | Accepted owner role | Accepted date | Review cadence |
|---|---|---|---|---|---|---|
| [concrete description] | [low / medium / high] | [low / medium / high] | [one-line basis] | [role, never an individual] | [YYYY-MM-DD] | [quarterly / on foundation-model swap / on corpus refresh-cadence change / etc.] |

"Low" without a basis is opinion. The basis column is required. Cross-reference any failed acceptance threshold in retrieval_quality, grounding_evaluation, or failure_modes to a residual-risk row; an unaccepted threshold breach is itself a finding.

---

## 10. Recommended owner actions

For each gap:

| Gap | Owner role | Deadline | Severity | Depends on |
|---|---|---|---|---|
| [concrete gap] | [function, never an individual] | [YYYY-MM-DD] | [low / medium / high / critical] | [other action / upstream artifact / external dependency] |

Severity is the second-line judgement, not the owner's. Critical-severity items typically block pre-prod sign-off. The standard recommended-action item that fires for any architecture depending on a third-party foundation model is the foundation-model swap re-validation flag in change management, with explicit re-run of this review on every change-of-version notice.

---

## 11. Source trace and confidence

For every material claim in the memo:

| Claim | Source | Evidence reference | Confidence |
|---|---|---|---|
| [claim] | [document, system, person, vendor evidence, or `[evidence needed]`] | [pointer] | [high / medium / low / evidence-needed] |

Vendor-supplied evaluation results carry vendor-self-attestation confidence (typically low to medium). Firm-internal evaluation results carry higher confidence. Do not collapse vendor and firm evidence into one line. `[evidence needed]` flags route to recommended actions.

---

## 12. Sector and cross-cutting overlay notes (when applicable)

When the engagement scope names a sector, the matching `references/sector-overlays/<sector>.md` adds named fields here. Examples:

- Banking: FFIEC IT Handbook touchpoint on data integrity for retrieval corpora; AML alert-narrative corpora and BSA officer involvement; sponsor-bank shared-responsibility allocation.
- Insurance: PHI corpora and HIPAA minimum-necessary at the retrieval layer; NAIC AIS Program documentation; state insurance fairness expectations on retrieval-driven decision support.
- Capital markets: research-note and transcript corpora; MAR / Reg AC adjacency on selective disclosure or biased retrieval; surveillance-system retrieval surface; Marketing Rule reach for AI-generated client-facing content.
- Payments and fintech: terms-of-service corpora, dispute-evidence corpora, sponsor-bank policy corpora.

When the engagement scope flags cross-cutting overlays, add the matching `references/cross-cutting/<topic>.md` fields:

- Privacy: per-source sensitivity tagging, retrieval-side minimisation and purpose limitation, retention cadence; cross-scope leakage as a privacy event class.
- Cyber: corpus access controls and retrieval-side authentication; indirect injection through corpus content as the prompt-injection-adjacent surface; pointer to `prompt-injection-risk` for the focused review.
- Conduct: fairness-of-retrieval across populations; customer-facing accuracy; complaint-rate and complaint-code drift as conduct signals.

If no overlay is loaded, this section is omitted.

---

## Reviewer attestation block

The memo is reviewable when sections 2 through 11 are filled and the source trace is complete. The human reviewer attests:

- **Reviewer**: [role, function]
- **Reviewer date**: [YYYY-MM-DD]
- **Decision**: [accept / accept-with-conditions / reject-and-rework]
- **Conditions (if any)**: [conditions, owner roles, dates]
- **Onward routing**: [AI risk committee / pre-prod gate / MRMO challenge file / exam response file / board pack]

The memo is filed only after attestation.
