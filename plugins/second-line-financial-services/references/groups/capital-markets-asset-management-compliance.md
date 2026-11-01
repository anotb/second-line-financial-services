# Capital Markets and Asset Management Compliance

Sector overlay plugin for SEC-registered investment advisers, broker-dealers, dual registrants, registered funds, and their advisers.

Audience: chief compliance officer, general counsel, head of compliance, head of risk, fund-board secretary, and the advisory teams running the same work for those firms.

## Posture

This is a strict sector-overlay plugin. It ships skills that are genuinely capital-markets-only, shaped by the Investment Advisers Act, the Investment Company Act, the Securities Exchange Act, and the FINRA rule set. Capability skills that already cover the underlying second-line function (control matrix, evidence binder, obligation mapping, regulatory impact assessment, exam brief, vendor diligence, AI use-case intake, model card, risk committee pack, and so on) are not duplicated here. Capital-markets nuance for those capability skills lives as a `references/sector-overlays.md#capital-markets` reference inside each capability skill.

## Skills

| Skill | What it produces |
|---|---|
| `adviser-exam-readiness` | SEC EXAMS / FINRA exam-readiness pack: gap matrix, evidence index, mock-interview prep, remediation list. Covers IA, BD, fund, and dual-registrant document-request lanes. |
| `best-execution-surveillance` | Periodic best-execution review: trade-by-trade exception sampling, aggregate venue and counterparty metrics, FINRA 5310 / IA Act §206 factor analysis, Rule 605 / 606 reconciliation, best-ex committee pack. |
| `fund-board-reporting` | §15(c) and §38a-1 fund-board materials: adviser approval / renewal package, CCO 38a-1 annual review report, compliance and risk reporting cadence, soft-dollar / brokerage / valuation disclosures. |
| `marketing-rule-evidence` | Rule 206(4)-1 marketing-claim evidence and substantiation: testimonial / endorsement compliance, hypothetical-performance treatment, third-party-rating substantiation, books-and-records evidence trail. |

## Capital-markets overlays into capability skills

The plugin contributes capital-markets overlay content into capability skills where the SEC / FINRA frame adds material nuance:

- `vendor-diligence`, `exit-plan`, `concentration-risk-review`.
- `regulatory-impact-assessment`, `rule-to-obligation-extraction`.
- `risk-committee-pack`, `cyber-disclosure-readiness`.
- `ai-act-triage`, `ai-risk-tiering`, `llm-vendor-evidence-review`.

`consumer-compliance-fair-lending` is generally out of scope for advisers, BDs, and asset managers; narrow cross-applicability cases are documented in spec memos rather than propagated as overlays.

## Source posture

Public anchors only. Named anchors include the IA Act, the ICA, the Exchange Act, FINRA Rules, SEC adopting releases, SEC Division of Examinations Risk Alerts, and SEC Examination Priorities. The SEC rule pipeline has been volatile (multiple vacaturs, withdrawals, and proposed rules in flight as of 2026). Skills in this plugin must be re-validated against current regulatory state before each major release; minimum annual refresh.

## Components

- `skills/` — the four skills above. Each ships its own `SKILL.md`, `references/source-anchors.md`, `templates/`, and (where useful) `schemas/` and `examples.md`.
- `references/` — plugin-level shared references: capital-markets source map, named decision forums.
- `schemas/` — capital-markets-specific artifacts.

## Operating posture

The skills draft second-line work product for qualified review by the firm's CCO, General Counsel, head of Compliance, head of Risk, fund-board secretary, or external counsel. They do not approve filings, certify FINRA 3130 / 38a-1 reports, sign Form ADV brochures, file Form PF, or close issues. Every output is staged for human sign-off.
