# Resume notes

Last updated: 2026-05-06, end of batch 2D-1, batch 2D-2 in flight.

This doc is for picking the build back up after a pause (token budget, rate limits, days off). Read it once and you should know the state, the design decisions, the open work, and how to dispatch.

## Where the build stands

- **Skills built clean against rules 1-4: ~57** (3 bench-build trio + 12 wave 1 + 12 batch 2A + 6 batch 2B + 13 batch 2C + 11 batch 2D-1).
- **In flight: batch 2D-2 (11 sector skills)**. When this batch lands, the build queue is closed. List of agent names: `w2d2-bank-fintech-partnership-review`, `w2d2-credit-risk-governance`, `w2d2-deposit-operations-controls`, `w2d2-adviser-exam-readiness`, `w2d2-best-execution-surveillance`, `w2d2-fund-board-reporting`, `w2d2-marketing-rule-evidence`, `w2d2-insurance-outsourcing-review`, `w2d2-life-health-pricing-governance`, `w2d2-fintech-partner-controls`, `w2d2-open-banking-data-controls`.
- **Quality baseline at end of 2D-1**: rule 1 (placeholder text) 253, rule 2 (description shape) 11, rule 3 (source-anchor depth) 11, rule 4 (duplicate-content pairs) 118. Down from pre-wave-1: 2,691 / 117 / 117 / 6,786.

## Repository layout

Root is now Anthropic-shaped:

- `plugins/capability-plugins/` (8 plugins), `plugins/sector-plugins/` (4 plugins), `plugins/agent-plugins/` (6 plugins).
- `docs/` — public-facing (architecture, source-map, test-strategy, conventions review, public examples).
- `scripts/` — `sync-agent-skills.py`, `check.py`, `check-skill-content.py`. Both check scripts are clean post-archive.
- `internal/` — research kept for future improvement.
  - `internal/specs/<plugin>/<skill>.md` — phase 1 spec sheet per skill (the contract for what each skill produces).
  - `internal/specs/<plugin>/AUDIT.md` — per-plugin audit memo.
  - `internal/reviews/` — phase 2 revision memos and the cleanup memo.
  - `internal/plans/` — rationalized plugin map + phase 2 build contract.
  - `internal/templates/skill-skeleton.md` — the v1 SKILL.md shape.
  - `internal/v0.2-archive/` — v0.2 root common/, examples/, tests/, run-content-tests.py.
  - `internal/RESUME-NOTES.md` — this file.

Each built skill folder contains:

- `SKILL.md` — the playbook
- `references/source-anchors.md` — cited regulatory anchors (named, dated, with section refs)
- `references/sector-overlays/<sector>.md` — sector flavor (banking / insurance / capital-markets / payments-fintech) where applicable
- `references/cross-cutting/<topic>.md` — cross-cutting flavor (cyber / privacy / climate / conduct) where applicable
- `templates/default-output.md` — content spec for the artifact
- `examples/*.md` — public-source-derived scenarios (optional)
- `TROUBLESHOOTING.md` — recurring defects (optional)
- `schemas/<output>.schema.json` — structured output contract (optional, only when downstream automation genuinely benefits)

## Design decisions (in order, with the reasoning)

These decisions were made over the course of the build and tightened multiple times. New work follows the latest version.

1. **Companion repo, not fork.** Positions as the second-line layer that complements anthropics/financial-services (which is first-line). README leads with this framing.
2. **US-deep v1, EU as overlays, UK as see-also.** Source map is US-anchored; EU and UK live in references where they apply.
3. **Capability plugins (8) + sector overlays (4) + standalone agent plugins (6).** Strict overlay rule: sector plugins ship sector-unique skills only; sector flavor on capability skills lives as a `references/sector-overlays/<sector>.md` reference inside the capability skill.
4. **Each agent plugin has primary `agent.md` + reader / critic / writer subagents.** Innovation over Anthropic's flat agent-plugin pattern. Cookbook-style YAML callable-agents (Anthropic's `managed-agent-cookbooks/`) are not in this repo; v1.1 may add 1-2 cookbook entries for upstream PR candidates (`ai-governance-reviewer`, `regulatory-change-analyst`).
5. **Scoping is the bootstrapping primitive.** New skill in `risk-compliance-core`. Produces a structured scope record every other skill consumes for institution profile, persona, source posture, sector and cross-cutting overlay sets. The schema is the canonical case for "schema where downstream automation genuinely helps".
6. **References-first design.** SKILL.md body uses generic regulator language. Specific regulator names and section refs live only in `references/source-anchors.md`. Sector-specific and cross-cutting nuance load conditionally based on the scope.
7. **No "Anchored to:" line in description.** Description shape is summary + `Best for:` + `Not the right tool when:`. Named regulators ride along with every activation if put in the description, polluting context for engagements that don't address those regulators. They belong in references, where they load conditionally.
8. **No "What's load-bearing and what flexes" section.** Engineer-speak meta-section. Non-negotiables (cite source, no fabrication, separate evidence from inference, human review gate, no named institutions) and adaptation guidance (audience, sector overlay loading, depth) bake inline in the workflow narrative.
9. **Schemas are optional.** Skip schema files unless the artifact has a structure that genuinely helps downstream automation (DORA register row mapping to EBA ITS table, scope record consumed across the repo, sanctions-screening alert payload). No shared `_defs.json` or cross-skill enum forcing — skills are for Claude to use, not regex-like output contracts.
10. **Deliverables are practitioner-natural formats: Word (docx), Excel (xlsx), PowerPoint (pptx).** Markdown is the content spec inside `templates/default-output.md`, not the deliverable. Skills define artifact substance and DELEGATE rendering to Anthropic's `document-skills` plugin. Same pattern Anthropic's `pitch-agent` uses.
11. **Voice picked per skill.** Anthropic's `comps-analysis` is judgement-shaped (conversational, "ask yourself first"); `dcf-model` is structured-artifact-shaped (numbered NON-NEGOTIABLE callouts, named fields). Match the voice to the work; scoping is judgement-shaped because scoping is judgement work, but a register builder or matrix is structured-artifact-shaped.

