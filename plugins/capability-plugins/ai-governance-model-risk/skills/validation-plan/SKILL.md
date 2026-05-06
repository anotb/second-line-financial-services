---
name: validation-plan
description: |
  Drafts the validator-side scope contract for an AI or model use case before testing starts. Sizes the work to tier, names the conceptual soundness, data review, outcomes analysis, robustness, fairness, and ongoing monitoring scope per pillar, and frames the effective challenge questions the model owner is expected to answer. Output is what the validator and the model owner agree to before validation executes.

  Best for:
  - A use case has cleared intake and tiering and validation is the next step before pre-prod or production approval.
  - An annual revalidation cycle needs a tailored plan rather than a copy-paste of last year's scope.
  - A vendor or foundation-model swap on an existing use case needs a delta-scoped revalidation plan.
  - A regulator request lands on a tier-1 or tier-2 model and the firm needs a documented validator scope to point to.

  Not the right tool when:
  - Validation has already executed and the work is the validation report write-up.
  - The use case has not been intaked or tiered (use ai-use-case-intake or ai-risk-tiering first).
  - The artifact required is the firm-side model card itself (use model-card-builder; this plan consumes the card and scopes the testing against it).
  - The artifact required is the full GenAI pre-prod gate review across people, process, and technology (use genai-pre-prod-review; this plan is the validator-side scope only).

  Anchored to: SR 11-7, OCC Bulletin 2026-13, NIST AI RMF, NIST AI 600-1 (Generative AI Profile), ISO/IEC 42001, EU AI Act Article 9 and Article 15. Citations and excerpts live in `references/source-anchors.md`.
argument-hint: "[use-case ID, model card, tiering output, prior validation report, vendor evidence, or scope statement]"
---

# Validation plan

A validation plan is the scope contract between the validator and the model owner before testing starts. It names what the validator will read against the model's design (conceptual soundness), what data and lineage will be reviewed, what tests will run with which datasets and success criteria (outcomes analysis), what attack classes and stress scenarios will be probed (robustness), what fairness and explainability work is in scope, what the validator expects to see in production once the model lands (ongoing monitoring), and what effective challenge questions the model owner is expected to answer with evidence. The plan is the artifact a model risk committee approves before the testing window opens, the artifact the validation report (phase 3) consumes as its scope contract, and the artifact a regulator is handed when they ask "how was this model independently challenged before it went live."

The plan serves both lenses. A 1.5-line model owner reads it to understand what evidence will be asked for and where the gaps are. A 2-line validator drafts it to set effective challenge boundaries before getting drawn into testing. The seam between the two is the effective challenge questions block and the source trace.

The plan is a draft until the validator and the model risk committee (or equivalent reviewer) attest. The skill stops at draft.

## Ask first

The work is recognisable enough by the time someone reaches for this skill that most of the inputs are on the table. A few things to settle before drafting:

- What tier is the model. Tier drives validation depth more than anything else; if `ai-risk-tiering` has not run, route there before scoping the plan.
- What validation type. Initial validation, annual revalidation, vendor-swap revalidation, off-cycle trigger, post-incident. The type drives which pillars carry weight; an annual revalidation of an unchanged in-production model leans heavy on outcomes analysis and monitoring, light on conceptual soundness, while a vendor-swap revalidation flips that pattern.
- What architecture. Traditional ML, foundation-model dependent, RAG, or agentic. Architecture flags drive the GenAI overlay block (vendor evidence in scope, prompt-injection and RAG-poisoning tests, foundation-model version monitoring) and the attack-class catalogue.
- Who reads the plan. The plan signs at the model risk committee or equivalent; for tier-1 models in OCC large-bank scope the validator independence expectation under 12 CFR Part 30 Appendix D applies, so the audience is structured. Working drafts are plain; committee plans are challenge-shaped; regulator response files are formal and full source-traced.

When the engagement-scope record is supplied, the skill consumes it for institution, persona, source posture, sector and cross-cutting overlays. Otherwise it asks the practitioner the few facts it needs and drafts against what is given. Source posture sets what the plan can assert at high confidence and what carries `[evidence needed]`.

## How the plan gets built

The plan has the same spine across model types. The order below has real dependency in places and reads as prose elsewhere.

Tier and validation type are read first; they drive depth across the three pillars. SR 11-7 §IV sets the three pillars (conceptual soundness, ongoing monitoring, outcomes analysis); the validator sets depth per pillar, not as a single label. A tier-1 in-house consumer-credit model on initial validation sets `full` across all three; a tier-2 vendor-hosted GenAI assistant on initial validation sets `targeted` on conceptual soundness (vendor evidence review substitutes for theory replication on the foundation model) and `full` on outcomes and monitoring; a tier-3 in-production model on annual revalidation sets `light-touch` on conceptual soundness and `targeted` on outcomes and monitoring.

