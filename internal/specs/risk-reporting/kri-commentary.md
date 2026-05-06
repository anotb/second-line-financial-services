# kri-commentary — spec sheet

Plugin: `risk-reporting`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Drafts second-line commentary on KRI / KCI movement and breaches: root cause, contributing factors, action taken, action planned, owner, ETA, residual-risk view. Output is a per-KRI commentary block ready to drop into the risk committee pack, the divisional risk pack, or the regulator response after qualified review.

Best for:
- Producing the standing commentary block for each KRI / KCI flagged AMBER or RED in the period, with named root cause and remediation status.
- Refreshing commentary on a watch-list KRI that has been at trigger or limit for multiple consecutive periods.
- Rewriting first-line draft commentary to second-line standard (challenge, source-anchored, owner-named, evidence-pointed).
- Producing the commentary appendix for a regulator response or a board memo when a specific KRI is the subject of supervisory interest.

Not the right tool when:
- The artifact is the full committee pack (use `risk-committee-pack`; this skill produces the per-KRI blocks consumed there).
- The artifact is a one-off issue write-up where the KRI breach is the symptom (use `risk-compliance-core/skills/issue-writeup` for the issue; use this skill for the commentary on the KRI itself).
- The artifact is the data-quality root cause for the KRI (use `bcbs239-gap-assessment` if the breach is driven by upstream data lineage).
- The work is defining the KRI itself (KRI design and threshold setting is risk-appetite work, out of scope here).

Anchored to: BCBS 239 (January 2013) Principles 7-11 (risk reporting practices, especially Principle 9 clarity and usefulness, Principle 7 accuracy); COSO ERM (2017) Performance component, principles on risk-appetite reporting; OCC Heightened Standards 12 CFR Part 30 Appendix D §III (risk appetite statement) [verify section]; Basel Committee Principles for Sound Operational Risk Management (revised March 2021) [verify date] for KRI taxonomy in operational risk; FRB SR 95-51 (rating risk management) [verify current applicability] for the four-element framing.

## Source anchors

Primary:
- BCBS 239 — Principles 7 (accuracy), 8 (comprehensiveness), 9 (clarity and usefulness), 10 (frequency), 11 (distribution). Principle 9 is the centre of this skill: the commentary must be clear, useful, and actionable for the audience.
- COSO ERM 2017 — Performance component, with a focus on tracking performance against risk appetite and reporting deviations. Use for: framing the residual-risk view.
- OCC Heightened Standards 12 CFR Part 30 Appendix D, §III (Risk Appetite Statement) [verify section labels]. Use for: the linkage between KRI breach and RAS metrics, which the committee pack expects.
- Basel Committee on Banking Supervision, Revisions to the Principles for the Sound Management of Operational Risk (March 2021) [verify date]. Use for: KRI taxonomy in operational risk, which dominates committee-pack KRI populations at most banks.
- FRB SR 95-51, Rating the Adequacy of Risk Management Processes [verify current applicability]. Use for: the four-element risk-management framing (oversight, policies and limits, risk monitoring and MIS, internal controls) that the commentary should implicitly reflect.

Secondary (overlay only):
- IIA Three Lines Model (2020 revision). Use for: the second-line voice — challenge, not first-line restatement.
- Risk Appetite Framework guidance (FSB 2013, Principles for an Effective Risk Appetite Framework) [verify section]. Use for: framing the link between KRI breach commentary and the firm's RAS.

## Sector overlays needed

