# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Conduct cross-cutting overlay for prompt-injection-risk

When the scope record flags `conduct` for a prompt-injection review, this overlay loads to address the conduct-risk dimension of prompt-injection exposure on customer-facing or distribution-touching GenAI use cases. The threat is not abstract: a successful injection on a customer-facing assistant can produce a misleading representation, a misstated material fact about a product, an undisclosed AI-generated communication on a matter of public interest, or an off-policy promise the firm has to honour or remediate. Those outcomes are conduct events on their face.

Loaded by: `prompt-injection-risk/SKILL.md` when `scope.cross_cutting_set` includes `conduct`. The conduct overlay loads where the use case generates or assists customer-facing communications, distribution materials, marketing assets, fiduciary-or-recommendation surfaces, or where the firm's conduct framework names the use case under its scope. The cyber overlay is the primary lens on this skill; conduct sits as a parallel lens, not a substitute. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- **CFPB UDAAP authority** — 12 USC §5531 (unfair, deceptive, or abusive acts or practices); the bureau's authority reaches algorithmic outcomes that produce UDAAP exposure. Where prompt-injection causes the system to generate a deceptive or misleading communication to a consumer, the conduct frame applies.
- **FTC Section 5** — 15 USC §45 unfair or deceptive acts or practices; for non-bank entities outside CFPB scope or for marketing-facing surfaces.
- **SEC Marketing Rule** — 17 CFR §275.206(4)-1 — for SEC-registered investment advisers, the Marketing Rule reaches advertisements and testimonial content; an AI-generated communication that constitutes an advertisement under the rule's definition is in scope.
- **FINRA communications rules** — Rule 2210 (communications with the public); Rule 2111 (suitability); Rule 2090 (KYC) — for broker-dealer customer-facing AI use cases.
- **Reg BI** — 17 CFR §240.15l-1 — Care Obligation, Disclosure Obligation, Conflict of Interest Obligation for broker-dealers making recommendations; AI-assisted recommendation surfaces inherit the obligations.
- **NAIC Model Acts and AI Bulletin (December 2023)** — Model #880 (Unfair Trade Practices), Model #900 (Unfair Claims Settlement Practices), and the AI Bulletin on insurer use of AI; for life, health, and P&C insurance customer-facing AI surfaces.
- **April 2023 Joint Statement** — CFPB, EEOC, DOJ Civil Rights Division, FTC — on enforcement of civil rights, fair competition, consumer protection, and equal opportunity laws against algorithmic discrimination and automated systems; the statement underwrites the conduct-and-fair-lending lens on AI.
- **CFPB AI / complex-model framing** — the bureau has reaffirmed that algorithmic outcomes are reachable under existing UDAAP, ECOA, and FCRA authorities; specific Circulars (2022-03 and 2023-03) were withdrawn May 12, 2025 and live in the source-anchors file as historical context, but the underlying regulatory reach was not the source of the obligation.
- **FCA SMCR and Consumer Duty** — for UK-licensed firms operating into the US or with US customer overlap; the cross-border perimeter of Consumer Duty is its own triage point and the senior-manager-accountability frame survives jurisdictional debate.

#### What changes when conduct is flagged

##### 1. Threat surface gains a customer-outcome read

Each carrier in the threat-surface table is read for its potential to produce a customer-facing outcome on injection success. The user-input carrier ties to whatever the consumer says next; the retrieved-content carrier ties to whatever the system tells the consumer based on content the consumer cannot see; the tool-output carrier ties to actions taken on the consumer's account; the multi-agent message carrier ties to upstream-agent decisions that shape the customer-facing agent's output. The conduct lens reads each carrier for: does an injection on this carrier produce a customer-facing communication, an account action, a recommendation, or a representation about a product. Where the answer is yes, the trust-basis column carries weight; "trusted because firm-controlled" reads differently when the failure mode is a UDAAP exposure than when the failure mode is a system-prompt leak.

##### 2. Tested attack classes expand to include conduct-relevant outcomes

