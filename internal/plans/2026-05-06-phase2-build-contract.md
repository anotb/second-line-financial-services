# Phase 2 build contract

Date: 2026-05-06
Status: contract for every phase 2 subagent. Read this before producing any skill content.
Plan: `docs/plans/2026-05-06-rationalized-plugin-map.md`

This contract is the constraint set for building one skill. It is short on purpose. The substantive direction lives in the per-skill spec sheets in `docs/specs/<plugin>/<skill>.md` and the project memory referenced below.

## Read first

- The plan: `docs/plans/2026-05-06-rationalized-plugin-map.md`. The amendment sections "Design principle: references hold the regulator, SKILL.md holds the workflow" and "New primitive: engagement-scoping" are mid-phase-1 additions you must follow.
- The project memory under `~/.claude/projects/-Users-anot-Sync-code-second-line-financial-services/memory/` — voice and audience, 1.5/2-line lens, references-first design, locked v1 decisions.
- The plugin's audit memo at `docs/specs/<your-plugin>/AUDIT.md`.
- The spec sheet for your skill at `docs/specs/<your-plugin>/<your-skill>.md` — that is the contract for what your skill produces.
- The anthropics/financial-services pattern for prescription level. `gh api repos/anthropics/financial-services/contents/plugins/vertical-plugins/financial-analysis/skills/comps-analysis/SKILL.md` is the canonical example. Note how `comps-analysis` opens with **"ALWAYS ask yourself first"** prompts, lists a "DO use" / "DO NOT use" pattern, and frames non-negotiable rigidity (formulas over hardcodes) sharply while leaving format and audience adaptation to context. That tone is the target.

## Tasteful prescription

The single most important rule for phase 2: skills guide Claude. They do not force rigid behavior on situations we have not fully thought through. Over-prescription is the failure mode to avoid. **A skill that reads like a process gauntlet has failed.**

The companion memory `feedback_anti_ai_tells.md` is required reading before you draft `SKILL.md`. The headline rules:

- **Default and flag, do not gate and stop.** Skills work with the inputs they have and note the defaults in `assumptions_and_dependencies` (or the equivalent). They do not block on missing inputs except where a load-bearing precondition genuinely fails.
- **No `[verify section]` markers in SKILL.md or in the activation-tuned description's "Anchored to:" line.** Verification flags belong in `references/source-anchors.md`.
- **Description's "Anchored to:" line names source TYPES, not sections.** Good: "US interagency model risk guidance, EU AI Act, NIST AI RMF, ISO/IEC 42001". Not good: "SR 11-7 §V, OCC Bulletin 2026-13 §III.A". The description is for activation triggering. Section refs go in references only.
- **SKILL.md body uses generic workflow language. No specific regulator names in narrative.** The body talks about "the named regulatory anchors", "the supervisory expectation", "the firm's regulator constellation". When the engagement scope flags a regulator, the skill loads the matching reference file. Embedding US-only sections in the body pollutes context for engagements addressing other regulators.
- **Sequencing where the order actually matters; not as structure for its own sake.** Claude executes the skill at runtime, so explicit sequencing is helpful where there is a real dependency chain (e.g., tier the model before setting model-card depth; gather upstream artifacts before drafting). What fails is padding — "10-step workflow" when the work has a spine, not ten dependent steps; numbered steps for parts that can run in any order; "Step 1: Confirm what triggered the engagement" when the trigger is obvious from the input. Test each numbered step: does the next step depend on this one's output? If not, fold into prose or a flat list.
- **Drop fake-precision ranges.** "Three to five exclusions", "three is normal, five is a stretch", "in 5-10 minutes", "Tier-1 cards have 12 sections" — these are AI tells. Empirically grounded numbers (e.g., "Reg E gives 10 days for provisional credit") stay; comfort-precision ranges go.
- **Drop engineer-voice tics.** "Fail the quality bar", "schema drift breaks the rest of the repo", "the chase is the work" — practitioner voice does not talk like that.
- **Drop marketing adjectives.** Comprehensive, robust, leverage, ensure, facilitate, streamline, optimize, enhance, holistic — practitioners write around these. So do you.
- **Drop hedge tics.** "It is worth noting", "you may want to consider", "important to note" — if it matters, just say it.
- **No repetition across sections.** Say it once in the place it belongs.
- **Pick one or two non-negotiables that genuinely matter and let the rest read as expected practice.** Repeated "must", "mandatory", "required", "non-negotiable" turns the skill into a compliance form.

The non-negotiables that DO stay across the repo: cite a source for material claims, separate evidence from inference, do not fabricate regulatory facts, no named institutions outside public consent-order defendants, the skill stops at draft (one mention is enough).

