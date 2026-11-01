# Troubleshooting: test-plan-builder

Recurring pitfalls. Read before drafting the plan and again before pre-fieldwork sign-off.

## Methodology and procedure discipline

### Conflating design and operating procedures

Design effectiveness is evaluated by walkthrough-and-inspection (does the control as designed address the criterion). Operating effectiveness is evaluated by sample-based reperformance, observation, inquiry, or confirmation (did the control operate as designed during the period). The plan separates them into two procedure lists with different methodology per procedure. A plan that runs design and operating into one procedure list cannot tell the workpaper how to draft the conclusion section, and the workpaper later cannot land separate design-effectiveness and operating-effectiveness conclusions cleanly. The schema enforces the separation: `design_procedures` and `operating_procedures` are separate arrays.

### Listing procedures without expected evidence or expected observable condition

A procedure with no expected artifact cannot be passed or failed cleanly at fieldwork. Each procedure carries the expected evidence (configuration screen, policy excerpt, attestation form template, training record for design; case file, system extract, attestation packet, reconciliation for operating) and the expected observable condition that supports a met or pass read. The schema requires both fields per procedure. A plan that names "test the control" without the expected evidence and observable condition is a draft, not a plan.

### Skipping the walkthrough on "small" controls

The walkthrough is the design read that justifies the procedures. Skipping it on small controls is the most common cause of a "design-gap" exception being surfaced for the first time only in the workpaper, when it should have been planned-against from the start. Where the prior cycle covered design and the current cycle is operating-only, the walkthrough plan can be a refresher walkthrough on system changes only, and the plan says so explicitly with the prior workpaper ID referenced. Skipping the walkthrough entirely needs a documented rationale and reviewer sign-off.

### Reusing a prior-cycle plan without restating criteria

Rules change. Section labels renumber. Firm policies update. The criteria list must be the current period's criteria. Copying the prior-cycle criteria list without re-reading the rule and the firm's policy is the most common drafting failure. The plan's source-trace section should carry the date of the rule version and the firm-policy version the criteria were drawn from.

## Scope and boundary discipline

### Letting first-line owners draft the plan

The plan is second-line work product. First-line input is welcome, particularly on process-flow detail and on planned interview roles, but the plan is signed off by the testing reviewer, not the control owner. A plan drafted by the first-line owner is the methodology equivalent of self-attestation. The reviewer-separation discipline starts at planning, not at fieldwork.

### Treating the plan as a one-off rather than the workpaper's contract

The plan is the contract for the workpaper. If the workpaper later diverges from the plan, the divergence is a finding in QA review unless the divergence was named at the time as a scope change with the named reviewer's sign-off. A plan that the testing pod does not refer to at fieldwork is a planning artifact wasted; the test plan is the document the workpaper drafter reads first.

### Drafting evidence pulls before reviewer sign-off

Pre-fieldwork sign-off is a hard gate. Evidence pulls happen after sign-off, not before. A plan signed after evidence has already been requested reads as a methodology weakness in bank-supervisory exams (CMS finding) and any second-line program quality review. The plan's reviewer-signoff date should precede the evidence-request fielding date, and the schema captures both the preparer date and the reviewer date for that audit trail.

### Conflating the test plan with the engagement charter

The engagement charter (from `scoping`) is the engagement-level scope. The test plan is the cycle-level scope for a single control. The plan consumes the charter; it does not duplicate it. Where the scope is not formalised separately, the plan says so in the limitations section and the testing program's standing posture is referenced.

## Population and sampling discipline

### Defining the population without naming the source of truth

The population definition is incomplete without naming the system or report from which the extract is taken and how the period defines inclusion (open during period, executed during period, action-taken during period). The plan also names the extract integrity check the workpaper will run against the extract for completeness. Without these, the workpaper cannot reconcile the population at fieldwork.

### Letting sampling decisions sit inline when they should sit in a sampling memo

For non-trivial tests, sampling memo work goes to `control-sampling`; the plan references the sampling memo by ID. Inline sample design in the plan is appropriate for small tests only; large tests with stratification, multiple risk tiers, or zero-tolerable subsets need a dedicated sampling memo so the methodology rationale is properly documented. The schema supports both modes (`sampling_id` for separate memo, `inline_sample_design` for small tests).

### Treating zero-tolerable populations as rate problems at planning time

