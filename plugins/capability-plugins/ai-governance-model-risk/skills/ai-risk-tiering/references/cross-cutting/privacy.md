# Privacy cross-cutting overlay for ai-risk-tiering

When the engagement-scope record flags `privacy` for the use case, this overlay supplies the privacy-specific factors that weight up the tier and the named triggers that force a re-tier when the privacy posture changes. The full privacy-impact assessment is its own artifact under the firm's privacy program; the tiering record names the privacy reach that drives the tier and routes downstream artifacts to address it.

Loaded by: `ai-risk-tiering/SKILL.md` when `engagement_scope.cross_cutting_set` includes `privacy`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- GLBA Safeguards Rule (16 CFR Part 314) for non-public personal information (NPI) handled by financial institutions.
- HIPAA Privacy and Security Rules where protected health information is in scope (life and health insurance, healthcare-adjacent fintechs, claims AI).
- CCPA / CPRA (California) and the rolling roster of state privacy laws (VCDPA, CTDPA, others) covering automated decisioning, consumer rights, and sensitive-personal-information categories.
- GDPR Article 22 (decisions based solely on automated processing, including profiling) where EU customers are in the operating footprint.
- EU AI Act Article 27 (fundamental rights impact assessment) where the use case is a high-risk AI system used by an in-scope deployer.
- ECOA / Reg B right-to-explanation in adverse-action notices for credit-decisioning models, sitting at the privacy/fair-lending intersection.

## Privacy-specific scoring guidance

The capability rubric scores `data_sensitivity` once. The overlay tells the rubric what counts as high, medium, low for this factor when privacy is flagged:

- **High** — any of: regulated NPI under GLBA in inputs, training data, or retrieval corpus; PHI under HIPAA at any point in the data flow; biometric data; children's data; customer-supplied prompt content that can carry NPI/PHI; cross-border transfer to a jurisdiction without an adequacy decision under GDPR.
- **Medium** — any of: confidential business data with privacy-relevant inferences (e.g., inferred customer segment); pseudonymised personal data; vendor-hosted model where the BAA or DPA posture is partial.
- **Low** — public data, fully anonymised data, or firm-internal non-personal operational data.

The privacy-driven data-sensitivity score is dominant where the use case is automated decisioning under GDPR Article 22 or where adverse-action notices under ECOA / Reg B are in scope; otherwise it is contributing.

## Privacy-specific re-tiering triggers

Add to the re-tiering trigger block when `cross_cutting_set` includes `privacy`:

- Expansion of data sources to include a new sensitivity category (NPI, PHI, biometric, children's data). Owner: privacy office with AI governance. Detection: change-management notice.
- Change in vendor BAA (HIPAA) or DPA (GDPR / state privacy) posture, including loss of BAA coverage on a vendor that handles PHI. Owner: vendor management with privacy office. Detection: vendor contract management plus change-management notice.
- Footprint change into a state with a stricter automated-decisioning regime, or into the EU/UK/Switzerland for an EU/UK customer base. Owner: regulatory change function with privacy office. Detection: regulatory horizon scan and business expansion notice.
- Change in the privacy notice covering the use case, or material change in customer-rights workflow. Owner: privacy office. Detection: privacy notice version control.
- For credit-decisioning under ECOA / Reg B, change in the adverse-action notice generation method or new CFPB Circular on algorithmic credit decisioning. Owner: consumer compliance with model owner. Detection: regulatory horizon scan plus change-management notice.

## Common pitfalls in privacy-flagged tiering

- Scoring data sensitivity from the training data only, missing the prompt surface. For GenAI customer-facing use cases, the prompt is where customer NPI/PHI most often enters; the data-sensitivity factor reflects the prompt surface as well as the corpus.
- Assuming a vendor BAA exists when it does not. PHI flowing into a non-BAA-covered model vendor is a tier-up factor, not a low-confidence assumption.
- Treating fully-automated decisioning under GDPR Article 22 as a documentation question. Article 22 reaches the legal posture (right to obtain meaningful information about the logic, right to obtain human intervention) and elevates the tier on its own.
- Underweighting state-by-state automated-decisioning expectations. CPRA and a growing number of state laws now address profiling and significant decisions; the privacy score reflects the strictest applicable state in the operating footprint, not the federal floor.
- Missing the cross-border privacy posture for a vendor-hosted foundation model. Vendor inference infrastructure may sit in a jurisdiction the customer data was not approved for; the data-residency posture is a tier-up factor where adequacy decisions or explicit consent are missing.