What this means in practice:

**Rigid where rigidity matters** (state these as non-negotiable in SKILL.md):
- Every material claim cites a source. Mark unsupported claims `[evidence needed]`.
- Separate source evidence, management assertions, public-source obligations, generated inferences, and open legal or compliance questions. The artifact shows the seams.
- Human review gate before any final action — approval, filing, customer communication, vendor onboarding, model release, SAR filing, issue closure. The skill stops at draft.
- No fabricated regulatory facts. If a section reference is unknown, write `[verify section]`. Do not invent.
- No named institutions in examples unless they are public defendants in a finalized enforcement action with a published consent order.

**Flexible where flexibility matters** (state these as "ask yourself first" or "adapt to context"):
- Artifact format depth — committee pack might be slides for the board, a memo for the working group, a one-pager for the CRO. Ask the audience.
- Sector tailoring — the engagement scope drives which sector overlay reference doc the skill loads. Skill consults the engagement scope or asks if missing.
- Cross-cutting overlays — same logic. Cyber, privacy, climate, conduct enter the skill's analysis when the engagement scope flags them.
- Tone and length — a partner-facing brief is not a board minute is not an examiner-response file. Adapt.
- Firm overlays — if a `references/firm-overlay.md` exists, consume it. If not, default to public posture.

The model: `comps-analysis/SKILL.md` opens with explicit "ALWAYS ask yourself first" prompts (preferred format, audience, key question, context). Mirror that pattern. The skill is a senior practitioner walking through how they approach the work — including the decision points where they ask the engagement lead before continuing.

## Per-skill output (the file set)

For each skill you build, produce:

```
plugins/<type>/<plugin>/skills/<skill>/
  SKILL.md                              # the workflow playbook
  references/
    source-anchors.md                   # cited excerpts, named sources, dated, with section refs
    sector-overlays/                    # only files for sectors where this skill has nuance
      banking.md
      insurance.md
      capital-markets.md
      payments-fintech.md
    cross-cutting/                      # only files for cross-cutting topics that apply
      cyber.md
      privacy.md
      climate.md
      conduct.md
  templates/
    default-output.md                   # named-section template for the artifact
  schemas/
    <output>.schema.json                # structured fields for downstream consumption
  examples/
    <public-source-derived>.md          # one to three worked examples
  TROUBLESHOOTING.md                    # optional: common pitfalls
  scripts/                              # optional: validators, link checkers
```

Files only when needed. If the skill has no insurance overlay, do not write `sector-overlays/insurance.md`. If the skill has no scripts, do not write a `scripts/` directory. Empty stubs fail the quality bar.

## SKILL.md contract

What goes in:

1. Frontmatter:
   - `name`: skill name.
   - `description`: activation-tuned. One-line summary, then "Best for:" (concrete triggers), "Not the right tool when:" (concrete anti-triggers), "Anchored to:" (named, dated regulatory sources at the top level — no excerpts).
2. Body:
   - Overview — one paragraph on what the skill produces and who consumes it.
   - "Ask yourself first" prompts — three to five questions a senior practitioner asks before starting (audience, scope, source posture, decision being supported, time pressure). Pattern from `comps-analysis`.
   - Engagement scope integration — if `engagement-scope` (per `risk-compliance-core/engagement-scoping`) is supplied, consume it; if not, ask the practitioner the relevant questions or default to public posture.
   - Workflow — the actual steps the skill performs, with the decision points called out. This is the bulk of the file.
   - Non-negotiable rigidities — flagged sharply. Citation, separation, no fabrication, human review gate.
   - Adaptation guidance — what to flex on (audience, depth, format, sector, cross-cutting).
   - Pointers to references — `references/source-anchors.md` for citations, `references/sector-overlays/<sector>.md` for sector flavor when the engagement scope flags that sector, `references/cross-cutting/<topic>.md` for cross-cutting overlays, `references/firm-overlay.md` if a firm has installed one.
   - Output handoff — what the skill emits, what schema it conforms to, what reviewer signs off.

What stays out:

- Verbatim regulatory excerpts. Those go in `references/source-anchors.md`.
- Citation lists beyond the description's "Anchored to:" line.
- Named institutions in narrative.
- Sector-specific text when the skill is a capability primitive — that goes in `references/sector-overlays/<sector>.md`.
- Engineer vocabulary. Practitioner voice, per the voice memory.

Length: long enough to do the job, short enough to read. `dcf-model/SKILL.md` is dense and detailed because the skill is technical; `comps-analysis/SKILL.md` is conversational because the skill is judgment-heavy. Match your skill's character.

## references/source-anchors.md contract

