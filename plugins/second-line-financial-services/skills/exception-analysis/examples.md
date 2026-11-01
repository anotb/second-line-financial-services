# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## access-recertification-cyber-test

### Example: access-recertification exception classification under a state security rule

#### Input

A second-line cyber-testing function at a state-licensed financial entity has run the quarterly logical-access-recertification control test on a sample of 30 recertification packets from the period 2026-01-01 to 2026-03-31. The criterion is the entity's IAM policy and the relevant state security-rule provision (the entity is in scope of NYDFS 23 NYCRR Part 500 §500.7 access-privileges) [verify current section labels]. The workpaper-drafter output (`WP-2026-Q1-IAM-Recert-02`) carries the sample-level results and surfaces eight deviations. The exception-analysis skill is called to classify them, rank severity, set disposition, and build the handoff to issue write-up.

The eight raw deviations from the workpaper:

- Four packets had blanket "approved" responses with no per-entitlement review captured.
- Two packets were completed after the policy-stated 30-day deadline.
- One privileged-access packet recorded an entitlement removal that was not actually revoked in the IAM system at the time of testing.
- One packet was for a user no longer employed at the entity (HR offboarded, IAM still provisioned).

The test plan's tolerable deviation rate was set at 5% on standard entitlements and 0% on privileged. Source posture is public-plus-firm-policy-plus-evidence. The scope flags capital-markets sector (the entity is a registered investment adviser) and cyber cross-cutting overlay. The privileged-access exception falls under the firm policy floor that all privileged-access deviations open at critical severity.

#### Why this scenario matters

This is the canonical cyber-control-testing use of exception-analysis. It exercises four of the six classifications (`control-failure`, `design-gap`, `data-integrity`, with implicit `evidence-gap` discrimination), the policy-floor severity override for privileged access, the repeat-issue flag pattern, the population-projection commentary that the design-gap finding affects 100% of packets (not just sampled ones) because the design itself does not require per-entitlement attestation, and the cyber-overlay disambiguation pattern between control-failure and evidence-gap (the un-revoked-access exception is corroborated by the IAM system showing the entitlement still active, so it cannot be an evidence-gap).

#### Output sketch

