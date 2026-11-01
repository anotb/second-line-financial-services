# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## hmda-lar-data-integrity

### Example: HMDA LAR data-integrity workpaper for the annual compliance-testing cycle

Public-source-derived. No named institution. The shape mirrors a common annual HMDA data-integrity test at a HMDA-reportable bank.

#### Input

- **Test cycle**: annual HMDA LAR data-integrity test, drafting the testing workpaper from completed fieldwork.
- **Test plan reference**: pre-fieldwork test plan (test ID `TP-CMP-HMDA-2026-01`) identifies the population (LAR records for the calendar year), the sample size (60 records, stratified by action-taken type), and the procedures (re-perform of selected LAR fields against source documents; reconciliation of LAR to the loan-origination system extract; demographic-firewall control reperformance).
- **Engagement scope supplied**: institution = state member bank; primary regulators = FRB, CFPB, state DFI; persona = compliance-testing manager; source posture = public-plus-firm-policy-plus-evidence; sector overlay = banking; cross-cutting overlays = conduct (consumer-facing), with privacy not loaded as the test does not touch GLBA Safeguards.
- **Exception register supplied**: from `exception-analysis`, exception_register_id `ER-CMP-HMDA-2026-01`. Six classified exceptions: two transposition errors on dollar amounts (data-integrity, medium); three missing-data points (one rate spread, two lien position) (documentation, medium); one mismatched property-type code (data-integrity, low). No design exceptions.
- **Test plan tolerable rate**: 3% data-point error rate for HMDA-reportable fields, set per firm policy and benchmarked against FFIEC HMDA Filing Instructions Guide [verify edition] data-validation thresholds.

#### Output sketch

The skill produces a testing workpaper. Headlines:

- **Header** — workpaper ID, test ID `TP-CMP-HMDA-2026-01`, control ID for the HMDA data-integrity control, obligation IDs for Reg C 12 CFR 1003.4 [verify subsection] data points and 12 CFR 1003.5 [verify subsection] reporting, period covered (calendar year), preparer role (compliance-testing analyst), reviewer role (compliance-testing manager — separate role), QA placeholder.
- **Scope and source posture** — annual HMDA testing cycle, 60-record sample of LAR records, source posture public-plus-firm-policy-plus-evidence, no scope changes from the test plan.
- **Source criteria** — Reg C §1003.4 (data points) [verify subsection] cited with specific data-point definitions for the tested fields (loan amount, action taken, rate spread, lien position, property type, demographic information). FFIEC HMDA Filing Instructions Guide [verify edition] cited as the field-validation logic anchor.
- **Walkthrough summary** — walkthrough conducted with the LAR preparer (role), the loan-operations data-quality lead (role), and the demographic-firewall control owner (role). Screens inspected: LOS underwriting-decision screen, LAR generation report, demographic-information data-flow. Walkthrough conclusion: design appears effective; the LOS-to-LAR pipeline supports per-field reperformance, the demographic firewall is structurally enforced through role-based system access.
- **Evidence inspected** — LAR extract per sample ID (system-of-record extract from the LAR generation system, extract date noted, completeness check against the LOS originated-loan count); underlying loan files per sample (URLA, AUS findings, rate-lock confirmation, settlement statement) (system-of-record, individually pulled by sample ID); demographic-firewall evidence (system-access entitlement extract for the production environment, attestation from the demographic-firewall control owner). Reliance test note on the LAR extract: completeness reconciled to the LOS count within tolerance; accuracy validated by sample re-extraction of three records cross-checked against the live LAR.
- **Procedures performed** — P1 reperformance of the data points listed in the test plan against source documents per sample (executed against all 60 samples; six exceptions surfaced); P2 LAR-to-LOS reconciliation at the population level (executed; reconciled within tolerance); P3 demographic-firewall reperformance (executed; no exceptions). All procedures executed as designed; no fieldwork additions.
- **Sample-level results** — table with 60 rows; six rows flagged with exception IDs into ER-CMP-HMDA-2026-01.
- **Exceptions identified** — summary by classification: 0 design, 0 operating, 3 documentation, 3 data-integrity. Summary by severity: 0 critical, 0 high, 5 medium, 1 low. Repeat-issue posture: two of the data-integrity exceptions reference a prior-cycle issue on the LOS-to-LAR pipeline. Tolerable rate 3%; observed deviation rate 10% on tested data points (six exceptions across multiple data points; weighted by data-point count, the field-level deviation rate is calculated rather than the record-level rate).
- **Aggregation and projection** — concentration commentary: exceptions concentrated in non-residential refinances, suggesting a segment-specific pipeline weakness rather than a systemic LOS-to-LAR break. Sample-design implication: stratification by action-taken type was adequate for the population overall but did not stratify by property type; future cycle should consider property-type stratification. Projection commentary: appropriate to project the data-point deviation rate to the segment-level population (non-residential refinances) at the field level; not appropriate to project to the full LAR population given the segment concentration.
- **Conclusion** — design effectiveness: effective (the LOS-to-LAR pipeline supports per-field reperformance and the demographic firewall is enforced through role-based access). Operating effectiveness: partially effective (observed deviation rate 10% on data points exceeds the 3% tolerable rate; concentration in non-residential refinances). Combined: not effective at the data-point level for the non-residential refinance segment; effective for the residential-refinance and home-purchase segments tested.
- **Issues elevated** — two issues handed to `issue-writeup`: a data-integrity issue on the rate-spread calculation queue (handoff ID I-2026-013, severity medium, repeat issue from prior cycle) and a documentation issue on lien-position capture at origination (handoff ID I-2026-014, severity medium).
- **Reviewer questions** — one reviewer question: whether the segment-level deviation rate warrants re-submission consideration under the FFIEC HMDA re-submission thresholds [verify FFIEC HMDA re-submission threshold guidance edition], routed to legal review and the head of regulatory affairs; not concluded in the workpaper.
- **Limitations and reliance** — period coverage limited to the calendar year; demographic-firewall testing covers the production environment as of the testing date and does not cover the prior period; reliance on the LOS-to-LAR pipeline integrity rests on the population-level reconciliation (P2) plus sample-level reperformance (P1); no reliance on prior testing.
- **Confidence label** — high (source posture public-plus-firm-policy-plus-evidence, sample size adequate for the segment-level conclusion, evidence inspected directly).

