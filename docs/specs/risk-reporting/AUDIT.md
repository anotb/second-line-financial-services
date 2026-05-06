# risk-reporting — Phase 1 audit memo

Date: 2026-05-06
Phase: 1 (per-plugin scoping)
Plan: `docs/plans/2026-05-06-rationalized-plugin-map.md`

## Plugin role

CRO-function risk reporting. The artifacts here are the load-bearing outputs of the second-line risk-reporting machine: the enterprise risk committee pack, the BCBS 239 self-assessment, KRI / KCI commentary blocks, SEC cyber disclosure readiness, management attestation packs, and management responses to regulator and audit findings. Audience: Chief Risk Officer office, head of risk reporting, head of operational-risk reporting, head of capital and liquidity risk reporting, board secretary teams, disclosure committee, and securities counsel as a downstream reviewer.

This is a risk-reporting plugin, not a compliance-reporting plugin. Compliance reporting (the obligations-to-controls-to-evidence chain) is `risk-compliance-core` and `compliance-testing`. Risk reporting is the wider 1.5 / 2-line function that aggregates across credit, market, liquidity, operational, compliance, financial-crime, model, third-party, cyber, and (where applicable) climate, then produces the named artifacts the committee, the regulator, and the auditor expect.

## v1 skill list (confirmed)

Six skills, all carried from v0.2:

1. `attestation-pack`
2. `bcbs239-gap-assessment`
3. `cyber-disclosure-readiness`
4. `kri-commentary`
5. `management-response`
6. `risk-committee-pack`

No deletions. No renames. No additions.

## Changes vs v0.2

- No skill changes inside this plugin.
- `cyber-disclosure-readiness` gains explicit cross-cutting overlay refs to both `cyber.md` (required, core anchor set) and `climate.md` (required, because the same disclosure machinery — DCP, materiality, 8-K Item 1.05 mechanic, 10-K Item 106 / Item 1500-series — handles cyber and climate material-event triggers).
- `risk-committee-pack` gains the climate cross-cutting overlay as required (heat-map placement of physical and transition risk, scenario commentary, and the link to the 10-K climate disclosure section); cyber overlay is optional (depth lives in `cyber-disclosure-readiness`).
- `attestation-pack` and `management-response` carry the cyber overlay as optional but frequently invoked (cyber-control attestations and cyber MRA / MRIA responses are common).
- All six SKILL.md files are currently boilerplate. Phase 2 rewrites content per the spec sheets in this folder.
- The current `description` frontmatter is the same long URL-list shape as the other capability plugins. Phase 2 replaces with the activation-tuned `Best for` / `Not the right tool when` / `Anchored to` shape.

## Cross-cutting overlays planned per skill

| Skill | cyber | climate | privacy | conduct |
| --- | --- | --- | --- | --- |
| `attestation-pack` | optional | not required | optional | optional |
| `bcbs239-gap-assessment` | optional | optional | not required | not required |
| `cyber-disclosure-readiness` | required (core) | required | optional | not required |
| `kri-commentary` | optional | optional | optional | optional |
| `management-response` | optional | not required | optional | optional |
| `risk-committee-pack` | optional | required | not required | not required |

The pattern: cyber and climate are the two cross-cutting overlays that earn their keep in this plugin. Privacy and conduct surface only in narrow cases (privacy-control attestations, consumer-conduct findings) and live as optional overlays when they apply.

## Plugin-level shared references plan

Stays plugin-level (reused by every skill or many skills):

- `references/source-map.md` — public-source map for the plugin. Today it is a near-duplicate of `common/references/source-map.md`. Phase 2 prunes to the rows actually used by the six skills and adds the SEC cyber disclosure final rule (Release Nos. 33-11216 / 34-97989), Reg S-K Item 106, federal banking agencies' Computer-Security Incident Notification Rule (12 CFR 53/225/304), NYDFS Part 500 §500.17 (post-November-2023 amendments), SEC Reg S-P amendments (May 2024), and the SEC Climate Disclosure Rule (Release Nos. 33-11275 / 34-99678) with the current-effectiveness caveat front-and-centre.
- `references/policy-control-library.md` — baseline risk taxonomy and committee-pack control pattern. Used by `risk-committee-pack`, `bcbs239-gap-assessment`, `attestation-pack`. Keep here; extend with the BCBS 239 fourteen-principle structure and the SR 12-17 / 12 CFR Part 30 Appendix D risk-governance-framework taxonomy.
- `references/review-gates.md` — named review gates and confidence labels. Plugin-wide. The disclosure-committee gate is the load-bearing gate for `cyber-disclosure-readiness`; the audit-committee gate is load-bearing for `management-response`; the risk-committee gate is load-bearing for `risk-committee-pack`. Keep here.

Moves per-skill in phase 2:

