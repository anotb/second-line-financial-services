# Cross-cutting overlay: privacy

Loaded when `scope.cross_cutting_overlay_set` includes privacy. Carries the data-handling, training-data sourcing, prompt-confidentiality, and consumer-rights frame for foundation-model vendor evidence-pack review.

## Supervisory frame

The privacy framings most often in scope for foundation-model deployments by financial-services entities:

- **GLBA and the FTC Safeguards Rule** (16 CFR Part 314) and Privacy Rule (16 CFR Part 313, where the entity is in FTC scope) for non-public personal information. NPI flowing to vendor prompts triggers Safeguards Rule considerations and, since May 2024, the §314.5(d) notification posture.
- **HIPAA Privacy Rule and Security Rule** (45 CFR Parts 160, 164) for entities handling PHI in health-touching deployments (life and health insurers, certain bank wealth and trust businesses with health-relevant clients). Vendor evidence-pack review for any PHI-touching deployment surfaces the business-associate-agreement posture.
- **State comprehensive privacy laws** (California CCPA/CPRA, Colorado CPA, Connecticut CTDPA, Virginia VCDPA, and the growing list as of the skill's authoring) for consumer personal information of state residents. The financial-institution exemptions in many state laws are scoped narrowly; non-GLBA-scoped data may still fall in.
- **GDPR and UK GDPR** for entities processing personal data of EU and UK data subjects, including AI-Act-adjacent obligations on automated decision-making and profiling.
- **State biometric-information laws** (Illinois BIPA, Texas, Washington) where biometric data may flow through the deployment.
- **State Insurance Data Security Model Law** for insurers in adopted states.

The cyber overlay (§500.17(a) NYDFS, GLBA §314.5(d), 36-hour banking incident notification, SEC 8-K Item 1.05, state breach laws) carries the incident-notification mechanics; the privacy overlay carries the data-handling, retention, training-data, and consumer-rights frame.

## Privacy-specific evidence asks

The privacy overlay surfaces the following beyond the cross-cutting baseline in the privacy-posture, training-data-posture, and abuse-monitoring-and-data-retention criteria:

- **Default-retention posture for prompts and outputs.** Vendor evidence on the default-zero-retention or default-short-window-retention posture for the contract tier in scope. Where the default does not match the firm's policy, the firm-side architecture (gateway, prompt-stripping, redaction at ingress) carries the obligation; record the responsibility shift.

- **Abuse-monitoring exception scope.** Most enterprise foundation-model contracts define an exception to default-zero-retention for abuse-monitoring purposes (vendor humans review flagged inputs under defined conditions). The privacy overlay records the named exception scope and the firm-side controls that limit data exposure (prompt scrubbing, classifier-based pre-flagging, contractual carve-outs for highly sensitive data classes).

- **Training-data sourcing posture.** Vendor evidence on whether customer prompts and outputs are used for vendor-side training. The standard enterprise-tier posture is no-training-on-customer-data with limited exceptions; record the contract-specific posture.

- **Sub-processor list and notification cadence.** Vendor's published sub-processor list (cloud infrastructure, evaluation contractors, support tooling) and the notification cadence for sub-processor changes. Material for GDPR-scope deployments and for state-comprehensive-privacy-law-scope deployments.

- **Data-residency posture.** Where the vendor offers regional pinning or dedicated capacity, the in-firm deployment context determines whether residency matters (cross-border-flow-restricted use cases, EU-data-subject use cases, sector-specific residency requirements).

- **Consumer-rights posture for state-comprehensive-privacy-law in-scope data.** Vendor's posture on supporting the firm's obligations around access, deletion, correction, and opt-out where the vendor processes consumer personal information; for most foundation-model deployments the vendor's posture is "the firm controls the data plane and bears the consumer-rights obligation", but the contract-allocation should be explicit.

- **HIPAA business-associate posture.** For PHI-touching deployments, the vendor's willingness to sign a business-associate agreement, the BAA's scope and limitations, and the vendor's HIPAA-relevant security posture under 45 CFR §164.308 to §164.312.

- **Children's information posture.** Where the use case may incidentally touch information of minors, COPPA implications carry weight; rare in second-line FS contexts but recorded where applicable.

## Privacy-specific co-reviewer expectations

The chief privacy officer or named privacy function is a co-reviewer for any deployment where NPI, PHI, biometric information, or state-comprehensive-privacy-law in-scope data flows to vendor-side processing. The privacy function attests jointly with the AI Governance Lead on `reviewer_attestation`. For HIPAA-scope deployments, the privacy officer (HIPAA-compliant function) holds a co-attestation gate.

## Privacy-specific re-review triggers

In addition to the baseline triggers, privacy adds:

- Vendor change to default-retention posture, abuse-monitoring exception scope, training-data sourcing posture, or sub-processor list.
- New or revised state comprehensive privacy law in a binding state, or amendment to GLBA, HIPAA, or sector-specific privacy regimes materially affecting vendor posture.
- Vendor incident disclosure involving customer data of any classification.
- Material change in the firm's deployment context affecting data-class flow (new RAG corpora containing regulated data, new use cases handling PHI or NPI).
- Cross-border flow change in vendor architecture or in firm deployment.

## Privacy-specific structured-output additions

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