Privileged-access populations, sanctions-screening populations, customer-funds-segregation populations, and beneficial-ownership-recertification-at-trigger-event populations typically carry a zero-tolerable rate. A single exception is a finding regardless of overall sample deviation rate. The plan's pass and fail criteria name the zero-tolerable subset and the severity-driven aggregation read explicitly so the workpaper does not collapse it into a rate read.

## Evidence-request discipline

### Drafting the evidence request list inside the plan when the dedicated skill exists

For non-trivial tests, the evidence request list goes to `evidence-request-builder`; the plan references the request list by ID. Inline request lists in the plan are appropriate for small tests only. The schema supports both modes (`evidence_request_list_id` for separate list, `inline_evidence_requests` for small tests).

### Overloading the plan with evidence-request operational detail

The plan names the evidence types and the expected observable conditions per procedure. The operational detail of who fields which request, by when, with what cadence, sits in the evidence-request list (or its dedicated skill output), not in the plan. The plan is the methodology contract; the request list is the operational ask.

## Pass and fail criteria discipline

### Writing pass criteria as legal compliance rather than control effectiveness

Pass and fail criteria are calibrated in second-line vocabulary. Pass: "the control operated as designed for the [population] during the period." Fail: "the control did not operate as designed for the [segment] population during the period." Not "the firm complied with [Reg X]" or "the firm violated [Reg X]." Legal-compliance and legal-violation determinations sit with legal counsel and regulator-led examinations, not the test plan or the workpaper that follows. The conduct overlay (when loaded) carries a consumer-harm-signal read distinct from the control-effectiveness read.

### Pass criteria that the procedures cannot test

If the procedures cannot produce evidence that supports the pass criterion, either the criterion is wrong for this cycle or the procedures are incomplete. The plan walks pass criterion to procedure to expected evidence; if any link is missing, the plan is not yet ready for sign-off.

## Engagement-scope and overlay loading

### Loading the wrong sector overlay

Institution type and the regulator the control was designed for drive the sector overlay. HMDA controls pull banking; an adviser compliance-program control pulls capital-markets; a sponsor-bank end-customer reconciliation control pulls payments-fintech and banking together (dual-overlay loading is normal for sponsor-bank arrangements). Do not collapse to one overlay when the scope says two.

### Skipping cyber overlay on IAM or Part 500 populations

Cyber overlay is default-on for any control test touching IAM, data-protection, or NYDFS Part 500-mandated areas. Skipping the cyber overlay because the test is "operationally categorised as compliance" misses the §500.7 [verify subsection], §500.5 [verify subsection], and §500.17(b) [verify subsection] frame.

### Skipping conduct overlay on consumer-facing tests

Conduct overlay is default-on for consumer-facing tests where customer-harm framing matters separately from technical control conclusion. UDAAP, fair-lending, complaint-handling, sales-practices, and Reg E error-resolution all benefit from the overlay's separate consumer-harm read at planning time so the procedures and pass criteria are set up to surface the signal.

## Output discipline

### Citing without sections

Every regulator citation in the plan carries a section reference or a `[verify section]` placeholder. URL alone does not pass the source-anchor depth check. Use `references/source-anchors.md` and the loaded overlays for the canonical citation set; do not restate excerpts in the plan body.

### Marking unsupported claims silently

Use `[evidence needed]` explicitly in the plan where a claim is not yet evidenced. An inferred claim presented as evidenced is the failure mode that the plan can carry forward to the workpaper if not surfaced at planning time.

### Closing with too much certainty

The confidence label is `high` only when source posture, criteria maturity, firm-policy maturity for the control area, and prior-cycle history line up. `medium` and `low` are normal where the source posture is below evidence-aware, where the firm policy is the only criterion for a specific value (with no external benchmark), or where the control area is new and prior-cycle history is thin. `unknown` is honest where the firm has not yet resourced the planning input.

### Drafting the workpaper inside the plan

The plan stops at planning. It does not pre-write conclusions, pre-classify exceptions, or pre-narrate the workpaper. Each of those is downstream work for `workpaper-drafter`, `exception-analysis`, and `qa-workpaper`. The plan that pre-writes the workpaper has skipped the testing.

### Filling the reviewer-questions section with questions the preparer answered

A reviewer question is something the preparer cannot resolve and is asking the named reviewer to decide before sign-off. A question the preparer answers in the plan is not a reviewer question; it is a footnote. Cluster reviewer questions for the audience that decides them (typically the testing manager; for plans that touch legal-conduct or regulator-confidential material, the question may route to the head of regulatory affairs or general counsel).
