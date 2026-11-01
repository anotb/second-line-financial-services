# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for genai-pre-prod-review

When the scope record names `banking` as the sector, this overlay adds banking-specific gate considerations: named co-reviewers, additional notification triggers, sector-specific monitoring expectations, and recommended-action items typical of banking GenAI gate reviews. Loaded by `genai-pre-prod-review/SKILL.md` when `scope.sector_overlay_set` includes `banking`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- The joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17 2026; supersedes SR 11-7 and SR 21-8) for traditional non-generative components in scope. The bulletin expressly excludes generative AI and agentic AI from its scope (footnote 3); for the GenAI use case itself the firm's model risk programme reaches it by analogy at firm policy level, and the pre-prod gate exercises the governance, validation, and documentation expectations the firm has elected to apply.
- Joint Interagency Guidance on Third-Party Relationships (June 2023; OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023) where the GenAI system is vendor-hosted or relies on a foundation-model provider.
- 12 CFR Part 30 Appendix D (OCC Heightened Standards) for OCC-supervised large banks where the GenAI use case sits inside a risk-appetite-statement-relevant function; the chief risk executive function signs the residual-risk acceptance.
- 12 CFR Part 53 (OCC), 12 CFR Part 225 Subpart N (FRB), 12 CFR Part 304 (FDIC) — the 36-hour banking computer-security incident notification rule (effective 2022).
- NYDFS 23 NYCRR Part 500 and the October 2024 AI Industry Letter for NY-footprint covered entities.
- FFIEC IT Examination Handbook, Information Security and AIO booklets, applied to the GenAI system's serving environment, change controls, and access controls.
- FFIEC BSA/AML Examination Manual where the use case touches AML alert handling, customer risk rating, KYC narrative drafting, or SAR drafting.

#### Co-reviewers the gate review brings in

Beyond the standard sign-off set (AI Governance Lead, model risk lead, CISO function, compliance, privacy, legal):

- **BSA officer** for any use case touching AML alert handling, KYC, customer risk rating, or SAR narrative. The BSA officer evaluates programme-integrity exposure and signs the residual-risk acceptance for AML-touching items.
- **Consumer compliance** for any customer-facing or customer-handling use case; UDAAP exposure on AI-generated or AI-assisted customer communication is the seam.
- **Chief risk executive function** for OCC large-bank scope where the use case sits inside a risk-appetite-statement-relevant function; the residual risk surfaces to the chief risk executive per Heightened Standards.
- **Vendor management** for any vendor-hosted or foundation-model-dependent use case; the third-party risk register entry references the gate review and the foundation-model swap re-validation policy.

#### Open conditions the overlay typically adds

- For OCC large-bank scope: documentation of the connection to the bank's risk-appetite-statement framework and named acceptance by the chief risk executive function.
- For BSA/AML-touching use cases: BSA officer co-signature on the residual-risk acceptance and on the monitoring-readiness section's AML-relevant signals (KYC narrative quality, alert-disposition-anomaly rate where applicable).
- For NY-footprint covered entities: NYDFS §500.17(a) notification-decision rehearsal as part of the IR drill scope.
- For vendor-hosted use cases: third-party risk register entry updated to reference the gate review and the foundation-model swap re-validation policy; vendor management co-signature.

#### Monitoring signals the overlay expects to see live before go-live

In addition to the standard signal set:

- Per-customer retrieval audit signal where the architecture handles customer data; the signal must be live before go-live for any customer-handling use case.
- AML alert-disposition anomaly signal where the use case supports alert handling; escalation to the BSA officer.
- KYC narrative quality signal (citation precision on KYC source attributions, analyst-edit rate) where the use case supports KYC analysis; escalation to the BSA officer with model owner.
- Marketing Rule analogue output-filter trip rate where the use case is customer-facing communication and the institution carries dual registrations (joint trust company / RIA / BD); escalation to compliance.

#### Incident-response triggers the overlay adds

In addition to the cyber-overlay-named triggers:

