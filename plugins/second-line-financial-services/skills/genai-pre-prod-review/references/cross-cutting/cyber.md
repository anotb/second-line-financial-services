# Cyber cross-cutting overlay for genai-pre-prod-review

When the scope record flags `cyber` for a pre-prod gate review, this overlay sits as a primary lens. The CISO function is a co-reviewer and a co-signer on the gate decision, not a downstream consumer of the memo. For most GenAI use cases inside regulated entities the cyber overlay should be considered the default cross-cutting overlay.

Loaded by: `genai-pre-prod-review/SKILL.md` when `scope.cross_cutting_set` includes `cyber`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- NYDFS 23 NYCRR Part 500, especially §500.9 (risk assessment), §500.11 (third-party service-provider security), §500.16 (incident-response and BCDR plan), §500.17(a) (notice to superintendent), and the October 2024 Industry Letter on AI cybersecurity that maps these obligations onto AI deployments.
- SEC cyber disclosure rules: 8-K Item 1.05 (material cybersecurity incident disclosure within four business days of materiality determination) and Reg S-K Item 106 (annual disclosure of cyber risk-management, strategy, and governance).
- FFIEC IT Examination Handbook, Information Security and AIO booklets, applied to the AI system's serving environment, change controls, access controls, and incident-response integration.
- US Treasury Department report on Managing Artificial Intelligence-Specific Cybersecurity Risks in the Financial Services Sector (March 2024) for sector-specific cyber-AI considerations.
- 12 CFR Part 53 / Part 225 / Part 304 — the 36-hour banking computer-security incident notification rule for federally regulated banks (loaded via the banking sector overlay).
- NIST SP 800-53 Rev. 5 control families (AC, AU, IR, SI, SR) as the underlying control catalogue for cyber-side mitigations.
- NIST AI 600-1 Generative AI Profile cyber considerations and the OWASP / MITRE / NCSC framings as the practitioner taxonomy for AI threat modelling.

## Co-reviewer expectation

The CISO function is a co-signer on the gate decision. The reviewer-attestation block on the gate review names the CISO function explicitly; a gate decision without CISO function sign-off on a cyber-flagged GenAI use case is incomplete.

For tier-1 GenAI use cases the CISO function brings the named cyber sub-functions to the table at gate time: the identity team (authentication and authorisation on the model serving endpoint), the network security team (network-layer controls), the security operations centre (monitoring integration and IR runbook readiness), and the IR team (drill execution).

## What changes when cyber is flagged

### Open conditions the overlay typically adds

- IR drill scope before go-live includes at minimum one AI-specific incident class (confirmed system-prompt exfiltration, confirmed indirect-injection-driven misrouted action, suspected RAG corpus poisoning, foundation-model behaviour shift suggesting upstream compromise). Annual at minimum; quarterly for tier-1 GenAI use cases.
- Cyber tabletop exercise with the privacy officer and the relevant business function for any GenAI use case handling NPI, PHI, or material non-public information.
- Notification-decision rehearsal: the materiality-assessment process for SEC 8-K Item 1.05 (for public registrants) and the §500.17(a) notification process (for NY-footprint covered entities) exercised against AI-specific incident scenarios.
- Audit-log retention aligned to the firm's cyber log-retention policy and to NYDFS Part 500 §500.6 audit-trail expectations; the audit-log retention is the load-bearing control for many AI-specific monitoring signals.
- Authentication and authorisation review on the AI system's serving endpoint and on each tool the system can invoke (where applicable for tool-using systems); the identity team co-signs.
- Vendor and supply-chain cyber posture documented for the foundation-model provider and any model-artefact dependencies.

### Monitoring readiness adds the cyber-tagged signal set

The baseline cyber signals that should be live before go-live when the overlay is flagged:

- Authentication and authorisation anomalies on the AI system's serving endpoint; escalation to the security operations centre.
- For tool-using systems: tool-invocation rate and pattern; sudden expansion of tool use or off-hours activity is an investigation trigger.
- Cross-scope tool query anomaly (e.g., the system queries a market-data API on tickers outside the analyst's coverage; the system retrieves customer records outside the agent's case load).
- Output-anomaly detection (sudden shifts in refusal rate, citation patterns, response-length distribution) as a leading indicator of compromise as well as drift.
- Vendor change-of-version signals for foundation-model and serving-environment dependencies; an unannounced version swap is a cyber signal as well as a model-risk signal.
- For retrieval-using systems, retrieval-source integrity signals (last-modified, content hash drift on dynamic sources).

