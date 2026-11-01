---
name: genai-pre-prod-review
description: "Run a pre-production gate review for a GenAI use case before release or material expansion."
argument-hint: "[use-case ID, model card, validation-plan results, prompt-injection review, RAG evaluation, vendor evidence review, IR runbook reference, or scope statement]"
---

# GenAI pre-prod gate review

A pre-prod gate review is the consolidating motion before a GenAI use case goes into initial release, before a material expansion of an existing deployment, or before a regulator pre-meet asks for the deployment-readiness package. It pulls the upstream artefacts on to one page, applies second-line judgement to the consolidated view, and lands a recommendation: go, go-with-conditions, hold, no-go. The committee owns the gate; this skill produces the memo the secretary signs into the meeting.

The audience reads from several angles at once. The AI Governance Lead consolidates the memo. The AI risk committee secretary owns the gate motion. The model risk officer (MRMO) inherits the model-risk seams from the validation-plan results. The model owner is the source of upstream evidence and the receiver of any blocking conditions assigned back. For most use cases the CISO function and the privacy officer are co-signers because the cyber and privacy overlays load by default; for customer-facing or decision-affecting use cases consumer compliance is a co-signer; for AML-touching use cases the BSA officer is in the room; for insurance underwriting and pricing the chief actuarial officer is in the room.

The gate review consolidates; it does not re-do the upstream work. The model card, the validation-plan results, the prompt-injection review, the RAG evaluation, and the vendor evidence review are each their own artefact with their own attestation. The gate review references them, carries their attested confidence forward, and concentrates on the deployment-readiness gap between what the artefacts establish and what is operationally true at gate time (monitoring live, IR drilled, off-switch documented, swap revalidation policy explicit, sign-offs collected).

The memo is a draft until the human reviewers attest. The decision is a recommendation; the committee owns the gate.

## When to use

Pre-production gate review for a GenAI use case before initial release or material expansion. Pulls together the upstream artifacts (intake, tier, model card, validation-plan results, prompt-injection review where applicable, RAG evaluation review where applicable, vendor evidence review where applicable) and produces a recommended decision (go, go-with-conditions, hold, no-go) with reasoning, named blocking and tracking conditions, owners, and source trace. The artifact a senior risk officer or AI risk committee secretary signs into the gate meeting.

Best for:
- A GenAI use case is at the pre-prod gate and the second-line function needs the gate-review memo with a clear recommendation.
- A material expansion of an existing GenAI deployment (new user population, new tool, new corpus, new geography) needs a re-gate.
- A regulator pre-meet, examiner request, or supervisory motion is asking for the gate package on a named GenAI use case.
- A recurring revalidation cycle has triggered a gate moment and the committee needs the consolidated view.

Not the right tool when:
- The use case has not produced its upstream artifacts yet (run intake, tier, model card, validation plan, prompt-injection review, RAG evaluation, vendor evidence review as applicable first; the gate review consumes them).
- The use case is non-generative ML (use validation-plan with the standard model-risk close-out flow; this skill is GenAI-specific).
- The artifact required is the executive committee or board pre-read (use board-ai-risk-pack; this skill produces the gate review, not the committee summary).
- The artifact required is the foundation-model vendor evidence pack (use llm-vendor-evidence-review; this skill consumes its output).

## Ask first

Most of what the gate review needs is on the table by the time someone reaches for this skill. A few things to settle before drafting:

- What gate is this. Initial release, material expansion, recurring revalidation, or regulatory response. The gate type drives which upstream artefacts must be current versus refreshed and which sections lean heavy. A material expansion that treats prior artefacts as still-current without re-running them against the expanded scope is the recurring failure mode.
- Are the upstream artefacts current. Intake, tier, model card, validation-plan results, and the GenAI-specific reviews (prompt-injection, RAG evaluation, vendor evidence) where applicable. Stale or missing artefacts block `go` by policy; the gate review does not assert coverage that the upstream work does not support.
- Who reads the memo. The AI risk committee secretary and the committee are the primary audience. For tier-1 use cases the board-ai-risk-pack downstream consumer pulls the residual-risk and recommended-decision summary; for examiner-relevant use cases the regulator response file pulls the full memo. The audience drives the depth and the formality.
- Which sector and cross-cutting overlays load. The named regulatory anchors and the named overlay files are loaded from the scope. Cyber should be considered the default cross-cutting overlay for GenAI gate reviews; privacy loads where regulated personal data is handled; conduct loads where customer-facing communication or decision-affecting output is in scope.

When the scope record is supplied, the skill consumes it for institution, persona, source posture, sector and cross-cutting overlays, gate type, and architecture flags. Otherwise the skill asks the practitioner the few facts it needs and drafts against what is given. Source posture sets what the memo can assert at high confidence and what carries `[evidence needed]`.