- 12 CFR Part 53 / Part 225 / Part 304 — the 36-hour banking computer-security incident notification rule. The bank notifies its primary federal regulator within 36 hours of determining a notification incident has occurred. Prompt-injection-driven or cross-customer-disclosure events causing material disruption, degradation, or actual harm to bank operations are within scope. The notification decision sits with the cyber and operational-resilience leads with general counsel.
- BSA/AML programme-integrity event triggers if the use case touches alert disposition, KYC narrative, or SAR drafting and the integrity of those outputs is in question; the BSA officer evaluates against the SAR continuing-activity reporting framework and against programme-integrity examination expectations.
- Consumer-protection event triggers if customer-facing AI output causes a UDAAP-relevant communication issue; consumer compliance evaluates.

The IR drill scope before go-live should exercise at minimum one banking-specific incident class (e.g., confirmed cross-customer information bleed for a customer-handling use case; KYC narrative integrity issue for a KYC use case; alert-disposition integrity issue for an AML use case).

#### Recommended-action items the overlay surfaces

- Where the use case is in OCC large-bank scope, the residual-risk acceptance routes to the chief risk executive function and the connection to the risk-appetite statement is documented.
- Where the use case is vendor-hosted or relies on a foundation-model provider, the third-party risk register entry references the gate review and the foundation-model swap re-validation policy.
- Where the use case touches AML alert handling or KYC narrative drafting, the BSA officer co-signs and BSA-relevant monitoring signals are live before go-live.
- Where the use case is customer-facing in NY footprint, the NYDFS §500.17(a) notification-decision process is rehearsed against AI-specific incident scenarios as part of the IR drill scope.

#### Common pitfalls specific to banking gate reviews

- Treating a vendor-hosted GenAI on a vendor-hosted foundation model as a single-vendor relationship. The vendor's foundation-model behaviour shift is a third-party event and a cyber event; the third-party risk register and the cyber overlay both bind.
- Omitting the 36-hour banking computer-security incident notification rule. It is distinct from the NYDFS 72-hour notice and from the SEC 8-K four-business-day disclosure; all three can apply concurrently for a single material event in a NY-footprint public-registrant bank.
- Failing to involve the BSA officer when the use case touches alert handling, KYC, or SAR drafting; an integrity issue with AI-assisted alert disposition or AI-assisted KYC narrative is a BSA programme issue, not just a model-risk issue.
- Treating the chief risk executive role under 12 CFR Part 30 Appendix D as out-of-scope for AI use cases. AI use cases inside risk-appetite-relevant functions are within the Heightened Standards seam; the residual-risk acceptance routes accordingly.
- Recording vendor SOC 2 or vendor system card as substituting for firm-side gate evidence. Vendor evidence is a foundation, not a substitute; the gate review records vendor evidence at vendor-self-attestation confidence and the firm-side gate items are firm-side responsibilities.

## capital-markets

### Capital markets sector overlay for genai-pre-prod-review

