# Pre-batch-2D cleanup and streamlining memo

Date: 2026-05-06
Author: pre-batch-2D reviewer
Audience: orchestrator dispatching the final 22 skills
Status: punch list. No skill content rewritten here.

The build is in good shape. 46 skills clean, validation green, plugin-level shared references already in place. The memo below is a list of nudges to make batch 2D cheaper and to leave the corpus marginally tidier than it is today. Most items are 30-minute fixes the orchestrator can do before dispatch; a few are guardrails for the briefs themselves.

## 1. Cross-skill consistency check

### Voice and length

The bench-build trio is still the cleanest. `scoping/SKILL.md` (82 lines), `vendor-diligence/SKILL.md` (76 lines), `model-card-builder/SKILL.md` (118 lines) hit the right register: senior, terse, prose-where-prose-belongs, sequencing-where-it-matters. The 2A and 2B builds mostly hold the line. 2C drifts longer in two specific directions and the orchestrator should call this out:

- `agentic-ai-controls/SKILL.md` (135 lines) is the longest body in the corpus. The body has the right substance but sprawls because every named section gets a paragraph and the `## What's load-bearing and what flexes` section turns into a 16-bullet checklist. By comparison `vendor-diligence` (also a complex artifact) holds two paragraphs for load-bearing-vs-flexes and trusts the reader.
- `concentration-risk-review` (125 lines), `bcbs239-gap-assessment` (126 lines), `udaap-risk-review` (122 lines), `fair-lending-test-plan` (121 lines) all run long for similar reasons (every output section gets two paragraphs).

This is a soft drift. The 2D brief should give a target: aim for 90 to 120 lines for body. Compress `What's load-bearing` to two paragraphs, not bullet-by-bullet enumeration.

### Description shape

Most descriptions are activation-tuned correctly with all three markers (`Best for:`, `Not the right tool when:`, `Anchored to:`). The activation-tuning quality varies:

- Clean (post-sharpening, type-only `Anchored to:`): `model-card-builder` ("SR 11-7, OCC Bulletin 2026-13, NIST AI RMF, NIST AI 600-1 (Generative AI Profile), ISO/IEC 42001, EU AI Act Article 11 and Annex IV"), `vendor-diligence`, `genai-pre-prod-review` ("US interagency model risk guidance, NIST AI RMF, NIST AI Generative AI Profile, ISO/IEC 42001, EU AI Act high-risk-deployer obligations…"), `llm-vendor-evidence-review`, `kri-commentary`. These read as activation triggers, not citation manifests.
- Drifted (specific section refs and `[verify section]` markers in the description): `agentic-ai-controls/SKILL.md:19` packs section refs (`§IV-V`, `Manage 2.7 / 2.8 / 4.1`, `§4.F`) AND `[verify subcategory numbering]` AND `[verify section]` into the Anchored-to line. This is the rule the references-first sharpening was supposed to kill. `udaap-risk-review/SKILL.md:20`, `fair-lending-test-plan/SKILL.md:18`, `cdd-risk-review/SKILL.md:18`, `regulatory-impact-assessment/SKILL.md:18`, `implementation-plan/SKILL.md:19`, `ai-act-triage/SKILL.md:18`, `ai-risk-tiering/SKILL.md:16` all enumerate specific articles, sections, or `[verify section]` flags in the description.

Why this matters: the description is what Claude reads on every activation decision. Pollution noise costs context budget across every invocation. Cleanup is mechanical: strip section refs, leave the named-source list, delete `[verify section]` markers from the description. This is one of the high-leverage cleanup actions below.

### Body genericness (post-references-first)

The bench-build trio and the 2C-clean ones (`vendor-diligence`, `model-card-builder`, `genai-pre-prod-review`, `kri-commentary`) keep the body in generic regulator language ("the named regulatory anchors", "the supervisory expectation"). A handful of 2A and 2C builds drift back into US-specific language in the body — `agentic-ai-controls` body names "NYDFS Part 500 §500.6", "FFIEC IT Handbook Information Security booklet", "12 CFR Part 53 (banking 36-hour rule)" in the workflow paragraphs (lines 73, 75). These should sit in the cyber overlay, not in the body. The body for any UK or EU engagement currently loads US-only context as noise.

