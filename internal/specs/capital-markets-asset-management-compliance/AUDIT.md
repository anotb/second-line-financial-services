# Plugin audit memo: capital-markets-asset-management-compliance

Date: 2026-05-06
Status: phase 1 audit, finalized after the lead spec-sheet pass.
Scope: SEC-registered investment advisers, broker-dealers, dual registrants, registered funds, and their advisers.

## v1 skill list (confirmed, no changes)

- `adviser-exam-readiness`
- `best-execution-surveillance`
- `fund-board-reporting`
- `marketing-rule-evidence`

All four are genuinely sector-unique under the strict sector-overlay rule. Each maps to a workflow that does not exist in any capability plugin and that is shaped by the IA Act, the ICA, the Exchange Act, and FINRA rule set, not by the interagency banking guidance, NAIC framework, or CFPB framework that drives capability skills.

## Deletions, renames, additions vs v0.2

None. The v0.2 list was already correctly cut.

## Strict overlay rule check

Each of the four was tested against the question "is this just a capability skill with capital-markets examples." None are. Reasoning per skill:

- `adviser-exam-readiness` — distinct artifact from the generic `regulatory-change-management/exam-brief`. The generic skill is the regulator-agnostic engagement playbook (entry, points of contact, document-handling protocol, privilege posture). This skill is the SEC EXAMS / FINRA-specific readiness sprint with the IA Act / ICA / Exchange Act / FINRA Rule lattice, EXAMS document-request playbook, current-year EXAMS priorities, and Form ADV / CRS / BD cross-checks. The two chain. Documented in both spec sheets' "Not the right tool when".
- `best-execution-surveillance` — the periodic governance review under §206 IA fiduciary duty / FINRA 5310 / Rule 605/606. No capability skill covers periodic best-ex; vendor-diligence covers vendor selection, which is an upstream, distinct workflow. Documented in the "Not the right tool when".
- `fund-board-reporting` — 15(c) and 38a-1 fund-board posture, distinct from adviser ERM committee reporting in `risk-reporting/risk-committee-pack`. Different audience, different statutory hooks. Documented.
- `marketing-rule-evidence` — Rule 206(4)-1 evidence and substantiation lane. Doctrinally distinct from UDAAP marketing review under Dodd-Frank §1031 (the consumer-compliance-fair-lending lane). Antifraud / fiduciary disclosure under §206 vs. UDAAP fair-and-balanced under §1031. Different statutory framework, different burden of proof, different examiner. Documented.

## Boundary calls documented in spec sheets

- `adviser-exam-readiness` vs `regulatory-change-management/exam-brief` — chains, not duplicates.
- `best-execution-surveillance` vs `third-party-operational-resilience/vendor-diligence` — periodic governance review vs vendor selection.
- `fund-board-reporting` vs `risk-reporting/risk-committee-pack` — fund (per-fund §15(c) and §38a-1) vs adviser ERM (firm-wide CRO function).
- `marketing-rule-evidence` vs `consumer-compliance-fair-lending/marketing-claim-review` — IA Act §206 antifraud vs Dodd-Frank §1031 UDAAP.

## Capital-markets sector overlays for capability skills

Drafted in `overlay-snippets.md`. Phase 2 builds these as `references/sector-overlays/capital-markets.md` files inside the named capability skills. Coverage:

- `third-party-operational-resilience/vendor-diligence` — sub-adviser oversight, fund service-provider 38a-1 adequacy, outsourced CCO arrangements, custody-rule implications, Reg S-P May 2024 amendments.
- `third-party-operational-resilience/exit-plan` — fund service-provider transitions, sub-adviser termination under ICA §15, FINRA 4370 BCM.
- `third-party-operational-resilience/concentration-risk-review` — broker concentration, custodian concentration, pricing-vendor concentration, sub-adviser concentration in fund complexes.
- `regulatory-change-management/regulatory-impact-assessment` — SEC adopting-release decomposition (preamble vs codified), three-date pattern (Federal Register / effective / compliance), Form PF tier-based compliance dates.
- `regulatory-change-management/rule-to-obligation-extraction` — SEC / FINRA citation conventions, vacated-rulemaking handling (PFA Rule June 2024).
- `risk-reporting/risk-committee-pack` — adviser-level ERM committee distinct from fund board, BD net capital and customer-protection feed, Form PF current-event triggers.
- `risk-reporting/cyber-disclosure-readiness` — public-company SEC cyber rule application to listed managers; Reg S-P May 2024 amendments; SEC cybersecurity rule for advisers/funds [verify current state]; FINRA Rule 4530 reportability; coordination with NYDFS Part 500 for NY-licensed entities.
- `ai-governance-model-risk/ai-act-triage` — already speced as needing capital-markets overlay; this lead confirms scope (SEC focus on AI in advisory; SEC predictive-analytics rule proposed July 2023, status [verify]; investment-recommendation, marketing, surveillance, valuation use-case typology).
- `ai-governance-model-risk/ai-risk-tiering` — adviser/BD-specific tier criteria.
- `ai-governance-model-risk/llm-vendor-evidence-review` — SEC and FINRA expectations on AI-vendor evidence in advisory and trading contexts.

