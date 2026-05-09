# Example: access-recertification exception classification under a state security rule

## Input

A second-line cyber-testing function at a state-licensed financial entity has run the quarterly logical-access-recertification control test on a sample of 30 recertification packets from the period 2026-01-01 to 2026-03-31. The criterion is the entity's IAM policy and the relevant state security-rule provision (the entity is in scope of NYDFS 23 NYCRR Part 500 §500.7 access-privileges) [verify current section labels]. The workpaper-drafter output (`WP-2026-Q1-IAM-Recert-02`) carries the sample-level results and surfaces eight deviations. The exception-analysis skill is called to classify them, rank severity, set disposition, and build the handoff to issue write-up.

The eight raw deviations from the workpaper:

- Four packets had blanket "approved" responses with no per-entitlement review captured.
- Two packets were completed after the policy-stated 30-day deadline.
- One privileged-access packet recorded an entitlement removal that was not actually revoked in the IAM system at the time of testing.
- One packet was for a user no longer employed at the entity (HR offboarded, IAM still provisioned).

The test plan's tolerable deviation rate was set at 5% on standard entitlements and 0% on privileged. Source posture is public-plus-firm-policy-plus-evidence. The scope flags capital-markets sector (the entity is a registered investment adviser) and cyber cross-cutting overlay. The privileged-access exception falls under the firm policy floor that all privileged-access deviations open at critical severity.

## Why this scenario matters

This is the canonical cyber-control-testing use of exception-analysis. It exercises four of the six classifications (`control-failure`, `design-gap`, `data-integrity`, with implicit `evidence-gap` discrimination), the policy-floor severity override for privileged access, the repeat-issue flag pattern, the population-projection commentary that the design-gap finding affects 100% of packets (not just sampled ones) because the design itself does not require per-entitlement attestation, and the cyber-overlay disambiguation pattern between control-failure and evidence-gap (the un-revoked-access exception is corroborated by the IAM system showing the entitlement still active, so it cannot be an evidence-gap).

## Output sketch

```yaml
analysis_id: EX-2026-Q1-IAM-Recert-02
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

## Why the register shape matters downstream

- `workpaper-drafter` reads this register by `analysis_id` and pulls the disposition summary, the design-gap projection commentary (100% of packets), and the privileged-access policy-floor classification into the workpaper's conclusion section.
- `risk-compliance-core/skills/issue-writeup` keys off `source_exception_id` for X1, X2, X3, and X4. The writer for X3 inherits the repeat-issue flag and the prior-issue link automatically; the matter-requiring-attention / matter-requiring-immediate-attention classification field on the issue schema reads "n/a" because the source is internal testing, not an examiner letter.
- The cyber overlay's evidence-gap-versus-control-failure disambiguation drove X3's classification: the IAM system showing the entitlement still active is corroborating evidence that the control did not operate, so it cannot be an evidence-gap.
- The firm policy floor on privileged access overrode what the underlying severity calibration would have produced; the severity rationale field carries the override explicitly.
- The reviewer questions route the right items to the right decision-makers (cyber steering committee, IAM operations, head of cyber risk testing).
