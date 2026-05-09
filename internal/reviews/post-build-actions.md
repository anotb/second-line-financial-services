# Post-build action register

Date: 2026-05-09
Status: rolled up from Phase 1 sweeps (A1-A6), Phase 2 editorial review (B1-B6), Phase 5 audit, the citation verification dossier, the engagement-scoping → scoping rename, the MIT license switch, the dora-register-builder relabel, the README and docs polish, and the follow-up agents (B7 overlay obvious wins, B8 / B8a / B8b currency sweep, B9 TROUBLESHOOTING and examples relevance audit). Source for each line is captured below so a reader can trace any decision to the work that produced it.

The point of this file: nothing the analysis surfaced should drop on the floor. Items are tagged **done**, **open**, **watch**, or **deferred** with a clear next move.

---

## Done in this build cycle

### Voice and structure (Phase 1, six sweeps A1-A6, commit 22dc202)

- Removed `Anchored to:` paragraph from SKILL.md description blocks across 68 source skills. Citations live in `references/source-anchors.md`.
- Replaced "What's load-bearing and what flexes" with `## Quality bar` and `## Adaptation` blocks. Editorial folding pass deferred to Phase 2.
- Softened "review gates" terminology outside `human-review-gates` (which keeps the term as the artifact's subject) to decision forum / owner / conditions / attestation block / sign-off question / decision checkpoint.
- Format-flexible `## Output` rewrites for the high-impact artifact skills: vendor-diligence, criticality-assessment, contract-gap-review, exit-plan, resilience-testing-pack, control-matrix, evidence-binder, issue-writeup, policy-gap-review, control-sampling, exception-analysis, qa-workpaper, workpaper-drafter.
- Synced to agent-plugin bundles via `scripts/sync-agent-skills.py`.

### Voice editorial layer (Phase 2, six reviews B1-B6, commit 5fd4cf6)

Per-plugin editorial pass over Phase 1's mechanical cleanup. Voice principle: in SKILL.md body, regulators are grounding not focus. Heavy citation work (joint-guidance issuance metadata, footnote scope quotes, asset thresholds, supersession language, section / subpart numbers) consolidated into `references/source-anchors.md` and overlay files.

- ai-governance-model-risk: April 2026 joint guidance (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026) verbatim language consolidated in source-anchors. SR 11-7 and SR 21-8 marked superseded. OWASP LLM Top 10 refreshed to 2025 numbering (LLM01-LLM08). EU AI Office Code of Practice refreshed from "in development" to published with 2 August 2025 GPAI effective date. agentic-ai-controls regulator-perspective paragraph reordered: cyber regimes binding first, OWASP / MITRE ATLAS / NCSC / CISA primary, joint-guidance demoted to by-analogy. ai-act-triage Article numbers retained (legitimate legal-triage exception).
- third-party-operational-resilience: DORA Article 28(1)-(8) and Article 30(2)/(3) canonical structure landed in source-anchors. OCC 2013-29 demoted to historical. Commission Delegated Regs (EU) 2025/532 (sub-contracting RTS) and 2025/1190 (TLPT RTS) added. PRA SS1/21, SS2/21, PS7/26 noted. FinCEN MSB §1010.380 corrected to §1022.380 across vendor-diligence, contract-gap-review, concentration-risk-review, criticality-assessment.
- risk-compliance-core: long lists of CFR cites, SR letters, NYDFS sections, Reg numbers, and NAIC model numbers pulled out of bodies and into source-anchors. obligation-mapping CFPB 1071 thresholds updated to May 2026 final rule (1,000 covered transactions, June 30 2026 effective, January 1 2028 compliance). human-review-gates got proportionality paragraph (low-risk artifacts don't inherit committee machinery). issue-writeup MRA / MRIA labelled banking-specific. policy-gap-review's `mrm-policy-vs-occ-2026-13` example reframed under traditional models with GenAI / agentic AI routed to a separate AI Governance Framework workstream.
- compliance-testing + consumer-compliance-fair-lending: section1071-readiness rebuilt around May 2026 revised final rule. CFPB current-status preamble plus withdrawn-circular tagging plus statute / Reg B / HUD framing across udaap-risk-review, fair-lending-test-plan, adverse-action-review, complaint-theme-analysis, marketing-claim-review. Pub. L. 119-11 BNPL Interpretive Rule nullification noted. FDIC Part 328 dates updated. control-sampling gets OCC Sampling Methodologies primary; provisional / pro-forma / in-flight branches added across the test-plan-builder pipeline.
- financial-crime + regulatory-change-management: sar-decision-qa Red-tier reframe per October 9 2025 SAR FAQ posture (90-day cadence is firm policy not BSA rule; separate post-SAR continuing reviews not rule-required; no-SAR documentation not BSA-required). aml-model-monitoring Red-tier model-scoping read added (joint-guidance models vs deterministic rules vs GenAI / agentic excluded). policy-diff: wrong OCC Bulletin 2021-36 anchor removed (it is information-security / authentication, not policy-governance). regulatory-impact-assessment: 12 CFR Part 30 Appendix B vs Appendix D distinction corrected. exam-brief template rebuilt from 5-section boilerplate to 14-section engagement-side scaffolding.
- risk-reporting + 4 sector plugins: bcbs239-gap-assessment removed SR 21-19 (rescinded); added SR 19-3 as LFI-rating operationalisation. attestation-pack GLBA Safeguards §314.4(g) → §314.4(i) post-2021 renumbering; added §314.4(j) breach-notification. cyber-disclosure-readiness NIST SP 800-61 Rev 2 → Rev 3 (April 2025, CSF 2.0). banking-supervision-readiness MRA / MRIA → SR 13-13; LFI (SR 19-3) vs RFI / C(D) branch. credit-risk-governance FRB SR 20-13 plus OCC 2020-44 plus FDIC FIL-50-2020. Reg E timing reconciled (10 BD investigation, 45 / 90 calendar days extension, 3 BD post-investigation notification). Insurance MGA Model #225 added; #880 kept in life-health-pricing-governance for unfair-discrimination / pricing; #900 holds for claims-handling. Payments §1033 stayed / reconsideration plus payment-app LPR nullification (Pub. L. 119-11) plus FDX recognition (CFPB January 8 2025) consistent across all four payments-fintech skills. SEC Rule 605 compliance August 1 2026; Names Rule December 2025 / June 2026 extensions; Reg S-P concrete dates.

### Citation verification dossier

Read-only verification of 28 currency-of-citation claims against official sources (OCC, FRB, FDIC, FinCEN, CFPB, SEC, NAIC, EUR-Lex, BIS, NIST, IIA, AICPA, OMB). 25 confirmed, 3 partial, 0 wrong. Lives at `internal/research/citation-verification-2026-05-08.md`. Notable findings:

- OCC Bulletin 2026-13 footnote 3 explicitly excludes generative AI and agentic AI from scope. The bulletin contains zero NIST references; AI-scope routes to NIST AI RMF, NIST AI 600-1, ISO/IEC 42001, EU AI Act, OWASP LLM Top 10, MITRE ATLAS, NCSC / CISA, NYDFS October 2024.
- FRB SR 26-2 and FDIC FIL-15-2026 are not parallels — they are the same joint document issued through each agency's machinery. Cite all three together as one document with three bibliographic anchors. Supersedes SR 11-7 (2011) and SR 21-8 (the AML interagency statement).
- FinCEN MSB registration is at 31 CFR §1022.380, not §1010.380 (which is the BOI / CTA reporting rule).
- NAIC Model #880 stays correct as the unfair-discrimination / pricing anchor; the Phase 1 swap to Model #900 applies only where #880 was mis-used as a claims-handling anchor. life-health-pricing-governance kept #880; insurance-outsourcing-review swapped to #900.
- Reg E timing pattern: 10 business days for investigation, 45 calendar days extension with provisional credit (90 calendar days for new accounts, POS, foreign-initiated transfers), 3 business days post-investigation to notify consumer.

### engagement-scoping → scoping rename (commit aa4500c)

Renamed the bootstrap skill from `engagement-scoping` to `scoping` for audience clarity ("engagement" reads as consulting argot to a 1.5-line / 2-line practitioner). Rename touched ~1,100 cross-references across capability and sector plugins, templates, examples, source-anchors, sector overlays, cross-cutting overlays, schemas, internal specs, and STATUS. Schema field renames: `engagement_scope_ref` → `scope_ref` and parallels. Templates' "Engagement charter" heading became "Scoping charter". Pre-existing narrative uses of "engagement" stay where they read naturally. IIA Standard 2220 literal name and external-convention citations preserved.

### License switch (commit aa4500c)

Apache 2.0 → MIT. The repo is intended for community fork and contribution; MIT's lighter, single-paragraph permission grant fits that posture better than Apache 2.0's heavier patent-grant machinery. Soft credit line added to README ("If these plugins prove useful in your work, a mention or link back is appreciated but not required"); the legal floor is MIT's mandatory copyright-notice clause.

### Phase 5 audit (commit deae432)

Read-only consolidated cross-skill audit at `internal/research/cross-skill-audit-2026-05-08.md`. Six dimensions:

- 5A sector overlay coverage: zero gaps, zero drift, zero differentiation issues across 53 capability-plugin skills.
- 5B cross-cutting overlay coverage: zero strict gaps, eight plausible-coverage flags routed to B7.
- 5C skill-chain integrity: two real schema field-name drifts in the controls test pipeline. Fixed.
- 5D schema / template / SKILL.md alignment: two misalignments. Fixed.
- 5E cross-references: four broken pointers. Fixed.
- 5F voice spot-check: seven skills sampled, all read strong; ~485 em-dashes total in SKILL.md (mostly markdown table separators); a handful of prose em-dashes flagged. Fixed.

### Phase 5 fix-applier (commit deae432)

- Schema field renames: `analysis_id` → `exception_register_id`, `request_list_id` → `evidence_request_list_id`. Canonical names declared as cross-skill foreign-key contracts.
- Four broken pointers repointed: `control-test-workpaper` → `workpaper-drafter` (two SKILL.md), `issue-management` → `issue-writeup`, `important-business-service-mapping` → `criticality-assessment` plus `resilience-testing-pack`.
- ai-act-triage cross-cutting overlay refs corrected: removed pointers to non-existent files. Cyber and privacy substance lives at Article level inside the body; no parallel domain overlays needed.
- Four prose em-dashes replaced with ellipses, semicolons, or colons.

### dora-register-builder light relabel (commit d11e3b5)

Repositioned as EU-DORA-context build pack and data-quality aid. Two explicit caveats added in `Not the right tool when`: not for direct submission to a national competent authority; not the official Register of Information template under Commission Implementing Reg (EU) 2024/2956. Preparation-grade only. Examples bodies and full schema rebuild deferred to a future Phase.

### Cross-cutting overlay obvious wins, B7 (commit d11e3b5)

Five new cross-cutting overlay files added on the four skills where the case was clear:

- `evidence-binder/references/cross-cutting/cyber.md` — binders carry NYDFS Part 500 attestations, IR workpapers, vulnerability extracts, SOC 2 evidence, vendor cyber assessments, §500.17 / 36-hour banking notice / 8-K Item 1.05 filings.
- `aml-model-monitoring/references/cross-cutting/privacy.md` — transaction-monitoring data is NPI under GLBA; segmentation features intersect state privacy laws; vendor stack sits inside §314.4(f); SAR-related references implicate the §5318(g) tipping-off frame.
- `prompt-injection-risk/references/cross-cutting/privacy.md` plus `conduct.md` — privacy load-bearing for training-data extraction, retrieval exfiltration, tool-driven egress; conduct load-bearing on customer-facing surfaces (UDAAP, Marketing Rule, Reg BI, NAIC AI Bulletin).
- `adverse-action-review/references/cross-cutting/conduct.md` — sharpens comprehensibility read on cited reasons, names sample-form-substitution and reason-suppression population patterns, adds disclosure-consistency read, flags AI / complex-model defects as conduct-event candidates.

Five skipped with rationale (filed under "open / watch" below if the call should be revisited): ai-act-triage, sar-decision-qa, sanctions-screening-qa, complaint-theme-analysis, negative-news-triage.

### CFPB / BNPL / FDIC currency sweep (commits d11e3b5 and follow-ups)

Phase 2 (B4) covered consumer-compliance-fair-lending. Phase 5.5 (B8) covered five additional plugins (ai-governance-model-risk, compliance-testing, regulatory-change-management, risk-compliance-core, third-party-operational-resilience) before stalling. Phase 5.6 finishers picked up the residuals:

- B8a: BNPL nullification across 12 files; CFPB Circular 2022-03 / 2023-03 withdrawal tagging across 8 files. Body softenings throughout: "per CFPB Circular 2022-03" replaced with Reg B §1002.9 plus Comment 9(b)(2)-3 framing, with the withdrawn-circular cite parenthetical and historical.
- B8b (in flight at the time of this register): currency sweep across the six plugins B8 didn't reach (financial-crime-governance, risk-reporting, banking-risk-compliance, payments-fintech-compliance, capital-markets-asset-management-compliance, insurance-risk-compliance). Result will be appended here.

### TROUBLESHOOTING and examples relevance audit, B9 (commit d11e3b5)

Verdict: keep all 64 TROUBLESHOOTING.md and 129 example files. No filler found across the corpus. Voice cleanup applied to retained files: em-dashes 1067 → 953 (114 prose em-dashes converted; list-row separators retained per pragmatic em-dash policy). H1 heading em-dashes normalised. Seven files synced with CFPB Circular withdrawal currency where they referenced the withdrawn circulars as binding.

### Docs and READMEs (commit deae432, refined in d11e3b5 and inline edits)

- Repo `README.md` rewritten for industry practitioners (not developers). Premise stated cleanly without overselling: "extends Anthropic's published financial-services plugin family. Where Anthropic's plugins cover the cross-industry first-line baseline, these plugins go deeper into US second-line and 1.5-line work and US supervisory expectations." Multi-system framing added: built primarily for Claude (and Claude Code), but the skill files follow the open SKILL.md format and load into other agentic systems. Audience line written as colleague metaphor.
- Eight previously-untouched plugin READMEs converged on common shape (premise, audience, skills, chain, source posture, overlays, components, install, operating posture).
- STATUS, CHANGELOG, CONTRIBUTING, ROADMAP, SECURITY refreshed against current state.
- Lingering "engagement" framing in READMEs converted to "scope" / "review" where the term was consulting argot. Plugin counts dropped where they would drift.

---

## Open / queued items

### Build candidates (missing TROUBLESHOOTING and examples) — B9 flagged

Three sector-flagship skills have neither a TROUBLESHOOTING.md nor any example file. The pattern across the corpus is one TROUBLESHOOTING plus two examples per skill, so these are gaps the build queue closed early on, not deliberate omissions:

- `banking-risk-compliance/skills/bank-fintech-partnership-review/`
- `capital-markets-asset-management-compliance/skills/adviser-exam-readiness/`
- `payments-fintech-compliance/skills/fintech-partner-controls/`

Action: build TROUBLESHOOTING.md and at least one realistic example per skill in the next cycle.

### Build calibration nudges — B9 flagged

- `capital-markets-asset-management-compliance/skills/fund-board-reporting/` ships one example. Add a second engagement-shape example (sub-adviser approval vs multi-manager) when next pass touches the skill.
- `banking-risk-compliance/skills/banking-supervision-readiness/` has no TROUBLESHOOTING. The skill is examination-orchestration heavy; plausibly fine, but a TROUBLESHOOTING listing CSI access-population breaches, MRA / MRIA conflation, CAMELS-component scope drift would help.

### Cross-cutting overlay editorial decisions deferred — B7 flagged

The five skills B7 declined to add overlays on, with rationale, in case the orchestrator wants to revisit:

- `ai-act-triage` (cyber, privacy): SKILL.md body inlines the substance at Article level (Article 15 / NIS2 / DORA seam; Article 27 FRIA / GDPR Article 35 reconciliation). A separate parallel domain overlay would duplicate body prose.
- `sar-decision-qa` (conduct, privacy): marginal beyond existing cyber overlay; the skill stays cleanly inside financial-crime governance.
- `sanctions-screening-qa` (conduct, climate, privacy): SKILL.md explicitly scopes these out at v1.
- `complaint-theme-analysis` (privacy, cyber, climate): SKILL.md explicitly scopes privacy not primary, cyber routed elsewhere, climate not applicable; conduct already shipped.
- `negative-news-triage` (cyber, privacy): cyber overlap into typology references not a separate overlay; privacy marginal.

If a later pass changes the call, the overlay shape is documented in the four files B7 did create.

### Schema and contract integrity — B1, Phase 5 flagged

- Pack-schema field naming parallel: `decision_items` (in one pack schema) vs `decisions_requested` (in another). Both refer to the same concept (decisions surfaced for the audience). Editorial decision needed: keep divergent for clarity, or align to a canonical name.
- Schema additivity contract: most output skills carry "additive changes only, never silent renames" prose for downstream consumers, but no validation enforces it. If a schema-evolution problem surfaces, this is where it would live. Add to `scripts/check.py` if appropriate.

### Plugin-level filename — B3 evaluated and decided

- `references/review-gates.md` plugin-level filename: kept as-is. Rename cascade was 35+ references across capability plugins and schemas; namespace collision with `human-review-gates` SKILL is suffix-only and meaningful (SKILL = artifact, reference = posture file). Decision sticks unless revisited.

### dora-register-builder full rebuild — Phase 4 deferred

Light relabel landed (commit d11e3b5). Still deferred:

- Schema rebuild against Commission Implementing Reg (EU) 2024/2956 — official ITS table / column codes, Annex labels, and ICT-service-type taxonomy verbatim.
- R-tables, RT-tables, and relational tables that sit alongside B-tables in the official template.
- Internal-to-ITS service-type mapping table (currently held in the firm-overlay slot as a pointer; the actual code list the official Annex prescribes is not embedded).
- Examples body relabelling from "first-cycle build" framing to "preparation pass" framing.

### Phase 3 schema relocation

Schemas borrowed across plugins for v1 should move to their owning plugins. Per-skill schemas land under `<skill>/schemas/`. Already in roadmap. Action: a single relocation pass.

### Live `claude plugin validate`

Has not been run from the build environment yet. Action: run against each plugin in the target Claude Code version.

### Em-dash strict pass — deferred

User-decided as pragmatic (table separators stay, prose em-dashes converted). 953 em-dashes remain in SKILL.md, mostly list-row separators (`**Label** — content`). If a strict pass is ever wanted, the work is mechanical; brief is "table separators may stay if they are markdown column dividers, otherwise convert."

### Archived examples — watch

`internal/v0.2-archive/examples/public-regulatory/ai-governance/` carries `agentic-ai-controls-review.md` and `eu-ai-act-creditworthiness-triage.md` referencing OCC 2026 in pre-correction framing. If those are revived as live examples, they need refresh to drop the OCC-2026-as-AI-frame implication. Otherwise leave in archive.

---

## Source watch items (re-verify before each engagement)

These are anchors where the regulatory state is volatile or where we could not pin a final cite from the build environment. Each is flagged in the relevant `references/source-anchors.md` with a `[verify]` marker, but a watch list helps.

- **CRA rule disposition**: 2023 rule rescinded by 2025 agency action; if a follow-on rulemaking emerges, source-anchor reference should be re-pointed.
- **§1033 docket**: stay-and-reconsideration posture is volatile; ANPR follow-on rule will trigger date-stamp refresh across open-banking-data-controls, payment-operations-incident-review, fintech-partner-controls, payments-risk-assessment.
- **Names Rule and Reg S-P (capital markets)**: SEC has historically issued staff guidance and short extensions; December 2025 / June 2026 dates may shift.
- **Rule 605 amendments (capital markets)**: August 1, 2026 compliance date subject to potential SEC extension or staff guidance.
- **PCAOB AS 2201 follow-on amendments (attestation-pack)**: release numbers flagged for verification at write time.
- **NYDFS Circular Letter No. 7 (2024)** (insurance-outsourcing-review, life-health-pricing-governance): final issuance date and any amendment.
- **CO Regulation 10-1-1** (insurance): October 15 2025 amendment scope; confirm whether extended beyond life-insurance underwriting.
- **MGA Model #225 state-by-state adoption** (insurance-outsourcing-review): state-level adoption pace; firm overlays should reflect operating-state adoption.
- **BCBS Newsletter No. 36 (January 2026 data-risk themes)** (risk-committee-pack, kri-commentary, bcbs239-gap-assessment): exact bis.org URL not pinned in the dossier; grab on engagement date.
- **EU AI Office Code of Practice** (llm-vendor-evidence-review): published with 2 August 2025 GPAI effective date; signatory list and any guideline updates evolve.

---

## Pointer index

- Citation verification dossier: `internal/research/citation-verification-2026-05-08.md`
- Cross-skill audit dossier: `internal/research/cross-skill-audit-2026-05-08.md`
- Codex per-skill scorecard: `internal/reviews/per-skill/scorecard.md`
- Codex per-skill memos: `internal/reviews/per-skill/<plugin-family>/`
- Codex spec sheets: `internal/specs/<plugin>/<skill>.md`
- Build contract and conventions: `internal/plans/`
- Build queue resume notes: `internal/RESUME-NOTES.md`