## How the memo gets built

The memo has the same spine across architectures and gate types. The order below has real dependency in places and reads as prose elsewhere.

The upstream artefact roll-up runs first: the gate review's spine is the consolidated view, and a partial roll-up is a partial gate. Mark each artefact `current`, `stale`, `missing`, or `not-applicable` with a basis in the notes column. Any `stale` or `missing` artefact reflects in the recommended decision; reducing scope is preferable to defaulting to go.

Next, residual risk consolidates from the upstream artefacts. The model card's limitations and known failure modes, the validation-plan results' open findings, the prompt-injection review's residual-risk table, and the RAG evaluation's findings are the inputs; the gate review's top three to five residuals (more for tier-1) are the consolidated view with attested confidence carried forward. Each residual carries likelihood, impact, basis, accepted owner role, and review cadence. "Low" without a basis is opinion; the basis column is required and typically references the upstream artefact that establishes the rating.

Open conditions are next. Each carries owner role (function, never an individual), SLA (date or named milestone), severity, and an explicit blocking-versus-tracking flag. Conditions without owners and SLAs become forever-open; missing fields fail the review. Critical-severity items typically block go.

Monitoring readiness, incident-response readiness, human oversight design, and foundation-model dependency posture are the deployment-readiness sections. These are where the gate review concentrates its diagnostic work, because they are the operational facts that may not have been current when the upstream artefacts attested. A signal listed as live but blocked on a control or configuration change is not actually live; the structure surfaces the dependency by construction. An IR procedure documented but not drilled for an AI-specific scenario is documented, not exercised; the drill is the load-bearing evidence. A human-in-the-loop design without an off-switch criterion degrades silently under volume pressure; the criterion is required for any tier-1 or tier-2 use case. A foundation-model dependency without a documented swap-revalidation policy has the trigger and no playbook; the policy is required when the dependency is present.

Sector and cross-cutting overlay sign-offs land before the consolidated sign-off block. Each loaded overlay names a co-reviewer or co-signer; the gate review records the status (signed, signed-with-conditions, dissent, pending, or not-applicable) for every loaded overlay. Pending sign-off is recorded explicitly rather than absent.

The recommended decision lands once the residual risk, the open conditions, and the deployment-readiness sections are filled. Four options: `go` (no blocking conditions, all overlays signed, monitoring live, IR drilled, off-switch documented, swap policy explicit where applicable), `go_with_conditions` (no blocking conditions, tracking conditions accepted with named owners and SLAs), `hold` (one or more blocking conditions exist or one or more upstream artefacts is stale or missing or one or more deployment-readiness item is not exercisable before go-live), `no_go` (the use case does not clear second-line judgement at this gate). The rationale paragraph names the conditions that drove the call. For `go_with_conditions`, the blocking-versus-tracking distinction is explicit; "go" with a long blocking list is no-go in disguise.

The sign-off block names the reviewers across the relevant functions. A single-name sign-off block on a tier-1 or tier-2 GenAI use case is itself a finding. The committee assumes broader sign-off than exists when only one role is named. Dissent is recorded explicitly with a basis; the gate decision proceeds with the dissent visible to the committee.

The source-trace section closes the memo. Every material claim, its source, the evidence pointer, and a confidence label. Vendor self-attestation carries vendor-self-attestation confidence (typically low to medium). Upstream artefacts that are themselves source-traced (model card, validation-plan results, prompt-injection review) carry their attested confidence forward; do not over-claim. `[evidence needed]` flags route to open conditions.

Depth flexes with tier and gate type. A tier-3 recurring-revalidation gate review compresses to one or two pages; a tier-1 initial-release gate review with full overlay loading runs long and dense. Empty named sections are not acceptable, but compression is.

## Sector and cross-cutting overlays

When the scope names a sector (banking, insurance, capital markets, payments-fintech), load the matching `references/sector-overlays.md#<sector>`. Each overlay carries sector-specific co-reviewers, additional notification triggers, sector-specific monitoring expectations, and recommended-action items. The overlay's named additions land in the memo; treating the overlay as background reading is the failure mode.

Cyber should be considered the default cross-cutting overlay for GenAI gate reviews. The CISO function is a co-signer on the gate decision, not a downstream consumer. Privacy loads where regulated personal data is handled (NPI, PHI, biometric data, state-comprehensive-privacy-law-relevant content). Conduct loads where customer-facing communication or decision-affecting output is in scope. Climate is not applicable to pre-prod gate reviews.

