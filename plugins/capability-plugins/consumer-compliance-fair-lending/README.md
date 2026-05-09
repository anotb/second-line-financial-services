# consumer-compliance-fair-lending

Second-line capability plugin for consumer compliance and fair-lending work. Six skills produce review artifacts, gap lists, and red flags for human decision. The plugin does not approve loans, deny adverse-action notices, finalize fair-lending or UDAAP determinations, file Section 1071 data, or take down live marketing.

## Audience

Consumer compliance officers, fair-lending and fair-housing leads, UDAAP review teams, marketing review teams, complaint management leads. Both inside regulated firms (depository, fintech with sponsor bank, mortgage, auto, BNPL, small-business lending) and inside advisory or consulting teams running the same work for those firms.

## Skills (v1)

1. `adverse-action-review` — Review a population of adverse action decisions and notices for ECOA / Reg B 1002.9 compliance, traceability of cited reasons back to the model and data, and disparate-impact red flags. Anchors on Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary plus the April 2023 Joint Statement on algorithmic discrimination where AI / complex models are in the decisioning path. (CFPB Circulars 2022-03 / 2023-03 are **withdrawn May 12, 2025; historical only.**)
2. `complaint-theme-analysis` — Aggregate and theme a population of consumer complaints (CFPB Complaint Database, internal, AG, social) into named themes with severity, root-cause hypotheses, regulatory exposure, and conduct-risk implications.
3. `fair-lending-test-plan` — Draft a fair-lending test plan covering scope, decision points, test types (redlining, comparative file review, regression on underwriting and pricing, marketing distribution, steering, servicing / loss mitigation, less-discriminatory-alternative search), and committee approval gate. Cites CFPB Circulars and HUD AI guidance where AI / ML decisioning is in scope.
4. `marketing-claim-review` — Review consumer-financial marketing assets for claim substantiation, Reg Z / MLA / TRID disclosure adequacy, fair-lending distribution / targeting, dark patterns, privacy claim accuracy, and UDAAP triggers.
5. `section1071-readiness` — Draft a Section 1071 small-business lending data readiness assessment against 12 CFR 1002.103-114, with data-point inventory aligned to 1002.107, firewall design under 1002.108, and reporting / FIG conformance.
6. `udaap-risk-review` — Review a product, feature, fee, disclosure flow, servicing process, or marketing motion for UDAAP risk under Dodd-Frank §1031 / §1036, element by element (deception, unfairness, abusiveness), with consumer-harm hypothesis and remediation.

## Source posture

Public-source anchored. Named regulatory sources, dated, with section references. Worked examples are derived from public CFPB / DOJ / FTC enforcement themes and consent orders; no named institutions unless they are public defendants in a finalized enforcement action with a published consent order. State-privacy citations are flagged with `[verify state-specific scope]` because state privacy law varies and is evolving.

## Cross-cutting overlays embedded in skills

Per the v1 plan, cross-cutting topics live as reference docs inside the skills they touch, not as separate plugins:

- Privacy: `adverse-action-review/references/cross-cutting/privacy.md` (GLBA Safeguards, state privacy implications), `marketing-claim-review/references/cross-cutting/privacy.md` (privacy-claim substantiation, AdChoices, dark-pattern privacy).
- Conduct: `udaap-risk-review/references/cross-cutting/conduct.md`, `complaint-theme-analysis/references/cross-cutting/conduct.md`.

AI-related cross-cutting is implicit on `adverse-action-review` and `fair-lending-test-plan`. Both MUST anchor on Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary and the April 2023 Joint Statement on algorithmic discrimination where the underlying decisioning is AI / ML. (CFPB Circulars 2022-03 / 2023-03 are **withdrawn May 12, 2025; historical only.** Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary continue to apply on their own terms.) `marketing-claim-review` and `udaap-risk-review` cite the Joint Statement when AI personalization or AI-generated content is in scope.

## Components

- `skills/` — the six v1 skills. Skills supersede legacy `commands/` for new content per current Claude Code guidance.
- `references/` — plugin-level shared references: source map (pruned to consumer-compliance / fair-lending in v1), policy-control library, decision checkpoints.
- `schemas/` — plugin-level schemas for cross-skill artifacts. Phase 3 moves borrowed schemas to their owning plugins; new per-skill schemas land under `<skill>/schemas/`.

Per-skill anatomy (v1, mirrors the Anthropic per-skill layout):

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