The AI-native attack classes carry through; the conduct overlay adds explicit testing for conduct-relevant outcomes on injection success:

- **Misleading-representation generation** — does the injected prompt cause the system to generate a misstated material fact about a product, fee, term, or risk. Tested against the firm's product-fact library and the operative disclosure language.
- **Off-policy promise generation** — does the injected prompt cause the system to commit the firm to a course of action outside policy (a fee waiver, a rate match, a settlement offer, a regulatory-treatment representation). Tested against the firm's commitment-authority matrix.
- **Recommendation-surface manipulation** — for systems with recommendation reach (Reg BI, suitability, IA fiduciary), does an injection cause the system to recommend a product the customer's profile does not support. Tested against the firm's suitability and recommendation-governance rules.
- **AI-disclosure suppression** — does an injection cause the system to suppress the AI-interaction disclosure or the AI-generated-content disclosure where one is required. Tested against the firm's disclosure-language inventory.
- **Vulnerable-customer-handling override** — does an injection cause the system to bypass the firm's vulnerable-customer-handling protocols (escalation triggers, hold-the-line scripts, mandatory transfer to a human). Tested against the firm's vulnerable-customer policy.
- **Complaint-pattern generation** — where the firm's complaint surveillance has flagged a theme tied to AI-generated communications, does an injection reproduce or amplify the theme. Tested where the complaint signal is present.

The `dataset_or_redteam_ref` field on these attack classes names whether the test set was constructed from the firm's product-fact library, the firm's complaint-monitoring extracts, or a third-party conduct-test corpus. Where the test was vendor-side only and did not exercise the firm's conduct surface, that gap is a recommended-action item.

##### 3. Mitigations expand to include the conduct control set

In addition to the AI-native and cyber-tagged mitigations, the conduct overlay expects the review to record:

- **Output-side fact-checking against the firm's product-fact library**: detection and refusal where the generated content states a fact that conflicts with the canonical product representation.
- **Commitment-authority enforcement**: detection of off-policy commitments (fee waivers, rate matches, settlement offers, regulatory-treatment representations) and routing to human approval.
- **AI-disclosure enforcement**: structured-output enforcement on the AI-interaction disclosure, the AI-generated-content disclosure (Marketing Rule, NAIC AI Bulletin posture), and any sector-specific disclosure tied to the use case.
- **Vulnerable-customer-handling guardrails**: hard-coded escalation triggers and transfer paths that injection cannot suppress; verified through testing.
- **Recommendation-surface controls** for Reg BI and suitability use cases: pre-decision review chain, reasoned-basis documentation, conflict-of-interest disclosure enforcement.
- **Customer-recourse path**: how a customer challenges an output the system produced; how complaints tied to the system route into the firm's complaint-handling and surveillance program; how complaints feed back to model change management.
- **Conduct-event taxonomy alignment**: tagging of injection-driven incidents as conduct-event candidates with a path to the conduct-risk function for classification.

Each conduct-tagged mitigation entry retains the schema's required fields (mitigation, type, evidence pointer, owner, exercised_in_test); the owner field for conduct-tagged entries typically names the conduct function (Head of Conduct Risk, Head of Consumer Compliance, Head of Sales Practices, Head of Distribution Compliance, Head of Marketing Review) or a named conduct-accountable manager role under SMCR for UK-licensed firms.

##### 4. Monitoring adds the conduct-tagged signal set

Beyond the cyber and privacy signals, the conduct overlay adds:

- **Off-policy-output detection rate**: rate at which output-side filters detect content conflicting with the firm's product-fact library or commitment-authority matrix.
- **Disclosure-omission rate**: rate at which generated communications lack the required AI-interaction or AI-generated-content disclosure.
- **Vulnerable-customer-handling bypass rate**: where the system serves a population that includes vulnerable customers, the rate of escalation-trigger non-fire.
- **Recommendation-rejection-on-review rate**: where the recommendation surface is human-reviewed pre-decision, the rate at which review rejects the AI-suggested recommendation; a sustained drop is a signal of either reviewer fatigue or upstream control regression.
- **Complaint-theme correlation**: the rate at which complaints tagged to AI-driven communication or AI-driven recommendation map to the use case under review; the conduct-risk function consumes the signal.

