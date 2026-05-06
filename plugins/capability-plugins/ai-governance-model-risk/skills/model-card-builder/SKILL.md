---
name: model-card-builder
description: |
  Drafts a model card for a financial-services AI or model use case, with named sections for intended use, training and reference data, performance, limitations and known failure modes, monitoring plan, controls, change management, and sign-off questions. The card is the firm-side governance artifact that supports model risk committee review, pre-prod gates, the model inventory of record, validator handoff, and regulator response files.

  Best for:
  - A first-line owner has proposed an AI use case and second-line needs the model card before a tier decision or pre-prod gate.
  - A model risk team is refreshing model cards as part of an annual model inventory exercise.
  - A new vendor model is replacing an existing one and the card needs to be updated to reflect the swap.
  - A regulator response file or examiner request requires the firm's documented view of an in-scope model.

  Not the right tool when:
  - The use case has not been intaked yet (use ai-use-case-intake first).
  - Validation testing has not run and there are no performance results to summarise (use validation-plan; the card consumes its outputs).
  - The artifact required is the EU AI Act Annex IV technical documentation. That is the provider-side file; the firm-side card sits alongside it. Use ai-act-triage to scope Annex IV deltas.

  Anchored to: SR 11-7, OCC Bulletin 2026-13, NIST AI RMF, NIST AI 600-1 (Generative AI Profile), ISO/IEC 42001, EU AI Act Article 11 and Annex IV. Citations and excerpts live in `references/source-anchors.md`.
argument-hint: "[use-case ID, intake record, validation report, monitoring evidence, vendor system card, or scope statement]"
---

# Model card builder

A model card is the firm-side governance artifact for an AI or model use case: intended use, system, data, performance, robustness, fairness, limitations, monitoring, controls, change management, sign-off questions, source trace. It is what the model risk committee reaches for, what the validator works against, what the pre-prod gate reviewer challenges, what the model inventory of record consumes, what an examiner is handed when they ask "what does this model do, where does it work, where does it fail, who is accountable, and what is monitored."

The card serves both lenses. A 1.5-line model owner uses the skill to consolidate the work as it stands today; a 2-line reviewer uses the same skill to challenge what was drafted. The seam between the two is the source-trace block and the sign-off questions.

The card is a draft until a human reviewer attests. Sign-off is the gate; this skill stops short.

## Ask first

Most of what the card needs is already on the table by the time someone reaches for this skill. A few things to settle before drafting:

- What tier is the model. Tier drives depth more than anything else; if `ai-risk-tiering` has not run, route there before building the card.
- Where is the model in lifecycle. Pre-prod cards lean on intended use, design rationale, and limitations. Production cards lean on monitoring evidence. Retirement cards lean on retention and audit trail. Same spine, different weights.
- Who reads it. A working-group draft is plain. A pre-prod committee card is challenge-shaped. A regulator response is formal and full source-traced. A board distillation pulls sign-off questions to the front.
- What architecture, and which overlays. Traditional ML, foundation-model, RAG, or agentic ... the answer triggers the GenAI overlay block (foundation-model dependence, RAG corpus, tool inventory, prompt-injection robustness, vendor change-of-version trigger) and decides which sector and cross-cutting overlays load.

When the engagement-scope record is supplied, the skill consumes it for institution, persona, source posture, sector and cross-cutting overlays, lifecycle stage, and architecture flags. Otherwise it asks the practitioner the few facts it needs, and source posture sets what the card can assert at high confidence and what carries `[evidence needed]`.

## How the card gets filled in

The card has the same spine across model types. The order below is roughly how a senior practitioner walks it; in practice the conversation surfaces sections in whatever order the evidence arrives, and the structured object sorts itself.

Tier drives depth, so consume the tier output before deciding how much weight any section carries. That order is load-bearing. Likewise, do not draft validation-related sections (performance, robustness, fairness) before the upstream `ai-use-case-intake` and `ai-risk-tiering` artifacts are in hand, and `validation-plan` outputs where they exist. Routing to those skills first is faster than re-doing the work.

**Metadata** names the model and version, owner, validator, second-line reviewer, date, tier, lifecycle stage, classification, and the upstream use-case and engagement-scope IDs. Owners are roles or functions, never named individuals.

**Intended use** sets purpose, intended users, the in-scope decisions, and the out-of-scope decisions. The out-of-scope list is what reviewers probe hardest; it is the firewall against scope drift after the model is in production.

**System description** covers model type and architecture, dependencies, autonomy level. For GenAI use cases, this is also where the foundation-model dependence, RAG corpus, and tool inventory land (see GenAI overlay below). Autonomy level is the input that drives the controls section.

**Training and reference data** lists each data source with purpose (training, fine-tuning, retrieval, evaluation, monitoring, reference), sensitivity (NPI, PHI, public, confidential), licensing, retention, lineage, and exclusions (prohibited rating factors, fairness-sensitive proxies, fields outside lawful basis). For foundation-model training data, firm visibility is typically limited to vendor system-card statements; record at appropriate confidence.

**Performance** reports segment-level results on protected and policy-relevant dimensions, even when overall performance is acceptable. Overall metrics alone hide segment exposure. Deployed-environment metrics dominate for production cards; lab-only metrics carry separately and are labelled. For GenAI: faithfulness, citation precision, refusal rate, latency, plus task-specific metrics.

**Robustness and stress testing** covers out-of-time backtests, stress scenarios, and segment robustness. For GenAI: prompt injection, jailbreak, and RAG poisoning tests, plus the vendor-supplied test set. For execution algos, the Rule 15c3-5 control overlap goes here (see capital-markets overlay).