The workpaper stops at preparer sign-off.

#### Why this scenario matters

- **Boundary check on conclusion language**: the workpaper concludes on control effectiveness, not on whether the firm violated Reg C. Re-submission consideration sits with legal review and the head of regulatory affairs.
- **Boundary check on exception-analysis handoff**: the workpaper consumes the classified exception register; it does not re-classify exceptions or invent severity beyond the register.
- **Boundary check on aggregation read**: observed deviation rate exceeds tolerable, but concentration analysis matters; the conclusion distinguishes segment-level from population-level performance.
- **Boundary check on issue-writeup handoff**: two issues are elevated with distinct handoff IDs, severities, and source exception IDs; the workpaper does not draft the issue narrative.
- **Boundary check on reviewer questions**: the FFIEC re-submission consideration is a reviewer question for legal and regulatory-affairs leadership, not a conclusion.

#### Anchors

- Reg C — 12 CFR Part 1003 (HMDA).
- FFIEC HMDA Filing Instructions Guide (current edition) [verify edition].
- AICPA AU-C 230 (Audit Documentation).
- AICPA AU-C 530 (Audit Sampling), §A18-§A22 (evaluating sample results) [verify paragraph references].
- FFIEC IT Examination Handbook, Audit booklet.

See `references/source-anchors.md` and `references/sector-overlays.md#banking` for full citations.

## nydfs-access-recertification

### Example: NYDFS Part 500 access-recertification workpaper for second-line cyber testing

Public-source-derived. No named institution. The shape mirrors a quarterly access-recertification control test at a NYDFS Covered Entity.

#### Input

