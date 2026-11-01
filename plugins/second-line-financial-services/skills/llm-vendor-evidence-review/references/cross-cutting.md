# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Cross-cutting overlay: conduct

Loaded when `scope.cross_cutting_overlay_set` includes conduct. Carries the responsible-use, harmful-content, and customer-conduct frame for foundation-model vendor evidence-pack review. Scopes in for any deployment touching customer-facing communications, recommendation, or decisioning.

#### Supervisory frame

The conduct framings most often in scope:

- **CFPB Circulars and supervisory highlights** for entities in CFPB scope. The adverse-action notice circular, the chatbot circular, and named circulars on AI-driven decisioning carry the CFPB's published views on AI-vendor decisions affecting consumers.
- **UDAAP** (Dodd-Frank §1031, §1036, FTC Act §5) reaches AI-driven content and decisioning that may be unfair, deceptive, or abusive. Foundation-model behaviour around hallucination, off-label financial advice, and refusal-around-restricted-content feeds the firm's UDAAP exposure assessment.
- **Fair-lending regimes** (ECOA / Reg B, FHA, state analogues) for any AI-vendor use in credit decisioning, marketing, or adverse-action determinations.
- **Telephone and electronic-communication regimes** (TCPA, CAN-SPAM, state anti-robocall) for AI-vendor use in customer outreach, where the model produces or selects message content.
- **State UDAP regimes** that layer on for state-licensed entities.
- **Sector-specific conduct regimes**: SEC Marketing Rule and FINRA Rule 2210 for capital-markets entities (carried in the capital-markets sector overlay); NAIC Unfair Trade Practices model and state insurance unfair-trade-practices acts for insurers; CFPB Regulation Z and Regulation E disclosures for consumer credit and electronic fund transfers.

The leading-practice references with weight in this scope: NIST AI 600-1 Manage subcategories on harmful-content management; vendor-published responsible-use policies and acceptable-use rules; vendor-published trust-and-safety pages on harm taxonomies and refusal behaviour.

#### Conduct-specific evidence asks

The conduct overlay surfaces the following beyond the cross-cutting baseline in the responsible-use-policy, evaluation-coverage (harmful-content-specific), and dangerous-capability-evaluations criteria:

- **Vendor harmful-content evaluation depth.** Vendor's published evaluation methodology and results on harmful-content categories relevant to the firm's deployment: financial-services-specific harmful content (off-label investment advice, unauthorised regulated-product solicitation, fabricated terms), consumer-protection-relevant content (false promises, misleading product descriptions, misrepresentation), conduct-relevant content (harassment, discriminatory output, off-policy solicitation). General-purpose harmful-content evaluation is starting context; financial-services-specific or domain-specific coverage is firm-side responsibility under `validation-plan` if vendor coverage is partial.

- **Refusal-behaviour calibration around restricted-use categories.** Vendor's published refusal-behaviour around regulated activities the firm is exposed to (giving investment advice, making loan-eligibility determinations, medical claims, immigration claims, legal advice). Where vendor refusal-behaviour is calibrated to categories the firm wants the model to engage with, the firm-side prompting and downstream-control architecture carries the responsibility; record the gap.

- **Adverse-action and explanation-depth posture.** For AI-vendor use in or adjacent to credit, insurance underwriting, or consumer-financial-services decisioning, vendor evidence on output-explanation-depth and refusal-around-determinative-statements feeds the firm's adverse-action-notice and reason-code obligations. The CCO and consumer-compliance function carry the regulatory-fit assessment; the evidence-pack review surfaces the inputs.

- **Marketing and communications posture.** Vendor's posture on output-control around marketing-relevant content (testimonials, performance claims, recommendations), and the vendor's acceptable-use rules around the use of the model for marketing automation. For SEC/FINRA-scope entities, this routes to the capital-markets sector overlay; for retail consumer-financial-services entities, the firm's marketing compliance function is in the room.

- **Bias and fairness evidence relevant to the deployment.** Vendor's published bias evaluations and fairness methodology; in many cases generic and not domain-specific, in which case domain-specific evaluation under `validation-plan` carries the firm-side coverage. For insurance and consumer-credit deployments the sector overlays add specific elements.

- **Acceptable-use enforcement posture.** Vendor's process for monitoring and enforcing its acceptable-use policy: how the vendor identifies misuse, what enforcement actions are available, how disputes are handled. Material for the firm's understanding of vendor reliability around restricted-use categories and for the firm's own enforcement of its acceptable-use policy.

#### Conduct-specific co-reviewer expectations