Upstream artifacts come next, before any scope item is drafted: the `ai-use-case-intake` record, the `ai-risk-tiering` output, the prior model card via `model-card-builder` if one exists, the prior validation report if this is a revalidation, and the vendor evidence (system card, evaluation report, red-team summary, contract addenda) if the foundation model is third-party. Drafting outcomes-analysis or robustness scope without these in hand produces a plan that is re-worked at the first committee read.

**Conceptual soundness scope** is what the validator will read against the model's design. For a built-in-house model this is theory and design rationale, segmentation choice, alternatives considered, and the policy on proxies. For a vendor-opaque foundation model the work pivots: theory replication is not available, so vendor evidence review takes its place. The validator reads the published system card, the vendor evaluation report, the red-team summary, and any contract addenda, and grades the firm-side rationale for selecting that model over alternatives. The conceptual soundness pillar is where reviewers most often flag effective-challenge weakness; vendor opacity is not a reason to skip the work, it changes what the work is.

**Data review scope** covers training data, evaluation data, retrieval corpora, lineage to system of record, fitness for purpose, and exclusions (prohibited rating factors, fairness-sensitive proxies removed in prior reviews, fields outside lawful basis). For foundation-model training data, firm visibility is typically limited to vendor system-card statements; record this as a known limitation, not as a data-review failure. The exclusions check is what fair-lending integration keys off when the model is in scope of ECOA / Reg B.

**Outcomes analysis scope** is the test catalogue. Each entry names the test, the method, the dataset, the segment cuts, the success criterion in firm-policy units, the owner, and what it benchmarks against (challenger model, prior version, vendor benchmark, external reference). Deployed-environment metrics dominate where the model is in production; lab-only metrics carry separately and are labelled. For traditional ML: KS, AUC, capture rate, segment-level performance, override analysis. For GenAI: faithfulness, citation precision, refusal rate, hallucination rate, agent-edit rate (when human-in-the-loop), latency, plus task-specific metrics. The validator's outcomes-analysis pillar must finish before robustness work; the failure mode is moving to robustness without a baseline against which to measure degradation.

**Robustness, adversarial, and stress testing scope** is tied to architecture flags. This is the recurring defect: the plan misses the most relevant attack class. For traditional ML: out-of-time backtest, stress scenario, segment robustness, adversarial input. For RAG: add direct prompt injection, indirect prompt injection on retrieved content, and RAG poisoning. For agentic systems: add tool misuse and goal hijack. For vendor-hosted GenAI: add a vendor model-version swap drill (a deliberate test of what happens to performance when the vendor floats the underlying model). For execution algos in capital markets: align with SEC Rule 15c3-5 pre-trade controls and load `references/sector-overlays/capital-markets.md`. Each entry names the attack class, the method, the success criterion, and the owner.

