# Example: RAG evaluation review for a compliance-analyst policy assistant

Public-source-derived. No named institution. Pattern aligns with the spec sheet's first scenario.

## Input description

A US bank holding company is approaching the pre-prod gate for a RAG-based assistant for compliance analysts. The assistant retrieves over the firm's internal compliance policy library and a vendor-supplied regulatory-text database, then drafts answers with citations for the analyst to review. No tools enabled. Foundation model is vendor-hosted with version pinning and contractual change-of-version notice.

Engagement scope provided by `engagement-scoping`:
- Institution type: bank holding company, mid-cap, primary regulators FRB and CFPB; OCC for the national-bank subsidiary.
- Persona: AI Governance Lead (second line), with MRMO as model-risk co-reviewer.
- Sector overlay: banking. Cross-cutting overlays: privacy (some policy documents reference NPI handling procedures), cyber (corpus access controls), conduct (analyst answers may inform customer-facing communications downstream).
- Source posture: public-plus-firm-policy-plus-system-of-record-evidence.
- Tier: tier-2.

Upstream artifacts: `model-card-builder` output is on file; `validation-plan` outcomes-analysis block is partially complete (vendor self-attestation results landed; firm-internal held-out analyst query set is in evaluation).

## Output sketch

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

## Why this scenario matters

- The scenario shows the per-source enumeration pattern: a single name ("compliance corpus") that splits into two sources of different freshness, provenance, and ownership. Rolling them up loses the freshness and provenance signal.
- Segment-level reporting on retrieval and grounding metrics is the spine. A single faithfulness number above the threshold can hide systematic failure on a query class; the worked example shows the segmentation surfacing the scenario-query gap.
- Citation precision defined as supports-the-claim is the load-bearing distinction. The vendor's headline citation-precision number was 1.0 on a contains-a-marker definition; the SME-adjudicated supports-the-claim definition surfaced a real gap.
- Refusal-rate evaluation requires a labelled out-of-scope set. The example treats the firm-confidential class as a separate label and surfaces a real refusal gap that the global refusal rate hides.
- The monitoring section names the ground-truth pipeline on every entry, not just the signal. Thumbs feedback is not in the table.