The full design plan is at `internal/plans/2026-05-06-rationalized-plugin-map.md`. The build contract is at `internal/plans/2026-05-06-phase2-build-contract.md`. The skeleton is at `internal/templates/skill-skeleton.md`. The four memories are at `~/.claude/projects/-Users-anot-Sync-code-second-line-financial-services/memory/feedback_*.md` — voice, practitioner lens, references-first, anti-AI-tells.

## The gold-standard skill

`plugins/capability-plugins/risk-compliance-core/skills/scoping/SKILL.md` is the canonical reference for the v1 sharpened rules. 72 lines. Everything that follows the sharpened rules models on it.

Do NOT model new skills on the older built skills. Many of them still carry `Anchored to:` lines, "What's load-bearing and what flexes" sections, or other pre-sharpening tells. They will get cleaned up in a retroactive pass.

## Open work

### Immediate (when 2D-2 lands)

- **Confirm 2D-2 closed cleanly.** Each agent reports rule-1-4 status. If any failed, spin up a finisher subagent for the missing pieces (the pattern from earlier batches: a "completer" subagent for missing files; a fresh build subagent if the SKILL.md was never written).
- **Commit 2D-2 outputs.** Standard git commit pattern: stage all, commit with a clear message naming the skills built, the rules followed, and the quality progression numbers.
- **Run the full validation sweep.** `python3 scripts/sync-agent-skills.py` then `python3 scripts/check.py` then `python3 scripts/check-skill-content.py`. All should pass. Capture the post-2D-2 baseline numbers.

### Retroactive cleanup (queued for a future session)

These items were noted during the build but explicitly not done so the build queue could close. They are not blocking.

- **Strip `Anchored to:` from description across ~49 built skills.** The sharpened rule (no Anchored-to in description) was added mid-build; older skills still have it. Mechanical fix: walk every `plugins/<type>/<plugin>/skills/<skill>/SKILL.md`, find the `Anchored to:` line in the description block, delete it. Keep the named regulators in `references/source-anchors.md` (they are already there in every built skill). One subagent can do all of these in a single pass.
- **Strip "What's load-bearing and what flexes" sections from older built skills.** Same kind of mechanical fix. Fold the substance inline into the workflow narrative where it belongs (cite-source rule into the evidence-reading paragraph, "stop at draft" into the closing paragraph). This is more substantive than the Anchored-to strip; will need careful per-skill judgement. Best as one subagent per plugin.
- **Convert markdown deliverables to Word/Excel/PowerPoint via `document-skills`.** All older built skills emit markdown. Update each SKILL.md's Output section to name the deliverable format and the rendering skill (`docx`, `xlsx`, or `pptx`). Update `templates/default-output.md` if the renderer needs a different shape. This is the largest retroactive cleanup. Best done plugin by plugin, with a fresh subagent per skill.
- **Strip schema enums.** Older skills with structured outputs use rigid enums (`severity`, `confidence`, `owner_role` as enum types). Convert to descriptive strings for backward compatibility with downstream skills that may emit different vocabulary. Lightweight; one subagent per plugin.
- **Drop `examples/` folder where the artifact is mechanical.** Several built skills have `examples/` folders that bloat the file count without adding value (control-matrix, DORA register, evidence-binder are mechanical artifacts where the template tells you everything). Audit per skill; remove where the example doesn't earn its place.

### Forward work (after retroactive cleanup)

- **v1.1 cookbook layer** for upstream PR candidates. Add `managed-agent-cookbooks/<agent>/` for `ai-governance-reviewer` and `regulatory-change-analyst` in Anthropic's exact format (`agent.yaml`, `subagents/<role>.yaml`, `steering-examples.json`, `README.md`).
- **Per-skill quality lift.** A second-line review pass on each skill (independent reviewer subagent compares against spec sheet, finds drift, drafts edits). The pattern for this is in `internal/reviews/scoping-revision-memo.md`, `model-card-builder-revision-memo.md`, `vendor-diligence-revision-memo.md`.
- **EU overlays expansion.** The current US-deep posture leaves EU coverage thin in many sector overlays. v1.1 broadens.
- **Eventually: GitHub publish.** Public-facing root is now clean (Anthropic-shaped). README needs a final polish pass before publish.

