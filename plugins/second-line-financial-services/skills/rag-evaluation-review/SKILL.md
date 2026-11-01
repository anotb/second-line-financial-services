---
name: rag-evaluation-review
description: "Review retrieval and grounding evaluation for a RAG-based GenAI use case at a regulated firm."
argument-hint: "[use-case ID, model-card record, validation-plan record, vendor evaluation report, firm evaluation report, monitoring evidence, or scope statement]"
---

# RAG evaluation review

A RAG evaluation review is the second-line judgement on whether a retrieval-augmented GenAI system can be relied on for its stated use. The work names the corpus the system actually retrieves over (per source, not per label), the metric framework used to evaluate retrieval and grounding (with semantics documented), the failure modes catalogued, the mitigations in place with evidence, the residual risk with framing, the production monitoring with a ground-truth pipeline, and the gaps that need to close. The reliance assertion is the headline; everything else supports it.

Three regulator perspectives sit on this work and they need to be kept distinct. The US interagency model-risk guidance (the joint OCC/FRB/FDIC revised guidance issued April 2026) carries binding language for in-scope statistical and quantitative models at supervised banks; that guidance expressly excludes generative AI and agentic AI from its scope, so a RAG system is not within it. Where the firm's model risk programme treats the RAG use case as a model by analogy, the principles still inform but the binding hook is firm policy, not the bulletin. The AI-specific framings (NIST AI RMF, NIST AI 600-1, ISO/IEC 42001) are voluntary and leading-practice; they are the substantive anchors for grounding evaluation, retrieval quality, and corpus governance. The metric family in widest practitioner use (the RAGAS-style families: faithfulness, answer relevance, context precision, context recall) is **industry practice, not regulator language**; no US financial-services regulator names these metrics in published guidance. Any equivalent named framework or in-house equivalent is acceptable as long as the metric semantics are documented. Be explicit in the review about which expectations carry binding regulator language and which carry industry-practice weight; over-claiming on either side is a finding.

The audience reads from three angles. The AI Governance Lead owns the artefact and consolidates the analysis. The MRMO function inherits the model-risk seam and challenges the residual-risk view; for any in-scope use case the MRMO is a co-acceptor on residual risk. The model owner is the source of upstream evidence (model card, validation plan, vendor evaluation results, monitoring data) and is the operational counterpart for the recommended actions.

The memo is a draft until the human reviewer attests. The skill stops short of filing or approving it.

## When to use

Reviews the retrieval and grounding evaluation for a RAG-based GenAI use case in a regulated financial-services firm. Confirms the corpus is fit for the intended purpose, retrieval quality is measured with named methods on a labelled set, grounding (faithfulness, citation precision, refusal on out-of-scope queries) is tested with documented metric semantics, failure modes are catalogued, mitigations are evidenced, and ongoing monitoring runs against a real ground-truth pipeline. Output is a second-line memo on whether the RAG implementation can be relied on for the use case's intended purpose, with named gaps, residual-risk framing, and owner actions.

Best for:
- A first-line owner has built a RAG system and second-line needs an evaluation review before pre-prod, expansion, or annual revalidation.
- A foundation-model swap or a retrieval-stack change has happened and the grounding evaluation needs to be re-confirmed.
- An incident on hallucination, off-corpus answer, or cross-scope leakage has surfaced and the committee needs an updated grounding posture.
- An exam-readiness motion needs the firm's RAG-evaluation posture documented for a defined population of GenAI use cases.

Not the right tool when:
- The system has no retrieval; use validation-plan with the GenAI testing block.
- The work is the prompt-injection threat-surface review; use prompt-injection-risk. The two skills sit side by side for a RAG agent and reference each other.
- The work is the corpus access-control review only; use the cyber and privacy overlays inside vendor-diligence or genai-pre-prod-review.
- The work is the firm-side governance card for the use case; use model-card-builder. This skill consumes the card and produces the focused memo.

## Ask first

Most of what the review needs is already on the table by the time someone reaches for this skill. A few things to settle before drafting.

