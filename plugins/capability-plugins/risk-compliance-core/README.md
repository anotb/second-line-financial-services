# Risk Compliance Core

Foundational primitives. The artifacts here show up across other capability plugins: the scope record, the obligation register, the control matrix, the evidence binder, the issue write-up, the named-gate matrix, the policy-gap review. Other capability plugins consume these primitives rather than redefining them.

Audience: second-line risk and compliance leads who write these artifacts (CRO-office, MRMO, TPRM, BSA, CCO, head of controls testing) and the advisory teams running the same work for those firms.

## Skills

| Skill | What it produces |
|---|---|
| `scoping` | Scoping charter and structured scope record (institution, review type, persona, source posture, sector overlay, cross-cutting overlay, exclusions). Bootstraps the downstream skills. |
| `obligation-mapping` | Structured obligation register from source documents (rules, guidance, exam manuals, internal policies) with applicability, control objectives, evidence required, and owners. |
| `control-matrix` | Obligation-anchored risk-control matrix mapping control objectives, activities, owners, frequency, evidence pointers, test method, last-test result, and open issues. |
| `evidence-binder` | Indexed evidence pack for an exam, internal audit, model validation, vendor review, or committee review, with system-of-record provenance and completeness flags. |
| `issue-writeup` | Finding using condition / criteria / cause / effect plus severity rationale, remediation, owner, target date, and closure-evidence definition. |
| `human-review-gates` | Named-gate matrix for a workflow (AI use-case lifecycle, vendor onboarding, issue rating) with required reviewers, decision criteria, stop conditions, and escalation paths. |
| `policy-gap-review` | Policy-versus-obligation gap matrix with severity, recommended edits, and evidence needs against a named obligation set or public-source benchmark. |

## Try it

- Scope a second-line review of third-party onboarding at a mid-size US bank, including regulators, source posture, and overlays.
- Build an obligation map for Regulation E error resolution (12 CFR 1005.11) from public sources, and mark firm evidence as needed.
- Draft an issue write-up: quarterly user-access reviews on the wire system were missed in two of the last four quarters.

## How this chains

The `scoping` skill runs first on most reviews and produces a structured scope record other skills in the repo can consume. `obligation-mapping` feeds `control-matrix`, which feeds `evidence-binder` and the testing skills in `compliance-testing`. `issue-writeup` is the standard finding shape that `compliance-testing/exception-analysis`, `third-party-operational-resilience` review skills, and the `risk-reporting/management-response` skill all hand off to. `human-review-gates` is the named-reviewer matrix referenced by AI use-case, vendor onboarding, and issue-rating workflows across the repo. `policy-gap-review` runs against the obligation register from `obligation-mapping` or the firm's policy text directly.

## Source posture

Public anchors only. Substantive base for the foundational primitives:

- COSO 2013 Internal Control Integrated Framework (Principles 1-17), COSO ERM 2017.
- IIA International Professional Practices Framework (Performance Standards 2200, 2210, 2220, 2240, 2310, 2320, 2330, 2340; Standard 1300 QAIP).
- AICPA AU-C 230, 300, 330, 500, 530 (audit-methodology anchors borrowed in second-line testing, not direct legal requirements).
- FFIEC IT Examination Handbook structure for evidence-binder shape.
- The relevant agency-specific anchors (interagency third-party guidance, OCC Heightened Standards, FRB SR letters, CFPB CMS expectations, NAIC Model Audit Rule, IIA standards) load from sector and cross-cutting overlays per skill.

Skills cite by anchor file path; the regulator and section references live in `references/source-anchors.md`.

## Sector and cross-cutting overlays

All four sectors and the cyber / privacy / conduct cross-cutting topics apply to most skills here. Overlays load conditionally from the scope record and live under each skill's `references/sector-overlays/` and `references/cross-cutting/` folders.

## Components

- `skills/` — the seven skills above. Each ships its own `SKILL.md`, `references/source-anchors.md`, sector and cross-cutting overlays where applicable, `templates/default-output.md`, and (where useful) `schemas/` and `examples/`.
- `references/` — plugin-level shared references: source map, policy and control library, named decision forums and confidence labels.
- `schemas/` — structured-output templates for obligations, controls, and issues. Each plugin self-ships the schemas its skills use, matching Anthropic's first-party self-contained pattern. Schema dedup (drop schemas a plugin's skills don't actually use) is tracked in [ROADMAP.md](https://github.com/anotb/second-line-financial-services/blob/main/ROADMAP.md).

## Operating posture

The plugin drafts second-line work product for qualified review. It does not approve, file, rate, onboard, decline, notify, or close items. Public regulatory and standards sources are anchors, not legal interpretations.

## Install

In Claude Code:

```
/plugin install risk-compliance-core --marketplace anotb/second-line-financial-services
```

## Data and behavior

The plugin is Markdown and JSON only: skills, references, schemas, and templates. It has no hooks, scripts, or MCP servers, and it does not send or store data itself. `.mcp.example.json` is an inactive template that Claude does not load, and it connects to nothing until a firm replaces it with an approved server. Documents you share are handled by Claude under your account's terms, so apply your firm's rules for confidential supervisory information, suspicious-activity material, and personal data before sharing them.

## Human review and AI disclosure

Intended for second-line and compliance professionals. Outputs are AI-assisted drafts. A qualified person with authority to change an output must review it before it is delivered or used in a decision, and stays accountable for it. Where an output supports advice to an individual or a decision about an individual, such as credit, insurance, employment, or legal rights, tell that individual AI was used to produce it. The plugin does not make credit, underwriting, claims, filing, or other final decisions, gives no personalized investment advice, and does not execute transactions or move money. It is not legal or regulatory advice.
