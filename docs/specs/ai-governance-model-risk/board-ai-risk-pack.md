# board-ai-risk-pack — Phase 1 spec sheet

Date: 2026-05-06
Plugin: ai-governance-model-risk
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Drafts the AI risk pack for the AI risk committee or the AI section of the board risk committee. Distils inventory state, tier mix, in-flight reviews, key decisions, incident posture, regulator and exam interactions, and the small number of items that need the committee's attention. Designed for a senior, time-constrained audience that wants the call-outs, not the catalogue.

Best for:
- A scheduled AI risk committee meeting needs its pre-read prepared from current second-line records.
- A board education session is needed on AI governance posture, with a curated narrative on tier mix, top risks, and key decisions.
- A regulator pre-meet needs a one-pack summary on AI governance posture for an exam request or supervisory letter response.

Not the right tool when:
- The audience is the enterprise risk committee for the firm at large (use risk-committee-pack in risk-reporting; the two are different audiences with overlapping inputs).
- The artifact required is the full AI inventory dump (this skill summarises; it does not list).
- The pack needs detailed vendor or third-party narrative (use the third-party-operational-resilience pack outputs as inputs to this pack).

Anchored to: SR 11-7 §II (board and senior management responsibilities) and §III (governance); OCC Bulletin 2026-13 (revised interagency model risk management guidance, 2026) [verify section on board oversight]; NIST AI RMF 1.0 Govern 1.x (organisational governance) and Govern 4.x (accountability); ISO/IEC 42001:2023 §5.1 (leadership and commitment) and §9.3 (management review); EU AI Act Article 26 (deployer obligations including monitoring and logs) [where applicable].

## Source anchors

- SR 11-7 §II — board and senior management responsibilities for model risk.
- SR 11-7 §III — governance, policies, and controls.
- OCC Bulletin 2026-13 (revised interagency model risk guidance, 2026) [verify section] — refreshed governance and oversight expectations including AI/ML and GenAI inclusion.
- FDIC FIL on revised interagency model risk management guidance, 2026 [verify section] — parallel governance expectations.
- NIST AI RMF 1.0 Govern 1.1 to 1.7 (governance establishment), Govern 4.1 to 4.3 (accountability), Govern 6.1 (third-party considerations).
- ISO/IEC 42001:2023 §5.1 (leadership and commitment), §6.2 (AI objectives), §9.3 (management review).
- EU AI Act Article 26 (deployer obligations), Article 71 (registration) — informational where the firm has EU-deployer exposure.
- NYDFS Industry Letter on Cybersecurity Risks Arising from AI (October 2024) — board-level cyber-AI exposure framing.
- BCBS 239 (informational) — risk data aggregation principles applicable when AI inventory data feeds the pack.

## Sector overlays needed

- `references/sector-overlays/banking.md` — board-pack framing for banking holding-company committees, alignment with CCAR governance reporting cadence.
- `references/sector-overlays/insurance.md` — alignment with own risk and solvency assessment (ORSA) governance cadence; NAIC Model Bulletin governance framing.
- `references/sector-overlays/capital-markets.md` — alignment with broker-dealer / investment adviser risk committee cadence; surveillance and execution AI framing.
- `references/sector-overlays/payments-fintech.md` — alignment with sponsor-bank governance reporting and program-management committees.

## Cross-cutting overlays

- `references/cross-cutting/cyber.md` — board-level AI cyber posture; NYDFS October 2024 letter alignment; named incident classes.
- `references/cross-cutting/conduct.md` — customer-facing AI exposure summary, complaint trend, fairness call-outs.

Privacy and climate not core to the pack. Privacy lands in the cyber overlay where it touches; climate not applicable.

## Output template named sections

1. Executive summary (five bullets maximum, the call-outs)
2. AI inventory state (count by tier, by sector, by deployment status; period-over-period change)
3. Top risks (a short, opinionated list with named owners and current trajectory)
4. In-flight reviews and decisions (what is in front of the committee this session)
5. Incidents and near-misses (a curated list, not the catalogue; with regulator-notification status)
6. Regulator and exam interactions (open MRA/MRIA, supervisory letters, exam findings on AI scope)
7. Vendor and third-party AI exposure (key vendors, foundation model dependence, concentration)
8. Policy and framework changes (since last meeting; with effective dates)
9. Forward look (what is on the runway for the next two cycles)
10. Decisions requested (specific, with options and recommended motion)
11. Appendix: source trace and definitions

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `pack_id` | string | Canonical pack ID (committee, date). |
| `committee` | string | Named committee. |
| `meeting_date` | string | ISO date. |
| `executive_summary` | array of strings | Up to five bullets. |
| `inventory_state` | object | Sub-fields: total_use_cases, by_tier, by_sector, change_since_last. |
| `top_risks` | array of objects | Each: risk, owner, trajectory, target action. |
| `in_flight_reviews` | array of objects | Each: use_case, stage, decision_due_date, recommendation. |
| `incidents` | array of objects | Each: incident_id, classification, regulator_notification_status, owner, status. |
| `regulator_interactions` | array of objects | Each: regulator, item (MRA/MRIA/letter/exam), status, owner, target close. |
| `vendor_exposure` | object | Sub-fields: top_vendors, foundation_model_concentration, key_dependencies. |
| `policy_changes` | array of objects | Each: change, effective_date, owner. |
| `forward_look` | array of strings | Items on the runway for the next two cycles. |
| `decisions_requested` | array of objects | Each: question, options, recommended_motion, owner. |
| `source_trace` | array of objects | Claim, source, evidence reference, confidence. |

## Example scenarios (public-source-derived, anonymous)

1. Quarterly AI risk committee at a US national bank. Pack distils: 47 in-production AI use cases, tier-1 count up by two, two newly tiered consumer-decisioning models in flight, one incident (a vendor foundation-model version swap caused a refusal-rate spike on the relationship-manager assistant; resolved, no customer impact, near-miss logged), open MRA on AI inventory completeness, recommended decision is approval of revised AI policy that adds GenAI-specific control expectations.

2. Annual board education session at a regional life insurer. Pack distils: AI inventory state (12 use cases, mostly pricing and underwriting decisioning), top risks (state insurance fairness exposure, NAIC Model Bulletin alignment, foundation model vendor concentration in the claims summarisation pilot), regulator interactions (state department information request on use of AI in underwriting acceleration, response in progress), forward look (claims summarisation pilot expected to seek production approval in two quarters), decisions requested (board endorsement of the AI governance framework as updated for the NAIC Model Bulletin alignment).

## Common pitfalls

1. Pack becomes a catalogue dump. Committee reads page nine instead of page one. Mitigation: executive summary is required, capped at five bullets, and the rest of the pack is curated, not exhaustive.
2. Top risks are stable across packs because no one wants to retire a risk. Trajectory becomes meaningless. Mitigation: trajectory field with explicit `improving` / `stable` / `worsening` / `new` enum, with one-line basis.
3. Incidents are presented as resolved with no near-miss reporting. The committee gets a false sense of security. Mitigation: near-miss section is required; if empty, state explicitly that no near-misses were logged this period.
4. Vendor concentration is buried. The committee does not see that 80% of GenAI use cases depend on one foundation-model provider until something happens. Mitigation: foundation-model concentration is a required field, with named providers and use-case counts.
5. Decisions requested are vague ("note the report"). Committee meeting closes with no decisions taken. Mitigation: decisions-requested entries must have options and a recommended motion; "note the report" is not a decision.
