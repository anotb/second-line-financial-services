# Rationalized plugin and skill map (v1)

Date: 2026-05-06
Status: Proposed. Pending sign-off before agent dispatch.
Audience: Second-line practitioners (financial-services firms, advisory and consulting firms).

## Why this rev

The v0.2 layout has the right shape: horizontal capability plugins, sector overlays, self-contained agent plugins, public-source-anchored references. The shape is sound. The content is not. Across the 78 skills today, every `SKILL.md` is the same generic seven-step procedure with only the name and description swapped. The plugin-level shared references are real and properly cited. The per-skill content is empty.

This plan does three things.

1. Consolidates the 78 skills, removes duplicates, tightens the cuts so each skill earns its place.
2. Pushes sector and cross-cutting context (cyber, privacy, climate, conduct) inside the skills that touch them, instead of standing up new plugins for topics that are really subsets of existing functions.
3. Sets a per-skill anatomy that matches the Anthropic pattern observed in `anthropics/financial-services`, so any single skill can be lifted into their repo as a focused contribution later, without dragging the rest of the repo with it.

The repo's positioning stays the same: companion to `anthropics/financial-services`, focused on the second-line layer that sits over their first-line workflows (investment banking, equity research, private equity, fund admin, wealth management, KYC operations).

## v1 audience and voice

Primary audience is two practitioner groups:

- Second-line teams inside regulated firms: model risk, AI governance, third-party risk, operational resilience, compliance testing, financial crime governance, consumer compliance, risk reporting.
- Advisory and consulting teams running second-line work for those firms: Big Four, boutique GRC, internal audit secondments, regulatory consulting.

Both groups recognise the same vocabulary (obligations, controls, evidence, gaps, issues, exam readiness, attestations, MRA, MRIA, criticality, exit plan, register of information, BCBS 239, SR letters, OCC bulletins, CFPB circulars, NYDFS, FFIEC, FinCEN, EU AI Act, DORA). The skills should sound the way a senior risk officer or partner would write the equivalent memo. Not academic, not marketing, not engineer-speak.

Agent and subagent vernacular is fine. Practitioners are getting comfortable with primary agent, subagent, orchestrator, callable agent, leaf worker, tool boundary. Use those terms naturally; do not over-explain. Where a software concept needs to land in a knowledge-work context, translate it (a shared schema is a structured output template; a manifest is a configuration file; drift is the same idea practitioners already use for control drift).

## What changes versus v0.2

### Plugin count

Same plugin count. Eight capability plugins, four sector overlays, six standalone agent plugins. Topics that looked like candidate plugins (cyber, climate, privacy, conduct) become embedded reference content inside the skills that already touch them.

Reasons:

- Each topic is a subset of existing second-line functions, not a free-standing review function. Cyber sits across third-party risk, operational resilience, control testing, and committee reporting. Adding a separate cyber plugin would fragment work that practitioners run as one motion.
- A flatter map is easier to discover and easier to install. Visibility comes from depth and clarity, not from an inflated plugin count.
- Sector and cross-cutting nuance lives where it is actually applied: inside the skill that produces the artifact.

### Strict sector overlay rule

Sector plugins ship sector-unique skills only. Skills that already exist in capability plugins do not get duplicated under a sector plugin. Sector flavor is captured as a reference document inside the relevant capability skill, for example:

`plugins/capability-plugins/ai-governance-model-risk/skills/ai-act-triage/references/sector-overlays/insurance.md`

This kills duplicates such as `insurance-ai-act-triage` and `claims-ai-controls`. It also clarifies what is genuinely sector-only and worth a dedicated skill: life and health pricing governance, best execution surveillance, deposit operations controls, and similar.

### Skill consolidations and renames

