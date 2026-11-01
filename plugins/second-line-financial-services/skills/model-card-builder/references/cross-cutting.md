# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Conduct cross-cutting overlay for model-card-builder

When the scope record flags `conduct` for the model use case, this overlay adds conduct-risk content to named card sections. Conduct risk in second-line vocabulary is not the same as fairness as a model property; it is the customer-outcome and market-integrity lens, the named-manager accountability lens, and the regulatory-engagement lens. The card's conduct content sits alongside the fairness-and-explainability section, not inside it.

Loaded by: `model-card-builder/SKILL.md` when `scope.cross_cutting_set` includes `conduct`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- FCA Senior Managers and Certification Regime (SMCR) for UK-licensed entities, where named-manager accountability for prescribed responsibilities reaches into model-related decisions for in-scope firms.
- US enforcement themes on algorithmic discrimination and unfair / abusive practices, including the April 2023 Joint Statement on Enforcement Efforts Against Discrimination and Bias in Automated Systems (CFPB, DOJ, EEOC, FTC) and the CFPB Circulars on AI in adverse-action notices and consumer credit.
- Conduct risk taxonomy as commonly framed by second-line conduct functions: customer outcomes, market integrity, employee conduct, regulatory engagement, financial-crime adjacency. Firm-specific taxonomy lives in `references/firm-overlay.md` when present.
- Product-governance expectations: target-market definition, product testing, distribution suitability. For FCA-regulated entities, PROD applies; for non-UK entities, the firm's own product-governance framework applies and the conduct overlay names that framework.

#### What changes for conduct-flagged model cards

##### 1. Intended use gains a customer-outcome lens

The intended-use section adds a customer-outcome subsection: who the customer is, what outcome the model produces for the customer (decision, price, experience, recommendation, refusal), and which customer journeys are touched. The firm-impact framing (efficiency, throughput, loss reduction) sits separately; the conduct lens is customer-outcome first. Out-of-scope decisions are sharpened to name the customer-outcome boundary.

##### 2. Fairness section addresses customer-outcome disparity, not only protected-class disparity

Customer-outcome disparity is the conduct-tagged extension of the fairness section: where the model produces materially different customer outcomes (price, eligibility, access, experience) across customer segments that are not protected classes but are policy-relevant (rural, low-balance, digital-only, English-as-second-language, recent-immigrant cohorts where lawful to consider), the conduct overlay expects those segments named and the disparity assessed. The vocabulary is "customer-outcome disparity" alongside the protected-class disparity vocabulary; the test framing is recorded so the reviewer sees which lens is in use.

##### 3. Controls section adds conduct-tagged review gates

Beyond model-risk-committee and validator review, conduct-flagged cards typically include a product committee or customer-outcome committee review gate; for UK-licensed firms with PROD in scope, the product-governance committee review is a controls-section item. For consumer-facing models, the complaint surface is a controls-section item: complaint-rate monitoring, complaint-code monitoring, root-cause feedback into the change-management table.

##### 4. Sign-off names the conduct-accountable manager

For UK-licensed firms in SMCR scope, the senior manager with allocated responsibility for the relevant prescribed responsibility is a named sign-off audience. For non-UK firms, the firm's conduct framework names a manager (often the head of the relevant business or the head of consumer / customer); the card names the role, not the individual. The model owner is not by default the conduct-accountable manager; the card is explicit about which is which.

##### 5. Change management adds conduct re-validation triggers

A change in target market or distribution channel, a change that materially shifts customer-outcome distribution, a complaint-rate breach, and a regulatory-engagement event (CFPB inquiry, FCA Section 166 review, state DOI inquiry, fair-lending exam finding) are each conduct re-validation triggers.

#### Conduct-specific output template additions

- A "Conduct considerations" subsection inside `intended_use` (in the structured object: `intended_use.conduct_subsection` covering customer-outcome lens, customer-journey impact, target market and distribution).
- Customer-outcome-disparity entries in `fairness_results[]` alongside protected-class-disparity entries, with `test_framing` set to make the lens explicit.
- Conduct-tagged entries in `controls[]` (product committee or customer-outcome committee gate, complaint-surface monitoring control, suitability or best-interest control where applicable).
- Conduct-tagged entries in `change_management[]` (target-market change, distribution-channel change, customer-outcome shift, complaint-rate breach, regulatory-engagement event).
- A `conduct_accountable_manager_role` field in `card_metadata` naming the role under SMCR or the firm's conduct framework, distinct from the model owner.
- Conduct-tagged sign-off questions (named conduct-accountable manager, customer-outcome assessment status, complaint-surface integration, target-market alignment, regulatory-engagement posture).

