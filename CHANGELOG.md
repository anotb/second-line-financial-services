# Changelog

## 1.0.3 — 2026-10-31

### Directory warnings cleared

Removes `icon`, `documentationUrl`, `supportUrl`, `privacyPolicyUrl`, and `termsOfServiceUrl` from `plugin.json`. The directory warned on them in every scan, and its listing recorded them at submission. `scripts/check.py` now fails if they return, or if the plugin uses phrases the scanner misreads.

### Docs for future releases

Adds `docs/releasing.md`, the release runbook for people and agents, and `AGENTS.md`. Stale references to the old 12-plugin layout are gone from the repo docs. `scripts/check-skill-content.py` Rule 3 now accepts a `Link:` bullet whose citation block has a section reference, as the roadmap called for.

## 1.0.2 — 2026-10-31

### Dead references removed

Five skills pointed at cross-cutting overlays that were never written. They now state the guidance directly or say no overlay exists. The scenario library's "Included example" paths, which were never in the plugin, now name the related skill.

## 1.0.1 — 2026-10-31

### Under the directory's file limit

The plugin goes from 852 files to 483, which clears the directory's hold on plugins over 512 files. No content is removed. In each skill, `references/sector-overlays/*.md` becomes `references/sector-overlays.md`, `references/cross-cutting/*.md` becomes `references/cross-cutting.md`, and `examples/*.md` plus `TROUBLESHOOTING.md` become `examples.md`, with one section per former file. Skills now say to read only the section they need. `scripts/check.py` fails if the plugin goes over 512 files.

## 1.0.0 — 2026-10-31

### One plugin

The 12 plugins are merged into `plugins/second-line-financial-services/`, so there is one thing to install and one listing to maintain. All 68 skills keep their names. Installs of the earlier plugins need to switch to this one.

- Shared `references/` and `schemas/` are merged: identical copies collapse, `risk-compliance-core`'s schema versions win, and differing references become one file with a section per group. Each old plugin README is now a guide under `references/groups/`.
- Cross-references such as `risk-compliance-core/skills/issue-writeup` now name the skill, `issue-writeup`.

### Short skill descriptions

Claude Code's skill listing budget is 1% of the context window, and it drops descriptions that don't fit. With 68 skills averaging 2,000 characters, most would have been dropped and stopped triggering. Each `description` is now 110 characters or fewer, and the full text, including `Best for:` and `Not the right tool when:`, moved to a `## When to use` section in the skill body.

## 0.5.0 — 2026-10-31

### Directory readiness

Prepares each plugin folder to be submitted on its own to Anthropic's plugin directory.

- Every plugin: `displayName`, listing icon at `assets/icon.png`, `LICENSE` file, `version` raised from 0.2.0 to 0.5.0 (the manifests had lagged the repo release), and `author.url`.
- Every README: `Try it` example prompts, a one-step install line, `Data and behavior`, and `Human review and AI disclosure`. `ROADMAP.md` links are now absolute because installs receive only the plugin folder.
- Every skill: a `Human review and AI disclosure` section that labels the deliverable as an AI-assisted draft, requires review by a qualified person, and requires telling an affected individual that AI was used.

- The inactive `.mcp.example.json` template moves out of every plugin folder to `docs/examples/mcp.example.json`, so installs carry no MCP configuration of any kind.

### `risk-compliance-core` dependency moved to the marketplace

`dependencies` moves from each `plugin.json` to its entry in `marketplace.json`. Installs from this marketplace still auto-pull `risk-compliance-core`. Directory copies no longer declare it: Claude Code keeps a plugin disabled when a declared dependency is missing, chat and Cowork ignore dependencies, and the skills only reference `risk-compliance-core` as an optional hand-off.

## 0.4.0 — 2026-05-09

### Manifest dependencies on risk-compliance-core

All 7 downstream capability plugins and all 4 sector plugins now declare `risk-compliance-core` as a bare-name dependency in `.claude-plugin/plugin.json`. Installing any one of them auto-pulls `risk-compliance-core` (and the `scoping` primitive). Refcount-aware: `claude plugin uninstall <plugin> --prune` removes `risk-compliance-core` only when no other plugin still requires it. Verified live against Claude Code 2.1.137.

### Pre-launch agentic eval and fix bundle

Eight-case validation eval (forked Opus maker subagent applies skill to a dummy brief; independent forked Opus checker reviews the output blind) covering 6 capability skills and the 2 most-used agent plugins. Findings: capability-skill layer is practitioner-grade; agent-plugin subagent layer is half-built (six-rule frontmatter stubs distinguished only by name; writer artifact shape and tool scope mismatched to program-level engagements; primaries under-prompt for engagement-level scoping moves).