For each named regulatory source the skill anchors to:

- The full citation (named, dated, with section reference if it exists).
- A one-paragraph excerpt or paraphrase of what the source says that this skill relies on.
- The link.
- A `[verify section]` flag if you do not know the exact section reference.

This is the file the firm overlays. A firm-specific anchor lives in `references/firm-overlay.md`, never in this file or in SKILL.md.

## templates/default-output.md contract

The artifact's actual named sections, in practitioner vocabulary. Not a generic table. Examples:

- For `model-card-builder`: `## Intended use`, `## Training and reference data`, `## Performance summary`, `## Limitations and known failure modes`, `## Monitoring plan`, `## Controls`, `## Sign-off questions`.
- For `dora-register-builder`: section headings aligned to the EBA ITS Register of Information tables.
- For `risk-committee-pack`: `## Heat map by risk type`, `## Top risks`, `## Material risk events`, `## KRI movement and breaches`, `## Issues and remediation status`, `## Forward-looking commentary`, `## Decision items`.

The template is a starting structure with placeholder content, not a forced shape. The artifact adapts to audience and engagement scope. Practitioners will edit the template down or up depending on context.

## schemas/<output>.schema.json contract

JSON Schema. Strict-typed, but generous on optional fields. The schema captures the artifact in a form downstream skills can consume programmatically (e.g., a register builder produces a JSON list of vendor entries that exit-plan can consume).

## examples/ contract

One to three worked examples. Each is a Markdown file with:

- Input description (2-3 sentences on the scenario).
- Output sketch (what the skill emits — abbreviated, not the full artifact).
- Why this scenario matters (what edge case or boundary it tests).

Public-source-derived only. Named institutions only when they are public defendants in a finalized enforcement action with a published consent order.

## Validation before declaring done

The skill must pass `python3 scripts/check-skill-content.py --plugin <plugin>` with zero violations on the skill being built. Specifically:

- Rule 1 (placeholder-text ban): zero hits.
- Rule 2 (description shape): "Best for:", "Not the right tool when:", "Anchored to:" all present.
- Rule 3 (source-anchor depth): `references/source-anchors.md` exists; every URL bullet has a section reference or a `[verify section]` placeholder.
- Rule 4 (duplicate-content): no other SKILL.md in the repo overlaps more than 50% with this one.

If you cannot resolve a `[verify section]` flag, leave it. Phase 2 carries verification load forward; phase 3 grinds it down. Fabrication fails the quality bar.

## Watchdog discipline

Subagent watchdog kills at 600 seconds without progress. Strategies that worked in phase 1:

- Plan the file list before writing. Know what you are producing.
- Write the smallest files first (schema, examples) so partial completion is recoverable.
- Save SKILL.md and source-anchors last so the rest exists if you stall.
- Do not over-research. The spec sheet has the source list; the activation-tuned description has the anchored-to list. You are not rediscovering regulation.

## engagement-scoping integration

If your skill is `engagement-scoping` itself, you are setting the bootstrapping pattern.

Otherwise: your SKILL.md should include an "Engagement scope" subsection with two paths:

- **Engagement scope supplied** — consume the structured engagement-scope record. Use `institution.type` and `institution.primary_regulators` to set tone and citation focus. Use `sector_overlay_set` to load the matching `references/sector-overlays/<sector>.md`. Use `cross_cutting_overlay_set` to load matching `references/cross-cutting/<topic>.md`. Use `persona.role` to set the artifact audience and review gate. Use `source_posture` to set evidence asks.
- **Engagement scope not supplied** — ask the practitioner four questions: institution type, primary regulator(s), persona/audience, source posture. Default to public posture if the practitioner declines. Note in the artifact that scope was not formalized.

The engagement-scope is consultative input, not a hard precondition. The skill works without it.

## Customization posture

Skills are designed for adoption by firms with their own policy, taxonomy, and overlays. The customization surface is the references directory:

- `references/firm-overlay.md` — firm-specific policy, taxonomy, review gates beyond the regulatory baseline. The skill consumes this when present.
- `references/sector-overlays/` — sector-specific nuance that the firm can extend.
- `references/cross-cutting/` — cross-cutting nuance that the firm can extend.
- A consulting firm shipping a client overlay does the same thing under a separate overlay file.

Never hardcode a firm name, policy line, threshold, owner, or system in SKILL.md. Those are runtime inputs or firm-overlay content.

## Voice reminder

Senior, terse, regulator-aware. Practitioner vocabulary (obligations, controls, evidence, gaps, MRA, MRIA, criticality, exit plan, register of information). Not academic, not marketing, not engineer-speak. No em-dashes. The voice memory is the canonical reference.