- `banking.md` — Covers OCC Heightened Standards expectations on RAS-anchored KRI commentary, FFIEC IT booklet KRI examples for cyber and operational risk, and CCAR / DFAST KRI commentary expectations during stress submissions.
- `insurance.md` — Covers ORSA KRI expectations (NAIC Model #505) [verify section] and state DOI conduct KRI commentary; ICP 16 (ERM for solvency purposes) [verify].
- `capital-markets.md` — Covers FINRA 3110 supervision KRI expectations (e.g., trade surveillance KRIs, customer-complaint KRIs) and SEC market-risk-rule KRI expectations for broker-dealers.
- `payments-fintech.md` — Covers OCC fintech bank-partnership KRI commentary expectations on third-party concentration and BaaS KRIs.

## Cross-cutting overlays needed

- `cyber.md` — Optional. Cyber KRIs (mean time to detect, mean time to respond, vulnerability ageing, phishing test results) are common in committee packs. The overlay covers when cyber KRI commentary needs to surface SEC Item 1.05 trigger considerations (a sustained KRI deterioration may be a leading indicator that should feed the disclosure-controls trace).
- `climate.md` — Optional. Where the firm reports climate KRIs (e.g., financed emissions, transition-risk-weighted exposures, physical-risk-weighted exposures), the overlay covers the data-quality caveat (vendor-supplied scenario data is often Principle 3 / Principle 6 vulnerable).
- `privacy.md` — Optional. Privacy KRIs (e.g., data-subject-access-request response times, breach-notification timeliness) appear in some committee packs.
- `conduct.md` — Optional. Conduct KRIs (complaint volume by theme, surveillance alerts by category) appear in CCRO / CCO packs.

## Output template named sections

The output is a per-KRI commentary block. The skill produces one or more blocks (typically the set of AMBER / RED / breached KRIs for the reporting period).

Per-KRI block:
- KRI identifier and name (e.g., `OPS-001 / Operational loss events > $1m`)
- Risk type and subtype (operational / sub: external fraud)
- Period and current value
- Threshold structure (limit, trigger, tolerance) and current status (within / at trigger / breach)
- Prior period value and direction
- RAG status (current and prior)
- Linked RAS metric (if any)
- Breach age (consecutive periods at trigger / breach)
- Root cause (named, evidence-pointed; not "TBD" or "investigation ongoing" for a multi-period breach)
- Contributing factors (data quality, control failures, external drivers, capacity, vendor)
- Action taken in period (what has already been done; named owner; date)
- Action planned (named action, named owner, target date, dependency)
- Residual-risk view (post-action expected RAG; rationale)
- Linked issues (foreign keys to `issue.schema.json`)
- Linked material events (foreign keys to `material_events` in `risk-committee-pack` wrapper)
- Source trace (evidence pointer for each material claim — system of record, report ID, sign-off log)
- Second-line challenge note (where second-line view diverges from first-line, surfaced explicitly)

Tail (across all blocks):
- Aggregate posture (count of RED, AMBER, breached; trend versus prior period)
- Cross-KRI correlations (where multiple KRIs share a root cause, surface it once)
- Confidence label (per block and aggregate)
- Reviewer questions

## Structured output fields

Schema: `schemas/risk-report.schema.json` (existing; extended in phase 2 per the `risk-committee-pack` spec) supplies the metric-level fields. This skill adds a commentary wrapper.

Per-block object (extends `risk-report.schema.json`):
- `metric` (existing): string. The KRI identifier and name.
- `threshold` (existing): string. Carries limit / trigger / tolerance structure.
- `current_value` (existing): string.
- `prior_value` (existing): string.
- `status` (existing): enum. `green` / `amber` / `red` / `not-rated`.
- `commentary` (existing): string. Becomes the structured root-cause + action paragraph.
- `owner` (existing): string. Role, not person.
- `action_required` (existing): string.

Phase 2 additions:
- `risk_type`: enum. Same values as `risk-committee-pack` heat_map.risk_type.
- `breach_age_periods`: integer. Number of consecutive reporting periods at trigger or breach.
- `linked_ras_metric_id`: string or null.
- `root_cause_named`: string. Replaces unstructured commentary; required for RED and multi-period AMBER.
- `contributing_factors`: array of enums. `data-quality` / `control-failure` / `external-driver` / `capacity` / `vendor` / `model-driver` / `other`.
- `action_taken`: array of objects with `action_description`, `owner`, `date_completed` (ISO date), `evidence_pointer`.
- `action_planned`: array of objects with `action_description`, `owner`, `target_date` (ISO date), `dependency_ids` (array).
- `residual_risk_view`: object with `expected_rag` (enum: green / amber / red), `rationale` (string).
- `linked_issue_ids`: array of strings.
- `linked_material_event_ids`: array of strings.
- `second_line_challenge_note`: string or null. Present when second-line view diverges from first-line.
- `bcbs239_principle_refs`: array of strings. Typically Principle 7 and Principle 9.
- `confidence_label`: enum. `high` / `medium` / `low` / `unknown`.
- `human_review_required`: boolean. Always true for v1.

Wrapper object (the set of blocks for a period):
- `period`: object. `start` (ISO date), `end` (ISO date).
- `blocks`: array of per-block objects.
- `aggregate_red_count`: integer.
- `aggregate_amber_count`: integer.
- `aggregate_breach_count`: integer.
- `cross_kri_correlations`: array of objects with `correlation_id`, `description`, `kri_metric_ids` (array).
- `aggregate_confidence_label`: enum.

## Example scenarios

### Scenario 1: RED KRI commentary on operational-loss events for the quarterly committee pack

Input: a bank's `OPS-001 / Operational loss events > $1m` KRI is RED for the second consecutive quarter. Prior quarter was AMBER. The KRI is breach (current value $14.8m gross loss, limit $10m). Source posture: BCBS 239 Principles 7 and 9, BCBS revised principles for sound management of operational risk (March 2021) [verify date], the firm's RAS, and the firm's operational risk taxonomy. The first-line ORM team has produced a draft commentary attributing the breach to "elevated external fraud activity"; second-line is rewriting.

Output emphasizes:
- Root cause (named): three discrete loss events drove $11.2m of the $14.8m: (i) account-takeover fraud on the digital channel (single event, $6.4m, May); (ii) check-kiting ring (single event, $3.1m, June); (iii) wire-fraud impersonation on a corporate-banking customer (single event, $1.7m, June).
- Contributing factors: `control-failure` (digital-channel step-up authentication was not triggered for two of the account-takeover sub-events), `external-driver` (industry-wide uptick in check-kiting reported by the Financial Crimes Enforcement Network), `vendor` (the third-party fraud-screening service had a 14-hour outage during the wire-fraud event window — see Material Event ME-2025-Q2-003).
- Action taken: digital-channel step-up authentication policy revised and deployed (Owner: CISO; Completed: July 11). Wire-fraud impersonation control retraining for corporate-banking RMs (Owner: Head of Corporate Banking; Completed: July 22).
- Action planned: review of the third-party fraud-screening service exit plan and dual-vendor architecture (Owner: Head of Vendor Management; Target: end of Q3); update of the operational-risk RAS metric on external-fraud loss tolerance (Owner: CRO; Target: presentation at the next Risk Committee).
- Residual-risk view: expected RAG next quarter is AMBER (not GREEN — three months is insufficient to establish trend; check-kiting external driver persists).
- Linked issues: ISS-2025-0712 (digital-channel control-design issue); ISS-2025-0723 (vendor outage issue).
- Linked material event: ME-2025-Q2-003.
- Second-line challenge note: first-line attribution of "elevated external fraud activity" understates the control-failure component (specifically the digital-channel step-up authentication gap). Second-line view is that the breach is materially driven by control failure, not external environment.
- BCBS 239 principle references: Principle 7 (accuracy of the loss attribution), Principle 9 (clarity and usefulness — the prior commentary was not actionable).
- Confidence label: high. The loss-event evidence is well-documented; the control-failure root cause is supported by the post-event review.

### Scenario 2: AMBER KRI commentary on cyber phishing-test results, with disclosure-controls overlap

Input: a bank's `CYB-007 / Phishing simulation click-through rate` KRI is AMBER for the third consecutive month. Prior month was AMBER, current value 12.4% (trigger 10%, limit 15%). Source posture: BCBS 239 Principles 7 and 9, FFIEC IT Examination Handbook Information Security booklet, and the firm's cyber-control framework. The cross-cutting cyber overlay flags a question for the disclosure-controls trace (sustained deterioration could be a leading indicator).

Output emphasizes:
- Root cause: shift in phishing-test difficulty (Q1 used basic templates, Q2 introduced AI-assisted spear-phishing templates that raised the difficulty curve) — the metric movement reflects test-design change, not a population control failure.
- Contributing factors: none control-side; the underlying control posture (mandatory training completion, MFA coverage, secure email gateway efficacy) is unchanged.
- Action taken: communication to the workforce on AI-assisted phishing patterns; targeted retraining for the highest click-through cohort (Owner: CISO; Completed: previous month).
- Action planned: refresh of the secure-email-gateway rules to detect AI-generated lures (Owner: CISO; Target: end of next month); review of training content (Owner: CHRO with CISO; Target: next quarter).
- Residual-risk view: expected RAG next quarter is AMBER (trending toward GREEN once retraining lands; not yet evidenced).
- Linked issues: none — this is a metric movement attributable to test redesign, not a control issue.
- Second-line challenge note: first-line draft proposed downgrading the trigger from 10% to 13% in light of the test-design change; second-line view is that the trigger should remain at 10% pending refreshed test population data over two more quarters; recalibrating mid-stream would mask the metric movement.
- BCBS 239 principle references: Principle 7, Principle 9.
- Cyber overlay note: the third consecutive AMBER period triggers the disclosure-controls leading-indicator review per the cross-cutting cyber overlay; phase 2 SKILL.md cross-references `cyber-disclosure-readiness` Artifact C (DCP readiness map) for the protocol.
- Confidence label: medium. Test-design change introduces non-comparability with prior periods; the metric requires two more quarters under the new template population to be reliable.

## Common pitfalls

1. Commentary that restates the metric. "OPS-001 was RED at $14.8m" is the metric, not commentary. Phase 2 must reject blocks where the commentary text does not include a named root cause, contributing factors, action taken, action planned, and residual-risk view.
2. First-line voice. The second-line commentary is challenge, not first-line restatement. Phase 2 must require either an explicit `second_line_challenge_note` or a documented rationale that the second-line view aligns with the first-line view.
3. "Investigation ongoing" for multi-period breaches. A second consecutive period of breach with no named root cause is not credible. Phase 2 must require a named root cause for `breach_age_periods` greater than 1 (or an explicit owner-and-date for when root cause will land).
4. Action planned without owner or target. Phase 2 must reject `action_planned` items missing `owner` or `target_date`.
5. Residual-risk view as wishful thinking. The expected RAG must have a documented rationale linked to the action plan and external-driver outlook. Phase 2 must reject `expected_rag = green` where the breach is multi-period and the action plan has not yet completed.
6. KRI threshold gaming. Recalibrating thresholds in response to a breach is sometimes legitimate (the metric or population has changed) and sometimes masking. Phase 2 must surface any threshold-recalibration request as an explicit commentary item, with rationale, and route it to the RAS-owner for committee approval.
7. Cyber KRI overlap with disclosure controls. Sustained cyber-KRI deterioration can be a leading indicator that should feed the disclosure-controls trace. Phase 2 must cross-reference `cyber-disclosure-readiness` when cyber KRIs trend deteriorating for two or more consecutive periods.
8. Climate KRI without data caveat. Climate KRIs that rely on vendor-supplied scenario or emissions data must carry the BCBS 239 Principle 3 / Principle 6 caveat in the commentary. Phase 2 must include a data-confidence note for any climate KRI block.