This is harder to fix mechanically because it requires moving content into overlays. Flag for cleanup at phase 3, not pre-batch-2D. But the 2D brief should reinforce the rule.

## 2. Reinvention and DRY opportunities

The plugin-level shared references already exist (`source-map.md`, `policy-control-library.md`, `review-gates.md`, `output-templates.md`, `public-regulatory-scenarios.md`) under every plugin's `references/` root. They are inconsistently consumed by SKILL.md. `vendor-diligence` references them explicitly at line 72; most other skills do not. This is fine for v1 (the files are there for any skill to consult) but represents a missed DRY opportunity that 2D could close.

### Specific shared assets that would reduce 2D rework

- **JSON Schema $defs library at plugin level.** Every per-skill schema today re-defines: `severity_enum` (low / medium / high / critical), `confidence_label` (high / medium / low / unknown), `source_trace_entry` (claim, source, evidence_pointer, confidence), `human_review_gate` (gate name, criterion, required reviewer, stop condition), `owner_role_enum` (function names; never individuals). Propose: a `schemas/_defs.json` per plugin that 2D schemas $ref into. Cuts schema-drafting effort and forces consistency. The orchestrator can also pre-write this single file before dispatch.
- **A SKILL.md skeleton.** The shape is now stable: frontmatter (name, description with three markers, argument-hint), one-paragraph overview, "Ask first" (3 to 5 prompts), workflow (the long part), "What's load-bearing and what flexes" (two paragraphs), pointers, output. Ship a 60-line skeleton in `internal/templates/skill-skeleton.md` and link it from the brief. The agent fills in section by section instead of re-deriving the shape.
- **Plugin-level "shared sector overlay anchor" file.** Every banking overlay across skills says the same five things at the top: applicable interagency guidance, FFIEC manual position, NYDFS scope where chartered, federal-banking confidential-supervisory-information regimes, and the 12 CFR Part 30 Appendix D heightened-standards posture. Propose: `references/sector-overlays/_banking-anchors.md` at plugin root naming these five things; per-skill `references/sector-overlays/banking.md` opens with a one-line `Anchored to: see references/sector-overlays/_banking-anchors.md` and then carries skill-specific banking content. Same pattern for insurance, capital-markets, payments-fintech.
- **Standard frontmatter blocks.** The argument-hint pattern `"[noun, noun, or scope statement]"` is consistent. A two-line snippet in the brief saves 2D agents from inventing.

### What not to over-DRY

Per-skill `Ask first` lists, workflow narratives, and example scenarios should stay per-skill. These carry the practitioner judgement that distinguishes one skill from the next. Trying to share these would flatten the value.

## 3. Reference-content duplication audit

Looking at `references/source-anchors.md` across skills:

- SR 11-7 is cited in at least 11 SKILL.md files (every AI-governance-model-risk skill plus model-risk-touching skills in financial-crime-governance, third-party, regulatory-change). Each of those source-anchors files repeats roughly the same SR 11-7 paragraph (development / validation / governance, three-component model risk).
- OCC Bulletin 2026-13 follows the same pattern across the same files.
- The interagency third-party guidance (June 2023) is cited across the seven third-party-resilience skills plus vendor-diligence-adjacent skills. Same paragraph.
- BCBS 239 is repeated across `bcbs239-gap-assessment`, `risk-committee-pack`, `evidence-binder`, `kri-commentary`, `attestation-pack`, `obligation-mapping`, `model-card-builder` (where it is referenced in the description).
- CFPB UDAAP Examination Manual paragraph repeated across `udaap-risk-review`, `fair-lending-test-plan`, `marketing-claim-review` (spec), `complaint-theme-analysis` (spec), `adverse-action-review` (spec).

Propose a per-plugin **anchor library** at `plugins/<type>/<plugin>/references/anchor-library.md` that names the anchors and excerpts once. Per-skill `references/source-anchors.md` shifts to: skill-specific excerpts of the anchor (the paragraph or sentence the skill leans on for its specific workflow) plus a `See plugin anchor-library.md for the full citation` line. Saves drafting time and ensures the anchor text stays consistent across the plugin.

