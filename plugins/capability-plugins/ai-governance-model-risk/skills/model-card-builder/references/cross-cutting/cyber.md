# Cyber cross-cutting overlay for model-card-builder

When the engagement-scope record flags `cyber` for the model use case, this overlay adds cyber-specific content to named card sections. It does not replace the firm's information-security risk assessment; it is the model-card-side surfacing of cyber considerations that a second-line reviewer (and an examiner) will look for when the model is itself an attack surface or attack target.

Loaded by: `model-card-builder/SKILL.md` when `engagement_scope.cross_cutting_set` includes `cyber`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- NYDFS 23 NYCRR Part 500, especially the third-party-risk, incident-response, and incident-notice provisions (Part 500 governs covered entities; the model is in scope when it sits inside a covered entity's information system or is hosted by a third-party service provider).
- SEC cyber disclosure rules: 8-K Item 1.05 (material cybersecurity incident disclosure) and Reg S-K Item 106 (cybersecurity risk management, strategy, and governance) where the registrant is public.
- FFIEC IT Examination Handbook, Information Security and Cybersecurity sections, applied to the model's serving environment, change controls, and access controls.
- NIST AI 600-1 (Generative AI Profile) cyber considerations: prompt-injection threat surface, model-supply-chain attack vectors, training-data poisoning, evasion and extraction attacks.

## What changes for cyber-flagged model cards

### 1. System description gains a cybersecurity considerations subsection

The card's system description block adds a cyber subsection that names the threat surface for this specific model: input channels (chat, API, batch, retrieval triggers), prompt-injection robustness posture (tested, untested, vendor-tested), model-supply-chain dependence (foundation-model provider, model-hosting environment, model artefact integrity controls), and tool/agent privileges where applicable. For a traditional ML model, the subsection is shorter: serving environment, model-artefact integrity, access controls. For a GenAI model with tool use or agentic behaviour, the subsection is the longest in the card.

### 2. Training and reference data section flags poisoning and extraction exposure

For models trained or fine-tuned on firm data, the data section flags training-data integrity controls (provenance, change-detection on training corpora) and the residual exposure to data-poisoning where the controls are partial. For RAG-using models, the retrieval corpus is itself a cyber-relevant surface (retrieval-corpus injection is a real attack pattern); the data section names corpus access controls, content-validation controls, and the refresh integrity model.

### 3. Robustness section gains adversarial cyber tests

Robustness entries for prompt injection, jailbreak, model extraction, and evasion are expected for GenAI cards in cyber-flagged scope. Vendor-supplied adversarial test results are recorded with vendor-self-attestation confidence; firm-independent red-team results carry higher confidence and are listed separately. Absence of firm-independent testing is itself a card-recordable item under the cyber overlay (it goes to source trace as `[evidence needed]` and to sign-off questions, not silently into the card body).

### 4. Monitoring plan adds cyber-relevant signals

Monitoring entries the cyber overlay expects:

- Authentication and authorisation anomalies on the model's serving endpoint.
- Prompt-injection detection signals (where the firm has a detection layer; if not, the absence is recorded).
- Output-anomaly detection (sudden shifts in refusal rate, citation patterns, tool-call patterns are leading indicators of compromise as well as drift).
- Vendor change-of-version signals for foundation-model and serving-environment dependencies; an unannounced version swap is a cyber signal as well as a model-risk signal.
- For GenAI with tools or agent privileges, tool-invocation rate and pattern monitoring; sudden expansion of tool use is an investigation trigger.

Each monitoring entry retains the five required fields (metric, threshold, frequency, owner, escalation path); cyber-relevant entries typically escalate to the CISO function in addition to the model owner.

### 5. Controls section adds cyber-tagged controls

Preventive: input validation, output filtering, prompt-template guardrails, tool-boundary controls, secrets-handling in prompt context. Detective: prompt-injection detection layer, output-anomaly detection, audit-logging on model invocations and retrievals. Response: incident-response runbook integration (the model-misuse playbook, the foundation-model-compromise playbook), with the named owner being the CISO function in coordination with the model owner.

### 6. Change management adds cyber re-validation triggers

Foundation-model swap is a cyber re-validation trigger as well as a model-risk re-validation trigger. Hosting-environment migration, retrieval-corpus access-control change, and tool-inventory expansion are each cyber re-validation triggers.

## Cyber-specific output template additions

- A "Cybersecurity considerations" subsection inside `architecture` (in the structured object: `architecture.cyber_subsection`).
- Cyber-tagged entries in `monitoring[]` with the named CISO-function escalation path.
- Cyber-tagged entries in `controls[]` (preventive, detective, response).
- Cyber-tagged entries in `change_management[]` (foundation-model swap, hosting-environment migration, retrieval-corpus access change, tool-inventory expansion).
- Cyber-tagged sign-off questions (named CISO-function reviewer, prompt-injection robustness posture, model-supply-chain dependence, incident-response integration).

## Common pitfalls in cyber-flagged model cards

- Treating "vendor pen-tested" or vendor-supplied adversarial-test results as evidence the deployed prompt surface is hardened. The firm's prompt template, retrieval corpus, and tool inventory are firm-side surfaces and need firm-side testing.
- Failing to monitor for prompt-injection-as-attack-vector, framing prompt-injection only as a quality issue. It is also a control-evasion path when the model has tool or agent privileges.
- Assuming model isolation when the model has tool or agent privileges. Tool privileges are lateral-movement opportunities; the card's controls section needs to surface tool-boundary controls explicitly.
- Omitting vendor change-of-version monitoring; a silent foundation-model swap is both a model-risk event and a cyber event.
- Treating the cyber overlay as the CISO's document. The card is the firm-side governance artifact; the CISO function is a reviewer and an escalation path, not the owner.
