# compliance-testing — Phase 1 audit memo

Date: 2026-05-06
Phase: 1 (per-plugin scoping)
Plan: `docs/plans/2026-05-06-rationalized-plugin-map.md`

## Plugin role

Capability plugin for second-line and internal-audit control testing work product. Covers the full testing arc for a single control or test cycle: scope and plan, sample, evidence ask, walkthrough and procedure execution, exception classification, workpaper drafting, QA review. Issue write-up and downstream issue tracking live in `risk-compliance-core` (the foundational primitives plugin), not here. The plugin produces drafts for qualified review; it does not approve, file, rate, close, or release work product.

Audience: compliance-testing managers, internal-audit leads, controls assurance and second-line testing pods at regulated firms; the equivalent advisory teams (Big Four, boutique GRC, internal-audit secondments).

## v1 skill list (confirmed)

Six skills, dropping one from v0.2:

1. `control-sampling`
2. `evidence-request-builder`
3. `exception-analysis`
4. `qa-workpaper`
5. `test-plan-builder`
6. `workpaper-drafter`

Dropped: `issue-writeup`. Canonical home is `risk-compliance-core/skills/issue-writeup`. Duplicating it in this plugin fragments the issue lifecycle and conflicts with the foundational-primitives positioning.

## Changes vs v0.2

- `issue-writeup` removed from the v1 skill list. The existing `skills/issue-writeup/` folder, its `SKILL.md`, and `templates/` files in this plugin are scheduled for removal in phase 3. Do not delete now — the removal happens after phase 2 content build is complete and phase 3 re-bundles the agent plugins.
- All six remaining `SKILL.md` files are currently the v0.2 boilerplate (same seven-step procedure with name swapped). Phase 2 rewrites each per the spec sheets in this folder.
- Source anchors today are bare URLs without section references. Phase 2 must add named, dated sources with section references (or `[verify section]` placeholders). The spec sheets carry that forward.
- The `argument-hint` value is identical across all six skills; phase 2 should rewrite per skill.
- Description frontmatter today is one long sentence listing source URLs. Phase 2 replaces it with the activation-tuned `Best for / Not the right tool when / Anchored to` shape per the spec sheets.

## Disagreements with the plan

None. The skill list as proposed matches what a senior testing practitioner expects to find in a compliance-testing plugin: scoping (test plan), sampling, evidence asks, exception classification, workpaper drafting, QA review. Two notes for phase 2:

- The plan correctly keeps `test-plan-builder`, `workpaper-drafter`, and `qa-workpaper` as three separate skills. They are sequential, not redundant: pre-fieldwork / during-and-post-fieldwork / review-of-completed-workpaper. Each spec sheet states this boundary explicitly so an agent does not invoke the wrong one mid-cycle.
- `exception-analysis` ends with a structured handoff package to `risk-compliance-core/skills/issue-writeup`. Phase 2 must implement the handoff fields (the `issue_handoff` sub-object on the exception register) and reciprocally accept them on the `issue.schema.json` side. Without the handoff plumbing, the boundary between the two plugins becomes a friction point.

## Boundary calls

The four boundary calls phase 2 has to keep clean:

1. **`test-plan-builder` / `control-sampling` / `evidence-request-builder`** — three pre-fieldwork artifacts that compose. The test plan is the parent; sampling and evidence-request output are referenced by ID on the test plan. Phase 2 must implement the foreign-key fields (`sampling_id`, `evidence_request_list_id`) on `test-plan.schema.json`.

2. **`test-plan-builder` → `workpaper-drafter` → `qa-workpaper`** — the sequential testing lifecycle. The test plan is the contract for the workpaper; the workpaper is the input to QA. Each skill's "Not the right tool when" section names the others by skill ID so an agent does not pick the wrong one.

3. **`workpaper-drafter` ← `exception-analysis`** — the workpaper consumes an exception register classified by `exception-analysis`. The workpaper does not classify exceptions; it surfaces and aggregates them. Phase 2 should add `exception_register_id` as a foreign key on `workpaper.schema.json`.

4. **`exception-analysis` → `risk-compliance-core/skills/issue-writeup`** — the cross-plugin handoff. An exception elevated to issue status carries a populated handoff package (criterion, condition, cause, effect, recommendation seed). Phase 2 must coordinate with `risk-compliance-core` to add `source_exception_id` on `issue.schema.json`. Without this, every `issue-writeup` invocation re-discovers context that already exists upstream.

