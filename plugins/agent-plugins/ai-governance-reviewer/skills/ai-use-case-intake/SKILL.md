---
name: ai-use-case-intake
description: |
  Turns a first-line AI or model use case description into a structured intake record at the front of the AI governance pipeline. Captures purpose, intended users, data sources, vendor and foundation-model dependencies, autonomy level, decision impact, regulatory exposure flags, proposed review gates, and the open questions a tier reviewer needs answered. The intake is the routing artifact downstream skills consume: ai-risk-tiering reads it to score the rubric, ai-act-triage reads it to scope Annex III overlap, model-card-builder reads it for system and data sections, validation-plan reads it to scope work, and the AI inventory of record consumes the structured object.

  Best for:
  - A first-line owner has proposed an AI use case and second-line needs the intake on file before tier, AI Act triage, or any downstream artifact is scoped.
  - An AI inventory refresh requires consistent intake metadata across in-flight, in-production, and decommissioned use cases.
  - A vendor-supplied AI tool is moving from POC to limited production and the firm needs the front-door record before the pre-prod gate.
  - A second-line reviewer is challenging a use case the business has been running off-inventory.

  Not the right tool when:
  - The use case is intaked already and the question is its risk tier (route to `ai-risk-tiering`).
  - The use case has cleared intake and tiering and the next artifact is the model card (route to `model-card-builder`).
  - The work is procurement-stage diligence on an AI vendor before any internal use case exists (route to `vendor-diligence` in `third-party-operational-resilience` with the AI-vendor scenario mode).
  - The artifact required is the EU AI Act Annex IV technical documentation (that is the provider-side file owned by the model provider; route to `ai-act-triage` to scope Annex IV deltas the firm carries).
argument-hint: "[use-case description, sponsor brief, vendor proposal, scope record, or scenario]"
---

# AI use case intake

The intake is the front door for everything else in the AI governance pipeline. Tiering decides depth, AI Act triage decides classification, the model card carries the artifact, validation scopes the work ... none of it is defensible if the intake under it is thin, ambiguous, or silent on what the use case actually does. Get the intake right and the rest of the pipeline runs against a record an examiner can read; get it wrong and every downstream artifact inherits the gap.

This skill produces a single intake record that downstream second-line workflows consume. The audience is the AI Governance Lead reviewing what the model owner has submitted, the second-line reviewer challenging what the business has been running, and the model owner carrying their use case into the pipeline. The record is short on purpose: the intake captures judgment-shaped facts about scope, exposure, and dependencies, not the validation evidence or the controls inventory. Those come downstream.

The intake is a draft until the AI Governance Lead (or named equivalent) attests. The skill stops short of filing into the inventory of record.

## Ask first

Most of what the intake needs is already on the table by the time someone reaches for this skill. A few things to settle before drafting:

- Who is the sponsor, and what stage is the use case in. A pre-build idea, an active POC, a limited-production deployment, and an already-running off-inventory tool need different evidence postures and different open-question lists. The same record shape; different confidence labels.
- What architecture. Traditional ML, foundation-model, RAG, agentic with tool use ... the answer fires the GenAI block (foundation-model identity and pinning posture, RAG corpus naming, tool inventory, autonomy uplift) and decides which sector and cross-cutting overlays load.
- What does the use case touch on the customer side. Internal-only with no customer surface, internal-only but processes customer data, customer-facing through staff intermediation, customer-facing directly. The answer drives the regulatory exposure flags and the preliminary tier suggestion.
- Which regulators reach the firm and the use case. Federal banking, state insurance, SEC and FINRA, CFPB, NYDFS, EU AI Act footprint, state privacy laws ... the regulators decide which sector and cross-cutting overlays carry weight in the intake.

When the scope record from `scoping` is supplied, the skill consumes it for institution, persona, source posture, sector and cross-cutting overlays, and primary regulators. Otherwise it asks the practitioner the few facts it needs and source posture sets what the intake can assert at high confidence and what carries `[evidence needed]`.

## How the intake gets filled in