Practical: this is a phase-3 refactor (touches every built skill). For 2D, do the lighter version: tell the agent "if this anchor is already in `plugins/<plugin>/references/source-map.md`, cite it by path and add only the skill-specific excerpt; do not re-write the full citation." The plugin-level `source-map.md` already exists in every plugin and already lists most anchors.

## 4. The 22 remaining skills: cuts, merges, sharpening notes

I read the spec sheets for the boundary-overlap candidates the brief flagged. None of the 22 are candidates for cutting. All have distinct artifacts, distinct audiences, and distinct statutory frames. The spec-sheet authors were already disciplined about boundary documentation. Specific reads:

- **`sanctions-screening-qa` vs `sar-decision-qa`.** Different artifact. Sanctions QA is real-time list-match QA (list management, fuzzy thresholds, 50-percent rule, FP rationale). SAR QA is suspicion-based behavioral review (typology fit, SAR narrative, escalation chain). The spec sheet documents this. Build both.
- **`aml-model-monitoring` vs `ai-governance-model-risk` siblings.** Boundary clear. The spec calls out: AML monitoring covers AML-specific monitoring governance (segmentation, scenario tuning, BTL testing, FFIEC SAR-side downstream effects); general model risk primitives (model definition, model inventory, validation framework) live in `ai-governance-model-risk`. The skill consumes those. No overlap to resolve.
- **`edd-escalation-pack` vs `cdd-risk-review` (built).** Sequence chain. CDD is baseline due-diligence review; EDD is the escalation pack the EDD committee reviews when CDD flags. The spec documents the chain. No overlap.
- **`adverse-action-review`, `complaint-theme-analysis`, `marketing-claim-review`, `section1071-readiness`.** All four are needed. Different artifacts (notice review, theme aggregation, marketing-asset review, readiness assessment), different rules (Reg B §1002.9, CFPB CMS, Reg Z + UDAAP, §1033 / 1071), different audiences. The "Not the right tool when" sections in the specs already cross-reference each other cleanly. Build all four.
- **`qa-workpaper` vs `workpaper-drafter` (built).** Sequence chain documented in spec: `test-plan-builder` (pre-fieldwork) → `workpaper-drafter` (during/post-fieldwork) → `qa-workpaper` (review of completed workpaper). Three sequential skills, not duplicates.
- **`evidence-request-builder` vs `evidence-binder` (built).** Different artifacts. Evidence-request builds the PBC list at fieldwork start; evidence-binder is the reviewable closure pack at the end. Spec documents the boundary.
- **`bank-fintech-partnership-review` vs `payments-fintech/fintech-partner-controls`.** Same partnership, opposite lenses. Bank-side principal-supervisory pack with §1867(c), Reg O / Reg W / Reg E / Reg DD vs fintech-side self-evidence pack for the sponsor bank's TPRM file. Both AUDIT memos document this clearly. Build both.
- **`adviser-exam-readiness` vs capability `exam-brief` (built).** Sequence chain. `exam-brief` is regulator-agnostic engagement playbook (entry meeting, document-handling, request-letter format). `adviser-exam-readiness` is the SEC-specific readiness sprint with IA Act / Exchange Act / FINRA rule lattice and EXAMS document-request playbook. Spec explicitly says the two chain. Build the SEC-specific skill.

### Sharpening notes the briefs should carry

- **`open-banking-data-controls`**: §1033 status note discipline — the spec mandates a `s1033_status_note` field. The agent must propagate the status-note pattern as a structured field, not narrative; this is a known phase-2 risk per the AUDIT memo.
- **`payment-operations-incident-review`**: explicit defer-to-cyber-disclosure-readiness for the cyber-leg; the spec carries this discipline; the brief should restate so the agent does not duplicate cyber-disclosure work.
- **`aml-model-monitoring`**: must explicitly call out that AML transaction monitoring IS in scope as a model under SR 11-7 / OCC 2026-13 (the most common AML-side mistake is treating it as "rules", not as a model). The spec's pitfall #1 names this. The brief should highlight.
- **`marketing-claim-review`**: spec already cross-references `complaint-theme-analysis` and `udaap-risk-review`. Brief should remind the agent that the asset-level scope (one creative, one campaign) is the unit of analysis; product-level UDAAP belongs next door.
- **Sector skills with paywalled rules** (NACHA, card networks, FedNow / RTP): the spec mandates a "current edition; verify against firm's licensed copy" disclaimer on every artifact citing these. Brief must restate; this is an easy thing to miss.

