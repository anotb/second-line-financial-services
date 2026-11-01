# Capital Markets and Asset Management Compliance

Sector overlay plugin for SEC-registered investment advisers, broker-dealers, dual registrants, registered funds, and their advisers.

Audience: chief compliance officer, general counsel, head of compliance, head of risk, fund-board secretary, and the advisory teams running the same work for those firms.

## Posture

This is a strict sector-overlay plugin. It ships skills that are genuinely capital-markets-only, shaped by the Investment Advisers Act, the Investment Company Act, the Securities Exchange Act, and the FINRA rule set. Capability skills that already cover the underlying second-line function (control matrix, evidence binder, obligation mapping, regulatory impact assessment, exam brief, vendor diligence, AI use-case intake, model card, risk committee pack, and so on) are not duplicated here. Capital-markets nuance for those capability skills lives as a `references/sector-overlays/capital-markets.md` reference inside each capability skill.

## Skills

| Skill | What it produces |
|---|---|
| `adviser-exam-readiness` | SEC EXAMS / FINRA exam-readiness pack: gap matrix, evidence index, mock-interview prep, remediation list. Covers IA, BD, fund, and dual-registrant document-request lanes. |
| `best-execution-surveillance` | Periodic best-execution review: trade-by-trade exception sampling, aggregate venue and counterparty metrics, FINRA 5310 / IA Act §206 factor analysis, Rule 605 / 606 reconciliation, best-ex committee pack. |
| `fund-board-reporting` | §15(c) and §38a-1 fund-board materials: adviser approval / renewal package, CCO 38a-1 annual review report, compliance and risk reporting cadence, soft-dollar / brokerage / valuation disclosures. |
| `marketing-rule-evidence` | Rule 206(4)-1 marketing-claim evidence and substantiation: testimonial / endorsement compliance, hypothetical-performance treatment, third-party-rating substantiation, books-and-records evidence trail. |

## Try it

- Prepare an SEC exam-readiness pack for a fictional mid-size registered investment adviser.
- Design best-execution surveillance for an adviser's equity order flow.
- List the substantiation evidence needed for a hypothetical performance claim under Marketing Rule 206(4)-1.

## Capital-markets overlays into capability skills

The plugin contributes capital-markets overlay content into capability skills where the SEC / FINRA frame adds material nuance:

- `third-party-operational-resilience/vendor-diligence`, `exit-plan`, `concentration-risk-review`.
- `regulatory-change-management/regulatory-impact-assessment`, `rule-to-obligation-extraction`.
- `risk-reporting/risk-committee-pack`, `cyber-disclosure-readiness`.
- `ai-governance-model-risk/ai-act-triage`, `ai-risk-tiering`, `llm-vendor-evidence-review`.

`consumer-compliance-fair-lending` is generally out of scope for advisers, BDs, and asset managers; narrow cross-applicability cases are documented in spec memos rather than propagated as overlays.

## Source posture

Public anchors only. Named anchors include the IA Act, the ICA, the Exchange Act, FINRA Rules, SEC adopting releases, SEC Division of Examinations Risk Alerts, and SEC Examination Priorities. The SEC rule pipeline has been volatile (multiple vacaturs, withdrawals, and proposed rules in flight as of 2026). Skills in this plugin must be re-validated against current regulatory state before each major release; minimum annual refresh.

## Components

- `skills/` — the four skills above. Each ships its own `SKILL.md`, `references/source-anchors.md`, `templates/`, and (where useful) `schemas/` and `examples/`.
- `references/` — plugin-level shared references: capital-markets source map, named decision forums.
- `schemas/` — capital-markets-specific artifacts.

## Operating posture

The skills draft second-line work product for qualified review by the firm's CCO, General Counsel, head of Compliance, head of Risk, fund-board secretary, or external counsel. They do not approve filings, certify FINRA 3130 / 38a-1 reports, sign Form ADV brochures, file Form PF, or close issues. Every output is staged for human sign-off.

## Install

In Claude Code:

```
/plugin install capital-markets-asset-management-compliance --marketplace anotb/second-line-financial-services
```

Pair with `regulatory-change-management`, `risk-compliance-core`, `risk-reporting`, `compliance-testing`, `ai-governance-model-risk`, and `third-party-operational-resilience` for the full second-line stack.

This plugin works on its own. Mentions of `risk-compliance-core` in the skills are optional hand-offs. Add that plugin for the shared `scoping`, `control-matrix`, and `issue-writeup` skills; installing from the GitHub marketplace adds it automatically.

## Data and behavior

The plugin is Markdown and JSON only: skills, references, schemas, and templates. It has no hooks, scripts, or MCP servers, and it does not send or store data itself. Documents you share are handled by Claude under your account's terms, so apply your firm's rules for confidential supervisory information, suspicious-activity material, and personal data before sharing them.

## Human review and AI disclosure

Intended for second-line and compliance professionals. Outputs are AI-assisted drafts. A qualified person with authority to change an output must review it before it is delivered or used in a decision, and stays accountable for it. Where an output supports advice to an individual or a decision about an individual, such as credit, insurance, employment, or legal rights, tell that individual AI was used to produce it. The plugin does not make credit, underwriting, claims, filing, or other final decisions, gives no personalized investment advice, and does not execute transactions or move money. It is not legal or regulatory advice.