The CCO is a co-reviewer for any deployment touching consumer-facing communications, recommendation, or decisioning. For sector-specific conduct overlays (SEC Marketing Rule, FINRA Rule 2210, NAIC unfair trade practices), the relevant sector function is in the room. For BSA-relevant decisioning, the BSA officer is in the room (and is also a co-reviewer per the payments-fintech sector overlay where applicable).

The consumer compliance function (Fair Lending officer, ECOA-compliance officer where named) co-reviews where the deployment touches credit decisioning or fair-lending-relevant decisioning. The CCO and the AI Governance Lead jointly attest on `reviewer_attestation`; for fair-lending-touching deployments the consumer-compliance function joins the attestation gate.

#### Conduct-specific re-review triggers

In addition to the baseline triggers, conduct adds:

- New or revised CFPB circular, FTC enforcement guidance, or sector-specific conduct rule materially affecting AI-vendor decisions in scope.
- Vendor change to acceptable-use policy, responsible-use policy, restricted-use enforcement, or harmful-content evaluation methodology.
- Vendor incident or supervisory action involving conduct-relevant outputs.
- Material change in the deployment scope towards consumer-facing communication or decisioning.

#### Conduct-specific structured-output additions

The `cross_cutting_overlay_notes.conduct` block in the schema carries the conduct-specific findings:

```
"cross_cutting_overlay_notes": {
  "conduct": {
    "harmful_content_evaluation_summary": "...",
    "refusal_behaviour_calibration_summary": "...",
    "adverse_action_explanation_depth": "...",
    "marketing_and_communications_posture": "...",
    "bias_and_fairness_evidence_summary": "...",
    "acceptable_use_enforcement_posture": "...",
    "udaap_exposure_input": "...",
    "consumer_compliance_function_attestation_status": "..."
  }
}
```

## cyber

### Cross-cutting overlay: cyber

Loaded when `scope.cross_cutting_overlay_set` includes cyber. The cyber overlay should be considered the default for foundation-model evidence-pack reviews; the threat surface a foundation-model vendor exposes is, in regulator framing, a cybersecurity risk class. The CISO function is a co-reviewer for the security and privacy criteria.

#### Supervisory frame

The cyber framings carrying binding supervisory expectation in their respective scopes:

- **NYDFS 23 NYCRR Part 500** for NY-footprint covered entities (state-chartered banks, insurers, money transmitters, virtual currency businesses operating in NY). The October 2024 Industry Letter on Cybersecurity Risks Arising from AI extends Part 500 application to AI-specific risks including third-party AI service-provider security under §500.11.
- **SEC cyber disclosure rules** (Reg S-K Item 106, Form 8-K Item 1.05) for SEC public registrants, where a vendor-AI incident contributes to a material cybersecurity incident requiring disclosure.
- **GLBA Safeguards Rule** (16 CFR Part 314) for FTC-supervised non-bank financial institutions, including the May 2024 notification provisions (16 CFR §314.5(d)) for unencrypted-customer-information events affecting 500 or more consumers.
- **State Insurance Data Security Model Law** (NAIC Model Law 668) for insurers in adopted states.
- **FFIEC IT Examination Handbook** for federally supervised banks; the Information Security and Architecture, Infrastructure, and Operations booklets carry application-security and third-party-risk sections relevant to AI-vendor posture.
- **The 36-hour banking computer-security incident notification rule** (12 CFR Part 53, with parallel FRB and FDIC rules) for bank-affiliated entities, where a vendor-AI incident constitutes a notification incident.

The leading-practice references that carry weight without being binding: NIST AI 600-1 Generative AI Profile (Govern 6.x for third-party considerations and Manage 3.x for incident-disclosure expectations); NIST SP 800-53 (control families for the cyber-side of vendor evidence: AC, AU, IR, SI, SR); ISO/IEC 27001/27002 and SOC 2 Trust Service Criteria as the third-party attestation frame.

#### Cyber-specific evidence asks

The cyber overlay surfaces the following beyond the cross-cutting baseline in the security-posture and privacy-posture criteria:

- **Authentication and authorisation posture for the model-serving endpoint.** Vendor evidence should establish identity and access controls on the API or serving plane; SOC 2 Type II covers the operating effectiveness of these controls in the relevant period. The complementary user-entity controls section of SOC 2 names the firm-side responsibilities; record acceptance of those by the firm's CISO function.

- **Audit logging of model invocations and retrievals.** Vendor evidence should establish what is logged, by whom, with what retention. The firm's incident-response capability depends on log-availability; vendor opacity here is a cyber-side gap that limits the firm's incident-investigation depth.

