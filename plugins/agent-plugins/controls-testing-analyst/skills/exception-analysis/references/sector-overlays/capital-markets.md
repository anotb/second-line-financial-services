# Sector overlay: capital-markets

Loads when `sector_overlay_set` includes `capital-markets`. Carries supervision-rule exception treatment for broker-dealer and investment-adviser testing, and enforcement-style language hygiene.

## Broker-dealer supervision exception treatment

Broker-dealer testing operates against FINRA supervision rules: FINRA Rule 3110 (supervision), Rule 3120 (supervisory control system), Rule 3130 (annual certification of compliance and supervisory processes). [verify the current rule text; FINRA periodically issues regulatory notices that update the supervisory expectations.]

What this means for the register:

- A supervisory-review deviation (sales-practice review, communications review, OBA / outside-business-activity attestation) reads as `control-failure` or `design-gap` depending on whether the review process exists but missed the item (`control-failure`) or the supervisory system itself does not require the review the criterion expects (`design-gap`).
- A trade-surveillance alert that was not adjudicated within the firm's documented timeframe reads as `control-failure`, severity scales with the alert tier and the volume of unadjudicated alerts.
- An annual-certification gap (Rule 3130) reads as `design-gap` if the certification process itself does not address the criterion the test surfaced; reads as `evidence-gap` if the process did address it but the artifact does not show it.

## Investment-adviser compliance-program exception treatment

Adviser testing operates against the Advisers Act compliance-program rule (Rule 206(4)-7) and the related code-of-ethics rule (Rule 204A-1). [verify rule citations and current SEC interpretive guidance.]

Classification calls:

- A compliance-program annual review deviation (no documented review, scope of review did not cover a material risk) reads as `design-gap` when the program design did not address the risk and as `control-failure` when the design did but the review missed it.
- A code-of-ethics violation (personal securities transaction not reported, late reporting, unapproved transaction) reads as `control-failure`; severity calibration references the access-person designation and the violation pattern.
- A custody-rule (Rule 206(4)-2) deviation reads with elevated severity because the custody framework itself is the supervisory bar; the criterion field cites the rule with a section reference.

## SEC EXAMS examination posture

SEC EXAMS deficiency letters and the related risk-alert publications shape what severity calibration the firm carries on testing exceptions in advance of a likely exam. [verify the current calendar-year EXAMS examination priorities and the risk-alert publications relevant to the firm's business model.]

Exception classification reads against EXAMS priorities:

- A deviation in an area called out in the current EXAMS priorities carries elevated severity rationale; the rationale field names the priority area.
- Repeat exceptions in priority areas raise the supervisory-finding-eligibility read meaningfully.

## Enforcement-style language hygiene

Capital-markets testing carries an additional discipline because the surrounding enforcement environment uses precise language for legal violations. The register concludes on control effectiveness and exception classification, not on legal violation. "The firm violated Rule X" is not register language; "the control did not operate as designed for the [population] during the period, the criterion being Rule X" is.

The handoff to issue write-up follows the same discipline: the recommendation seed names the control or process change, not the legal conclusion. Legal-violation determinations are for legal counsel and regulator-led proceedings, not for second-line testing artifacts.
