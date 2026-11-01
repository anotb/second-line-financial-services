# Sector overlay: banking

Loads when `sector_overlay_set` includes `banking`. Carries large-bank supervisory-finding terminology context, heightened-standards severity flavour, and the BSA/AML and consumer-compliance exception conventions that shape classification and severity calibration in bank-side compliance testing.

## Supervisory-finding terminology context

Bank examiners use a structured ladder for supervisory findings: matter-requiring-attention, matter-requiring-immediate-attention, formal enforcement action. Federal Reserve, OCC, and FDIC each carry their own variants; large banks are typically in scope of more than one. The firm does not invent a regulator-issued matter; it drafts its own exceptions in the same shape so its records align with examiner vocabulary.

What this means for the register:

- An exception severity-ranked `critical` should be readable in the shape an examiner would expect to see for a matter-requiring-immediate-attention candidate (clearly stated condition, criterion with section reference, dated, scoped, with quantified effect where possible). The register itself carries internal severity, not an examiner classification.
- A repeat-issue flag with a prior issue ID raises the supervisory-finding-eligibility read. Repeat exceptions on the same control or population are the classic pattern that converts a matter-requiring-attention into something heavier on the next exam cycle.
- Exception conditions and effects that touch board-reported metrics or consolidated risk reporting carry escalated severity rationale (the supervisory expectation is that board-reported information is reliable). [verify the exact framing in current Federal Reserve and OCC guidance.]

The firm's escalation playbook is the firm's; this overlay does not substitute for it. The handoff to issue write-up populates fields the firm uses to ladder its own internal escalation, and `issue-writeup` carries the matter-requiring-attention / matter-requiring-immediate-attention classification field where the source is examiner-issued.

## Heightened-standards severity flavour

For large insured national banks within scope of 12 CFR Part 30 Appendix D, the three-lines-of-defense structure is part of the supervisory expectation rather than a methodology preference. [verify section labels.]

Exception classification carries this:

- A control-failure exception in the front-line that the independent risk-management function did not surface earlier in the lifecycle reads with different severity than the same exception caught earlier. The severity rationale field names the second-line and internal-audit roles in the chain.
- Risk-governance-framework exceptions (limits framework, risk-appetite reporting, board-level risk reporting) carry the heightened-standards framing; the criterion field cites Appendix D with a section reference.

## BSA/AML exception conventions

BSA/AML testing produces a distinctive set of exception patterns: customer-due-diligence file completeness, beneficial-ownership documentation, currency-transaction reporting accuracy, suspicious-activity-report timing, OFAC sanctions-screening hits clearance. The criterion is typically the BSA/AML rule with a section reference (31 CFR Chapter X) and the FFIEC BSA/AML examination manual section. [verify rule and manual sections per the current edition.]

Classification calls for the BSA/AML population:

- A missing CDD document where the customer relationship was nonetheless onboarded with required risk rating in the system reads as `evidence-gap`, severity moderates against frequency and customer risk tier.
- A late SAR filing reads as `control-failure` with timing being the load-bearing fact; severity calibration uses the SAR-timing rule's deadlines, not the firm's internal SLA.
- A sanctions-screening hit not cleared within the firm's escalation SLA reads as `control-failure`, severity scales with the watch-list source and the customer relationship type. Critical when the hit is on a primary sanctions list.

Conduct-overlay loading is automatic when the BSA/AML population includes consumer-facing accounts.

## Consumer-compliance exception conventions

Consumer-compliance testing covers Reg E (electronic fund transfer error resolution), Reg Z (truth in lending), Reg B (equal credit opportunity), Reg DD (truth in savings), HMDA (home mortgage disclosure), Reg X (RESPA), and the CFPB UDAAP frame. [verify CFR citations per current editions.]

Classification calls:

- Timing-rule deviations (Reg E provisional credit, error resolution finals, Reg X disclosure timing) read as `control-failure`, severity calibrated against the regulatory deadline and the consumer-impact pattern.
- HMDA LAR data accuracy deviations split between `data-integrity` (system of record disagrees with the LAR submission) and `control-failure` (the source data was wrong).
- UDAAP-touching exceptions load the conduct cross-cutting overlay; the severity rationale field carries customer-harm framing distinct from the technical control deviation.

## Sponsor-bank programme overlay (intersection with payments-fintech)

Bank-as-a-service / sponsor-bank engagements are bank-side; they often load alongside `payments-fintech.md` because the controls under test span the bank's oversight machinery and the fintech partner's operational execution. Exception classification here often turns on whether the deviation is in the bank's oversight control (sponsor-bank-side `control-failure` or `design-gap`) or in the partner's execution that the bank's oversight should have caught (still classified at the bank's control, not the partner's, because the bank is the testing subject). [verify the relevant interagency third-party guidance section labels.]