- Drop `issue-writeup` from `compliance-testing`. It already lives in `risk-compliance-core`, where the foundational primitives belong.
- Drop `ai-vendor-review` from `ai-governance-model-risk`. Add an "AI vendor" mode to `vendor-diligence` in `third-party-operational-resilience`. AI vendors are a scenario of vendor diligence, not a separate workflow.
- Drop `insurance-ai-act-triage` and `claims-ai-controls` from `insurance-risk-compliance`. The capability skills (`ai-act-triage`, `agentic-ai-controls`) absorb insurance overlay reference docs.
- Keep `board-ai-risk-pack` and `risk-committee-pack` separately. Different audiences (AI committee versus enterprise risk committee). Both reference the shared committee-pack template under `risk-reporting`.
- Keep `obligation-mapping` (capability primitive) and `rule-to-obligation-extraction` (regulatory-change-management) separately. Same shape, different inputs: any source document versus a discrete piece of new rule text.

### GenAI expansion in `ai-governance-model-risk`

Add four GenAI-specific skills, drop the consolidated `ai-vendor-review`:

- `prompt-injection-risk` — second-line review of prompt injection threat surface for a deployed GenAI use case.
- `rag-evaluation-review` — second-line review of retrieval and grounding evaluation for a RAG deployment.
- `genai-pre-prod-review` — pre-production gate review for a GenAI use case before initial release.
- `llm-vendor-evidence-review` — review of large-model-vendor evidence packs (system cards, evaluation reports, red team results) against firm criteria.

This is the bucket with the most regulator activity in 2025-26 (NIST AI RMF generative profile, NYDFS October 2024 guidance on GenAI cybersecurity, OCC and FRB supervisory letters, EU AI Act general-purpose AI obligations, ISO/IEC 42001 implementation pressure). It is also the most discoverable bucket for the repo.

After the swap, `ai-governance-model-risk` has eleven skills:

`ai-use-case-intake`, `ai-risk-tiering`, `ai-act-triage`, `model-card-builder`, `validation-plan`, `agentic-ai-controls`, `board-ai-risk-pack`, `prompt-injection-risk`, `rag-evaluation-review`, `genai-pre-prod-review`, `llm-vendor-evidence-review`.

### Cross-cutting reference content

Each cross-cutting topic becomes embedded reference material inside the skills it touches.

Cyber:

- `risk-reporting/skills/cyber-disclosure-readiness/references/source-anchors.md` (SEC cyber 8-K, FFIEC IT booklet, NYDFS Part 500).
- `third-party-operational-resilience/skills/vendor-diligence/references/cross-cutting/cyber.md`.
- `third-party-operational-resilience/skills/exit-plan/references/cross-cutting/cyber.md`.
- `risk-compliance-core/skills/control-matrix/references/cross-cutting/cyber.md`.

Climate:

- `risk-reporting/skills/risk-committee-pack/references/cross-cutting/climate.md` (SEC climate disclosure rule, TCFD-aligned reporting).
- `risk-reporting/skills/cyber-disclosure-readiness/references/cross-cutting/climate.md` for the disclosure machinery overlap.

Privacy:

- `third-party-operational-resilience/skills/vendor-diligence/references/cross-cutting/privacy.md` (GLBA Safeguards, CCPA / CPRA, state privacy laws).
- `consumer-compliance-fair-lending/skills/marketing-claim-review/references/cross-cutting/privacy.md`.
- `consumer-compliance-fair-lending/skills/adverse-action-review/references/cross-cutting/privacy.md`.

Conduct:

- `financial-crime-governance/skills/edd-escalation-pack/references/cross-cutting/conduct.md`.
- `consumer-compliance-fair-lending/skills/udaap-risk-review/references/cross-cutting/conduct.md`.
- `consumer-compliance-fair-lending/skills/complaint-theme-analysis/references/cross-cutting/conduct.md`.

The published skill remains the workflow. The reference document is the criteria the workflow applies. Practitioners installing the skill receive the criteria as part of the installation.

## Design principle: references hold the regulator, SKILL.md holds the workflow