Each signal retains the schema's required fields (signal, threshold, frequency, owner, escalation path); conduct-tagged entries escalate to the conduct function in addition to or in place of the model owner.

##### 5. Incident-response section names conduct-relevant routing

The conduct overlay's load-bearing addition to the IR section is conduct-event classification and conduct-function routing. Per incident class, the entries record:

- **Conduct-event candidate flag** — whether the incident class is on the firm's conduct-event taxonomy (typically yes for any injection-driven misleading communication, off-policy commitment, recommendation-surface override, or disclosure suppression).
- **Conduct-function notification** — the path to the Head of Conduct Risk and to the conduct-accountable manager (under SMCR for UK-licensed; under firm framework otherwise) on confirmed incidents.
- **Customer-redress decision path** — where the incident produced customer harm or potential harm, the path to the redress decision (typically the consumer compliance function, with counsel on close calls).
- **Complaint-response and surveillance-loop integration** — the path back to complaint surveillance to set or refresh the watch theme on complaint coding for the affected population.
- **Regulator-engagement posture** — separate from the cyber-notification triggers (which the cyber overlay carries), the conduct overlay records the regulator-engagement triggers tied to conduct exposure (CFPB inquiry, state-AG referral, FINRA Rule 4530 reportable event, FCA Section 166 review, NAIC market-conduct exam scope).

The conduct-event candidate flag is non-optional on customer-facing systems. An injection-driven incident on a customer-facing surface that the IR section does not classify as a conduct-event candidate is a finding.

##### 6. Recommended actions add the conduct-specific items

The standard conduct-tagged recommended-actions items the overlay surfaces:

- **Conduct review on every change-of-version notice and every material change in retrieval corpus, tool inventory, or system prompt.** The conduct function or named conduct-accountable manager signs.
- **Customer-outcome distribution monitoring** — where the use case affects pricing, eligibility, or recommendation, periodic review of the distribution against the firm's conduct-framework expectations.
- **Disclosure-language refresh cadence** — the AI-interaction and AI-generated-content disclosure language is reviewed against the firm conduct-framework refresh cycle and against vendor change-of-version triggers; the customer-comprehension assessment is a conduct artifact.
- **Vulnerable-customer-handling tabletop** — annual at minimum; quarterly for tier-1 customer-facing use cases. Tests the escalation triggers, the hold-the-line scripts, and the mandatory-transfer paths against injection-driven scenarios.
- **Complaint-loop closure** — defined complaint codes the firm watches post-deployment, the cadence of the read, the escalation trigger if a theme persists.

#### Conduct-specific output additions

In the structured object (`schemas/prompt-injection-review.schema.json`):

- `cross_cutting_overlay_notes.conduct` carries the conduct-specific fields: customer-outcome read on threat-surface entries, conduct-relevant tested-attack classes, named conduct-side mitigations, conduct-event candidate classification per incident class, conduct-function routing path, conduct-accountable manager role.
- `mitigations[]` entries with conduct-tagged owner (conduct function or sub-function; named conduct-accountable manager role).
- `monitoring_detection[]` entries with conduct-tagged escalation path.
- `incident_response[]` entries with `conduct_event_candidate` and `conduct_function_notification_path` populated where applicable.
- `recommended_actions[]` entries with conduct-tagged owner role.

#### Common pitfalls in conduct-flagged prompt-injection reviews

