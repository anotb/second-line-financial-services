# Example: RAG evaluation review for a regional life insurer's claims-summary assistant

Public-source-derived. No named institution. Pattern aligns with the spec sheet's second scenario.

## Input description

A regional US life insurer is approaching the in-prod-periodic review for a RAG-based claims-summary assistant. The assistant retrieves over claim-file documents only (PHI), produces a structured summary the adjuster reviews and edits, and never communicates with the policyholder directly. No external corpora. No tools enabled. Foundation model is vendor-hosted with version pinning. The system has been in production for nine months; this is the second post-go-live review.

Engagement scope provided by `scoping`:
- Institution type: state-domiciled life insurer; primary regulator the state DOI; NAIC AI Bulletin adopted in the domiciliary state.
- Persona: AI Governance Lead (second line), with the chief actuary and the privacy officer as named co-reviewers.
- Sector overlay: insurance. Cross-cutting overlays: privacy (PHI corpus, HIPAA scope), conduct (claims-handling fairness expectations under the unfair claims-settlement-practices framework), cyber (per-claim retrieval scoping is a security-relevant control).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence-plus-production-monitoring.
- Tier: tier-2.

Upstream artifacts: `model-card-builder` output is on file and was refreshed at the six-month mark; `validation-plan` outcomes-analysis block is up to date; nine months of production monitoring evidence is available.

## Output sketch

Sections produced (abbreviated):

