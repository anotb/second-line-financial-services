# Privacy cross-cutting overlay for validation-plan

When the scope record flags `privacy` for the model use case, this overlay adds privacy-specific scope items to the validation plan. The validation plan is not the firm's privacy-impact assessment; the PIA is its own artifact under the firm's privacy program. The plan scopes the privacy-relevant tests and evidence the validator needs, and points to the PIA in source trace.

Loaded by: `validation-plan/SKILL.md` when `scope.cross_cutting_set` includes `privacy`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- GLBA Safeguards Rule (16 CFR Part 314) for non-public personal information (NPI) handled by financial institutions.
- CCPA / CPRA (California) and the rolling state-privacy roster (VCDPA Virginia, CTDPA Connecticut, and others following the same general structure).
- HIPAA Privacy and Security Rules (45 CFR Parts 160 and 164) where protected health information is in scope (life and health insurance; healthcare-adjacent fintechs; claims AI).
- GDPR Article 22 (decisions based solely on automated processing, including profiling) and the right to obtain meaningful information about the logic involved.
- EU AI Act Article 27 (fundamental rights impact assessment, FRIA) where the model is a high-risk AI system used by a deployer in scope of the obligation.
- ECOA / Reg B right-to-explanation in adverse-action notices for credit-decisioning models, sitting at the intersection of fair-lending and privacy.

## What changes for privacy-flagged validation plans

### 1. Data review gains a privacy-classification subsection

Each data source in scope of validation carries a privacy classification: NPI under GLBA, PHI under HIPAA, PCI cardholder data, customer-supplied prompts, public, confidential. For foundation-model training data, firm visibility is typically limited to vendor system-card statements; record at vendor-self-attestation confidence and do not extend vendor claims to cover the firm's deployed prompt surface (the most common error).

A specific subsection covers the prompt surface for GenAI: where prompt content is stored, retention period, whether prompts are used for any vendor-side training or evaluation, the BAA or DPA posture with the model vendor, and the firm-side controls preventing prompt content from flowing into vendor training. Lawful-basis-for-processing is a data-section field where a state or international privacy law in operating footprint requires it.

### 2. Outcomes analysis adds privacy-specific tests

Privacy-specific tests in scope:

- PII / NPI memorisation: query the model for known training records (or known retrieval entries) and measure leakage rate.
- Training-data extraction: structured prompts attempting to reconstruct training samples; measure reconstruction precision.
- Cross-customer retrieval (for RAG): test queries from one customer context that should not surface another customer's content; measure leak rate.
- PHI-leak (HIPAA contexts): output sampling for PHI elements not in the input or in scope of the use case.
- Prompt-template extraction: query-based attempts to surface the system prompt or retrieval prompt; measure extraction rate.

For each test, the success criterion is in firm-policy units (zero leaks, leak rate at or below threshold) and the owner is named.

### 3. Robustness scope adds privacy-relevant adversarial tests

Privacy-relevant adversarial tests overlap with the cyber overlay but have privacy-specific framing:

- Membership-inference attack on training-data privacy.
- Prompt-injection on indirect content (uploaded documents, retrieved content) attempting to extract NPI/PHI from the prompt context.
- Differential-privacy guarantees check (where the firm asserts DP; verify the assertion).

### 4. Monitoring scope adds privacy signals

Privacy monitoring entries, each with the six required fields:

- PII/NPI leak detection on outputs (sampling cadence, threshold, owner: privacy office in coordination with model owner, escalation: CPO, revalidation trigger: any leak above threshold).
- Cross-customer retrieval audit (for RAG; continuous if feasible, escalation: information security and privacy office).
- Customer-rights-request processing for the model's outputs (right to know, right to delete, right to opt out of automated decisioning where applicable); turnaround time as a metric.
- Privacy-incident detection on the model's processing surface; integration with the firm's incident-response function.

### 5. Effective challenge gains privacy-tagged questions

Privacy-tagged effective-challenge questions probe concrete gaps:

- The PIA was completed at design; what evidence supports that the deployed system matches the PIA assumptions.
- The vendor BAA / DPA covers the model service; what is the firm's evidence that prompt content does not flow into vendor training or evaluation.
- For an automated-decisioning use case in EU footprint, what is the firm's process for the right to obtain meaningful information about the logic involved (GDPR Article 22).
- For a credit-decisioning model, what is the SHAP / reason-code-mapped adverse-action notice generation method, and how does it satisfy the principal-reasons standard under Reg B §1002.9 and Comment 9(b)(2)-3 of the Official Staff Commentary.
- For a GenAI model with NPI/PHI in the prompt context, what is the firm's leak-detection cadence and what is the off-switch criterion.

### 6. Dependencies add privacy functions

The plan's dependencies list adds:

- Privacy office review of the data classification and the PIA.
- BAA / DPA evidence for any vendor handling NPI/PHI.
- Customer-rights workflow integration evidence (for jurisdictions with right-to-know / right-to-delete obligations).
- For EU footprint, GDPR Article 22 right-to-explanation evidence and (where applicable) Article 27 FRIA.

## Privacy-specific output template additions

- `data_review.privacy_classification` — per-data-source classification (NPI, PHI, PCI, customer-supplied prompts, public, confidential).
- `data_review.prompt_surface` — for GenAI, retention, vendor-side training posture, BAA / DPA reference, redaction posture.
- `data_review.lawful_basis_for_processing` — where a state or international privacy law requires it.
- `outcomes_analysis[]` — PII/NPI memorisation, training-data extraction, cross-customer retrieval, PHI-leak, prompt-template extraction tests.
- `robustness_testing[]` — membership-inference, indirect-prompt-injection-for-NPI/PHI-extraction, differential-privacy verification where asserted.
- `monitoring[]` — PII/NPI leak detection, cross-customer retrieval audit, customer-rights-request processing turnaround, privacy-incident detection.
- `effective_challenge_questions[]` — privacy-tagged (PIA conformance, vendor BAA/DPA evidence, GDPR Article 22 right-to-explanation, ECOA adverse-action method, NPI/PHI leak-detection cadence).
- `dependencies[]` — privacy office review, BAA/DPA evidence, customer-rights workflow integration, FRIA evidence where applicable.

## Common pitfalls in privacy-flagged validation plans

- Classifying foundation-model training data without addressing in-context customer prompts. The prompt surface is where customer NPI/PHI most often enters a GenAI use case; vendor system-card statements about training-data privacy do not extend to the firm's deployed prompt surface.
- Treating a vendor's data-processing posture as covering the firm; the firm's BAA (HIPAA) or DPA (GDPR / state privacy) is the firm's evidence, not the vendor's marketing.
- Assuming a HIPAA business-associate agreement with the LLM vendor exists when it does not; PHI flowing into a non-BAA-covered model is a recordable issue, not a plan-body assertion of HIPAA coverage.
- Defaulting to "this is anonymous" without actually anonymising prompts in the leak test. PII redaction is a control with evidence; the claim without the control is a plan-recordable issue.
- Omitting the customer-rights workflow validation for an automated-decisioning use case; right to know, right to delete, and (where applicable) right to opt out of automated decisioning are workflow obligations that the plan's monitoring scope should test.
- Carrying the PIA conclusion into the plan as if it were the validator's privacy-program output. The plan points to the PIA in source trace; the PIA itself is the privacy-program artifact.
- Setting the cross-customer retrieval test as a one-time pre-prod test only; for RAG architectures, this is an ongoing-monitoring item, not just a pre-prod gate item.
