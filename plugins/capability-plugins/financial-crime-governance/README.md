# Financial Crime Governance

Second-line review layer over a firm's BSA / AML, sanctions, and adverse-media program.

Audience: BSA officers, AML compliance leads, sanctions officers, financial-crime QA teams, EDD analysts, AML model risk leads, and the advisory teams running the same work for those firms. Skills draft review artifacts. Qualified humans (BSA officer, sanctions officer, EDD committee, SAR review committee, model risk committee) approve, file, rate, escalate, or close. Nothing in this plugin makes a final SAR, sanctions, onboarding, exit, rating, or filing decision.

## Skills

| Skill | What it produces |
|---|---|
| `cdd-risk-review` | Review of a CDD file (new account, periodic refresh, event-driven) against the four CDD pillars: customer identification and verification, beneficial ownership, nature and purpose, and ongoing monitoring. Output is a review memo with material gaps and recommended decision points. |
| `edd-escalation-pack` | Draft EDD escalation pack for a higher-risk customer profile (PEP, private banking, correspondent, cash-intensive, complex ownership, sanctions-adjacent). Assembles ownership chain, source of funds and source of wealth, expected versus actual activity, adverse media, sanctions posture, conduct-risk indicators, and reviewer questions. |
| `sar-decision-qa` | QA review of a SAR / no-SAR decision file against FFIEC SAR section expectations. Reviews alert chronology, investigation steps, evidence, decision rationale, continuing-activity posture, and confidentiality controls. Refreshed against the October 9 2025 SAR FAQs. |
| `aml-model-monitoring` | Review of ongoing monitoring evidence for an AML transaction-monitoring system as a model under MRM guidance. Covers data quality, segmentation drift, scenario tuning, threshold-change governance, alert volume and productivity, validation evidence, and below-the-line testing. |
| `sanctions-screening-qa` | Review of a sanctions screening program: list-management governance, customer and transaction screening configuration, match-logic and fuzzy-matching tuning, list-update timeliness, alert disposition documentation, false-positive rationale, escalation paths, 50-percent-rule and sectoral-sanctions handling, and screening-evasion exposure (cyber overlay). |
| `negative-news-triage` | Triage of an adverse-media or negative-news hit set against a customer or entity for relevance, identity confidence, source reliability, materiality, and downstream action. Feeds into `cdd-risk-review`, `edd-escalation-pack`, and `sar-decision-qa`. |

## How this chains

`negative-news-triage` is the upstream feeder. `cdd-risk-review` runs at onboarding and periodic refresh; the EDD path branches to `edd-escalation-pack` for higher-risk profiles. Detection-side alerts run through `sanctions-screening-qa` (list-side) and `aml-model-monitoring` (behaviour-side); investigation-side files run through `sar-decision-qa`. The model primitives the AML monitoring system flows through (definition of model, inventory, intake, tiering, model card, validation framework, governance, effective challenge) live in `ai-governance-model-risk` and are reused; `aml-model-monitoring` is the AML-specific lens on alert volume, scenario tuning, BTL testing, and downstream SAR effects.

## Source posture

US-deep first. Named anchors include FFIEC BSA / AML Examination Manual (CDD, SAR, Beneficial Ownership, OFAC sections), FinCEN CDD Final Rule (May 2016, effective May 2018), 31 CFR 1010.230 Beneficial Ownership Rule, 31 CFR 1010.380 BOI reporting (date as-of given CTA litigation timeline), 31 CFR 1020.320 / 1023.320 and parallels for SAR, 31 USC 5318(g) SAR statutory authority, FinCEN MSB rules at 31 CFR 1022, OFAC Framework for Compliance Commitments (May 2019), OFAC SDN and SSI lists, OFAC 50 Percent Rule guidance (August 2014), the April 2026 joint guidance on model risk management for AML monitoring as a model, OCC / FRB / FDIC / NCUA Joint Statement on Risk-Focused BSA / AML Supervision (July 2021), FinCEN / Federal Banking Agencies Joint Statement on Innovation in BSA / AML Compliance (December 2018), and applicable FinCEN advisories. EU and UK overlays (FATF, EBA AML guidelines, UK MLRs, UK OFSI) come in v1.1 as reference docs inside the skills.

OFAC list citations and FinCEN advisory citations are dated as-of in every artifact. Sanctions and BOI rule status are perishable and must not be asserted without a current date.

## Cross-cutting overlays

- Conduct on `edd-escalation-pack`: PEP, private banking, and high-risk-customer profiles intersect with conduct risk in ways the EDD committee should see (foreign-procurement exposure, sales-practice exposure, vulnerable-customer overlap).
- Cyber on `sanctions-screening-qa`: sanctions evasion via virtual currency, ransomware payments, identity manipulation, BIN sponsorship, and bridge / DeFi exposure. Anchored to OFAC virtual-currency and ransomware guidance and parallel FinCEN advisories.

## Components

- `skills/` — the six skills above. Each ships its own `SKILL.md`, `references/source-anchors.md`, sector and cross-cutting overlays where applicable, `templates/default-output.md`, and (where useful) `schemas/` and `examples/`.
- `references/` — plugin-level shared references: source map (trimmed to financial-crime), policy and control library, named review forums (EDD committee, SAR review committee, sanctions release, model validation), shared output conventions.
- `schemas/` — `issue.schema.json` plus financial-crime artifacts (`cdd-file`, `alert-disposition`, `sanctions-alert`).

## Operating posture

The plugin drafts second-line work product for qualified review. It does not approve, file, rate, onboard, decline, notify, or close items. Public regulatory sources are anchors, not legal interpretations.
