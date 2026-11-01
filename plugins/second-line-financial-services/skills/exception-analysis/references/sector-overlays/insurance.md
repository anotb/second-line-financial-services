# Sector overlay: insurance

Loads when `sector_overlay_set` includes `insurance`. Carries state-DOI market-conduct exception conventions and the model-audit-rule severity framing for ICFR-relevant findings.

## State DOI market-conduct exception conventions

State insurance departments examine market-conduct practices on a multi-state or single-state basis, working from the NAIC Market Regulation Handbook and state-specific examination procedures. [verify the current NAIC Market Regulation Handbook edition and the state-specific procedure references for the entity's domicile and material states.]

What this means for the register:

- Exception classification on market-conduct testing populations (claims handling timing, producer licensing, advertising compliance, complaint handling, underwriting discrimination, replacement-of-policy practices) reads against the NAIC handbook standards and the relevant state-specific timing rules.
- A claims-timing deviation reads as `control-failure` with the state-specific prompt-pay-rule deadline as the load-bearing fact.
- A producer-licensing deviation reads as `control-failure` or `data-integrity` depending on whether the producer was unlicensed in the state at the time of the transaction (control-failure) or the producer was licensed but the licensing record in the firm system was stale (data-integrity).
- A complaint-handling deviation that surfaces a UDAAP-analogue pattern (state insurance unfair-trade-practices acts) loads the conduct cross-cutting overlay; the severity rationale carries consumer-harm framing.

The handoff to issue write-up populates fields the firm's market-conduct response register consumes; severity calibration uses the firm's published thresholds where they exist and the state-specific examination procedure's severity hierarchy where they do not.

## NAIC Model Audit Rule severity framing for ICFR-relevant findings

Insurer ICFR-over-financial-reporting testing operates against the NAIC Model Audit Rule (Model #205) framework for insurers above the audit-exemption threshold. [verify Model #205 current revision date and the state adoption status for the entity's domicile.]

ICFR-relevant exception classification:

- A material-weakness candidate reads at `critical` severity. The severity rationale references both the dollar materiality threshold and the qualitative-materiality factors (regulatory exposure, ORSA-impact, board-reported figure exposure).
- A significant-deficiency candidate reads at `high` severity.
- A control-deficiency that is neither carries lower severity but the rationale still references the insurer's own materiality framework and the auditor's analogous evaluation under AU-C 265.

Where the test was scoped to support an ORSA filing or a Form B / Form F filing under the NAIC Insurance Holding Company System Regulatory Act, the criterion field cites the NAIC model and the state-specific adoption with a section reference. [verify the holding-company-act references for the entity's lead-state regulator.]

## Captive-insurer and reinsurance considerations

For captive insurers and reinsurance arrangements, the regulatory regime varies by domicile (Vermont, Bermuda, Cayman, others). Exception classification follows the applicable domicile's exam manual and the relevant accreditation standard. [verify the domicile-specific exam manual sections.] The register notes the regulatory regime explicitly in the criterion field; do not import US state-DOI conventions wholesale into a non-US captive register.
