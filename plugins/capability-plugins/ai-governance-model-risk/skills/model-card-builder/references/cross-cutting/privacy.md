# Privacy cross-cutting overlay for model-card-builder

When the scope record flags `privacy` for the model use case, this overlay adds privacy-specific content to named card sections. The model card is not the firm's privacy-impact assessment; the PIA is its own artifact under the firm's privacy program. The card surfaces the privacy considerations that a second-line reviewer (and a privacy-office reviewer) needs to see in the model-card frame, and points to the PIA in source trace.

Loaded by: `model-card-builder/SKILL.md` when `scope.cross_cutting_set` includes `privacy`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- GLBA Safeguards Rule (16 CFR Part 314) for non-public personal information (NPI) handled by financial institutions, including the program-design and risk-assessment provisions.
- CCPA / CPRA (California) and state privacy laws including VCDPA (Virginia), CTDPA (Connecticut), and the rolling roster of state laws that follow the same general structure (consumer rights to know, delete, correct, opt out of certain uses).
- HIPAA Privacy and Security Rules where protected health information is in scope (life and health insurance contexts, healthcare-adjacent fintechs, claims AI).
- GDPR Article 22 (decisions based solely on automated processing, including profiling) where EU customers are in the operating footprint; right to obtain meaningful information about the logic involved.
- EU AI Act Article 27 (fundamental rights impact assessment, FRIA) where the model is a high-risk AI system used by a deployer in scope of the obligation.
- ECOA / Reg B (US) right-to-explanation in adverse-action notices for credit-decisioning models, which sits at the intersection of fair-lending and privacy.

## What changes for privacy-flagged model cards

### 1. Intended use names the privacy posture

The intended-use section adds a privacy-notice-posture line: which privacy notice covers this use, when it was last updated to reflect this use, and where the disclosure to the consumer lives. For consumer-facing GenAI, the prompt-as-customer-data lens is named explicitly: customer-supplied prompt content may itself be NPI, PHI, or otherwise regulated, and the privacy posture covers the prompt surface as well as the training and reference data.

### 2. Training and reference data section gains a privacy-classification subsection

Each data source carries a privacy classification: NPI under GLBA, PHI under HIPAA, PCI cardholder data, customer-supplied prompts, public, confidential. For foundation-model training data, firm visibility is typically limited to vendor system-card statements; record at vendor-self-attestation confidence and do not extend vendor claims to cover the firm's deployed prompt surface (the most common error). Lawful-basis-for-processing is a data-section field where a state or international privacy law in operating footprint requires it.

A specific subsection covers the prompt surface for GenAI: where prompt content is stored, retention period, whether prompts are used for any vendor-side training or evaluation, the BAA or DPA posture with the model vendor, and the firm-side controls preventing prompt content from flowing into vendor training.

### 3. Controls section adds privacy-tagged controls

Preventive: data-minimisation in training and prompt content, redaction or tokenisation of NPI/PHI before model invocation where required, retention controls on prompt and output stores. Detective: privacy-incident detection (e.g., model-output containing NPI/PHI not in the input), audit-logging on data access. Response: privacy-incident response runbook integration, customer-rights-request handling (right to know, right to delete, right to opt out of automated decisioning where applicable).

### 4. Change management adds privacy re-validation triggers

A change in privacy notice covering the use case, expansion of data sources to include a new sensitivity category (NPI, PHI, biometric, children's data), a change in vendor BAA/DPA posture, and entry into a new state or jurisdiction with privacy-law differences are each re-validation triggers.

### 5. Sign-off questions tagged to privacy

The named privacy-office reviewer is a sign-off audience; questions cover the privacy-notice coverage, the prompt-surface classification, the BAA/DPA posture, the customer-rights workflow, the PIA status (is one on file, when, by whom), and for credit-decisioning under ECOA the right-to-explanation method.

## Privacy-specific output template additions

- A "Privacy considerations" subsection inside `intended_use` and inside `data` (in the structured object: `intended_use.privacy_subsection`, `data[].privacy_classification`, `data[].lawful_basis_for_processing` where applicable, `data[].vendor_baa_or_dpa_reference`).
- Prompt-surface treatment in the data block when the architecture is GenAI, with retention, vendor-side training posture, and redaction posture as named fields.
- Privacy-tagged entries in `controls[]` (preventive on data-minimisation and redaction, detective on privacy-incident detection, response on customer-rights workflow).
- Privacy-tagged entries in `change_management[]` (privacy notice change, data-sensitivity expansion, BAA/DPA change, jurisdiction expansion).
- Privacy-tagged sign-off questions (named privacy-office reviewer, PIA status, customer-rights workflow integration, prompt-surface classification, where applicable Article 22 right-to-explanation method).

## Common pitfalls in privacy-flagged model cards

- Classifying foundation-model training data without addressing in-context customer prompts. The prompt surface is where customer NPI/PHI most often enters a GenAI use case; vendor system-card statements about training-data privacy do not extend to the firm's deployed prompt surface.
- Treating a vendor's data-processing posture as covering the firm; the firm's BAA (HIPAA) or DPA (GDPR / state privacy) is the firm's evidence, not the vendor's marketing.
- Assuming a HIPAA business-associate agreement with the LLM vendor exists when it does not; PHI flowing into a non-BAA-covered model is a recordable issue, not a card-body assertion of HIPAA coverage.
- Defaulting to "this is anonymous" without actually anonymising prompts. PII redaction is a control with evidence; the claim without the control is a card-recordable issue.
- Omitting the customer-rights workflow for an automated-decisioning use case. Right to know, right to delete, and where applicable right to opt out of automated decisioning are workflow obligations, not policy statements.
- Carrying the PIA conclusion into the card as if it were the PIA. The card points to the PIA in source trace; the PIA itself is the privacy-program artifact.
