# Post-build action register

Date: 2026-05-09 (updated)
Status: rolled up from Phase 1 sweeps (A1-A6), Phase 2 editorial review (B1-B6), Phase 5 audit, the citation verification dossier, the modular install analysis, the engagement-scoping → scoping rename, the MIT license switch, the dora-register-builder relabel, the README and docs polish, and the follow-up agents (B7 overlay obvious wins, B8 / B8a / B8b currency sweep, B9 TROUBLESHOOTING and examples relevance audit, B10a-c sector-flagship skill builds, B11 small-items bundle). Source for each line is captured below so a reader can trace any decision to the work that produced it.

The point of this file: nothing the analysis surfaced should drop on the floor. Items are tagged **done**, **open**, **watch**, or **deferred** with a clear next move.

---

## Done in this build cycle

### Voice and structure (Phase 1, six sweeps A1-A6, commit 22dc202)

- Removed `Anchored to:` paragraph from SKILL.md description blocks across 68 source skills. Citations live in `references/source-anchors.md`.
- Replaced "What's load-bearing and what flexes" with `## Quality bar` and `## Adaptation` blocks. Editorial folding pass ran in Phase 2.
- Softened "review gates" terminology outside `human-review-gates` (which keeps the term as the artifact's subject) to decision forum / owner / conditions / attestation block / sign-off question / decision checkpoint.
- Format-flexible `## Output` rewrites for the high-impact artifact skills.
- Synced to agent-plugin bundles via `scripts/sync-agent-skills.py`.

### Voice editorial layer (Phase 2, six reviews B1-B6, commit 5fd4cf6)

Per-plugin editorial pass over Phase 1's mechanical cleanup. Voice principle: in SKILL.md body, regulators are grounding not focus. Heavy citation work consolidated into `references/source-anchors.md` and overlay files. Highlights documented in CHANGELOG 0.3.0; full per-skill notes preserved in the per-plugin agent reports.

### Citation verification dossier

Read-only verification of 28 currency-of-citation claims against official sources. 25 confirmed, 3 partial, 0 wrong. Lives at `internal/research/citation-verification-2026-05-08.md`. Notable: OCC Bulletin 2026-13 footnote 3 explicitly excludes generative AI and agentic AI from scope; FRB SR 26-2 and FDIC FIL-15-2026 are the same joint document not parallels; FinCEN MSB registration is at 31 CFR §1022.380 not §1010.380 (which is the BOI / CTA reporting rule); NAIC Model #880 stays correct as the unfair-discrimination / pricing anchor (only the claims-handling mis-use needed the swap to Model #900); Reg E timing is 10 business days investigation, 45 / 90 calendar days extension.

### engagement-scoping → scoping rename + MIT license (commit aa4500c)

Renamed the bootstrap skill for audience clarity ("engagement" reads as consulting argot). ~1,100 cross-references updated. Schema field renames (`engagement_scope_ref` → `scope_ref` and parallels). Templates' "Engagement charter" → "Scoping charter". License switched Apache 2.0 → MIT for community fork-and-contribute fit. Soft credit line added to README.

### Phase 5 audit + fix-applier (commit deae432)

Six-dimension consolidated cross-skill audit at `internal/research/cross-skill-audit-2026-05-08.md`. Findings:
- 5A sector overlay coverage: zero gaps, zero drift, zero differentiation issues across 53 capability-plugin skills.
- 5B cross-cutting overlay coverage: zero strict gaps, eight plausible-coverage flags routed to B7.
- 5C skill-chain integrity: two real schema field-name drifts in the controls test pipeline.
- 5D schema / template / SKILL.md alignment: two misalignments.
- 5E cross-references: four broken pointers.
- 5F voice spot-check: seven skills sampled, all read strong; prose em-dashes flagged.

Fix-applier landed:
- Schema field renames: `analysis_id` → `exception_register_id`; `request_list_id` → `evidence_request_list_id`. Cross-skill foreign-key contracts declared on the renamed fields.
- Four broken pointers repointed.
- ai-act-triage cross-cutting overlay refs corrected.
- Four prose em-dashes converted.

### dora-register-builder light relabel (commit d11e3b5)

Repositioned as EU-DORA-context build pack and data-quality aid; not for direct submission to a national competent authority; not the official Register of Information template under Commission Implementing Reg (EU) 2024/2956. Preparation-grade only. Full rebuild deferred to v1.1 (see ROADMAP).

### Cross-cutting overlay obvious wins, B7 (commit d11e3b5)

Five new cross-cutting overlay files added on the four skills where the case was clear:
- `evidence-binder/references/cross-cutting/cyber.md`
- `aml-model-monitoring/references/cross-cutting/privacy.md`
- `prompt-injection-risk/references/cross-cutting/privacy.md` plus `conduct.md`
- `adverse-action-review/references/cross-cutting/conduct.md`

Five skipped with rationale (see "Editorial decisions on declined cases" below).

### CFPB / BNPL / FDIC currency sweep (commits d11e3b5, 12e8020)

- Phase 2 (B4) covered consumer-compliance-fair-lending. Phase 5.5 (B8) covered five additional plugins. Phase 5.6 finishers (B8a, B8b) picked up the residuals across the remaining six plugins.
- B8a: BNPL nullification across 12 files; CFPB Circular 2022-03 / 2023-03 withdrawal tagging across 8 files. Body softenings throughout: "per CFPB Circular X" replaced with Reg B § 1002.9 plus Comment 9(b)(2)-3 framing.
- B8b: financial-crime-governance, risk-reporting, banking-risk-compliance, payments-fintech-compliance, capital-markets-asset-management-compliance, insurance-risk-compliance updated. FinCEN Order FIN-2026-R001 (CDD exceptive relief, February 13, 2026); FinCEN BOI / CTA March 26, 2025 IFR (foreign-only reporting); investment-adviser AML rule compliance delay to January 1, 2028 (FinCEN final rule January 2, 2026); SAR FAQs October 9, 2025 inline tag; § 1033 stay (Forcht Bank, October 29, 2025) plus ANPR (August 22, 2025); § 1071 May 2026 revised final rule; NIST SP 800-61 Rev 3 (April 3, 2025); Names Rule corrected dates; FDIC Part 328 December 2023 final rule plus 2024-2025 extensions; SR 11-7 demoted to historical with joint guidance promoted to operative.

### TROUBLESHOOTING and examples relevance audit, B9 (commit d11e3b5)

Verdict: keep all 64 TROUBLESHOOTING.md and 129 example files. No filler found. Voice cleanup applied: em-dashes 1067 → 953 (114 prose em-dashes converted; list-row separators retained per pragmatic policy). H1 heading em-dashes normalised. Seven files synced with CFPB Circular withdrawal currency.

### Sector-flagship skill builds, B10a-c (commit pending)

Three skills had no TROUBLESHOOTING and no examples (build queue closed early). Built each:
- `bank-fintech-partnership-review`: TROUBLESHOOTING (9 failure modes) plus a community-bank-BaaS-with-mid-sized-fintech example.
- `adviser-exam-readiness`: TROUBLESHOOTING (7 failure modes) plus a mid-sized IA pre-exam command-center example.
- `fintech-partner-controls`: TROUBLESHOOTING (8 failure modes) plus a payment-app-mid-sized-fintech sponsor-bank-side review example.

### Small-items bundle, B11 (commit pending)

- Pack-schema field canonicalisation: `decision_items` → `decisions_requested` in risk-committee-pack schema. Practitioner framing: what does the audience need to decide.
- Reg E § 1005.11 timing rewrite in deposit-operations-controls cross-cutting/conduct.md: 10 business days investigation, 45 / 90 calendar days extension, 3 business days post-investigation notification.
- banking-supervision-readiness TROUBLESHOOTING.md (7 failure modes including CSI access-population breach, MRA / MRIA conflation, CAMELS-component scope drift, Reg YY mis-attribution, Heightened Standards at non-OCC sponsor, LFI rating framework applied below threshold, closure-readiness without sustained evidence).
- fund-board-reporting second example: sub-adviser approval at a multi-manager fund under the trust's manager-of-managers exemptive relief.

### Modular install analysis (analysis only, decisions deferred)

Read-only conceptual analysis at `internal/research/modular-install-analysis-2026-05-09.md`. Mapped Claude Code v2.1.110+ `dependencies` mechanism, the actual coupling map (risk-compliance-core has 57 cross-references from other plugins), 8 practitioner personas with minimum-viable-install paths, four install-pattern options, broken-pointer audit of partial-install scenarios. Recommendation: Hybrid (Option D) in two stages.

Decision (2026-05-09): both stages deferred to v1.1. Persona-shell agent plugin expansion declined. Analysis preserved as v1.1 starting reference.

### Docs and READMEs (commits deae432, 12e8020, plus inline polish)

- Repo `README.md` rewritten for industry practitioners (not developers). Premise stated cleanly without overselling. Multi-system framing: built primarily for Claude (and Claude Code), but the skill files follow the open SKILL.md format. Audience line written as colleague metaphor.
- Eight previously-untouched plugin READMEs converged on common shape.
- STATUS, CHANGELOG, CONTRIBUTING, ROADMAP, SECURITY refreshed.
- Lingering "engagement" framing in READMEs converted to "scope" / "review" where it was consulting argot. Plugin counts dropped where they would drift. Totalising language hedged ("every skill" → "skills").

---

## Editorial decisions on declined cases

### Cross-cutting overlays B7 declined (5 skills)

The five skills where the overlay-add case wasn't clear, with rationale, in case the call should be revisited:

- `ai-act-triage` (cyber, privacy): SKILL.md body inlines the substance at Article level. A separate parallel domain overlay would duplicate body prose.
- `sar-decision-qa` (conduct, privacy): marginal beyond the existing cyber overlay; the skill stays cleanly inside financial-crime governance.
- `sanctions-screening-qa` (conduct, climate, privacy): SKILL.md explicitly scopes these out at v1.
- `complaint-theme-analysis` (privacy, cyber, climate): SKILL.md explicitly scopes privacy not primary, cyber routed elsewhere, climate not applicable; conduct already shipped.
- `negative-news-triage` (cyber, privacy): cyber overlap into typology references not a separate overlay; privacy marginal.

### Plugin-level review-gates.md filename (B3 evaluated)

Kept as-is. Rename cascade was 35+ references across capability plugins and schemas; namespace collision with `human-review-gates` SKILL is suffix-only and meaningful (SKILL = artifact, reference = posture file).

### Em-dash strict pass

User-decided pragmatic. Table separators stay; prose em-dashes converted. 953 em-dashes remain in SKILL.md, mostly list-row separators. No further action unless a strict pass is later wanted.

---

## Open items

### Live `claude plugin validate`

Not yet run from the build environment. Action: run against each plugin in the target Claude Code version. Documented in ROADMAP.

### Per-skill independent reviewer pass

Drafting edits against the spec sheets in `internal/specs/`. Documented in ROADMAP.

### Modular install Stage 1 + Stage 2 (v1.1)

Deferred to v1.1 per user decision 2026-05-09. Analysis preserved at `internal/research/modular-install-analysis-2026-05-09.md`. Documented in ROADMAP.

### dora-register-builder full rebuild (v1.1)

Light relabel landed. Schema rebuild against Commission Implementing Reg (EU) 2024/2956, R-tables / RT-tables / relational tables, internal-to-ITS service-type mapping, examples body relabelling — all deferred. Documented in ROADMAP.

### Schema dedup (v1.1)

Phase 3 schema relocation reconsidered: plugin self-containment matters more than dedup for distribution; Anthropic's first-party FS plugins follow self-containing pattern. Replacement v1.1 plan: drop schemas a plugin's skills don't actually use. Documented in ROADMAP.

### Schema additivity contract validation (test backlog)

Most output skills carry "additive changes only, never silent renames" prose for downstream consumers, but no validation enforces it. Add to `scripts/check.py` if a schema-evolution problem surfaces. Documented in ROADMAP test backlog.

---

## Source watch items (re-verify before each engagement)

These are anchors where the regulatory state is volatile or the cite couldn't be pinned from the build environment. Each is flagged in the relevant `references/source-anchors.md` with a `[verify]` marker.

- **CRA rule disposition**: 2023 rule rescinded by 2025 agency action; if a follow-on rulemaking emerges, source-anchor reference should be re-pointed.
- **§1033 docket**: stay-and-reconsideration posture is volatile; ANPR follow-on rule will trigger date-stamp refresh across open-banking-data-controls, payment-operations-incident-review, fintech-partner-controls, payments-risk-assessment.
- **Names Rule and Reg S-P (capital markets)**: SEC has historically issued staff guidance and short extensions; current dates may shift.
- **Rule 605 amendments (capital markets)**: August 1, 2026 compliance date subject to potential SEC extension or staff guidance.
- **PCAOB AS 2201 follow-on amendments (attestation-pack)**: release numbers flagged for verification at write time.
- **NYDFS Circular Letter No. 7 (2024)** (insurance-outsourcing-review, life-health-pricing-governance): final issuance date and any amendment.
- **CO Regulation 10-1-1** (insurance): October 15 2025 amendment scope; confirm whether extended beyond life-insurance underwriting.
- **MGA Model #225 state-by-state adoption** (insurance-outsourcing-review): firm overlays should reflect operating-state adoption.
- **BCBS Newsletter No. 36 (January 2026 data-risk themes)** (risk-committee-pack, kri-commentary, bcbs239-gap-assessment): exact bis.org URL not pinned in the dossier; grab on engagement date.
- **EU AI Office Code of Practice** (llm-vendor-evidence-review): published with 2 August 2025 GPAI effective date; signatory list and any guideline updates evolve.
- **Archived examples** in `internal/v0.2-archive/examples/public-regulatory/ai-governance/`: if revived as live examples, refresh to drop the OCC-2026-as-AI-frame implication.

---

## Pointer index

- Citation verification dossier: `internal/research/citation-verification-2026-05-08.md`
- Cross-skill audit dossier: `internal/research/cross-skill-audit-2026-05-08.md`
- Modular install analysis: `internal/research/modular-install-analysis-2026-05-09.md`
- Codex per-skill scorecard: `internal/reviews/per-skill/scorecard.md`
- Codex per-skill memos: `internal/reviews/per-skill/<plugin-family>/`
- Codex spec sheets: `internal/specs/<plugin>/<skill>.md`
- Build contract and conventions: `internal/plans/`
- Build queue resume notes: `internal/RESUME-NOTES.md`