- Treating prompt injection as cyber-only when the use case is customer-facing. The cyber overlay covers the access, logging, and notification; the conduct overlay covers the customer-outcome path, which is where the firm gets sued, fined, or remediated.
- Reading vendor red-team coverage as evidence the firm's conduct surface is hardened. Vendor red-team sets do not exercise the firm's product-fact library, commitment-authority matrix, or vulnerable-customer-handling protocols.
- Recording residual risk on a customer-facing use case without a conduct-event-candidate evaluation. Injection-driven misleading communications and off-policy commitments are conduct events; the IR section names the classification.
- Naming the model owner as the conduct-accountable manager when the firm's conduct framework names a different role. The two are separable and frequently are separated; the review is explicit.
- Treating disclosure-language as a legal artifact alone. Disclosure language is a conduct artifact; the conduct function owns the customer-comprehension assessment and the refresh cadence.
- Skipping the complaint-loop closure. A use case that ships without defined complaint codes the firm watches post-deployment is shipping without a feedback mechanism.
- Using cyber-only IR runbooks for conduct-relevant incidents. The IR runbook integration includes the path to conduct, consumer compliance, and customer-redress decision-makers.

## cyber

### Cyber cross-cutting overlay for prompt-injection-risk

When the scope record flags `cyber` for a prompt-injection review, this overlay sits as the primary lens, not a secondary one. Prompt injection is, in regulator framing, a cybersecurity risk class. The AI governance team often owns the review, but the CISO function is a co-reviewer and a co-decision-maker, not a downstream consumer.

Loaded by: `prompt-injection-risk/SKILL.md` when `scope.cross_cutting_set` includes `cyber`. For most GenAI use cases inside regulated entities, this overlay should be considered the default. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- NYDFS 23 NYCRR Part 500, especially §500.9 (risk assessment), §500.11 (third-party service-provider security), §500.16 (incident-response and BCDR plan), §500.17(a) (notice to superintendent), and the October 2024 Industry Letter on AI cybersecurity that maps these obligations onto AI deployments.
- SEC cyber disclosure rules: 8-K Item 1.05 (material cybersecurity incident disclosure within four business days of materiality determination) and Reg S-K Item 106 (annual disclosure of cyber risk-management, strategy, and governance).
- FFIEC IT Examination Handbook, Information Security and AIO booklets, applied to the AI system's serving environment, change controls, access controls, and incident-response integration.
- NIST SP 800-53 Rev. 5 control families (AC, AU, IR, SI, SR) as the underlying control catalogue for the cyber-side mitigations the review records.
- NIST AI 600-1 Generative AI Profile cyber considerations and the OWASP/MITRE/NCSC framings as the practitioner taxonomy for the threat surface.

#### What changes when cyber is flagged

##### Threat surface gains a cyber-tagging convention

Each carrier in the threat-surface table is tagged with the relevant control-catalogue families and the responsible CISO-side function. The system-prompt carrier ties to AC and SI; user input ties to AC and SI; retrieved content ties to SI and SR (supply-chain); tool output ties to SR and the application-security framing for the tool's API; memory ties to AC and SI; multi-agent message ties to SI and to the agent-platform's identity model.

The tagging is not bureaucratic; it is the seam that lets the cyber team integrate the review into existing control mappings without re-doing the work in a parallel taxonomy.

##### Tested attack classes are framed in the cyber team's vocabulary alongside the AI vocabulary

A second-line review presented in OWASP-only vocabulary lands as a foreign object on the CISO's desk. The same review presented with MITRE ATLAS technique IDs and with mappings to existing offensive-security testing categories (application security, red-team engagement, third-party assessment) lands as an extension of work already on the cyber team's plan. Both vocabularies should appear on the same row of `tested_attacks[]`.

The `dataset_or_redteam_ref` field on each tested-attack entry should name the source explicitly: vendor red-team set (vendor-self-attestation confidence), firm-internal red team (firm CISO red team or contracted offensive-security partner), third-party AI-specific assessment (e.g., independent prompt-injection assessor). Mixing these into a single line collapses the confidence signal.

##### Mitigations expand to include the standard cyber control set

In addition to the AI-native mitigations (input filtering, output filtering, structured-output enforcement, refusal behaviour, content provenance), the cyber overlay expects the review to record:

- Authentication and authorisation on the AI system's serving endpoint and on each tool the system can invoke.
- Audit logging of every model invocation, every retrieval, every tool call, every inter-agent message, with retention aligned to the firm's cyber log-retention policy and to NYDFS Part 500 §500.6 audit-trail expectations.
- Network-layer controls on the serving environment and on outbound calls (web fetch, API calls).
- Secrets handling in the prompt context: secrets should not appear in the system prompt or in retrieved content; if they do, the exfiltration risk is structural.
- Vendor and supply-chain controls: foundation-model provider security posture, model-artefact integrity controls, dependency-tree controls for self-hosted components.
- Incident-response runbook integration: the AI-misuse playbook and the foundation-model-compromise playbook are named runbooks under the firm's IR programme, not standalone AI artefacts.

Each cyber-tagged mitigation entry retains the schema's required fields (mitigation, type, evidence pointer, owner, exercised_in_test); the owner field for cyber-tagged entries typically names the CISO function or a named cyber sub-function (identity team, network security, security operations, IR).

##### Monitoring adds the cyber-tagged signal set

The baseline cyber signals to add when the overlay is flagged:

- Authentication and authorisation anomalies on the AI system's serving endpoint.
- Tool-invocation rate and pattern; for systems with tool use, sudden expansion of tool use or off-hours activity is an investigation trigger.
- Cross-scope tool query anomaly (e.g., the system queries a market-data API on tickers outside the analyst's coverage; the system retrieves customer records outside the agent's case load).
- Output-anomaly detection (sudden shifts in refusal rate, citation patterns, response-length distribution) as a leading indicator of compromise as well as drift.
- Vendor change-of-version signals for foundation-model and serving-environment dependencies; an unannounced version swap is a cyber signal as well as a model-risk signal.
- For retrieval-using systems, retrieval-source integrity signals (last-modified, content hash drift on dynamic sources).

Each signal retains the schema's required fields (signal, threshold, frequency, owner, escalation path); cyber-tagged entries escalate to the CISO function or to the security operations centre, in addition to or in place of the model owner.

##### Incident-response section names regulator-notification triggers

This is the cyber overlay's load-bearing addition to the review. The `incident_response[]` entries list, per incident class, the regulator-notification trigger that applies in the firm's footprint:

- NYDFS-covered entities: 23 NYCRR Part 500 §500.17(a) requires notice to the superintendent within 72 hours of determining a cybersecurity event has occurred that meets the rule's criteria. Prompt-injection-driven cyber events that result in unauthorised access, unauthorised action, or impairment to the security or integrity of the information system meet the criteria. The October 2024 Industry Letter signals that AI-deployment-driven events fall within scope.
- SEC public registrants: 8-K Item 1.05 requires disclosure of material cybersecurity incidents within four business days of materiality determination. Prompt-injection events causing or contributing to material cyber incidents are within scope. The materiality assessment is the registrant's; the prompt-injection review is one input.
- GLBA Safeguards Rule entities (FTC scope): 16 CFR §314.5(d) requires FTC notification of notification events involving the unauthorised acquisition of unencrypted customer information of 500 or more consumers.
- State breach laws: cross-state patchwork; the firm's privacy and incident-response programme normally maintains a state-by-state notification matrix that the review should reference rather than restate.
- Sector-specific notification triggers (state insurance commissioner notices, banking-agency notification requirements under 12 CFR Part 53 / Part 225 / Part 304 36-hour banking computer-security incident notification rule) are loaded from the relevant sector overlay.

The off-switch criterion column is where the cyber overlay bites operationally: a cyber incident class without a defined off-switch is a finding, not an acceptable position.

##### Recommended actions add the cyber-specific items

The standard cyber-tagged recommended-actions items the overlay surfaces:

- `foundation_model_swap_revalidation` flag in change management with explicit re-run of the prompt-injection review on every vendor change-of-version notice; cyber signs off on the re-run.
- IR drill cadence including AI-specific incident classes (confirmed system-prompt exfiltration, confirmed indirect-injection-driven misrouted action, suspected RAG corpus poisoning, foundation-model behaviour shift suggesting upstream compromise). Annual at minimum; quarterly for tier-1 GenAI use cases.
- Cyber tabletop exercise with the privacy officer and the relevant business function for any GenAI use case handling NPI, PHI, or material non-public information.
- Notification-decision rehearsal: the materiality-assessment process for SEC 8-K Item 1.05 and the §500.17(a) notification process for NYDFS-covered entities, exercised against AI-specific incident scenarios.

