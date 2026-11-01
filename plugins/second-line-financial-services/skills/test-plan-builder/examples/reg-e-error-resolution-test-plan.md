# Example: annual Reg E error-resolution test plan for a regional bank

Public-source-derived. No named institution. The shape mirrors a common annual Reg E error-resolution test plan at a HMDA-reportable, Reg E-active bank.

## Input

- **Trigger**: annual program coverage; the prior-cycle test plan covers the same control with a known finding on in-app dispute submissions launched mid-prior-cycle that the current cycle is asked to fold in.
- **Control mapping supplied**: control ID `CTRL-CMP-REGE-ERR-001` from the firm's control inventory, addressing the consumer-dispute error-resolution control under Reg E §1005.11.
- **Engagement scope supplied**: institution = state-member bank; primary regulators = FRB, CFPB, state DFI; persona = compliance-testing manager; source posture = public-plus-firm-policy-plus-evidence; sector overlay = banking; cross-cutting overlay = conduct (consumer-facing).
- **Period under test**: most recent calendar year.
- **Prior-cycle test ID**: `TP-CMP-REGE-2025-01`. Cycle closed with a documentation finding on in-app dispute submissions; the current cycle restates that observation as a planning input.

## Output sketch

The skill produces a control test plan. Headlines:

- **Header** — test ID `TP-CMP-REGE-2026-01`, control ID `CTRL-CMP-REGE-ERR-001`, obligation IDs for Reg E §1005.11(c) (provisional credit timing) and §1005.11(d) (notice of resolution) [verify subsection labels], period covered (calendar year), preparer role (compliance-testing analyst), reviewer role (compliance-testing manager — separate role), confidence label medium pending firm-policy update on in-app dispute handling.
- **Scope statement** — annual Reg E error-resolution testing for the calendar year; in scope: consumer disputes raised through call centre, branch, and the in-app dispute channel launched mid-prior-cycle; out of scope: Reg Z billing-error disputes (separate cycle), commercial Reg E claims where applicable.
- **Test objective** — read: design-and-operating combined. Statement: the cycle concludes on whether the dispute-handling control is designed to enforce the §1005.11 procedural clocks across all three intake channels and whether it operated as designed during the period.
- **Source criteria** — Reg E §1005.11(c) (provisional credit timing — day 10 generally, day 5 for new accounts [verify §1005.11(c) timing]); §1005.11(d) (notice of resolution — within three business days of completing the investigation [verify subsection]); the firm's dispute-handling policy section 4 (intake channels, routing, investigator assignment, customer notice generation). FFIEC Consumer Compliance Rating System cited as the rating-frame anchor [verify Federal Register citation]. CFPB CMS examination procedures cited as the testing-program scoping anchor [verify section labels].
- **Population and sampling reference** — population: Reg E disputes raised in the calendar year (extracted from the dispute-management system; period-boundary rule is intake date during period). Stratification planned by intake channel (call centre, branch, in-app) to ensure the new in-app channel is meaningfully sampled. Extract integrity check planned: reconciliation of dispute-management-system extract to the case-management-ticketing-system case count plus the call-centre-CRM dispute-flagged-call count. Sampling memo to be produced separately under `control-sampling`; sampling_id will be written back to this plan.
- **Walkthrough plan** — full walkthrough this cycle (in-app channel was new mid-prior-cycle). Roles to interview: dispute-intake lead (call centre), branch-operations dispute-handling lead, in-app dispute product owner, deposit-operations provisional-credit lead, customer-communications operations lead. Processes to observe: dispute intake (call centre and branch), in-app dispute submission flow, case routing, investigation assignment, provisional credit issuance, notice-of-resolution generation, customer-notice mailing or e-delivery. Screens to inspect: dispute-management-system intake screen, case-routing logic configuration, provisional-credit posting screen in deposit-operations system, notice-template approval screen.
- **Design-effectiveness procedures** — DP1: walkthrough-and-inspection of the dispute-management system workflow configuration to confirm the provisional-credit clock (day 10 generally, day 5 for new accounts) is enforced at the workflow level for all three channels; expected evidence is the workflow configuration export. DP2: walkthrough-and-inspection of the in-app dispute submission flow against the §1005.11(b) error-notice content requirements; expected evidence is the in-app screen flow capture plus the screen-content text. DP3: inspection of the firm's policy section 4 against §1005.11 to confirm the policy carries the procedural clocks and the channel-coverage scope.
- **Operating-effectiveness procedures** — OP1: reperformance methodology, sample of 50 disputes (per sampling memo, stratified across channels) tested against the provisional-credit clock; expected evidence per sample is the case file with timestamps for intake date, investigation start, and provisional-credit posting. OP2: reperformance methodology, same 50 disputes tested against the notice-of-resolution clock; expected evidence per sample is the customer-notice generation timestamp and the notice content. OP3: inspection methodology, the 50-dispute sample tested for routing accuracy (intake channel to investigator); expected evidence is the routing-log entry per case.
- **Evidence-request reference** — to be produced separately under `evidence-request-builder`; evidence_request_list_id will be written back. Inline list omitted.
- **Pass and fail criteria** — pass criterion: 100% of sampled disputes within the §1005.11(c) provisional-credit clock and the §1005.11(d) notice-of-resolution clock with current evidence in the case file; design procedures meet the workflow-enforcement and policy-coverage observable conditions. Fail criterion: any sampled item outside either procedural clock without escalation evidence; or design procedures show the workflow does not enforce the clock for at least one channel; or the policy is silent on a procedural clock that the rule requires. Tolerable deviation rate: 0% on the §1005.11(c) and (d) clocks per firm policy (zero-tolerable for procedural-clock breach without escalation), severity-driven aggregation.
- **Limitations and assumptions** — period coverage limited to the calendar year; reliance on prior testing for the existing call-centre and branch channels (prior workpaper ID `WP-CMP-REGE-2025-01` covers design effectiveness on these channels — current cycle confirms via refresher walkthrough plus operating-effectiveness procedures); Reg Z billing-error disputes out of scope (separate cycle). Assumes the dispute-management-system extract is the authoritative population; if the case-management-ticketing-system or call-centre-CRM count diverges materially, sample design will be revisited.
- **Downstream consumers** — `workpaper-drafter`, `qa-workpaper`, `exception-analysis`, `issue-writeup` (where any issue elevation is needed).
- **Reviewer questions** — one reviewer question for pre-fieldwork sign-off: whether the in-app channel sample size of 15 (proposed by sampling memo) is sufficient to support an operating-effectiveness conclusion specific to the in-app channel given its mid-prior-cycle launch, or whether the channel should be 100%-tested for the first full cycle.
- **Confidence label** — medium pending firm-policy update on in-app dispute handling (the policy section 4 was last updated before the in-app launch; firm-policy maturity for the in-app channel is the open question).