## Plugin-level shared references

Stays plugin-level (referenced by every or nearly every skill):

- `references/source-map.md` — public-source map. Plugin-wide. Trim sections that are only used by one skill (move those into the skill's own `references/source-anchors.md` in phase 2). The current map is largely a duplicate of `common/references/source-map.md`; phase 2 should prune it to the rows actually used by the six skills (IIA Standards, AICPA AU-C 230 / 330 / 500 / 530, FFIEC IT booklet, SR 08-8, OCC PPM 5310-3 [verify], CFPB CMS exam manual, COSO 2013 Principle 16/17).
- `references/policy-control-library.md` — baseline risk taxonomy and control pattern. Plugin-wide. Useful to all six skills as the firm-side analog of the source map. Keep here.
- `references/review-gates.md` — named review gates and confidence labels. Plugin-wide. Used by every skill for reviewer sign-off blocks and stop conditions. Keep here.

Moves per-skill in phase 2:

- `references/output-templates.md` — the control-test workpaper outline fragment relocates into `workpaper-drafter/templates/default-output.md`. The obligation-map fragment (currently sitting in this plugin) is `risk-compliance-core/skills/obligation-mapping` material and is being moved out under that plugin's audit. The executive risk-pack outline is `risk-reporting/skills/risk-committee-pack` material and should be removed from this plugin.
- `references/public-regulatory-scenarios.md` — repo-level index, move to `common/references/` or `docs/` in phase 3.

Schemas review:

- `test-plan.schema.json` — belongs here. Phase 2 expands it per the `test-plan-builder` spec sheet.
- New schemas Phase 2 must add: `sampling.schema.json`, `evidence-request.schema.json`, `exception.schema.json`, `workpaper.schema.json`, `qa-review.schema.json`. Each spec sheet specifies the wrapper structure.
- `obligation.schema.json`, `control.schema.json`, `issue.schema.json`, `ai-use-case.schema.json`, `vendor.schema.json`, `risk-report.schema.json` — these belong to other plugins (mostly `risk-compliance-core`). Borrowed presence here is a structural concern, not a blocker. Phase 3 cleans up.

## Structural concerns

1. `plugin.json` description lists the seven v0.2 skills inline. Phase 3 tightens the wording and drops `issue-writeup`.
2. There is no `agents/` folder. Capability plugins do not require agents. Confirmed correct.
3. None of the six skills currently have `references/` or `examples/` subfolders. Phase 2 creates `references/source-anchors.md` per skill, plus `references/cross-cutting/` and `references/sector-overlays/` where the spec sheet calls for them. Each skill needs `examples/<scenario>.md` for both example scenarios in its spec sheet.
4. The `issue-writeup` directory is still present and will be flagged by `scripts/check.py` if not addressed. Phase 2 leaves it alone (per instructions). Phase 3 removes it after the agent-plugin re-bundle confirms no agent plugin still imports it from this plugin.
5. Reviewer-separation is a recurring methodology bar across all six skills. The plugin-level `references/review-gates.md` should be the single source of truth for the named gates, and each skill's spec sheet references it rather than restating. Phase 2 should not re-document gates inside individual SKILL.md files.
6. The current generic `argument-hint` (`"[source files, policy text, rule text, data extract, or scenario]"`) is wrong for every skill. Phase 2 rewrites per spec sheet (e.g., for `control-sampling`: `"[control ID, population description, prior testing, or risk-based stratification factors]"`).

## Phase 2 readiness

All six skills have spec sheets in this folder:

- `control-sampling.md`
- `evidence-request-builder.md`
- `exception-analysis.md`
- `qa-workpaper.md`
- `test-plan-builder.md`
- `workpaper-drafter.md`

Each spec sheet contains:
- Activation-tuned description (Best for / Not the right tool when / Anchored to).
- Source anchors with named, dated standards and section references (or `[verify section]` placeholders).
- Sector-overlay decisions for banking, insurance, capital-markets, payments-fintech.
- Cross-cutting overlay decisions for cyber, privacy, climate, conduct.
- Output template named sections (practitioner-headings: Population definition, Sample size rationale, Tolerable deviation rate, etc., for sampling; standard testing workpaper sections for workpaper-drafter; QA review note structure for qa-workpaper).
- Structured output fields (typed wrappers and existing/new schema references).
- Two public-source-derived example scenarios per skill.
- Common pitfalls.

Phase 2 subagents take the spec sheet as their contract.
