---
name: ai-risk-tiering
description: |
  Assigns a defensible risk tier (tier-1 through tier-4) to an AI or model use case using a multi-factor rubric, and books the tier alongside the named gates and validation depth it triggers. The tier is the routing decision that drives validation depth, monitoring frequency, committee path, and vendor-diligence depth for the rest of model risk and AI governance.

  Best for:
  - An intake record exists and second-line needs to set the tier before sequencing validation, monitoring, or committee work.
  - A periodic re-tiering exercise on the AI inventory after a change in scope, autonomy, customer exposure, vendor, or supervisory posture.
  - A sponsor has proposed a tier and second-line needs to challenge or concur with reasoning that an examiner can read.

  Not the right tool when:
  - The use case has not been intaked yet. Route to `ai-use-case-intake` first; the tier decision is decided against an intake record version.
  - The question is whether the use case is high-risk under the EU AI Act specifically. Route to `ai-act-triage`; the AI Act has a regulation-driven classification, not a firm-defined rubric. This skill flags Annex III overlap as a routing trigger, not a determination.
  - The question is the validation plan itself. Route to `validation-plan`; this skill sets the depth, the next skill scopes the work.

  Anchored to: SR 11-7, OCC Bulletin 2026-13, NIST AI RMF, NIST AI 600-1 (Generative AI Profile), ISO/IEC 42001, EU AI Act.
argument-hint: "[use-case ID, intake record, engagement-scope record, or scenario]"
---

# AI risk tiering

The tier is the load-bearing decision in model risk. Validation depth, monitoring cadence, committee route, vendor-diligence depth, and which sign-offs an examiner expects to find all flow from it. Get it wrong on the low side and the firm under-controls a customer-binding model. Get it wrong on the high side and the bench drowns in tier-1 work that nothing distinguishes from anything else.

This skill produces a tier (tier-1, tier-2, tier-3, tier-4) with reasoning that an AI risk committee secretary or a model risk lead reads and an examiner can challenge. The output is short on purpose. Tiering is judgment, not artifact-padding; the spine is the named factors, the regulator constellation, and the dissent record where the second line disagreed with the sponsor.

The tier is a draft until the named decider attests. Sign-off is the gate; this skill stops short.

## Ask first

Most of what the tier needs is on the table by the time someone reaches for this skill. A few things to settle before scoring:

- Has the use case been intaked. If not, route to `ai-use-case-intake` first. The tier is decided against an intake record version, not a verbal scope.
- What does the sponsor propose. Sponsor pressure runs in both directions: pushing the tier down to skip validation depth, or pushing it up to claim governance maturity. Surface the proposal so the dissent line records the disagreement when it stands.
- What is the engagement-scope set. When `engagement-scoping` has run, the institution profile, persona, source posture, and sector and cross-cutting overlay sets come from there. Otherwise the skill asks the practitioner the few facts it needs and flags defaults.
- What architecture, and which overlays. Traditional ML, foundation-model, RAG, or agentic. The answer fires the GenAI factor block (foundation-model dependence, RAG corpus, tool inventory, prompt-injection exposure) and decides which sector and cross-cutting overlays load.
- What lifecycle stage. Pre-prod tiering reads from intent and design; production re-tiering reads from monitoring evidence and supervisory posture; retirement reads from residual obligations. Same rubric, different evidence weights.

## How the tier gets decided

The rubric has the same spine across model types. Walk it in the order the evidence arrives; the structured object sorts itself. Every named factor is scored or marked `n/a` with a reason. An empty factor or an unjustified `n/a` is a tell that the rubric was collapsed to one factor (usually customer impact) and the rest skipped.

Tier names and quantitative cutoffs are firm policy, not regulatory mandate. The skill cites the source for the factors but does not invent the firm's tier-1 threshold; where a firm overlay is installed (`references/firm-overlay.md`), the skill consumes the firm's named tiers and cutoffs.

**Customer impact** covers customer-binding decisions, customer-facing surfaces, and indirect customer-outcome effects. A model that is the principal driver of an adverse-action-eligible decision (consumer credit, insurance underwriting, claims handling) reads high; an internal-use research summarisation tool with no client surface reads low. Customer impact alone is not enough to fix the tier, but it is the most-frequent dominant factor.

