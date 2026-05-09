# Cyber cross-cutting overlay for prompt-injection-risk

When the scope record flags `cyber` for a prompt-injection review, this overlay sits as the primary lens, not a secondary one. Prompt injection is, in regulator framing, a cybersecurity risk class. The AI governance team often owns the review, but the CISO function is a co-reviewer and a co-decision-maker, not a downstream consumer.

Loaded by: `prompt-injection-risk/SKILL.md` when `scope.cross_cutting_set` includes `cyber`. For most GenAI use cases inside regulated entities, this overlay should be considered the default. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- NYDFS 23 NYCRR Part 500, especially §500.9 (risk assessment), §500.11 (third-party service-provider security), §500.16 (incident-response and BCDR plan), §500.17(a) (notice to superintendent), and the October 2024 Industry Letter on AI cybersecurity that maps these obligations onto AI deployments.
- SEC cyber disclosure rules: 8-K Item 1.05 (material cybersecurity incident disclosure within four business days of materiality determination) and Reg S-K Item 106 (annual disclosure of cyber risk-management, strategy, and governance).
- FFIEC IT Examination Handbook, Information Security and AIO booklets, applied to the AI system's serving environment, change controls, access controls, and incident-response integration.
- NIST SP 800-53 Rev. 5 control families (AC, AU, IR, SI, SR) as the underlying control catalogue for the cyber-side mitigations the review records.
- NIST AI 600-1 Generative AI Profile cyber considerations and the OWASP/MITRE/NCSC framings as the practitioner taxonomy for the threat surface.

## What changes when cyber is flagged

### Threat surface gains a cyber-tagging convention

Each carrier in the threat-surface table is tagged with the relevant control-catalogue families and the responsible CISO-side function. The system-prompt carrier ties to AC and SI; user input ties to AC and SI; retrieved content ties to SI and SR (supply-chain); tool output ties to SR and the application-security framing for the tool's API; memory ties to AC and SI; multi-agent message ties to SI and to the agent-platform's identity model.

The tagging is not bureaucratic; it is the seam that lets the cyber team integrate the review into existing control mappings without re-doing the work in a parallel taxonomy.

### Tested attack classes are framed in the cyber team's vocabulary alongside the AI vocabulary

A second-line review presented in OWASP-only vocabulary lands as a foreign object on the CISO's desk. The same review presented with MITRE ATLAS technique IDs and with mappings to existing offensive-security testing categories (application security, red-team engagement, third-party assessment) lands as an extension of work already on the cyber team's plan. Both vocabularies should appear on the same row of `tested_attacks[]`.

The `dataset_or_redteam_ref` field on each tested-attack entry should name the source explicitly: vendor red-team set (vendor-self-attestation confidence), firm-internal red team (firm CISO red team or contracted offensive-security partner), third-party AI-specific assessment (e.g., independent prompt-injection assessor). Mixing these into a single line collapses the confidence signal.

### Mitigations expand to include the standard cyber control set

In addition to the AI-native mitigations (input filtering, output filtering, structured-output enforcement, refusal behaviour, content provenance), the cyber overlay expects the review to record:

- Authentication and authorisation on the AI system's serving endpoint and on each tool the system can invoke.
- Audit logging of every model invocation, every retrieval, every tool call, every inter-agent message, with retention aligned to the firm's cyber log-retention policy and to NYDFS Part 500 §500.6 audit-trail expectations.
- Network-layer controls on the serving environment and on outbound calls (web fetch, API calls).
- Secrets handling in the prompt context: secrets should not appear in the system prompt or in retrieved content; if they do, the exfiltration risk is structural.
- Vendor and supply-chain controls: foundation-model provider security posture, model-artefact integrity controls, dependency-tree controls for self-hosted components.
- Incident-response runbook integration: the AI-misuse playbook and the foundation-model-compromise playbook are named runbooks under the firm's IR programme, not standalone AI artefacts.

Each cyber-tagged mitigation entry retains the schema's required fields (mitigation, type, evidence pointer, owner, exercised_in_test); the owner field for cyber-tagged entries typically names the CISO function or a named cyber sub-function (identity team, network security, security operations, IR).

### Monitoring adds the cyber-tagged signal set

The baseline cyber signals to add when the overlay is flagged:

- Authentication and authorisation anomalies on the AI system's serving endpoint.
- Tool-invocation rate and pattern; for systems with tool use, sudden expansion of tool use or off-hours activity is an investigation trigger.
- Cross-scope tool query anomaly (e.g., the system queries a market-data API on tickers outside the analyst's coverage; the system retrieves customer records outside the agent's case load).
- Output-anomaly detection (sudden shifts in refusal rate, citation patterns, response-length distribution) as a leading indicator of compromise as well as drift.
- Vendor change-of-version signals for foundation-model and serving-environment dependencies; an unannounced version swap is a cyber signal as well as a model-risk signal.
- For retrieval-using systems, retrieval-source integrity signals (last-modified, content hash drift on dynamic sources).