### Standalone agent plugins pulled pending rebuild

Six agent plugins (`ai-governance-reviewer`, `regulatory-change-analyst`, `third-party-risk-reviewer`, `controls-testing-analyst`, `risk-reporting-analyst`, `financial-crime-governance-reviewer`) pulled from the marketplace pending a rebuild that adds a maker / checker loop with genuine context-isolated subagent forking, primary-plus-critic two-agent shape, engagement-level scoping prompts, and plugin dependencies in place of bundled-skill copies. See ROADMAP.

Marketplace manifest reduced from 18 to 12 entries (8 capability + 4 sector).

### New cross-cutting overlay: ai-ethics

`references/cross-cutting/ai-ethics.md` shipped to the 5 most load-bearing AI / model-risk skills: `genai-pre-prod-review`, `ai-use-case-intake`, `ai-risk-tiering`, `agentic-ai-controls`, `board-ai-risk-pack`. Per-skill tailored intro and pitfalls heading; body content matches existing `privacy.md` / `conduct.md` / `cyber.md` overlay structure (Source basis, Co-reviewer expectation, What changes when X is flagged with Open conditions / Monitoring readiness / Incident-response readiness / Recommended-action items, X-specific output additions, Common pitfalls). SKILL.md `Pointers` cross-cutting load list updated in all 5 skills to add `ai-ethics` to the brace expansion. Rollout to the remaining 6 AI / model-risk skills tracked in ROADMAP.

### New cross-cutting overlay: privacy for `dora-register-builder`

`references/cross-cutting/privacy.md` shipped at `dora-register-builder`. Threads GDPR (Articles 28, 30, 32, 35, 44-49, 25), SCCs (Decision 2021/914), EU-US DPF (with `[verify current adequacy status]`), EDPB Recommendations 01/2020 on supplementary measures, and national-supervisor data-protection guidance through the existing register fields (data classification, residency, sub-processor chain) without reshaping the artefact. SKILL.md `Pointers` updated to load privacy alongside cyber.

### Capability skill fixes from eval

- **`scoping`**: schema persona enum gains `compliance-risk-lead`; new optional `accountable_executive_role` field surfaces the running-lead vs accountable-executive split. SKILL.md and `templates/default-output.md` updated to name the split. Milestone block tightened from open list to defaulted three-row shape (kickoff, mid-engagement check, target completion); full sequencing pushed to the workplan.
- **`sar-decision-qa`**: new `templates/sample-roll-up.md` companion template for the sample-based QA review type. Matches `default-output.md` voice and shape; tracks the multi-item table pattern used in `complaint-theme-analysis` and `udaap-risk-review`. SKILL.md `Pointers` names both templates.
- **`fair-lending-test-plan`**: `templates/default-output.md` thickened to carry the per-test specification block (test ID, hypothesis, scope, methodology, sample, controls, decision points, evidence, AAN-coverage method) directly. Default-and-flag posture preserved; missing fields surface as `[evidence needed]` rather than blocking.
- **`dora-register-builder`** capital-markets sector overlay: new "National-supervisor outsourcing texts (alongside DORA)" section names CSSF Circular 22/806 (Luxembourg), KAGB plus BaFin MaRisk plus KAIT (Germany), AMF Position-Recommandation 2018-04 plus DOC-2014-13 (France), CBI Cross-Industry Guidance on Outsourcing 2021 (Ireland). Each entry hedged with `[verify section]` markers. New common-pitfall added: treating DORA as the sole outsourcing reference for UCITS / AIFM entities.
- **`genai-pre-prod-review`** conduct overlay: B2B-with-customer-flow-through trigger added as a third loading-rule bullet. Closes the trap where 1L declares a tool "internal-only" while the documents the tool acts on encode customer-facing obligations (contract content, regulatory correspondence, marketing assets, complaint files, regulatory submissions). Rollout to the other 8 conduct overlay files in `ai-governance-model-risk` tracked in ROADMAP.

## 0.3.0 — 2026-05-08

### Phase 2 editorial review (commit 5fd4cf6)

Per-plugin editorial layer (B1-B6) over Phase 1's mechanical cleanup. Voice principle: in SKILL.md body, regulators are grounding not focus. Heavy citation work (joint-guidance issuance metadata, footnote scope quotes, asset thresholds, supersession language, section / subpart numbers) consolidated into `references/source-anchors.md` and overlay files; skill bodies use natural practitioner framing.