- **Model supply-chain controls.** Foundation-model vendors depend on training-data sources, evaluation contractors, red-team contractors, cloud infrastructure. The supply-chain posture of the model itself is part of the cyber assessment; the SR control family in NIST SP 800-53 frames the asks.

- **Adversarial-robustness evidence.** The vendor's published red-team summary, dangerous-capability evaluations, and jailbreak-resistance benchmarks feed the firm's understanding of the cyber-relevant adversarial profile. These are vendor self-attestation; record at vendor-self-attestation confidence and chain to `prompt-injection-risk` for in-firm coverage of the deployed system.

- **Incident-disclosure history and notification-cadence posture.** The vendor's historical incident disclosures and the cadence and granularity of disclosure feed the firm's ability to meet its own regulator-notification obligations. Where the vendor's notification cadence is loose, the firm's disclosure posture under §500.17(a), Item 1.05, GLBA §314.5(d), and the 36-hour banking rule is at risk; record the residual reliance.

- **Network controls and data-isolation posture.** For hosted-API forms, the network-isolation posture (regional pinning, VPC peering, dedicated capacity options) feeds the firm's data-residency and data-isolation posture; the privacy overlay carries the residency specifics.

- **Secrets-handling posture.** API keys, signing keys, customer-data-encryption keys: the vendor's posture on secrets handling and rotation feeds the firm's CISO assessment.

#### Cyber-specific co-reviewer expectations

The CISO function is a co-reviewer for the security-posture, privacy-posture, content-provenance, and incident-disclosure-history criteria of `sufficiency_view[]`. The CISO function attests jointly with the AI Governance Lead on `reviewer_attestation`. For NY-footprint entities, the Part 500 CISO sign-off responsibility extends to the AI-vendor evidence review; record alignment with the CISO function's annual certification cycle.

#### Cyber-specific re-review triggers

In addition to the baseline triggers, cyber adds:

- Vendor-disclosed cybersecurity incident affecting the model variant in scope or the underlying serving plane.
- New cybersecurity-related supervisory action (NYDFS, federal banking, SEC) referencing the vendor or vendor class.
- Material change in the vendor's SOC 2 scope, control objectives, or auditor opinion.
- Material change in the vendor's API security posture, authentication mechanism, or default network controls.
- Disclosure of a vulnerability or compromise affecting the vendor's adversarial-robustness controls.

#### Cyber-specific structured-output additions

The `cross_cutting_overlay_notes` block in the schema carries the cyber-specific findings:

```
"cross_cutting_overlay_notes": {
  "cyber": {
    "soc2_summary": "...",
    "iso27001_summary": "...",
    "authn_authz_posture": "...",
    "audit_logging_depth": "...",
    "model_supply_chain_posture": "...",
    "adversarial_robustness_evidence_summary": "...",
    "incident_disclosure_cadence": "...",
    "network_isolation_posture": "...",
    "secrets_handling_posture": "...",
    "ny_part500_alignment_status": "...",
    "sec_8k_item105_materiality_input": "...",
    "glba_safeguards_rule_alignment": "...",
    "ciso_attestation_status": "..."
  }
}
```

## privacy

### Cross-cutting overlay: privacy

Loaded when `scope.cross_cutting_overlay_set` includes privacy. Carries the data-handling, training-data sourcing, prompt-confidentiality, and consumer-rights frame for foundation-model vendor evidence-pack review.

#### Supervisory frame

The privacy framings most often in scope for foundation-model deployments by financial-services entities:

