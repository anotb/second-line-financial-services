# Insurance sector overlay for genai-pre-prod-review

When the engagement-scope record names `insurance` as the sector, this overlay adds insurance-specific gate considerations: named co-reviewers, additional notification triggers, sector-specific monitoring expectations, and recommended-action items typical of insurance GenAI gate reviews. Loaded by `genai-pre-prod-review/SKILL.md` when `engagement_scope.sector_overlay_set` includes `insurance`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023), AIS Program elements covering risk management, testing and validation, third-party AI accountability, monitoring, and documentation; binding only to the extent state DOIs adopt it (state-adoption tracker maintained by the NAIC AI Working Group).
- NYDFS Insurance Circular Letter on the Use of AI Systems and ECDIS in Insurance Underwriting and Pricing (January 2024) for NY-licensed life carriers.
- Colorado Division of Insurance regulation implementing SB 21-169 (life insurance underwriting governance for ECDIS and predictive models).
- HIPAA Privacy Rule (45 CFR Part 164) and Security Rule (45 CFR Part 164 Subpart C) where the use case handles PHI under a covered-entity or business-associate relationship.
- HIPAA Breach Notification Rule (45 CFR §§164.400-414) for PHI exfiltration events.
- State insurance commissioner cybersecurity regulations modelled on the NAIC Insurance Data Security Model Law (e.g., 23 NYCRR Part 500 for NY); state breach-notification laws for non-adopting states.
- State unfair-discrimination statutes (NAIC Model #880 vocabulary) for underwriting and pricing use cases.

## Co-reviewers the gate review brings in

Beyond the standard sign-off set:

- **Chief actuarial officer** for any underwriting, pricing, claims-decisioning, or reserving-relevant use case; the actuary signs the residual-risk acceptance for unfair-discrimination exposure and material decision integrity.
- **Privacy Officer** for any use case handling PHI or other regulated personal data; HIPAA breach evaluation is the seam.
- **Consumer compliance** for any policyholder-facing or claimant-facing use case; state insurance advertising rules and state suitability requirements apply.
- **State-level compliance** for any multi-state use case where AIS Program documentation, state Insurance Data Security Model Law adoption, or state-specific notification obligations vary.
- **SIU** (Special Investigations Unit) where the use case touches fraud detection or claim-investigation referral integrity.

## Open conditions the overlay typically adds

- AIS Program documentation per NAIC Model Bulletin in each adopting state in scope (the documentation is per state; one home-state package does not cover the others).
- HIPAA breach-notification process rehearsal as part of the IR drill scope where the use case handles PHI.
- State Insurance Data Security Model Law notification-decision process rehearsal in adopting states.
- For underwriting and pricing use cases: unfair-discrimination output-filter specification signed off by the underwriting actuary.
- For NY-licensed life-carrier underwriting: NYDFS Circular Letter governance, fairness-testing, disclosure, and consumer-recourse expectations mapped to the gate review's open conditions.
- For Colorado life-carrier underwriting: SB 21-169 implementing-regulation governance and unfair-discrimination testing mapped to the gate review.

## Monitoring signals the overlay expects to see live before go-live

In addition to the standard signal set:

- Per-claim and per-policy retrieval audit signal where the architecture handles claim or policy data; live before go-live for any claim-handling or policy-handling use case.
- ECDIS source-integrity monitoring (vendor change-of-content, last-modified, content hash on dynamic sources) for underwriting and pricing assistants.
- Unfair-discrimination output-filter trip rate where applicable; escalation to the underwriting actuary and to the chief actuarial officer.
- State insurance advertising rule output-filter trip rate where the use case is policyholder-facing or producer-facing.
- Cyber-side signals from the cyber overlay apply per NYDFS Part 500 and adopting-state Insurance Data Security Model Law equivalents.

## Incident-response triggers the overlay adds

In addition to the cyber-overlay-named triggers:

- HIPAA breach notification: the Breach Notification Rule (45 CFR §§164.400-414) requires notification to affected individuals, HHS, and in some cases the media following discovery of a breach of unsecured PHI. Prompt-injection-driven or cross-claim-disclosure events causing PHI exfiltration are within scope.
- State Insurance Data Security Model Law-adopting jurisdictions: cybersecurity event notification to the state insurance commissioner per the adopting state's regulation (timing varies; commonly 72 hours).
- State unfair-discrimination event triggers if an injection-driven or model-drift event causes a discriminatory output that affects an underwriting or pricing decision; the state DOI may be the appropriate notification authority depending on jurisdiction.
- Producer-side conduct triggers if the system is used in a way that violates state insurance advertising rules or state suitability requirements; consumer compliance evaluates.

The IR drill scope before go-live should exercise at minimum one insurance-specific incident class (e.g., confirmed cross-claim PHI disclosure for a claims use case; ECDIS-driven discriminatory output for an underwriting use case).

## Recommended-action items the overlay surfaces

- Where the use case is in scope of the NAIC Bulletin (in adopting states), the AIS Program documentation is updated to reference the gate review and the residual-risk acceptance is recorded against the AIS Program element on documentation.
- Where the use case is in NY-licensed life-carrier underwriting scope, the NYDFS Circular Letter governance, fairness-testing, disclosure, and consumer-recourse expectations are mapped to the gate review.
- Where the use case is in Colorado life-carrier underwriting scope, the SB 21-169 implementing-regulation governance is mapped.
- Where the use case handles PHI, the privacy officer co-signs the residual-risk acceptance and the HIPAA breach-notification process is rehearsed.
- Where the use case is multi-state, the state-by-state notification matrix is documented and consumer compliance signs off on the complaint-channel readiness per state.

## Common pitfalls specific to insurance gate reviews

- Treating ECDIS-sourced content as trusted because the data vendor is on the firm's approved-vendor list. The vendor's source-of-source is third-party-controlled; ECDIS-specific source-vetting and change-detection are the load-bearing controls, not vendor approval at procurement time.
- Omitting OCR-stage sanitisation for scanned correspondence in claims assistants. The OCR output is the point at which injected content lands in the prompt path; sanitisation at the OCR stage is more reliable than at the prompt-construction stage.
- Failing to involve the privacy officer when the use case handles PHI; a HIPAA-relevant exfiltration is a privacy event with binding notification timelines, not a discretionary AI-governance decision.
- Treating the unfair-discrimination overlay as separable from the prompt-injection overlay for underwriting assistants. An injection-driven feature shift in an ECDIS-sourced input can produce discriminatory output that violates state unfair-discrimination law; the two overlays are entangled.
- Treating a multi-state expansion as a single gate motion. AIS Program documentation, state breach laws, state Insurance Data Security Model Law adoption, and state insurance advertising rules vary by state; the gate review records state-by-state status rather than asserting national readiness.
- Recording vendor system card as substituting for firm-side AIS Program documentation. The AIS Program is a firm-side governance artefact; vendor evidence is one input.