Updated 2026-05-06 mid-phase-1 per practitioner feedback. SKILL.md is the workflow the skill performs — scoping, evidence gathering, analysis, output assembly, review gates. SKILL.md cites references by file path; it does not restate regulatory text or enumerate citations beyond the activation-tuned description's "Anchored to:" line. All regulator-specific content (cited excerpts, section references, dated source links, sector overlays, cross-cutting overlays) lives in `references/` and changes there without modifying the playbook.

Maintenance benefit: when SR 11-7 next gets revised, the change is one reference file, not seventy SKILL.md files. Customization benefit: a firm overlaying its internal policy on a skill adds a `references/firm-overlay.md`; it does not fork the skill. Same goes for an advisory firm shipping a client-specific overlay or a regulator-specific overlay.

The phase 2 content quality check enforces this. New rule: SKILL.md flagged if it contains regulatory citations or text excerpts not present in `references/source-anchors.md` and not part of the activation-tuned description. The script can be relaxed if a phrase is doctrinally part of the workflow (e.g., "issue an MRA"), but verbatim regulatory excerpts in the playbook fail the check.

## New primitive: engagement-scoping

Added 2026-05-06 mid-phase-1 per practitioner feedback. The repo gains one new primitive in `risk-compliance-core`, bumping that plugin from 6 to 7 skills:

`engagement-scoping` — produces a structured engagement context that other skills consume. Output covers:

- **Institution profile** — type (bank holding company, national bank, state member bank, savings association, broker-dealer, investment adviser, registered fund, insurance company, money transmitter, fintech, sponsor-bank program, mutual, credit union, public company), asset size, charter, registrations, geographic footprint, primary regulator constellation.
- **Engagement profile** — type (internal second-line review, advisory engagement, exam-readiness sprint, audit support, model validation engagement, regulatory change implementation, board-pack preparation, exception remediation, vendor onboarding review), timeframe, sponsor, audience, deliverable shape.
- **Persona profile** — practitioner role and function (CRO, head of model risk, head of TPRM, head of operational resilience, CCO, BSA officer, AI governance lead, head of regulatory affairs, head of internal audit, partner / engagement lead at advisory firm, embedded business risk officer 1.5-line), decision rights, review gates.
- **Source posture** — public-only, public-plus-firm-policy, public-plus-firm-policy-plus-system-of-record-evidence, connector-aware.
- **Risk lens** — which risk types are in scope (credit, market, liquidity, operational, strategic, reputational, model, climate, cyber, conduct, financial crime, consumer compliance, third-party, ICT).
- **Sector overlay set** — which of {banking, insurance, capital-markets, payments-fintech} apply.
- **Cross-cutting overlay set** — which of {cyber, privacy, climate, conduct} apply.

Downstream skills accept `engagement-scope` as optional input. When present, the skill tailors its sector and cross-cutting overlay loading, its evidence asks, its review-gate set, and its tone. When absent, the skill asks or defaults. Both 1.5-line and 2-line workflows benefit; advisory engagements use the scope rigidly, internal teams use it lighter, both produce traceable artifacts.

`engagement-scoping` is the natural first skill called in any non-trivial second-line engagement. The output is a reusable engagement charter that the engagement keeps and revises as scope shifts.

## Per-skill anatomy

This is the v1 standard for every skill folder. It mirrors the pattern in `anthropics/financial-services/plugins/vertical-plugins/<vertical>/skills/<skill>/`:

```
<skill-name>/
  SKILL.md                       # the playbook the agent follows
  references/
    source-anchors.md            # cited excerpts, named regulatory sources, with section refs
    sector-overlays/             # only where the skill has sector-specific nuance
      banking.md
      insurance.md
      capital-markets.md
      payments-fintech.md
    cross-cutting/               # only where applicable
      cyber.md
      privacy.md
      climate.md
      conduct.md
  templates/
    default-output.md            # named-section template for the artifact this skill produces
  schemas/
    <output>.schema.json         # structured output fields for the artifact
  examples/
    <public-source-derived>.md   # one to three worked examples
  scripts/                       # optional: validators, citation checkers, link checkers
  TROUBLESHOOTING.md             # optional: common pitfalls
```

