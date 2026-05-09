# Model-card-builder revision review memo

Date: 2026-05-06
Reviewer: phase-2 reviewer subagent
Subject: revised `plugins/capability-plugins/ai-governance-model-risk/skills/model-card-builder/SKILL.md`
Compared against: spec sheet (`docs/specs/ai-governance-model-risk/model-card-builder.md`), the scoping revision-memo as pattern reference, build contract, anti-AI-tells memory (with the sequencing nuance update), spec sheets for downstream consumers (`validation-plan`, `board-ai-risk-pack`, `ai-governance-reviewer` agent).

## 1. Top-line judgment

About right, leaning slightly under-cut in three specific spots. The revision is in much better shape than the scoping first cut. The reviser kept what mattered: the named-section spine survives in narrative form, the GenAI overlay trigger conditions are explicit and correct, the 1.5-line / 2-line lens is named, the tier-to-depth and upstream-artifacts ordering is explicitly load-bearing, the lifecycle stage lean (pre-prod / production / retirement) is in the "Ask first" and is picked up implicitly through the body. Downstream consumers are named with what each pulls — that is the right move and is more concrete than the scoping equivalent.

What did get under-cut: schema-stability discipline (one passing reference to `schemas/model-card.schema.json`, no additive-only / versioned-migration line — and this skill's schema is the input contract for `validation-plan`, `board-ai-risk-pack`, the `ai-governance-reviewer` agent, and the model inventory of record, so it carries more weight than the scoping schema does). The "Ask first" four questions are good (tier, lifecycle, audience, evidence) but miss the architecture-flag question that drives the GenAI overlay (the spec's pitfall #3 is "GenAI cards inherit a structure designed for traditional ML and miss foundation-model dependency, prompt injection, RAG corpus drift" — and the way to head that off is to ask the architecture question early, not to wait for it to surface during drafting). And the sector / cross-cutting overlay question is missing from "Ask first" entirely; the scope record may not be present, in which case the practitioner needs to be asked.

A handful of small AI tells survived ("the most common defect" appears twice, "the single most common defect on first-time GenAI cards" once). Those are fake-precision residue.

There is also a structural gap: the SKILL.md points to `references/cross-cutting/{cyber,privacy,conduct}.md` in the Pointers section, but the cross-cutting directory and files do not exist on disk. This is outside the SKILL.md text itself but is the skill's own broken pointer.

Net: seven proposed edits, all small, none reintroducing rigidity tells. The single biggest gap is the missing architecture / GenAI-trigger question in "Ask first."

## 2. What got dropped or weakened

### 2.1 Architecture flag / GenAI trigger missing from "Ask first"

The spec's common pitfall #3:

> GenAI cards inherit a structure designed for traditional ML and miss foundation-model dependency, prompt injection, RAG corpus drift, and content provenance. Mitigation: GenAI overlay block is required when architecture flags `foundation_model` or `uses_rag` or `uses_tools`.

The revised "Ask first" has four questions (tier, lifecycle, audience, evidence). The architecture-flag question is not asked. The GenAI overlay block triggers downstream of architecture, but the practitioner has to surface architecture early or the card spine for a GenAI use case starts on the wrong shape and gets retrofitted. A senior practitioner asks "is this a foundation-model use case, RAG, agentic, or traditional ML" before they pick up the pen, not three sections in.

Equivalent for the sector / cross-cutting question. The skill has banking, insurance, capital-markets, payments-fintech sector overlays plus cyber, privacy, conduct cross-cutting overlays. The body says "When the scope record is supplied, the skill consumes it for institution, persona, source posture, sector and cross-cutting overlays, and lifecycle stage. Otherwise it asks the practitioner the few facts it needs." That is the right model. But the "Ask first" list does not include the overlay question explicitly, and a practitioner reading the list would not know to ask it. Either fold it into the existing list or keep the deferral in the body and add a sentence that says "and which sector and cross-cutting overlays apply" — which is what gets picked up later but should be visible at the top.

The "Ask first" list does not need to be five bullets. Four well-chosen ones are fine. But the four currently chosen are not the right four. Tier, lifecycle, audience, evidence — these miss the load-bearing architecture question (which gates the entire GenAI overlay) and the overlay question (which the skill consumes from scope or asks).

### 2.2 Schema-stability discipline

The revision's "Output" section:

> Two artifacts: the card per `templates/default-output.md`, and the structured object per `schemas/model-card.schema.json`. The reviewer attestation block (named reviewer, date, decision, conditions, onward routing) is filled by the human reviewer, not by the skill. The card is filed only after attestation.
>
> Downstream consumers: `board-ai-risk-pack` pulls metadata, tier, intended use, performance and limitations summary, and material sign-off questions. `validation-plan` pulls architecture and data sections to scope validation work. The `ai-governance-reviewer` agent pulls the structured object for second-line challenge. The model inventory of record pulls the structured object for the central registry. The card itself is what an examiner is handed.

The downstream-consumer paragraph is good — concrete, named, says what each pulls. Better than scoping's equivalent.

What's missing is the schema-stability rule. Scoping has:

> The schema is the cross-skill contract; additive changes only, never silent edits. Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream skills told in advance.

(After the scoping memo's Edit 2 lands, that is.) Model-card has zero equivalent line. Given that the model-card schema feeds four named consumers including an entire agent, the discipline matters more here than in scoping. One sentence is enough; do not balloon it.

### 2.3 The four "Ask first" practitioner questions

Re-stated for clarity. The current four:

- What tier
- Where in lifecycle
- Who reads it
- What evidence is available

These are good questions. The gap is what is not asked: architecture posture (traditional ML vs foundation-model vs RAG vs agentic), and which overlays apply.

The fix is not "add two more bullets" — that swells the list to six and starts to feel comprehensive in the AI-tell way. The fix is to recompose the four around what actually drives the card's shape early. Proposed:

- Tier (drives depth).
- Lifecycle stage (drives which sections lean heavy).
- Audience (drives tone and depth).
- Architecture and overlays (drives which spine — traditional or GenAI — and which sector / cross-cutting overlays load).

Fold "evidence" into the scope paragraph that already exists below the list ("source posture sets what the card can assert at high confidence and what carries `[evidence needed]`"). Evidence is not a question the practitioner answers; it is a status the engagement carries. Lifecycle, audience, tier, architecture-and-overlays are decisions.

This is a recomposition rather than an expansion. List stays at four.

### 2.4 Sector / cross-cutting overlay loading: the directive pattern

The revised SKILL.md says:

> When the scope names a sector (banking, insurance, capital markets, payments-fintech), load the matching `references/sector-overlays/<sector>.md`. The overlay's named fields and sign-off questions land in the card; treating the overlay as background reading is the failure mode. Same pattern for the cross-cutting overlays this skill carries: cyber, privacy, conduct. Climate is not applicable to model cards.

This is good. "Treating the overlay as background reading is the failure mode" is a real practitioner observation, not engineer-voice. Keep it.

What's missing: "load only the overlays the scope names" is in the next paragraph but the symmetry with scoping's "directive to downstream skills" framing is not surfaced. Scoping says the overlay sets are directives downstream skills consume; this skill is a downstream skill consuming them. One sentence acknowledging the contract from the consumer side would close the loop. Minor; skip if it bloats.

### 2.5 Surviving AI tells

Two instances of "the most common defect" in the body:

- "Missing the owner or the escalation path is the most common defect; the chase across functions..."
- "Missing the GenAI sections on a GenAI card is the single most common defect on first-time GenAI cards."

Both are fake-precision tells. The reviser caught "fail the quality bar" and "ensure / facilitate / streamline" — those are gone. But "the most common defect" is the same family of unsupported specificity. A senior practitioner would say "the section that fails most often is monitoring" or "missing the GenAI sections is what reviewers flag first" — both grounded in observable practitioner experience without claiming a frequency rank. Or just delete the framing and let the substance carry.

Minor. Two edits.

### 2.6 Reviewer attestation language

The revised SKILL.md says:

> The reviewer attestation block (named reviewer, date, decision, conditions, onward routing) is filled by the human reviewer, not by the skill. The card is filed only after attestation.

Combined with:

> The card is a draft until a human reviewer attests. Sign-off is the gate; this skill stops short.

(Earlier in the body.) This is two mentions of the same gate. The build contract says "one mention of 'the skill produces a draft, sponsor signs off' is enough; do not repeat the gate at every juncture." Two is on the edge. The earlier mention is in context (the lens paragraph) and reads naturally; the later one is in the Output section and could be tightened to one sentence: "The reviewer attestation block is filled by the human reviewer; the card is filed only after." Drops the parenthetical (the named fields are in the template anyway) and the "by the skill" hedge. Minor.

### 2.7 The cross-cutting overlay files do not exist on disk

The Pointers section names:

> `references/cross-cutting/{cyber,privacy,conduct}.md` — cross-cutting overlays loaded from scope.

The directory does not exist. The skill points at files it does not ship. This is outside the SKILL.md text proper (it is a separate gap in the skill build) but the SKILL.md is making a promise the skill cannot keep. Either ship the three files (small; the spec gives them clear scope) or remove the pointer.

This is a structural gap, not a content edit. Flagging here so the orchestrator knows. Probably the right fix is to ship the three cross-cutting overlay files; the skill needs them, the spec calls for them, the sector overlays already exist as a pattern to follow.

### 2.8 What the revision did NOT drop

To save the orchestrator a re-check:

- Named-section spine (all 14): present in narrative form. Metadata, intended use, system description, data, performance, robustness, fairness/explainability, limitations, monitoring, controls, change management, sign-off, source trace. Out-of-scope is folded into the intended-use paragraph; that is correct. Spine survives.
- GenAI overlay trigger conditions: explicit and correct. "When `architecture.foundation_model` is set, or `architecture.uses_rag` is true, or `architecture.uses_tools` is true, the GenAI overlay block fires." The four landed-section behaviors (system description, robustness, monitoring, change management) are each named.
- 1.5-line vs 2-line lens: present and well-stated, with the seam (source-trace block, sign-off questions) called out. Better than the scoping equivalent.
- Lifecycle stage lean: in "Ask first" as one bullet, picked up explicitly in the body as pre-prod / production / retirement. Good.
- Tier-to-depth and upstream-artifacts sequencing: explicit, framed as "load-bearing", correctly identified as the two real dependency chains. The sequencing-nuance update to the anti-AI-tells memory is exactly what this revision did. Good.
- Engagement-scope integration: present as a body sentence, not as a heavy procedural section. Good.
- Downstream consumers named: `board-ai-risk-pack`, `validation-plan`, `ai-governance-reviewer`, model inventory of record. This is more concrete than what scoping does and should not be cut.

## 3. Proposed edits

Seven edits, all small. None reintroduce numbered ladders, fake-precision ranges, "fail the quality bar" stacking, or AI-tell prose.

### Edit 1 — recompose the "Ask first" four questions

**Location**: the bullet list under "## Ask first."

**Current**:
> - What tier is the model. Tier drives depth more than anything else; if `ai-risk-tiering` has not run, route there before building the card.
> - Where is the model in lifecycle. Pre-prod cards lean on intended use, design rationale, and limitations. Production cards lean on monitoring evidence. Retirement cards lean on retention and audit trail. Same spine, different weights.
> - Who reads it. A working-group draft is plain. A pre-prod committee card is challenge-shaped. A regulator response is formal and full source-traced. A board distillation pulls sign-off questions to the front.
> - What evidence is actually available today. Source posture sets what the card can assert at high confidence and what carries `[evidence needed]`.

**Proposed**:
> - What tier is the model. Tier drives depth more than anything else; if `ai-risk-tiering` has not run, route there before building the card.
> - Where is the model in lifecycle. Pre-prod cards lean on intended use, design rationale, and limitations. Production cards lean on monitoring evidence. Retirement cards lean on retention and audit trail. Same spine, different weights.
> - Who reads it. A working-group draft is plain. A pre-prod committee card is challenge-shaped. A regulator response is formal and full source-traced. A board distillation pulls sign-off questions to the front.
> - What architecture, and which overlays. Traditional ML, foundation-model, RAG, or agentic — the answer triggers the GenAI overlay block (foundation-model dependence, RAG corpus, tool inventory, prompt-injection robustness, vendor change-of-version trigger) and decides which sector and cross-cutting overlays load.

Then update the paragraph below the list:

> When the scope record is supplied, the skill consumes it for institution, persona, source posture, sector and cross-cutting overlays, lifecycle stage, and architecture flags. Otherwise it asks the practitioner the few facts it needs, and source posture sets what the card can assert at high confidence and what carries `[evidence needed]`.

**Why**: the architecture question gates the GenAI overlay block — which is the spec's pitfall #3 mitigation — and the overlay set is named load-bearing input downstream. The "evidence" question gets folded into the scope paragraph because evidence is not really a question the practitioner answers, it is a status the engagement carries. Tier, lifecycle, audience, architecture-and-overlays is what a senior practitioner actually asks.

### Edit 2 — add the schema-stability sentence

**Location**: end of the "Output" section, after the existing downstream-consumers paragraph.

**Proposed addition** (one sentence appended to the consumer paragraph or as a short standalone sentence):

> The schema is the input contract for those consumers; additive changes only, never silent renames. Breaking changes ship as a versioned migration with the consumers told in advance.

**Why**: this skill's schema feeds four named downstream consumers including an agent. The discipline matters and currently has no mention. Pattern matches the scoping memo's Edit 2.

### Edit 3 — cut "the most common defect" framing

**Location**: monitoring paragraph in the body.

**Current**:
> All five fields. Missing the owner or the escalation path is the most common defect; the chase across functions (consumer compliance owns complaint rate, infosec owns prompt-injection signal, vendor management owns version notice) is part of the work.

**Proposed**:
> All five fields. The owner and the escalation path are what reviewers flag first; the chase across functions (consumer compliance owns complaint rate, infosec owns prompt-injection signal, vendor management owns version notice) is part of the work.

**Why**: "the most common defect" is fake-precision residue. "What reviewers flag first" is grounded practitioner observation without the false frequency claim. Same substance, no AI tell.

### Edit 4 — same fix in the GenAI overlay paragraph

**Location**: closing sentence of the GenAI overlay block.

**Current**:
> Missing the GenAI sections on a GenAI card is the single most common defect on first-time GenAI cards.

**Proposed**:
> Missing the GenAI sections on a GenAI card is what a second-line reviewer flags first when the card lands for challenge.

**Why**: same fake-precision tell. The reframing keeps the "this is what fails on first-time GenAI cards" point but grounds it in what a reviewer does, not in an unsupported frequency claim.

### Edit 5 — tighten the reviewer attestation reference in Output

**Location**: first paragraph of "## Output."

**Current**:
> Two artifacts: the card per `templates/default-output.md`, and the structured object per `schemas/model-card.schema.json`. The reviewer attestation block (named reviewer, date, decision, conditions, onward routing) is filled by the human reviewer, not by the skill. The card is filed only after attestation.

**Proposed**:
> Two artifacts: the card per `templates/default-output.md`, and the structured object per `schemas/model-card.schema.json`. The reviewer attestation block is filled by the human reviewer; the card is filed only after.

**Why**: the body already establishes the gate ("Sign-off is the gate; this skill stops short") earlier. The Output section repeating it with parenthetical detail is the kind of stacking the build contract bans. The named fields are in the template anyway. One sentence here is enough.

### Edit 6 — surface the consumer-side overlay-loading contract (skip if bloat)

**Location**: end of the "Sector and cross-cutting overlays" subsection.

**Proposed addition** (one sentence):

> The overlay sets are directives produced by the scope record; this skill is one of the consumers.

**Why**: closes the loop with scoping's framing. The overlay sets are described in `scoping` as directives downstream skills consume; from the consumer side the symmetry is worth one sentence. Skip if the section starts to feel structured-for-its-own-sake; the substance is reachable without it.

### Edit 7 — ship the cross-cutting overlay files (structural, not SKILL.md text)

**Location**: outside SKILL.md. The Pointers section names `references/cross-cutting/{cyber,privacy,conduct}.md`; the directory does not exist.

**Proposed action**: ship `references/cross-cutting/cyber.md`, `references/cross-cutting/privacy.md`, `references/cross-cutting/conduct.md`. Spec sheet section "Cross-cutting overlays" gives the scope for each. Pattern follows the four sector overlays already shipped.

**Why**: the SKILL.md makes a promise the skill cannot keep. Either remove the pointer (worse — the skill needs the overlays) or ship the files. The spec says climate is not applicable to model cards; that is correctly omitted.

## 4. What the revision did right and should not be undone

In case the orchestrator over-corrects after this memo:

- **The "Ask first" prompts are four plain-English bullets, not numbered.** Right call. Numbered ladders for non-sequential lists are the AI tell. Do not renumber. (Edit 1 recomposes the four; it does not number them.)
- **Tier-to-depth and upstream-artifacts ordering is explicitly load-bearing and called out as such.** Right. This is exactly what the sequencing-nuance update to the anti-AI-tells memory describes — explicit ordering where the order is a real dependency chain. Do not remove the "load-bearing" framing.
- **The named-section spine walks as prose paragraphs, not a numbered 1-12 ladder.** Right. The spec sheet enumerates fourteen sections; the practitioner walks them in narrative shape. Do not re-enumerate.
- **The GenAI overlay block is a single subsection with the trigger conditions named once and the four landed-section behaviors listed.** Right. No repetition across other sections. Keep this.
- **"Both lenses" framing for 1.5-line owner / 2-line reviewer is specific and names the seam.** Right. Better than the scoping equivalent and the practitioner-lens memory specifically calls out that 1.5/2 both matter. Keep.
- **Downstream consumers are named with what each pulls.** Right and concrete. Better than scoping. Keep verbatim.
- **No `[verify section]` markers in SKILL.md or the description's "Anchored to:" line.** Right. Those belong in `references/source-anchors.md`.
- **No "fail the quality bar" residue, no "must / mandatory / required" stack, no marketing adjectives ("comprehensive", "robust", "ensure"), no hedge tics ("it is worth noting").** Right. Two minor "most common defect" tells slipped through (Edits 3 and 4); the rest is clean.
- **One "What's load-bearing and what flexes" section, not parallel "non-negotiable rigidities / adaptation guidance" pair.** Right. Anti-AI-tells memory specifically bans the pair. Keep this as one section.
- **The opening paragraph names what the card is and who reaches for it (model risk committee, validator, pre-prod gate reviewer, model inventory of record, examiner) without inflating into mission-statement prose.** Right. Keep.
- **`Pointers` section is short, file-path-only, no commentary.** Right. (Subject to Edit 7 — ship the cross-cutting files so the pointers are honest.)

## 5. Closing

The revision is good. Three substantive restorations (Ask-first recomposition for architecture/overlays, schema-stability sentence, two minor AI-tell cleanups), one tightening (reviewer attestation in Output), one optional (consumer-side overlay-loading symmetry), and one structural fix outside SKILL.md (ship the three cross-cutting overlay files the Pointers section already names).

If the orchestrator can only land one edit, land Edit 1 (the Ask-first recomposition). Schema stability (Edit 2) and the cross-cutting overlay files (Edit 7) are close behind and arguably tied for second.

None of the proposed edits restore numbered ladders, fake-precision ranges, repeated "must / mandatory / required" stacking, "fail the quality bar" prose, marketing adjectives, or hedge tics.