**Fairness, explainability, and transparency scope** names the protected and policy-relevant dimensions, the metric, and the method's limitations. For credit decisioning under ECOA / Reg B, the validator's scope and the consumer-compliance fair-lending test plan reference each other but stay distinct artifacts; CFPB Circulars 2022-03 and 2023-03 set the adverse-action-reason quality bar for explainability output. For insurance pricing or underwriting, frame the test against unfair discrimination per state insurance code (NAIC Model #880 vocabulary) in addition to or in place of generic fairness vocabulary, and load `references/sector-overlays/insurance.md`.

**Ongoing monitoring scope** is what the validator expects to see in production once the model lands. Each entry names the metric, the threshold, the frequency, the owner, the escalation path, and a `revalidation_trigger` flag. All six fields. The trigger flag is what distinguishes the validator's monitoring view from the model owner's operational monitoring view; the same metric may appear in both, but the validator's view is the one that triggers a re-validation cycle when breached. Validator monitoring copy-pasted from the model card without re-grounding is the recurring defect; the model owner's operational monitoring is not the same as the validator's revalidation triggers.

**Effective challenge questions** are the plan's signature. Each names the design choice or assumption it interrogates, the expected evidence, and the owner of the response. SR 11-7 §IV.5 sets the effective challenge expectation: validators have sufficient stature, knowledge, and incentive to challenge the model. Compliance-theatre questions ("does the model meet our policy", "is the model fit for purpose") apply to every model and challenge nothing. Real challenge probes a specific design choice and a specific failure mode: "the agent-review gate is the only preventive control between the assistant output and the customer; what is the off-switch criterion if agent-edit rate falls below threshold for two consecutive months", "the override policy assumes underwriters override at less than five percent; what is the test for that assumption and what triggers a model retire decision if overrides drift above ten percent", "the vendor floats the underlying foundation model with thirty-day notice; what is the validator's drill and what is the rollback path."

**Dependencies and prerequisites** lists the access and evidence the plan needs in hand for testing to execute: data extracts and feeds, validation environment and replay capability, vendor evidence package, foundation-model card, upstream artifacts, and cross-function access (consumer compliance for fair-lending integration, information security for cyber tests, vendor management for vendor evidence chase). A plan that depends on access the engagement does not have flags it as `[evidence needed]` rather than asserting the access exists.

**Timeline, owner, deliverables** is plain. Milestones with dates and function-level owners; deliverables include the validation report (phase 3), the refreshed model card, the issue-log entries, and the pre-prod or production approval input.

**Source trace and confidence** records every material scope claim, its source, the evidence pointer, and a confidence label. Vendor self-attestation carries low to medium confidence; firm-independent evaluation carries higher confidence. Do not collapse vendor and firm evidence into one line. Items without evidence carry `[evidence needed]` and route to the engagement issue log.

Depth flexes per pillar with tier and validation type. The section list does not. A targeted revalidation may compress conceptual soundness to a paragraph; a full initial validation expands every section. Empty named sections are not acceptable, but compression is.

### GenAI overlay

When the model has a foundation model in the loop, or uses RAG, or uses tools, the GenAI overlay block fires. It lands inside the named sections rather than as a separate document:

- Conceptual soundness: foundation-model selection rationale, RAG architecture review, prompt design review, tool boundary review for agentic configurations, and the `vendor_model_card_review` step.
- Data review: retrieval corpora inventory, retrieval scoping rules, refresh cadence, and access controls on the corpora.
- Outcomes analysis: faithfulness, citation precision, refusal rate, hallucination rate against held-out reference data.
- Robustness: direct prompt injection, indirect prompt injection on retrieved content, jailbreak, RAG poisoning; for agentic, tool misuse and goal hijack; for vendor-hosted, the vendor model-version swap drill.
- Monitoring: foundation-model version monitoring, prompt-injection signal, retrieval-source audit, citation-precision sampling, agent-edit rate (when human-in-the-loop), customer complaint code drift, with `revalidation_trigger` set on the version-change and faithfulness-drift metrics.
- Effective challenge: at least one question on vendor change-of-version, one on RAG corpus integrity, one on tool-boundary control.

The overlay is mandatory once triggered. Skipping the indirect-prompt-injection test on a RAG plan, or skipping the vendor model-version swap drill on a vendor-hosted plan, is what a second-line reviewer flags first.

### Sector and cross-cutting overlays

When the engagement scope names a sector (banking, insurance, capital markets, payments-fintech), load the matching `references/sector-overlays/<sector>.md`. The overlay's named scope items land in the plan's sector-overlay-notes section; treating the overlay as background reading is the failure mode. Same pattern for the cross-cutting overlays this skill carries: cyber, privacy, conduct. Climate is not applicable to validation plans.

Load only the overlays the engagement scope names. Stuffing every overlay into a plan adds noise that the model risk committee then has to read past.

## What's load-bearing and what flexes

A handful of things do not flex:

- Every material scope claim cites a source. Unsupported items carry `[evidence needed]` and go to the engagement issue log.
- Evidence is separated from inference. Vendor self-attestation is not the same line as firm-independent evaluation.
- No fabricated regulatory facts. Unknown section references carry `[verify section]` in the source-anchors file (not in the plan body).
- The GenAI overlay fires when triggered. No skipping the indirect-injection or the vendor-version-swap drill on a plan that has a foundation model, a RAG corpus, or tool use.
- Effective challenge questions name the design choice or assumption they interrogate. Compliance-theatre wording does not satisfy the field.
- The plan is a draft until the validator and the model risk committee attest. The skill does not assert sign-off, file the plan, or open the testing window.

Everything else adapts to context. Tier and validation type drive depth per pillar. Architecture drives the attack-class catalogue and the GenAI overlay. Audience drives tone (working group is plain, committee is structured, regulator response is formal). Persona drives the review-gate machinery; tier-1 models in OCC large-bank scope key off 12 CFR Part 30 Appendix D independence expectations. Sector and cross-cutting overlays are loaded from the engagement scope. Where firm-specific policy or taxonomy applies (named system-of-record paths, named committees, internal model-risk-policy thresholds), it lives in `references/firm-overlay.md` (consumed when present) and never in the plan directly.

## Output

Two artifacts: the plan per `templates/default-output.md`, and the structured object per `schemas/validation-plan.schema.json`. The reviewer attestation block is filled by the human reviewer; the plan is filed only after.

Downstream consumers: the validation report skill (phase 3, in `ai-validation-and-monitoring`) consumes this plan as its scope contract; `model-card-builder` consumes the outcomes-analysis and monitoring blocks for the firm-side card refresh; the `ai-governance-reviewer` agent consumes the structured object for second-line challenge; the model risk committee approves it before testing executes. The schema is the input contract for those consumers; additive changes only, never silent renames. Breaking changes ship as a versioned migration with the consumers told in advance.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/{banking,insurance,capital-markets,payments-fintech}.md` — sector overlays loaded from engagement scope.
- `references/cross-cutting/{cyber,privacy}.md` — cross-cutting overlays loaded from engagement scope.
- `references/firm-overlay.md` — firm policy, taxonomy, named owners and committees (consumed when present).
- `templates/default-output.md` — plan template.
- `schemas/validation-plan.schema.json` — structured-output contract.
- `examples/` — credit-scoring ML annual revalidation; vendor-hosted GenAI customer-service initial validation.
- `TROUBLESHOOTING.md` — recurring defects.
