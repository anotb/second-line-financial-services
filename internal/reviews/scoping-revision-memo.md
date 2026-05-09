# Scoping revision review memo

Date: 2026-05-06
Reviewer: phase-2 reviewer subagent
Subject: revised `plugins/capability-plugins/risk-compliance-core/skills/scoping/SKILL.md`
Compared against: spec sheet (`docs/specs/risk-compliance-core/scoping.md`), supporting artifacts (template, troubleshooting), build contract, anti-AI-tells memory.

## 1. Top-line judgment

The revision lands closer to right than wrong. It reads like a senior practitioner walking a junior through the work. AI tells are mostly gone. Voice is good.

But it over-cut in three places where the load-bearing substance was the substance, not the rigidity. Specifically: the dual-trigger entry pattern (called fresh vs called from another skill mid-flight) is compressed to a single sentence at the bottom of "Working with what you have" and now reads as an afterthought rather than the second of two valid entry paths. The schema-stability discipline is one clause; given that every other skill in the repo consumes this schema, it deserves slightly more emphasis. The persona depth lost the explicit 1.5-line vs 2-line vs advisory-firm distinction in named form, which is one of the things the practitioner-lens memory specifically calls out as load-bearing.

Net: under-cut nothing, over-cut substance in a few specific spots, and dropped two named items the spec sheet calls out. Six proposed edits below, all small.

## 2. What got dropped or weakened

### 2.1 The dual-trigger pattern

The spec sheet's "Best for" list has four triggers; the fourth ("a downstream skill called with contested or unclear scope") is the bootstrap-from-mid-flight pattern. The revision keeps it in the description list. Good.

The original bench-build (per the build contract) had this as a named workflow path. The revision compressed it to one sentence at the end of "Working with what you have":

> When this skill is called from another skill that has hit contested scope (source posture too low to proceed, persona review gates missing, sector overlay unclear), focus on the contested section first and produce a revised record; the calling skill resumes from there.

This is fine prose. It is also buried. The mid-flight invocation is one of two valid entry paths and a senior practitioner would treat it as such. Right now the revision reads as if scoping is mainly a kickoff skill that occasionally gets pulled in mid-flight; the reality is the mid-flight invocation will be common because every other skill in the repo can fall into it.

### 2.2 Schema-stability emphasis

The revision keeps:

> The schema is the cross-skill contract — additive changes only, never silent edits.

This is the right sentence. It is also the only sentence. Given that every other skill in the repo consumes this schema as input, and given that the revision otherwise correctly de-emphasizes engineer-voice tics, I think the discipline deserves one more sentence of context — specifically that fields are added, never renamed or repurposed, and that breaking changes mean a versioned migration. Without that the "additive changes only" line reads as a slogan rather than a working rule.

(I am not asking for "schema drift breaks the rest of the repo" — that is the engineer-voice tic the anti-AI-tells memory bans.)

### 2.3 Persona depth

The spec sheet's persona enum lists thirteen named roles plus "other." The original bench-build (per the spec) walked through them with the 1.5-line / 2-line / advisory distinction. The revision says:

> CRO-led engagements run on ERM machinery, CCO-led on compliance committee, AI-governance-led on AI risk committee, advisory engagements add partner approval and independent QA. Capture which.

This is good practitioner prose. It is also missing the 1.5-line vs 2-line distinction by name. The practitioner-lens memory (`feedback_practitioner_lens.md`) specifically calls out that "1.5 line and 2 line both matter" and that skills should serve both. The revision earlier mentions "Both 1.5-line embedded teams and 2-line independent reviewers benefit," which is fine for the overview, but in the persona section the line-of-defense distinction is the thing that drives review gates. Without it the persona section reads as a list of named C-suites.

### 2.4 Multi-entity / holding-company nuance

The spec sheet's pitfall #1 names "treating the charter as a one-time deliverable"; the revision covers that under "the first charter is a working draft" and the revision-log mention. Fine.