Each signal retains the schema's required fields (signal, threshold, frequency, owner, escalation path); cyber-tagged entries escalate to the CISO function or to the security operations centre, in addition to or in place of the model owner.

### Incident-response readiness names regulator-notification triggers

This is the cyber overlay's load-bearing addition to the gate review. The `incident_response_readiness.regulator_notification_triggers` list names, in the firm's footprint:

- NYDFS-covered entities: 23 NYCRR Part 500 §500.17(a) requires notice to the superintendent within 72 hours of determining a cybersecurity event has occurred that meets the rule's criteria. Prompt-injection-driven cyber events that result in unauthorised access, unauthorised action, or impairment to the security or integrity of the information system meet the criteria. The October 2024 Industry Letter signals AI-deployment-driven events fall within scope.
- SEC public registrants: 8-K Item 1.05 requires disclosure of material cybersecurity incidents within four business days of materiality determination. Prompt-injection or AI-related cyber events causing or contributing to material cyber incidents are within scope.
- GLBA Safeguards Rule entities (FTC scope): 16 CFR §314.5(d) requires FTC notification of notification events involving the unauthorised acquisition of unencrypted customer information of 500 or more consumers.
- State breach laws: cross-state patchwork; the firm's privacy and incident-response programme normally maintains a state-by-state notification matrix that the gate review references rather than restates.
- Sector-specific notification triggers (state insurance commissioner notices via the insurance overlay; the 36-hour banking computer-security incident notification rule via the banking overlay; state money-transmitter notifications via the payments-fintech overlay) are loaded from the relevant sector overlay.

### Off-switch documentation

The off-switch criterion column in the gate review's incident-response section is where the cyber overlay bites operationally. A cyber-relevant incident class without a defined off-switch is a finding, not an acceptable position. For agentic systems with tool use, the off-switch is typically a combination of cutting tool privileges and pausing the model serving endpoint. For human-in-the-loop systems, the off-switch is typically a combination of pausing the assistant and switching to the manual workflow.

`incident_response_readiness.off_switch_documented = true` is required for the gate decision to proceed to `go` or `go_with_conditions` on a cyber-flagged use case.

### Recommended-action items the overlay surfaces

The standard cyber-tagged recommended-actions items:

- `foundation_model_swap_revalidation` flag in change management with explicit re-run of the prompt-injection review and the gate review on every vendor change-of-version notice; cyber signs off on the re-run.
- IR drill cadence including AI-specific incident classes; annual at minimum, quarterly for tier-1.
- Cyber tabletop exercise with the privacy officer and the relevant business function for any GenAI use case handling sensitive data.
- Notification-decision rehearsal for the named regulator-notification triggers.

## Cyber-specific output additions

In the structured object (`schemas/genai-pre-prod-review.schema.json`):

- `cross_cutting_overlay_notes.cyber` carries cyber-specific fields: control-family tagging on monitoring entries, MITRE ATLAS mapping references on residual-risk entries that derive from the prompt-injection review, named cyber-side recommended-action items.
- `signoff[]` array includes the CISO function or named cyber sub-function as a co-signer.
- `monitoring_readiness[]` entries with cyber-tagged escalation path (security operations centre, IR team, identity team).
- `incident_response_readiness.regulator_notification_triggers` populated with the named triggers per the firm's footprint.
- `overlay_signoffs[]` includes a cyber entry with named owner role.

## Common pitfalls in cyber-flagged pre-prod gate reviews

- Treating the AI Governance Lead as the sole gate decision-maker. Prompt injection and other cyber-relevant AI risk classes are, in regulator framing, cybersecurity risk classes; the CISO function co-decides on the gate.
- Recording vendor SOC 2 or vendor system card as substituting for firm-side cyber gate evidence. Vendor evidence is one input; firm-side serving environment, identity, network, and IR integration are firm-side responsibilities.
- Failing to integrate the AI-misuse runbook into the firm's IR programme. A standalone AI playbook that does not connect to the named cyber IR runbook is a paper artefact; the gate review records the integration explicitly.
- Recording residual risk without a regulator-notification trigger evaluation. NYDFS §500.17(a), SEC 8-K Item 1.05, the 36-hour banking computer-security incident notification rule, GLBA Safeguards Rule notification, and state breach laws are not optional considerations; the trigger evaluation is recorded in `incident_response_readiness.regulator_notification_triggers`.
- Omitting the off-switch criterion for cyber-relevant incident classes; a confirmed exfiltration with no defined off-switch blocks `go`.
- Using AI-only vocabulary in a gate review the cyber team has to consume. MITRE ATLAS mappings and control-family tagging cost little to add and turn the artefact into something the cyber team can integrate without translation.
