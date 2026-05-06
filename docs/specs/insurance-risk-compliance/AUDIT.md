# Plugin audit: insurance-risk-compliance (v1)

Date: 2026-05-06
Phase: 1 (scoping pass; no SKILL.md content here).
Status: Spec sheets and overlay snippets drafted. Folder deletions deferred to phase 3.

## v1 skill list

Two retained skills, both genuinely insurance-only and both in line with the strict sector-overlay rule.

| Skill | Status | Why retained |
|---|---|---|
| `insurance-outsourcing-review` | Retained | NAIC outsourcing model-law family + Insurance Data Security Model Law §4.F. Different statutory frame, audience (state DOI), and artifact (oversight memo for market-conduct-exam-grade review of MGA / MGU / TPA / claims-administrator arrangements) from the bank-flavored capability `vendor-diligence`. |
| `life-health-pricing-governance` | Retained | NAIC unfair-discrimination tradition under Model #880, life and health rate-filing law, state DOI AI bulletins for AU and ML rating, ACA pricing rules, Model #582 illustrations. Different statutory frame from the ECOA / Reg B fair-lending capability skill. |

Two skills dropped from v0.2.

| Skill | Status | Reason |
|---|---|---|
| `insurance-ai-act-triage` | Dropped | Same shape as `ai-governance-model-risk/ai-act-triage` with insurance examples. Sector flavor moves to `ai-governance-model-risk/skills/ai-act-triage/references/sector-overlays/insurance.md`. |
| `claims-ai-controls` | Dropped | Same shape as `ai-governance-model-risk/agentic-ai-controls` with insurance scenarios. Sector flavor moves to `ai-governance-model-risk/skills/agentic-ai-controls/references/sector-overlays/insurance.md`. |

The two dropped skill folders (`plugins/sector-plugins/insurance-risk-compliance/skills/insurance-ai-act-triage/` and `.../claims-ai-controls/`) are scheduled for deletion in phase 3 alongside the re-bundle. They remain in place in phase 1 so phase 2 can lift any salvageable references / templates / examples into the corresponding capability-skill insurance overlays before deletion.

## Strict overlay-rule check

- `insurance-outsourcing-review`: insurance-only. The closest capability analog is `third-party-operational-resilience/vendor-diligence`, but that skill does not produce a state-DOI-grade outsourcing-oversight memo and does not invoke NAIC Model #440 / #450 / #668 / #880 / Producer Licensing. Pass.
- `life-health-pricing-governance`: insurance-only. The closest capability analog is `consumer-compliance-fair-lending/fair-lending-test-plan`, but that skill is built on ECOA / Reg B, not on NAIC Model #880 unfair-discrimination, ACA pricing rules, Model #582 illustrations, or state DOI rate-filing expectations. Pass.

Both skills clear the strict overlay rule: their statutory frame, audience, and artifact are insurance-specific and do not duplicate any capability skill.

## Plugin-level shared references plan

Today, `plugins/sector-plugins/insurance-risk-compliance/references/` holds:

- `output-templates.md`
- `policy-control-library.md`
- `public-regulatory-scenarios.md`
- `review-gates.md`
- `source-map.md`

In v1 with two retained skills, those plugin-level shared references should be tightened so they do not duplicate per-skill references.

Recommended posture for phase 2:

- `source-map.md`: keep at plugin level. Curate to the insurance-specific anchor list (NAIC Model #440 / #450 / #668 / #880 / #505 / #582 / #275 / #670 / Producer Licensing; NAIC Bulletin Dec 2023; NAIC Principles on AI 2020; CO regulation, NY DFS Circular Letter, CA bulletin; HIPAA Privacy and Security Rule; ACA pricing rules; SR 11-7 / OCC 2026-13 [verify] for analogous model-risk language). Date every citation.
- `policy-control-library.md`: keep at plugin level only if it carries genuinely cross-skill insurance controls (e.g., AIS Program elements, §4.F third-party-service-provider control families). Otherwise, fold into the per-skill references in phase 2.
- `output-templates.md`: deprecate at plugin level. Each retained skill carries its own template under `templates/default-output.md` per the v1 anatomy. Keep this file only if it carries insurance-specific cross-cutting boilerplate (disclaimer language, citation block format).
- `review-gates.md`: deprecate at plugin level. Gates are skill-specific in v1; embed in each skill's `SKILL.md`.
- `public-regulatory-scenarios.md`: keep at plugin level as the canonical scenario library so phase 2 example writing reuses scenarios consistently across the two retained skills and the seven overlay snippets.

Phase 2 brief: do not copy plugin-level references into per-skill folders. Per-skill folders carry their own `references/source-anchors.md` with skill-specific citations. Plugin-level references are the cross-skill canonical list.

## Capability-skill insurance overlays (drafted as outlines in `overlay-snippets.md`)

Seven capability skills get insurance overlays in v1:

1. `ai-governance-model-risk/ai-act-triage` — absorbs deprecated `insurance-ai-act-triage`. Drafted deep.
2. `ai-governance-model-risk/agentic-ai-controls` — absorbs deprecated `claims-ai-controls`. Drafted deep.
3. `ai-governance-model-risk/ai-risk-tiering` — insurance tier criteria.
4. `ai-governance-model-risk/llm-vendor-evidence-review` — insurance vendor-AI evidence demands.
5. `third-party-operational-resilience/vendor-diligence` — NAIC outsourcing + Model #668.
6. `risk-reporting/risk-committee-pack` — ORSA Summary Report mapping.
7. `consumer-compliance-fair-lending/fair-lending-test-plan` — Model #880 unfair-discrimination overlay (different statutory frame from ECOA / Reg B).

Phase 2 contract: each capability-skill spec sheet (written by the capability-plugin lead) must reference the corresponding outline in `overlay-snippets.md` so the phase-2 content writer receives the brief. The two AI overlays (items 1 and 2) are written deeper in the snippets file because they carry the substance of the deprecated skills.

## Structural concerns

- **Vendor-AI accountability triple-coverage.** NAIC Bulletin Dec 2023 vendor-AI accountability appears in `insurance-outsourcing-review`, in the `vendor-diligence` insurance overlay, and in the `llm-vendor-evidence-review` insurance overlay. This is correct (different artifacts, different audiences) but phase 2 needs to keep the language consistent across the three so the carrier can see the same bar in three places without contradiction.
- **State DOI variation under #668 and the AI Bulletin.** Adoption is state-by-state. The plugin-level `source-map.md` should point to the NAIC adoption tracker rather than freezing a state list.
- **Model-number `[verify]` markers.** Several model numbers are flagged [verify] in the spec sheets and overlay snippets where I am not 100 percent sure of the exact model number from the NAIC index (Model #440 vs #450 family; Model #275 suitability in annuity transactions; Model #305 corporate governance annual disclosure; Model #670 insurance information and privacy protection). Phase 2 must confirm against the live NAIC Model Laws & Regulations index before any [verify] marker survives into a SKILL.md.
- **EU Solvency II.** US-deep is the v1 default. EU Solvency II is captured as a see-also overlay reference in `risk-committee-pack/references/sector-overlays/insurance.md` in v1.1; not in scope for v1.
- **P&C-specific pricing.** Out of v1 scope. `life-health-pricing-governance` is explicit about its boundary (life, health, annuity, disability, LTC). A P&C-specific pricing-governance skill is a candidate for v1.1 if state DOI rating-bureau frames warrant it.

## Voice and source-confidence summary

- Voice: senior, terse, regulator-aware, practitioner vocabulary. Both spec sheets and the overlay-snippets file read like a Big Four insurance-regulatory practice or a state DOI examiner brief, not like product copy.
- Source-anchor confidence:
  - `insurance-outsourcing-review`: high on the NAIC Model #668, #880, ORSA, and Producer Licensing anchors. Medium on the exact Model numbers for the holding-company act and reg (#440 / #450), flagged [verify] in the spec sheet.
  - `life-health-pricing-governance`: high on Model #880, NAIC Bulletin Dec 2023, NY DFS Circular Letter (Jan 2024), CO SB 21-169 implementing regulation, ACA rating rules, Model #582. Medium on suitability-in-annuity Model #275 and on whether SR 11-7 / OCC 2026-13 framing belongs in the artifact (it does, but the citation language must be careful — these are analogous, not directly applicable).
  - AI overlay snippets (items 1 and 2): high. The substance of the deprecated `insurance-ai-act-triage` and `claims-ai-controls` is recoverable from the same public-source list (NAIC Bulletin Dec 2023, CO regulation, NY DFS Circular Letter, CA bulletin, Model #880, Model #668 §4.F, HIPAA, EU AI Act Annex III). The overlays carry that substance with named citations and named output additions.

## Phase-3 to-do (for the re-bundle pass)

- Delete `plugins/sector-plugins/insurance-risk-compliance/skills/insurance-ai-act-triage/`.
- Delete `plugins/sector-plugins/insurance-risk-compliance/skills/claims-ai-controls/`.
- Confirm the seven capability-skill insurance overlays exist as `references/sector-overlays/insurance.md` and contain the substance from the corresponding outline in `overlay-snippets.md`.
- Confirm plugin-level shared references in `plugins/sector-plugins/insurance-risk-compliance/references/` are tightened per the recommendation above.
- Run `python3 scripts/sync-agent-skills.py` and `python3 scripts/check.py` after the deletes.
