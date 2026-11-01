# Insurance sector overlay for prompt-injection-risk

When the scope record names `insurance` as the sector, this overlay adds insurance-specific carriers, mitigations, monitoring signals, and incident-notification triggers to the review. Loaded by `prompt-injection-risk/SKILL.md` when `scope.sector_overlay_set` includes `insurance`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023), AIS Program elements covering risk management, testing and validation, third-party AI accountability, monitoring, and documentation; binding only to the extent state DOIs adopt it (state-adoption tracker maintained by the NAIC AI Working Group).
- NYDFS Insurance Circular Letter on the Use of AI Systems and ECDIS in Insurance Underwriting and Pricing (January 2024) for NY-licensed life carriers.
- NYDFS October 2024 cyber-AI Industry Letter for NY-licensed insurers (NYDFS-covered entity status applies under 23 NYCRR Part 500).
- Colorado Division of Insurance regulation implementing SB 21-169 (life insurance underwriting governance for ECDIS and predictive models).
- HIPAA Privacy Rule (45 CFR Part 164) where the GenAI use case handles PHI under a covered-entity or business-associate relationship; HIPAA Security Rule (45 CFR Part 164 Subpart C) for the security side.
- State insurance commissioner cybersecurity regulations modelled on the NAIC Insurance Data Security Model Law (e.g., 23 NYCRR Part 500 for NY, similar regulations in other adopting states); state breach-notification laws for non-adopting states.
- ACORD standards and carrier proprietary forms for document-handling injection considerations.

## Carriers and trust posture nuances specific to insurance

The recurring insurance GenAI use-case patterns and the carriers that usually drive the threat surface:

- **Claims-summary assistant**: retrieves over scanned correspondence (claimant letters, third-party adjuster notes, repair estimates), medical records, police reports, attorney correspondence, recorded statement transcripts. Highest-likelihood vector is indirect injection via scanned correspondence and via medical-record content; OCR'd content is partially trusted and contains content originating from claimants, providers, attorneys, and third-party adjusters who may have an adversarial interest in claim outcome.

- **Underwriting assistant** (life and health): retrieves over application data, medical records, prescription history, motor vehicle records, public-records databases, ECDIS sources (consumer reports, social and behavioural data sources). Highest-likelihood vector is indirect injection via ECDIS content (third-party-controlled at source) and the unfair-discrimination overlay is structural; the NYDFS Circular Letter and Colorado SB 21-169 framings both apply where in jurisdiction.

- **Customer-service assistant** (P&C and life): retrieves over policy data, call and chat history, claims status. Similar pattern to banking customer-service assistant; cross-policy and cross-policyholder bleed is the structural risk.

- **Producer/agent assistant**: retrieves over product documentation, illustration software output, regulatory filings. Marketing Rule analogues (state insurance advertising rules and SEC Rule 156 for variable products) are the conduct-side seam.

- **Fraud-detection assistant**: retrieves over claim files, social-media content, third-party fraud-network data. Indirect injection in third-party intelligence is the structural risk; SIU referral integrity is the downstream consequence.

## Mitigations the review should expect to see

Beyond the standard set:

- HIPAA-aligned access controls on PHI carriers; per-claim or per-policy query scoping is the default for any claim or policy-handling assistant.
- ECDIS-specific input controls: source-vetting at the data-vendor layer, change-detection on ECDIS sources, drift monitoring on ECDIS-sourced features (NYDFS Circular Letter and Colorado SB 21-169 expectations on ECDIS governance flow into the prompt-injection mitigation set).
- OCR-stage input sanitisation for scanned correspondence: normalisation of suspicious patterns, separation of OCR'd text from system instructions in the prompt structure, content-type tagging.
- State unfair-discrimination output filtering for any underwriting or pricing recommendation; the underwriting actuary signs off on the filtering specification.
- Marketing Rule equivalents for any customer-facing or agent-facing communication generated or assisted by the system; state insurance advertising rules apply.
- Foundation-model and vendor change-of-version notice and audit rights, captured in the third-party AI register required by the NAIC Bulletin AIS Program element on third-party accountability.

## Monitoring signals the overlay adds

- Per-claim and per-policy retrieval audit; any confirmed cross-claim or cross-policy bleed is a HIPAA evaluation trigger and may be a NYDFS §500.17(a) trigger for NY-licensed entities.
- ECDIS source-integrity monitoring (vendor change-of-content, last-modified, content hash on dynamic sources) for underwriting and pricing assistants.
- Unfair-discrimination output-filter trip rate where applicable; escalation to the underwriting actuary and to the chief actuarial officer or equivalent.
- State insurance advertising rule output-filter trip rate where applicable; escalation to compliance.
- Cyber-side signals from the cyber overlay (authentication anomalies, tool-invocation patterns, vendor change-of-version) apply per NYDFS Part 500 and adopting-state Insurance Data Security Model Law equivalents.

## Incident-response triggers the overlay adds

In addition to the cyber-overlay-named triggers:

- HIPAA breach notification: the Breach Notification Rule (45 CFR §§164.400-414) requires notification to affected individuals, HHS, and in some cases the media following discovery of a breach of unsecured PHI. Prompt-injection events causing PHI exfiltration are within scope.
- State Insurance Data Security Model Law-adopting jurisdictions: cybersecurity event notification to the state insurance commissioner per the adopting state's regulation (timing varies; commonly 72 hours).
- State unfair-discrimination event triggers if an injection-driven event causes a discriminatory output that affects an underwriting or pricing decision; the state DOI may be the appropriate notification authority depending on jurisdiction.
- Producer-side conduct triggers if the system is used in a way that violates state insurance advertising rules or state suitability requirements.

## Recommended-action items the overlay surfaces

- Where the use case is in scope of the NAIC Bulletin (in adopting states), the AIS Program documentation is updated to reference the prompt-injection review and the residual risk acceptance is recorded against the AIS Program element on documentation.
- Where the use case is in NY-licensed life-carrier underwriting scope, the NYDFS Circular Letter governance, fairness-testing, disclosure, and consumer-recourse expectations are mapped to the review's mitigations and recommended actions.
- Where the use case is in Colorado life-carrier underwriting scope, the SB 21-169 implementing regulation is referenced and the unfair-discrimination testing is mapped to the review's tested-attack and monitoring sections.
- Where the use case handles PHI, the privacy officer co-signs the residual-risk acceptance and the HIPAA breach-notification process is rehearsed.

## Common pitfalls specific to insurance

- Treating ECDIS-sourced content as trusted because the data vendor is on the firm's approved-vendor list. The vendor's source-of-source is third-party-controlled; ECDIS-specific source-vetting and change-detection are the load-bearing controls, not vendor approval at procurement time.
- Omitting OCR-stage sanitisation for scanned correspondence in claims assistants. The OCR output is the point at which injected content lands in the prompt path; sanitisation at the OCR stage is more reliable than at the prompt-construction stage.
- Failing to involve the privacy officer when the use case handles PHI; a HIPAA-relevant exfiltration is a privacy event with binding notification timelines, not a discretionary AI-governance decision.
- Treating the unfair-discrimination overlay as separable from the prompt-injection overlay for underwriting assistants. An injection-driven feature shift in an ECDIS-sourced input can produce discriminatory output that violates state unfair-discrimination law; the two overlays are entangled.
- Omitting state-by-state breach-notification analysis when the firm operates across multiple states; the state patchwork is the firm's responsibility to maintain and the review references the firm's matrix rather than restating it.
