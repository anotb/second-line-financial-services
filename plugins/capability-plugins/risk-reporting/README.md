# Risk Reporting

CRO-function risk reporting. The artifacts here are the load-bearing outputs of the second-line risk-reporting machine.

This is the broader 1.5 / 2-line risk-reporting function, not compliance reporting. It covers the enterprise risk committee pack, the BCBS 239 self-assessment, KRI / KCI commentary, SEC cyber disclosure readiness, management attestation packs, and management responses to regulator and audit findings. Audience: Chief Risk Officer office, head of risk reporting, head of operational-risk reporting, head of capital and liquidity risk reporting, board secretary teams, and the disclosure committee.

Compliance reporting (the obligations-to-controls-to-evidence chain) lives in `risk-compliance-core` and `compliance-testing`. Risk reporting subsumes compliance reporting at the committee-pack level but is much wider: it aggregates across credit, market, liquidity, operational, compliance, financial-crime, model, third-party, cyber, and (where applicable) climate.

## v1 skill list

| Skill | Artifact |
| --- | --- |
| `risk-committee-pack` | Enterprise risk committee pack: heat map, top risks, material risk events, KRI movement and breaches, RAS status, issues and remediation, forward-looking commentary, decision items. |
| `bcbs239-gap-assessment` | BCBS 239 self-assessment against the fourteen principles, organized by overarching governance, aggregation, reporting, and supervisory review. |
| `kri-commentary` | Per-KRI / KCI commentary block: root cause, contributing factors, action taken, action planned, residual-risk view, second-line challenge note. |
| `cyber-disclosure-readiness` | SEC cyber disclosure readiness pack: 8-K Item 1.05 trigger and materiality workpaper, 10-K Item 106 disclosure draft, disclosure-controls (DCP) readiness map. |
| `attestation-pack` | Management attestation pack: scope, control inventory, evidence index, exceptions, compensating controls, prior-period remediation, assertion language, sign-off. |
| `management-response` | Management response to a regulator MRA / MRIA, audit finding, or external assessor finding: acceptance posture, root cause, action plan with milestones, evidence-of-effectiveness plan, reporting cadence. |

## Use note

A second-line lead picks up this plugin when the work is one of these named artifacts: a quarterly risk committee pack, a BCBS 239 self-assessment ahead of a horizontal review, a per-KRI commentary block at second-line standard, the disclosure-committee readiness for an 8-K Item 1.05 trigger, an annual management attestation pack, or a draft management response to an MRA / MRIA or audit finding. The skills draft. A qualified reviewer signs off.

## Operating posture

This plugin drafts second-line work product for qualified review. It does not approve, file, rate, onboard, decline, notify, or close items. The named reviewers for the artifacts produced here are the CRO, the head of risk reporting, the board secretary, the disclosure committee chair (with securities counsel), and the audit committee chair, depending on the artifact. Public regulatory and standards sources are anchors, not legal interpretations.

## Source posture

Public anchors only. The substantive set:

- BCBS 239, Principles for Effective Risk Data Aggregation and Risk Reporting (January 2013), and the BCBS Progress Reports (2017, 2020, 2023, and the most recent thematic review).
- COSO ERM 2017 (Enterprise Risk Management: Integrating with Strategy and Performance).
- OCC Heightened Standards, 12 CFR Part 30 Appendix D (large-bank risk-governance framework).
- FRB SR 12-17, Consolidated Supervision Framework for Large Financial Institutions (December 2012).
- FRB SR 13-13, Supervisory Considerations for the Communication of Supervisory Findings (June 2013), for the MRA / MRIA framework.
- SEC Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure final rule (Release Nos. 33-11216 / 34-97989, July 26, 2023): Form 8-K Item 1.05, Form 6-K cross-reference, Regulation S-K Item 106, Exchange Act Rule 13a-15.
- SEC Climate Disclosure Rule (Release Nos. 33-11275 / 34-99678, final March 2024). Current effectiveness is unsettled (the rule has been subject to legal challenges and was voluntarily stayed by the SEC pending judicial review). Phase 2 SKILL.md text must verify SEC posture as of the report date and use TCFD (Final Report June 2017; Implementing 2021) for substantive content where the SEC rule is not currently effective.
- Federal banking agencies' Computer-Security Incident Notification Rule (12 CFR 53 / 225 / 304, effective May 1, 2022): the 36-hour notification clock that runs alongside the SEC Item 1.05 4-business-day clock for covered banking organizations.
- NYDFS 23 NYCRR 500 (Part 500), §500.17, post-November-2023 amendments.
- SEC Reg S-P amendments (final May 16, 2024), customer-information incident notification.
- ECB Guide on effective risk data aggregation and risk reporting (May 2024 final), for SSM-supervised firms.
- AICPA SSAE 18 (AT-C 320 for SOC 1; AT-C 105 / 205 for SOC 2), PCAOB AS 2201, and SOX Sections 302 / 404 sub-certification structures, for the attestation-pack source set.
- IIA International Standards for the Professional Practice of Internal Auditing (Standard 2500 series), for management-response and attestation-pack framing.
- TCFD Recommendations (Final Report June 2017; Implementing 2021), and NGFS reference scenarios, for climate reporting where the SEC rule is not currently relied on.

## Components

- `skills/` — the six skills above, each with a `SKILL.md` and a `templates/default-output.md`. Phase 2 adds per-skill `references/`, `examples/`, and (where applicable) `scripts/`.
- `references/` — plugin-level shared references: public-source map, policy and control library, review gates and confidence labels.
- `schemas/` — structured-output templates. `risk-report.schema.json` is canonical to this plugin (extended in phase 2 with `risk_type`, `breach_age_days`, and `bcbs239_principle_refs`). New schemas added in phase 2: `bcbs239-assessment.schema.json`, `attestation-pack.schema.json`, `cyber-incident-disclosure.schema.json`, `item-106-disclosure.schema.json`, `dcp-readiness.schema.json`, `management-response.schema.json`. Schemas borrowed from other plugins (`ai-use-case`, `control`, `issue`, `obligation`, `test-plan`, `vendor`) live here for v1 and move to their owning plugins in phase 3.

## Install

```bash
/plugin install risk-reporting@second-line-financial-services
```

## Disclaimer

This plugin produces draft second-line risk-reporting artifacts for qualified review. It does not provide legal advice, regulatory interpretation, or filing decisions. Materiality determinations, 8-K and 10-K disclosure decisions, attestations, and responses to supervisory findings remain the responsibility of the firm's named officers and counsel. Public regulatory and standards sources cited here are anchors, not legal interpretations, and several of the rules referenced (notably the SEC Climate Disclosure Rule) are subject to ongoing litigation or staff guidance evolution; verify current effectiveness as of the report date.
