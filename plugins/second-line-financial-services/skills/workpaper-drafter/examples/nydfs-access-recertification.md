# Example: NYDFS Part 500 access-recertification workpaper for second-line cyber testing

Public-source-derived. No named institution. The shape mirrors a quarterly access-recertification control test at a NYDFS Covered Entity.

## Input

- **Test cycle**: quarterly access-recertification control test for Q1, drafting the workpaper from completed fieldwork.
- **Test plan reference**: pre-fieldwork test plan (test ID `TP-CYB-AR-2026-Q1`) identifies the population (recertification packets due in the quarter), sample size (30 packets, stratified by privilege tier — 10 standard, 10 privileged, 10 service-account), and procedures (per-packet attestation reperformance, IAM-system reperformance for revocations, HR-IAM feed reconciliation for terminated employees).
- **Engagement scope supplied**: institution = NY-licensed bank; primary regulators = NYDFS, FRB, CFPB; persona = head of cyber risk, with the cyber-risk committee as the deliverable consumer and the §500.17(b) annual certification process as the downstream dependency; source posture = public-plus-firm-policy-plus-evidence; sector overlay = banking; cross-cutting overlays = cyber (default-on for Part 500 Covered Entity).
- **Exception register supplied**: from `exception-analysis`, exception_register_id `ER-CYB-AR-2026-Q1`. Eight classified exceptions: one design exception (the attestation form supports blanket per-system approval rather than per-entitlement attestation), two operating exceptions on attestation timing (timing, medium), one critical operating exception on un-revoked privileged access for a transferred employee (operating, critical), one data-integrity exception on a terminated employee retaining access for fourteen days post-termination due to an HR-IAM feed lag (data-integrity, high), three documentation gaps (attestation packets missing reviewer acknowledgement; documentation, low).
- **Test plan tolerable rate**: 5% standard population, 0% privileged population, set per firm policy and aligned to NYDFS 23 NYCRR §500.7 [verify subsection] expectations on privileged-access governance.

## Output sketch

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

## Why this scenario matters

- **Boundary check on design-versus-operating separation**: the design exception on the form is distinct from operating exceptions on form usage; the workpaper conclusion separates the two reads.
- **Boundary check on tolerable-rate framing**: the privileged sub-population tolerable rate is zero; the workpaper aggregation reads severity-driven rather than rate-driven.
- **Boundary check on repeat-issue handling**: the un-revoked privileged-access exception is a repeat issue from a prior cycle; the workpaper flags it for the issue-writeup handoff with the prior issue ID referenced.
- **Boundary check on §500.17(b) certification posture**: the workpaper does not certify; it surfaces the design gap as a reviewer question for the senior officer who certifies.
- **Boundary check on cyber overlay defaults**: the conduct overlay is not loaded (this is a cyber-control test, no consumer-facing dimension); the privacy overlay is not loaded (no GLBA Safeguards or HIPAA scope in the test plan).

## Anchors

- NYDFS 23 NYCRR Part 500.7, §500.17(b).
- AICPA AU-C 230 (Audit Documentation).
- AICPA AU-C 530 (Audit Sampling).
- FFIEC IT Examination Handbook, Information Security booklet.
- NIST SP 800-53A Rev. 5 (control-test documentation conventions).

See `references/source-anchors.md` and `references/cross-cutting/cyber.md` for full citations.