Three things matter most.

- `SKILL.md` is skill-specific, not the generic seven-step template. It explains how a second-line reviewer actually does this piece of work, with the artifact in mind.
- `references/source-anchors.md` contains real cited excerpts from the named regulatory source, with section references where they exist. URL alone is not sufficient.
- `examples/` is concrete enough that a partner or chief risk officer can read the input, read the output, and decide whether the skill is doing the right thing.

A skill written this way is also the natural unit of an upstream contribution. A single self-contained skill folder, with its references, templates, schemas, and examples, can be lifted into a new vertical of the Anthropic repo (proposed: `risk-and-compliance`) without touching the rest of this repo.

## Skill description discipline

The skill description is the activation contract: it is how Claude decides when this skill is the right tool. The current descriptions in v0.2 are formulaic and look the same across all 78 skills. Anthropic's descriptions in `comps-analysis` and similar are activation-tuned: they list when the skill is the right tool and when it is not.

Every skill in v1 gets a description with this shape:

```
[One-line summary of what the skill produces.]

Best for:
- [Concrete trigger 1]
- [Concrete trigger 2]

Not the right tool when:
- [Concrete anti-trigger 1]
- [Concrete anti-trigger 2]

Anchored to: [Named regulatory sources, dated.]
```

Example for `model-card-builder`:

```
Drafts a model card for a financial-services AI or model use case, with intended use, training and reference data, performance, limitations, monitoring plan, controls, and sign-off questions.

Best for:
- A first-line owner has proposed an AI use case and second-line needs the model card before a tier decision or pre-prod gate.
- A model risk team is refreshing model cards as part of an annual model inventory exercise.

Not the right tool when:
- The use case has not been intaked yet (use ai-use-case-intake first).
- Validation testing has not run (use validation-plan; the model card consumes its outputs).

Anchored to: SR 11-7 §V model documentation; OCC Bulletin 2026-13 (revised interagency model risk management guidance, 2026); NIST AI RMF 1.0 Map function; ISO/IEC 42001:2023 §7.5 documented information.
```

This change alone improves discovery quality. It also gives reviewers a written contract for what each skill should and should not do.

## Agent plugin pattern (kept)

The six standalone agent plugins keep their primary plus reader, critic, and writer subagent shape. The Anthropic analogous pattern in `managed-agent-cookbooks/<agent>/subagents/*.yaml` uses callable-agent manifests (researcher, modeler, deck-writer; transcript-reader, model-updater, note-writer; doc-reader, rules-engine, escalator). Same conceptual roles:

- Reader: read-only ingestion of evidence and source documents.
- Critic: second-line challenge function. Compares evidence to source criteria and surfaces gaps.
- Writer: assembles the reviewable artifact. The only subagent with write permission.

Tool boundaries are enforced at the subagent level. The reader can read only. The critic can read only. The writer can read and write. This mirrors how a real second-line review pod operates.

The bonus PR pathway: v1.1 can layer on a `managed-agent-cookbooks/` subtree with cookbook entries (`agent.yaml`, `subagents/<role>.yaml`, `steering-examples.json`, `README.md`) for one or two agents in Anthropic's exact format. The CLAUDE.md note about not adding cookbook scaffolding to the main path stays in force; cookbooks for upstream contribution live in their own subtree, isolated from the rest of the repo.

## Quality bar

Every skill in v1 must clear all of these before being marked done.