```yaml
exception_register_id: EX-2026-Q1-IAM-Recert-02
test_id: TP-2026-Q1-IAM-Recert-02
workpaper_id: WP-2026-Q1-IAM-Recert-02
control_id: CTL-IAM-RECERT-Q
obligation_ids: [OBL-NYDFS-500.7, OBL-firm-IAM-Policy-v3.4]
engagement_id: ENG-2026-Cyber-IAM-Q1
period_start: 2026-01-01
period_end: 2026-03-31
business_unit: IT Risk and IAM
jurisdictions: [US-NY, US-federal]
source_posture: public-plus-firm-policy-plus-evidence
scope_statement: >
  Quarterly logical-access-recertification test for 2026-Q1. Population is
  recertification packets due in the quarter for in-scope systems
  (production-tier and privileged-tier). Excludes test and development
  environments and service accounts (separate scope).
preparer: {role: cyber compliance-testing analyst, date: 2026-04-18}
reviewer: {role: head of cyber risk testing, date: }

exceptions:
  - exception_id: X1
    sample_id: S03, S07, S12, S19
    population_reference: standard-entitlement packets
    criterion_source: NYDFS 23 NYCRR §500.7(a)(2); firm IAM Policy v3.4 §4.2 (per-entitlement attestation requirement)
    condition: >
      On four sampled recertification packets (S03 quarterly review of CRM
      access; S07 quarterly review of trading-system read-only access; S12
      quarterly review of finance-system access; S19 quarterly review of
      portfolio-system access), the reviewer recorded a single "approved"
      response covering all entitlements in the packet without per-entitlement
      attestation. The recertification form does not have a per-entitlement
      attestation column.
    classification: design-gap
    severity: high
    severity_rationale: >
      The form itself does not require what the criterion expects; the
      design-gap affects 100% of recertification packets, not just the four
      sampled. Pattern, not operating miss. Customer impact none-identified
      directly; regulatory exposure on access-privileges control design.
    root_cause_hypothesis:
      category: process
      description: >
        Recertification form template does not include per-entitlement
        attestation column. Reviewers cannot per-entitlement-attest because
        the form does not capture it.
    repeat_issue: false
    prior_issue_id: null
    disposition: elevated-to-issue
    disposition_rationale: >
      Design problem; remediation is form redesign and reviewer training,
      not a one-off correction.
    issue_handoff:
      criterion: NYDFS 23 NYCRR §500.7(a)(2); firm IAM Policy v3.4 §4.2
      condition: >
        Recertification form does not require per-entitlement attestation;
        four sampled packets in 2026-Q1 carry blanket "approved" responses,
        and the form design pattern affects 100% of packets across in-scope
        systems.
      cause: >
        Recertification form template lacks per-entitlement attestation
        column; reviewer workflow does not surface entitlements individually.
      effect: >
        Per-entitlement attestation is not occurring across the in-scope
        recertification population; access-privileges control design does
        not satisfy the rule and the firm's own policy.
      recommendation_seed: >
        Redesign recertification form to require per-entitlement attestation;
        retrain reviewer population; re-run a sample of 2026-Q1 packets
        with the new form to confirm the design-gap is closed.
      rollup_grouping: ISS-2026-Q1-IAM-Recert-design

  - exception_id: X2
    sample_id: S05, S21
    population_reference: standard-entitlement packets
    criterion_source: firm IAM Policy v3.4 §4.4 (30-day completion deadline)
    condition: >
      On two sampled packets, completion timestamp was 34 and 41 days after
      the packet was issued, exceeding the policy-stated 30-day deadline.
    classification: control-failure
    severity: medium
    severity_rationale: >
      Two of thirty (above tolerable). One-off at the entity level (no
      prior-cycle pattern identified). Compensating control (escalation at
      day 28) operated for one packet and did not for the other.
    root_cause_hypothesis:
      category: people
      description: >
        Reviewer-population coverage during the quarter; two of the late
        packets sat with reviewers who were on extended leave with no
        documented delegation.
    repeat_issue: false
    prior_issue_id: null
    disposition: elevated-to-issue
    disposition_rationale: >
      Pattern enough to elevate; remediation is on the delegation policy,
      not on the recertification control itself.
    issue_handoff:
      criterion: firm IAM Policy v3.4 §4.4
      condition: >
        Two 2026-Q1 recertification packets completed 4 and 11 days past
        the policy-stated 30-day deadline; both packets sat with reviewers
        on extended leave without documented delegation.
      cause: >
        Delegation procedure for reviewer-extended-leave does not require
        explicit IAM-recertification delegation; the day-28 escalation
        triggers but does not auto-reassign.
      effect: >
        Recertification timing exposure on standard entitlements during
        extended-leave windows; pattern likely reflects in any quarter
        where reviewers are on leave without delegation.
      recommendation_seed: >
        Extend reviewer-leave delegation procedure to require explicit
        IAM-recertification reassignment; add auto-reassignment logic to
        the day-28 escalation.

  - exception_id: X3
    sample_id: S08
    population_reference: privileged-entitlement packets
    criterion_source: NYDFS 23 NYCRR §500.7(a)(3) (privileged access); firm IAM Policy v3.4 §5.2 (privileged-access policy floor)
    condition: >
      On one sampled privileged-access packet, the recertification recorded
      removal of "Production-Database-Admin" entitlement for user-role-A
      effective 2026-02-15. The IAM system shows the entitlement is still
      active for that user-role as of testing date 2026-04-15.
    classification: control-failure
    severity: critical
    severity_rationale: >
      Privileged access. Firm policy floor: all privileged-access deviations
      open at critical. Repeat-issue: a similar un-revoked privileged-access
      pattern was found in 2025-Q3 (issue ISS-2025-Q3-IAM-04, status open as
      of 2026-04-15). Customer impact none-identified directly; regulatory
      exposure on privileged-access control operation is direct and high.
      Compensating control (privileged-access activity monitoring) did not
      surface the unauthorized persistence.
    root_cause_hypothesis:
      category: technology
      description: >
        IAM system entitlement-removal workflow does not auto-execute on
        recertification-decision-to-remove; removal requires a separate
        manual ticket that did not get filed for this packet.
    repeat_issue: true
    prior_issue_id: ISS-2025-Q3-IAM-04
    disposition: elevated-to-issue
    disposition_rationale: >
      Critical severity, repeat issue, privileged access. Immediate
      elevation; the prior issue's remediation (auto-execution from
      recertification decision) was scheduled for 2026-Q1 and did not land.
    issue_handoff:
      criterion: NYDFS 23 NYCRR §500.7(a)(3); firm IAM Policy v3.4 §5.2
      condition: >
        Production-Database-Admin entitlement marked for removal on
        2026-02-15 recertification packet; entitlement still active in
        IAM system as of 2026-04-15. Repeat pattern from 2025-Q3
        (ISS-2025-Q3-IAM-04, open).
      cause: >
        IAM entitlement-removal workflow requires separate manual ticket
        after recertification decision; auto-execution from recertification
        decision was scheduled for 2026-Q1 and did not land.
      effect: >
        Privileged production-database access persisted unauthorized for
        eight weeks; activity monitoring did not flag. Pattern likely
        affects every recertification-decision-to-remove until the
        auto-execution lands.
      recommendation_seed: >
        Accelerate the auto-execution-from-recertification-decision delivery;
        in the interim, add a 7-day post-recertification reconciliation
        between recertification decisions and IAM-system state, with
        exceptions auto-paged to IAM operations.
      rollup_grouping: ISS-2026-Q1-IAM-Recert-privileged-critical

  - exception_id: X4
    sample_id: S15
    population_reference: standard-entitlement packets
    criterion_source: firm IAM Policy v3.4 §4.6 (HR-IAM offboarding feed)
    condition: >
      On one sampled packet, the user under recertification was no longer
      employed at the entity as of 2025-12-20 (HR offboarding date). The
      IAM system still provisioned the user's standard entitlements as of
      packet issuance 2026-02-01 and as of testing 2026-04-15.
    classification: data-integrity
    severity: high
    severity_rationale: >
      Pattern indicator on the HR-IAM offboarding feed; even one terminated-
      employee with active access is a heightened-severity finding under the
      firm policy. Customer impact none-identified directly; regulatory
      exposure on access-privileges control reliability.
    root_cause_hypothesis:
      category: governance
      description: >
        HR-IAM offboarding feed has a known lag pattern; the feed cadence
        and the offboarding ticket-cutoff windows do not align. Root cause
        spans HR offboarding procedure and IAM provisioning workflow.
    repeat_issue: false
    prior_issue_id: null
    disposition: elevated-to-issue
    disposition_rationale: >
      Single instance but the data-integrity gap on the offboarding feed
      suggests a population-level exposure the sample did not size for.
      Elevate; expanded-sample procedure to size the population belongs
      with the issue remediation, not with this register.
    issue_handoff:
      criterion: firm IAM Policy v3.4 §4.6
      condition: >
        Terminated employee (HR offboarding 2025-12-20) carried active
        IAM entitlements through to testing date 2026-04-15.
      cause: >
        HR-IAM offboarding feed lag pattern; the feed cadence and HR
        ticket-cutoff windows do not align.
      effect: >
        Terminated-employee access exposure on standard entitlements;
        pattern affects an unknown population pending expanded sampling.
      recommendation_seed: >
        Accelerate HR-IAM offboarding feed to event-driven from batch;
        in the interim, run a daily reconciliation between HR-system
        terminated-employee list and IAM-active-user list with exceptions
        auto-paged.

aggregation:
  deviation_rate_observed: 0.27
  tolerable_deviation_rate: 0.05
  anomaly_or_systemic: systemic
  projection_commentary: >
    The design-gap finding (X1) affects 100% of recertification packets in
    the in-scope population, not the four sampled. The privileged-access
    deviation (X3) is at zero-tolerable and represents a repeat pattern. The
    timing deviations (X2) reflect a delegation-procedure gap that affects
    extended-leave windows and is likely to recur. The data-integrity
    deviation (X4) suggests an HR-IAM-feed exposure the sample did not size
    for; expanded sampling belongs with the issue remediation.
  stratum_breakdown:
    - stratum_label: standard-entitlement packets
      sample_size: 26
      deviations_observed: 7
      deviation_rate: 0.27
      tolerable: 0.05
      notes: design-gap, timing, and data-integrity findings cluster here
    - stratum_label: privileged-entitlement packets
      sample_size: 4
      deviations_observed: 1
      deviation_rate: 0.25
      tolerable: 0.00
      notes: zero-tolerable; one critical-severity un-revoked-privileged finding

reviewer_questions:
  - >
    Whether the design-gap (X1) and the timing-failure (X2) roll up into a
    single recertification-control issue or open as separate issues; the
    remediation tracks differ but the underlying control set is the same.
  - >
    Whether the privileged-access critical (X3) escalates to the cyber
    steering committee in addition to the standard issue ladder, given the
    repeat-issue posture.
  - >
    Whether the HR-IAM-feed data-integrity finding (X4) drives a separate
    expanded-sample procedure ahead of the issue write-up, or whether the
    sizing belongs in the issue's remediation plan.

confidence_label: high
human_review_required: true
```

