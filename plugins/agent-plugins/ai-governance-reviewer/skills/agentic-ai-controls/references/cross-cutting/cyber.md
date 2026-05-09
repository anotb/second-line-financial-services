# Cyber cross-cutting overlay for agentic-ai-controls

When the scope record flags `cyber` for an agentic-controls review, this overlay sits as the primary lens, not a secondary one. Tool use, identity, and external-system actuation widen the cyber surface materially. The AI governance team often owns the artifact, but the CISO function is a co-reviewer and a co-decision-maker on residual-risk acceptance, not a downstream consumer.

Loaded by: `agentic-ai-controls/SKILL.md` when `scope.cross_cutting_set` includes `cyber`. For most v1 agentic deployments inside regulated entities (any agent with tool use, identity, or external-system actuation), this overlay should be considered the default. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- NYDFS 23 NYCRR Part 500, especially §500.6 (audit trail), §500.9 (risk assessment), §500.11 (third-party service-provider security), §500.16 (incident-response and BCDR plan), §500.17(a) (notice to superintendent), and the October 2024 Industry Letter on AI cybersecurity that maps these obligations onto AI deployments.
- SEC cyber disclosure rules: 8-K Item 1.05 (material cybersecurity incident disclosure within four business days of materiality determination) and Reg S-K Item 106 (annual disclosure of cyber risk-management, strategy, and governance).
- 12 CFR Part 53 / Part 225 / Part 304 — banking computer-security incident notification rule (36-hour notification for "notification incidents") for bank-affiliated entities.
- FFIEC IT Examination Handbook, Information Security and AIO booklets, applied to the agent's serving environment, change controls, access controls, and incident-response integration.
- NIST SP 800-53 Rev. 5 control families (AC, AU, IR, SI, SR, SC) as the underlying control catalogue for the cyber-side mitigations the review records.
- NIST AI 600-1 Generative AI Profile cyber considerations and the OWASP LLM Top 10 / MITRE ATLAS / NCSC framings as the practitioner taxonomy for the agentic threat surface.

## What changes when cyber is flagged

### Authority statement gains a cyber-impact framing

The out-of-scope list gains explicit cyber-relevant entries: no credential issuance or rotation by the agent; no security-tool reconfiguration; no IR-system or audit-system writes; no privileged-account actions. These are non-optional for any agent operating in or near regulated systems.

### Tool inventory gains control-family tagging

Each tool is tagged with the relevant NIST SP 800-53 control families and the responsible CISO sub-function. Read tools tie to AC and AU; write tools tie to AC, AU, and SI; execute tools tie to SC (sandboxing) and SI; communicate tools tie to AC, SC, and the application-security framing; compute tools tie to SC and resource-quota controls.

The tagging is not bureaucratic; it is the seam that lets the cyber team integrate the review into existing control mappings without re-doing the work in a parallel taxonomy.

### Identity and authorisation get the cyber-side bar

The CISO identity-team is the named owner for service-account scoping, credential rotation, and secrets handling. The minimum bar:

- Service account separated from any human identity, with named owner and rotation cadence.
- Least-privilege scopes per tool, per customer, per case, per session — enforced at the platform layer, not asserted in policy.
- Secrets not in the agent's prompt context; if they appear, the exfiltration risk is structural and the residual-risk view records it.
- Identity-layer rate limits sized against the blast-radius framing, not against expected operational load.

### Tested attack classes are framed in the cyber team's vocabulary alongside the AI vocabulary

A second-line review presented in OWASP-only vocabulary lands as a foreign object on the CISO's desk. The same review presented with MITRE ATLAS technique IDs and with mappings to existing offensive-security testing categories (application security, red-team engagement, third-party assessment) lands as an extension of work already on the cyber team's plan. Both vocabularies should appear on the same row of `threat_assessment[]`.

The agentic-specific attack classes that are non-optional under the cyber overlay: tool hijack, cross-scope tool query, excessive agency exploitation (LLM08), planner-executor seam, multi-agent message injection (where applicable), memory poisoning (where persistent memory applies), sandbox escape (where code execution applies). The `dataset_or_redteam_ref` field on each entry should name the source explicitly: vendor red-team set (vendor-self-attestation confidence), firm-internal red team (firm CISO red team or contracted offensive-security partner), third-party AI-specific assessment.