#### Cyber-specific output additions

In the structured object (`schemas/prompt-injection-review.schema.json`):

- `cross_cutting_overlay_notes.cyber` carries the cyber-specific fields: control-family tagging on threat-surface entries, MITRE ATLAS technique mapping on tested-attack entries, named cyber-side mitigations, named regulator-notification triggers per incident class.
- `mitigations[]` entries with cyber-tagged owner (CISO function or sub-function).
- `monitoring_detection[]` entries with cyber-tagged escalation path.
- `incident_response[]` entries with `regulator_notification_trigger` populated where applicable.
- `recommended_actions[]` entries with cyber-tagged owner role.

#### Common pitfalls in cyber-flagged prompt-injection reviews

The recurring failure modes the review should not fall into:

- Treating the AI governance team as the sole reviewer. Prompt injection is, in NYDFS framing, a cybersecurity risk class; the CISO function co-reviews and co-decides on the residual risk acceptance.
- Treating vendor adversarial-test results as evidence the deployed prompt surface is hardened. The firm's prompt template, retrieval corpus, and tool inventory are firm-side surfaces and need firm-side testing.
- Failing to integrate the AI-misuse runbook into the firm's IR programme. A standalone AI playbook that does not connect to the named cyber IR runbook is a paper artefact.
- Recording residual risk without a regulator-notification trigger evaluation. NYDFS §500.17(a) and SEC 8-K Item 1.05 are not optional considerations.
- Omitting the off-switch criterion for cyber-relevant incident classes. A confirmed exfiltration with no defined off-switch is a finding.
- Using AI-only vocabulary in a review the cyber team has to consume. MITRE ATLAS mappings cost little to add and turn the artefact into something the cyber team can integrate without translation.

## privacy

### Privacy cross-cutting overlay for prompt-injection-risk

