# complaint-theme-analysis — Phase 1 spec sheet

Date: 2026-05-06
Plugin: consumer-compliance-fair-lending
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Aggregates and themes a population of consumer complaints (CFPB Complaint Database extracts, internal complaint system extracts, social listening, AG referrals) into named themes with severity, root-cause hypotheses, regulatory exposure, and trended movements. Produces a second-line memo for the complaint management committee, UDAAP review, and fair-lending escalation. Themes — not individual complaints — are the unit of analysis.

Best for:
- Quarterly or monthly complaint themes pack for the consumer compliance committee or risk committee.
- Pre-exam preparation: re-running the firm's last 12-24 months of CFPB Complaint Database public data against current product set to triangulate examiner focus areas.
- Triage after a regulator inquiry on a specific product, to scope the population and trend.
- Input to udaap-risk-review or fair-lending-test-plan when a theme suggests a specific product or process is the issue.

Not the right tool when:
- The question is one specific complaint disposition (use the firm's complaint case management workflow).
- The question is whether a marketing claim is misleading (use marketing-claim-review).
- The question is statistical fair-lending testing on outcomes data (use fair-lending-test-plan).
- The question is the firm's CMS overall (use risk-compliance-core / compliance-testing).

Anchored to: CFPB Consumer Complaint Database (public data; field documentation); CFPB Compliance Management System Examination Procedures (current edition) — complaint management as a CMS pillar; CFPB Supervisory Highlights (latest two issues at time of review); UDAAP Dodd-Frank §1031 / §1036 — complaints as evidence of consumer harm; Joint Statement on Enforcement of Civil Rights, Fair Lending, Fair Housing, and Consumer Financial Protection Laws (April 2023) where complaints surface algorithmic discrimination patterns; Reg B 12 CFR 1002.9 (where complaints relate to adverse action); Reg Z 12 CFR 1026 (where complaints relate to APR / fee / disclosure).

## Source anchors

- CFPB Consumer Complaint Database — https://www.consumerfinance.gov/data-research/consumer-complaints/ ; field reference (product, sub-product, issue, sub-issue, company response, narrative consent flag, state, ZIP3, date received).
- CFPB Compliance Management System Examination Procedures (current edition) [verify edition date] — complaint management as a CMS pillar; expectations for root-cause analysis, trending, escalation, and board / committee reporting.
- CFPB Supervisory Highlights (most recent two issues at time of review) [verify issue numbers and dates] — themes the bureau is publicly focused on; mirror against firm themes.
- UDAAP authority: Dodd-Frank §1031 (12 U.S.C. §5531) and §1036 (12 U.S.C. §5536); CFPB UDAAP Examination Manual (current edition) — complaint patterns as one of the indicators of unfairness, deception, or abusiveness.
- Joint Statement (CFPB / DOJ / FTC / EEOC, April 25, 2023) — complaints as a surveillance vector for algorithmic discrimination.
- CFPB consent orders citing complaint volume and theme as part of the factual basis (used as worked-example anchors).
- State AG complaint portals — used selectively where the firm operates in those states.

## Sector overlays needed

- `references/sector-overlays/banking.md` — deposit account complaints (overdraft, returned items, pricing changes), credit-card complaints, mortgage servicing complaints, HELOC complaints; CRA complaint types.
- `references/sector-overlays/payments-fintech.md` — Reg E error resolution complaints, P2P fraud / scam complaints, BNPL complaints, sponsor bank vs. fintech complaint attribution, app-store reviews as a non-CFPB complaint channel.
- `references/sector-overlays/capital-markets.md` — retail brokerage complaints (FINRA Rule 4513 / 4530), customer complaint reporting; not CFPB-jurisdictional but the same theming method.
- `references/sector-overlays/insurance.md` — state DOI complaints, MGA complaint flow; non-CFPB but theme analysis pattern reusable. Flag scope boundary.

## Cross-cutting overlays

- `references/cross-cutting/conduct.md` — complaints as the canonical conduct-risk surveillance signal; FCA-style conduct framework parallel; complaint themes as input to root-cause analysis on culture, incentives, and product-design issues. Conduct risk taxonomy mapping.
- (AI-related cross-cutting is implicit where complaints reference algorithmic decisions, AI agents, AI-generated communications. SKILL.md should reference Joint Statement April 2023 where themes touch algorithmic decision-making.)

Privacy not applicable as a primary overlay. Cyber not applicable as a primary overlay. Climate not applicable.

## Output template named sections

1. Scope and population
2. Theming method (taxonomy used, reproducibility, BISG / geographic enrichment if applied)
3. Top themes (named, with theme definition, count, share, trend, comparable peer signal where public data permits)
4. Severity rubric and severity assigned per theme
5. Root-cause hypotheses (per theme)
6. Regulatory exposure mapping (per theme — UDAAP, Reg E, Reg Z, Reg B, FCRA, FHA, state-AG, CFPB Circulars)
7. Conduct-risk implications (per theme)
8. Trends and movements (period-over-period, with seasonality treatment)
9. Recommended actions (per theme — owner, due date, named control)
10. Open questions and dissent
11. Source trace and confidence label

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `analysis_id` | string | Unique reference. |
| `period` | object | Start, end, comparison period. |
| `population` | object | Source(s) used (CFPB public, internal, social, AG), count, scope filters. |
| `taxonomy_version` | string | Theme taxonomy reference, for reproducibility. |
| `themes[]` | array of objects | One per theme. |
| `themes[].theme_id` | string | Stable across periods. |
| `themes[].theme_label` | string | Human-readable. |
| `themes[].definition` | string | Theme inclusion criteria. |
| `themes[].count` | int | Period count. |
| `themes[].share` | float | Share of total complaints in period. |
| `themes[].trend` | enum | `up`, `down`, `flat`, `new`. |
| `themes[].severity` | enum | `low`, `medium`, `high`, `critical`. |
| `themes[].severity_rationale` | string | Per-theme reasoning. |
| `themes[].root_cause_hypotheses[]` | array of strings | Tested or untested. |
| `themes[].regulatory_exposure[]` | array of objects | Source, citation, exposure level. |
| `themes[].conduct_risk_flag` | bool | Whether theme is a conduct-risk signal. |
| `themes[].fair_lending_flag` | bool | Whether theme suggests protected-class disparity. |
| `themes[].ai_flag` | bool | Whether theme touches algorithmic decisioning / AI agents. |
| `themes[].demographic_skew` | object | State / ZIP3 / BISG-derived signals where present. |
| `themes[].recommended_actions[]` | array of objects | Action, owner, due date, named control. |
| `cross_references[]` | array of strings | Pointer to udaap-risk-review or fair-lending-test-plan when escalation is recommended. |
| `source_trace[]` | array of objects | Claim, source, evidence, confidence. |

## Example scenarios (public-source-derived, anonymous)

1. Quarterly review of a mid-size credit-card issuer's CFPB complaint volume. Top theme: "fees not disclosed at point of sale" (28% of period complaints, trend up from 19% prior quarter). Root-cause hypothesis: a December marketing campaign restructured the rewards-bonus offer with a small-print foreign-transaction fee disclosure that was below the fold on mobile. Regulatory exposure: UDAAP §1031 deception; potential Reg Z 12 CFR 1026.6(b) disclosure issue; theme echoes a recent CFPB Supervisory Highlights focus. Conduct risk flag set. Recommended actions: marketing review on disclosure prominence (cross-reference marketing-claim-review); operations review of cardholder agreement disclosure path; UDAAP risk re-rating (cross-reference udaap-risk-review); fee waiver decisioning consistency check.

2. A mortgage servicer's CFPB complaint extract over 12 months shows clustered "loss mitigation application repeatedly lost" complaints concentrated in three MSAs. Per-MSA share is 4-7x the firm's overall mortgage complaint share. State / ZIP3 / BISG enrichment shows two of those MSAs are majority-minority. Severity assigned `high`. Fair-lending flag set. Conduct flag set. Recommended actions: fair-lending escalation (cross-reference fair-lending-test-plan); loss-mit operations workflow control review; complaint-management committee root-cause memo. (Pattern derived from public CFPB consent orders on mortgage servicing loss mitigation themes.)

## Common pitfalls

1. Counting complaints by sub-issue without theming. Sub-issue is the CFPB taxonomy, not a root-cause taxonomy. Two distinct root causes can map to the same sub-issue. Mitigation: use a firm taxonomy and map back, document the mapping for reproducibility.
2. Reading narratives selectively. Confirmation bias drives theme inflation. Mitigation: theming method must be pre-registered in the analysis and applied to the entire sample, not just narratives the reviewer reads.
3. Treating CFPB public data as the firm's full complaint surface. It is not. Internal complaints, AG complaints, social, and app-store reviews are separate populations. Mitigation: scope and population field must enumerate every channel reviewed and explicitly state channels excluded.
4. Comparing volume without exposure adjustment. A doubling in complaints is meaningless if loan volume doubled. Mitigation: report rate (complaints per 1,000 customers / accounts / applications) alongside count where data permits.
5. BISG / geographic enrichment used to assert disparate impact. It is signal, not proof. Mitigation: feed BISG signal into fair-lending-test-plan for finding-grade analysis; flag here, do not finalize.
6. Trend comparison ignores product or marketing campaign launches. Apparent theme spikes are sometimes a launch-driven volume artifact. Mitigation: include product / campaign timeline in scope and call out timing relationships explicitly.
7. Skill produces a UDAAP determination or a fair-lending finding. It does not. Themes are surveillance output for human decision; escalations are recommended actions, not findings.

## Guardrail (mandatory in SKILL.md)

This skill does not approve loans, deny adverse-action notices, finalize UDAAP or fair-lending determinations, or take action on individual complaints. It themes a population of complaints, surfaces red flags, and recommends escalation paths for human decision by qualified compliance, fair-lending, conduct, legal, and product reviewers.