## consumer-compliance-fair-lending applicability

Generally not applicable to advisers, BDs, asset managers. Three narrow cross-applicability cases noted in `overlay-snippets.md` (BD margin lending under Reg T; BD-distributed branded credit cards / affiliated bank deposits; marketing-rule and UDAAP doctrinal distinction). Phase 2 decision: no capital-markets overlay file under any consumer-compliance-fair-lending skill. The cross-applicability cases are documented in `overlay-snippets.md` and remain there.

## Plugin-level shared references plan

Stays plugin-level (genuinely shared across the four skills):

- `references/source-map.md` — IA Act / ICA / Exchange Act / FINRA / SEC EXAMS / FINRA Notices anchor list.
- `references/policy-control-library.md` — capital-markets-shaped control patterns (Rule 206(4)-7 written compliance program, Rule 38a-1 fund compliance program, FINRA 3110 supervisory system).
- `references/review-gates.md` — capital-markets review gates (committee, board, CCO certification under FINRA 3130).

Moves per-skill (phase 2):

- Output templates currently sitting in `references/output-templates.md` should be split into per-skill `templates/default-output.md` files (each artifact has a different shape).
- Public regulatory scenarios in `references/public-regulatory-scenarios.md` should be split into per-skill `examples/` files.

## Schema ownership

Borrowed schemas presently in `schemas/` (`obligation`, `control`, `issue`, `ai-use-case`, `vendor`, `test-plan`, `risk-report`) belong to other plugins and should be removed in phase 3 once the owning plugins ship them. Capital-markets-specific schemas needed in phase 2:

- `examination-readiness-pack.schema.json`
- `best-execution-review.schema.json`
- `fund-board-pack.schema.json`
- `marketing-rule-evidence.schema.json`

## Current-state caveats (verify before publishing)

- SEC Private Fund Advisers Rule — adopted Aug 23 2023; vacated by 5th Circuit in National Association of Private Fund Managers v. SEC, June 5 2024. The rule is not in force. Antifraud and recordkeeping reach via §206 / Rule 204-2 remains.
- SEC Cybersecurity Risk Management Rules for Advisers and Funds — proposed Feb 9 2022. [verify current state: re-proposed, withdrawn, or still pending.]
- SEC Predictive Data Analytics Rule (proposed July 2023, "Conflicts of Interest Associated with the Use of Predictive Data Analytics by Broker-Dealers and Investment Advisers"). [verify current state.]
- SEC Reg S-P amendments adopted May 16 2024. [verify exact compliance dates by entity type and size.]
- Form PF 2023 amendments and current-event reporting. [verify the current-event reporting effectiveness post-PFA-vacatur context.]
- Rule 605 / 606 amendments adopted via Release 34-99679, March 6 2024. [verify release number and exact compliance dates.]
- SEC EXAMS Annual Examination Priorities — refresh required to current year.
- FINRA 2024-2026 best-execution refresh notice. [verify whether issued and content.]

## Structural concerns

1. The plugin's name (`capital-markets-asset-management-compliance`) is correct vocabulary but long. README copy should consistently shorten to "capital markets and asset management" in narrative.
2. Adviser, BD, fund, and dual registrant are four distinct registration classes with overlapping but not identical rule lattices. Each spec sheet calls out which classes its workflow targets. Phase 2 must keep this discipline in the SKILL.md.
3. Form-driven artifacts (Form ADV, Form CRS, Form PF, Form N-CEN, Form BD) are referenced across multiple skills. A shared references doc on form structure / timing / cross-checks could reduce duplication. Defer the call to phase 2.
4. The SEC rule pipeline has been unusually volatile in 2023-2026 (multiple vacaturs, withdrawals, proposed rules in flight). The skills in this plugin must be re-validated against the regulatory state before each major release. Annual minimum.

## Source-anchor confidence per skill

| Skill | Confidence | Notes |
|---|---|---|
| adviser-exam-readiness | high on statutory/regulatory text (Rule 206(4)-7, 204A-1, 206(4)-2, 206(4)-1, 204-2, 204(b)-1, 204-3); medium on EXAMS Annual Priorities and Risk Alerts (annual refresh required); medium on PFA Rule, Reg S-P, predictive-analytics, cyber rule current state |
| best-execution-surveillance | high on §206, FINRA 5310, Rule 605/606 baseline; medium on Rule 605/606 March 2024 amendment release number and compliance dates; medium on FINRA 2024-2026 best-execution refresh |
| fund-board-reporting | high on §15(c), §38a-1, ICA §17(e), §28(e); medium on current SEC fund-board guidance and EXAMS focus areas |
| marketing-rule-evidence | high on Rule 206(4)-1 (Dec 2020 adopting release) and the September 2022 + April 2023 Marketing Rule Risk Alerts (April 2023 alert title flagged for verification); high on EXAMS focus area pattern |

Phase 2 must resolve every `[verify]` placeholder before publishing.