When the scope record names `capital-markets` as the sector, this overlay adds capital-markets-specific gate considerations: named co-reviewers, additional notification triggers, sector-specific monitoring expectations, and recommended-action items typical of capital-markets GenAI gate reviews (research assistants, surveillance assistants, analyst assistants, execution-related assistants). Loaded by `genai-pre-prod-review/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- SEC Rule 206(4)-1 (Investment Adviser Marketing Rule) and Rule 204-2 (Books and Records) for AI-generated client-facing content from registered investment advisers.
- SEC Rule 17a-3 and Rule 17a-4 (broker-dealer books and records) and FINRA Rule 2210 (communications with the public) and Rule 3110 (supervision) for AI-generated or AI-assisted communications and supervisory review.
- SEC Rule 15c3-5 (Market Access Rule) for execution-related AI controls; pre-trade controls and risk management.
- SEC Regulation Best Interest (Reg BI) and the related fiduciary-lens framing for retail-facing investment recommendations.
- Market Abuse Regulation (MAR) Articles 12 and 15 (market manipulation and inside information) for surveillance-system adjacency.
- SEC and FINRA cybersecurity-related rules and guidance; SEC Reg S-P (privacy) where customer information is in scope.
- NYDFS 23 NYCRR Part 500 for NY-licensed entities including state-licensed broker-dealers and money managers.

#### Co-reviewers the gate review brings in

Beyond the standard sign-off set:

- **Chief compliance officer (registered investment adviser)** or **head of compliance (broker-dealer)** for any client-facing or supervised-communication use case; Marketing Rule and FINRA Rule 2210 review.
- **Head of supervision** for any use case touching FINRA Rule 3110 supervisory review (research, communications, trade surveillance).
- **Head of trading or chief market structure officer** for any execution-adjacent use case (algorithm-related research, execution-quality analysis, pre-trade controls).
- **Head of research** for research-assistant use cases; Marketing Rule reach to research output is the seam.
- **Surveillance / market integrity** for surveillance-system AI augmentation; MAR and SEC market-manipulation framing.
- **Books-and-records function** for any AI-generated or AI-assisted output that constitutes a book or record subject to retention.

#### Open conditions the overlay typically adds

- Books-and-records preservation policy explicitly covering AI-generated and AI-assisted communications; the retention policy applies to AI artefacts including prompts, retrieved content, and outputs to the extent they constitute communications subject to Rule 17a-4 or Rule 204-2.
- Marketing Rule output-filter specification signed off by chief compliance officer for any client-facing communication generated or assisted by the system.
- FINRA Rule 2210 supervisory-review workflow named for any broker-dealer use case generating or assisting public communications.
- For surveillance-augmenting use cases: documented evaluation that the AI augmentation does not introduce false-negative bias against MAR-relevant patterns; surveillance / market integrity co-sign.
- For execution-adjacent use cases: SEC Rule 15c3-5 pre-trade control review; head of trading co-sign.
- For client-facing recommendation-adjacent use cases: Reg BI or fiduciary-lens framing documented; chief compliance officer signs.

#### Monitoring signals the overlay expects to see live before go-live

In addition to the standard signal set:

- Marketing Rule output-filter trip rate; escalation to chief compliance officer.
- FINRA Rule 2210 supervisory-review queue throughput where the use case generates public communications; escalation to head of supervision.
- For research assistants: citation accuracy and source-attribution audit; escalation to head of research and chief compliance officer.
- For surveillance assistants: false-negative-rate sampling against known-positive patterns; escalation to surveillance / market integrity.
- For execution-adjacent: pre-trade control trip rate; escalation to head of trading.
- Books-and-records retention coverage signal: completeness of capture for AI-relevant artefacts; escalation to books-and-records function.

#### Incident-response triggers the overlay adds

In addition to the cyber-overlay-named triggers:

- SEC Reg S-P notification triggers for customer-information-relevant events.
- FINRA reporting obligations under Rule 4530 for certain reportable events including specified disciplinary events that may arise from AI-assisted communications causing supervisory-review failures.
- SEC self-reporting expectations under SEC Enforcement guidance where AI-assisted communications cause material misleading statements.
- State Marketing Rule analogues and state insurance advertising rules where the institution carries dual licensure.

The IR drill scope before go-live should exercise at minimum one capital-markets-specific incident class (e.g., confirmed Marketing Rule violation in AI-assisted client communication; confirmed surveillance false-negative in AI-augmented surveillance; confirmed books-and-records gap in AI-relevant artefact capture).

#### Recommended-action items the overlay surfaces

- Books-and-records preservation policy updated to cover AI artefacts; books-and-records function co-signs.
- Marketing Rule and FINRA Rule 2210 supervisory-review workflow updated to integrate AI-assisted output for any public-communication-adjacent use case.
- For surveillance-augmenting use cases: documented baseline against the prior surveillance system's true-positive and false-negative rate, with a defined regression-test cadence.
- For execution-adjacent use cases: SEC Rule 15c3-5 pre-trade control review; coordination with the existing market-access risk-management framework.
- For dual-licensed entities (RIA + BD or BD + insurance): cross-regulator notification matrix documented per the firm's regulator constellation.

#### Common pitfalls specific to capital-markets gate reviews

- Treating an AI-assisted research draft as out of Marketing Rule scope because the analyst reviews before publication. The Marketing Rule applies to the output as published; the AI-assisted draft is one input but the published communication carries the same obligation. The supervisory-review workflow needs to handle AI-assisted material distinctly enough that the supervisor can apply Marketing Rule judgement.
- Treating books-and-records as a downstream IT problem. Rule 17a-4 and Rule 204-2 apply to AI artefacts to the extent they constitute communications subject to retention; the books-and-records function is a co-reviewer and co-signer, not a downstream consumer.
- Treating a surveillance-augmenting use case as a control improvement without baseline-against-prior-system evidence. A new AI surveillance layer that improves true positives while shifting false negatives in unrelated MAR-relevant patterns is a net regression; the gate review records the regression test explicitly.
- Treating an execution-adjacent use case as not in SEC Rule 15c3-5 scope because the AI does not directly execute. Pre-trade controls apply to inputs to execution; AI-assisted decision support that materially shapes execution decisions is within scope of the firm's market-access risk-management framework.
- Omitting the chief compliance officer co-signature on client-facing AI use cases at registered investment advisers. The Marketing Rule fiduciary-lens framing is the chief compliance officer's seat; the gate decision is incomplete without it.

## insurance

### Insurance sector overlay for genai-pre-prod-review

When the scope record names `insurance` as the sector, this overlay adds insurance-specific gate considerations: named co-reviewers, additional notification triggers, sector-specific monitoring expectations, and recommended-action items typical of insurance GenAI gate reviews. Loaded by `genai-pre-prod-review/SKILL.md` when `scope.sector_overlay_set` includes `insurance`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023), AIS Program elements covering risk management, testing and validation, third-party AI accountability, monitoring, and documentation; binding only to the extent state DOIs adopt it (state-adoption tracker maintained by the NAIC AI Working Group).
- NYDFS Insurance Circular Letter on the Use of AI Systems and ECDIS in Insurance Underwriting and Pricing (January 2024) for NY-licensed life carriers.
- Colorado Division of Insurance regulation implementing SB 21-169 (life insurance underwriting governance for ECDIS and predictive models).
- HIPAA Privacy Rule (45 CFR Part 164) and Security Rule (45 CFR Part 164 Subpart C) where the use case handles PHI under a covered-entity or business-associate relationship.
- HIPAA Breach Notification Rule (45 CFR §§164.400-414) for PHI exfiltration events.
- State insurance commissioner cybersecurity regulations modelled on the NAIC Insurance Data Security Model Law (e.g., 23 NYCRR Part 500 for NY); state breach-notification laws for non-adopting states.
- State unfair-discrimination statutes (NAIC Model #880 vocabulary) for underwriting and pricing use cases.

#### Co-reviewers the gate review brings in

Beyond the standard sign-off set:

- **Chief actuarial officer** for any underwriting, pricing, claims-decisioning, or reserving-relevant use case; the actuary signs the residual-risk acceptance for unfair-discrimination exposure and material decision integrity.
- **Privacy Officer** for any use case handling PHI or other regulated personal data; HIPAA breach evaluation is the seam.
- **Consumer compliance** for any policyholder-facing or claimant-facing use case; state insurance advertising rules and state suitability requirements apply.
- **State-level compliance** for any multi-state use case where AIS Program documentation, state Insurance Data Security Model Law adoption, or state-specific notification obligations vary.
- **SIU** (Special Investigations Unit) where the use case touches fraud detection or claim-investigation referral integrity.

#### Open conditions the overlay typically adds

- AIS Program documentation per NAIC Model Bulletin in each adopting state in scope (the documentation is per state; one home-state package does not cover the others).
- HIPAA breach-notification process rehearsal as part of the IR drill scope where the use case handles PHI.
- State Insurance Data Security Model Law notification-decision process rehearsal in adopting states.
- For underwriting and pricing use cases: unfair-discrimination output-filter specification signed off by the underwriting actuary.
- For NY-licensed life-carrier underwriting: NYDFS Circular Letter governance, fairness-testing, disclosure, and consumer-recourse expectations mapped to the gate review's open conditions.
- For Colorado life-carrier underwriting: SB 21-169 implementing-regulation governance and unfair-discrimination testing mapped to the gate review.

#### Monitoring signals the overlay expects to see live before go-live

In addition to the standard signal set:

- Per-claim and per-policy retrieval audit signal where the architecture handles claim or policy data; live before go-live for any claim-handling or policy-handling use case.
- ECDIS source-integrity monitoring (vendor change-of-content, last-modified, content hash on dynamic sources) for underwriting and pricing assistants.
- Unfair-discrimination output-filter trip rate where applicable; escalation to the underwriting actuary and to the chief actuarial officer.
- State insurance advertising rule output-filter trip rate where the use case is policyholder-facing or producer-facing.
- Cyber-side signals from the cyber overlay apply per NYDFS Part 500 and adopting-state Insurance Data Security Model Law equivalents.

#### Incident-response triggers the overlay adds

In addition to the cyber-overlay-named triggers:

- HIPAA breach notification: the Breach Notification Rule (45 CFR §§164.400-414) requires notification to affected individuals, HHS, and in some cases the media following discovery of a breach of unsecured PHI. Prompt-injection-driven or cross-claim-disclosure events causing PHI exfiltration are within scope.
- State Insurance Data Security Model Law-adopting jurisdictions: cybersecurity event notification to the state insurance commissioner per the adopting state's regulation (timing varies; commonly 72 hours).
- State unfair-discrimination event triggers if an injection-driven or model-drift event causes a discriminatory output that affects an underwriting or pricing decision; the state DOI may be the appropriate notification authority depending on jurisdiction.
- Producer-side conduct triggers if the system is used in a way that violates state insurance advertising rules or state suitability requirements; consumer compliance evaluates.

The IR drill scope before go-live should exercise at minimum one insurance-specific incident class (e.g., confirmed cross-claim PHI disclosure for a claims use case; ECDIS-driven discriminatory output for an underwriting use case).

#### Recommended-action items the overlay surfaces

- Where the use case is in scope of the NAIC Bulletin (in adopting states), the AIS Program documentation is updated to reference the gate review and the residual-risk acceptance is recorded against the AIS Program element on documentation.
- Where the use case is in NY-licensed life-carrier underwriting scope, the NYDFS Circular Letter governance, fairness-testing, disclosure, and consumer-recourse expectations are mapped to the gate review.
- Where the use case is in Colorado life-carrier underwriting scope, the SB 21-169 implementing-regulation governance is mapped.
- Where the use case handles PHI, the privacy officer co-signs the residual-risk acceptance and the HIPAA breach-notification process is rehearsed.
- Where the use case is multi-state, the state-by-state notification matrix is documented and consumer compliance signs off on the complaint-channel readiness per state.

#### Common pitfalls specific to insurance gate reviews

- Treating ECDIS-sourced content as trusted because the data vendor is on the firm's approved-vendor list. The vendor's source-of-source is third-party-controlled; ECDIS-specific source-vetting and change-detection are the load-bearing controls, not vendor approval at procurement time.
- Omitting OCR-stage sanitisation for scanned correspondence in claims assistants. The OCR output is the point at which injected content lands in the prompt path; sanitisation at the OCR stage is more reliable than at the prompt-construction stage.
- Failing to involve the privacy officer when the use case handles PHI; a HIPAA-relevant exfiltration is a privacy event with binding notification timelines, not a discretionary AI-governance decision.
- Treating the unfair-discrimination overlay as separable from the prompt-injection overlay for underwriting assistants. An injection-driven feature shift in an ECDIS-sourced input can produce discriminatory output that violates state unfair-discrimination law; the two overlays are entangled.
- Treating a multi-state expansion as a single gate motion. AIS Program documentation, state breach laws, state Insurance Data Security Model Law adoption, and state insurance advertising rules vary by state; the gate review records state-by-state status rather than asserting national readiness.
- Recording vendor system card as substituting for firm-side AIS Program documentation. The AIS Program is a firm-side governance artefact; vendor evidence is one input.

## payments-fintech

### Payments and fintech sector overlay for genai-pre-prod-review

When the scope record names `payments-fintech` as the sector, this overlay adds payments-and-fintech-specific gate considerations: sponsor-bank co-acceptance where applicable, payments-specific notification triggers, sector-specific monitoring expectations, and recommended-action items typical of payments and fintech GenAI gate reviews (customer-service assistants, fraud-detection augmentation, transaction-monitoring augmentation, dispute-handling assistants). Loaded by `genai-pre-prod-review/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- Joint Interagency Guidance on Third-Party Relationships (June 2023; OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023) for sponsor-bank / fintech relationships and BaaS arrangements.
- Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services (July 2024) and related interagency guidance for BaaS arrangements.
- Reg E (12 CFR Part 1005) for consumer electronic fund transfer dispute handling and provisional-credit obligations.
- Reg Z (12 CFR Part 1026) where the use case touches credit-product communications.
- CFPB UDAAP authority and CFPB circulars for AI-assisted customer communications and dispute handling.
- BSA/AML obligations for non-bank financial institutions registered with FinCEN; transaction-monitoring augmentation considerations.
- Card-network rules (Visa, Mastercard, Amex, Discover) for fraud and chargeback handling where applicable.
- State money-transmitter laws and state DFI / DBO supervision for licensed non-bank entities.
- Network rules for ACH (Nacha Operating Rules) and real-time payments where applicable.
- NYDFS 23 NYCRR Part 500 and the BitLicense framework for NY-licensed money transmitters and virtual currency businesses.