#### Common pitfalls in conduct-flagged model cards

- Framing fairness as a model property without addressing customer-outcome disparity. A model can clear disparate-impact tests on protected classes and still produce materially different customer outcomes across policy-relevant segments; conduct frames the second lens.
- Treating SMCR or the firm's conduct framework as compliance overhead rather than as a conduct-risk-management input to the card. The named-manager role is a substantive sign-off, not a signature line.
- Assuming the model owner is the conduct-accountable manager when the conduct framework names a different role. The two are separable and frequently are separated; the card is explicit.
- Missing the customer-journey impact when the model affects customer experience but not directly customer pricing or eligibility. A chatbot that handles initial enquiries shapes customer outcome through access and friction, not only through the explicit decision; the conduct lens catches this where a fairness-only lens does not.
- Carrying enforcement-theme risk into the card as a generic warning. Where the firm has a specific monitoring posture for a specific enforcement theme (CFPB AI circulars, the April 2023 Joint Statement themes), the card records the firm posture; where it does not, the gap is recorded as a sign-off question rather than asserted as coverage.
- Treating the complaint surface as a customer-service metric rather than a conduct signal. Complaint-rate and complaint-code drift are leading indicators of customer-outcome harm and belong in the monitoring plan with named owner and escalation.

## cyber

### Cyber cross-cutting overlay for model-card-builder

When the scope record flags `cyber` for the model use case, this overlay adds cyber-specific content to named card sections. It does not replace the firm's information-security risk assessment; it is the model-card-side surfacing of cyber considerations that a second-line reviewer (and an examiner) will look for when the model is itself an attack surface or attack target.

