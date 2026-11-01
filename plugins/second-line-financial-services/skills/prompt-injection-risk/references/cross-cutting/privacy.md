# Privacy cross-cutting overlay for prompt-injection-risk

When the scope record flags `privacy` for a prompt-injection review, this overlay loads alongside the cyber overlay (which is the default cross-cutting lens on this skill). Privacy is not a secondary concern. Prompt injection has three load-bearing privacy paths: training-data and prompt-history extraction (the model emits content that the firm has stored, sometimes regulated personal data, sometimes another customer's data), retrieval exfiltration (the system surfaces RAG-corpus content the requesting user is not authorised to read), and tool-driven personal-data egress (an injected instruction directs a tool call that exfiltrates regulated personal data to an attacker-controlled destination). The privacy function is a co-reviewer on any review where these paths are material.

Loaded by: `prompt-injection-risk/SKILL.md` when `scope.cross_cutting_set` includes `privacy`. For any GenAI use case touching NPI, PHI, PCI, biometric data, customer prompts that may contain regulated personal data inadvertently (claims FNOL, customer-support chats, RAG-over-customer-documents flows), this overlay should be considered the default. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- **GLBA Safeguards Rule, 16 CFR Part 314 (FTC scope) and the interagency Safeguards rule for banks** — §314.4 program elements, §314.4(c) access controls and encryption, §314.4(d) monitoring and testing, §314.4(f) service-provider obligations, §314.5(d) FTC notification of notification events involving the unauthorised acquisition of unencrypted customer information of 500 or more consumers.
- **GLBA Privacy Rule, Regulation P, 12 CFR Part 1016** — privacy-notice and information-sharing posture; relevant where prompt content or model output flows into a service-provider chain.
- **HIPAA Privacy and Security Rules, 45 CFR Parts 160, 162, and 164** — where prompts or model outputs may carry PHI (claims-handling assistants, member-services chatbots, life and health underwriting copilots), the BAA chain to the foundation-model provider, the inference-platform provider, and any retrieval / vector-database vendor is required. Model outputs derived from PHI inherit PHI status; retention of outputs is a HIPAA business-associate question.
- **State comprehensive privacy laws** — CCPA / CPRA (California), VCDPA (Virginia), CTDPA (Connecticut), CPA (Colorado), and the rolling list. GLBA-covered data is excluded from many state regimes but the GLBA-exemption scope is read state-by-state and feature-by-feature; prompt-history retention often crosses the GLBA-covered scope into general personal-data territory (employee identifiers, free-text input outside transaction context).
- **FCRA, 15 USC §1681, and Regulation V, 12 CFR Part 1022** — where the AI surface consumes consumer-report data (a prompt to "summarise this credit report" or a RAG corpus including consumer-report excerpts), FCRA reach attaches to the surface and to the audit trail.
- **Reg S-P, 17 CFR §248.30 (May 2024 amendments)** [verify exact compliance dates by entity type and size] — for SEC-registered advisers, BDs, and funds, customer-information-safeguarding and breach-notification posture; service-provider written contracts requiring breach notification.
- **NYDFS 23 NYCRR Part 500 §500.13 and §500.15** — access controls and encryption requirements bearing on prompt-content access and storage; the privacy frame layers on top of the cyber-program frame.
- **GDPR / UK GDPR** — for systems with EU / UK exposure, Article 5 principles (purpose limitation, data minimisation, storage limitation), Article 22 automated-decision-making, Article 28 processor relationships, Article 32 security of processing. Data Protection Impact Assessment under Article 35 is the parallel artifact; the prompt-injection review is one input where the DPIA covers the GenAI use case.

## What changes when privacy is flagged

### 1. Threat surface gains a privacy-tagging convention

Each carrier in the threat-surface table is tagged with the personal-data classes it may carry and the lawful basis under which the system processes them. The user-input carrier ties to NPI / PHI / employee data (the customer or employee typed it); the retrieved-content carrier ties to whatever personal data the RAG corpus contains; the tool-output carrier ties to whatever the tool returns from a system-of-record; the memory carrier ties to the personal-data classes the memory retains across sessions. The trust-basis column reads alongside the lawful-basis column: a carrier marked "trusted, no controls" with PHI in its content is a privacy finding before it is a cyber finding.

### 2. Tested attack classes expand to include personal-data extraction paths

The AI-native attack classes (direct override, indirect injection, system-prompt exfiltration, jailbreak, tool hijack, agent redirect, multi-agent message injection, multimodal injection, memory poisoning) carry through; the privacy overlay adds explicit testing for the personal-data extraction surface:

- **Training-data extraction** (model recites training content verbatim under adversarial prompting). Vendor red-team coverage on base-model training-data extraction is vendor-side evidence; the firm's deployed system extends the surface (firm fine-tuning data, firm RAG content) and needs firm-side testing.
- **Cross-tenant / cross-user retrieval exfiltration** (the model returns RAG content the requesting user is not authorised to read). The retrieval-source authorisation model is the seam; testing exercises whether instruction-following can defeat the authorisation check.
- **Memory cross-contamination** (one user's session content leaks into another user's session via shared memory). Exercises the isolation boundary on persistent-memory systems.
- **Tool-driven personal-data egress** (the model issues a tool call that exfiltrates personal data to a non-firm destination). Exercises the tool authorisation surface and the network-egress controls.
- **Output-channel exfiltration** (the model encodes personal data into outputs intended to flow to attacker-readable channels — log lines, error messages, audit trails). Exercises the output-routing surface.

The `dataset_or_redteam_ref` field on these attack classes names the source explicitly: vendor red-team coverage on the base model is named as such; firm-side coverage on the deployed-system surface is named separately; published research benchmarks (TruthfulQA, AnthropicEval, MITRE ATLAS adversarial test suites) are named where the firm's red team consumed them.

### 3. Mitigations expand to include the standard privacy control set

In addition to the AI-native and cyber-tagged mitigations, the privacy overlay expects the review to record:

- **Prompt-content classification at intake**: detection of NPI / PHI / PCI in user input before model invocation; routing to redaction, masking, or refuse-to-process per policy.
- **Retention windows on prompt content and model output**: zero retention, configurable retention, vendor default with abuse-monitoring exception, firm-side audit-log retention. The contract clause and the trust-and-safety pages set the operative posture; marketing copy is not evidence.
- **Training-use posture**: vendor-default opt-out for enterprise contracts is the normal frame, but the contract clause (not the marketing page) is what binds. The review records the contract reference and the effective date.
- **Customer-data isolation**: fine-tune data and RAG-context data isolated from other tenants; multi-tenant models with shared training pools change the privacy calculus.
- **Output-retention and downstream propagation**: where the model output flows into a downstream system, the privacy posture of the downstream system extends the surface.
- **Cross-border egress controls**: prompt processing in non-firm-permitted regions is a residency violation; region-pinning evidence (region tags, transfer-restriction enforcement, data-residency reports) is recorded.
- **Right-to-deletion and right-to-correction handling**: how the firm responds to a data-subject-rights request when the data may have flowed through prompt history, fine-tuning, or retention windows; the contractual mechanism with the foundation-model and inference-platform vendors.
- **Sub-processor list and change-notice mechanism**: the foundation-model provider's sub-processors and the inference-platform provider's sub-processors are named.
- **PIA / DPIA coverage**: where the firm's privacy program requires a PIA for use cases meeting the threshold, the PIA reference is recorded; the prompt-injection review feeds the PIA on the prompt-injection-driven risk class.

Each privacy-tagged mitigation entry retains the schema's required fields (mitigation, type, evidence pointer, owner, exercised_in_test); the owner field for privacy-tagged entries typically names the privacy function (CPO, DPO, Head of Privacy, Privacy Counsel) or a named privacy sub-function (privacy operations, privacy engineering, BAA management).

### 4. Monitoring adds the privacy-tagged signal set

Beyond the cyber-tagged signals (auth anomalies, tool-invocation rate, output-anomaly detection, vendor-version monitoring, retrieval-source integrity), the privacy overlay adds:

- **Output-PII detection rate**: the rate at which output-side filters detect personal data being returned where the policy says it should not be. A spike is a leading indicator of either a successful injection or a control regression.
- **Retrieval-authorisation violation signals**: where the retrieval pipeline tracks per-user authorisation, violations are surfaced as a privacy signal as well as an authorisation signal.
- **Cross-tenant or cross-user retrieval anomalies**: signals from the retrieval-authorisation layer that user A's session retrieved content from user B's scope.
- **Region-egress anomalies on the inference path**: where the firm pins inference to a region, anomalies in the region tag on inference responses are a privacy signal.
- **Sub-processor change signals**: where the vendor publishes sub-processor changes, the signal is a privacy event with a contract-clock attached.
- **Output-retention overrun**: where the firm's policy says outputs are retained N days and the firm-side log shows older content, the signal is a privacy event.

Each signal retains the schema's required fields (signal, threshold, frequency, owner, escalation path); privacy-tagged entries escalate to the privacy function in addition to or in place of the model owner.

### 5. Incident-response section names privacy-notification triggers

This is the privacy overlay's load-bearing addition. The `incident_response[]` entries list, per incident class, the privacy-notification trigger that applies in the firm's footprint:

- **GLBA Safeguards Rule (FTC scope)**: 16 CFR §314.5(d) FTC notification within 30 days of discovery of a notification event involving the unauthorised acquisition of unencrypted customer information of 500 or more consumers. A prompt-injection-driven exfiltration meeting the threshold falls within scope.
- **GLBA Safeguards Rule (banking interagency)**: customer-notice obligations under the interagency rule's 2005 incident-response standards; the firm's privacy program normally maintains the notification matrix.
- **State breach laws**: cross-state patchwork; a prompt-injection-driven exfiltration of regulated personal data triggers the state-by-state notification matrix the firm maintains. The prompt-injection review references the matrix; it does not restate it.
- **HIPAA Breach Notification Rule (45 CFR Part 164 Subpart D)**: where PHI is in scope, the 60-day-to-individual / immediate-to-HHS / annual-or-immediate-to-media notification clocks apply; the BAA chain governs the vendor's downstream obligation to the firm.
- **Reg S-P (May 2024 amendments)**: customer-notice obligations on covered institutions; service-provider written-contract requirements for breach notification.
- **GDPR / UK GDPR**: Article 33 supervisory-authority notification within 72 hours of awareness; Article 34 data-subject notification where the breach is likely to result in high risk to rights and freedoms.
- **NAIC Insurance Data Security Model Law (Model #668)**: where adopted in the firm's state-of-operation, the cybersecurity-event notification clock and content requirements apply; the overlay anchors here for life and health insurance assistants.
- **Sector-specific notification triggers** (state insurance commissioner notices for insurance carriers; SEC Reg S-P for advisers / BDs / funds; banking-agency notification under 12 CFR Part 53 / Part 225 / Part 304 36-hour rule where the prompt-injection-driven event is also a computer-security incident under that rule) are loaded from the relevant sector overlay.

The off-switch criterion column for privacy-relevant incident classes is non-optional. A confirmed cross-tenant retrieval exfiltration with no off-switch is a finding.

### 6. Recommended actions add the privacy-specific items

The standard privacy-tagged recommended-actions items the overlay surfaces:

- **DPIA / PIA refresh on every change-of-version notice and every material change in the retrieval corpus or tool inventory.** The privacy function signs the refresh.
- **BAA chain refresh on PHI-touching use cases** at the same cadence as foundation-model and inference-platform vendor changes.
- **Sub-processor change-notice review cadence** with the privacy function as named owner.
- **Privacy tabletop exercise** with the CISO function for any GenAI use case handling NPI, PHI, or material non-public information; rehearses the §314.5(d) / state / HIPAA / Reg S-P / GDPR notification chains against AI-specific incident scenarios.
- **Right-to-deletion-against-LLM rehearsal** for use cases subject to state privacy laws or GDPR, exercising the firm's response mechanism with the foundation-model and inference-platform vendors.

## Privacy-specific output additions

In the structured object (`schemas/prompt-injection-review.schema.json`):

- `cross_cutting_overlay_notes.privacy` carries the privacy-specific fields: personal-data-class tagging on threat-surface entries, lawful-basis column, named privacy-side mitigations, retention windows, training-use posture per contract, sub-processor list reference, named privacy-notification triggers per incident class.
- `mitigations[]` entries with privacy-tagged owner (privacy function or sub-function).
- `monitoring_detection[]` entries with privacy-tagged escalation path.
- `incident_response[]` entries with `privacy_notification_trigger` populated where applicable.
- `recommended_actions[]` entries with privacy-tagged owner role.

## Common pitfalls in privacy-flagged prompt-injection reviews

- Skipping the prompt-as-customer-data analysis on a use case because the firm "doesn't intend to send PII". Inadvertent NPI / PHI in narratives is the dominant failure mode (claims FNOL, customer-support chats, RAG over customer documents).
- Treating the vendor's marketing-page training-use posture as the contractual posture. The contract clause is the operative document.
- Reading SOC 2 Type II as if it covered privacy specifically. SOC 2 covers the Privacy criterion only when the vendor opts in.
- Missing the HIPAA business-associate analysis on a "tech vendor" that incidentally touches PHI through prompts or retrieval.
- Treating the GLBA exemption from a state privacy law as blanket exemption when the prompt content or RAG corpus reaches data outside the GLBA-covered scope.
- Recording residual risk without a privacy-notification trigger evaluation. §314.5(d), state laws, HIPAA, Reg S-P, and GDPR Article 33 are not optional considerations.
- Cross-border egress handled silently. Offshore inference endpoints and cross-region serving are named, not assumed.
- Right-to-deletion and right-to-correction treated as out of scope. The mechanism with the foundation-model vendor and the inference-platform vendor is part of the privacy posture; the contract clause is recorded.