- `references/output-templates.md` — currently houses generic templates not matched to any of these six artifact shapes. Phase 2 moves artifact-specific templates into each skill's `templates/default-output.md`. The plugin-level file is removed.
- `references/public-regulatory-scenarios.md` — repo-level index, not plugin-level. Move to `common/references/` or `docs/` in phase 3 alongside the same move for the other capability plugins.

Phase 2 will add per-skill `references/source-anchors.md` for every skill, plus `references/cross-cutting/<cyber|climate>.md` per the per-skill table above.

## Schema ownership

Owned by this plugin (canonical home):

- `risk-report.schema.json` — used by `risk-committee-pack` and extended by `kri-commentary`. Currently sits in `risk-compliance-core/schemas/` as a borrowed schema. Phase 3 moves it here. Phase 2 extends it with `risk_type` (enum), `breach_age_days` (integer), and `bcbs239_principle_refs` (array) per the `risk-committee-pack` and `kri-commentary` spec sheets.

New schemas needed in phase 2 (additions, all owned here):

- `bcbs239-assessment.schema.json` — wrapper plus per-principle objects for the fourteen-principle assessment, per the `bcbs239-gap-assessment` spec.
- `attestation-pack.schema.json` — wrapper for attestation-pack output; reuses `control.schema.json` and `issue.schema.json` from `risk-compliance-core`. Per the `attestation-pack` spec.
- `cyber-incident-disclosure.schema.json` — Artifact A of `cyber-disclosure-readiness` (8-K Item 1.05 trigger and disclosure decision pack).
- `item-106-disclosure.schema.json` — Artifact B of `cyber-disclosure-readiness` (10-K Item 106 disclosure pack).
- `dcp-readiness.schema.json` — Artifact C of `cyber-disclosure-readiness` (disclosure controls and procedures readiness map).
- `management-response.schema.json` — wrapper for management-response output; reuses `issue.schema.json` from `risk-compliance-core`.

Borrowed today, scheduled for phase 3 removal:

- `ai-use-case.schema.json`, `control.schema.json`, `issue.schema.json`, `obligation.schema.json`, `test-plan.schema.json`, `vendor.schema.json` — these belong to `ai-governance-model-risk`, `risk-compliance-core`, `risk-compliance-core`, `risk-compliance-core`, `compliance-testing`, and `third-party-operational-resilience` respectively. Keep here meanwhile to avoid dangling references; remove in phase 3 once the canonical homes are settled and import paths are updated.

## Current-state caveats

The substantive risk in this plugin is regulatory-fact freshness. Several of the source anchors are in active flux as of the report date and phase 2 SKILL.md text must not assert current effectiveness without verification.

- **SEC Climate Disclosure Rule (Release Nos. 33-11275, 34-99678)** — finalized March 2024. Subject to multiple legal challenges in federal courts and was voluntarily stayed by the SEC pending judicial review. Current effectiveness is unsettled. Phase 2 default posture: cite the rule with `[verify current effectiveness]`, lean on TCFD (Final Report June 2017; Implementing 2021) for substantive content, and route any committee-pack or 10-K climate-section claim through a current-status check at SKILL.md write time. The `risk-committee-pack` and `cyber-disclosure-readiness` spec sheets carry this caveat and phase 2 must not strip it.
- **SEC cyber disclosure final rule (Release Nos. 33-11216, 34-97989; July 26, 2023)** — effective dates phased: 8-K Item 1.05 effective December 18, 2023 for non-smaller-reporting-companies and June 15, 2024 for SRCs; Item 106 effective for fiscal-year filings ending on or after December 15, 2023 (large filers) with phased applicability for SRCs. The rule itself is in force; phase 2 must verify the SRC phase-in dates and any post-adoption staff guidance (CD&Is) at SKILL.md write time.
- **SEC Reg S-P amendments (final May 16, 2024)** — customer-information incident notification, 30-day clock for individuals reasonably likely to have been affected, with phased compliance dates. Phase 2 must verify the compliance dates applicable to the firm size and registrant type at SKILL.md write time. Affects `cyber-disclosure-readiness` parallel-clocks table for SEC-registered broker-dealers, investment advisers, and funds.
- **Federal banking agencies' Computer-Security Incident Notification Rule (12 CFR 53 / 225 / 304)** — effective May 1, 2022, with the 36-hour notification clock running from determination of a notification incident. Stable as a rule but phase 2 must verify the OCC / FRB / FDIC implementing guidance current as of SKILL.md write date.
- **NYDFS 23 NYCRR 500 (Part 500)** — November 2023 amendments effective with phased compliance through November 2025; §500.17 cybersecurity-event notification clock and §500.17(b) annual CISO certification (Form B) revised by the amendments. Phase 2 must verify section labels post-amendment.
- **BCBS 239 supervisory expectations evolution** — the principles themselves date from January 2013 and are stable. The supervisory expectations are not. BCBS Progress Reports (2017, 2020, 2023, and any subsequent thematic review) document persistent gaps, especially on Principles 2 (architecture), 3 (accuracy), and 6 (adaptability). The ECB Guide on effective risk data aggregation and risk reporting (May 2024 final) raises the SSM bar incrementally. Phase 2 must (a) verify the most recent BCBS thematic review at SKILL.md write time and (b) keep the ECB Guide's incremental expectations distinguished from the BCBS 239 baseline so the assessment reads cleanly from either supervisor's lens.
- **OCC Heightened Standards 12 CFR Part 30 Appendix D** — section labels (II Risk Governance Framework, III Risk Appetite Statement, IV Roles and Responsibilities of the Board) are referenced across `risk-committee-pack`, `bcbs239-gap-assessment`, `attestation-pack`, and `kri-commentary`. The spec sheets carry `[verify section]` placeholders consistently; phase 2 must resolve those to pin cites.
- **FRB SR 13-13 (MRA / MRIA framework, June 2013)** — referenced by `management-response`. Stable but phase 2 must verify the OCC PPM 5310-3 successor number and the FDIC Risk Management Manual section labels at write time.
- **Dodd-Frank Section 165(b) risk committee threshold** — amended by EGRRCPA 2018; phase 2 must verify the current threshold and the FRB tailoring framework's interaction at SKILL.md write time. Affects `risk-committee-pack` charter scope framing.
- **TSC Industries v. Northway materiality standard** — used by `cyber-disclosure-readiness`. Pin cites flagged `[verify]` in the spec sheet; phase 2 must resolve.

