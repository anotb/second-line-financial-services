# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## bsa-cdd-refresh-test-plan

### Example: BSA/AML CDD refresh control test plan against FFIEC manual expectations

Public-source-derived. No named institution. The shape mirrors a periodic CDD refresh control test plan at a bank with a high-risk customer population.

#### Input

- **Trigger**: annual program coverage; design effectiveness was tested in the prior cycle and is not retested this cycle.
- **Control mapping supplied**: control ID `CTRL-BSA-CDD-REFRESH-002` from the firm's control inventory, addressing the periodic CDD refresh control on high-risk customers (personal and business).
- **Engagement scope supplied**: institution = national bank; primary regulators = OCC, FinCEN, FRB; persona = BSA officer's compliance-testing pod lead, with the BSA officer as the deliverable consumer; source posture = public-plus-firm-policy-plus-evidence; sector overlay = banking; cross-cutting overlay = none additional (BSA testing sits inside banking).
- **Period under test**: refresh-due window for the most recent twelve months.
- **Prior-cycle test ID**: `TP-BSA-CDD-2025-02`. Cycle closed with design effectiveness rated effective; current cycle reads operating effectiveness only.

#### Output sketch

The skill produces a control test plan. Headlines:

- **Header** — test ID `TP-BSA-CDD-2026-02`, control ID `CTRL-BSA-CDD-REFRESH-002`, obligation IDs for the FFIEC BSA/AML CDD module [verify section] and 31 CFR §1010.230 (beneficial ownership for legal-entity customers) [verify subsection], period covered (twelve-month refresh-due window), preparer role (BSA-testing analyst), reviewer role (BSA-testing manager — separate role from preparer and from the BSA officer), confidence label high on procedures and medium on the firm-policy refresh windows (no external benchmark for the 12-month and 18-month windows).
- **Scope statement** — periodic CDD refresh testing for high-risk customers due for refresh in the period; in scope: high-risk personal customers due in the period (firm-policy 12-month window) and high-risk business / legal-entity customers due in the period (firm-policy 18-month window); out of scope: standard-risk and medium-risk refresh cycles (separate plans), customer-risk-rating accuracy testing (separate plan against the CRR methodology).
- **Test objective** — read: operating-effectiveness-only. Statement: the cycle concludes on whether the periodic CDD refresh occurred within the firm-policy window for sampled high-risk customers, whether the refreshed customer risk profile reflects current activity, and whether beneficial-ownership recertification was obtained for entity customers under 31 CFR §1010.230 [verify subsection]. Design effectiveness was tested in the prior cycle (`TP-BSA-CDD-2025-02`); refresher walkthrough this cycle covers system changes only.
- **Source criteria** — FFIEC BSA/AML Examination Manual CDD module [verify section] (periodic refresh expectation for high-risk customers; risk-profile maintenance); 31 CFR §1010.230 [verify subsection] (beneficial ownership recertification for legal-entity customers on triggering events); firm BSA/AML policy section on high-risk customer refresh (12-month window for personal, 18-month window for business; firm policy, no external-benchmark equivalent).
- **Population and sampling reference** — population: high-risk customers due for refresh in the twelve-month period (extracted from the customer-risk-rating system; period-boundary rule is refresh-due-date during period, where refresh-due-date is the prior refresh date plus the firm-policy window). Stratification planned by risk tier (CDD-Tier-1 personal, CDD-Tier-1 business, CDD-Tier-2 personal, CDD-Tier-2 business). Extract integrity check planned: reconciliation of CRR-system extract to the customer-master extract for the same period plus an independent count from the AML-monitoring system on the high-risk-customer flag. Sampling memo to be produced separately under `control-sampling`; sampling_id will be written back. Stratified sample expected.
- **Walkthrough plan** — refresher walkthrough on system changes only; full walkthrough was performed in the prior cycle and the walkthrough conclusion is incorporated by reference. Roles to interview: CRR-system operations lead (changes since prior cycle), CDD/EDD analyst pod lead (process changes), beneficial-ownership recertification owner (process and trigger logic). Screens to inspect: any CRR-system or EDD-workflow screens changed since the prior cycle. Evidence to capture: change log for the CRR system and the EDD workflow since the prior cycle; refresher walkthrough conclusion (whether design changes are material to operating-effectiveness procedures).
- **Operating-effectiveness procedures** — OP1: reperformance methodology, sample of high-risk customers (per sampling memo) tested against the firm-policy refresh window; expected evidence per sample is the refresh-completed timestamp in the CRR system plus the refresh-evidence package (refreshed CDD questionnaire, EDD enrichment evidence). OP2: inspection methodology, the same sample tested for whether the refreshed customer risk profile reflects current activity (qualitative reperformance against AML-monitoring activity for the prior twelve months); expected evidence is the refreshed risk-profile record and the AML-monitoring activity summary. OP3: reperformance methodology, the legal-entity subset of the sample tested for beneficial-ownership recertification under §1010.230 [verify subsection]; expected evidence per sample is the recertification form, the certifier-attestation record, and any change-of-ownership trigger evidence.
- **Evidence-request reference** — to be produced separately under `evidence-request-builder`; evidence_request_list_id will be written back. Inline list omitted.
- **Pass and fail criteria** — pass criterion: 100% of sampled refreshes within the firm-policy window with current refresh-evidence package; refreshed risk profile reflects current activity; beneficial-ownership recertification obtained for the legal-entity subset. Fail criterion: any refresh outside the firm-policy window without escalation evidence (escalation-approved extension or the customer offboarded with documented rationale); refreshed risk profile does not reflect current activity; beneficial-ownership recertification missing for a legal-entity customer where a trigger event occurred. Tolerable deviation rate: 0% on the refresh-window timing breach without escalation (zero-tolerable per firm policy), severity-driven aggregation; 0% on missing beneficial-ownership recertification at trigger events (zero-tolerable per §1010.230 expectation [verify subsection]).
- **Limitations and assumptions** — the cycle does not assess the accuracy of the customer risk rating itself (a separate plan against the CRR methodology covers that); the cycle does not assess CIP at account-opening (a separate plan covers that); reliance on prior-cycle design-effectiveness conclusion (`WP-BSA-CDD-2025-02`) is named with the prior workpaper ID and the rationale; the refresher walkthrough is the cross-check on whether design changes since the prior cycle invalidate that reliance. Period coverage limited to the twelve-month refresh-due window. SAR content is not inspected as part of this plan; SAR-decision testing is a separate plan with the access-control posture noted.
- **Downstream consumers** — `workpaper-drafter`, `qa-workpaper`, `exception-analysis`, `issue-writeup` (where any issue elevation is needed).
- **Reviewer questions** — one reviewer question for pre-fieldwork sign-off: whether the firm-policy 18-month window for high-risk business / legal-entity customers should be benchmarked against any external reference for this cycle, given the absence of a regulator-set window for the high-risk business population (the FFIEC BSA/AML manual sets the periodic refresh expectation but not the specific window).
- **Confidence label** — high on procedures (FFIEC manual and §1010.230 are direct anchors for the operating tests); medium on the firm-policy refresh-window criterion (no external-benchmark equivalent for the 12-month and 18-month windows, so the criterion sits on firm policy alone for those specific timing values).

