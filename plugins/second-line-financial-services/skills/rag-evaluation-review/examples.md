# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## claims-summary-assistant

### Example: RAG evaluation review for a regional life insurer's claims-summary assistant

Public-source-derived. No named institution. Pattern aligns with the spec sheet's second scenario.

#### Input description

A regional US life insurer is approaching the in-prod-periodic review for a RAG-based claims-summary assistant. The assistant retrieves over claim-file documents only (PHI), produces a structured summary the adjuster reviews and edits, and never communicates with the policyholder directly. No external corpora. No tools enabled. Foundation model is vendor-hosted with version pinning. The system has been in production for nine months; this is the second post-go-live review.

Engagement scope provided by `scoping`:
- Institution type: state-domiciled life insurer; primary regulator the state DOI; NAIC AI Bulletin adopted in the domiciliary state.
- Persona: AI Governance Lead (second line), with the chief actuary and the privacy officer as named co-reviewers.
- Sector overlay: insurance. Cross-cutting overlays: privacy (PHI corpus, HIPAA scope), conduct (claims-handling fairness expectations under the unfair claims-settlement-practices framework), cyber (per-claim retrieval scoping is a security-relevant control).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence-plus-production-monitoring.
- Tier: tier-2.

Upstream artifacts: `model-card-builder` output is on file and was refreshed at the six-month mark; `validation-plan` outcomes-analysis block is up to date; nine months of production monitoring evidence is available.

#### Output sketch

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

#### Why this scenario matters

- The scenario shows a single-corpus, per-scope-bound architecture where the cross-scope leakage risk is structurally low (per-claim retrieval enforced at the retriever) but the failure mode is still tracked because the structural control is the only line of defence.
- OCR-driven retrieval miss is a real failure mode for claims and other document-heavy use cases. The OCR confidence gate is a load-bearing mitigation; the example shows it tracked as a monitoring signal in addition to a mitigation.
- Adjuster-edit rate is a downstream-acceptance signal that flags summary-quality drift before the SME-adjudicated faithfulness sample picks it up. The example surfaces it as a recommended-action item to land on the AI risk committee dashboard.
- In-prod-periodic reviews compress on threat-surface enumeration (the architecture is settled) and expand on monitoring evidence and residual-risk recalibration. The example shows that compression-and-expansion shape.
- The retrieval-bias assessment is annual rather than continuous, with a baseline plus annual reassessment. The example documents the cadence rather than asserting continuous bias monitoring (which would be over-claim).

## compliance-policy-assistant

### Example: RAG evaluation review for a compliance-analyst policy assistant

Public-source-derived. No named institution. Pattern aligns with the spec sheet's first scenario.

#### Input description

A US bank holding company is approaching the pre-prod gate for a RAG-based assistant for compliance analysts. The assistant retrieves over the firm's internal compliance policy library and a vendor-supplied regulatory-text database, then drafts answers with citations for the analyst to review. No tools enabled. Foundation model is vendor-hosted with version pinning and contractual change-of-version notice.

Engagement scope provided by `scoping`:
- Institution type: bank holding company, mid-cap, primary regulators FRB and CFPB; OCC for the national-bank subsidiary.
- Persona: AI Governance Lead (second line), with MRMO as model-risk co-reviewer.
- Sector overlay: banking. Cross-cutting overlays: privacy (some policy documents reference NPI handling procedures), cyber (corpus access controls), conduct (analyst answers may inform customer-facing communications downstream).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.
- Tier: tier-2.

Upstream artifacts: `model-card-builder` output is on file; `validation-plan` outcomes-analysis block is partially complete (vendor self-attestation results landed; firm-internal held-out analyst query set is in evaluation).

#### Output sketch

Sections produced (abbreviated):

- **Use case reference and RAG architecture summary** — `policy-assistant-v1.0`, tier-2, pre-prod. Foundation model `vendor-X model-Y vN`, pinned, change-of-version notice required by contract. Retriever: hybrid (dense vector + BM25 with reranker). Two corpora indexed; per-corpus enumeration in section 3. Per-user scoping at the retriever layer with role-based entitlement to the policy library; the regulatory-text database is read-only across all analysts.