#### Co-reviewers the gate review brings in

Beyond the standard sign-off set:

- **Sponsor bank** for any BaaS or sponsor-bank-relationship use case; the sponsor bank's own model risk and AI governance functions co-accept the gate decision per the relationship agreement.
- **Consumer compliance** for any consumer-facing or consumer-handling use case; UDAAP, Reg E, and Reg Z exposure on AI-generated or AI-assisted customer communication.
- **BSA officer** for non-bank financial institutions registered with FinCEN where the use case touches transaction monitoring, customer due diligence, or SAR drafting.
- **Fraud and disputes function** for any use case touching fraud detection, dispute handling, or chargeback processing.
- **Network compliance** for any use case touching card-network or ACH-network operations; network-rule conformance.
- **State money-transmitter compliance** for any multi-state licensed non-bank entity; state-by-state notification and licensing variation.

#### Open conditions the overlay typically adds

- Sponsor-bank co-acceptance documented in the BaaS or sponsor-bank relationship file for any sponsor-bank-relationship use case; the sponsor bank's gate decision and the firm's gate decision align before go-live.
- Reg E provisional-credit-handling workflow documented for any AI-assisted dispute-handling use case; the 10-day provisional-credit clock runs regardless of AI handling decisions.
- UDAAP output-filter specification signed off by consumer compliance for any consumer-facing communication generated or assisted by the system.
- For transaction-monitoring augmentation: documented evaluation that the AI augmentation does not introduce false-negative bias against BSA-relevant patterns; BSA officer co-signs.
- For fraud-detection augmentation: documented baseline against the prior fraud-detection system; fraud and disputes function co-signs.
- For non-bank entities in state-money-transmitter scope: state-by-state licensing and notification matrix documented.