**Fairness and explainability** names the protected and policy-relevant dimensions, the metric, the disparity assessment, and the method's limitations. For insurance pricing or underwriting, frame against unfair discrimination using NAIC #880 vocabulary in addition to or in place of generic fairness terminology; load the insurance overlay.

**Limitations and known failure modes** are concrete, each with an example. "Model may not generalise" tells a reviewer nothing. If you cannot give an example, surface the limitation as a sign-off question instead.

**Monitoring** entries each name a metric, threshold, frequency, owner, and escalation path. All five fields. The owner and the escalation path are what reviewers flag first; the chase across functions (consumer compliance owns complaint rate, infosec owns prompt-injection signal, vendor management owns version notice) is part of the work.

**Controls** are preventive, detective, response, or compensating. Each has a named owner and a pointer to evidence. A control without an evidence pointer is policy, not a control.

**Change management** lists the re-validation triggers: feature change, training-window shift, performance breach for N consecutive periods. For GenAI: foundation-model swap, RAG corpus scope change, tool addition, autonomy-level change. The card is a living document; foundation-model version monitoring is not optional once a vendor LLM is in the loop.

**Sign-off questions** are tagged to sections, answerable from the card itself, and specific to this card. "Is this fit for purpose" applies to every card and challenges nothing. "The agent-review gate is the only preventive control between the assistant output and the customer; what is the off-switch criterion if agent-edit rate falls below threshold for two consecutive months" applies to one card and one model.

**Source trace and confidence** records every material claim, its source, the evidence pointer, and a confidence label. Vendor system cards and vendor evaluations carry vendor-self-attestation confidence (typically low to medium); firm-independent evaluation carries higher confidence. Do not collapse vendor and firm evidence into one line. Items without evidence carry `[evidence needed]` and route to the engagement issue log.

Depth flexes with tier and audience. A short tier-4 card may compress sections to two or three lines apiece; a deep tier-1 card expands every section. Empty named sections are not acceptable, but compression is.

### GenAI overlay

When `architecture.foundation_model` is set, or `architecture.uses_rag` is true, or `architecture.uses_tools` is true, the GenAI overlay block fires. It lands inside the named sections rather than as a separate document:

- System description: foundation-model provider, name, version, pinning posture (pinned, floating, rolling-with-notice); RAG corpora named with retrieval scoping rules and refresh cadence; tool inventory with tool-boundary controls and autonomy level.
- Robustness: prompt injection, jailbreak, RAG poisoning test results.
- Monitoring: foundation-model version monitoring, prompt-injection signal, retrieval-source audit, citation-precision sampling, agent-edit rate (when human-in-the-loop), customer complaint code drift.
- Change management: vendor change-of-version notice, RAG corpus scope change, and tool addition are each re-validation triggers.

The overlay is mandatory once triggered. Missing the GenAI sections on a GenAI card is what a second-line reviewer flags first when the card lands for challenge.

### Sector and cross-cutting overlays

When the engagement scope names a sector (banking, insurance, capital markets, payments-fintech), load the matching `references/sector-overlays/<sector>.md`. The overlay's named fields and sign-off questions land in the card; treating the overlay as background reading is the failure mode. Same pattern for the cross-cutting overlays this skill carries: cyber, privacy, conduct. Climate is not applicable to model cards.

Load only the overlays the engagement scope names. Gold-plating a card with overlays the engagement does not implicate adds noise without challenge value.

## What's load-bearing and what flexes

A handful of things do not flex:

- Every material claim cites a source. Unsupported items carry `[evidence needed]` and go to the engagement issue log, not silently into the card.
- Evidence is separated from inference. Vendor self-attestation is not the same line as firm-independent evaluation.
- No fabricated regulatory facts. Unknown section references carry `[verify section]` in the source-anchors file (not in the card body).
- The GenAI overlay fires when triggered. No skipping it on a card that has a foundation model, a RAG corpus, or tool use.
- The card is a draft until the human reviewer attests. The skill does not assert sign-off, file the card, post to the inventory of record, or respond to a regulator request.

Everything else adapts to context. Tier drives depth. Lifecycle stage drives which sections lean heavy. Audience drives tone (working group is plain, committee is structured, examiner response is formal, board is distilled). Persona drives the review-gate machinery. Sector and cross-cutting overlays are loaded from the engagement scope. Where firm-specific policy or taxonomy applies, it lives in `references/firm-overlay.md` (consumed when present) and never in the card directly.

## Output

Two artifacts: the card per `templates/default-output.md`, and the structured object per `schemas/model-card.schema.json`. The reviewer attestation block is filled by the human reviewer; the card is filed only after.

Downstream consumers: `board-ai-risk-pack` pulls metadata, tier, intended use, performance and limitations summary, and material sign-off questions. `validation-plan` pulls architecture and data sections to scope validation work. The `ai-governance-reviewer` agent pulls the structured object for second-line challenge. The model inventory of record pulls the structured object for the central registry. The card itself is what an examiner is handed. The schema is the input contract for those consumers; additive changes only, never silent renames. Breaking changes ship as a versioned migration with the consumers told in advance.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/{banking,insurance,capital-markets,payments-fintech}.md` — sector overlays loaded from engagement scope.
- `references/cross-cutting/{cyber,privacy,conduct}.md` — cross-cutting overlays loaded from engagement scope.
- `references/firm-overlay.md` — firm policy, taxonomy, named owners (consumed when present).
- `templates/default-output.md` — card template.
- `schemas/model-card.schema.json` — structured-output contract.
- `examples/` — anonymised public-source-derived scenarios.
- `TROUBLESHOOTING.md` — recurring defects.