The plan stops at preparer sign-off; the reviewer signs separately, before evidence pulls begin.

#### Why this scenario matters

- **Boundary check on operating-only framing**: the plan reads operating effectiveness only this cycle, with the prior-cycle design-effectiveness conclusion incorporated by reference and a refresher walkthrough as the cross-check on whether design changes invalidate that reliance. Silent inheritance is the failure mode this avoids.
- **Boundary check on zero-tolerable framing**: the refresh-window timing breach without escalation and the missing beneficial-ownership recertification at trigger events are both zero-tolerable, severity-driven; the plan does not collapse them into a rate read.
- **Boundary check on out-of-scope items**: customer-risk-rating accuracy and CIP at account-opening are explicitly out of scope; the plan does not let the testing pod drift into them.
- **Boundary check on firm-policy criteria with no external benchmark**: the 12-month and 18-month refresh windows are firm-policy criteria; the confidence label reflects the absence of an external-benchmark equivalent for those specific values.
- **Boundary check on SAR access posture**: SAR content is restricted; the plan names the access-control posture and routes SAR-decision testing to a separate plan rather than absorbing it.

#### Anchors

- FFIEC BSA/AML Examination Manual, CDD module [verify section].
- 31 CFR §1010.230 (beneficial ownership for legal-entity customers) [verify subsection].
- IIA Global Internal Audit Standards — Standard 13 (Planning Engagements) [verify section].
- AICPA AU-C 330, Performing Audit Procedures in Response to Assessed Risks [verify paragraph references].
- AICPA AU-C 530, Audit Sampling [verify paragraph references].
- SR 08-8 (Federal Reserve, October 16, 2008) [verify section].