Each signal retains the schema's required fields (signal, threshold, frequency, owner, escalation path); cyber-tagged entries escalate to the CISO function or to the security operations centre, in addition to or in place of the model owner.

### Incident-response section names regulator-notification triggers

This is the cyber overlay's load-bearing addition to the review. The `incident_response[]` entries list, per incident class, the regulator-notification trigger that applies in the firm's footprint:

- NYDFS-covered entities: 23 NYCRR Part 500 §500.17(a) requires notice to the superintendent within 72 hours of determining a cybersecurity event has occurred that meets the rule's criteria. Prompt-injection-driven cyber events that result in unauthorised access, unauthorised action, or impairment to the security or integrity of the information system meet the criteria. The October 2024 Industry Letter signals that AI-deployment-driven events fall within scope.
- SEC public registrants: 8-K Item 1.05 requires disclosure of material cybersecurity incidents within four business days of materiality determination. Prompt-injection events causing or contributing to material cyber incidents are within scope. The materiality assessment is the registrant's; the prompt-injection review is one input.
- GLBA Safeguards Rule entities (FTC scope): 16 CFR §314.5(d) requires FTC notification of notification events involving the unauthorised acquisition of unencrypted customer information of 500 or more consumers.
- State breach laws: cross-state patchwork; the firm's privacy and incident-response programme normally maintains a state-by-state notification matrix that the review should reference rather than restate.
- Sector-specific notification triggers (state insurance commissioner notices, banking-agency notification requirements under 12 CFR Part 53 / Part 225 / Part 304 36-hour banking computer-security incident notification rule) are loaded from the relevant sector overlay.

The off-switch criterion column is where the cyber overlay bites operationally: a cyber incident class without a defined off-switch is a finding, not an acceptable position.

### Recommended actions add the cyber-specific items

The standard cyber-tagged recommended-actions items the overlay surfaces:

- `foundation_model_swap_revalidation` flag in change management with explicit re-run of the prompt-injection review on every vendor change-of-version notice; cyber signs off on the re-run.
- IR drill cadence including AI-specific incident classes (confirmed system-prompt exfiltration, confirmed indirect-injection-driven misrouted action, suspected RAG corpus poisoning, foundation-model behaviour shift suggesting upstream compromise). Annual at minimum; quarterly for tier-1 GenAI use cases.
- Cyber tabletop exercise with the privacy officer and the relevant business function for any GenAI use case handling NPI, PHI, or material non-public information.
- Notification-decision rehearsal: the materiality-assessment process for SEC 8-K Item 1.05 and the §500.17(a) notification process for NYDFS-covered entities, exercised against AI-specific incident scenarios.

## Cyber-specific output additions

In the structured object (`schemas/prompt-injection-review.schema.json`):

- `cross_cutting_overlay_notes.cyber` carries the cyber-specific fields: control-family tagging on threat-surface entries, MITRE ATLAS technique mapping on tested-attack entries, named cyber-side mitigations, named regulator-notification triggers per incident class.
- `mitigations[]` entries with cyber-tagged owner (CISO function or sub-function).
- `monitoring_detection[]` entries with cyber-tagged escalation path.
- `incident_response[]` entries with `regulator_notification_trigger` populated where applicable.
- `recommended_actions[]` entries with cyber-tagged owner role.

## Common pitfalls in cyber-flagged prompt-injection reviews

The recurring failure modes the review should not fall into:

- Treating the AI governance team as the sole reviewer. Prompt injection is, in NYDFS framing, a cybersecurity risk class; the CISO function co-reviews and co-decides on the residual risk acceptance.
- Treating vendor adversarial-test results as evidence the deployed prompt surface is hardened. The firm's prompt template, retrieval corpus, and tool inventory are firm-side surfaces and need firm-side testing.
- Failing to integrate the AI-misuse runbook into the firm's IR programme. A standalone AI playbook that does not connect to the named cyber IR runbook is a paper artefact.
- Recording residual risk without a regulator-notification trigger evaluation. NYDFS §500.17(a) and SEC 8-K Item 1.05 are not optional considerations.
- Omitting the off-switch criterion for cyber-relevant incident classes. A confirmed exfiltration with no defined off-switch is a finding.
- Using AI-only vocabulary in a review the cyber team has to consume. MITRE ATLAS mappings cost little to add and turn the artefact into something the cyber team can integrate without translation.
