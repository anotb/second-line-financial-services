# Cross-cutting overlay: cyber

Loads when `cross_cutting_overlay_set` includes `cyber`. Default-on for any control test touching IAM, data-protection, or supervisory-rule-mandated security areas. Carries the disambiguation pattern between evidence gap and control failure for cyber controls (the distinction matters more here than in most populations because cyber evidence is often log-based).

## The evidence-gap-versus-control-failure disambiguation

Cyber control testing surfaces a recurring classification problem: the absence of a log entry can mean either the control did not operate (control-failure) or the control operated but did not log (evidence-gap). The disambiguation matters because severity, root-cause hypothesis, and remediation differ.

The disambiguation pattern:

- If a corroborating system shows the control operated (a downstream system reflects the action, a different log captures the same event, an attestation exists), classify as `evidence-gap`. The remediation is logging or documentation, not control redesign.
- If no corroborating system shows the control operated and the testing inquiry of the control owner cannot point to where else the action would be visible, classify as `control-failure`. Default to control-failure when corroborating evidence is genuinely absent; do not let "the system probably did it" close out the exception.
- If the corroborating system itself is in scope of the test and is also missing the entry, classify as `data-integrity` and route the root cause toward the upstream feed, the system clock, or the log-retention configuration.

NIST SP 800-53 control-effectiveness language is the methodology anchor; the control-effectiveness assessment turns on whether the control achieved its objective, not on whether it was logged. [verify the current SP 800-53 revision and the relevant control-family assessment-procedure references — typically AU-2, AU-6, AU-12 for the audit-and-accountability family.]

## IAM-recertification exception flavour

Quarterly or periodic access-recertification testing produces a distinctive set of exception patterns. The criterion is typically a NIST SP 800-53 AC-family control [verify revision], a NYDFS Part 500 §500.7 control (access privileges) [verify current section labels], a SOX-relevant ITGC, or the firm's IAM policy. The exception patterns:

- Blanket-approval deviations (the recertification packet has a single "approved" response covering all entitlements without per-entitlement attestation): classify as `design-gap` when the recertification form does not require per-entitlement attestation, and as `control-failure` when the form does require it but the reviewer bypassed it. Severity escalates when the population includes privileged entitlements.
- Timing deviations (recertification completed after the policy-stated deadline): classify as `control-failure`. Severity calibrates against the entitlement tier and the persistence of the timing miss.
- Un-revoked access (the recertification removed an entitlement but the IAM system still grants it): classify as `control-failure` with elevated severity, particularly for privileged access. Repeat-issue flag check is important; this pattern often recurs.
- Terminated-employee access (the user is no longer employed but the IAM system still grants access): classify as `data-integrity` because the root cause typically spans HR offboarding and IAM provisioning. Severity escalates with the entitlement tier and the time-since-termination.
- Service-account or shared-credential entries that the recertification did not reach: classify as `design-gap` (the recertification scope did not include service accounts) or `evidence-gap` (the scope did include them but the packet did not surface them).

## Incident-response control-effectiveness language

For tests scoped to incident-response controls (NYDFS Part 500 §500.16 [verify], SEC Item 1.05 of Form 8-K cyber-incident disclosure process [verify rule citation], firm IRP), exception classification reads against the documented IRP rather than the firm's intuition about what the response should look like.

- Detection-timing deviations (the incident was detected later than the IRP's expected detection time for that incident type) classify as `control-failure`. Severity calibration references the incident severity and the population of in-flight customers or systems during the detection window.
- Containment or eradication step deviations classify as `control-failure` against the IRP's named step.
- Notification deviations (regulator, customer, board, vendor notification timing or content) classify as `control-failure`; the criterion field cites the notification-rule section and the firm's notification policy.
- Post-incident-review absence or delay classifies as `evidence-gap` (the review happened but no artifact) or `control-failure` (the review did not happen). The remediation differs.

## Third-party security-policy exception patterns

NYDFS Part 500 §500.11 [verify], the interagency third-party-relationships guidance, and the firm's TPRM policy combine to set the criteria for vendor security testing. Exception classification reads against the vendor's risk tier and the firm's tier-specific control expectation.

- Missing SOC 2 Type II report for a critical-tier vendor: `control-failure` at the firm's TPRM monitoring control, severity calibrated against vendor criticality and the time-since-expected-report.
- SOC 2 qualified opinion not assessed by the firm: `control-failure` at the firm's SOC-review control. Severity escalates when the qualification touches a control the firm relies on.
- Vendor incident not reported within the contractual window: classify against the firm's vendor-monitoring control (the firm's control is to detect / receive the report; the vendor's control is to issue it).

## Source posture limits on cyber exception detail

Cyber exception detail can carry information that would help an attacker. Where source posture is anything other than firm-restricted-or-tighter, redact specific system names, control configurations, and detection thresholds from the register body; carry them in the structured record at the appropriate confidentiality posture and pull into a higher-posture artifact when needed.
