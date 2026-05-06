# Troubleshooting — workpaper-drafter

Recurring pitfalls. Read before producing the workpaper and again before preparer sign-off.

## Methodology and conclusion discipline

### Conclusions that are not tied to evidence

Every conclusion sentence must point to a procedure result that points to an evidence item. The AU-C 230 "experienced reviewer with no prior connection" test [verify paragraph reference] is the bar. A conclusion sentence with no traceable evidence chain is a QA finding regardless of how plausible the conclusion sounds. The source-trace section closes the file; if the trace is incomplete, the conclusion is not yet drafted.

### Mixing evidence inspection with conclusion language

Evidence inspected is what was looked at. Procedures performed is what was done with it. Conclusions are what the look-at and the doing supports. Three sections, no narrative blending. A workpaper that runs evidence-procedures-conclusion together in prose makes it impossible for a QA reviewer to test whether the conclusion is supported.

### Stating legal violations

Second-line workpapers conclude on control effectiveness, not legal compliance. Use "the control did not operate as designed for the [segment] population during the period," not "the firm violated [Reg X]." Legal-violation determinations sit with legal counsel and regulator-led examinations, not the testing workpaper. Conduct overlay (when loaded) carries a consumer-harm signal read distinct from the control-effectiveness conclusion; that signal is for legal review, not a legal conclusion in the workpaper.

### Forgetting reviewer separation

Preparer and reviewer must be different roles. A workpaper signed by the same role at preparer and reviewer is a QA fail and a CMS finding in bank exams. The sign-off block makes the separation structural; the schema makes it explicit (preparer.role and reviewer.role are separate fields and should not match).

### Skipping limitations

The limitations section is the reviewer's protection paragraph. It explicitly names what the workpaper does not conclude on (a separate control, a separate process, a different period, a different population segment), what reliance was placed on prior testing or vendor SOC work or management-prepared schedules, and what scope exclusions the test plan had. A workpaper without a limitations section gives a QA reviewer nothing to push back on.

### Workpaper drift from test plan

If the procedures executed do not match the test plan, either the plan must be amended pre-fieldwork (with reviewer sign-off captured by reference) or the divergence must be documented as a scope change in the workpaper. Silent drift is a QA finding. Procedures added or substituted in fieldwork carry a pre-fieldwork sign-off reference in the procedures section; the schema requires it when `added_or_substituted` is true.

## Exception handling discipline

### Re-classifying exceptions in the workpaper

The workpaper consumes the classified exception register from `exception-analysis`. It does not re-classify exceptions or invent severity beyond the register. If the workpaper preparer disagrees with the classification, that goes to `exception-analysis` for re-classification, not silent re-write here. The schema enforces the boundary: `exception_register_id` is the foreign key, and the summary fields aggregate what the register says.

### Conflating exception count with deviation rate

Deviation rate is calculated against the sample size and the procedure design. A 60-record sample with six exceptions is a 10% record-level rate; if the test was on multiple data points per record, the field-level rate is calculated separately. The workpaper carries both where the test plan called for procedure-level tolerable rates. Conflating record-level and field-level rates produces wrong projection commentary.

### Treating zero-tolerable populations as rate problems

Privileged-access populations, sanctions-screening populations, and customer-funds-segregation tests typically carry a zero-tolerable rate. A single exception is a finding regardless of overall sample deviation rate. The aggregation section reads severity-driven for these populations, not rate-driven; the conclusion picks up the severity-driven call.

### Skipping the repeat-issue read

An exception that references a prior issue is a repeat. Repeat issues carry asymmetric implications under bank-supervisory expectations (escalating severity), under FINRA 3120 / 3130 (CEO certification posture), and under NYDFS §500.17(b) certification. The workpaper flags repeat-issue posture in the exception summary and the issue-elevation handoff carries the prior issue ID for `issue-writeup` to consume.

## Evidence reliance discipline

### Treating management-prepared schedules as system-of-record evidence

Management-prepared schedules require completeness and accuracy checks. The reliance test note records what the preparer did to validate the schedule against the underlying system. Treating a management-prepared schedule as if it were a system extract without the validation step is a QA finding.

### Relying on prior-period testing without reviewer sign-off

Reliance on prior-period testing is named explicitly in the reliance section with the prior workpaper ID and the rationale. Reviewer sign-off on the reliance posture is captured before the reliance is invoked, not after the workpaper is drafted on top of it. Silent reliance is a QA finding.