**Financial impact** covers balance-sheet, capital, liquidity, and material P&L exposure. A pricing model on a multi-billion portfolio reads high; an analyst productivity tool with no decision authority reads low. The threshold against firm risk-appetite materiality is the read; absent a firm overlay, cite the appetite-statement category in the rationale rather than invent a dollar figure.

**Regulatory impact** covers named regulator reach (federal, state, foreign), examination posture, and supervisory-letter exposure. A consumer-credit AI under CFPB Circular 2022-03 reach, an AML transaction-monitoring model under FFIEC examination, an execution algo under SEC Rule 15c3-5 ... each is a regulator-facing surface that elevates the factor independent of customer impact. Multiple regulators amplify; cite each.

**AI Act category** is a routing flag, not a classification. Annex III overlap (creditworthiness assessment of natural persons §5(b); risk assessment and pricing in life and health insurance §5(c); biometric identification §1; employment §4) elevates the tier in the firm rubric and routes to `ai-act-triage` for the formal call. EU footprint absent Annex III overlap is still a regulatory factor (EU AI Act general obligations apply); flag and route.

**Autonomy level** covers advisory through agentic-with-tool-use through fully-autonomous. A model that suggests and a human approves reads lower than one that decides and a human exception-reviews reads lower than one that acts on tools without a human in the loop. Agentic configurations with tool use are tier-elevation factors regardless of customer-binding; route to `agentic-ai-controls` once tier is set.

**Data sensitivity** covers regulated NPI (GLBA), PHI (HIPAA), payment data (PCI), customer-supplied prompt content, biometric data, and children's data. NPI in inputs, training data, or RAG corpus reads as a tier-up; PHI reads higher. The factor is independent of customer impact: an internal analyst tool that retrieves NPI elevates on data sensitivity even when the user surface is internal.

**Model concentration** covers single-model dominance in a decision flow with no challenger or fallback. A sole credit-decisioning model in a channel reads high; a model with a parallel rules-based fallback and override workflow reads lower. The factor is what separates "the model is the decision" from "the model is one input."

**Vendor dependence** covers foundation-model vendor, RAG infrastructure vendor, scoring-engine vendor. Single-vendor concentration on a foundation model with no swap path reads high; firm-built models with vendor data feeds only read lower. Sponsor-bank arrangements amplify (the bank carries the model risk for fintech-built models; OCC Bulletin 2023-17 and the July 2024 joint statement reach).

**Cyber exposure** covers prompt-injection surface, training-data poisoning surface, supply-chain dependence, and AI-enabled social-engineering exposure. NYDFS October 2024 industry letter reach is a tier-up factor for 23 NYCRR Part 500 covered entities; cite it. The factor often goes overlooked on cards designed before GenAI; do not skip it.

**Conduct exposure** covers customer-binding decisions, fairness exposure, complaint vector, and market-integrity reach. ECOA / Reg B for credit; NAIC unfair-discrimination framing for insurance; MAR / Reg AC adjacency for research; Marketing Rule (Investment Advisers Act 206(4)-1) for adviser AI in client communications. The factor weights independent of regulatory factor; double-counting where both apply is the point, not a defect.

**GenAI-specific** fires when foundation-model dependence is present or RAG retrieval or tool use is in the design. Foundation-model swap risk, RAG corpus drift, hallucination exposure, content-provenance exposure, autonomy-level uplift via tool use ... none of these are captured by a rubric designed for pre-GenAI ML. Score the block; do not let it land in `n/a` because the legacy rubric had no entry. NIST AI 600-1 Map 1.1 and Measure 2.6 frame the factor.

**Sector-specific** is the elevation from the loaded sector overlay. The overlay's named factors and tier-up criteria land in the rubric; treating the overlay as background reading is the failure mode. Banking reads CCAR / DFAST and Heightened Standards reach; insurance reads NAIC Model Bulletin AIS Program proportionality and CO / NY footprint; capital markets reads Rule 15c3-5, Marketing Rule, and books-and-records preservation reach; payments-fintech reads sponsor-bank arrangement and BSA/AML reach.

The rationale is two to four sentences, regulator-readable. It names the dominant factors, the regulator constellation, and why the tier is what it is. It does not restate the per-factor table. An examiner reads the rationale, looks for the factor scores that justify it, and probes the dissent line.

## What the tier triggers

Tier drives the gates. The default mapping is the firm's to set; the skill carries a starting map that firm overlay can shift:

| Tier | Validation depth | Monitoring frequency | Committee route |
|---|---|---|---|
| tier-1 | full | quarterly or continuous | AI risk committee |
| tier-2 | full or targeted | quarterly | model risk committee |
| tier-3 | targeted | semi-annual | model risk team |
| tier-4 | light-touch or monitor-only | annual | model owner with second-line concurrence |

Each gate carries an owner (a function, never a named individual), a frequency, and a stop condition. A gate without a stop condition is a meeting, not a control.

Re-tiering triggers are named events with monitoring owners. Dates do not earn a row; "annual review" is a refresh cadence, not a re-tiering trigger. Autonomy-level change, customer-base expansion, scope expansion, vendor swap, RAG corpus scope change, data-sensitivity expansion, regulatory change, performance breach for N consecutive periods, supervisory-letter event ... each names what to watch and who watches.

### Sector and cross-cutting overlays

When the engagement scope names a sector, load the matching `references/sector-overlays/<sector>.md`. The overlay's tier-elevation criteria land in the per-factor justifications. Same pattern for the cross-cutting overlays this skill carries: cyber and privacy. Conduct lives inside the rubric directly because conduct exposure is a named factor; the cross-cutting `references/cross-cutting/conduct.md` is consulted where the conduct lens needs more depth than the factor row carries. Climate is not applicable to AI tiering.

Load only the overlays the engagement scope names. Gold-plating a tier with overlays the engagement does not implicate adds noise without challenge value.

## What's load-bearing and what flexes

A handful of things do not flex:

- Every named factor is scored or marked `n/a` with a reason. An empty factor or an unjustified `n/a` is a defect.
- Tier-1 is reserved. Tier-1 for everything customer-facing makes tier-1 meaningless. Reserve tier-1 for customer-binding decisions, material financial exposure, or named appetite-statement reach; require justification against a named threshold.
- The GenAI factor block fires when triggered. Skipping it on a use case with a foundation model, RAG corpus, or tool use is the failure mode a second-line reviewer flags first.
- Dissent is recorded when the tier disagrees with the sponsor. The dissent field names the reviewer role, the position, and the basis. At tier-1 and tier-2, the AI risk committee secretary signs the dissent line; at tier-3 and tier-4, the second-line reviewer signs.
- Re-tiering triggers carry events and owners, not just dates. The use case grows beyond its tier between annual reviews; the trigger is what catches it.
- AI Act overlap is flagged and routed, not classified. The formal call belongs to `ai-act-triage`.
- The tier is a draft until the decider attests. The skill does not file the tier, post to the inventory, route to validation, or schedule committee.

Everything else adapts to context. Tier names and cutoffs are firm policy. Lifecycle stage drives which evidence weighs heaviest. Source posture sets what the tier can assert at high confidence and what carries `[evidence needed]`. Where firm-specific policy or taxonomy applies, it lives in `references/firm-overlay.md` (consumed when present) and never in the tier record directly.

## Output

Two artifacts: the tier record per `templates/default-output.md`, and the structured object per `schemas/risk-tier.schema.json`. The decider attestation block is filled by the named decider; the record is filed only after.

Downstream consumers: `model-card-builder` pulls the tier and overlay flags to set card depth and section weights. `validation-plan` pulls the tier, validation depth, and factor justifications to scope conceptual-soundness, data-quality, benchmarking, outcomes-analysis, and monitoring work. `agentic-ai-controls` pulls the tier and the autonomy-level factor to scope tool-boundary controls and human-in-the-loop machinery. `genai-pre-prod-review` pulls the tier and GenAI-specific factor to scope the gate. `board-ai-risk-pack` pulls the tier distribution across the inventory. `ai-act-triage` consumes the AI Act overlap flag for the formal classification. The schema is the input contract for those consumers; additive changes only, never silent renames. Breaking changes ship as a versioned migration with the consumers told in advance.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/{banking,insurance,capital-markets,payments-fintech}.md` — sector overlays loaded from engagement scope.
- `references/cross-cutting/{cyber,privacy}.md` — cross-cutting overlays loaded from engagement scope; conduct lives in the factor row.
- `references/firm-overlay.md` — firm tier names, cutoffs, named committees, validation-depth mapping (consumed when present).
- `templates/default-output.md` — tier-record template.
- `schemas/risk-tier.schema.json` — structured-output contract.
- `examples/` — public-source-derived scenarios: in-house consumer credit-decisioning ML; GenAI internal-tool tiering.