- **Corpus fitness** — two rows (the assistant's "compliance corpus" is actually two distinct sources):
  - Internal compliance policy library (system of record: policy management platform); refreshed quarterly with a known two-week post-effective-date lag; coverage gap on BSA/AML procedures (housed in the BSA programme document set, not the policy library); sensitivity: confidential; provenance: per-document tagged with last-approved date and approver function; owner: Policy Management; access controls: role-based.
  - Vendor regulatory-text database (system of record: vendor SaaS); updated weekly with vendor-supplied provenance metadata (issuing regulator, citation, effective date, last-amended date); coverage assessment: covers federal banking regulations; gap on state-level guidance and CFPB Circulars (vendor roadmap item); sensitivity: public; provenance: vendor-tagged; owner: AI governance team in coordination with vendor management; access controls: read-only across analysts.

- **Retrieval quality evaluation** — three metrics with segment-level reporting:
  - context_precision: definition documented; method: RAGAS-style framework, in-house pipeline, vN; dataset: held-out analyst query set (1,200 queries, labelled by senior analyst pair); segmented by query type (policy-lookup, scenario, ambiguous) and by corpus; headline value 0.78 (policy-lookup 0.86 / scenario 0.71 / ambiguous 0.62); threshold ≥ 0.80 on policy-lookup and ≥ 0.70 on scenario; result: scenario passes, policy-lookup misses by 2 points, ambiguous below threshold; evidence pointer cited; owner: AI governance team. Routed to recommended actions.
  - context_recall: definition documented; same method and dataset; segmented by query type and corpus; headline 0.74; threshold ≥ 0.75 on policy-lookup; result: marginal miss; routed to recommended actions.
  - retrieval_latency: p50 / p95 / p99 reported; p99 above the 1.5-second user-experience threshold during the morning batch window; routed to capacity action.

- **Grounding evaluation** — four metrics:
  - faithfulness: definition documented (claim is entailed by retrieved context); method: RAGAS-style framework with LLM-judge calibrated against a 200-case SME-adjudicated set; dataset: same held-out analyst query set; segmented by query type and corpus; headline 0.82; threshold ≥ 0.85; below threshold on scenario queries against the policy library; routed to recommended actions.
  - answer_relevance: 0.88 on the same set; threshold ≥ 0.85; passes.
  - citation_precision: defined as "the cited document section supports the claim", not "the output contains a citation marker"; method: SME-adjudicated 200-case sample; headline 0.79; threshold ≥ 0.85; significant gap on regulatory-text citations where the system cited the regulation correctly but to the wrong subsection; routed to recommended actions and to a citation-enforcement mitigation enhancement.
  - refusal_rate_on_out_of_scope: dataset is a labelled 300-case out-of-scope set covering firm-confidential matters, off-corpus questions, and questions about the assistant itself; segmented by class; headline refusal-rate 0.91; threshold ≥ 0.95; misses on firm-confidential class (0.84) routed to recommended actions.

- **Failure modes catalogued** — six rows:
  - stale_content_answer: observed at approximately 4% on policy-lookup against the policy library; basis: 200-case sample over the past quarter cross-checked against the post-effective-date policy version; mitigation: freshness gate (planned), routed to recommended actions.
  - citation_fabrication: not observed in the SME-adjudicated set; the gap is citation precision (wrong subsection), not fabrication; mitigation: citation-enforcement mitigation in place, exercised in evaluation.
  - off_corpus_answer: observed where the assistant draws on parametric knowledge of regulation rather than the corpus; mitigation: prompt design instructs the assistant to refuse if the corpus does not support; not fully exercised on ambiguous queries; routed to recommended actions.
  - retrieval_bias: not assessed; routed to recommended actions for a baseline assessment by query type and corpus before annual revalidation.
  - over_refusal_on_in_scope: noted at low frequency on novel scenario queries; mitigation: prompt design refinement; tracked on the refusal-rate dashboard.
  - cross_scope_leakage: not applicable (no per-customer scoping; assistant is firm-internal across compliance staff).

- **Mitigations in place** — seven rows: corpus curation owned by Policy Management with quarterly refresh cycle (evidence: refresh log, exercised); source vetting on the vendor regulatory-text database via vendor-management diligence (evidence: vendor due-diligence file, exercised in vendor change controls); reranking of retrieved passages (evidence: retriever config, exercised in retrieval-quality evaluation); citation enforcement requires a corpus reference for any factual claim (evidence: prompt template, exercised in citation-precision sampling, but enhancement scope opened on subsection precision); structured-output enforcement on the answer schema (evidence: vendor-side, exercised); refusal behaviour for queries the assistant cannot ground (evidence: prompt template, partial exercise on firm-confidential class); analyst-review gate before any answer is acted on (evidence: workflow design, preventive control).

- **Monitoring** — six signals with all five fields:
  - Faithfulness sampling against SME-adjudicated ground truth; sampling cadence weekly (50 cases); ground-truth pipeline: SME review on a rotating basis from compliance-quality function; threshold drop greater than 3 points week-over-week; owner: AI governance team; escalation: model risk committee.
  - Citation-precision sampling; sampling cadence weekly (50 cases); ground-truth pipeline: SME review; threshold drop greater than 3 points; owner: AI governance team; escalation: model risk committee.
  - Refusal-rate dashboard segmented by query class; sampling cadence continuous; ground-truth pipeline: golden-set replay against the labelled out-of-scope set monthly; threshold any drop greater than 5 points on the firm-confidential class; owner: AI governance team; escalation: CISO function jointly with AI Governance Lead.
  - Retrieval-source audit (continuous logging, weekly review for source-distribution drift); ground-truth pipeline: rule-based detection on per-source retrieval frequency; threshold ±20% drift week-over-week on policy-library share; owner: AI governance team with Policy Management; escalation: model risk committee.
  - Retrieval latency p50 / p95 / p99; sampling cadence continuous; ground-truth pipeline: automated; threshold p99 > 1.5s for any rolling-15-minute window; owner: platform engineering with AI governance; escalation: platform engineering then AI Governance Lead.
  - Foundation-model version monitoring; sampling cadence continuous; ground-truth pipeline: vendor change-of-version notice plus version-string check; threshold any change; owner: vendor management; escalation: AI Governance Lead, with re-run of this review per change-management table.

- **Residual risk** — four concrete items:
  - Stale-policy answer where the policy library refresh lag exceeds two weeks. Likelihood: medium (lag is a known operational pattern). Impact: medium (analyst output may inform customer-facing communications; UDAAP-relevant if it lands in customer communication). Owner: AI Governance Lead with Policy Management; quarterly review.
  - Citation precision below threshold on regulatory-text subsections. Likelihood: medium. Impact: medium-to-high (analyst reliance on a wrongly-cited subsection in a compliance context). Owner: AI Governance Lead; review on every citation-enforcement mitigation update.
  - Retrieval-bias not assessed. Likelihood: unknown. Impact: unknown. Owner: AI Governance Lead; not accepted; remains an open finding pending baseline assessment.
  - Foundation-model swap shifts faithfulness or refusal behaviour. Likelihood: medium (change-of-version cadence is approximately monthly per vendor public roadmap). Impact: medium. Owner: AI Governance Lead jointly with vendor management; review on every change-of-version notice.

- **Recommended owner actions** — seven gaps with owner role, deadline, severity:
  - Close context_precision threshold gap on policy-lookup queries through reranker tuning and corpus enrichment. Owner: AI governance team; deadline: pre-prod gate plus 30 days; severity: high.
  - Close context_recall and faithfulness threshold gaps on scenario queries. Owner: AI governance team; deadline: pre-prod gate plus 30 days; severity: high.
  - Enhance citation enforcement to subsection precision. Owner: AI governance team; deadline: pre-prod gate plus 45 days; severity: high.
  - Improve refusal behaviour on firm-confidential class. Owner: AI governance team; deadline: pre-prod gate plus 30 days; severity: medium.
  - Implement freshness gate at retrieval (filter out policy versions superseded after the current effective date). Owner: AI governance team with Policy Management; deadline: within 60 days of go-live; severity: medium.
  - Establish retrieval-bias baseline assessment by query type and corpus. Owner: AI governance team; deadline: annual revalidation; severity: medium.
  - Add `foundation_model_swap_revalidation` flag to change management. Owner: AI Governance Lead jointly with vendor management; deadline: pre-prod gate; severity: high.

- **Source trace and confidence** — vendor self-attestation results recorded at vendor confidence (low-to-medium); SME-adjudicated firm-internal results at high confidence; retrieval-bias assessment carries `[evidence needed]` until baseline runs.

- **Reviewer attestation** — pending; expected decision: accept-with-conditions, conditional on closing the high-severity threshold gaps and the citation-enforcement enhancement.

#### Why this scenario matters

- The scenario shows the per-source enumeration pattern: a single name ("compliance corpus") that splits into two sources of different freshness, provenance, and ownership. Rolling them up loses the freshness and provenance signal.
- Segment-level reporting on retrieval and grounding metrics is the spine. A single faithfulness number above the threshold can hide systematic failure on a query class; the worked example shows the segmentation surfacing the scenario-query gap.
- Citation precision defined as supports-the-claim is the load-bearing distinction. The vendor's headline citation-precision number was 1.0 on a contains-a-marker definition; the SME-adjudicated supports-the-claim definition surfaced a real gap.
- Refusal-rate evaluation requires a labelled out-of-scope set. The example treats the firm-confidential class as a separate label and surfaces a real refusal gap that the global refusal rate hides.
- The monitoring section names the ground-truth pipeline on every entry, not just the signal. Thumbs feedback is not in the table.

## troubleshooting

### Troubleshooting: rag-evaluation-review

Recurring defects from RAG evaluation reviews and how to address them. Read alongside the skill spec sheet's common-pitfalls list and the loaded sector and cross-cutting overlay common-pitfalls sections.

#### "Corpus" recorded as a single name when it is actually multiple sources

The most common review defect. The use case documents its "compliance corpus" or "claims corpus" or "research corpus" as a single name; the actual implementation indexes three or four sources of varying provenance, freshness, and ownership. Rolling them up loses the freshness, provenance, and ownership signal.

Fix: per-source enumeration is non-optional. Each row in `corpus_fitness[]` names one source by its system of record, with its own freshness, provenance, sensitivity, and owner. If the use case document calls it one corpus and the implementation has three sources, the review records three rows and notes the documentation gap as a recommended action.

#### Faithfulness reported as a single number with no segmentation

A single global faithfulness number above the threshold can hide systematic failure on a query class, a corpus, or a population segment. The headline number is comforting; the segment-level detail is the analytical work.

Fix: required segment-level reporting on at least query type and corpus for every grounding metric. Where the use case has a population dimension (customer segment, geography, line of business), add the population segmentation. The conduct overlay surfaces fairness segmentation as the load-bearing extension.

#### Refusal-rate measured but no labelled out-of-scope set exists

Refusal rate without a labelled out-of-scope test set is meaningless; the metric measures the rate at which the assistant refuses, but without a known-correct refusal target the rate has no reference.

Fix: refusal-rate evaluation requires a labelled out-of-scope test set documented in `dataset_ref`. If the dataset is absent or vague, the entry routes to recommended actions. The labelled set carries multiple classes (firm-confidential, off-corpus questions, questions about the assistant itself, scope-violating queries) with per-class labels; per-class refusal rates are the right segmentation.

#### Citation precision reported as 100% because every output contains a citation marker

Citation precision defined as "the output contains a citation marker" is meaningless; it measures formatting compliance, not whether the cited document supports the claim. This is a recurring failure mode; vendor-supplied citation-precision numbers are often defined this way.

Fix: citation precision must be defined as supports-the-claim, not contains-a-marker. The `metric_definition` field carries the definition explicitly. Method requires SME adjudication on a sample (typically a few hundred cases) where the SME judges whether the cited document section supports the claim, not whether a citation marker is present. Vendor-supplied citation-precision numbers are recorded at vendor-self-attestation confidence; firm-side SME-adjudicated numbers carry higher confidence.

#### Mitigations listed without evidence and without test coverage

A mitigation entry without an evidence pointer is policy, not a control. A mitigation entry with `exercised_in_test = false` is asserted coverage, not demonstrated coverage.

Fix: each `mitigations[]` entry requires an evidence pointer (config link, test report, change record, or `[evidence needed]`). Each entry needs `exercised_in_test` set explicitly. Mitigations marked `[evidence needed]` or `exercised_in_test = false` route to recommended actions, not silently into the memo body.

#### Residual risk recorded as "low" without basis

"Low" without a one-line basis is opinion. The residual-risk table requires likelihood, impact, and basis on every entry.

Fix: re-write each residual-risk entry with the basis populated. The basis names the controls that hold the likelihood down, the failure mode that drives the impact, and the assumption that fails first when the control set degrades. If the basis cannot be written, the rating is unsupported and routes to recommended actions for further analysis.

#### Monitoring relies on user-feedback thumbs only

Thumbs feedback from end users is sentiment, not ground truth. A monitoring section that lists thumbs as the primary signal is a dashboard, not a control programme.

Fix: every `monitoring[]` entry requires a `ground_truth_pipeline` populated. The pipeline is one of: sampled adjudication against SME judgement, golden-set replay against a labelled ground-truth set, automated scoring with a calibrated method, or rule-based detection with periodic SME calibration. Thumbs feedback can supplement (as a downstream-acceptance signal alongside adjuster-edit rate or analyst-edit rate) but does not substitute.

#### Stale-content answer treated as hallucination

A stale-content answer is a corpus-fitness failure (the corpus did not contain the current version) or a freshness-gate failure (the retriever returned a superseded version), not a grounding failure. Treating it as hallucination misses the framing and routes the residual-risk and recommended-action to the wrong owner.

Fix: stale-content answer is its own failure-mode row, with the freshness gate as the linked mitigation. The corpus-fitness section names the refresh cadence and the known lag. The mitigation includes the freshness gate (filter out versions superseded after the current effective date) where the use case can support that filter.

#### Per-customer or per-claim scoping asserted at the prompt layer rather than the retriever layer

Prompt-layer scoping is bypassable; an injected instruction in retrieved content can extract or reference data outside the intended scope. Retrieval-layer scoping is structural; the retriever cannot return content outside the scope by construction.

Fix: the review confirms the layer at which scoping is enforced. Prompt-layer-only scoping is a finding for any use case touching regulated personal data (NPI, PHI, MNPI). The recommended-action names the retrieval-platform owner and the implementation path.

#### Retrieval-bias not assessed

Retrieval-bias is the canonical fairness question for RAG systems with a population dimension: does retrieval surface representative content across populations? The default behaviour of dense-vector retrievers can favour content that is well-represented in the training corpus, which can correlate with demographic attributes.

Fix: where the use case has a population dimension and the conduct overlay loads, retrieval-bias assessment is non-optional. Annual reassessment at minimum; continuous monitoring for high-volume customer-facing use cases. Method is documented in the firm's fair-lending or fairness-monitoring methodology; the residual-risk acceptance carries a basis.

#### Foundation-model swap re-validation flag missing

For any architecture depending on a third-party foundation model, the standard recommended-action item that fires is the foundation-model swap re-validation flag in change management: an explicit re-run of this review on every vendor change-of-version notice. A vendor model swap can shift faithfulness, refusal behaviour, and citation patterns and invalidate the residual-risk view.

Fix: confirm the recommended-actions section includes the foundation-model swap re-validation item. If the foundation-model versioning posture is rolling-with-notice, additionally surface a recommended action to move to pinned versioning for tier-1 and tier-2 use cases.

#### Vendor evaluation results presented as firm-side coverage

Vendor-supplied evaluation results test the vendor's foundation-model and the vendor's evaluation pipeline against the vendor's test set. They do not test the firm's prompt template, the firm's corpus, the firm's retrieval scoping, or the firm's intended-purpose-tied thresholds.

Fix: the metric entries record the source explicitly. Source-trace entries record vendor evidence at vendor-self-attestation confidence (typically low to medium). Recommended actions surface firm-internal evaluation gaps as `[evidence needed]` items.

#### Cross-scope leakage treated as hallucination

Cross-scope leakage (cross-customer, cross-claim, cross-policy, cross-account) is a privacy event, not a model issue. Treating it as a hallucination misses the framing and routes the response posture to the wrong runbook.

Fix: cross-scope leakage is a separate failure-mode row with a privacy framing. A confirmed event triggers the privacy overlay's incident-response framing and the regulator-notification trigger evaluation. The mitigation set centres on retrieval-layer scoping; the monitoring set centres on rule-based detection plus SME spot-check.

#### Adjacency to prompt-injection-risk not surfaced

Indirect injection through corpus content is the prompt-surface seam to a RAG system. This skill catalogues the grounding-side failure mode (off-corpus answer, citation fabrication driven by injected content); the focused threat-surface review lives in `prompt-injection-risk`.

Fix: confirm a `prompt-injection-risk` review is on file or in flight for the same use case. The recommended-actions section names the adjacency. The cyber overlay carries the framing.

#### OCR-driven retrieval miss treated as an OCR engineering issue

OCR-driven retrieval miss on poor-scan documents (legacy medical records, scanned policy documents, handwritten notes) is a corpus-fitness issue, not just an OCR engineering question. Documents below the OCR confidence threshold are corpus-incomplete documents.

Fix: the OCR confidence gate is part of the corpus-fitness control set. Sub-threshold documents flag for human OCR review or re-processing before inclusion in retrieval. The monitoring section includes OCR confidence trend as a signal; ingestion-pass-rate drift is a leading indicator.

#### Sector overlay loaded but the sector-specific seam not surfaced

Each sector overlay carries seams the RAG evaluation review tends to miss without the overlay (banking BSA officer involvement; insurance HIPAA minimum-necessary at retrieval; capital markets information-barrier enforcement at retrieval; payments-fintech sponsor-bank shared-responsibility allocation). Loading the overlay without surfacing the seam in the review is the failure mode.

Fix: re-read the loaded sector overlay against the review and confirm each named overlay-specific consideration is reflected in the corpus-fitness, mitigations, monitoring, or recommended-actions sections.

#### Engagement scope not formalised

When the scope record is not supplied and the practitioner declines to formalise scope, the review still proceeds against a default public posture but should record the omission.

Fix: the review-metadata section notes that scope was not formalised; the recommended-actions section includes formalising scope as a low-or-medium-severity item; the source-trace confidence labels reflect the lack of formalised scope on items that would have been resolved by it.