- **Test cycle**: quarterly access-recertification control test for Q1, drafting the workpaper from completed fieldwork.
- **Test plan reference**: pre-fieldwork test plan (test ID `TP-CYB-AR-2026-Q1`) identifies the population (recertification packets due in the quarter), sample size (30 packets, stratified by privilege tier — 10 standard, 10 privileged, 10 service-account), and procedures (per-packet attestation reperformance, IAM-system reperformance for revocations, HR-IAM feed reconciliation for terminated employees).
- **Engagement scope supplied**: institution = NY-licensed bank; primary regulators = NYDFS, FRB, CFPB; persona = head of cyber risk, with the cyber-risk committee as the deliverable consumer and the §500.17(b) annual certification process as the downstream dependency; source posture = public-plus-firm-policy-plus-evidence; sector overlay = banking; cross-cutting overlays = cyber (default-on for Part 500 Covered Entity).
- **Exception register supplied**: from `exception-analysis`, exception_register_id `ER-CYB-AR-2026-Q1`. Eight classified exceptions: one design exception (the attestation form supports blanket per-system approval rather than per-entitlement attestation), two operating exceptions on attestation timing (timing, medium), one critical operating exception on un-revoked privileged access for a transferred employee (operating, critical), one data-integrity exception on a terminated employee retaining access for fourteen days post-termination due to an HR-IAM feed lag (data-integrity, high), three documentation gaps (attestation packets missing reviewer acknowledgement; documentation, low).
- **Test plan tolerable rate**: 5% standard population, 0% privileged population, set per firm policy and aligned to NYDFS 23 NYCRR §500.7 [verify subsection] expectations on privileged-access governance.

#### Output sketch

The skill produces a testing workpaper. Headlines:

- **Header** — workpaper ID, test ID `TP-CYB-AR-2026-Q1`, control ID for the access-recertification control, obligation ID for NYDFS Part 500 §500.7 [verify subsection], period (Q1 calendar quarter), preparer role (cyber-testing analyst), reviewer role (cyber-testing manager — separate role), QA placeholder.
- **Scope and source posture** — quarterly access-recertification testing, 30-packet sample, source posture public-plus-firm-policy-plus-evidence, no scope changes from the test plan.
- **Source criteria** — NYDFS 23 NYCRR §500.7 [verify subsection] (access privileges and management) cited with the periodic-review and least-privilege requirements; firm IAM control standard cited as the firm-side control specification.
- **Walkthrough summary** — walkthrough conducted with the IAM operations lead (role), the recertification campaign owner (role), and the HR-IAM feed integration owner (role). Screens inspected: IAM administrative console showing the recertification campaign, the attestation form template, the HR-IAM data-flow architecture diagram, sample feed-event logs. Walkthrough conclusion: design gap surfaced — the attestation form supports blanket per-system approval rather than per-entitlement attestation; this is a design-effectiveness finding distinct from operating effectiveness on the form as designed.
- **Evidence inspected** — recertification packets per sample ID (system-of-record extract from the IAM recertification module, with extract date and completeness check against the campaign-wide packet count); IAM entitlement extract for the population (system-of-record, with extract date and reconciliation to the IAM authoritative count); manager attestation logs (system-generated report); revocation tickets (system-of-record from the IAM ticketing system); HR-IAM feed event log (system-of-record); HR termination report (system-of-record extract from the HRIS).
- **Procedures performed** — P1 per-packet attestation reperformance (executed against all 30 packets; eight exceptions surfaced including the design observation on form structure); P2 IAM-system reperformance for revocations (executed; revocation lag observed in two packets where revocation tickets were opened but not closed within the firm clock); P3 HR-IAM feed reconciliation for terminated employees (executed across the broader termination population for the period; one data-integrity exception surfaced on a fourteen-day post-termination access retention). All procedures executed as designed; one supplemental sub-procedure added in fieldwork to reconcile the revocation-ticket-closure timeline with the IAM access-removal effective date (added with pre-fieldwork reviewer sign-off, reference noted).
- **Sample-level results** — table with 30 rows; eight rows flagged with exception IDs into ER-CYB-AR-2026-Q1; the design observation on form structure carried as a separate row with no specific sample ID (design exception applies to the population).
- **Exceptions identified** — summary by classification: 1 design, 3 operating, 3 documentation, 1 data-integrity. Summary by severity: 1 critical, 1 high, 3 medium, 3 low. Repeat-issue posture: the un-revoked privileged-access exception is the second occurrence in two cycles; the workpaper flags it as a repeat issue. Tolerable rate 5% standard population, 0% privileged; observed deviation rate 27% across the full sample, with one exception in the privileged sub-population.
- **Aggregation and projection** — anomaly versus systemic: systemic on the design dimension (the form does not support per-entitlement attestation, affecting the entire recertification campaign); systemic on the operating timing dimension (multiple timing exceptions); anomaly on the privileged exception (single occurrence, but tolerable is zero so the call is severity-driven not rate-driven). Sample-design implication: the privileged sub-sample size of 10 is small for a zero-tolerable-rate test; expanding the privileged sub-population to full enumeration is recommended for the next cycle. Projection commentary: appropriate to project the design exception to the population (the form is the same across the population); appropriate to project the timing-rate operating exception to the population at the same rate; not appropriate to project the data-integrity HR-IAM-lag exception to the population without expanded sampling.
- **Conclusion** — design effectiveness: not effective (the attestation form does not support per-entitlement attestation; per-system blanket approval undermines the §500.7 [verify subsection] least-privilege expectation). Operating effectiveness: not effective (observed deviation rate 27% exceeds tolerable; one privileged exception against a 0% tolerable; HR-IAM feed timing produces post-termination access retention beyond firm tolerance). Combined: not effective.
- **Issues elevated** — three issues handed to `issue-writeup`: a design-gap issue on the recertification form structure (handoff ID I-2026-021, severity high); a critical privileged-access issue on un-revoked privileged access for a transferred employee (handoff ID I-2026-022, severity critical, repeat issue); an HR-IAM data-integrity issue on the post-termination access lag (handoff ID I-2026-023, severity high).
- **Reviewer questions** — one reviewer question: whether the design-gap issue rises to a §500.17(b) [verify subsection] notification consideration in the next annual certification cycle, routed to legal review and the CISO; not concluded in the workpaper.
- **Limitations and reliance** — period coverage limited to Q1; entitlement-provisioning at onboarding is a separate control, separate workpaper; reliance on the HR-IAM feed integration rests on the feed-event log review (P3) plus the HR termination report reconciliation; no reliance on prior testing; reliance on the IAM ticketing system completeness for revocation tracking, with the supplemental sub-procedure as the cross-check.
- **Confidence label** — high (source posture, evidence inspected directly, sample size adequate for the design-and-systemic operating call; the privileged sub-sample size limitation is named in the limitations section).

