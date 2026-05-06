# capital-markets-asset-management-compliance

Sector overlay plugin for SEC-registered investment advisers, broker-dealers, dual registrants, registered funds, and their advisers.

## Posture

This plugin ships skills that are genuinely capital-markets-only — workflows shaped by the Investment Advisers Act, the Investment Company Act, the Securities Exchange Act, and the FINRA rule set. Capability skills that already cover the underlying second-line function (control matrix, evidence binder, obligation mapping, regulatory impact assessment, exam brief, vendor diligence, AI use-case intake, model card, risk committee pack, and so on) are not duplicated here. The capital-markets nuance for those capability skills lives as a `references/sector-overlays/capital-markets.md` reference document inside each capability skill.

## Skills

| Skill | What it produces |
|---|---|
| `adviser-exam-readiness` | SEC EXAMS / FINRA exam-readiness pack: gap matrix, evidence index, mock-interview prep, remediation list. Covers IA, BD, fund, and dual-registrant document-request lanes. |
| `best-execution-surveillance` | Periodic best-execution review: trade-by-trade exception sampling, aggregate venue and counterparty metrics, FINRA 5310 / IA Act §206 factor analysis, Rule 605/606 reconciliation, best-ex committee pack. |
| `fund-board-reporting` | §15(c) and §38a-1 fund-board materials: adviser approval / renewal package, CCO 38a-1 annual review report, compliance and risk reporting cadence, soft-dollar / brokerage / valuation disclosures. |
| `marketing-rule-evidence` | Rule 206(4)-1 marketing claim evidence and substantiation: testimonial / endorsement compliance, hypothetical-performance treatment, third-party-rating substantiation, books-and-records evidence trail. |

## Sector-overlay contributions to capability skills

The plugin contributes capital-markets overlay reference content to capability skills where capital-markets adds material nuance. Phase-2 build targets (per `docs/specs/capital-markets-asset-management-compliance/overlay-snippets.md`):

- `third-party-operational-resilience/vendor-diligence`, `exit-plan`, `concentration-risk-review`
- `regulatory-change-management/regulatory-impact-assessment`, `rule-to-obligation-extraction`
- `risk-reporting/risk-committee-pack`, `cyber-disclosure-readiness`
- `ai-governance-model-risk/ai-act-triage`, `ai-risk-tiering`, `llm-vendor-evidence-review`

`consumer-compliance-fair-lending` is generally out of scope for advisers, BDs, and asset managers; narrow cross-applicability cases are documented in `overlay-snippets.md` rather than propagated as overlay docs.

## Operating posture

The skills in this plugin draft second-line work product for qualified review by the firm's Chief Compliance Officer, General Counsel, head of Compliance, head of Risk, fund board secretary, or external counsel. They do not approve filings, certify FINRA 3130 / 38a-1 reports, sign Form ADV brochures, file Form PF, or close issues. Every output is staged for human sign-off.

## Source posture

Public regulatory sources only. The named anchors include the IA Act, the ICA, the Exchange Act, FINRA Rules, SEC adopting releases, SEC Division of Examinations Risk Alerts, and SEC Examination Priorities. The SEC rule pipeline has been volatile (multiple vacaturs, withdrawals, and proposed rules in flight as of 2026). Skills in this plugin must be re-validated against current regulatory state before each major release; minimum annual refresh.

## Install

```
claude plugin marketplace add /path/to/second-line-financial-services
claude plugin install capital-markets-asset-management-compliance@second-line-financial-services
```

Pair with `regulatory-change-management`, `risk-compliance-core`, `risk-reporting`, `compliance-testing`, `ai-governance-model-risk`, and `third-party-operational-resilience` for the full second-line stack.

## Disclaimer

Nothing in this plugin is legal, compliance, investment, tax, accounting, regulatory, audit, or supervisory advice. The plugin drafts second-line work product for qualified professional review. It does not approve filings, file regulatory reports, certify compliance programs, sign brochures, or close issues.