When the scope record flags `privacy` for a prompt-injection review, this overlay loads alongside the cyber overlay (which is the default cross-cutting lens on this skill). Privacy is not a secondary concern. Prompt injection has three load-bearing privacy paths: training-data and prompt-history extraction (the model emits content that the firm has stored, sometimes regulated personal data, sometimes another customer's data), retrieval exfiltration (the system surfaces RAG-corpus content the requesting user is not authorised to read), and tool-driven personal-data egress (an injected instruction directs a tool call that exfiltrates regulated personal data to an attacker-controlled destination). The privacy function is a co-reviewer on any review where these paths are material.

Loaded by: `prompt-injection-risk/SKILL.md` when `scope.cross_cutting_set` includes `privacy`. For any GenAI use case touching NPI, PHI, PCI, biometric data, customer prompts that may contain regulated personal data inadvertently (claims FNOL, customer-support chats, RAG-over-customer-documents flows), this overlay should be considered the default. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- **GLBA Safeguards Rule, 16 CFR Part 314 (FTC scope) and the interagency Safeguards rule for banks** — §314.4 program elements, §314.4(c) access controls and encryption, §314.4(d) monitoring and testing, §314.4(f) service-provider obligations, §314.5(d) FTC notification of notification events involving the unauthorised acquisition of unencrypted customer information of 500 or more consumers.
- **GLBA Privacy Rule, Regulation P, 12 CFR Part 1016** — privacy-notice and information-sharing posture; relevant where prompt content or model output flows into a service-provider chain.
- **HIPAA Privacy and Security Rules, 45 CFR Parts 160, 162, and 164** — where prompts or model outputs may carry PHI (claims-handling assistants, member-services chatbots, life and health underwriting copilots), the BAA chain to the foundation-model provider, the inference-platform provider, and any retrieval / vector-database vendor is required. Model outputs derived from PHI inherit PHI status; retention of outputs is a HIPAA business-associate question.
- **State comprehensive privacy laws** — CCPA / CPRA (California), VCDPA (Virginia), CTDPA (Connecticut), CPA (Colorado), and the rolling list. GLBA-covered data is excluded from many state regimes but the GLBA-exemption scope is read state-by-state and feature-by-feature; prompt-history retention often crosses the GLBA-covered scope into general personal-data territory (employee identifiers, free-text input outside transaction context).
- **FCRA, 15 USC §1681, and Regulation V, 12 CFR Part 1022** — where the AI surface consumes consumer-report data (a prompt to "summarise this credit report" or a RAG corpus including consumer-report excerpts), FCRA reach attaches to the surface and to the audit trail.
- **Reg S-P, 17 CFR §248.30 (May 2024 amendments)** [verify exact compliance dates by entity type and size] — for SEC-registered advisers, BDs, and funds, customer-information-safeguarding and breach-notification posture; service-provider written contracts requiring breach notification.
- **NYDFS 23 NYCRR Part 500 §500.13 and §500.15** — access controls and encryption requirements bearing on prompt-content access and storage; the privacy frame layers on top of the cyber-program frame.
- **GDPR / UK GDPR** — for systems with EU / UK exposure, Article 5 principles (purpose limitation, data minimisation, storage limitation), Article 22 automated-decision-making, Article 28 processor relationships, Article 32 security of processing. Data Protection Impact Assessment under Article 35 is the parallel artifact; the prompt-injection review is one input where the DPIA covers the GenAI use case.

#### What changes when privacy is flagged

##### 1. Threat surface gains a privacy-tagging convention

Each carrier in the threat-surface table is tagged with the personal-data classes it may carry and the lawful basis under which the system processes them. The user-input carrier ties to NPI / PHI / employee data (the customer or employee typed it); the retrieved-content carrier ties to whatever personal data the RAG corpus contains; the tool-output carrier ties to whatever the tool returns from a system-of-record; the memory carrier ties to the personal-data classes the memory retains across sessions. The trust-basis column reads alongside the lawful-basis column: a carrier marked "trusted, no controls" with PHI in its content is a privacy finding before it is a cyber finding.

##### 2. Tested attack classes expand to include personal-data extraction paths

The AI-native attack classes (direct override, indirect injection, system-prompt exfiltration, jailbreak, tool hijack, agent redirect, multi-agent message injection, multimodal injection, memory poisoning) carry through; the privacy overlay adds explicit testing for the personal-data extraction surface:

- **Training-data extraction** (model recites training content verbatim under adversarial prompting). Vendor red-team coverage on base-model training-data extraction is vendor-side evidence; the firm's deployed system extends the surface (firm fine-tuning data, firm RAG content) and needs firm-side testing.
- **Cross-tenant / cross-user retrieval exfiltration** (the model returns RAG content the requesting user is not authorised to read). The retrieval-source authorisation model is the seam; testing exercises whether instruction-following can defeat the authorisation check.
- **Memory cross-contamination** (one user's session content leaks into another user's session via shared memory). Exercises the isolation boundary on persistent-memory systems.
- **Tool-driven personal-data egress** (the model issues a tool call that exfiltrates personal data to a non-firm destination). Exercises the tool authorisation surface and the network-egress controls.
- **Output-channel exfiltration** (the model encodes personal data into outputs intended to flow to attacker-readable channels — log lines, error messages, audit trails). Exercises the output-routing surface.

The `dataset_or_redteam_ref` field on these attack classes names the source explicitly: vendor red-team coverage on the base model is named as such; firm-side coverage on the deployed-system surface is named separately; published research benchmarks (TruthfulQA, AnthropicEval, MITRE ATLAS adversarial test suites) are named where the firm's red team consumed them.

##### 3. Mitigations expand to include the standard privacy control set

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

##### 4. Monitoring adds the privacy-tagged signal set

Beyond the cyber-tagged signals (auth anomalies, tool-invocation rate, output-anomaly detection, vendor-version monitoring, retrieval-source integrity), the privacy overlay adds:

- **Output-PII detection rate**: the rate at which output-side filters detect personal data being returned where the policy says it should not be. A spike is a leading indicator of either a successful injection or a control regression.
- **Retrieval-authorisation violation signals**: where the retrieval pipeline tracks per-user authorisation, violations are surfaced as a privacy signal as well as an authorisation signal.
- **Cross-tenant or cross-user retrieval anomalies**: signals from the retrieval-authorisation layer that user A's session retrieved content from user B's scope.
- **Region-egress anomalies on the inference path**: where the firm pins inference to a region, anomalies in the region tag on inference responses are a privacy signal.
- **Sub-processor change signals**: where the vendor publishes sub-processor changes, the signal is a privacy event with a contract-clock attached.
- **Output-retention overrun**: where the firm's policy says outputs are retained N days and the firm-side log shows older content, the signal is a privacy event.

Each signal retains the schema's required fields (signal, threshold, frequency, owner, escalation path); privacy-tagged entries escalate to the privacy function in addition to or in place of the model owner.

##### 5. Incident-response section names privacy-notification triggers

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

##### 6. Recommended actions add the privacy-specific items

The standard privacy-tagged recommended-actions items the overlay surfaces:

- **DPIA / PIA refresh on every change-of-version notice and every material change in the retrieval corpus or tool inventory.** The privacy function signs the refresh.
- **BAA chain refresh on PHI-touching use cases** at the same cadence as foundation-model and inference-platform vendor changes.
- **Sub-processor change-notice review cadence** with the privacy function as named owner.
- **Privacy tabletop exercise** with the CISO function for any GenAI use case handling NPI, PHI, or material non-public information; rehearses the §314.5(d) / state / HIPAA / Reg S-P / GDPR notification chains against AI-specific incident scenarios.
- **Right-to-deletion-against-LLM rehearsal** for use cases subject to state privacy laws or GDPR, exercising the firm's response mechanism with the foundation-model and inference-platform vendors.

#### Privacy-specific output additions

In the structured object (`schemas/prompt-injection-review.schema.json`):

- `cross_cutting_overlay_notes.privacy` carries the privacy-specific fields: personal-data-class tagging on threat-surface entries, lawful-basis column, named privacy-side mitigations, retention windows, training-use posture per contract, sub-processor list reference, named privacy-notification triggers per incident class.
- `mitigations[]` entries with privacy-tagged owner (privacy function or sub-function).
- `monitoring_detection[]` entries with privacy-tagged escalation path.
- `incident_response[]` entries with `privacy_notification_trigger` populated where applicable.
- `recommended_actions[]` entries with privacy-tagged owner role.

#### Common pitfalls in privacy-flagged prompt-injection reviews

- Skipping the prompt-as-customer-data analysis on a use case because the firm "doesn't intend to send PII". Inadvertent NPI / PHI in narratives is the dominant failure mode (claims FNOL, customer-support chats, RAG over customer documents).
- Treating the vendor's marketing-page training-use posture as the contractual posture. The contract clause is the operative document.
- Reading SOC 2 Type II as if it covered privacy specifically. SOC 2 covers the Privacy criterion only when the vendor opts in.
- Missing the HIPAA business-associate analysis on a "tech vendor" that incidentally touches PHI through prompts or retrieval.
- Treating the GLBA exemption from a state privacy law as blanket exemption when the prompt content or RAG corpus reaches data outside the GLBA-covered scope.
- Recording residual risk without a privacy-notification trigger evaluation. §314.5(d), state laws, HIPAA, Reg S-P, and GDPR Article 33 are not optional considerations.
- Cross-border egress handled silently. Offshore inference endpoints and cross-region serving are named, not assumed.
- Right-to-deletion and right-to-correction treated as out of scope. The mechanism with the foundation-model vendor and the inference-platform vendor is part of the privacy posture; the contract clause is recorded.