Each loaded cross-cutting overlay names a co-reviewer or co-signer (CISO function for cyber, Privacy Officer for privacy, consumer compliance for conduct) and adds named regulator-notification triggers to the incident-response readiness section. Loading the overlay without surfacing the seam in the sign-off block, the open conditions, the residual risk, the monitoring readiness, or the incident-response triggers is the failure mode.

Load only the overlays the scope names. Gold-plating with overlays the engagement does not implicate adds noise without challenge value.

## Quality bar

The memo is only credible when these hold:

- Every material claim cites a source. Unsupported items carry `[evidence needed]` and route to open conditions, not silently into the memo body.
- Evidence is separated from inference. Vendor self-attestation is not the same line as firm-independent evidence; upstream artefacts carry their attested confidence forward.
- No fabricated regulatory facts. Unknown section references carry `[verify section]` in the source-anchors file (not in the memo body).
- The upstream artefact roll-up is the spine. Stale or missing artefacts block `go` by policy.
- Open conditions carry owner role, SLA, severity, and an explicit blocking-versus-tracking flag.
- "Go" with material blocking conditions is not the recommendation; the decision is `go_with_conditions` or `hold`. The blocking-versus-tracking distinction is explicit in the rationale.
- Foundation-model swap re-validation policy is named when the dependency is present. Silent policy is itself a critical-severity finding.
- Off-switch criterion is named for cyber-relevant incident classes and for tier-1 or tier-2 human-in-the-loop designs.
- The sign-off block names multiple reviewer roles across the relevant functions. A single-name sign-off on tier-1 or tier-2 is itself a finding.
- No named institutions outside finalised public enforcement actions; examples are anonymised and public-source-derived.
- The memo is a draft until the human reviewers attest. The skill does not file the gate decision, post to the AI risk committee, or open production.

## Adaptation

Tier and gate type drive depth. Audience drives tone (working group is plain, committee is structured, examiner response is formal, board distillation pulls residual risk and recommended decision to the front). Sector and cross-cutting overlays load from the scope. Source posture sets what the memo can assert at high confidence and what carries `[evidence needed]`. Where firm-specific policy or taxonomy applies (named committees, named decision owners, internal model-risk-policy thresholds, firm-specific decision-forum machinery), it lives in `references/firm-overlay.md` (consumed when present) and never in the memo directly.

## Output

Default to drafting the memo against `templates/default-output.md`. Render as Word for committee distribution, or another format the audience asks for; the AI risk committee secretary usually wants a Word memo to file with the meeting record. Produce the structured record at `schemas/genai-pre-prod-review.schema.json` when a downstream consumer (`board-ai-risk-pack`, `ai-governance-reviewer`, the model inventory) needs it. The reviewer-attestation block is filled by the human reviewers (AI Governance Lead consolidating; AI risk committee secretary owning the gate motion; CISO function for cyber-flagged reviews; Privacy Officer for privacy-flagged reviews; consumer compliance for conduct-flagged reviews; sector-specific co-signers per the loaded overlay); the memo is filed only after.

Downstream consumers: `board-ai-risk-pack` pulls the residual-risk summary, the recommended decision, and the open conditions for tier-1 and tier-2 use cases with material residual risk. The `ai-governance-reviewer` agent pulls the structured object for second-line challenge. The model inventory of record records the gate decision and the open conditions against the use-case entry. The regulator response file consumes the full memo with source trace where the use case is examiner-relevant. The schema is the input contract for those consumers; additive changes only, never silent renames. Breaking changes ship as a versioned migration with the consumers told in advance.

## Pointers

`references/sector-overlays.md` and `references/cross-cutting.md` hold one section per sector or topic, and `examples.md` one per example. Find the heading and read only that section.

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays.md` — sector overlays loaded from scope.
- `references/cross-cutting.md` — cross-cutting overlays loaded from scope. Cyber is the default for GenAI gate reviews.
- `references/firm-overlay.md` — firm policy, taxonomy, named committees, named owners, gate machinery (consumed when present).
- `templates/default-output.md` — gate-review memo template.
- `schemas/genai-pre-prod-review.schema.json` — structured-output contract.
- `examples.md` — anonymised public-source-derived scenarios (banking KYC analyst assistant initial release; insurance claims summarisation material expansion).
- `examples.md#troubleshooting` — recurring defects.

## Human review and AI disclosure

Open the deliverable with this line, and remove it only after the review below: `AI-assisted draft. Requires review by a qualified person before use.`

A qualified person with authority to change the output reviews it before it is delivered or relied on, and stays accountable for it. Where the output supports advice to an individual or a decision about an individual (credit, insurance underwriting, pricing or claims, employment, legal rights, or similar), that individual must be told AI was used to produce it. This skill does not make final decisions, file with a regulator, notify customers, execute transactions, or move money or other financial assets.