- What is the architecture, and where does the review draw its scope. Foundation model and version pinning posture, retriever type, corpora indexed, scoping rules, downstream consumers. If `model-card-builder` has run, the system-description and GenAI-overlay sections of the card name this; consume the card.
- Where is the use case in lifecycle, and what triggered this review. Pre-prod-gate review consumes vendor-supplied evaluation results and projects the firm-internal coverage gap. In-prod-periodic review consumes production-monitoring evidence and re-calibrates residual risk. Post-foundation-model-swap or post-retrieval-stack-change review re-runs the grounding-evaluation block against the new configuration. Post-incident review reframes around the incident pattern. Annual revalidation rolls all of these together.
- What is the use case's intended purpose, and what reliance does it support. The reliance assertion is what the residual-risk framing and the metric thresholds are calibrated against. A back-office analyst-support use case carries different thresholds than a customer-facing communication use case; the conduct overlay carries the framing for the latter.
- Who is co-reviewing. The MRMO is a co-acceptor on residual risk for any in-scope use case. Where the corpus contains regulated personal data, the privacy officer is a co-reviewer; where the use case is customer-facing or decision-support, consumer compliance or the fair-lending function is in the room; where the use case touches AML alert work, the BSA officer is in the room.
- What sector and cross-cutting overlays load. Banking, insurance, capital markets, or payments-fintech as sector; privacy as the default cross-cutting overlay (most regulated-FS RAG corpora contain regulated personal data); cyber and conduct as additional cross-cutting overlays where the scope flags them.

When the scope record is supplied, the skill consumes it for institution, persona, source posture, sector and cross-cutting overlays, lifecycle stage, and architecture flags. Otherwise it asks the practitioner the few facts it needs, and source posture sets what the memo can assert at high confidence and what carries `[evidence needed]`.

## How the memo gets filled in

The memo has the same spine across architectures. The order below is the dependency chain a senior practitioner walks; sections without dependencies fill in as evidence arrives.

Tier and architecture drive depth, so consume the model card and the scope record before deciding how heavy any section sits. Corpus enumeration must happen before retrieval-quality scoping (segmentation by corpus only works once the corpora are individually named). Retrieval quality must be in hand before grounding evaluation is interpreted (a grounding miss can be a retrieval miss in disguise). Mitigation evidence must be in hand before residual-risk framing (residual risk is the gap between the failure modes and the mitigations that hold them down).

**Review metadata** names the reviewer role, the review stage (pre-prod-gate, in-prod-periodic, post-incident, post-foundation-model-swap, post-retrieval-stack-change, annual-revalidation, exam-readiness), the date, and the upstream artefact IDs (scope, model card, validation plan). Reviewer roles are functions, never named individuals.

**Use case reference and RAG architecture summary** lands the architecture facts: foundation-model provider and version pinning posture, retriever type, embedding model, reranker, corpus count, refresh-cadence summary, scoping rules. The intended purpose is named; the reliance assertion downstream is judged against it. A pointer to the model card's system description is preferable to restating; the RAG memo is not the place to re-derive architecture.

**Corpus fitness** is per source, not per label. A "corpus" documented as a single name but actually three sources of varying provenance and freshness records as three rows. Each row carries source (system of record), freshness (refresh cadence, last refresh, known lag), coverage assessment (fit against the intended purpose, with named gaps), sensitivity (per the data-category enum, with the privacy-overlay tagging applied where the overlay loads), provenance (per-document tagging posture and basis), owner (function), and access controls (retrieval-side enforcement; pointer to the cyber overlay if applicable). The coverage assessment is the second-line judgement on whether the corpus actually answers the use case's intended question space; named gaps carry more analytical weight than asserted "coverage".

**Retrieval quality evaluation** records the retrieval-side metrics (the practitioner-standard families: context precision, context recall, retrieval latency; reranker lift and scoping correctness where applicable). Each entry carries the metric, a plain-language definition, the method (framework named with version where relevant; LLM-judge basis if used), the dataset reference (the labelled held-out set, named explicitly), the segmentation (by query type, by corpus, by population dimension where the use case has one), the headline result, the acceptance threshold tied to the intended purpose, the evidence pointer, and the owner. A single number with no segmentation hides systematic failure on a query class; required reporting at minimum is by query type and corpus.

**Grounding evaluation** records the grounding-side metrics (the practitioner-standard families: faithfulness, answer relevance, citation precision, refusal rate on a labelled out-of-scope set; hallucination rate and stale-content rate where measured). Each entry carries the same fields as retrieval quality. Two definitions are load-bearing: citation precision must be defined as the cited document section supports the claim, not as the output contains a citation marker (the contains-a-marker definition is meaningless for second-line review purposes); refusal rate requires a labelled out-of-scope test set in the dataset reference (refusal rate measured without a labelled set is meaningless and routes to recommended actions).