#### Why the register shape matters downstream

- `workpaper-drafter` reads this register by `exception_register_id` and pulls the disposition summary, the design-gap projection commentary (100% of packets), and the privileged-access policy-floor classification into the workpaper's conclusion section.
- `issue-writeup` keys off `source_exception_id` for X1, X2, X3, and X4. The writer for X3 inherits the repeat-issue flag and the prior-issue link automatically; the matter-requiring-attention / matter-requiring-immediate-attention classification field on the issue schema reads "n/a" because the source is internal testing, not an examiner letter.
- The cyber overlay's evidence-gap-versus-control-failure disambiguation drove X3's classification: the IAM system showing the entitlement still active is corroborating evidence that the control did not operate, so it cannot be an evidence-gap.
- The firm policy floor on privileged access overrode what the underlying severity calibration would have produced; the severity rationale field carries the override explicitly.
- The reviewer questions route the right items to the right decision-makers (cyber steering committee, IAM operations, head of cyber risk testing).

## reg-e-error-resolution-bank

### Example: Reg E error-resolution exception classification at a regional bank

#### Input

A regional bank's compliance-testing function has finished a quarterly Reg E error-resolution test (12 CFR 1005.11, Subpart A) on a sample of 50 customer-disputed transactions from the period 2026-01-01 to 2026-03-31. The workpaper-drafter output (`WP-2026-Q1-RegE-04`) carries the sample-level results and surfaces six deviations. The exception-analysis skill is called to classify them, rank severity, set disposition, and build the handoff to issue write-up.