The workpaper stops at preparer sign-off.

#### Why this scenario matters

- **Boundary check on design-versus-operating separation**: the design exception on the form is distinct from operating exceptions on form usage; the workpaper conclusion separates the two reads.
- **Boundary check on tolerable-rate framing**: the privileged sub-population tolerable rate is zero; the workpaper aggregation reads severity-driven rather than rate-driven.
- **Boundary check on repeat-issue handling**: the un-revoked privileged-access exception is a repeat issue from a prior cycle; the workpaper flags it for the issue-writeup handoff with the prior issue ID referenced.
- **Boundary check on §500.17(b) certification posture**: the workpaper does not certify; it surfaces the design gap as a reviewer question for the senior officer who certifies.
- **Boundary check on cyber overlay defaults**: the conduct overlay is not loaded (this is a cyber-control test, no consumer-facing dimension); the privacy overlay is not loaded (no GLBA Safeguards or HIPAA scope in the test plan).

#### Anchors

- NYDFS 23 NYCRR Part 500.7, §500.17(b).
- AICPA AU-C 230 (Audit Documentation).
- AICPA AU-C 530 (Audit Sampling).
- FFIEC IT Examination Handbook, Information Security booklet.
- NIST SP 800-53A Rev. 5 (control-test documentation conventions).

See `references/source-anchors.md` and `references/cross-cutting.md#cyber` for full citations.

## troubleshooting

### Troubleshooting: workpaper-drafter

Recurring pitfalls. Read before producing the workpaper and again before preparer sign-off.

#### Methodology and conclusion discipline

##### Conclusions that are not tied to evidence

Every conclusion sentence must point to a procedure result that points to an evidence item. The AU-C 230 "experienced reviewer with no prior connection" test [verify paragraph reference] is the bar. A conclusion sentence with no traceable evidence chain is a QA finding regardless of how plausible the conclusion sounds. The source-trace section closes the file; if the trace is incomplete, the conclusion is not yet drafted.