#### Monitoring signals the overlay expects to see live before go-live

In addition to the standard signal set:

- UDAAP output-filter trip rate; escalation to consumer compliance.
- Reg E dispute-handling SLA tracking (10-day provisional-credit clock, 45-day resolution clock); escalation to consumer compliance and dispute function.
- For fraud-detection augmentation: false-negative-rate and false-positive-rate sampling against the prior system baseline; escalation to fraud and disputes function.
- For transaction-monitoring augmentation: alert-quality and alert-disposition-anomaly signals; escalation to BSA officer.
- Sponsor-bank notification feed throughput where applicable; escalation to vendor management with sponsor-bank relationship owner.
- Network-rule conformance signal where applicable (chargeback-processing accuracy, ACH-return-handling accuracy).

#### Incident-response triggers the overlay adds

In addition to the cyber-overlay-named triggers:

- For sponsor-bank-relationship use cases: notification to the sponsor bank under the BaaS or sponsor-bank relationship agreement; the sponsor bank's notification obligations to its primary federal regulator (including the 36-hour banking computer-security incident notification rule under 12 CFR Part 53 / Part 225 / Part 304) flow back via the relationship.
- BSA programme-integrity event triggers for non-bank financial institutions in FinCEN scope where the use case touches transaction monitoring or SAR drafting; FinCEN reporting obligations apply.
- Reg E error-resolution-process integrity event triggers if AI-assisted dispute handling causes a procedural failure that affects a consumer's rights under Reg E.
- Card-network notification obligations where a fraud or chargeback handling AI failure crosses a network-rule notification threshold.
- State money-transmitter licensing notification obligations per state where applicable.

