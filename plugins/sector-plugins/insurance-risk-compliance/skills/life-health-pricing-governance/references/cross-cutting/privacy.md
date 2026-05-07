# Cross-cutting overlay — privacy

Required-on for any pricing-governance review where the underwriting or pricing model touches PHI (most life-and-health AU and rating use cases) or where ECDIS is in the input set. The privacy overlay carries the substantive HIPAA, ECDIS-disclosure, and state insurance-information-privacy analysis.

The overlay does not substitute for a federal-and-state privacy-program review (which is its own work product). The artifact names the operative regimes, the controls, and the gap pointers.

## Anchor frame

- **HIPAA Privacy Rule, 45 CFR Part 164 Subpart E**. §164.502 uses and disclosures of PHI; §164.504 organizational requirements; §164.506 uses for treatment, payment, and health care operations; §164.508 authorization for non-routine uses; §164.514 de-identification standard. Applies wherever the pricing or underwriting model touches PHI. The "underwriting purposes" use under §164.506 has constraints and the use is not unbounded; verify the carrier's notice-of-privacy-practices and the consent posture on the analysis date.
- **HIPAA Security Rule, 45 CFR Part 164 Subpart C**. Applies where PHI is in electronic form (most pricing-governance contexts).
- **GINA Title I (group health) and Title II (employment)**, codified at 42 U.S.C. §2000ff et seq. Restricts the use of genetic information in health insurance underwriting and rating. Applies primarily to health plans; the life and disability sides have a separate but related state-law landscape. Verify state-by-state on the analysis date.
- **NAIC Insurance Information and Privacy Protection Model Act, Model #670** (verify model number). State-by-state adoption variable; in adopting states, sets disclosure and consumer-rights obligations for insurance-information practices including underwriting.
- **State insurance information privacy frameworks**. Most states have adopted a version of Model #670 or a related state-specific framework; verify state-by-state.
- **State comprehensive privacy laws** — CCPA / CPRA, VCDPA, CPA, CTDPA, UCPA, TDPSA, OCPA, MTCDPA, and others. Insurance-licensee carve-outs vary state-by-state; some states exempt insurance entities subject to GLBA and state insurance privacy law, others apply only to certain activities. Verify per state.
- **GLBA — Gramm-Leach-Bliley Act privacy provisions**. State insurance regulators implement GLBA Title V for the insurance sector via state-specific rules adapted from Model #672 (the Privacy of Consumer Financial and Health Information Regulation — verify model number). Notice and opt-out mechanics for non-public personal information.
- **Colorado SB 21-169 implementing regulation**. ECDIS provenance, governance, monitoring, and consumer-recourse for life-insurance underwriting in Colorado. Verify whether the regulation has been extended beyond life-insurance underwriting on the analysis date.
- **NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024)**. Disclosure and consumer-recourse expectations.
- **HHS OCR enforcement and guidance on HIPAA and underwriting**. Verify current state.

## What the overlay puts into the artifact

In the **rating-factor map** (Excel workbook): for each ECDIS-derived factor, the privacy-input column (HIPAA-applicability flag; FCRA-applicability flag; state insurance privacy framework flag; comprehensive-state-privacy-law flag); the consumer-consent posture column; the data-source contractual-permitted-use column.

In the **AIS Program** section, **documentation** element: HIPAA-applicability documentation; data-lineage documentation showing PHI flows into and out of the model; minimum-necessary analysis under §164.502; de-identification documentation under §164.514 where the model uses de-identified inputs.

In the **disparate-impact red flags** section: ECDIS provenance and proxy-variable risk; consumer-recourse channel and SLA; adverse-information-disclosure posture and timing.

In the **state DOI bulletin alignment** section: per-state privacy-rule alignment alongside the AI-bulletin alignment (Model #670 status; state comprehensive privacy law applicability with insurance carve-out posture).

In the **privacy and consumer-disclosure posture** section (the dedicated section in the Word memo): the substantive analysis. HIPAA notice-of-privacy-practices alignment; HIPAA authorization posture for non-routine uses; HIPAA business-associate-agreement chain for vendor AI; state insurance privacy framework alignment; ECDIS consumer-recourse channel description; ECDIS adverse-information-disclosure posture.

## HIPAA-specific check items

- **PHI scope.** Which model inputs are PHI (claims data, prescription history, medical records, lab results, biometric data, application-form medical questions). The carrier's HIPAA designation (covered entity / business associate / hybrid entity) drives the scope.
- **Underwriting purposes use under §164.506.** Permitted; constraints apply (the §164.502(a)(5)(i) restriction on use of genetic information for underwriting purposes — verify section). Documentation needs to show the use is within "underwriting purposes" as defined.
- **De-identification under §164.514.** Where the model uses de-identified inputs, the de-identification methodology must satisfy either the safe-harbour standard (§164.514(b)(2)) or the expert-determination standard (§164.514(b)(1)). De-identified data is not PHI; re-identification creates new PHI.
- **Authorization under §164.508 for non-routine uses.** Where the use exceeds "underwriting purposes" or "treatment, payment, and health care operations", written authorization is required.
- **Minimum necessary under §164.502(b)**. The model should use the minimum PHI necessary for the underwriting purpose; over-collection is a frequent gap.
- **Business-associate chain.** Vendor AI handling PHI is a business associate; the BAA must be on file under §164.504(e). Subcontractor BAAs flow through.
- **Breach-notification posture under §164.404 et seq.** Procedures for breach assessment and notification.

## ECDIS-specific check items

- **Source identification and contractual permitted use.** Which third party supplied the data; whether the data source's terms permit insurance-underwriting use; whether the underlying records carry consumer-consent requirements.
- **FCRA applicability where the data source is a consumer reporting agency.** Permissible-purpose analysis under 15 U.S.C. §1681b; adverse-action notice obligations under §1681m.
- **Consumer-recourse channel.** CO regulation and NY DFS Circular Letter set explicit expectations on the channel, the SLA, and the documentation. The artifact names the channel, the SLA, the owner, and the documentation posture.
- **Adverse-information-disclosure posture.** Where required, name the consumer notification timing and content. Link to the FCRA adverse-action regime where FCRA applies.
- **Proxy-variable risk.** Privacy and unfair-discrimination overlap. Where a proxy-variable analysis surfaces a privacy issue (e.g., the proxy reveals a sensitive attribute), the artifact names both lanes.

## Common pitfalls

- Treating "underwriting purposes" under HIPAA §164.506 as unbounded. The use is permitted but constrained; the GINA carve-out and the minimum-necessary principle apply.
- Treating de-identified data as out of scope without verifying the de-identification methodology against §164.514.
- Missing the business-associate-agreement chain for vendor AI handling PHI.
- Defaulting to "GLBA covers it" without checking state insurance privacy framework adoption (Model #670 or state-specific).
- Treating the state comprehensive privacy laws as inapplicable to insurance without verifying the state's insurance-licensee carve-out.
- Skipping FCRA where the ECDIS source is a consumer reporting agency.
- Naming the consumer-recourse channel as "the carrier's general consumer line" without an SLA, owner, and documentation posture. CO regulation and NY DFS Circular Letter are explicit.