##### Mixing evidence inspection with conclusion language

Evidence inspected is what was looked at. Procedures performed is what was done with it. Conclusions are what the look-at and the doing supports. Three sections, no narrative blending. A workpaper that runs evidence-procedures-conclusion together in prose makes it impossible for a QA reviewer to test whether the conclusion is supported.

##### Stating legal violations

Second-line workpapers conclude on control effectiveness, not legal compliance. Use "the control did not operate as designed for the [segment] population during the period," not "the firm violated [Reg X]." Legal-violation determinations sit with legal counsel and regulator-led examinations, not the testing workpaper. Conduct overlay (when loaded) carries a consumer-harm signal read distinct from the control-effectiveness conclusion; that signal is for legal review, not a legal conclusion in the workpaper.

##### Forgetting reviewer separation

Preparer and reviewer must be different roles. A workpaper signed by the same role at preparer and reviewer is a QA fail and a CMS finding in bank exams. The sign-off block makes the separation structural; the schema makes it explicit (preparer.role and reviewer.role are separate fields and should not match).

##### Skipping limitations

The limitations section is the reviewer's protection paragraph. It explicitly names what the workpaper does not conclude on (a separate control, a separate process, a different period, a different population segment), what reliance was placed on prior testing or vendor SOC work or management-prepared schedules, and what scope exclusions the test plan had. A workpaper without a limitations section gives a QA reviewer nothing to push back on.

##### Workpaper drift from test plan

If the procedures executed do not match the test plan, either the plan must be amended pre-fieldwork (with reviewer sign-off captured by reference) or the divergence must be documented as a scope change in the workpaper. Silent drift is a QA finding. Procedures added or substituted in fieldwork carry a pre-fieldwork sign-off reference in the procedures section; the schema requires it when `added_or_substituted` is true.

#### Exception handling discipline

##### Re-classifying exceptions in the workpaper

The workpaper consumes the classified exception register from `exception-analysis`. It does not re-classify exceptions or invent severity beyond the register. If the workpaper preparer disagrees with the classification, that goes to `exception-analysis` for re-classification, not silent re-write here. The schema enforces the boundary: `exception_register_id` is the foreign key, and the summary fields aggregate what the register says.

##### Conflating exception count with deviation rate

Deviation rate is calculated against the sample size and the procedure design. A 60-record sample with six exceptions is a 10% record-level rate; if the test was on multiple data points per record, the field-level rate is calculated separately. The workpaper carries both where the test plan called for procedure-level tolerable rates. Conflating record-level and field-level rates produces wrong projection commentary.

##### Treating zero-tolerable populations as rate problems

Privileged-access populations, sanctions-screening populations, and customer-funds-segregation tests typically carry a zero-tolerable rate. A single exception is a finding regardless of overall sample deviation rate. The aggregation section reads severity-driven for these populations, not rate-driven; the conclusion picks up the severity-driven call.

##### Skipping the repeat-issue read

An exception that references a prior issue is a repeat. Repeat issues carry asymmetric implications under bank-supervisory expectations (escalating severity), under FINRA 3120 / 3130 (CEO certification posture), and under NYDFS §500.17(b) certification. The workpaper flags repeat-issue posture in the exception summary and the issue-elevation handoff carries the prior issue ID for `issue-writeup` to consume.

#### Evidence reliance discipline

##### Treating management-prepared schedules as system-of-record evidence

Management-prepared schedules require completeness and accuracy checks. The reliance test note records what the preparer did to validate the schedule against the underlying system. Treating a management-prepared schedule as if it were a system extract without the validation step is a QA finding.

##### Relying on prior-period testing without reviewer sign-off

Reliance on prior-period testing is named explicitly in the reliance section with the prior workpaper ID and the rationale. Reviewer sign-off on the reliance posture is captured before the reliance is invoked, not after the workpaper is drafted on top of it. Silent reliance is a QA finding.

##### Relying on vendor SOC reports without CUEC analysis