**Failure modes catalogued** records each observed or anticipated failure with frequency (rate, basis), example (anonymised pattern), and linked mitigation. The baseline set is hallucination, off-corpus answer, citation fabrication, stale-content answer, retrieval bias, cross-scope leakage; OCR-or-parsing miss for systems with OCR-driven retrieval; refusal failure on out-of-scope and over-refusal on in-scope as two-sided failure modes. Failure modes not applicable to the architecture record as "not applicable" rather than omitted.

**Mitigations in place** record each control with type, owner, evidence pointer, and whether the mitigation was exercised in any evaluation run. A mitigation without an evidence pointer is policy, not a control. A mitigation listed but not exercised in any evaluation run is recorded with `exercised_in_test = no` and routed to recommended actions; do not treat it as coverage.

**Monitoring** records each production signal with sampling cadence, ground-truth pipeline (sampled adjudication, golden-set replay, SME review, automated scoring), threshold, owner, and escalation path. User-feedback thumbs alone is not a monitoring programme; a ground-truth pipeline at a defined cadence is required. The baseline signal set for a typical RAG system is faithfulness sampling, citation-precision sampling, refusal-rate dashboard, retrieval-source audit, retrieval latency, foundation-model version monitoring, corpus refresh-cadence monitoring; for systems with regulated-personal-data corpora add cross-scope leakage detection; for OCR-driven retrieval add OCR confidence trend.

**Residual risk** names each concrete residual risk with likelihood, impact, basis, accepted owner role, accepted date, and review cadence. "Low" without a basis is opinion. Cross-reference any failed acceptance threshold in retrieval quality, grounding evaluation, or failure modes to a residual-risk row; an unaccepted threshold breach is itself a finding.

**Recommended owner actions** name each gap with owner role (function), deadline, severity, and any depends-on. Severity is the second-line judgement, not the owner's. Critical-severity items typically block pre-prod sign-off. The standard recommended-action item that fires for any architecture depending on a third-party foundation model is the foundation-model swap re-validation flag in change management, with explicit re-run of this review on every change-of-version notice.

**Source trace and confidence** records every material claim, its source, the evidence pointer, and a confidence label. Vendor-supplied evaluation results carry vendor-self-attestation confidence (typically low to medium); firm-internal SME-adjudicated results carry higher confidence. Do not collapse vendor and firm evidence into one line. Items without evidence carry `[evidence needed]` and route to recommended actions.

Depth flexes with tier and audience. A pre-prod-gate review for a tier-2 analyst-support assistant compresses to a few pages of substance with weight on the corpus-fitness and grounding-evaluation sections; a tier-1 customer-facing or decision-support review with conduct overlay can run long and dense. An in-prod-periodic review compresses on threat-surface enumeration (architecture is settled) and expands on monitoring evidence and residual-risk recalibration. Empty named sections are not acceptable, but compression is.

## Sector and cross-cutting overlays

When the scope names a sector (banking, insurance, capital markets, payments-fintech), load the matching `references/sector-overlays/<sector>.md`. Each overlay carries sector-specific corpora considerations, mitigations, monitoring signals, regulator-notification triggers, and co-reviewer expectations. The overlay's named additions land in the memo; treating the overlay as background reading is the failure mode.

The privacy cross-cutting overlay should be considered the default for most regulated-FS RAG reviews. Most corpora contain regulated personal data of one form or another (NPI, PHI, MNPI), and the corpus-governance and minimum-necessary framings are load-bearing. The overlay carries the data-category tagging convention, the retrieval-side minimisation framing, the cross-scope-leakage incident framing, and the regulator-notification triggers per applicable regime.

The cyber cross-cutting overlay loads where the scope flags it. For a RAG system the cyber framings are corpus access control, retrieval-side authentication and authorisation, and the indirect-injection adjacency to `prompt-injection-risk`. This skill catalogues the grounding-side failure mode (off-corpus answer, citation fabrication driven by injected content); the focused threat-surface review lives in `prompt-injection-risk`. The two skills work side by side for a RAG-using GenAI system.

The conduct cross-cutting overlay loads where the use case has a population dimension or where outputs flow into customer-facing communications. The overlay extends the segmentation requirement on retrieval and grounding metrics to include fairness segmentation and surfaces UDAAP, Marketing Rule, and fair-lending framings as load-bearing seams.

Climate is not applicable.

Load only the overlays the scope names. Gold-plating with overlays the engagement does not implicate adds noise without challenge value.

## Quality bar

The memo is only credible when these hold:

- Every material claim cites a source. Unsupported items carry `[evidence needed]` and route to recommended actions, not silently into the memo body.
- Evidence is separated from inference. Vendor-supplied evaluation results are not the same line as firm-internal SME-adjudicated results; vendor self-attestation confidence is recorded explicitly.
- No fabricated regulatory facts. Unknown section references carry `[verify section]` in the source-anchors file (not in the memo body).
- Per-source corpus enumeration is non-optional. A "corpus" that is actually multiple sources records as multiple rows.
- Citation precision is defined as supports-the-claim, not contains-a-marker. The metric definition field carries the documentation.
- Refusal rate requires a labelled out-of-scope test set. Without it the metric is meaningless and routes to recommended actions.
- Segment-level reporting on grounding metrics covers query type and corpus at minimum; population dimension where the use case has one.
- Mitigations without evidence pointers route to recommended actions. They do not count as coverage.
- Residual risk carries likelihood, impact, and basis. Rating without basis is opinion.
- Monitoring entries carry all five fields (signal, sampling cadence, ground-truth pipeline, owner, escalation path). User-feedback thumbs alone is not a ground-truth pipeline.
- Foundation-model swap re-validation is a non-optional recommended action for any architecture depending on a third-party foundation model.
- The grounding-evaluation metric vocabulary is industry practice, not regulator language. The review does not over-claim binding regulator endorsement of any specific metric framework; it cites the underlying validation expectations and applies the practitioner-standard framing.
- No named institutions outside finalised public enforcement actions; examples are anonymised and public-source-derived.
- Reviewer roles are functions, never named individuals.
- The memo is a draft until the human reviewer attests. The skill does not file the memo, post to the AI risk committee, or trigger an incident-response runbook.

## Adaptation

Tier drives depth. Lifecycle stage drives which sections lean heavy. Audience drives tone (working group is plain, committee is structured, examiner response is formal, board distillation pulls residual risk and recommended actions to the front). Sector and cross-cutting overlays load from the scope. Source posture sets what the memo can assert at high confidence and what carries `[evidence needed]`. Where firm-specific policy or taxonomy applies (named metric framework, named ground-truth pipeline, named owners), it lives in `references/firm-overlay.md` (consumed when present) and never in the memo directly.

## Output

Default to drafting the memo against `templates/default-output.md`. Render as Word for committee review, or another format the audience asks for. Produce the structured record at `schemas/rag-evaluation-review.schema.json` when downstream consumers (`genai-pre-prod-review`, `board-ai-risk-pack`, `ai-governance-reviewer`) need it. The reviewer-attestation block is filled by the human reviewer (AI Governance Lead with MRMO co-acceptance for in-scope use cases; co-acceptors per sector and cross-cutting overlay where applicable); the memo is filed only after.

Downstream consumers: `genai-pre-prod-review` consumes the structured object for the gate decision; `board-ai-risk-pack` pulls the residual-risk summary and the recommended-actions list; the `ai-governance-reviewer` agent pulls the structured object for second-line challenge; the firm's model risk programme consumes the review as input to the validation file. The schema is the input contract for those consumers; additive changes only.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/{banking,insurance,capital-markets,payments-fintech}.md` — sector overlays loaded from scope.
- `references/cross-cutting/privacy.md` — privacy overlay, the default cross-cutting overlay for regulated-FS RAG reviews.
- `references/cross-cutting/cyber.md` — cyber overlay; loads alongside privacy where the scope flags it; carries the indirect-injection adjacency to `prompt-injection-risk`.
- `references/cross-cutting/conduct.md` — conduct overlay; loads where the use case has a population dimension or feeds customer-facing communications.
- `references/firm-overlay.md` — firm policy, taxonomy, named metric framework, named owners (consumed when present).
- `templates/default-output.md` — memo template.
- `schemas/rag-evaluation-review.schema.json` — structured-output contract.
- `examples/` — anonymised public-source-derived scenarios (compliance-policy assistant; insurer claims-summary assistant).
- `TROUBLESHOOTING.md` — recurring defects.

## Human review and AI disclosure

Open the deliverable with this line, and remove it only after the review below: `AI-assisted draft. Requires review by a qualified person before use.`

A qualified person with authority to change the output reviews it before it is delivered or relied on, and stays accountable for it. Where the output supports advice to an individual or a decision about an individual (credit, insurance underwriting, pricing or claims, employment, legal rights, or similar), that individual must be told AI was used to produce it. This skill does not make final decisions, file with a regulator, notify customers, execute transactions, or move money or other financial assets.