Loaded by: `model-card-builder/SKILL.md` when `scope.cross_cutting_set` includes `cyber`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- NYDFS 23 NYCRR Part 500, especially the third-party-risk, incident-response, and incident-notice provisions (Part 500 governs covered entities; the model is in scope when it sits inside a covered entity's information system or is hosted by a third-party service provider).
- SEC cyber disclosure rules: 8-K Item 1.05 (material cybersecurity incident disclosure) and Reg S-K Item 106 (cybersecurity risk management, strategy, and governance) where the registrant is public.
- FFIEC IT Examination Handbook, Information Security and Cybersecurity sections, applied to the model's serving environment, change controls, and access controls.
- NIST AI 600-1 (Generative AI Profile) cyber considerations: prompt-injection threat surface, model-supply-chain attack vectors, training-data poisoning, evasion and extraction attacks.

#### What changes for cyber-flagged model cards

##### 1. System description gains a cybersecurity considerations subsection

The card's system description block adds a cyber subsection that names the threat surface for this specific model: input channels (chat, API, batch, retrieval triggers), prompt-injection robustness posture (tested, untested, vendor-tested), model-supply-chain dependence (foundation-model provider, model-hosting environment, model artefact integrity controls), and tool/agent privileges where applicable. For a traditional ML model, the subsection is shorter: serving environment, model-artefact integrity, access controls. For a GenAI model with tool use or agentic behaviour, the subsection is the longest in the card.

##### 2. Training and reference data section flags poisoning and extraction exposure

For models trained or fine-tuned on firm data, the data section flags training-data integrity controls (provenance, change-detection on training corpora) and the residual exposure to data-poisoning where the controls are partial. For RAG-using models, the retrieval corpus is itself a cyber-relevant surface (retrieval-corpus injection is a real attack pattern); the data section names corpus access controls, content-validation controls, and the refresh integrity model.

##### 3. Robustness section gains adversarial cyber tests

Robustness entries for prompt injection, jailbreak, model extraction, and evasion are expected for GenAI cards in cyber-flagged scope. Vendor-supplied adversarial test results are recorded with vendor-self-attestation confidence; firm-independent red-team results carry higher confidence and are listed separately. Absence of firm-independent testing is itself a card-recordable item under the cyber overlay (it goes to source trace as `[evidence needed]` and to sign-off questions, not silently into the card body).

##### 4. Monitoring plan adds cyber-relevant signals

Monitoring entries the cyber overlay expects:

- Authentication and authorisation anomalies on the model's serving endpoint.
- Prompt-injection detection signals (where the firm has a detection layer; if not, the absence is recorded).
- Output-anomaly detection (sudden shifts in refusal rate, citation patterns, tool-call patterns are leading indicators of compromise as well as drift).
- Vendor change-of-version signals for foundation-model and serving-environment dependencies; an unannounced version swap is a cyber signal as well as a model-risk signal.
- For GenAI with tools or agent privileges, tool-invocation rate and pattern monitoring; sudden expansion of tool use is an investigation trigger.

Each monitoring entry retains the five required fields (metric, threshold, frequency, owner, escalation path); cyber-relevant entries typically escalate to the CISO function in addition to the model owner.

##### 5. Controls section adds cyber-tagged controls

Preventive: input validation, output filtering, prompt-template guardrails, tool-boundary controls, secrets-handling in prompt context. Detective: prompt-injection detection layer, output-anomaly detection, audit-logging on model invocations and retrievals. Response: incident-response runbook integration (the model-misuse playbook, the foundation-model-compromise playbook), with the named owner being the CISO function in coordination with the model owner.

##### 6. Change management adds cyber re-validation triggers

Foundation-model swap is a cyber re-validation trigger as well as a model-risk re-validation trigger. Hosting-environment migration, retrieval-corpus access-control change, and tool-inventory expansion are each cyber re-validation triggers.

#### Cyber-specific output template additions

- A "Cybersecurity considerations" subsection inside `architecture` (in the structured object: `architecture.cyber_subsection`).
- Cyber-tagged entries in `monitoring[]` with the named CISO-function escalation path.
- Cyber-tagged entries in `controls[]` (preventive, detective, response).
- Cyber-tagged entries in `change_management[]` (foundation-model swap, hosting-environment migration, retrieval-corpus access change, tool-inventory expansion).
- Cyber-tagged sign-off questions (named CISO-function reviewer, prompt-injection robustness posture, model-supply-chain dependence, incident-response integration).

#### Common pitfalls in cyber-flagged model cards

- Treating "vendor pen-tested" or vendor-supplied adversarial-test results as evidence the deployed prompt surface is hardened. The firm's prompt template, retrieval corpus, and tool inventory are firm-side surfaces and need firm-side testing.
- Failing to monitor for prompt-injection-as-attack-vector, framing prompt-injection only as a quality issue. It is also a control-evasion path when the model has tool or agent privileges.
- Assuming model isolation when the model has tool or agent privileges. Tool privileges are lateral-movement opportunities; the card's controls section needs to surface tool-boundary controls explicitly.
- Omitting vendor change-of-version monitoring; a silent foundation-model swap is both a model-risk event and a cyber event.
- Treating the cyber overlay as the CISO's document. The card is the firm-side governance artifact; the CISO function is a reviewer and an escalation path, not the owner.

## privacy

### Privacy cross-cutting overlay for model-card-builder

When the scope record flags `privacy` for the model use case, this overlay adds privacy-specific content to named card sections. The model card is not the firm's privacy-impact assessment; the PIA is its own artifact under the firm's privacy program. The card surfaces the privacy considerations that a second-line reviewer (and a privacy-office reviewer) needs to see in the model-card frame, and points to the PIA in source trace.

Loaded by: `model-card-builder/SKILL.md` when `scope.cross_cutting_set` includes `privacy`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- GLBA Safeguards Rule (16 CFR Part 314) for non-public personal information (NPI) handled by financial institutions, including the program-design and risk-assessment provisions.
- CCPA / CPRA (California) and state privacy laws including VCDPA (Virginia), CTDPA (Connecticut), and the rolling roster of state laws that follow the same general structure (consumer rights to know, delete, correct, opt out of certain uses).
- HIPAA Privacy and Security Rules where protected health information is in scope (life and health insurance contexts, healthcare-adjacent fintechs, claims AI).
- GDPR Article 22 (decisions based solely on automated processing, including profiling) where EU customers are in the operating footprint; right to obtain meaningful information about the logic involved.
- EU AI Act Article 27 (fundamental rights impact assessment, FRIA) where the model is a high-risk AI system used by a deployer in scope of the obligation.
- ECOA / Reg B (US) right-to-explanation in adverse-action notices for credit-decisioning models, which sits at the intersection of fair-lending and privacy.

#### What changes for privacy-flagged model cards

##### 1. Intended use names the privacy posture

The intended-use section adds a privacy-notice-posture line: which privacy notice covers this use, when it was last updated to reflect this use, and where the disclosure to the consumer lives. For consumer-facing GenAI, the prompt-as-customer-data lens is named explicitly: customer-supplied prompt content may itself be NPI, PHI, or otherwise regulated, and the privacy posture covers the prompt surface as well as the training and reference data.

##### 2. Training and reference data section gains a privacy-classification subsection

Each data source carries a privacy classification: NPI under GLBA, PHI under HIPAA, PCI cardholder data, customer-supplied prompts, public, confidential. For foundation-model training data, firm visibility is typically limited to vendor system-card statements; record at vendor-self-attestation confidence and do not extend vendor claims to cover the firm's deployed prompt surface (the most common error). Lawful-basis-for-processing is a data-section field where a state or international privacy law in operating footprint requires it.

A specific subsection covers the prompt surface for GenAI: where prompt content is stored, retention period, whether prompts are used for any vendor-side training or evaluation, the BAA or DPA posture with the model vendor, and the firm-side controls preventing prompt content from flowing into vendor training.

##### 3. Controls section adds privacy-tagged controls

Preventive: data-minimisation in training and prompt content, redaction or tokenisation of NPI/PHI before model invocation where required, retention controls on prompt and output stores. Detective: privacy-incident detection (e.g., model-output containing NPI/PHI not in the input), audit-logging on data access. Response: privacy-incident response runbook integration, customer-rights-request handling (right to know, right to delete, right to opt out of automated decisioning where applicable).

##### 4. Change management adds privacy re-validation triggers

A change in privacy notice covering the use case, expansion of data sources to include a new sensitivity category (NPI, PHI, biometric, children's data), a change in vendor BAA/DPA posture, and entry into a new state or jurisdiction with privacy-law differences are each re-validation triggers.

##### 5. Sign-off questions tagged to privacy

The named privacy-office reviewer is a sign-off audience; questions cover the privacy-notice coverage, the prompt-surface classification, the BAA/DPA posture, the customer-rights workflow, the PIA status (is one on file, when, by whom), and for credit-decisioning under ECOA the right-to-explanation method.

#### Privacy-specific output template additions

- A "Privacy considerations" subsection inside `intended_use` and inside `data` (in the structured object: `intended_use.privacy_subsection`, `data[].privacy_classification`, `data[].lawful_basis_for_processing` where applicable, `data[].vendor_baa_or_dpa_reference`).
- Prompt-surface treatment in the data block when the architecture is GenAI, with retention, vendor-side training posture, and redaction posture as named fields.
- Privacy-tagged entries in `controls[]` (preventive on data-minimisation and redaction, detective on privacy-incident detection, response on customer-rights workflow).
- Privacy-tagged entries in `change_management[]` (privacy notice change, data-sensitivity expansion, BAA/DPA change, jurisdiction expansion).
- Privacy-tagged sign-off questions (named privacy-office reviewer, PIA status, customer-rights workflow integration, prompt-surface classification, where applicable Article 22 right-to-explanation method).

#### Common pitfalls in privacy-flagged model cards

- Classifying foundation-model training data without addressing in-context customer prompts. The prompt surface is where customer NPI/PHI most often enters a GenAI use case; vendor system-card statements about training-data privacy do not extend to the firm's deployed prompt surface.
- Treating a vendor's data-processing posture as covering the firm; the firm's BAA (HIPAA) or DPA (GDPR / state privacy) is the firm's evidence, not the vendor's marketing.
- Assuming a HIPAA business-associate agreement with the LLM vendor exists when it does not; PHI flowing into a non-BAA-covered model is a recordable issue, not a card-body assertion of HIPAA coverage.
- Defaulting to "this is anonymous" without actually anonymising prompts. PII redaction is a control with evidence; the claim without the control is a card-recordable issue.
- Omitting the customer-rights workflow for an automated-decisioning use case. Right to know, right to delete, and where applicable right to opt out of automated decisioning are workflow obligations, not policy statements.
- Carrying the PIA conclusion into the card as if it were the PIA. The card points to the PIA in source trace; the PIA itself is the privacy-program artifact.