- AI governance and model risk: April 2026 joint guidance verbatim language consolidated into `model-card-builder` source-anchors and banking overlay. OWASP LLM Top 10 refreshed to 2025 numbering (LLM01-LLM08) in `agentic-ai-controls` and `prompt-injection-risk`. EU AI Office Code of Practice refreshed from "in development" to published with 2 August 2025 GPAI effective date in `llm-vendor-evidence-review`. `agentic-ai-controls` regulator-perspective paragraph reordered: cyber regimes binding first, OWASP / MITRE ATLAS / NCSC / CISA primary, joint-guidance demoted to by-analogy. `ai-act-triage` Article numbers retained (legitimate legal-triage exception).
- Third-party and operational resilience: DORA Article 28(1)-(8) and Article 30(2)/(3) canonical structure landed in source-anchors. OCC 2013-29 demoted to historical. Commission Delegated Regs 2025/532 (sub-contracting RTS) and 2025/1190 (TLPT RTS) added. PRA SS1/21 / SS2/21 reframed.
- Compliance testing: OCC PPM 5310-3 framing corrected.
- Financial crime governance: `aml-model-monitoring` reframed as a model-scoping read.
- Risk reporting: SEC climate-rule current-state language refreshed.
- Consumer compliance and fair lending: `section1071-readiness` rebuilt around the May 1 2026 Section 1071 final rule.
- Financial crime governance: `sar-decision-qa` Red-tier reframed per October 9 2025 SAR FAQs.

### Phase 1 cross-cutting cleanup (commit 22dc202)

Six plugin-scoped sweeps (A1-A6) covering all 68 source skills.