## How to dispatch agents

The pattern that worked across this build:

1. **Use Claude Code's `Agent` tool with `model: "opus"`** for build / review / cleanup work. `general-purpose` subagent type.
2. **Each subagent gets a self-contained brief.** Subagents have no context from the parent session. The brief points to the contract, the four memories, the gold-standard reference, the per-skill spec sheet, and the plugin AUDIT. Plus any sibling skills that chain or define boundaries.
3. **Run in parallel** (`run_in_background: true`). 11-13 in flight simultaneously is the sweet spot. 22 at once hit infrastructure throttling.
4. **Expect rate-limit pauses.** Anthropic's 5-hour budget window can hit on either end (account-level or infrastructure-level). When agents return with "Server is temporarily limiting requests" or "You've hit your limit", stop dispatching and wait for the reset. The fixer pattern (read what landed, dispatch finishers for missing pieces) handles partial output.
5. **Every batch followed by a commit.** Standard git commit message: `build: phase 2 batch <X> — <N> skills clean`. Include quality progression numbers in the body.
6. **Validation before declaring batch done.** `python3 scripts/check.py` should pass. `python3 scripts/check-skill-content.py` should show progressive reduction in violation counts.

When in doubt, look at how batch 2C and 2D-1 were dispatched (search for `w2c-` and `w2d1-` agent names in this session's history; the brief shape is reusable).

## Pipeline issues caught and fixed during the build

- `scripts/sync-agent-skills.py` was looking for the v0.2 root `common/` folder after we archived it. Fixed: removed the `COMMON` constant and the per-plugin `references` and `schemas` copy step that was failing.
- `scripts/check.py` had stale checks for v0.2 root `examples/` and root `schemas/`. Removed `check_public_examples()` and `check_schemas()`. Also fixed the multi-line YAML description parser (was treating `description: |` as a one-character value, causing every phase-2 skill to fail "description too short").
- `scripts/check-skill-content.py` rule 2 originally required all three of `Best for:`, `Not the right tool when:`, `Anchored to:`. Updated to drop the `Anchored to:` requirement when that line was removed from the design.

These fixes are committed; the scripts are clean.

## Watchouts when resuming

- **Anchored-to drift.** Even with explicit "no Anchored to" in the brief, ~10 of 11 batch-2D-1 builds reverted to including it. The agents pull from sibling skills that still have it. The retroactive Anchored-to strip closes the loop; until then, expect drift in any new builds.
- **Voice over-correction.** Agents that read the anti-AI-tells memory closely sometimes write SKILL.md files that anxiously avoid every banned word and end up sounding scrubbed. Read for confidence, not rule compliance.
- **References folder bloat.** Subagents under watchdog pressure create stub files because the skeleton has slots for them. Empty or near-empty sector overlays should be cut at review.
- **Schemas creeping back in.** Anything ending in `-register`, `-matrix`, `-pack`, `-binder` triggers the structure instinct. Reject schemas that don't have a named downstream consumer.

## Key files to read when resuming

- `STATUS.md` — public-facing summary (will need refresh post-2D-2).
- `internal/RESUME-NOTES.md` — this file.
- `internal/plans/2026-05-06-rationalized-plugin-map.md` — design plan with all major decisions.
- `internal/plans/2026-05-06-phase2-build-contract.md` — what every phase 2 build was held to.
- `internal/templates/skill-skeleton.md` — the v1 SKILL.md shape.
- `internal/reviews/pre-batch-2d-cleanup-memo.md` — pre-2D cleanup analysis.
- `internal/reviews/gold-standard-review-vs-anthropic.md` — independent review of the gold-standard against Anthropic's pattern.
- The four feedback memories at `~/.claude/projects/-Users-anot-Sync-code-second-line-financial-services/memory/feedback_*.md`.
- The gold-standard skill at `plugins/capability-plugins/risk-compliance-core/skills/scoping/SKILL.md`.

## What this build actually is

A second-line GRC plugin set for financial services, sized to be a credible companion to anthropics/financial-services. ~68 skills covering AI governance, model risk, third-party risk, operational resilience, compliance testing, risk reporting, financial crime governance, consumer compliance, regulatory change management, plus sector overlays for banking, insurance, capital markets, and payments-fintech, plus six standalone agent plugins that bundle the skills into end-to-end workflows.

Audience: second-line practitioners at regulated firms (CRO, head of model risk, head of TPRM, CCO, BSA officer) and advisory / consulting teams (Big Four, boutique GRC, internal-audit secondments). Posture: public regulatory sources only, defensible work product, every artifact stops at draft for human sign-off.

Build process learned a few things across the iterations: voice matters, prescription matters less than the right kind of prescription, schemas are not the deliverable, references load conditionally, and senior practitioners do not have meta-sections about what is mandatory.