The spec doesn't explicitly call out multi-entity structures in pitfalls, but the institution enum includes `bank-holding-company` alongside `national-bank`, `state-member-bank`, `broker-dealer`, `investment-adviser`, `registered-fund`. The revision handles this with one sentence under "What not to do":

> Do not mix engagements. A holding-company review and a subsidiary review need separate charters even if the same practitioner runs both.

This actually survived. Fine. Leave it.

### 2.5 Source-posture flex (shifts logged in revision log)

The spec common-pitfall #5 says "Saying 'connector-aware' without confirming connector availability leads downstream skills to ask the wrong evidence questions." The revision keeps the substance under "Source posture":

> The same engagement may run at public-only for an early scoping conversation and shift up once firm access lands; that shift goes in the revision log.

Survived. Good.

### 2.6 Overlay-set-as-directive

Spec section "Sector overlay set" and "Cross-cutting overlay set" frame these as flags downstream skills consume. The revision keeps:

> Both sets are directives to downstream skills, telling them which `references/sector-overlays/<sector>.md` and `references/cross-cutting/<topic>.md` to load.

Survived. Good.

### 2.7 Revision log mechanic

Spec template section 12 is a revision log table with date / reason / delta / approved by. The revision keeps the append-only mechanic:

> The revision log is append-only; the first row is the initial scope and every material change adds a row.