See `references/source-anchors.md` and `references/sector-overlays.md#banking` for full citations.

## reg-e-error-resolution-test-plan

### Example: annual Reg E error-resolution test plan for a regional bank

Public-source-derived. No named institution. The shape mirrors a common annual Reg E error-resolution test plan at a HMDA-reportable, Reg E-active bank.

#### Input

- **Trigger**: annual program coverage; the prior-cycle test plan covers the same control with a known finding on in-app dispute submissions launched mid-prior-cycle that the current cycle is asked to fold in.
- **Control mapping supplied**: control ID `CTRL-CMP-REGE-ERR-001` from the firm's control inventory, addressing the consumer-dispute error-resolution control under Reg E §1005.11.
- **Engagement scope supplied**: institution = state-member bank; primary regulators = FRB, CFPB, state DFI; persona = compliance-testing manager; source posture = public-plus-firm-policy-plus-evidence; sector overlay = banking; cross-cutting overlay = conduct (consumer-facing).
- **Period under test**: most recent calendar year.
- **Prior-cycle test ID**: `TP-CMP-REGE-2025-01`. Cycle closed with a documentation finding on in-app dispute submissions; the current cycle restates that observation as a planning input.

#### Output sketch

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

#### Why this scenario matters

- **Boundary check on design-and-operating separation**: the plan separates design procedures (DP1-DP3, walkthrough-and-inspection) from operating procedures (OP1-OP3, sample-based reperformance and inspection); the workpaper later reads against the same separation.
- **Boundary check on prior-cycle reliance**: the plan names reliance on the prior-cycle workpaper for design effectiveness on existing channels and confirms via refresher walkthrough; it does not silently inherit the prior conclusion.
- **Boundary check on tolerable rate**: the procedural-clock breach is zero-tolerable per firm policy; the aggregation is severity-driven, and the plan says so explicitly so the workpaper does not collapse it into a rate read.
- **Boundary check on cross-skill handoffs**: sampling and evidence-request work go to dedicated skills with foreign-key write-back; the plan does not invent the sample design or the evidence ask independently.
- **Boundary check on reviewer questions**: the in-app-sample-size question is for the named reviewer to decide before sign-off; the plan does not pre-judge it.

#### Anchors

- Reg E — 12 CFR Part 1005, especially §1005.11(c) and §1005.11(d) [verify subsection labels].
- IIA Global Internal Audit Standards — Standard 13 (Planning Engagements) [verify section].
- AICPA AU-C 300, Planning an Audit [verify paragraph references].
- AICPA AU-C 330, Performing Audit Procedures in Response to Assessed Risks [verify paragraph references].
- FFIEC Consumer Compliance Rating System [verify Federal Register citation].
- CFPB Compliance Management Review examination procedures [verify section labels].

See `references/source-anchors.md`, `references/sector-overlays.md#banking`, and `references/cross-cutting.md#conduct` for full citations.

## troubleshooting

### Troubleshooting: test-plan-builder

Recurring pitfalls. Read before drafting the plan and again before pre-fieldwork sign-off.

#### Methodology and procedure discipline

##### Conflating design and operating procedures

Design effectiveness is evaluated by walkthrough-and-inspection (does the control as designed address the criterion). Operating effectiveness is evaluated by sample-based reperformance, observation, inquiry, or confirmation (did the control operate as designed during the period). The plan separates them into two procedure lists with different methodology per procedure. A plan that runs design and operating into one procedure list cannot tell the workpaper how to draft the conclusion section, and the workpaper later cannot land separate design-effectiveness and operating-effectiveness conclusions cleanly. The schema enforces the separation: `design_procedures` and `operating_procedures` are separate arrays.

