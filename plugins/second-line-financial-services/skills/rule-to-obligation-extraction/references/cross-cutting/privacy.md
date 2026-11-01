# Privacy cross-cutting overlay — rule-to-obligation-extraction

Load when the rule under extraction is anchored to privacy, data protection, notice-and-consent, data minimisation, deletion rights, or disposal of consumer information. Privacy rules cross sector boundaries: GLBA Privacy Rule and Safeguards Rule land on most financial institutions; Reg P implements the GLBA Privacy Rule for CFPB-regulated entities; SEC Reg S-P amendments add incident-response programme requirements for SEC registrants; state privacy laws (CCPA/CPRA, VCDPA, CTDPA, others) layer on top with broad data-controller obligations; sector-specific privacy rules (HIPAA for protected health information) apply where in scope.

## Notice-and-consent extraction pattern

Privacy rules typically decompose into a notice-and-consent spine plus the substantive data-handling controls:

- **Initial-notice obligation**. At account opening or relationship establishment, the regulated party must deliver a privacy notice describing the categories of nonpublic personal information collected, disclosed, and the right (where it exists) to opt out of certain disclosures.
- **Annual-notice obligation** (where it applies). Where the rule requires annual delivery of the privacy notice (Reg P §1016.5; some state laws), the extraction captures the cadence and the form.
- **Opt-out obligation**. Where the consumer has the right to opt out of certain disclosures (e.g., disclosures to non-affiliated third parties under Reg P §1016.10; sale or sharing under CCPA/CPRA), the extraction captures the right, the timing of the notice giving effect to the right, and the recipient-side obligation to honour the opt-out.
- **Consent obligation** (where it applies). Where the rule requires affirmative consent for certain processing (e.g., targeted-advertising opt-in under CTDPA for sensitive data; sensitive-personal-information opt-in under CPRA; HIPAA authorisation for non-treatment uses), the extraction captures the trigger, the form, and the duration.

## Reg P / GLBA Privacy Rule worked pattern

12 CFR Part 1016 (CFPB Reg P; the rule was formerly Federal Reserve Reg P at 12 CFR Part 216 before Dodd-Frank transferred authority). Extraction decomposes into:

- §1016.4 Initial notice. Programme row: initial-notice content and timing.
- §1016.5 Annual notice. Frequency: periodic (annual). Action_type: notice_or_disclosure. Exception: §1016.5(e) eliminates annual notice in some circumstances when the FI has not changed sharing practices and provides specific limited disclosures.
- §1016.6 Information to be included. Content rows.
- §1016.7 Form of opt-out notice. Form-of-notice rows.
- §1016.10 Limits on disclosure of nonpublic personal information to non-affiliated third parties. Prohibition rows; exception rows for service-provider and joint-marketing arrangements (§1016.13), processing-and-servicing exceptions (§1016.14), other exceptions (§1016.15).
- §1016.16 Limits on redisclosure and reuse of information. Prohibition rows.
- §1016.17 Limits on sharing account-number information for marketing purposes. Prohibition row.

## GLBA Safeguards Rule worked pattern

16 CFR Part 314 (FTC). The 2021 amendments (effective in stages through June 9 2023) and the 2023 amendments (notification event added) restructured the Rule. Extraction decomposes into:

- §314.3 Standards for safeguarding customer information. Programme row.
- §314.4 Elements of the information-security programme. Each element is a row: §314.4(a) qualified-individual designation; §314.4(b) risk-assessment; §314.4(c) safeguards (eight enumerated controls, each a row); §314.4(d) regular monitoring and testing; §314.4(e) employee training and oversight; §314.4(f) service-provider oversight; §314.4(g) periodic re-evaluation; §314.4(h) incident-response plan; §314.4(i) annual report by the qualified individual to the board or governing body.
- §314.5 Notification event reporting (added 2023). Trigger and clock as captured in `cross-cutting/cyber.md`.

## SEC Reg S-P amendments worked pattern

89 FR 47688 (June 3 2024) [verify final FR cite], codified amendments to 17 CFR Part 248. Extraction decomposes into incident-response programme; customer-notice obligation following an unauthorised access or use of customer information; service-provider oversight; recordkeeping. Compliance dates staged by registrant size.

## State comprehensive privacy laws

State privacy laws (CCPA, CPRA, CDPA Virginia, CPA Colorado, CTDPA Connecticut, UCPA Utah, and others adopted since 2018) impose data-controller and data-processor obligations on a broad range of businesses. Extraction patterns vary by state but the spine is consistent:

- **Notice obligation** (privacy policy on collection and processing).
- **Consumer-rights obligations**: right to know; right to access; right to delete; right to correct; right to opt out of sale or sharing or targeted advertising; right to portability; right to limit use of sensitive personal information (CPRA only, with parallels in some other states).
- **Sensitive-personal-information processing obligation**: opt-in consent (most states) or opt-out (CCPA-style).
- **Data-protection-impact-assessment obligation** (most states except CCPA/CPRA, which has narrower assessment requirements).
- **Service-provider/processor contract obligation**: minimum contractual provisions on processing.
- **Universal opt-out signal recognition** (CPRA; CTDPA; CDPA opt-out preference signals).

Extraction is state-by-state. Where the rule under extraction is a single state's law, pin to that state's code. Where the work is a multi-state inventory, each state is a separate extraction.

## HIPAA Privacy and Security Rules (where in scope)

Where the financial-services entity is a covered entity or business associate under HIPAA (e.g., an insurer that issues health plans; a third-party administrator), the HIPAA Privacy Rule (45 CFR Part 164 Subpart E) and HIPAA Security Rule (45 CFR Part 164 Subpart C) apply. Extraction follows the standard programme-plus-notice-plus-rights pattern; pin to 45 CFR §164.NNN.

## When to layer with sector overlays

Privacy obligations frequently sit on top of sector-specific rules. When the rule under extraction is Reg P, load `cross-cutting/privacy.md` and `sector-overlays/payments-fintech.md` (or banking, depending on the institution). When the rule is SEC Reg S-P, load `cross-cutting/privacy.md` and `sector-overlays/capital-markets.md`. When the rule is NAIC Model 668 (which has both cyber and privacy elements), load `cross-cutting/cyber.md`, `cross-cutting/privacy.md`, and `sector-overlays/insurance.md`.