- Removed `Anchored to:` paragraph from SKILL.md description blocks. Citations live in `references/source-anchors.md` rather than duplicated in the description.
- Split "What's load-bearing and what flexes" sections into a `Quality bar` block (invariants across every artifact) plus an `Adaptation` block (what flexes by engagement). Editorial folding pass deferred to Phase 2.
- Softened "review gates" terminology outside `human-review-gates` (which keeps the term as the artifact's subject) to decision forum / owner / conditions / attestation block / sign-off question / decision checkpoint by context.
- Format-flexible Output sections for the high-impact artifact skills: `vendor-diligence`, `criticality-assessment`, `contract-gap-review`, `exit-plan`, `resilience-testing-pack`, `control-matrix`, `evidence-binder`, `issue-writeup`, `policy-gap-review`, `control-sampling`, `exception-analysis`, `qa-workpaper`, `workpaper-drafter`. Default-to-template plus Word / Excel / PowerPoint / Markdown rendering per audience; structured record only when a downstream consumer needs it.
- Removed unsupported GenAI scope claims attributed to OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026 (April 17 2026 joint guidance). The bulletin expressly excludes generative AI and agentic AI from its scope (footnote 3); GenAI substantive anchors are NIST AI RMF 1.0, NIST AI 600-1, ISO/IEC 42001:2023, EU AI Act, OWASP LLM Top 10, MITRE ATLAS, NCSC / CISA secure-AI guidance, NYDFS October 2024 letter, and the NAIC AI Bulletin for insurers.
- FinCEN MSB BOI citation corrected from §1010.380 to §1022.380.

### Cross-skill audit and fix-applier (commit deae432)

Six-dimension consolidated cross-skill audit. Fixes:

- Schema field renames in the controls test pipeline: `analysis_id` → `exception_register_id`; `request_list_id` → `evidence_request_list_id`. Cross-skill foreign-key contracts declared on the renamed fields.
- Four broken cross-reference pointers repointed: `control-test-workpaper` → `workpaper-drafter`; `issue-management` → `issue-writeup`; `important-business-service-mapping` → `criticality-assessment` plus `resilience-testing-pack`.
- `ai-act-triage` cross-cutting overlay refs corrected: removed pointers to non-existent files (the cyber and privacy substance lives at Article level inside the body).
- Four prose em-dashes replaced.

### dora-register-builder light relabel + cross-cutting overlays + sweep finishers (commit d11e3b5)

- `dora-register-builder` repositioned as EU-DORA-context build pack and data-quality aid; not for direct submission to a national competent authority; not the official Register of Information template under Commission Implementing Reg (EU) 2024/2956. Preparation-grade only. Schema rebuild tracked in ROADMAP.
- Cross-cutting overlay obvious wins (B7): five new overlay files added (cyber for `evidence-binder`; privacy for `aml-model-monitoring`; privacy and conduct for `prompt-injection-risk`; conduct for `adverse-action-review`). Five plausible-coverage flags declined with rationale where the SKILL.md already inlined the substance or scoped it out.
- TROUBLESHOOTING + examples relevance audit (B9): zero deletions warranted; voice cleanup applied to retained files (em-dashes 1067 → 953; H1 heading em-dashes normalised; CFPB Circular withdrawal currency synced into seven referencing files).
- Partial currency sweep on five plugins.

### CFPB / BNPL / FDIC / SAR-FAQ / FinCEN / NIST / SEC currency sweep finishers (commit 12e8020)

Two follow-up agents picked up the residuals:

- B8a (BNPL plus bare CFPB circular tagging across the corpus, mechanical): CFPB Circular 2022-03 / 2023-03 inline withdrawal tag (May 12 2025) applied across the eight files where the cite was still bare; "per CFPB Circular X" prose softened to ECOA / Reg B § 1002.9 plus Comment 9(b)(2)-3 of the Official Staff Commentary as the operative anchor. BNPL Interpretive Rule "nullified by Pub. L. 119-11 (May 9, 2025); historical only" tag applied across twelve files. BNPL-as-product-scope mentions left alone.
- B8b (currency sweep across the six plugins B8 did not reach): financial-crime-governance, risk-reporting, banking-risk-compliance, payments-fintech-compliance, capital-markets-asset-management-compliance, insurance-risk-compliance updated. FinCEN Order FIN-2026-R001 (CDD exceptive relief, February 13, 2026); FinCEN BOI / CTA March 26, 2025 IFR (foreign-only reporting); investment-adviser AML rule compliance delay to January 1, 2028 (FinCEN final rule January 2, 2026); SAR FAQs October 9, 2025 inline tag; § 1033 stay (Forcht Bank, October 29, 2025) plus ANPR (August 22, 2025); § 1071 May 2026 revised final rule; NIST SP 800-61 Rev 3 (April 3, 2025); Names Rule corrected dates; FDIC Part 328 December 2023 final rule plus 2024-2025 effective-date extensions; SR 11-7 demoted to historical with joint guidance promoted to operative.

### Sector-flagship skill builds and small-items bundle (commit pending)

Three sector-flagship skills with no TROUBLESHOOTING and no example shipped (build queue closure gap, B9 flagged):

- `bank-fintech-partnership-review`: TROUBLESHOOTING (9 failure modes) plus a community-bank-BaaS-with-mid-sized-fintech example.
- `adviser-exam-readiness`: TROUBLESHOOTING (7 failure modes) plus a mid-sized IA pre-exam command-center example.
- `fintech-partner-controls`: TROUBLESHOOTING (8 failure modes) plus a payment-app-mid-sized-fintech sponsor-bank-side review example.

Small-items bundle (B11):

- Pack-schema field canonicalisation: `decision_items` → `decisions_requested` in risk-committee-pack schema. Practitioner framing: what does the audience need to decide.
- Reg E § 1005.11 timing rewrite in `deposit-operations-controls/references/cross-cutting/conduct.md`: 10 business days investigation; 45 calendar days extension with provisional credit; 90 calendar days extension for new accounts / POS / foreign-initiated transfers; 3 business days post-investigation notification.
- `banking-supervision-readiness` TROUBLESHOOTING (7 failure modes covering CSI access-population breach, MRA / MRIA conflation, CAMELS-component scope drift, Reg YY mis-attribution, Heightened Standards at non-OCC sponsor, LFI rating framework applied below threshold, closure-readiness without sustained evidence).
- `fund-board-reporting` second example: sub-adviser approval at a multi-manager fund under the trust's manager-of-managers exemptive relief (off-cycle, new-relationship, exemptive-order conditions).

### Modular install analysis (analysis only)

Read-only conceptual analysis. Confirms Claude Code v2.1.110+ supports `dependencies` in `.claude-plugin/plugin.json`. Maps the actual coupling (`risk-compliance-core` is a hub with 57 cross-references), eight practitioner personas with minimum-viable-install paths, four install-pattern options. Recommendation: Hybrid (Option D) in two stages (README install paths + manifest dependency declarations). Both stages tracked in ROADMAP.

### Other

- Renamed `engagement-scoping` to `scoping` and revised as the gold-standard reference.
- Switched from Apache 2.0 to MIT.
- ROADMAP refreshed: modular install Stages 1 and 2, dora-register-builder full rebuild, schema dedup, with per-item rationale.

## 0.2.0

- Removed managed-agent cookbook content.
- Replaced vertical source taxonomy with capability and sector plugin groups.
- Added standalone agent subagents under each agent plugin.
- Replaced example set with public-source-derived regulatory scenarios.
- Added common policy, risk, control, source, review-gate, and output-template references.
- Added validation and sync scripts.

## 0.1.0

- Initial scaffold.