##### Listing procedures without expected evidence or expected observable condition

A procedure with no expected artifact cannot be passed or failed cleanly at fieldwork. Each procedure carries the expected evidence (configuration screen, policy excerpt, attestation form template, training record for design; case file, system extract, attestation packet, reconciliation for operating) and the expected observable condition that supports a met or pass read. The schema requires both fields per procedure. A plan that names "test the control" without the expected evidence and observable condition is a draft, not a plan.

##### Skipping the walkthrough on "small" controls

The walkthrough is the design read that justifies the procedures. Skipping it on small controls is the most common cause of a "design-gap" exception being surfaced for the first time only in the workpaper, when it should have been planned-against from the start. Where the prior cycle covered design and the current cycle is operating-only, the walkthrough plan can be a refresher walkthrough on system changes only, and the plan says so explicitly with the prior workpaper ID referenced. Skipping the walkthrough entirely needs a documented rationale and reviewer sign-off.

##### Reusing a prior-cycle plan without restating criteria

Rules change. Section labels renumber. Firm policies update. The criteria list must be the current period's criteria. Copying the prior-cycle criteria list without re-reading the rule and the firm's policy is the most common drafting failure. The plan's source-trace section should carry the date of the rule version and the firm-policy version the criteria were drawn from.

#### Scope and boundary discipline

##### Letting first-line owners draft the plan

The plan is second-line work product. First-line input is welcome, particularly on process-flow detail and on planned interview roles, but the plan is signed off by the testing reviewer, not the control owner. A plan drafted by the first-line owner is the methodology equivalent of self-attestation. The reviewer-separation discipline starts at planning, not at fieldwork.

##### Treating the plan as a one-off rather than the workpaper's contract

The plan is the contract for the workpaper. If the workpaper later diverges from the plan, the divergence is a finding in QA review unless the divergence was named at the time as a scope change with the named reviewer's sign-off. A plan that the testing pod does not refer to at fieldwork is a planning artifact wasted; the test plan is the document the workpaper drafter reads first.

##### Drafting evidence pulls before reviewer sign-off

Pre-fieldwork sign-off is a hard gate. Evidence pulls happen after sign-off, not before. A plan signed after evidence has already been requested reads as a methodology weakness in bank-supervisory exams (CMS finding) and any second-line program quality review. The plan's reviewer-signoff date should precede the evidence-request fielding date, and the schema captures both the preparer date and the reviewer date for that audit trail.

##### Conflating the test plan with the engagement charter

The engagement charter (from `scoping`) is the engagement-level scope. The test plan is the cycle-level scope for a single control. The plan consumes the charter; it does not duplicate it. Where the scope is not formalised separately, the plan says so in the limitations section and the testing program's standing posture is referenced.

#### Population and sampling discipline

##### Defining the population without naming the source of truth

The population definition is incomplete without naming the system or report from which the extract is taken and how the period defines inclusion (open during period, executed during period, action-taken during period). The plan also names the extract integrity check the workpaper will run against the extract for completeness. Without these, the workpaper cannot reconcile the population at fieldwork.

##### Letting sampling decisions sit inline when they should sit in a sampling memo

For non-trivial tests, sampling memo work goes to `control-sampling`; the plan references the sampling memo by ID. Inline sample design in the plan is appropriate for small tests only; large tests with stratification, multiple risk tiers, or zero-tolerable subsets need a dedicated sampling memo so the methodology rationale is properly documented. The schema supports both modes (`sampling_id` for separate memo, `inline_sample_design` for small tests).

##### Treating zero-tolerable populations as rate problems at planning time

Privileged-access populations, sanctions-screening populations, customer-funds-segregation populations, and beneficial-ownership-recertification-at-trigger-event populations typically carry a zero-tolerable rate. A single exception is a finding regardless of overall sample deviation rate. The plan's pass and fail criteria name the zero-tolerable subset and the severity-driven aggregation read explicitly so the workpaper does not collapse it into a rate read.

#### Evidence-request discipline

##### Drafting the evidence request list inside the plan when the dedicated skill exists