The intake has the same spine across use case types. Walk it in the order the conversation surfaces; the structured object sorts itself. Two things are load-bearing in sequence: confirm the architecture before applying overlays (the GenAI block fires off architecture flags), and confirm regulator reach before flagging EU AI Act overlap (the AI Act flag is a routing decision into `ai-act-triage`, not a classification this skill makes).

**Identity and sponsor.** Use case ID and version, short human-readable name, sponsor business unit, accountable first-line owner (a role, never a named individual), AI Governance Lead reviewer. Lifecycle stage: idea, POC, limited production, full production, retirement. The version field exists because intake is a living record; downstream tier and card decisions are decided against an intake version, and a re-intake is recorded as a new version.

**Business purpose and target outcome.** One paragraph in plain language: what the use case does, what business outcome it supports, why this approach over the alternative. The target outcome anchors the validation conversation downstream; an intake that says "leverage AI to enhance productivity" tells nobody anything. Senior practitioners say what the use case actually does and what success looks like.

**Intended users and decision points.** Internal staff, customers, third parties, agentic callers from another system. Each user role names the decision the use case influences and where the human review point sits in the flow. A relationship-manager-facing assistant and a customer-facing chatbot are different use cases even when the underlying model is the same vendor LLM.

**Decision impact.** Customer impact, financial impact, regulatory impact, operational impact, each scored none / low / medium / high with a one-line basis. Customer impact covers customer-binding decisions, customer-facing surfaces, and indirect customer-outcome effects. Financial impact covers balance-sheet, capital, liquidity, and material P&L exposure. Regulatory impact covers named regulator reach. Operational impact covers process criticality and operational-resilience exposure if the use case fails. The scores carry into the tiering rubric; do not collapse to a single dimension.

**Autonomy level.** Human-in-the-loop, human-on-the-loop, fully automated, agentic with tool use. The autonomy level is not what the architecture diagram says; it is what the human review point actually does. A button-push approval where the human approves at scale without inspecting reads as human-on-the-loop or worse, not human-in-the-loop. The effective-human-oversight expectation in the AI frameworks frames this; where the evidence of effective oversight is thin, flag the autonomy level as an open question rather than over-claim.

**Architecture.** Model type (traditional, ML, foundation-model, agentic), deployment posture (in-house, vendor API, on-prem), foundation-model identity and version with pinning posture (pinned to a specific version, floating with vendor change-of-version notice, rolling without notice), RAG retrieval scoping rules and corpus names, tool inventory with the actions each tool can take. For foundation-model use cases, missing the foundation-model identity is what a downstream reviewer flags first; the model card cannot be drafted without it.