The IR drill scope before go-live should exercise at minimum one payments-or-fintech-specific incident class (e.g., confirmed Reg E timeline failure in AI-assisted dispute handling; confirmed UDAAP-relevant misleading communication; confirmed BSA programme-integrity issue in AI-assisted transaction monitoring; sponsor-bank-relationship-relevant confirmed event for BaaS use cases).

#### Recommended-action items the overlay surfaces

- Where the use case is sponsor-bank-relationship-dependent, the BaaS or sponsor-bank relationship file is updated to reference the gate review and the sponsor bank's co-acceptance is recorded.
- Where the use case touches AI-assisted dispute handling, the Reg E error-resolution workflow and the provisional-credit clock are documented as not affected by AI handling latency.
- Where the use case touches UDAAP-relevant customer communications, consumer compliance signs off on the output-filter specification and on the complaint-channel readiness.
- Where the use case touches BSA-relevant transaction monitoring or SAR drafting, the BSA officer co-signs and BSA-relevant monitoring signals are live before go-live.
- Where the entity holds multiple state money-transmitter licences, the state-by-state notification matrix and the licensing-variation matrix are documented.

#### Common pitfalls specific to payments-fintech gate reviews

- Treating a sponsor-bank-relationship use case as if the firm has unilateral gate decision authority. The sponsor bank's own AI governance and model risk functions co-accept by relationship agreement; an unaccepted gate decision in the sponsor bank is not a firm-side go.
- Omitting the Reg E error-resolution timeline analysis for AI-assisted dispute handling. The 10-day provisional-credit clock and the 45-day resolution clock are statutory and run independently of AI handling; AI latency or handling failure does not toll the clock.
- Treating UDAAP exposure on AI-generated customer communications as a downstream consumer-compliance review. UDAAP is the seat consumer compliance owns at the gate, not after; the gate decision is incomplete without consumer compliance sign-off.
- Treating a fraud-detection or transaction-monitoring augmentation as a control improvement without baseline-against-prior-system evidence. A new AI augmentation that improves alert quality while shifting false negatives in BSA-relevant patterns is a programme-integrity issue; the gate review records the regression test explicitly.
- Treating multi-state money-transmitter licensing as a uniform compliance posture. State licensing terms, notification obligations, and supervisory examination postures vary; the gate review records state-by-state status.
- Relying on sponsor-bank evidence as substituting for firm-side gate evidence. Sponsor-bank evidence is one input; the firm-side gate items are firm-side responsibilities.