The plan stops at preparer sign-off; the reviewer signs separately, before evidence pulls begin.

## Why this scenario matters

- **Boundary check on design-and-operating separation**: the plan separates design procedures (DP1-DP3, walkthrough-and-inspection) from operating procedures (OP1-OP3, sample-based reperformance and inspection); the workpaper later reads against the same separation.
- **Boundary check on prior-cycle reliance**: the plan names reliance on the prior-cycle workpaper for design effectiveness on existing channels and confirms via refresher walkthrough; it does not silently inherit the prior conclusion.
- **Boundary check on tolerable rate**: the procedural-clock breach is zero-tolerable per firm policy; the aggregation is severity-driven, and the plan says so explicitly so the workpaper does not collapse it into a rate read.
- **Boundary check on cross-skill handoffs**: sampling and evidence-request work go to dedicated skills with foreign-key write-back; the plan does not invent the sample design or the evidence ask independently.
- **Boundary check on reviewer questions**: the in-app-sample-size question is for the named reviewer to decide before sign-off; the plan does not pre-judge it.

## Anchors

- Reg E — 12 CFR Part 1005, especially §1005.11(c) and §1005.11(d) [verify subsection labels].
- IIA Global Internal Audit Standards — Standard 13 (Planning Engagements) [verify section].
- AICPA AU-C 300, Planning an Audit [verify paragraph references].
- AICPA AU-C 330, Performing Audit Procedures in Response to Assessed Risks [verify paragraph references].
- FFIEC Consumer Compliance Rating System [verify Federal Register citation].
- CFPB Compliance Management Review examination procedures [verify section labels].

See `references/source-anchors.md`, `references/sector-overlays/banking.md`, and `references/cross-cutting/conduct.md` for full citations.