- **Use case reference and RAG architecture summary** — `claims-summary-v1.2`, tier-2, prod. Foundation model `vendor-X model-Y vN`, pinned. Retriever: dense-vector with reranker. One corpus indexed: claim-file documents per claim, including correspondence, medical records, prior summaries, and adjuster notes. Per-claim scoping enforced at the retriever layer (the retriever is parameterised on claim ID; cross-claim retrieval cannot occur at the retriever level by construction). Refresh cadence: continuous (new documents land in the claim file as scanned-and-OCR'd or as digital uploads).

- **Corpus fitness** — one row, sub-detailed:
  - Per-claim corpus (system of record: claims platform with document-management add-on); freshness continuous; coverage assessment: full per-claim file in scope; documented gap on legacy claims (claims opened before the document-management migration) where retrieval may be incomplete; sensitivity: regulated-PHI; provenance: per-document type-tagged (claim form, medical record, adjuster note, correspondence) with source-system tagging and ingestion-date stamp; owner: Claims Operations with the Privacy Officer as data-protection co-owner; access controls: claim-bound retrieval enforced at the retriever; document-level access bound to the adjuster's case load.

- **Retrieval quality evaluation** — three metrics:
  - context_precision: definition documented; method: in-house evaluation pipeline against a held-out adjuster query set (800 claims sampled by adjuster); segmented by document type (medical, correspondence, prior-summary, adjuster-note) and by claim age; headline 0.84; threshold ≥ 0.80; passes; segment performance lower on legacy-claim subset (0.71) routed to recommended actions.
  - context_recall: definition documented; same method; headline 0.91; threshold ≥ 0.75 (over-retrieval is acceptable when filtered downstream); passes.
  - retrieval_latency: p99 ≤ 1.2s; threshold ≤ 1.5s; passes.

- **Grounding evaluation** — five metrics:
  - faithfulness: definition documented; method: in-house LLM-judge calibrated against an SME-adjudicated 300-case set (300 cases reviewed by senior claims-quality function); dataset: held-out adjuster claim set; segmented by document type and by claim type (auto, life, disability); headline 0.91; threshold ≥ 0.90; passes; lower on disability claims (0.86) where medical records carry more interpretation; routed to monitoring rather than recommended action (within tolerance, but tracked).
  - answer_relevance: 0.93 on the same set; threshold ≥ 0.85; passes.
  - citation_precision: defined as "the cited document supports the claim"; method: SME-adjudicated 300-case sample; headline 0.92; threshold ≥ 0.90; passes.
  - refusal_rate_on_out_of_scope: dataset is a labelled 200-case set covering cross-claim queries (e.g., "what other claims has this policyholder filed?"), questions about firm policy, questions about the assistant itself; headline 0.97; threshold ≥ 0.95; passes; segment performance is 1.0 on cross-claim queries (the per-claim retrieval scoping makes this near-impossible to fail at retrieval level).
  - hallucination_rate: defined as a claim made in the summary that is not supported by any retrieved document; method: SME-adjudicated subsample of the faithfulness set; headline 0.06; threshold ≤ 0.10; passes; segment performance higher on disability claims; routed to monitoring.

- **Failure modes catalogued** — six rows:
  - hallucination: 6% baseline; example: medical fact stated in the summary that does not appear in retrieved medical records; mitigation: faithfulness sampling and citation enforcement; exercised in evaluation; tracked on monitoring.
  - cross_scope_leakage: not observed in nine months of production monitoring; basis: per-claim retrieval enforced at the retriever; mitigation: retrieval scoping; exercised continuously by construction.
  - ocr_or_parsing_miss: observed at approximately 3% on legacy-claim medical records (poor scan quality); mitigation: OCR confidence threshold (claims below threshold flagged for human OCR review before inclusion in retrieval); exercised in evaluation; routed to recommended actions for OCR-quality programme.
  - stale_content_answer: not applicable in the standard sense (claim files are continuous, not refresh-cadence-bound); failure surfaces as the assistant answering on prior-summary content rather than current evidence; mitigation: summary versioning and date-stamping; exercised in evaluation.
  - citation_fabrication: not observed in the SME-adjudicated set.
  - retrieval_bias: assessed across claim type and policyholder demographic segment in the annual revalidation; no statistically significant bias observed at the most recent assessment; tracked on monitoring with annual reassessment.

- **Mitigations in place** — eight rows: per-claim retrieval scoping (evidence: retriever platform config, exercised continuously); reranking on document-type relevance (evidence: retriever config, exercised in retrieval-quality evaluation); OCR confidence threshold (evidence: ingestion pipeline config, exercised on legacy claims); citation enforcement requires a document reference for any factual claim (evidence: prompt template, exercised); structured-output enforcement on the summary schema (evidence: vendor-side, exercised); refusal behaviour for cross-claim and out-of-scope queries (evidence: prompt template, exercised); adjuster-review gate (evidence: workflow design, preventive control); output-filter refusal of any cross-claim ID reference in summary (evidence: post-process filter config, exercised in cross-scope leakage testing).

- **Monitoring** — seven signals with all five fields:
  - Faithfulness sampling against SME-adjudicated ground truth; sampling cadence weekly (40 cases); ground-truth pipeline: SME review by claims-quality function; threshold drop greater than 3 points week-over-week; owner: AI governance team; escalation: model risk committee with the chief actuary.
  - Citation-precision sampling; sampling cadence weekly (40 cases); ground-truth pipeline: SME review; threshold drop greater than 3 points; owner: AI governance team; escalation: model risk committee.
  - Refusal-rate dashboard segmented by class; sampling cadence continuous; ground-truth pipeline: golden-set replay against the labelled out-of-scope set monthly; threshold any drop greater than 3 points on cross-claim class; owner: AI governance team; escalation: privacy officer plus AI Governance Lead.
  - Cross-scope leakage detection (rule-based detection on cross-claim ID surfaces in summary output); sampling cadence continuous; ground-truth pipeline: rule-based plus weekly SME spot-check; threshold any confirmed event triggers incident response; owner: privacy officer; escalation: privacy officer plus CISO function plus AI Governance Lead.
  - OCR confidence trend; sampling cadence continuous; ground-truth pipeline: automated against ingestion pipeline; threshold ingestion-pass-rate drop greater than 5 points; owner: claims operations with AI governance; escalation: AI Governance Lead.
  - Adjuster-edit rate (adjuster acceptance posture as a leading indicator of summary quality drift); sampling cadence continuous; ground-truth pipeline: workflow event log; threshold edit-rate increase greater than 10 points week-over-week; owner: claims operations; escalation: AI Governance Lead.
  - Foundation-model version monitoring; sampling cadence continuous; ground-truth pipeline: vendor change-of-version notice; threshold any change; owner: vendor management; escalation: AI Governance Lead with re-run of this review per change-management table.

- **Residual risk** — three concrete items:
  - Hallucinated medical fact on disability-claim summaries. Likelihood: low-to-medium (within tolerance but elevated on the segment). Impact: medium (adjuster review is the preventive control; under volume pressure, edit rates compress and the gate weakens). Owner: AI Governance Lead with chief actuary; quarterly review with attention to the adjuster-edit-rate signal.
  - Legacy-claim retrieval miss on poor-scan medical records. Likelihood: medium (3% baseline). Impact: medium. Owner: claims operations with AI Governance Lead; review on every OCR-quality programme update.
  - Foundation-model swap shifts faithfulness or refusal behaviour. Likelihood: medium. Impact: medium. Owner: AI Governance Lead jointly with vendor management; review on every change-of-version notice.

- **Recommended owner actions** — five gaps:
  - Improve legacy-claim retrieval through OCR re-processing of high-impact legacy medical records. Owner: claims operations with AI governance; deadline: within 90 days; severity: medium.
  - Tighten faithfulness threshold on disability-claim segment through prompt-design refinement. Owner: AI governance team; deadline: next quarterly review; severity: medium.
  - Add adjuster-edit-rate signal to the AI risk committee dashboard as a load-bearing indicator. Owner: AI Governance Lead; deadline: next AI risk committee cycle; severity: medium.
  - Confirm `foundation_model_swap_revalidation` flag is operating as designed (no skipped revalidations in the past nine months). Owner: AI Governance Lead jointly with vendor management; deadline: this review cycle; severity: medium.
  - Refresh the retrieval-bias assessment with the most recent policyholder population data ahead of annual revalidation. Owner: AI Governance Lead with chief actuary; deadline: annual revalidation; severity: low.

- **Source trace and confidence** — production monitoring data at high confidence; SME-adjudicated evaluation at high confidence; vendor self-attestation results recorded separately at vendor confidence (low-to-medium).

- **Reviewer attestation** — pending; expected decision: accept (the system is in tolerance against thresholds; recommended actions are continuous-improvement, not blockers).

## Why this scenario matters

- The scenario shows a single-corpus, per-scope-bound architecture where the cross-scope leakage risk is structurally low (per-claim retrieval enforced at the retriever) but the failure mode is still tracked because the structural control is the only line of defence.
- OCR-driven retrieval miss is a real failure mode for claims and other document-heavy use cases. The OCR confidence gate is a load-bearing mitigation; the example shows it tracked as a monitoring signal in addition to a mitigation.
- Adjuster-edit rate is a downstream-acceptance signal that flags summary-quality drift before the SME-adjudicated faithfulness sample picks it up. The example surfaces it as a recommended-action item to land on the AI risk committee dashboard.
- In-prod-periodic reviews compress on threat-surface enumeration (the architecture is settled) and expand on monitoring evidence and residual-risk recalibration. The example shows that compression-and-expansion shape.
- The retrieval-bias assessment is annual rather than continuous, with a baseline plus annual reassessment. The example documents the cadence rather than asserting continuous bias monitoring (which would be over-claim).