1. `SKILL.md` is skill-specific. No two `SKILL.md` files share more than half their text.
2. `references/source-anchors.md` cites named, dated regulatory sources with section references where they exist (for example, SR 11-7 §V; OCC Bulletin 2026-13 §III.A; CFPB §1071, 12 CFR 1002.107). URLs alone are not sufficient.
3. The default-output template is the actual artifact shape a regulator or auditor expects, not a generic table.
4. Structured output fields match the template fields.
5. At least one worked example using public-source-derived material. No named institutions unless they are public defendants in a finalized enforcement action with a published consent order.
6. Description is activation-tuned (Best for / Not the right tool when / Anchored to).
7. Voice is FS or consulting practitioner. Not academic, not marketing, not engineer.

The existing `scripts/check.py` validates plugin shape. v1 adds a content quality check that flags formulaic-sounding `SKILL.md` content and missing description shape.

## Phased agent dispatch

Two phases, each running multiple agents in parallel. Each "agent" here is a Claude Code Task subagent dispatched from the main session with a tightly scoped brief.

### Phase 1: per-plugin scoping pass (12 subagents, parallelisable)

One lead subagent per capability plugin and per sector plugin. Each lead does:

1. Reads the current state of its plugin (`SKILL.md` files, references, schemas, README).
2. Confirms its skill list against this plan (deletions, renames, additions).
3. For every skill in the final list, writes a one-page spec sheet to `docs/specs/<plugin>/<skill>.md` covering:
   - Activation-tuned description (final wording).
   - Source anchors specific to this skill (named, dated, with section references).
   - Sector overlays needed.
   - Cross-cutting overlays needed.
   - Output template named sections.
   - Structured output fields.
   - Two example scenarios (public-source-derived).
   - Common pitfalls.
4. Tightens the plugin-level shared references so they do not duplicate skill-level references.
5. Updates the plugin README.

Output of phase 1: 12 plugin audit memos and roughly 70 skill spec sheets in `docs/specs/`. This is the contract for phase 2.

### Phase 2: per-skill content build (~70 subagents, parallelisable)

One subagent per skill. Each takes its spec sheet and produces:

- `SKILL.md`
- `references/source-anchors.md`
- `references/sector-overlays/*.md` where applicable
- `references/cross-cutting/*.md` where applicable
- `templates/default-output.md`
- `schemas/<output>.schema.json`
- `examples/<scenario>.md`
- `TROUBLESHOOTING.md` where applicable
- `scripts/<validator>.py` where applicable

Each is independent because the spec sheet is the contract.

### Phase 3: re-bundle, validate, and content quality sweep

- Run `scripts/sync-agent-skills.py` to re-bundle skills into the six standalone agent plugins.
- Run `scripts/check.py` for shape validation.
- Run a new content quality check that flags formulaic `SKILL.md` drift.
- Update each agent plugin's primary `agent.md` to reflect the new skill list.
- Update root `README.md`, `STATUS.md`, `ROADMAP.md`, `CHANGELOG.md`.

### v1.1: cookbook layer for upstream PR

Add `managed-agent-cookbooks/` with one or two cookbook entries in Anthropic's exact format. Strongest candidates:

- `ai-governance-reviewer` — cleanest fit with Anthropic's agent style; high regulator interest; low overlap with their first-line agents.
- `regulatory-change-analyst` — clean output, strong source-anchor story, complements their existing first-line workflow agents.

## Decisions made (2026-05-06)

D6. Phase 1 runs 12 subagents (capability plus sector only). The six agent plugins are downstream consumers of capability plugin skills and are handled in phase 3, not phase 1.

D7. The content quality check is added now, with starter rules that ban v0.2 placeholder text patterns and missing description shape. This gives phase 2 subagents an automated check to run before declaring a skill done.

D8. The v1.1 cookbook upstream-contribution candidates are `ai-governance-reviewer` and `regulatory-change-analyst`.

D9. CLAUDE.md is updated to: "Managed-agent cookbooks are not in scope for the main path. Upstream-contribution cookbooks, if any, live under `managed-agent-cookbooks/<agent>/` and are excluded from the marketplace manifest and from `scripts/sync-agent-skills.py`." `docs/architecture.md` is updated to match.