The six raw deviations from the workpaper:

- Three sample items where provisional credit was issued more than 10 business days after the dispute was filed (the rule's deadline).
- Two sample items with no investigation notes in the case-management file but with system-logged status changes showing investigation activity.
- One sample item where the fee-reversal amount in the case-management system disagreed with the fee-reversal amount in the core deposit ledger.

The test plan's tolerable deviation rate was set at 5%. Source posture is public-plus-firm-policy-plus-evidence. The scope flags banking sector and conduct cross-cutting overlays. The current cycle is the third consecutive Reg E test; the prior two cycles also surfaced timing deviations on online disputes.

#### Why this scenario matters

This is the canonical consumer-compliance use of exception-analysis. It exercises three of the six classifications (`control-failure`, `evidence-gap`, `data-integrity`), the conduct-overlay severity calibration shift for consumer-harm framing, the repeat-issue flag pattern, the aggregation-and-projection logic against a tolerable rate the test plan set, and the handoff-package population for `issue-writeup`. The example also tests the disposition split: not every deviation elevates; one of the evidence-gap items closes at exception level after supplemental evidence is reviewed.

#### Output sketch

```yaml
exception_register_id: EX-2026-Q1-RegE-04
test_id: TP-2026-Q1-RegE-04
workpaper_id: WP-2026-Q1-RegE-04
control_id: CTL-RegE-PROVCRED-01
obligation_ids: [OBL-RegE-1005.11, OBL-firm-DepositOps-DisputePolicy-v6.2]
engagement_id: ENG-2026-CMS-RegE-Q1
period_start: 2026-01-01
period_end: 2026-03-31
business_unit: Deposit Operations: Disputes
jurisdictions: [US-federal, multi-state]
source_posture: public-plus-firm-policy-plus-evidence
scope_statement: >
  Quarterly Reg E error-resolution test for the period 2026-Q1. Population is
  customer-disputed transactions where the bank's investigation deadline fell
  inside the period. Excludes commercial accounts (out of Reg E scope).
preparer: {role: compliance-testing analyst, date: 2026-04-22}
reviewer: {role: compliance-testing manager, date: }

exceptions:
  - exception_id: X1
    sample_id: S07
    population_reference: online-channel disputes
    criterion_source: 12 CFR 1005.11(c)(2) provisional credit deadline; references/source-anchors.md#cfpb
    condition: >
      On three sampled disputes filed via online channel between 2026-01-09
      and 2026-02-14, provisional credit was issued 12, 13, and 15 business
      days after the dispute was filed, exceeding the 10-business-day
      regulatory deadline.
    classification: control-failure
    severity: high
    severity_rationale: >
      Recurring (third consecutive cycle on online channel). Customer impact
      identifiable (customers without provisional credit during the gap
      window). Regulatory exposure is direct rule-deadline violation.
      Compensating controls (manual review queue) did not catch.
    root_cause_hypothesis:
      category: technology
      description: >
        SLA monitor on the dispute-routing queue does not page when online
        channel volume spikes into the third business day; the page logic
        keys off branch-channel volume only.
    repeat_issue: true
    prior_issue_id: ISS-2025-Q4-RegE-02
    disposition: elevated-to-issue
    disposition_rationale: >
      Pattern, not isolated. Severity high. Repeat issue with prior issue still
      open as of 2026-04-15.
    issue_handoff:
      criterion: 12 CFR 1005.11(c)(2)
      condition: >
        On three online-channel disputes in 2026-Q1, provisional credit was
        issued 12-15 business days after dispute filing, exceeding the
        10-business-day deadline.
      cause: >
        Dispute-routing-queue SLA monitor does not page on online-channel
        volume; the page logic is branch-channel-only.
      effect: >
        Three identifiable customers without provisional credit during a
        2-5 business-day gap window in 2026-Q1; pattern recurring across
        three consecutive cycles. Customer-side remediation (back-dated
        provisional-credit equivalent) needed.
      recommendation_seed: >
        Extend dispute-routing-queue SLA monitor page logic to include
        online-channel volume on the same trigger thresholds as branch
        channel; verify with two-cycle observation period.
      rollup_grouping: ISS-2026-Q1-RegE-timing-rollup

  - exception_id: X2
    sample_id: S14
    population_reference: branch-channel disputes
    criterion_source: 12 CFR 1005.11(c) investigation requirement; firm Dispute Investigation Policy v6.2 §3.1
    condition: >
      On two sampled disputes (S14 and S22) the case-management file did not
      carry investigation notes, but the system audit log showed investigator
      status changes (assigned, in-progress, resolved) consistent with
      investigation activity.
    classification: evidence-gap
    severity: medium
    severity_rationale: >
      System log corroborates the investigation occurred. Frequency moderate
      (two of fifty). Customer impact not identified (the disputes were
      resolved with appropriate consumer-side outcome). Regulatory exposure
      is documentation, not control operation.
    root_cause_hypothesis:
      category: people
      description: >
        Case-management training does not require notes capture before status
        change; the system permits status change without note entry.
    repeat_issue: false
    prior_issue_id: null
    disposition: closed-at-exception
    disposition_rationale: >
      Supplemental evidence (system audit log) reviewed and confirms
      investigation activity. One of the two flagged for re-test next cycle
      to verify the documentation behaviour shifts after the training
      addressed in the related X3 disposition.

  - exception_id: X3
    sample_id: S22
    population_reference: branch-channel disputes
    criterion_source: 12 CFR 1005.11(c) investigation requirement; firm Dispute Investigation Policy v6.2 §3.1
    condition: >
      Same condition pattern as X2 on a different sample item.
    classification: evidence-gap
    severity: medium
    severity_rationale: >
      Same as X2.
    root_cause_hypothesis:
      category: process
      description: >
        Case-management workflow does not enforce notes-before-status-change.
    repeat_issue: false
    prior_issue_id: null
    disposition: re-test-required
    disposition_rationale: >
      Re-test next cycle to verify documentation behaviour after workflow
      enhancement scheduled for 2026-Q2 lands.

  - exception_id: X4
    sample_id: S31
    population_reference: branch-channel disputes
    criterion_source: 12 CFR 1005.11(c)(1) error correction; firm Reconciliation Policy v4.0 §2.4
    condition: >
      On one sampled dispute, the fee-reversal amount in the case-management
      system was $25.00 and the fee-reversal amount in the core deposit
      ledger was $35.00. The customer received the $35.00 reversal; the
      case-management record was not updated.
    classification: data-integrity
    severity: medium
    severity_rationale: >
      Single instance. Customer impact resolved (customer received the larger
      reversal). Regulatory exposure on case-management record reliability.
      Reconciliation between case-management system and core ledger is a
      named control under firm policy.
    root_cause_hypothesis:
      category: data
      description: >
        Reconciliation between dispute case-management system and core
        deposit ledger is daily-batch; manual fee-reversal adjustments made
        in core ledger after the batch window do not flow back to case
        management.
    repeat_issue: false
    prior_issue_id: null
    disposition: elevated-to-issue
    disposition_rationale: >
      Single instance but the data-integrity gap suggests a population the
      sample did not size for. Elevate for issue tracking; remediation is
      structural.
    issue_handoff:
      criterion: 12 CFR 1005.11(c)(1); firm Reconciliation Policy v4.0 §2.4
      condition: >
        Case-management fee-reversal record disagrees with core ledger
        on at least one 2026-Q1 sample item; the discrepancy was not
        surfaced by the daily reconciliation batch.
      cause: >
        Daily-batch reconciliation between dispute case-management system
        and core deposit ledger does not capture late-window manual
        adjustments in core ledger.
      effect: >
        Case-management record unreliable as system-of-record for dispute
        outcomes; downstream reporting (Reg E error-resolution metrics
        used in board reporting) reads off case management.
      recommendation_seed: >
        Extend reconciliation cadence to capture late-window adjustments,
        or add a back-feed from core ledger fee-reversal events to case
        management.
      rollup_grouping: ISS-2026-Q1-RegE-data-integrity

aggregation:
  deviation_rate_observed: 0.12
  tolerable_deviation_rate: 0.05
  anomaly_or_systemic: systemic
  projection_commentary: >
    Timing deviations concentrate in online channel (three of three). The
    online-channel deviation rate is 16% (three of nineteen online-channel
    samples). Branch-channel deviation rate is 6% (three of thirty-one
    branch-channel samples), which is also above tolerable but the rate
    reflects two evidence-gap items closed at exception. The data-integrity
    deviation suggests a separate population the sample did not size for;
    expanded sampling on the case-management-versus-core-ledger
    reconciliation may be warranted.
  stratum_breakdown:
    - stratum_label: online-channel disputes
      sample_size: 19
      deviations_observed: 3
      deviation_rate: 0.16
      tolerable: 0.05
      notes: timing-rule deviations clustered here; root cause is online-channel SLA monitor
    - stratum_label: branch-channel disputes
      sample_size: 31
      deviations_observed: 3
      deviation_rate: 0.10
      tolerable: 0.05
      notes: two evidence-gap items closed at exception; one data-integrity item elevated

reviewer_questions:
  - >
    Whether the timing-failure root cause (online-channel SLA monitor)
    warrants its own issue separate from the documentation-gap issue, or
    whether they share an issue under the dispute-handling control set.
  - >
    Whether the data-integrity deviation should drive an expanded-sample
    procedure on the reconciliation control before the issue write-up
    proceeds, or whether the elevation can carry forward at single-sample
    confidence.
  - >
    Whether the consumer-side remediation track (back-dated provisional-
    credit equivalent for the three timing-deviation customers) is in scope
    of this engagement or routes to the consumer-remediation function as a
    separate handoff.

confidence_label: high
human_review_required: true
```

#### Why the register shape matters downstream

- `workpaper-drafter` reads this register by `exception_register_id` and pulls the disposition summary into the workpaper's exceptions-identified section without re-classifying.
- `issue-writeup` keys off `source_exception_id` for X1 and X4 and consumes the populated handoff packages directly; the writer refines the recommendation seed but does not re-discover criterion, condition, cause, or effect.
- The conduct cross-cutting overlay shaped X1's severity calibration (consumer-harm read pushed severity from medium to high on the timing pattern).
- The repeat-issue flag on X1 routes to the issue log to link to the prior open issue, so the issue writer can decide whether to extend the existing issue or open a fresh one with linkage.
- Reviewer questions cluster the items the testing manager and the compliance manager need to decide before sign-off; the open question on consumer-side remediation routes the right item to the right function.

## troubleshooting

### Troubleshooting: exception-analysis

Recurring defects in exception registers and the pattern that catches them.

#### 1. Treating every deviation as a finding

Symptom: every row in the register reads `control-failure` or `design-gap`; nothing classifies as `evidence-gap` or `anomaly`; disposition is uniformly `elevated-to-issue`.

Why it goes wrong: the preparer is collapsing classification into "exception" because the test plan called the deviation an exception. Six buckets exist for a reason; not every deviation is a control-side problem.

Catch it: if classification is uniform across the register, walk three rows back through the criterion and the condition. Ask: did the system do the right thing and just fail to record it (`evidence-gap`)? Did the test surface a one-off with positive evidence it does not recur (`anomaly`)? Did the tester and control owner read the criterion differently (`scope-disagreement`)? If the answers are all "no" across the register, the uniformity is real; if any answer is "yes" on a row, reclassify.

#### 2. Confusing evidence gap with control failure

Symptom: a row classifies as `control-failure` but the condition reads "no evidence in the file" without a corroborating-system check; or a row classifies as `evidence-gap` but no corroborating evidence is named.

Why it goes wrong: the disambiguation between evidence-gap and control-failure is the most common classification error. Evidence-gap is "the system did the right thing, the file does not record it"; control-failure is "the system did not do the right thing." The disambiguation requires a corroborating-system check.

Catch it: every `evidence-gap` row names the corroborating evidence (system audit log, downstream system state, attestation, alternative record). Every `control-failure` row that hinges on absent documentation names what corroborating system was checked and showed no record. If neither side names the corroboration, the classification is not yet defensible.

The cyber overlay carries the disambiguation pattern in detail; load it for cyber populations.

#### 3. Skipping root-cause hypothesis

Symptom: `root_cause_hypothesis.description` reads "human error", "training gap", "system limitation", or is blank.

Why it goes wrong: surface labels do not name the control attribute that failed. The downstream issue write-up needs the cause field populated with a specific weakness; without it, the recommendation seed cannot land and the issue is unactionable.

Catch it: read the description aloud. Does it name what specifically failed at the design or operation level? "Reviewer-leave delegation procedure does not require IAM-recertification reassignment" passes. "Training gap" does not. Where the root cause is genuinely unknown, the field reads "root cause analysis pending" with an open action; do not invent a cause to fill the field, but do not let "human error" stand as the cause either.

#### 4. Projecting anomalies

Symptom: a row classifies as `anomaly` without positive evidence the deviation does not recur; or the aggregation reads `anomaly` because the sample size felt small.

Why it goes wrong: AICPA AU-C 530 [verify §A22 in the current edition] makes the methodology bar explicit: a deviation can be an anomaly only when there is positive evidence it is non-recurring. Default is systemic; downgrade to anomaly demands evidence, not intuition.

Catch it: any `anomaly` classification or any `aggregation.anomaly_or_systemic = anomaly` carries a named-evidence sentence in the description or the projection commentary. "Sample of one, treating as anomaly" is not evidence. "The condition arose from a one-time data-load event on a date the firm independently verified, with corroborating logs showing the event did not recur in the period" is evidence.

#### 5. Severity inflation by the first-line owner

Symptom: severity is uniformly high or critical across the register; severity rationale fields are sparse; the preparer notes "owner self-rated as critical".

Why it goes wrong: first-line owners sometimes self-identify high or critical to pre-empt examiner attention, on the theory that an aggressively self-rated finding looks better than a regulator-rated one. The pattern distorts the population view, fills the issue ladder with mis-prioritised items, and burns reviewer attention.

Catch it: severity rationale references the firm's published thresholds (where they exist), frequency, customer impact, regulatory exposure, and compensating controls. If the rationale is one sentence and the severity is critical, the rating is not yet defensible. Push back to the calibration rubric in `references/firm-overlay.md` (firm-installed) or to the AU-C 265 deficiency / significant-deficiency / material-weakness severity hierarchy.

The exception works the other way too: severity deflation by first-line owners ("we'll just call it a low and close it") happens; the same rationale-field discipline catches it.

#### 6. Empty handoff packages

Symptom: rows with disposition `elevated-to-issue` have empty or sparse `issue_handoff` fields; the issue writer downstream re-discovers criterion, condition, cause, effect, and recommendation seed from the workpaper.

Why it goes wrong: the whole point of the handoff is to make `issue-writeup` not re-discover work. An empty handoff package means the issue writer reads the workpaper from scratch; the integration between the two skills loses its value.

Catch it: every `elevated-to-issue` row has all five handoff fields populated (criterion, condition, cause, effect, recommendation seed) before the register is signed off. The reviewer's last check before sign-off is the handoff completeness; an empty package is a sign-off blocker.

The recommendation seed is declarative ("redesign recertification form to require per-entitlement attestation"), not interrogative ("consider whether the form should be redesigned"). The issue writer refines the seed but should not have to invent it.

#### 7. Aggregation read against the wrong tolerable rate

Symptom: aggregation commentary reads against a tolerable rate that does not match the test plan; or aggregation commentary invents a tolerable rate the test plan did not set.

Why it goes wrong: the tolerable deviation rate is set in `test-plan-builder` for a reason. Inventing or substituting it in the register undermines the sample design and produces an unsupportable projection.

Catch it: the tolerable rate in `aggregation.tolerable_deviation_rate` is pulled from the test plan by `test_id`. If the test plan did not set one, that is a test-plan defect to flag back, not a number to invent here. The aggregation commentary then reads "tolerable rate not set in the test plan; flagging back to test-plan-builder for amendment".

#### 8. Mixing register voice with legal-conclusion voice

Symptom: the register concludes that "the firm violated Reg X" or "the entity is non-compliant with §Y".

Why it goes wrong: the register concludes on control effectiveness and exception classification, not on legal violation. Legal-violation language is for legal counsel and regulator-led determinations.

Catch it: the register reads "the control did not operate as designed for the [population] during the period, the criterion being [rule with section]". The capital-markets sector overlay carries the language-hygiene pattern in detail because the surrounding enforcement environment makes the discipline particularly important there; the same pattern applies across sectors.

#### 9. Reviewer-separation breaks

Symptom: preparer and reviewer roles are the same; or the reviewer signs off without a separate role.

Why it goes wrong: reviewer separation is structural, not advisory. The same role cannot both classify and review classification.

Catch it: `preparer.role` and `reviewer.role` differ. Where the testing function is small and the same person fills two roles, the separation is on role label and on review responsibility, not on body, but the register's audit trail records the separate sign-off explicitly.

#### 10. Repeat-issue flag false-negative

Symptom: a row classifies a deviation that is the third consecutive cycle of the same condition without flagging `repeat_issue: true`.

Why it goes wrong: the issue log was not checked before classification. Repeat exceptions are different severity and different issue-writeup handoff; missing the repeat-issue flag mis-sets both.

Catch it: before sign-off, every row's condition and root-cause hypothesis is searched against the issue log for the same control or population. Where the search returns a prior open or recently closed issue, the repeat-issue flag is on and `prior_issue_id` is populated. Where the search returns nothing, the flag is off but the search itself is documented in the limitations-and-reliance field so the reviewer can see the check happened.
