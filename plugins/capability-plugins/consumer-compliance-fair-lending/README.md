# consumer-compliance-fair-lending

Second-line capability plugin for consumer compliance and fair-lending work. Six skills produce review artifacts, gap lists, and red flags for human decision. The plugin does not approve loans, deny adverse-action notices, finalize fair-lending or UDAAP determinations, file Section 1071 data, or take down live marketing.

## Audience

Consumer compliance officers, fair-lending and fair-housing leads, UDAAP review teams, marketing review teams, complaint management leads. Both inside regulated firms (depository, fintech with sponsor bank, mortgage, auto, BNPL, small-business lending) and inside advisory or consulting teams running the same work for those firms.

## Skills

1. `adverse-action-review` — Review a population of adverse action decisions and notices for ECOA / Reg B 1002.9 compliance, traceability of cited reasons back to the model and data, and disparate-impact red flags. Anchors on Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary plus the April 2023 Joint Statement on algorithmic discrimination where AI / complex models are in the decisioning path. (CFPB Circulars 2022-03 / 2023-03 are **withdrawn May 12, 2025; historical only.**)
2. `complaint-theme-analysis` — Aggregate and theme a population of consumer complaints (CFPB Complaint Database, internal, AG, social) into named themes with severity, root-cause hypotheses, regulatory exposure, and conduct-risk implications.
3. `fair-lending-test-plan` — Draft a fair-lending test plan covering scope, decision points, test types (redlining, comparative file review, regression on underwriting and pricing, marketing distribution, steering, servicing / loss mitigation, less-discriminatory-alternative search), and committee approval gate. Cites CFPB Circulars and HUD AI guidance where AI / ML decisioning is in scope.
4. `marketing-claim-review` — Review consumer-financial marketing assets for claim substantiation, Reg Z / MLA / TRID disclosure adequacy, fair-lending distribution / targeting, dark patterns, privacy claim accuracy, and UDAAP triggers.
5. `section1071-readiness` — Draft a Section 1071 small-business lending data readiness assessment against 12 CFR 1002.103-114, with data-point inventory aligned to 1002.107, firewall design under 1002.108, and reporting / FIG conformance.
6. `udaap-risk-review` — Review a product, feature, fee, disclosure flow, servicing process, or marketing motion for UDAAP risk under Dodd-Frank §1031 / §1036, element by element (deception, unfairness, abusiveness), with consumer-harm hypothesis and remediation.

## Try it

- Draft a fair-lending test plan for a US auto lender's dealer-markup program.
- Review this marketing claim for UDAAP risk: "Get approved in minutes with no impact to your credit."
- Build a Section 1071 readiness assessment for a mid-size small-business lender.

## Source posture

Public-source anchored. Named regulatory sources, dated, with section references. Worked examples are derived from public CFPB / DOJ / FTC enforcement themes and consent orders; no named institutions unless they are public defendants in a finalized enforcement action with a published consent order. State-privacy citations are flagged with `[verify state-specific scope]` because state privacy law varies and is evolving.

## Cross-cutting overlays embedded in skills

Cross-cutting topics live as reference docs inside the skills they touch, not as separate plugins:

- Privacy: `adverse-action-review/references/cross-cutting/privacy.md` (GLBA Safeguards, state privacy implications), `marketing-claim-review/references/cross-cutting/privacy.md` (privacy-claim substantiation, AdChoices, dark-pattern privacy).
- Conduct: `udaap-risk-review/references/cross-cutting/conduct.md`, `complaint-theme-analysis/references/cross-cutting/conduct.md`.

AI-related cross-cutting is implicit on `adverse-action-review` and `fair-lending-test-plan`. Both MUST anchor on Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary and the April 2023 Joint Statement on algorithmic discrimination where the underlying decisioning is AI / ML. (CFPB Circulars 2022-03 / 2023-03 are **withdrawn May 12, 2025; historical only.** Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary continue to apply on their own terms.) `marketing-claim-review` and `udaap-risk-review` cite the Joint Statement when AI personalization or AI-generated content is in scope.

## Components

- `skills/` — the six skills. Skills supersede legacy `commands/` for new content per current Claude Code guidance.
- `references/` — plugin-level shared references: source map (scoped to consumer-compliance / fair-lending), policy-control library, decision checkpoints.
- `schemas/` — plugin-level schemas for cross-skill artifacts. Per-skill schemas live under `<skill>/schemas/`. Schema dedup (drop schemas a plugin's skills don't actually use) is tracked in [ROADMAP.md](https://github.com/anotb/second-line-financial-services/blob/main/ROADMAP.md).

Per-skill anatomy (mirrors the Anthropic per-skill layout):

```
<skill>/
  SKILL.md
  references/
    source-anchors.md
    sector-overlays/{banking,insurance,capital-markets,payments-fintech}.md
    cross-cutting/{privacy,conduct}.md     # where applicable
  templates/default-output.md
  schemas/<skill>.schema.json
  examples/<scenario>.md
```

## Operating posture

- Drafts second-line work product for qualified review.
- Does not approve, file, rate, onboard, decline, notify, or close items.
- Treats public guidance as anchor, not as binding legal interpretation.
- Separates source evidence, management assertion, public-source obligation, and inference.
- Marks unsupported items as `[evidence needed]`.
- Stops before any final approval, adverse action notification, customer communication, marketing launch, 1071 filing, or issue closure.

## Install

In Claude Code:

```
/plugin install consumer-compliance-fair-lending --marketplace anotb/second-line-financial-services
```

This plugin works on its own. Mentions of `risk-compliance-core` in the skills are optional hand-offs. Add that plugin for the shared `scoping`, `control-matrix`, and `issue-writeup` skills; installing from the GitHub marketplace adds it automatically.

## Data and behavior

The plugin is Markdown and JSON only: skills, references, schemas, and templates. It has no hooks, scripts, or MCP servers, and it does not send or store data itself. `.mcp.example.json` is an inactive template that Claude does not load, and it connects to nothing until a firm replaces it with an approved server. Documents you share are handled by Claude under your account's terms, so apply your firm's rules for confidential supervisory information, suspicious-activity material, and personal data before sharing them.

## Human review and AI disclosure

Intended for second-line and compliance professionals. Outputs are AI-assisted drafts. A qualified person with authority to change an output must review it before it is delivered or used in a decision, and stays accountable for it. Where an output supports advice to an individual or a decision about an individual, such as credit, insurance, employment, or legal rights, tell that individual AI was used to produce it. The plugin does not make credit, underwriting, claims, filing, or other final decisions, gives no personalized investment advice, and does not execute transactions or move money. It is not legal or regulatory advice.
