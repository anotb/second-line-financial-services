# Privacy cross-cutting overlay for genai-pre-prod-review

When the engagement-scope record flags `privacy` for a pre-prod gate review, this overlay adds privacy-specific gate considerations: Privacy Officer co-review, regulated-data-handling expectations, additional notification triggers, and recommended-action items typical of privacy-flagged GenAI gate reviews. Loaded for any use case handling NPI, PHI, biometric data, or other regulated personal data with potential for inappropriate disclosure or use.

Loaded by: `genai-pre-prod-review/SKILL.md` when `engagement_scope.cross_cutting_set` includes `privacy`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- GLBA Safeguards Rule (16 CFR Part 314), as amended December 2021, with FTC notification provisions added October 2023 effective May 2024 (16 CFR §314.5(d)).
- GLBA Privacy Rule (16 CFR Part 313 and parallel federal-banking-agency rules at 12 CFR Part 1016) for the consumer-privacy notice and information-sharing framing.
- HIPAA Privacy Rule (45 CFR Part 164) and Security Rule (45 CFR Part 164 Subpart C) for PHI under covered-entity or business-associate relationships.
- HIPAA Breach Notification Rule (45 CFR §§164.400-414) for PHI exfiltration events.
- SEC Reg S-P (17 CFR Part 248) for broker-dealer and investment-adviser customer-information privacy.
- State comprehensive privacy laws (CCPA / CPRA in California, VCDPA in Virginia, CPA in Colorado, CTDPA in Connecticut, UCPA in Utah, and the growing state patchwork) where consumer rights and data-handling obligations apply.
- State biometric privacy laws (BIPA in Illinois and analogues) where the use case handles biometric data.
- State breach-notification laws (50-state patchwork; the firm's privacy programme maintains the state-by-state matrix).
- For NY-licensed entities: NYDFS 23 NYCRR Part 500 cybersecurity-and-privacy intersection; NYDFS Insurance Circular Letter (January 2024) for ECDIS and underwriting privacy considerations.
- COPPA (15 USC §6501-6506) where the use case may interact with content from users under 13.

## Co-reviewer expectation

The Privacy Officer is a co-signer on the gate decision for any privacy-flagged use case. The reviewer-attestation block names the Privacy Officer explicitly. For HIPAA-relevant use cases, the privacy-officer role is typically the HIPAA Privacy Official; for GLBA-only use cases the role may be a privacy lawyer or chief privacy officer depending on firm structure.

For tier-1 use cases handling regulated personal data, the data protection officer (where the firm has one), the records-management function (for retention and deletion), and the consumer-recourse function (for consumer-rights handling) are also expected at gate time.

## What changes when privacy is flagged

### Open conditions the overlay typically adds

- Data-minimisation review: the gate review documents that the data the model consumes (training, retrieval corpora, prompt context, persistent memory) is the minimum necessary for the use case purpose. Excess data in the prompt path is a structural risk multiplier for exfiltration events.
- Retention review: documented retention period for prompt logs, retrieved content snapshots, output artefacts, and any persistent memory; alignment with regulator-required minima and firm policy.
- Consent and notice posture review: where the use case consumes content covered by an applicable privacy notice (GLBA notice, HIPAA notice of privacy practices, CCPA disclosure), the use of the data for AI processing is consistent with the notice.
- For HIPAA covered entities: business-associate agreement coverage for any vendor in the AI processing path (foundation-model provider, retrieval infrastructure, observability tools).
- For state-comprehensive-privacy-law footprint: consumer-rights-handling workflow (access, deletion, correction, opt-out of certain processing) covers AI artefacts where applicable; deletion requests propagate to retrieved content snapshots and persistent memory.
- For biometric-data use cases: BIPA-and-analogue consent capture and retention-schedule documentation.

### Monitoring readiness adds the privacy-tagged signal set

In addition to the standard signal set:

- Cross-record retrieval audit signal where the architecture handles regulated personal data (per-customer query scoping, per-claim query scoping, per-policy query scoping); any confirmed cross-record event is a privacy investigation trigger.
- PHI / NPI / biometric-data exfiltration leading-indicator signals (anomalous output length, unusual identifier surface in output, output-content sampling for regulated-data tokens).
- Consumer-rights-handling SLA tracking where applicable; escalation to the Privacy Officer.
- Retention-policy-violation signal: outputs or prompt logs retained beyond policy are themselves a privacy event.

### Incident-response readiness names privacy-specific notification triggers

The `incident_response_readiness.regulator_notification_triggers` list adds:

- HIPAA Breach Notification Rule (45 CFR §§164.400-414) for PHI exfiltration or unauthorised use; notification to affected individuals, HHS, and in some cases the media.
- GLBA Safeguards Rule notification under 16 CFR §314.5(d): FTC notification for unauthorised acquisition of unencrypted customer information of 500 or more consumers; required for FTC-scope financial institutions.
- State breach-notification laws: per state, with timing and scope variation; the firm's matrix is the reference.
- For state-comprehensive-privacy-law footprint: where applicable, state Attorney General notification per state law.
- For NY-licensed entities: NYDFS §500.17(a) overlap with privacy-tagged events that meet the cybersecurity-event criteria.
- COPPA-related notification where the use case interacts inappropriately with under-13 content.

The IR drill scope before go-live should exercise at minimum one privacy-specific incident class (e.g., confirmed cross-record disclosure of regulated personal data; confirmed PHI exfiltration via output channel; confirmed biometric-data inappropriate retention).

### Recommended-action items the overlay surfaces

- For HIPAA-relevant use cases: HIPAA breach-notification process rehearsal as part of the IR drill scope; business-associate agreement coverage documented for all vendors in the processing path.
- For GLBA Safeguards Rule entities: notification-decision process rehearsal for FTC notification under 16 CFR §314.5(d).
- For state-comprehensive-privacy-law footprint: consumer-rights-handling workflow updated to cover AI artefacts; deletion-request propagation documented.
- For biometric-data use cases: BIPA-and-analogue consent capture and retention-schedule documented.
- Data-minimisation and retention review documented; signed off by the Privacy Officer.

## Privacy-specific output additions

In the structured object (`schemas/genai-pre-prod-review.schema.json`):

- `cross_cutting_overlay_notes.privacy` carries privacy-specific fields: data-minimisation review status, retention review status, consent and notice posture review status, business-associate agreement coverage status, consumer-rights-handling workflow status.
- `signoff[]` array includes the Privacy Officer as a co-signer.
- `monitoring_readiness[]` entries with privacy-tagged escalation path (Privacy Officer, data protection officer where applicable).
- `incident_response_readiness.regulator_notification_triggers` populated with the named privacy-specific triggers.
- `overlay_signoffs[]` includes a privacy entry with named owner role.

## Common pitfalls in privacy-flagged pre-prod gate reviews

- Treating data minimisation as a downstream control. The data the model consumes is the structural risk surface for exfiltration; minimisation is a gate-time decision, not a post-go-live optimisation.
- Omitting the business-associate agreement check for HIPAA-relevant use cases. Every vendor in the processing path (foundation-model provider, retrieval infrastructure, observability) needs BAA coverage; a vendor in the path without a BAA is a HIPAA programme issue.
- Treating state-comprehensive-privacy-law consumer-rights handling as out-of-scope for AI artefacts. Deletion requests need to propagate to retrieved content snapshots and persistent memory; access requests need to handle AI-generated output where it constitutes personal data.
- Treating retention as policy without runtime enforcement. Retained-beyond-policy prompt logs and output artefacts are themselves a privacy event; the retention policy needs runtime enforcement and the gate review records the enforcement evidence.
- Recording vendor system card statements about training-data privacy as substituting for firm-side data-minimisation review. Vendor practices on training data are one consideration; the firm's prompt-path data minimisation is firm-side responsibility.
- Failing to involve the Privacy Officer at gate time. A privacy-flagged use case without Privacy Officer sign-off proceeds with unaccepted privacy residual risk; the gate decision is incomplete.
