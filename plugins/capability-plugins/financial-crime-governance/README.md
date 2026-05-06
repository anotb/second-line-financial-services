# Financial Crime Governance

Second-line review layer over a firm's BSA/AML, sanctions, and adverse-media program.

This plugin is for second-line practitioners (BSA officers, AML compliance leads, sanctions officers, financial crime QA teams, EDD analysts) at regulated firms and the advisory and consulting teams that run the same work for those firms. The skills draft review artifacts. Qualified humans (BSA officer, sanctions officer, EDD committee, SAR review committee, model risk committee) approve, file, rate, escalate, or close. Nothing in this plugin makes a final SAR, sanctions, onboarding, exit, rating, or filing decision.

## v1 skill list

- `cdd-risk-review` — review a customer due diligence file (new account, periodic refresh, event-driven refresh) against the four CDD pillars: customer identification and verification, beneficial ownership identification and verification, nature and purpose of the relationship, and ongoing monitoring. Produces a review memo with material gaps and recommended human-review gates.
- `edd-escalation-pack` — draft an EDD escalation pack for a higher-risk customer profile (PEP, private banking, correspondent, cash-intensive, complex ownership, sanctions-adjacent). Assembles ownership chain, source of funds and source of wealth, expected vs actual activity, adverse media, sanctions posture, conduct-risk indicators, and reviewer questions for the EDD committee.
- `sar-decision-qa` — quality-review a SAR / no-SAR decision file against FFIEC SAR section expectations. Reviews alert chronology, investigation steps, evidence, decision rationale, continuing-activity posture, and confidentiality controls. Does not file, decline, amend, or close.
- `aml-model-monitoring` — review ongoing monitoring evidence for an AML transaction-monitoring system as a model under model risk management guidance. Covers data quality, segmentation drift, scenario tuning, threshold-change governance, alert volume and productivity, validation evidence, and below-the-line testing. Boundary with `ai-governance-model-risk` documented in `docs/specs/financial-crime-governance/AUDIT.md`.
- `sanctions-screening-qa` — review sanctions screening program evidence: list-management governance, customer and transaction screening configuration, match-logic and fuzzy-matching tuning, list-update timeliness, alert disposition documentation, false-positive rationale, escalation paths, 50-percent-rule and sectoral-sanctions handling, and screening-evasion exposure (cyber overlay).
- `negative-news-triage` — triage an adverse-media or negative-news hit set against a customer or entity for relevance, identity confidence, source reliability, materiality, and downstream action. Feeds into `cdd-risk-review`, `edd-escalation-pack`, and `sar-decision-qa`.

## Source anchor base

US-deep first. Every skill anchored to named, dated US public sources: FFIEC BSA/AML Examination Manual (CDD, SAR, Beneficial Ownership, OFAC sections), FinCEN CDD Final Rule (May 2016, effective May 2018), 31 CFR 1010.230 Beneficial Ownership Rule, 31 CFR 1010.380 BOI reporting (date as-of given CTA litigation timeline), 31 CFR 1020.320 / 1023.320 / parallels for SAR, 31 USC 5318(g) SAR statutory authority, A Framework for OFAC Compliance Commitments (May 2019), OFAC SDN and SSI lists, OFAC 50 Percent Rule guidance (August 2014), SR 11-7 / OCC Bulletin 2026-13 for AML monitoring as a model, OCC/FRB/FDIC/NCUA Joint Statement on Risk-Focused BSA/AML Supervision (July 2021), FinCEN/Federal Banking Agencies Joint Statement on Innovation in BSA/AML Compliance (December 2018), and applicable FinCEN advisories (typology references, dated as-of). EU and UK overlays (FATF, EBA AML guidelines, UK MLRs, UK OFSI) come in v1.1 as overlay reference docs inside the skill.

## Cross-cutting overlays embedded in skills

- Conduct on `edd-escalation-pack` — PEP, private banking, and high-risk-customer profiles intersect with conduct risk in ways the EDD committee should see (foreign-procurement exposure, sales-practice exposure, vulnerable-customer overlap).
- Cyber on `sanctions-screening-qa` — sanctions screening evasion via virtual currency, ransomware payment exposure, identity manipulation, BIN sponsorship, and bridge / DeFi exposure. Anchored to OFAC virtual-currency and ransomware guidance and parallel FinCEN advisories.

## Boundary with `ai-governance-model-risk`

`aml-model-monitoring` lives here because the artifact is AML-specific (segmentation drift, scenario tuning, alert volume and productivity, BTL testing, downstream SAR effects). The model primitives — definition of "model", inventory, intake, tiering, model card, validation framework, governance, and effective challenge — live in `ai-governance-model-risk` and are reused. AML monitoring systems flow through those primitives the same way every other model does. See `docs/specs/financial-crime-governance/AUDIT.md` for the full hand-off.

## Components

- `skills/` — the six skills above. Each ships a `SKILL.md` and a `templates/default-output.md`. Phase 2 adds per-skill `references/source-anchors.md`, sector overlays, cross-cutting overlays for `edd-escalation-pack` and `sanctions-screening-qa`, `examples/`, and (where applicable) `scripts/`.
- `references/` — plugin-level shared references: trimmed public-source map, financial-crime policy and control library, named review gates (EDD committee, SAR review committee, sanctions release, model validation), and shared output conventions.
- `schemas/` — structured-output templates. `issue.schema.json` is used by every skill that surfaces material findings. Phase 2 adds three plugin-specific schemas: `cdd-file`, `alert-disposition`, `sanctions-alert`. Other plugin schemas currently sitting in this folder move to their owning plugins in phase 3.

## Operating posture

The plugin drafts second-line work product for qualified review. It does not approve, file, rate, onboard, decline, notify, or close items. Public regulatory sources are anchors, not legal interpretations. OFAC list citations and FinCEN advisory citations are dated as-of in every artifact; sanctions and BOI rule status are perishable and must not be asserted without a current date.
