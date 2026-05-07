---
name: <skill-slug>
description: |
  <!-- One paragraph: what the artifact is, what it produces, who consumes it. No regulator names — they live in references/source-anchors.md and load conditionally. No `[verify section]` markers. -->
  <One paragraph naming the artifact, the audience, and the cross-skill contract it feeds.>

  Best for:
  - <Concrete trigger 1: who calls it, in what situation.>
  - <Concrete trigger 2.>
  - <Concrete trigger 3.>

  Not the right tool when:
  - <Adjacent skill does it better; name the skill.>
  - <Out-of-scope situation; route elsewhere.>
argument-hint: "[concise input shape: scope record, prior artifact ID, or free-text trigger]"
---

# <Skill display name>

<!-- One paragraph overview: what the artifact is, what it carries, who reaches for it, what decision it supports. Mirror the bench-build trio voice. -->
<Overview paragraph. Name the artifact, its consumers, and the seam between 1.5-line drafting and 2-line challenge.>

## Ask first

<!-- Questions a senior practitioner asks before drafting. Not a checklist. 3-5 bullets, each one sentence + one clarifying line. -->

Before drafting, get plain answers to a few things. Defaults are fine when an answer is missing; flag the default in the artifact.

- <Question 1. Why it matters in one line.>
- <Question 2. Why it matters in one line.>
- <Question 3. Why it matters in one line.>
- <Question 4. Why it matters in one line.>

When `engagement-scope` is supplied, the skill consumes it for institution, persona, source posture, sector and cross-cutting overlay sets. When it is not, ask the questions above and default source posture to public-only; flag the absence in the artifact.

## How the <artifact> gets built

<!-- Prose paragraphs walking the artifact's spine. Generic regulator language. Sequencing only where dependency-driven (e.g., tier before depth). Otherwise: "the order the conversation surfaces evidence". -->

The <artifact> has the same spine across <variant set>. A senior reviewer fills it in roughly in the order the engagement and the evidence offer it, not in lockstep.

<Section-1 paragraph: what it carries, what reviewers probe, the load-bearing fields.>

<Section-2 paragraph.>

<Section-3 paragraph. Continue until the spine is walked.>

<Closing paragraph: how the artifact closes (recommendation, sign-off questions, revision log, etc.).>

<!--
Non-negotiables and adaptation guidance go INLINE in the workflow narrative above, not in a separate "load-bearing and flexes" section. Examples to bake into the workflow paragraphs:
- Cite a source for every material claim. Mark unsupported claims `[evidence needed]`.
- The skill stops at draft / recommendation; sponsor or sign-off owner closes.
- Sector and cross-cutting overlays load from the engagement scope; skill loads only what the engagement names.
- Audience drives depth (working group plain, committee structured, examiner response formal, board distilled).
Senior practitioners do not have a meta-section about what is mandatory; the must-do's are part of how they describe the work.
-->

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/{banking,insurance,capital-markets,payments-fintech}.md` — sector overlays loaded per engagement-scope.
- `references/cross-cutting/{cyber,privacy,climate,conduct}.md` — cross-cutting overlays loaded per engagement-scope.
- `references/firm-overlay.md` — firm-installed policy, taxonomy, review gates; consumed when present.
- `templates/default-output.md` — content spec for the artifact (named sections, fields).
- `examples/` — anonymised public-source-derived scenarios.
- `TROUBLESHOOTING.md` — recurring defects.
- `schemas/<skill-slug>.schema.json` — OPTIONAL: include only when the artifact has a structure that genuinely helps downstream automation (e.g., DORA register row mapping to EBA ITS table; structured engagement-scope record). Most skills skip this.

## Output

<!-- Name the artifact and the rendering format. Practitioners get Word memos, Excel matrices, PowerPoint decks. Markdown is the content spec, not the deliverable. -->

The deliverable is a <Word memo / Excel matrix / PowerPoint deck>. The skill defines the artifact substance (named sections, fields, populated content per `templates/default-output.md`) and delegates rendering to Anthropic's `document-skills` plugin: `docx` for memos and write-ups, `xlsx` for matrices / registers / workpapers, `pptx` for committee and board decks.

Downstream consumers: `<consumer-skill-1>` reads <what>; `<consumer-skill-2>` reads <what>. <If a structured record is emitted, name it and the schema; otherwise omit this sentence.>