Survived. Good. (Could be strengthened by noting that the log is the audit trail when scope is later contested, which is in the template's footer note but not in SKILL.md. Minor.)

### 2.8 The "Ask first" prompts

The build contract calls for "three to five questions a senior practitioner asks before starting." The revision has five, in prose-friendly bullet form. They are good practitioner questions. Drop the original's seven if it had seven; five is right. No edit needed here.

## 3. Proposed edits

Six edits, all small. None reintroduce numbered-step rigidity or AI-tell prose.

### Edit 1 — surface the dual-trigger entry pattern earlier

**Location**: replace the existing penultimate sentence of "Working with what you have" (the "When this skill is called from another skill..." sentence) and lift it into a short standalone paragraph closer to the top of the body, just after the opening overview paragraphs.

**Proposed text** (paragraph, no heading):

> Scoping runs in two situations. At kickoff, the engagement lead calls it to set the charter before any review work begins. Mid-flight, another skill calls it because it has hit contested or unclear scope — the source posture is too low for the evidence ask, the persona review gates are unnamed, the sector overlay is ambiguous. Both entries produce the same artifact; the mid-flight version focuses the revision on the contested section and hands back to the calling skill.

**Why**: load-bearing because every other skill in the repo can land in the mid-flight path. Senior practitioners treat both entries as first-class. Burying the second entry under "Working with what you have" misreads the operational reality.

### Edit 2 — one more sentence on schema stability

**Location**: "Output" section, after the existing line "The schema is the cross-skill contract — additive changes only, never silent edits."

**Proposed text**:

> Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream skills told in advance.

**Why**: the discipline matters because the schema is the cross-skill contract for the entire repo. One slogan-line is not enough operational guidance. Two sentences are enough; do not balloon it into a sub-section.

### Edit 3 — name the line-of-defense distinction in the persona paragraph

**Location**: third sentence of the persona paragraph in "What goes in the charter," replacing the current "which line of defense applies (1.5, 2, sometimes 3 for audit support)" parenthetical and the sentence after.

**Proposed text** (replacing two existing sentences):

> The persona profile names the role running the engagement and the line of defense it sits in. 1.5-line is the embedded business risk officer, the regional risk lead, the BU controls tester — accountable to the business but with a risk mandate. 2-line is the independent function — CRO, head of model risk, head of TPRM, head of operational resilience, CCO, BSA officer, AI governance lead, head of regulatory affairs. Audit support and advisory engagements layer their own review machinery on top — partner approval, independent QA, internal audit sign-off. Capture which line and which review gates; the downstream skills key off both.

**Why**: this is the practitioner-lens memory's named load-bearing substance. The current revision generalizes 1.5/2 into "both benefit" up top and then drops the distinction in the section that actually uses it. Naming the roles by line of defense is what a senior practitioner would do.

### Edit 4 — strengthen the revision-log purpose

**Location**: the existing "The revision log is append-only..." sentence at the end of the "What goes in the charter" section.

**Proposed text** (replacing the existing sentence):

> The revision log is append-only; the first row is the initial scope, every material change adds a row, and the log is the audit trail when scope is later contested in steering, in court, or with a regulator.

**Why**: the spec common-pitfall #1 ("Treating the charter as a one-time deliverable") and the template's footer note both call out the contestation defense. The revision keeps the mechanic but loses the why. One added clause restores the substance without adding a section.

### Edit 5 — small addition to "What not to do"

**Location**: end of the "What not to do" bullet list. Add one bullet.

**Proposed text**:

> - Do not over-list primary regulators. Primary regulators is who this engagement is actually addressing, not every regulator that touches the institution. Conceivable-but-secondary regulators go in assumptions.

**Why**: this is spec common-pitfall #4 and TROUBLESHOOTING #4. The revision currently has nothing on it. The institution-profile paragraph mentions the regulators are "actually addressing" the engagement, which is correct but easy to miss. A single bullet in "What not to do" makes it harder to skip. (Skip this edit if the bullet count starts to feel like a list-for-its-own-sake; the substance is also accessible via TROUBLESHOOTING.)

### Edit 6 — clarify what "this skill" means in the very first paragraph

**Location**: opening paragraph after the heading. Currently:

> The first thing a senior reviewer does on any non-trivial second-line engagement is set the scope. Who is the institution. What is the engagement. Who is the persona running it. What evidence is actually available. Which risks are in scope. Which sector and cross-cutting overlays apply. What is excluded. What is being assumed. What is left to clarify.

This is good and reads well. No edit. Including this for the orchestrator's reference because edits 1-5 do not touch it and that is intentional.

## 4. What the revision did right and should not be undone

In case the orchestrator over-corrects after this memo:

- **The "Ask first" prompts are five plain-English bullets, not numbered.** Right call. Numbered ladders are the AI tell the user flagged. Do not renumber.
- **The "What goes in the charter" section is prose paragraphs walking the spine of the artifact, not a numbered 1-11 ladder.** Right call. The spec sheet enumerates eleven sections; the practitioner walks them in the order the conversation surfaces. Do not re-enumerate.
- **No "[verify section]" markers in the description's "Anchored to:" line.** Right. Those belong in `references/source-anchors.md`.
- **No "fail the quality bar" repetition, no "must / mandatory / required" stack, no marketing adjectives, no hedge tics.** Right.
- **One "what not to do" section, not a parallel "non-negotiable rigidities / adaptation guidance" pair.** Right. The anti-AI-tells memory specifically calls out the pair as a tell. Keep it as one section.
- **The opening overview lands the practitioner immediately into the work.** Right.
- **`Pointers` section is short, file-path-only, no commentary.** Right. The orchestrator was right not to inflate it.
- **The dual-audience nod ("Both 1.5-line embedded teams and 2-line independent reviewers benefit; advisory engagements run the charter formally, internal teams run it lighter")** is one sentence at the right moment. Do not delete this even if Edit 3 lands. The line in the overview names the audience; Edit 3 puts the line-of-defense distinction in the section that uses it.

## 5. Closing

The revision is good. It needs three substantive restorations (mid-flight entry path, schema-stability operational rule, named line-of-defense distinction in the persona section) and two small clarifications (revision-log purpose, primary-regulator over-listing). Total proposed: six edits, none of which restore numbered ladders, fake-precision ranges, repeated "must" / "mandatory" stacking, or AI-tell prose.

If the orchestrator can only land one edit, land Edit 1 (mid-flight entry path). The schema (Edit 2) and persona (Edit 3) are close behind.