### Relying on vendor SOC reports without CUEC analysis

A clean SOC 1 or SOC 2 opinion covers the auditor's selected criteria over the auditor's selected period. The reliance test note covers the SOC scope, the SOC period (continuous coverage of the test period), the exception list (any noted), and the complementary user entity controls (CUECs the firm must implement for the vendor's controls to be effective). A workpaper relying on a clean SOC opinion with critical CUECs unaddressed is a QA finding. The schema's `cuec_posture` enum makes the read explicit.

### Population-extract integrity not checked

A LAR extract, an IAM entitlement extract, a transaction extract, a complaint-management extract — each carries an extract date and is validated against an independent count for completeness. The reliance test note records the extract date and the completeness check. Without the extract-integrity step, every sample-level conclusion sits on an unconfirmed population.

## Sample-design and projection discipline

### Projecting from a sample the test plan did not design for projection

Sample design and projection authority are set in the test plan. A judgmental sample, a 100% sample on a small population, or a stratified sample without random selection within strata may not support population-level projection. The aggregation section reads honestly; if projection is not appropriate, the workpaper says so and conclusion language stays segment-specific.

### Treating a sample-design mismatch as the next cycle's problem

If observed exceptions concentrate in a population segment the sample did not stratify for, the workpaper flags the sample-design implication in the aggregation section. The next cycle picks it up; the current cycle's conclusion notes the limitation.

### Confusing "no exceptions in the sample" with "no exceptions in the population"

A clean sample supports a conclusion of operating effectiveness for the tested period at the sample size's confidence level. It does not support a conclusion of zero population exceptions. The conclusion language is calibrated to what the sample can support.

## Engagement-scope and overlay loading

### Drafting without engagement scope or test-plan-defined scope

If neither engagement-scope nor test-plan scope is on file, the workpaper has no scope to test against. Stop and route to `engagement-scoping` (or `test-plan-builder`) before drafting. The workpaper is not a place to invent scope.

### Loading the wrong sector overlay

Institution type and the regulator the test was designed for drive the sector overlay. HMDA testing pulls banking; an adviser compliance-program test pulls capital-markets; a sponsor-bank end-customer reconciliation test pulls payments-fintech and banking together (dual-overlay loading is normal for sponsor-bank arrangements). Do not collapse to one overlay when the engagement scope says two.

### Skipping cyber overlay on IAM or Part 500 populations

Cyber overlay is default-on for any control test touching IAM, data-protection, or NYDFS Part 500-mandated areas. Skipping the cyber overlay because the test is "operationally categorised as compliance" misses the §500.7 [verify subsection], §500.5 [verify subsection], and §500.17(b) [verify subsection] frame.

### Skipping conduct overlay on consumer-facing tests

Conduct overlay is default-on for consumer-facing tests where customer-harm framing matters separately from technical control conclusion. UDAAP, fair-lending, complaint-handling, sales-practices, and Reg E error-resolution all benefit from the overlay's separate consumer-harm read.

## Output discipline

### Citing without sections

Every regulator citation in the workpaper carries a section reference or a `[verify section]` placeholder. URL alone does not pass the source-anchor depth check. Use `references/source-anchors.md` and the loaded overlays for the canonical citation set; do not restate excerpts in the workpaper body.

### Marking unsupported claims silently

Use `[evidence needed]` explicitly in the workpaper where a claim is not yet evidenced. An inferred claim presented as evidenced is the failure mode and a QA finding.

### Closing with too much certainty

The confidence label is `high` only when source posture, evidence sufficiency, sample size, and reliance posture line up. `medium` and `low` are normal where the source posture is below evidence-aware, where the sample is small relative to the conclusion's scope, or where reliance on second-hand evidence is material. `unknown` is honest where the firm has not yet resourced the evidence ask.

### Drafting the issue narrative in the workpaper

The workpaper elevates issues with a handoff ID, severity, source exception IDs, and a one-line description. The issue narrative (criterion, condition, cause, effect, recommendation seed) is built from the exception register's classification fields and consumed by `issue-writeup`. Drafting the issue narrative in the workpaper duplicates work and creates two versions to keep in sync.

### Filling the QA placeholder

The QA reviewer placeholder is filled by `qa-workpaper`, downstream. The schema captures it as a separate object with QA record ID. The workpaper is not signed by QA at preparer sign-off.