## 5. Streamlined batch-2D brief template

Current 2A/2B/2C briefs run 500 to 700 words. Most of that is restating the build contract. Trim to 350 words.

```
# Brief: <skill-name>

You are building one skill: <skill-name> in <plugin>.

Pre-reads (MUST read before drafting):
- Build contract: internal/plans/2026-05-06-phase2-build-contract.md
- Spec sheet: internal/specs/<plugin>/<skill-name>.md
- Reference patterns to mirror (pick by skill character):
  - Judgement-heavy: plugins/capability-plugins/risk-compliance-core/skills/scoping/SKILL.md
  - Structured artifact: plugins/capability-plugins/ai-governance-model-risk/skills/model-card-builder/SKILL.md
  - Diligence pack: plugins/capability-plugins/third-party-operational-resilience/skills/vendor-diligence/SKILL.md
- Skeleton: internal/templates/skill-skeleton.md (pre-fill it; do not re-derive shape)

Anti-AI-tells (the rules with most repeat violations):
- Description Anchored-to line: NAMED SOURCES ONLY. No section refs. No [verify section] markers. The line is for activation, not citation.
- SKILL.md body uses generic regulator language. No US-only section references in the workflow paragraphs. Specific section refs go in references/source-anchors.md only.
- Body length target: 90 to 120 lines. If you are over, the "What's load-bearing" section is probably the offender; compress to two paragraphs.
- Default and flag, do not gate. Skills work with what they have.
- Drop fake-precision ranges, marketing adjectives, hedge tics, repetition across sections.

Outputs (per the build contract; no empty stubs):
- SKILL.md
- references/source-anchors.md (skill-specific excerpts; cite plugin source-map.md by path for repeated anchors)
- references/sector-overlays/<sector>.md (only sectors with skill-specific nuance)
- references/cross-cutting/<topic>.md (only topics that apply)
- templates/default-output.md
- schemas/<output>.schema.json ($ref into plugin schemas/_defs.json for shared enums)
- examples/ (one to three; public-source-derived; no named institutions outside public consent-order defendants)
- TROUBLESHOOTING.md (optional)

Validation (must pass before declaring done):
- python3 scripts/check-skill-content.py --plugin <plugin> with zero violations on this skill
- Self-check: count [verify section] markers in SKILL.md (should be 0 in description, 0 in body for the activation-tuned line; OK in source-anchors.md)

Watchdog: 600 seconds. Write smallest files first (schema, examples), SKILL.md and source-anchors last.
```

That is roughly 320 words including the code block. Drop any restatement of the contract; agents read the contract.

## 6. Light pre-batch cleanup tasks

These are the high-leverage things the orchestrator can do before dispatching 2D. Maximum 2 hours of work; biggest return is item 1.