### Sandbox guarantees are the cyber overlay's load-bearing addition

For agents with code execution, browser automation, or shell access, the sandbox section is examined under the SC family lens. Process isolation, filesystem scoping, network-egress controls, secret isolation, time-bounded execution, resource quotas, and snapshot-and-rollback posture each carry an enforcement-evidence pointer. Policy without enforcement evidence routes to recommended actions, not to coverage. For tool-use-only systems without execution, the explicit boundary statement is the cyber-side artifact ("no code-execution surface; agent is restricted to enumerated tool calls").

### Mitigations expand to include the standard cyber control set

In addition to the AI-native guardrails (input filtering, output filtering, structured-output enforcement, refusal behaviour, content provenance), the cyber overlay expects the review to record:

- Authentication and authorisation on the agent's serving endpoint and on each tool.
- Audit logging of every model invocation, every retrieval, every tool call, every inter-agent message, every oversight event, every kill-switch action, with retention aligned to firm cyber log-retention policy and to NYDFS Part 500 §500.6 audit-trail expectations.
- Network-layer controls on the serving environment and on outbound calls.
- Secrets handling in the prompt context — secrets should not appear in the system prompt or in retrieved content; if they do, the exfiltration risk is structural.
- Vendor and supply-chain controls — foundation-model provider security posture, model-artefact integrity controls, dependency-tree controls for self-hosted components.
- Incident-response runbook integration — the AI-misuse playbook, the foundation-model-compromise playbook, and the agentic-tool-misuse playbook are named runbooks under the firm's IR programme, not standalone AI artefacts.

### Kill-switch and drill cadence are the cyber overlay's other load-bearing addition

Drill cadence is examined under the IR family lens. Annual at minimum; quarterly for tier-1 agentic use cases; on every tool addition or major version change for any tier. The drill exercises both the technical kill-switch (cutting tool privileges, pausing serving endpoint) and the operational decision chain (who calls it, who confirms, who records, who signs off on resumption). Drill records carry into the source-trace at high confidence.

### Monitoring adds the cyber-tagged signal set

The baseline cyber signals to add when the overlay is flagged:

- Authentication and authorisation anomalies on the agent's serving endpoint and per tool.
- Tool-invocation rate and pattern per tool — for systems with tool use, sudden expansion of tool use, off-hours activity, or new-tool-call patterns are investigation triggers.
- Cross-scope tool query anomaly — the agent invokes a tool with arguments outside its allowed scope (e.g., the system queries a market-data API on tickers outside the analyst's coverage; retrieves customer records outside the agent's case load; sends an outbound communication to a non-customer recipient).
- Output-anomaly detection (sudden shifts in refusal rate, citation patterns, response-length distribution) as a leading indicator of compromise as well as drift.
- Vendor change-of-version signals for foundation-model and serving-environment dependencies.
- Sandbox-escape signal — for systems with code execution, any boundary-violation event is a signal regardless of whether it caused harm.

Each signal retains the schema's required fields (signal, threshold, frequency, owner, escalation path); cyber-tagged entries escalate to the CISO function or to the security operations centre.

### Incident-response section names regulator-notification triggers

The cyber overlay's most load-bearing addition. The `incident_response[]` entries list, per incident class, the regulator-notification trigger that applies in the firm's footprint:

- NYDFS-covered entities: 23 NYCRR Part 500 §500.17(a) requires notice to the superintendent within 72 hours of determining a cybersecurity event has occurred that meets the rule's criteria. Tool-misuse events resulting in unauthorised access, unauthorised action, or impairment to the security or integrity of the information system meet the criteria. The October 2024 Industry Letter signals that AI-deployment-driven events fall within scope.
- Bank-affiliated entities: 12 CFR Part 53 / Part 225 / Part 304 require notification to the primary federal regulator within 36 hours of determining a "notification incident" has occurred. Agentic tool-misuse events that materially disrupt or degrade banking services meet the threshold.
- SEC public registrants: 8-K Item 1.05 requires disclosure of material cybersecurity incidents within four business days of materiality determination. Agentic-AI-driven events causing or contributing to material cyber incidents are within scope.
- GLBA Safeguards Rule entities (FTC scope): 16 CFR §314.5(d) requires FTC notification of notification events involving the unauthorised acquisition of unencrypted customer information of 500 or more consumers.
- State breach laws: cross-state patchwork; the firm's privacy and incident-response programme normally maintains a state-by-state notification matrix that the review references rather than restating.
- Sector-specific notification triggers (state insurance commissioner notices for adopting Insurance Data Security Model Law states, banking-agency notification under 12 CFR Part 53 / Part 225 / Part 304) are loaded from the relevant sector overlay.

The off-switch criterion column is where the cyber overlay bites operationally: a cyber incident class without a defined off-switch is a finding, not an acceptable position.

### Recommended actions add the cyber-specific items

The standard cyber-tagged recommended-actions items the overlay surfaces:

- `foundation_model_swap_revalidation` flag in change management with explicit re-run of the agentic-controls review on every vendor change-of-version notice; cyber signs off on the re-run.
- Kill-switch drill cadence ratification — annual at minimum, quarterly for tier-1, on every tool addition or major version change.
- IR drill cadence including agentic-specific incident classes (confirmed tool-misuse outside scope, confirmed cross-scope tool query, confirmed external-system unauthorised action, suspected agent compromise, foundation-model behaviour shift, sandbox-escape attempt).
- Cyber tabletop exercise with the privacy officer and the relevant business function for any agentic use case handling NPI, PHI, or material non-public information.
- Notification-decision rehearsal: the materiality-assessment process for SEC 8-K Item 1.05, the §500.17(a) notification process for NYDFS-covered entities, and the 36-hour banking-rule process for bank-affiliated entities, exercised against agentic-AI incident scenarios.
- Per-tool blast-radius re-validation on any tool addition; cyber co-signs the re-validation.

## Cyber-specific output additions

In the structured object (`schemas/agentic-controls-review.schema.json`):

- `cross_cutting_overlay_notes.cyber` carries the cyber-specific fields: control-family tagging on tool-inventory entries, MITRE ATLAS technique mapping on threat-assessment entries, named cyber-side mitigations, named regulator-notification triggers per incident class, drill records.
- `tool_inventory[]` entries with cyber control-family tagging in `notes` or `evidence_pointer`.
- `kill_switch[]` entries with `last_drilled` and `drill_cadence` populated.
- `incident_response[]` entries with `regulator_notification_trigger` populated where applicable.
- `escalation_triggers[]` entries with cyber-tagged escalation path.
- `recommended_actions[]` entries with cyber-tagged owner role.

## Common pitfalls in cyber-flagged agentic-controls reviews

The recurring failure modes the review should not fall into:

- Treating the AI governance team as the sole reviewer. Agentic AI with tool use is, in NYDFS framing, a cybersecurity risk class; the CISO function co-reviews and co-decides on residual-risk acceptance.
- Treating vendor adversarial-test results as evidence the deployed agent is hardened. The firm's tool inventory, authority logic, sandbox configuration, and oversight design are firm-side surfaces and need firm-side testing.
- Recording sandbox guarantees as policy assertion without enforcement evidence. A sandbox the firm has not exercised is a sandbox that does not bind in incident response.
- Treating "documented" kill switch as evidence. The drill record is the evidence; absence is theatre.
- Failing to integrate the agentic-tool-misuse runbook into the firm's IR programme. A standalone AI playbook that does not connect to the named cyber IR runbook is a paper artefact.
- Recording residual risk without a regulator-notification trigger evaluation. NYDFS §500.17(a), 12 CFR Part 53 36-hour rule, SEC 8-K Item 1.05 are not optional considerations.
- Omitting the off-switch criterion for cyber-relevant incident classes.
- Using AI-only vocabulary in a review the cyber team has to consume. MITRE ATLAS mappings cost little to add and turn the artefact into something the cyber team can integrate without translation.