A clean SOC 1 or SOC 2 opinion covers the auditor's selected criteria over the auditor's selected period. The reliance test note covers the SOC scope, the SOC period (continuous coverage of the test period), the exception list (any noted), and the complementary user entity controls (CUECs the firm must implement for the vendor's controls to be effective). A workpaper relying on a clean SOC opinion with critical CUECs unaddressed is a QA finding. The schema's `cuec_posture` enum makes the read explicit.

##### Population-extract integrity not checked

A LAR extract, an IAM entitlement extract, a transaction extract, a complaint-management extract: each carries an extract date and is validated against an independent count for completeness. The reliance test note records the extract date and the completeness check. Without the extract-integrity step, every sample-level conclusion sits on an unconfirmed population.

#### Sample-design and projection discipline

##### Projecting from a sample the test plan did not design for projection

Sample design and projection authority are set in the test plan. A judgmental sample, a 100% sample on a small population, or a stratified sample without random selection within strata may not support population-level projection. The aggregation section reads honestly; if projection is not appropriate, the workpaper says so and conclusion language stays segment-specific.

##### Treating a sample-design mismatch as the next cycle's problem

If observed exceptions concentrate in a population segment the sample did not stratify for, the workpaper flags the sample-design implication in the aggregation section. The next cycle picks it up; the current cycle's conclusion notes the limitation.

##### Confusing "no exceptions in the sample" with "no exceptions in the population"

A clean sample supports a conclusion of operating effectiveness for the tested period at the sample size's confidence level. It does not support a conclusion of zero population exceptions. The conclusion language is calibrated to what the sample can support.

#### Engagement-scope and overlay loading

##### Drafting without scope or test-plan-defined scope

If neither scope nor test-plan scope is on file, the workpaper has no scope to test against. Stop and route to `scoping` (or `test-plan-builder`) before drafting. The workpaper is not a place to invent scope.

##### Loading the wrong sector overlay

Institution type and the regulator the test was designed for drive the sector overlay. HMDA testing pulls banking; an adviser compliance-program test pulls capital-markets; a sponsor-bank end-customer reconciliation test pulls payments-fintech and banking together (dual-overlay loading is normal for sponsor-bank arrangements). Do not collapse to one overlay when the scope says two.

##### Skipping cyber overlay on IAM or Part 500 populations

Cyber overlay is default-on for any control test touching IAM, data-protection, or NYDFS Part 500-mandated areas. Skipping the cyber overlay because the test is "operationally categorised as compliance" misses the §500.7 [verify subsection], §500.5 [verify subsection], and §500.17(b) [verify subsection] frame.

##### Skipping conduct overlay on consumer-facing tests

Conduct overlay is default-on for consumer-facing tests where customer-harm framing matters separately from technical control conclusion. UDAAP, fair-lending, complaint-handling, sales-practices, and Reg E error-resolution all benefit from the overlay's separate consumer-harm read.

#### Output discipline

##### Citing without sections

Every regulator citation in the workpaper carries a section reference or a `[verify section]` placeholder. URL alone does not pass the source-anchor depth check. Use `references/source-anchors.md` and the loaded overlays for the canonical citation set; do not restate excerpts in the workpaper body.

##### Marking unsupported claims silently

Use `[evidence needed]` explicitly in the workpaper where a claim is not yet evidenced. An inferred claim presented as evidenced is the failure mode and a QA finding.

##### Closing with too much certainty

The confidence label is `high` only when source posture, evidence sufficiency, sample size, and reliance posture line up. `medium` and `low` are normal where the source posture is below evidence-aware, where the sample is small relative to the conclusion's scope, or where reliance on second-hand evidence is material. `unknown` is honest where the firm has not yet resourced the evidence ask.

##### Drafting the issue narrative in the workpaper

The workpaper elevates issues with a handoff ID, severity, source exception IDs, and a one-line description. The issue narrative (criterion, condition, cause, effect, recommendation seed) is built from the exception register's classification fields and consumed by `issue-writeup`. Drafting the issue narrative in the workpaper duplicates work and creates two versions to keep in sync.

##### Filling the QA placeholder

The QA reviewer placeholder is filled by `qa-workpaper`, downstream. The schema captures it as a separate object with QA record ID. The workpaper is not signed by QA at preparer sign-off.
