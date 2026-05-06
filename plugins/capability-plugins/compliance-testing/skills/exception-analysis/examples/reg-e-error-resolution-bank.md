# Example: Reg E error-resolution exception classification at a regional bank

## Input

A regional bank's compliance-testing function has finished a quarterly Reg E error-resolution test (12 CFR 1005.11, Subpart A) on a sample of 50 customer-disputed transactions from the period 2026-01-01 to 2026-03-31. The workpaper-drafter output (`WP-2026-Q1-RegE-04`) carries the sample-level results and surfaces six deviations. The exception-analysis skill is called to classify them, rank severity, set disposition, and build the handoff to issue write-up.

The six raw deviations from the workpaper:

- Three sample items where provisional credit was issued more than 10 business days after the dispute was filed (the rule's deadline).
- Two sample items with no investigation notes in the case-management file but with system-logged status changes showing investigation activity.
- One sample item where the fee-reversal amount in the case-management system disagreed with the fee-reversal amount in the core deposit ledger.

The test plan's tolerable deviation rate was set at 5%. Source posture is public-plus-firm-policy-plus-evidence. The engagement scope flags banking sector and conduct cross-cutting overlays. The current cycle is the third consecutive Reg E test; the prior two cycles also surfaced timing deviations on online disputes.

## Why this scenario matters

This is the canonical consumer-compliance use of exception-analysis. It exercises three of the six classifications (`control-failure`, `evidence-gap`, `data-integrity`), the conduct-overlay severity calibration shift for consumer-harm framing, the repeat-issue flag pattern, the aggregation-and-projection logic against a tolerable rate the test plan set, and the handoff-package population for `risk-compliance-core/skills/issue-writeup`. The example also tests the disposition split: not every deviation elevates; one of the evidence-gap items closes at exception level after supplemental evidence is reviewed.

## Output sketch

```yaml
analysis_id: EX-2026-Q1-RegE-04
test_id: TP-2026-Q1-RegE-04
workpaper_id: WP-2026-Q1-RegE-04
control_id: CTL-RegE-PROVCRED-01
obligation_ids: [OBL-RegE-1005.11, OBL-firm-DepositOps-DisputePolicy-v6.2]
engagement_id: ENG-2026-CMS-RegE-Q1
period_start: 2026-01-01
period_end: 2026-03-31
business_unit: Deposit Operations — Disputes
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

## Why the register shape matters downstream

- `workpaper-drafter` reads this register by `analysis_id` and pulls the disposition summary into the workpaper's exceptions-identified section without re-classifying.
- `risk-compliance-core/skills/issue-writeup` keys off `source_exception_id` for X1 and X4 and consumes the populated handoff packages directly; the writer refines the recommendation seed but does not re-discover criterion, condition, cause, or effect.
- The conduct cross-cutting overlay shaped X1's severity calibration (consumer-harm read pushed severity from medium to high on the timing pattern).
- The repeat-issue flag on X1 routes to the issue log to link to the prior open issue, so the issue writer can decide whether to extend the existing issue or open a fresh one with linkage.
- Reviewer questions cluster the items the testing manager and the compliance manager need to decide before sign-off; the open question on consumer-side remediation routes the right item to the right function.