- **GLBA and the FTC Safeguards Rule** (16 CFR Part 314) and Privacy Rule (16 CFR Part 313, where the entity is in FTC scope) for non-public personal information. NPI flowing to vendor prompts triggers Safeguards Rule considerations and, since May 2024, the §314.5(d) notification posture.
- **HIPAA Privacy Rule and Security Rule** (45 CFR Parts 160, 164) for entities handling PHI in health-touching deployments (life and health insurers, certain bank wealth and trust businesses with health-relevant clients). Vendor evidence-pack review for any PHI-touching deployment surfaces the business-associate-agreement posture.
- **State comprehensive privacy laws** (California CCPA/CPRA, Colorado CPA, Connecticut CTDPA, Virginia VCDPA, and the growing list as of the skill's authoring) for consumer personal information of state residents. The financial-institution exemptions in many state laws are scoped narrowly; non-GLBA-scoped data may still fall in.
- **GDPR and UK GDPR** for entities processing personal data of EU and UK data subjects, including AI-Act-adjacent obligations on automated decision-making and profiling.
- **State biometric-information laws** (Illinois BIPA, Texas, Washington) where biometric data may flow through the deployment.
- **State Insurance Data Security Model Law** for insurers in adopted states.

The cyber overlay (§500.17(a) NYDFS, GLBA §314.5(d), 36-hour banking incident notification, SEC 8-K Item 1.05, state breach laws) carries the incident-notification mechanics; the privacy overlay carries the data-handling, retention, training-data, and consumer-rights frame.

#### Privacy-specific evidence asks

The privacy overlay surfaces the following beyond the cross-cutting baseline in the privacy-posture, training-data-posture, and abuse-monitoring-and-data-retention criteria:

- **Default-retention posture for prompts and outputs.** Vendor evidence on the default-zero-retention or default-short-window-retention posture for the contract tier in scope. Where the default does not match the firm's policy, the firm-side architecture (gateway, prompt-stripping, redaction at ingress) carries the obligation; record the responsibility shift.

- **Abuse-monitoring exception scope.** Most enterprise foundation-model contracts define an exception to default-zero-retention for abuse-monitoring purposes (vendor humans review flagged inputs under defined conditions). The privacy overlay records the named exception scope and the firm-side controls that limit data exposure (prompt scrubbing, classifier-based pre-flagging, contractual carve-outs for highly sensitive data classes).

- **Training-data sourcing posture.** Vendor evidence on whether customer prompts and outputs are used for vendor-side training. The standard enterprise-tier posture is no-training-on-customer-data with limited exceptions; record the contract-specific posture.

- **Sub-processor list and notification cadence.** Vendor's published sub-processor list (cloud infrastructure, evaluation contractors, support tooling) and the notification cadence for sub-processor changes. Material for GDPR-scope deployments and for state-comprehensive-privacy-law-scope deployments.

- **Data-residency posture.** Where the vendor offers regional pinning or dedicated capacity, the in-firm deployment context determines whether residency matters (cross-border-flow-restricted use cases, EU-data-subject use cases, sector-specific residency requirements).

- **Consumer-rights posture for state-comprehensive-privacy-law in-scope data.** Vendor's posture on supporting the firm's obligations around access, deletion, correction, and opt-out where the vendor processes consumer personal information; for most foundation-model deployments the vendor's posture is "the firm controls the data plane and bears the consumer-rights obligation", but the contract-allocation should be explicit.

- **HIPAA business-associate posture.** For PHI-touching deployments, the vendor's willingness to sign a business-associate agreement, the BAA's scope and limitations, and the vendor's HIPAA-relevant security posture under 45 CFR §164.308 to §164.312.

- **Children's information posture.** Where the use case may incidentally touch information of minors, COPPA implications carry weight; rare in second-line FS contexts but recorded where applicable.

#### Privacy-specific co-reviewer expectations

The chief privacy officer or named privacy function is a co-reviewer for any deployment where NPI, PHI, biometric information, or state-comprehensive-privacy-law in-scope data flows to vendor-side processing. The privacy function attests jointly with the AI Governance Lead on `reviewer_attestation`. For HIPAA-scope deployments, the privacy officer (HIPAA-compliant function) holds a co-attestation gate.

#### Privacy-specific re-review triggers

In addition to the baseline triggers, privacy adds:

- Vendor change to default-retention posture, abuse-monitoring exception scope, training-data sourcing posture, or sub-processor list.
- New or revised state comprehensive privacy law in a binding state, or amendment to GLBA, HIPAA, or sector-specific privacy regimes materially affecting vendor posture.
- Vendor incident disclosure involving customer data of any classification.
- Material change in the firm's deployment context affecting data-class flow (new RAG corpora containing regulated data, new use cases handling PHI or NPI).
- Cross-border flow change in vendor architecture or in firm deployment.

#### Privacy-specific structured-output additions

The `cross_cutting_overlay_notes.privacy` block in the schema carries the privacy-specific findings:

```
"cross_cutting_overlay_notes": {
  "privacy": {
    "default_retention_posture": "...",
    "abuse_monitoring_exception_scope": "...",
    "training_data_sourcing_posture": "...",
    "subprocessor_list_summary": "...",
    "subprocessor_notification_cadence": "...",
    "data_residency_posture": "...",
    "consumer_rights_allocation": "...",
    "hipaa_baa_status": "...",
    "in_scope_data_classes": [...],
    "privacy_function_attestation_status": "..."
  }
}
```
