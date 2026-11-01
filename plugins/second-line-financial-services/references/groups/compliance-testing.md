# Compliance Testing

Second-line and internal-audit control testing skills for financial-services firms and the advisory teams that support them. Covers the full testing arc for a single control or test cycle: scoping, sampling, evidence ask, exception classification, workpaper drafting, and QA review. Issue write-up and downstream issue tracking live in `risk-compliance-core` (the foundational primitives plugin).

## Skills

- `control-sampling` — Sampling memo (population, stratification, method, size rationale, selection, tolerable deviation rate, sample drawn).
- `evidence-request-builder` — Numbered, traceable evidence request list per control test or examination ask.
- `exception-analysis` — Classifies sampled deviations (control-failure / design-gap / evidence-gap / scope-disagreement / data-integrity / anomaly), severity-rates them, and produces a handoff package to `issue-writeup` for elevated items.
- `qa-workpaper` — QA review of a completed workpaper against firm methodology and IIA / AU-C standards. Decision: accept / return for rework / conditional accept.
- `test-plan-builder` — Pre-fieldwork test plan (objective, criteria, walkthrough, design and operating procedures, sampling reference, evidence reference, pass/fail criteria).
- `workpaper-drafter` — Standard testing workpaper from completed fieldwork (criteria, evidence inspected, procedures performed, sample-level results, exceptions, conclusion, issues elevated).

## Sequencing

The three workpaper-lifecycle skills are sequential, not redundant:

1. `test-plan-builder` — pre-fieldwork; signed off before evidence pulls.
2. `workpaper-drafter` — during/post-fieldwork; consumes the test plan and the exception register.
3. `qa-workpaper` — review of the completed workpaper before closure or examiner sharing.

The supporting skills compose into the test plan and workpaper:

- `control-sampling` produces the sampling memo referenced by the test plan and the workpaper.
- `evidence-request-builder` produces the evidence request list referenced by the test plan and the workpaper.
- `exception-analysis` classifies deviations identified in the workpaper before they become issues.

## Components

- `skills/` — invocable Claude Code skills. New plugins use skills, not legacy `commands/`.
- `references/` — public-source map, policy-control library, decision checkpoints, and output templates copied into this plugin so it is self-contained after installation.
- `schemas/` — JSON schemas for test plans, controls, obligations, issues, and adjacent artifacts. Several schemas are borrowed from `risk-compliance-core`; schema dedup is tracked in [ROADMAP.md](https://github.com/anotb/second-line-financial-services/blob/main/ROADMAP.md).

## Source posture

Skills are anchored to public, named regulatory and standards sources. Primary anchors include:

- IIA International Professional Practices Framework (Performance Standards 2200, 2210, 2220, 2240, 2310, 2320, 2330, 2340; Standard 1300 QAIP).
- AICPA AU-C 230 (Audit Documentation), 300 (Planning), 330 (Audit Procedures in Response to Assessed Risks), 500 (Audit Evidence), 530 (Audit Sampling). Borrowed in second-line testing as methodology anchors, not direct legal requirements.
- COSO 2013 Internal Control — Integrated Framework, Principles 16 and 17.
- FFIEC IT Examination Handbook, Audit booklet (April 2012).
- SR 08-8 (Federal Reserve, Compliance Risk Management Programs, October 2008).
- OCC PPM 5310-3 (compliance management systems for OCC-supervised banks). [verify exact reference and current effective date]
- CFPB Compliance Management System Review Procedures (current Supervision and Examination Manual edition).

Sector overlays (banking, insurance, capital markets, payments and fintech) and cross-cutting overlays (cyber, privacy, conduct on UDAAP-related testing) live as reference documents inside the skills they apply to. Climate is out of scope for testing-cycle work product.

## Operating posture

This plugin drafts second-line work product for qualified review. It does not approve, file, rate, onboard, decline, notify, or close items. Every artifact carries a confidence label and an explicit reviewer sign-off block. Public examples in this repository are derived from public regulatory and standards material; real implementation requires firm policy overlays, jurisdiction-specific legal review, and system-of-record evidence.