## Source-anchor confidence per skill

| Skill | Confidence | Notes |
| --- | --- | --- |
| `attestation-pack` | Solid | COSO 2013, SOX 302/404, SSAE 18, BCBS 239 Principle 1 land directly. PCAOB AS 2201 pin cites flagged `[verify]`. OCC Heightened Standards section labels flagged `[verify]`. The interagency third-party guidance (June 2023) lands directly. |
| `bcbs239-gap-assessment` | Solid | The fourteen principles are stable and direct. BCBS Progress Reports are dated and verifiable. ECB Guide May 2024 land directly with a `[verify version]` flag. FRB SR 12-17 lands directly. OCC Heightened Standards section labels flagged `[verify]`. |
| `cyber-disclosure-readiness` | Watch | SEC final rule lands directly with cited release numbers. Item 1.05 mechanic and Item 106 subitems are stable. The climate-rule overlay must carry `[verify current effectiveness]`. NYDFS Part 500 §500.17 must be verified post-November-2023 amendments. Reg S-P May 2024 amendments must be verified for compliance dates. Federal banking agencies' notification rule (12 CFR 53/225/304) stable. TSC / Basic pin cites flagged `[verify]`. |
| `kri-commentary` | Solid | BCBS 239 Principles 7 to 11 are direct. COSO ERM 2017 lands directly. OCC Heightened Standards §III flagged `[verify section]`. Basel revised principles for sound management of operational risk (March 2021) flagged `[verify date]`. FRB SR 95-51 flagged `[verify current applicability]`. |
| `management-response` | Watch | FRB SR 13-13 lands directly. OCC PPM 5310-3 number flagged `[verify]`. FDIC Risk Management Manual section labels flagged `[verify]`. IIA Standard 2500 / 2500.A1 lands directly. PCAOB AS 2201 pin cites flagged `[verify]`. NYDFS supervisory communications are not a single named source; phase 2 must keep this framed as supervisory practice. |
| `risk-committee-pack` | Watch | BCBS 239 Principles 7 to 11 direct. COSO ERM 2017 direct. OCC Heightened Standards section labels flagged `[verify]`. Dodd-Frank §165(b) threshold flagged `[verify post-EGRRCPA]`. SEC Climate Rule must carry `[verify current effectiveness]`. TCFD 2017 + 2021 stable as voluntary anchor. NGFS scenarios stable as reference. |

Phase 2 must hold the bar on the `Watch` rows. The credibility of the artifacts produced by this plugin depends on accurate regulator citation; over-claiming current effectiveness on the SEC climate rule, or rolling forward stale Item 106 disclosure language, is the failure mode this audit memo is trying to prevent.

## Phase 2 readiness

All six skills have spec sheets in this folder:

- `attestation-pack.md`
- `bcbs239-gap-assessment.md`
- `cyber-disclosure-readiness.md`
- `kri-commentary.md`
- `management-response.md`
- `risk-committee-pack.md`

Each spec sheet contains the activation-tuned description, source anchors with section refs (or `[verify section]` placeholders), sector and cross-cutting overlay decisions, output template named sections, structured output fields, two example scenarios, and common pitfalls. Phase 2 subagents take the spec sheet as their contract and must respect the current-state caveats above.
