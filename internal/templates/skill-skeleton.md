---
name: <skill-slug>
description: |
  <!-- One paragraph: what the skill produces, who consumes it. Anchored to NAMED SOURCES, NOT SECTIONS. No `[verify section]` markers in this block. -->
  <One paragraph naming the artifact, the audience, and the cross-skill contract it feeds.>

  Best for:
  - <Concrete trigger 1: who calls it, in what situation.>
  - <Concrete trigger 2.>
  - <Concrete trigger 3.>

  Not the right tool when:
  - <Adjacent skill does it better; name the skill.>
  - <Out-of-scope situation; route elsewhere.>

  Anchored to: <NAMED REGULATORY SOURCES AND STANDARDS, comma-separated. No section numbers here>. Citations and excerpts live in `references/source-anchors.md`.
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

## What's load-bearing and what flexes

<!-- Two paragraphs total. NOT a bulleted checklist. Rule-1 violation patterns ARE the load-bearing list (cite sources, distinguish evidence from inference, no fabricated section refs, stop at the recommendation). -->

Load-bearing across every <artifact>: every material claim cites a source from `references/source-anchors.md` (or a loaded overlay) by path; unsupported claims are marked `[evidence needed]`; section references that cannot be confirmed get `[verify section]` rather than fabricated; <skill-specific evidence-vs-inference rule>; the skill stops at <the gate, e.g., recommendation, draft for human attestation>.

Flexes to the engagement: depth and length scale to <tier or criticality>; audience drives shape (working group is plain, committee is structured, examiner response is formal, board is distilled); persona drives the review-gate machinery; sector and cross-cutting overlays load from engagement-scope. Where firm-specific policy or taxonomy applies, it lives in `references/firm-overlay.md` (consumed when present) and never in the artifact directly.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/{banking,insurance,capital-markets,payments-fintech}.md` — sector overlays loaded per engagement-scope.
- `references/cross-cutting/{cyber,privacy,climate,conduct}.md` — cross-cutting overlays loaded per engagement-scope.
- `references/firm-overlay.md` — firm-installed policy, taxonomy, review gates; consumed when present.
- `templates/default-output.md` — artifact template.
- `schemas/<skill-slug>.schema.json` — structured-output contract for downstream consumption.
- `examples/` — anonymised public-source-derived scenarios.
- `TROUBLESHOOTING.md` — recurring defects.

## Output

<!-- Name the artifact, the schema, and downstream consumers concretely. The schema is the cross-skill contract; additive changes only. Name downstream skills by slug, not by hand-wave. -->

The skill emits <artifact> in `templates/default-output.md` shape and a structured record conforming to `schemas/<skill-slug>.schema.json`. Downstream consumers: `<consumer-skill-1>` reads <named fields>; `<consumer-skill-2>` reads <named fields>; `<consumer-skill-3>` reads <named fields>. The schema is the cross-skill contract; additive changes only. Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream skills told in advance.
