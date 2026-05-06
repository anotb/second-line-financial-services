# risk-compliance-core — Phase 1 audit memo

Date: 2026-05-06
Phase: 1 (per-plugin scoping)
Plan: `docs/plans/2026-05-06-rationalized-plugin-map.md`

> **Mid-phase-1 amendment, 2026-05-06**: A seventh skill, `engagement-scoping`, has been added to this plugin per practitioner feedback. It is the bootstrapping primitive other skills consume to set institution, persona, source posture, risk lens, and overlay context. See `engagement-scoping.md` in this directory for the spec sheet. The plugin v1 list is now: `control-matrix`, `evidence-binder`, `engagement-scoping`, `human-review-gates`, `issue-writeup`, `obligation-mapping`, `policy-gap-review`.

## Plugin role

Foundational primitives reused by other capability plugins. Other plugins (compliance-testing, third-party-operational-resilience, regulatory-change-management, ai-governance-model-risk, risk-reporting, financial-crime-governance, consumer-compliance-fair-lending) import and extend these primitives rather than redefining them. This plugin is the canonical home for control matrices, evidence binders, obligation maps, issue write-ups, human-review gates, and policy gap reviews.

## v1 skill list (confirmed)

Six skills, all carried from v0.2:

1. `control-matrix`
2. `evidence-binder`
3. `human-review-gates`
4. `issue-writeup`
5. `obligation-mapping`
6. `policy-gap-review`

No deletions. No renames. No additions.

## Changes vs v0.2

- No skill changes inside this plugin.
- This plugin is reaffirmed as the canonical home for `issue-writeup`. The duplicate `issue-writeup` in `compliance-testing` is dropped under that plugin's own audit.
- All six SKILL.md files are currently boilerplate (same seven-step procedure with name swapped). Phase 2 rewrites content per the spec sheets in this folder.
- Source anchors today are bare URLs without section references. Phase 2 must add section references (or `[verify section]` placeholders) to every anchor; this is a v1 quality bar item.

## Disagreements with the plan

None. The skill list as proposed in the plan matches what a senior second-line practitioner would expect to find in a foundational primitives plugin. Two notes for phase 2 to keep in mind:

- `human-review-gates` is borderline a cross-cutting reference rather than a discrete artifact. It earns its keep because the artifact it produces (a named-gate matrix mapping decisions to required reviewers, criteria, and stop conditions) is reused as a standalone deliverable when firms stand up an AI or model governance committee charter, vendor onboarding gate, or issue-rating committee. Phase 2 should keep the artifact concrete (a matrix), not a discursive memo.
- `obligation-mapping` overlaps in shape with `regulatory-change-management/skills/rule-to-obligation-extraction`. The plan correctly keeps both — different inputs (any source document including policy and exam request, vs. a discrete piece of new rule text). Phase 2 description discipline (Best for / Not the right tool when) must keep the boundary clean so an agent does not invoke both for the same job.

## Plugin-level shared references

Stays plugin-level (foundational, referenced by every skill):

- `references/source-map.md` — the public-source map. Plugin-wide. Trim sections that are only used by one or two skills (move those into the skill's own `references/source-anchors.md` in phase 2). The current map is a near-duplicate of `common/references/source-map.md` and should be pruned to the rows actually relevant to this plugin's six skills.
- `references/policy-control-library.md` — the baseline risk taxonomy and control pattern. Plugin-wide. Used by `control-matrix`, `policy-gap-review`, `issue-writeup`. Keep here.
- `references/review-gates.md` — the named review gates and confidence labels. Plugin-wide. Used by every skill, especially `human-review-gates`. Keep here.

Moves per-skill in phase 2:

- `references/output-templates.md` — currently houses an obligation-map table, control-test workpaper outline, and executive risk pack outline. The obligation-map fragment moves into `obligation-mapping/templates/default-output.md`. The control-test workpaper outline does not belong to this plugin (it is `compliance-testing/skills/control-test-workpaper`) and should be removed here. The executive risk pack outline belongs to `risk-reporting/skills/risk-committee-pack` and should be removed here.
- `references/public-regulatory-scenarios.md` — currently a cross-plugin index pointing at `examples/public-regulatory/*`. This is a repo-level index, not a plugin-level reference. Move to `common/references/` or `docs/` in phase 3.

Schemas stay plugin-level under `schemas/` because multiple skills consume them. Specifically:

- `obligation.schema.json` — used by `obligation-mapping`, referenced by `policy-gap-review` and `control-matrix`.
- `control.schema.json` — used by `control-matrix`, referenced by `policy-gap-review`.
- `issue.schema.json` — used by `issue-writeup`, referenced by every other skill that surfaces gaps.
- `ai-use-case.schema.json`, `vendor.schema.json`, `test-plan.schema.json`, `risk-report.schema.json` — these belong to other capability plugins. Phase 3 should move them to their respective plugins (`ai-governance-model-risk`, `third-party-operational-resilience`, `compliance-testing`, `risk-reporting`). Until then, leaving them here as borrowed schemas is a structural concern, not a blocker.

## Structural concerns

1. `plugin.json` description currently lists the six skills inline. Keep the structure but tighten the wording in phase 3 to match the v1 positioning (foundational primitives reused by other capability plugins).
2. There is no `agents/` folder. Capability plugins do not require agents — that is the agent-plugins job. Confirmed correct.
3. There is no `examples/` folder under any of the six skills. Phase 2 must create `examples/<scenario>.md` per skill (two scenarios per spec sheet).
4. None of the six skills currently have a `references/` subfolder. Phase 2 creates `references/source-anchors.md` per skill, plus `references/cross-cutting/cyber.md` for `control-matrix` (already called out in the plan).
5. The current `argument-hint` is the same generic string across all six skills. Phase 2 should rewrite per skill (e.g., `"[obligation source: rule text, exam request, or policy]"` for `obligation-mapping`).
6. The current `description` frontmatter is malformed for activation purposes — it is one long sentence listing source URLs, not the activation-tuned `Best for` / `Not the right tool when` / `Anchored to` shape. Phase 2 fixes this per the spec sheet.

## Phase 2 readiness

All six skills have spec sheets in this folder:

- `control-matrix.md`
- `evidence-binder.md`
- `human-review-gates.md`
- `issue-writeup.md`
- `obligation-mapping.md`
- `policy-gap-review.md`

Each spec sheet contains the activation-tuned description, source anchors with section refs (or `[verify section]` placeholders), sector and cross-cutting overlay decisions, output template named sections, structured output fields, two example scenarios, and common pitfalls. Phase 2 subagents take the spec sheet as their contract.