1. **Strip Anchored-to drift in the seven offending built SKILL.md files.** The drift list: `agentic-ai-controls`, `ai-act-triage`, `ai-risk-tiering`, `udaap-risk-review`, `fair-lending-test-plan`, `cdd-risk-review`, `regulatory-impact-assessment`, `implementation-plan`. For each, edit the description's `Anchored to:` line to the type-only pattern (named regulatory sources, no section refs, no `[verify section]` markers). Keep the section refs in `references/source-anchors.md`. This is a mechanical edit, 5 minutes per file. It also removes activation-time context noise across every invocation.
2. **Pre-write the schemas/_defs.json per plugin.** Standard enums (severity, confidence, owner_role) and shared object shapes (source_trace_entry, human_review_gate). Five minutes per plugin x 12 plugins = 1 hour. Then 2D agents `$ref` into them instead of redefining.
3. **Pre-write `internal/templates/skill-skeleton.md`.** Frontmatter + the standard body section headers in order, with one-line guidance per section. 30 minutes. Cuts every 2D agent's bootstrapping.
4. **Update the build contract's "watchdog discipline" section** to add: "Pre-fill the skill-skeleton; do not re-derive shape." And add the `[verify section]`-in-description rule explicitly to the contract's tasteful-prescription section (it is implied today via the references-first sharpening but is being missed).
5. **Update `STATUS.md`.** It still reads as if v0.2 is the state of play. Document phase 2 progress (46 of 68 skills built clean) and the references-first sharpening as a v1 lock.
6. **Run `python3 scripts/sync-agent-skills.py`** if you have not since the last 2C build. The agent plugins re-bundle from capability skills; if 2C added skills that agent plugins claim, the sync may be stale. (Check `plugins/agent-plugins/*/skills/` for agent-side stub SKILL.md files dated before the latest capability skill build; the sync script regenerates these.)
7. **Skip the placeholder-content failures on unbuilt skills.** `check-skill-content.py` flags 1135 violations across the unbuilt-skill stubs that still carry v0.2 boilerplate. This is expected (the stubs are about to be overwritten by 2D). Do not "fix" them; let 2D agents replace them. But add a `--exclude-unbuilt` flag to the script if it is easy, so post-2D check is meaningful.

## 7. Watchdog and rate-limit lessons

### Batch sizing

W1 (12 skills) shipped clean. 2A (12) shipped clean. 2B (6) shipped clean. 2C (13) had occasional length sprawl but no failures. The pattern: 12 to 13 skills per batch is the comfortable size; 6 is comfortable but expensive in dispatch overhead.

22 skills in one push is too many. The skills span seven plugins and four sectors; coordination overhead spikes with that span. Recommend splitting:

- **Batch 2D-1 (12 skills, capability-heavy)**: financial-crime-governance (4), consumer-compliance-fair-lending (4), compliance-testing (2), payments-fintech-compliance (2: `open-banking-data-controls`, `payment-operations-incident-review`).
- **Batch 2D-2 (10 skills, sector-heavy)**: banking-risk-compliance (3), capital-markets-asset-management-compliance (4), insurance-risk-compliance (2), payments-fintech-compliance (1: `fintech-partner-controls`).

Why this split: capability skills consume capability-side anchors (already well-trodden in W1 / 2A / 2B / 2C); sector skills consume sector-side anchors (most of which are still being shaken in). Run the capability-heavy batch first so any anchor-library-mode cleanup from item 6 can land before sector skills fire. Sector skills are also the ones most likely to want the new shared `_banking-anchors.md` / `_payments-fintech-anchors.md` patterns.

### Patterns from agent reports that signal trouble

- "Schema is large" — usually means the agent is restating shared enums inline. Fix is `_defs.json` (item 6.2 above).
- "AI overlay branch needed" — usually means the spec calls out a GenAI branch and the agent is confused whether it should fold into the body or create a separate overlay. The pattern from `vendor-diligence` (the AI-vendor branch is real and surfaces a conditional `ai_specific_findings` block in-line) and `model-card-builder` (the GenAI overlay block fires inside named sections) is the model. Brief should reference these.
- "Watchdog timeout" — almost always SKILL.md drafting time. Mitigation: write schema and examples first per the contract; SKILL.md last. The skeleton (item 6.3) speeds drafting.
- "Section refs uncertain" — agent gets stuck verifying. Mitigation: brief is explicit that `[verify section]` belongs in `source-anchors.md` only, never in body or description. Move on; do not re-research.

### Final disposition

Build 2D-1 first. Run the 30-minute cleanup pass (items 1, 2, 3) before dispatching. Run check-skill-content.py with the unbuilt-exclude flag after each sub-batch lands. Hold the sector-heavy 2D-2 dispatch until the capability sub-batch is in and the sector overlay anchor-library files (item 2.3 / 6.7) are tidy.

— end memo —
