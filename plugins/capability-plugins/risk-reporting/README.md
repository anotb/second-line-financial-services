# Risk Reporting

CRO-function risk reporting. The artifacts here are the load-bearing outputs of the second-line risk-reporting machine: the enterprise risk committee pack, the BCBS 239 self-assessment, KRI / KCI commentary, SEC cyber-disclosure readiness, management attestation packs, and management responses to MRA / MRIA and audit findings.

This is the broader 1.5 / 2-line risk-reporting function, not compliance reporting. Compliance reporting (the obligations-to-controls-to-evidence chain) lives in `risk-compliance-core` and `compliance-testing`. Risk reporting subsumes compliance reporting at the committee-pack level but reaches across credit, market, liquidity, operational, compliance, financial crime, model, third-party, cyber, and (where applicable) climate.

Audience: Chief Risk Officer office, head of risk reporting, head of operational-risk reporting, head of capital and liquidity risk reporting, board secretary teams, the disclosure committee, and the advisory teams supporting these functions.

## Skills

| Skill | What it produces |
|---|---|
| `risk-committee-pack` | Enterprise risk committee pack: heat map, top risks, material risk events, KRI movement and breaches, RAS status, issues and remediation, forward-looking commentary, decision items. |
| `bcbs239-gap-assessment` | BCBS 239 self-assessment against the fourteen principles, organised by overarching governance, aggregation, reporting, and supervisory review. |
| `kri-commentary` | Per-KRI / KCI commentary block: root cause, contributing factors, action taken, action planned, residual-risk view, second-line challenge note. |
| `cyber-disclosure-readiness` | SEC cyber-disclosure readiness: 8-K Item 1.05 trigger and materiality workpaper, 10-K Item 106 disclosure draft, disclosure-controls (DCP) readiness map. |
| `attestation-pack` | Management attestation pack: scope, control inventory, evidence index, exceptions, compensating controls, prior-period remediation, assertion language, sign-off. |
| `management-response` | Management response to a regulator MRA / MRIA, audit finding, or external assessor finding: acceptance posture, root cause, action plan with milestones, evidence-of-effectiveness plan, reporting cadence. |

## How this chains

`risk-committee-pack` aggregates upstream artifacts from across the repo: KRI commentary from `kri-commentary`, issue write-ups from `risk-compliance-core/issue-writeup`, AI risk roll-up from `ai-governance-model-risk/board-ai-risk-pack`, third-party risk roll-up from `third-party-operational-resilience/concentration-risk-review`, financial-crime themes from `financial-crime-governance`. `cyber-disclosure-readiness` and `attestation-pack` are public-company / large-bank artifacts that intersect with `compliance-testing` evidence pulls and the firm's disclosure-committee process. `management-response` is the formal response-side companion to issue write-ups produced anywhere in the repo.

## Source posture

Public anchors only. Substantive base:

- BCBS 239, Principles for Effective Risk Data Aggregation and Risk Reporting (January 2013), and the BCBS Progress Reports (2017, 2020, 2023, and the most recent thematic review).
- COSO ERM 2017.
- OCC Heightened Standards, 12 CFR Part 30 Appendix D (large-bank risk-governance framework).
- FRB SR 12-17, Consolidated Supervision Framework for Large Financial Institutions (December 2012).
- FRB SR 13-13, Supervisory Considerations for the Communication of Supervisory Findings (June 2013), for the MRA / MRIA framework.
- SEC Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure final rule (Release Nos. 33-11216 / 34-97989, July 26 2023): Form 8-K Item 1.05, Form 6-K cross-reference, Regulation S-K Item 106, Exchange Act Rule 13a-15.
- SEC Climate Disclosure Rule (Release Nos. 33-11275 / 34-99678, final March 2024). Verify current effectiveness as of report date; the rule has been subject to legal challenges and was voluntarily stayed pending judicial review. Use TCFD (Final Report June 2017; Implementing 2021) for substantive content where the SEC rule is not currently effective.
- Federal banking agencies' Computer-Security Incident Notification Rule (12 CFR 53 / 225 / 304, effective May 1 2022): the 36-hour notification clock that runs alongside the SEC Item 1.05 4-business-day clock for covered banking organizations.
- NYDFS 23 NYCRR 500 (Part 500), §500.17, post-November 2023 amendments.
- SEC Reg S-P amendments (final May 16 2024), customer-information incident notification.
- ECB Guide on effective risk data aggregation and risk reporting (May 2024 final), for SSM-supervised firms.
- AICPA SSAE 18 (AT-C 320 for SOC 1; AT-C 105 / 205 for SOC 2), PCAOB AS 2201, and SOX §302 / §404 sub-certification structures, for the attestation-pack source set.
- IIA International Standards (Standard 2500 series), for management-response and attestation-pack framing.
- TCFD Recommendations (Final Report June 2017; Implementing 2021), and NGFS reference scenarios, for climate reporting where the SEC rule is not relied on.

Several rules referenced (notably the SEC Climate Disclosure Rule) are subject to ongoing litigation or staff guidance evolution. Skills must verify current effectiveness as of the report date.

## Sector overlays

All four sectors apply. Banking overlay carries Heightened Standards integration, BHC SR 12-17 cycle, and Call Report / UBPR pointers. Insurance overlay carries ORSA Summary Report mapping (NAIC Model #505) and CGAD support. Capital-markets overlay carries §38a-1 fund-board reporting and SEC adviser annual-review cadence. Payments / fintech overlay carries sponsor-bank reporting expectations, NACHA risk reporting, and the CFPB larger-participant supervision posture.

## Components

- `skills/` — the six skills above. Each ships its own `SKILL.md`, `references/source-anchors.md`, sector overlays, `templates/default-output.md`, and (where useful) `schemas/` and `examples/`.
- `references/` — plugin-level shared references: source map, policy and control library, named decision forums and confidence labels.
- `schemas/` — `risk-report.schema.json` (canonical), `bcbs239-assessment.schema.json`, `attestation-pack.schema.json`, `cyber-incident-disclosure.schema.json`, `item-106-disclosure.schema.json`, `dcp-readiness.schema.json`, `management-response.schema.json`. Schema dedup (drop schemas a plugin's skills don't actually use) is tracked in [ROADMAP.md](../../../ROADMAP.md).

## Install

```bash
claude plugin install risk-reporting@second-line-financial-services
```

## Operating posture

Drafts second-line risk-reporting artifacts for qualified review. Does not provide legal advice, regulatory interpretation, or filing decisions. Materiality determinations, 8-K and 10-K disclosure decisions, attestations, and responses to supervisory findings remain the responsibility of the firm's named officers and counsel. Public regulatory and standards sources cited here are anchors, not legal interpretations.
