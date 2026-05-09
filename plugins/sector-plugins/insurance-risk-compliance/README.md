# Insurance Risk Compliance

US-deep insurance-sector overlay plugin for second-line practitioners at insurers, reinsurers, MGA / MGU / TPA arrangements, and advisory teams running second-line work for them. Companion to the capability plugins in this repo; not a standalone toolkit.

## Posture

This is a **strict sector-overlay plugin**. It ships only sector-unique skills. Workflows that already exist as capability skills (AI Act triage, agentic-AI controls, AI risk tiering, LLM vendor evidence review, vendor diligence, risk-committee pack, fair-lending test plan) are not duplicated here. Insurance flavor for those workflows lives as `references/sector-overlays/insurance.md` inside the relevant capability skill.

## Skills

Two skills, both genuinely insurance-only (NAIC outsourcing model law, NAIC unfair-discrimination, ACA pricing, life-illustration, life and health AU and ECDIS rules):

- `insurance-outsourcing-review` — second-line review of an MGA, MGU, TPA, claims-administrator, or other delegated-authority arrangement against NAIC outsourcing model law (Insurance Holding Company Model #440 / #450 family [verify]), Insurance Data Security Model Law (Model #668) §4.F, NAIC Unfair Claims Settlement Practices Act (Model #900) plus the relevant state unfair-claims-settlement-practices acts where claims handling is delegated, and Producer Licensing Model Act expectations. Output is a state-DOI-grade oversight memo with disposition.
- `life-health-pricing-governance` — second-line governance review of life or health pricing, rate-filing, accelerated-underwriting, or ML-rating-factor changes against NAIC Model #880 unfair-discrimination, NAIC Bulletin on the Use of AI Systems by Insurers (December 2023), state DOI AI bulletins (Colorado SB 21-169 implementing regulation, NY DFS Insurance Circular Letter on AI and ECDIS in life insurance, January 2024, California DOI bulletin), ACA pricing rules where in scope, and Model #582 illustrations where in scope.

Insurance AI Act triage and claims-AI control substance now live as the insurance overlay inside `ai-governance-model-risk/ai-act-triage` and `ai-governance-model-risk/agentic-ai-controls` rather than as standalone insurance skills here.

## Capability-skill insurance overlays (cross-link)

The plugin contributes overlay reference content into seven capability skills:

- `ai-governance-model-risk/ai-act-triage` — absorbs the deprecated `insurance-ai-act-triage`.
- `ai-governance-model-risk/agentic-ai-controls` — absorbs the deprecated `claims-ai-controls`.
- `ai-governance-model-risk/ai-risk-tiering` — insurance tier criteria (AU, claims-AI, marketing-AI).
- `ai-governance-model-risk/llm-vendor-evidence-review` — insurance vendor-AI evidence demands.
- `third-party-operational-resilience/vendor-diligence` — NAIC outsourcing model + Insurance Data Security Model Law §4.F.
- `risk-reporting/risk-committee-pack` — ORSA Summary Report mapping (Model #505) and CGAD support (Model #305 [verify]).
- `consumer-compliance-fair-lending/fair-lending-test-plan` — Model #880 unfair-discrimination overlay (different statutory frame from ECOA / Reg B).

Outlines for these overlays live in `internal/specs/insurance-risk-compliance/overlay-snippets.md`. The two AI overlays carry the substance previously carved out as standalone `insurance-ai-act-triage` and `claims-ai-controls` skills, now absorbed into the cross-industry skills via the insurance overlay.

## Components

- `skills/`: Claude Code skills. Two skills: `insurance-outsourcing-review` and `life-health-pricing-governance`. The earlier `insurance-ai-act-triage` and `claims-ai-controls` content was absorbed into the cross-industry AI skills' insurance overlays.
- `references/`: plugin-level insurance source map and shared library, scoped to insurance-specific cross-skill anchors. Per-skill source anchors live under each skill's own `references/source-anchors.md`.
- `schemas/`: JSON schemas for the artifacts produced by the two skills.

## Source posture

US-deep first. EU Solvency II is tracked in [ROADMAP.md](../../../ROADMAP.md) for inclusion as a see-also reference inside `risk-committee-pack/references/sector-overlays/insurance.md`. Public sources only: NAIC Model Laws and Regulations, NAIC Bulletins, state DOI bulletins, federal statutes (HIPAA, ACA), and SEC where applicable for publicly-listed carriers.

## Operating posture

The plugin drafts second-line work product for qualified review. It does not approve, file, rate, onboard, decline, notify, or close items. Every external source is treated as an anchor, not a substitute for legal interpretation. Every citation is dated.