**Data sources and sensitivity.** Each source named with sensitivity tag (public, internal, confidential, regulated NPI under GLBA, regulated PHI under HIPAA, payment data under PCI, biometric, customer-supplied prompt content, children's data) and purpose (training, fine-tuning, retrieval, evaluation, monitoring, reference). Field-level tagging is required for any source flagged regulated; a "CRM extract" source hides regulated NPI inside an otherwise internal data source, and the tier reviewer cannot score data sensitivity off a source-level tag alone.

**Vendor and third-party dependencies.** Each vendor named with role (foundation-model provider, model-serving infrastructure, RAG infrastructure, evaluation provider, data provider), criticality (the operational-resilience criticality, not the model-risk tier), contractual posture for change-of-version notice, and the firm-side fallback if the vendor exits. Sponsor-bank arrangements are a vendor-dependence pattern with their own regulatory weight; flag those explicitly.

**Regulatory exposure flags.** Tags for the regulators and rules the use case touches. The flag set varies by institution and use case — bank model-risk supervisory expectations for traditional models, the AI-specific frameworks (NIST AI RMF, NIST AI 600-1, ISO/IEC 42001), EU AI Act Annex III categories where the firm or its customers reach the EU, state insurance AI bulletins, NYDFS cybersecurity reach, consumer-credit fair-lending exposure, securities marketing and recordkeeping rules, FFIEC manual reach for BSA/AML use cases, privacy frameworks where regulated personal data is in play. Each flag carries a one-line basis and a routing destination (which downstream skill consumes it). The flags are routing inputs, not enforcement claims; the named anchors live in `references/source-anchors.md`.

**Preliminary tier proposal.** A draft tier (tier-1 to tier-4) with one-paragraph rationale. The proposal is what the model owner thinks; the formal tier is decided downstream by `ai-risk-tiering` against the intake record. Sponsor pressure runs in both directions (down to skip validation depth, up to claim governance maturity); the dissent line in `ai-risk-tiering` records the disagreement when it stands.

**Proposed decision checkpoints and human oversight.** Named checkpoints: independent validation, AI risk committee approval, pre-prod gate, vendor diligence, monitoring cadence, complaint surveillance. Each names an owner (a function), a frequency, and a stop condition (what halts the use case if the checkpoint fails). The proposed checkpoints are an input to tiering; the firm's tier-to-checkpoint mapping is firm policy, set at tiering time.

**Open questions for second-line follow-up.** Each tagged with the downstream skill that needs the answer (`ai-risk-tiering`, `ai-act-triage`, `model-card-builder`, `validation-plan`, `agentic-ai-controls`, `vendor-diligence`). Open questions are not defects; they are the work-in-flight handoff to the downstream skill. A clean intake with an empty open-questions list either is a tier-4 use case with no exposure, or had its open questions sanitised. Senior reviewers look for the second case more than the first.

**Next twelve-month change plan.** Named owner, planned scope changes, planned autonomy uplift (e.g., adding tool use), planned customer-surface expansion, planned vendor changes. The intake is a record of today plus the planned roadmap; tier and gates set on a moving target without the change plan field drift within a quarter. A blank field with a recent intake date and an active use case is a tell that the conversation has not happened.

**Source trace and confidence.** Every material claim names the source (intake conversation, sponsor memo, vendor proposal, system design document, vendor system card, prior intake version, `[evidence needed]`), the evidence pointer, and a confidence label (high, medium, low, evidence-needed). Vendor-supplied facts about the vendor's own model carry vendor-self-attestation confidence (typically low to medium); firm-controlled facts carry higher confidence. Items without evidence either close before the intake is filed, or are accepted as open questions with an owner.

### GenAI overlay

When the architecture flags `model_type = foundation_model`, or `uses_rag = true`, or `uses_tools = true`, the GenAI overlay block fires inside the named sections rather than as a separate document. Specifically:

- Architecture: foundation-model provider, model name, version, pinning posture (pinned, floating, rolling-with-notice); RAG corpus names with retrieval scoping rules and refresh cadence; tool inventory with the actions each tool can take and the tool-boundary controls.
- Data sources: any retrieval corpus is itself a data source with its own sensitivity tagging; vendor-supplied corpora carry vendor-self-attestation confidence and a separate field-level review flag.
- Regulatory flags: GenAI use cases pick up the AI-specific framework anchors (NIST AI RMF and the GenAI Profile, ISO/IEC 42001) and, for NYDFS-covered entities, the October 2024 AI cybersecurity industry letter. EU AI Act GPAI obligations are a routing-to-`ai-act-triage` call, not a classification this skill makes.
- Open questions: foundation-model swap path, RAG corpus refresh and provenance, tool addition control flow, prompt-injection exposure, content-provenance posture. These tag to `validation-plan`, `prompt-injection-risk`, `rag-evaluation-review`, `genai-pre-prod-review`, `llm-vendor-evidence-review` as relevant.

The GenAI overlay is mandatory once triggered. Missing the foundation-model identity, the RAG corpus inventory, or the tool inventory on a GenAI intake is what `ai-risk-tiering` flags first when the record lands.

### Sector and cross-cutting overlays

When the scope names a sector (banking, insurance, capital-markets, payments-fintech), load the matching `references/sector-overlays/<sector>.md`. The overlay's named fields and regulatory flags land in the intake; treating the overlay as background reading is the failure mode. Same pattern for the cross-cutting overlays this skill carries: cyber, privacy, conduct. Climate is not applicable.

Load only the overlays the scope names. Gold-plating an intake with overlays the engagement does not implicate adds noise without challenge value.

## Quality bar

The intake is only credible when these hold:

- Every material claim cites a source. Unsupported items carry `[evidence needed]` and route to the open-questions list with a downstream-skill tag, not silently into the intake.
- Evidence is separated from inference. Sponsor assertion ("the autonomy is human-in-the-loop because there's a button") is not the same line as observed control evidence; record both with their own confidence labels.
- Foundation-model identity is named when a foundation model is in use. Pinned-versus-floating posture is named. RAG corpora are named. Tool inventory is named. The downstream pipeline cannot run without these, and the intake is where they get captured.
- Field-level data sensitivity is required for any source flagged regulated NPI, PHI, PCI, or biometric. Source-level tagging hides exposure inside aggregate sources.
- No fabricated regulatory facts. Unknown section references carry `[verify section]` in the source-anchors file (not in the intake body); regulatory tags carry their named source.
- No named institutions outside finalised public enforcement actions; examples are anonymised and public-source-derived.
- The intake is a draft until the AI Governance Lead attests. The skill does not file the intake into the inventory of record, route to tiering, post to the AI risk committee agenda, or notify regulators.

## Adaptation

Lifecycle stage drives which evidence weighs heaviest (intake on a POC reads from intent and design; intake on a running off-inventory tool reads from observed behaviour). Audience drives tone (AI Governance Lead intake review is technical; AI risk committee submission is structured; examiner-response file is formal). Persona sets the review path and the named decision owners. Source posture sets what the intake can assert at high confidence. Where firm-specific policy or taxonomy applies (firm tier names, firm decision checkpoints, named owners, firm AI inventory schema extensions), it lives in `references/firm-overlay.md` and never in the intake body directly.

## Output

Default to drafting the intake against `templates/default-output.md`. Render as Word for narrative review, or another format the audience asks for. Produce the structured record at `schemas/ai-use-case-intake.schema.json` because every downstream skill in the AI governance pipeline (`ai-risk-tiering`, `ai-act-triage`, `model-card-builder`, `validation-plan`, `agentic-ai-controls`, `vendor-diligence`, `genai-pre-prod-review`) consumes it. The reviewer attestation block is filled by the AI Governance Lead; the record is filed only after.

Downstream consumers: `ai-risk-tiering` reads the structured object to score the tiering rubric and decide tier, validation depth, monitoring cadence, and committee route. `ai-act-triage` reads the regulatory flags and architecture for Annex III overlap and the formal AI Act classification. `model-card-builder` reads architecture, data sources, autonomy, intended use, and intake metadata for the card sections. `validation-plan` reads architecture, data sources, decision impact, and the open-questions list to scope conceptual-soundness, data-quality, benchmarking, outcomes-analysis, and monitoring work. `agentic-ai-controls` reads autonomy level and tool inventory when the use case has tool privileges. `vendor-diligence` (in TPRM) reads the vendor dependencies block when the AI-vendor scenario mode runs. `genai-pre-prod-review` reads the full record for the pre-prod gate roll-up. The schema is the cross-skill contract; additive changes only, never silent renames. Breaking changes ship as a versioned migration with the consumers told in advance.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/{banking,insurance,capital-markets,payments-fintech}.md` — sector overlays loaded from scope.
- `references/cross-cutting/{cyber,privacy,conduct}.md` — cross-cutting overlays loaded from scope.
- `references/firm-overlay.md` — firm policy, taxonomy, named owners, AI inventory schema extensions (consumed when present).
- `templates/default-output.md` — intake-record template.
- `schemas/ai-use-case-intake.schema.json` — structured-output contract.
- `examples/` — public-source-derived scenarios: relationship-manager assistant at a regional bank; accelerated-underwriting model at a life insurer.
- `TROUBLESHOOTING.md` — recurring defects in intake records.