For non-trivial tests, the evidence request list goes to `evidence-request-builder`; the plan references the request list by ID. Inline request lists in the plan are appropriate for small tests only. The schema supports both modes (`evidence_request_list_id` for separate list, `inline_evidence_requests` for small tests).

##### Overloading the plan with evidence-request operational detail

The plan names the evidence types and the expected observable conditions per procedure. The operational detail of who fields which request, by when, with what cadence, sits in the evidence-request list (or its dedicated skill output), not in the plan. The plan is the methodology contract; the request list is the operational ask.

#### Pass and fail criteria discipline

##### Writing pass criteria as legal compliance rather than control effectiveness

Pass and fail criteria are calibrated in second-line vocabulary. Pass: "the control operated as designed for the [population] during the period." Fail: "the control did not operate as designed for the [segment] population during the period." Not "the firm complied with [Reg X]" or "the firm violated [Reg X]." Legal-compliance and legal-violation determinations sit with legal counsel and regulator-led examinations, not the test plan or the workpaper that follows. The conduct overlay (when loaded) carries a consumer-harm-signal read distinct from the control-effectiveness read.

##### Pass criteria that the procedures cannot test

If the procedures cannot produce evidence that supports the pass criterion, either the criterion is wrong for this cycle or the procedures are incomplete. The plan walks pass criterion to procedure to expected evidence; if any link is missing, the plan is not yet ready for sign-off.

#### Engagement-scope and overlay loading

##### Loading the wrong sector overlay

Institution type and the regulator the control was designed for drive the sector overlay. HMDA controls pull banking; an adviser compliance-program control pulls capital-markets; a sponsor-bank end-customer reconciliation control pulls payments-fintech and banking together (dual-overlay loading is normal for sponsor-bank arrangements). Do not collapse to one overlay when the scope says two.

##### Skipping cyber overlay on IAM or Part 500 populations

Cyber overlay is default-on for any control test touching IAM, data-protection, or NYDFS Part 500-mandated areas. Skipping the cyber overlay because the test is "operationally categorised as compliance" misses the §500.7 [verify subsection], §500.5 [verify subsection], and §500.17(b) [verify subsection] frame.

##### Skipping conduct overlay on consumer-facing tests

Conduct overlay is default-on for consumer-facing tests where customer-harm framing matters separately from technical control conclusion. UDAAP, fair-lending, complaint-handling, sales-practices, and Reg E error-resolution all benefit from the overlay's separate consumer-harm read at planning time so the procedures and pass criteria are set up to surface the signal.

#### Output discipline

##### Citing without sections

Every regulator citation in the plan carries a section reference or a `[verify section]` placeholder. URL alone does not pass the source-anchor depth check. Use `references/source-anchors.md` and the loaded overlays for the canonical citation set; do not restate excerpts in the plan body.

##### Marking unsupported claims silently

Use `[evidence needed]` explicitly in the plan where a claim is not yet evidenced. An inferred claim presented as evidenced is the failure mode that the plan can carry forward to the workpaper if not surfaced at planning time.

##### Closing with too much certainty

The confidence label is `high` only when source posture, criteria maturity, firm-policy maturity for the control area, and prior-cycle history line up. `medium` and `low` are normal where the source posture is below evidence-aware, where the firm policy is the only criterion for a specific value (with no external benchmark), or where the control area is new and prior-cycle history is thin. `unknown` is honest where the firm has not yet resourced the planning input.

##### Drafting the workpaper inside the plan

The plan stops at planning. It does not pre-write conclusions, pre-classify exceptions, or pre-narrate the workpaper. Each of those is downstream work for `workpaper-drafter`, `exception-analysis`, and `qa-workpaper`. The plan that pre-writes the workpaper has skipped the testing.

##### Filling the reviewer-questions section with questions the preparer answered

A reviewer question is something the preparer cannot resolve and is asking the named reviewer to decide before sign-off. A question the preparer answers in the plan is not a reviewer question; it is a footnote. Cluster reviewer questions for the audience that decides them (typically the testing manager; for plans that touch legal-conduct or regulator-confidential material, the question may route to the head of regulatory affairs or general counsel).
