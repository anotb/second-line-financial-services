# Privacy cross-cutting overlay for rag-evaluation-review

When the engagement-scope record flags `privacy` for a RAG evaluation review, this overlay sits as the primary cross-cutting lens. Most regulated-FS RAG systems retrieve over corpora containing NPI, PHI, MNPI, or other regulated personal data; the privacy overlay is the default cross-cutting overlay for these cases, the way cyber is the default for prompt-injection reviews.

Loaded by: `rag-evaluation-review/SKILL.md` when `engagement_scope.cross_cutting_set` includes `privacy`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- Gramm-Leach-Bliley Act and the Safeguards Rule (16 CFR Part 314) for FTC-scope financial institutions; the May 2024 notification provisions in 16 CFR §314.5(d) for events involving 500 or more consumers' unencrypted information.
- HIPAA Privacy Rule (45 CFR Part 164 Subpart E) and HIPAA Security Rule (45 CFR Part 164 Subpart C) for PHI; minimum-necessary at retrieval is the load-bearing control.
- State privacy laws and breach-notification regimes; the firm's privacy programme normally maintains a state-by-state matrix that the review references rather than restates.
- EU GDPR (Regulation (EU) 2016/679) Articles 5 (principles including purpose limitation, data minimisation, storage limitation), 25 (privacy by design), 32 (security of processing), 33-34 (notification) for EU-touch entities.
- California Consumer Privacy Act / CPRA for California-resident data.
- NYDFS 23 NYCRR Part 500 §500.11 (third-party service-provider security) and the October 2024 AI Industry Letter where corpus access controls are part of the cyber overlay seam.

## What changes when privacy is flagged

### Corpus-fitness gains a privacy-tagging convention

Each corpus row in the corpus-fitness section is tagged with the relevant data-protection regime and the data-minimisation posture. Sensitivity is one of the schema enums (public, internal, confidential, regulated-NPI, regulated-PHI, MNPI, privileged); the privacy overlay adds the regime-specific tagging:

- GLBA-NPI: customer financial information in scope of the Safeguards Rule.
- HIPAA-PHI: health information in HIPAA scope.
- State-private: residency-specific privacy law scope (CCPA, etc.).
- GDPR-personal-data: EU-scope personal data with controller-processor framing.

Per-document provenance tagging is the corpus-fitness spine; for privacy purposes, the per-document data-category tagging is what supports the minimum-necessary determination at retrieval.

### Retrieval-side minimisation and purpose limitation

Per-customer, per-claim, per-policy, per-account, per-dispute scoping at the retriever is the minimum-necessary mechanism in operation. The review confirms the scoping is enforced at the retrieval layer (not the prompt layer) and confirms the purpose-limitation posture: the corpus is indexed for the use case's stated purpose and is not repurposable without a separate review.

Retention cadence on retrieval logs and on cached retrieval outputs aligns to the firm's record-retention schedule and to the relevant data-protection regime. Where the use case generates outputs that themselves contain personal data, the output-retention posture is part of the privacy overlay's review.

### Cross-scope leakage as a privacy event class

The cross-scope leakage failure mode (cross-customer, cross-claim, cross-policy, cross-account) is the canonical privacy-event class for RAG systems. The overlay expects:

- A rule-based detection for cross-scope ID surfaces in retrieval output and in summary output.
- Continuous logging plus weekly SME spot-check on the detection.
- Any confirmed event triggers incident response and a regulator-notification trigger evaluation per the loaded sector overlay and the cyber overlay.

A confirmed cross-scope leakage event is a privacy incident, not a model issue. Treating it as a hallucination misses the framing.

### Mitigations expand to include the privacy control set

Beyond the standard set:

- Retrieval-layer access enforcement aligned to the firm's identity and access management.
- Output-side de-identification where the use case generates outputs that flow downstream beyond the operator (e.g., outputs feeding analytics, training data for downstream models, exports to vendors); the de-identification approach is documented and the residual re-identification risk is named.
- Input-side de-identification or pseudonymisation where the use case retrieves over an over-broad corpus and the prompt-side data-category exposure exceeds the minimum-necessary posture.
- Audit logging on every retrieval, with retrieval-source and per-document access recorded, retained per the record-retention schedule, and queryable by the privacy officer.
- Vendor and supply-chain privacy controls where the foundation-model provider, the embedding-model provider, or the retrieval-platform provider is a third party; data-processing-agreement coverage is confirmed in the third-party risk register.

### Monitoring adds the privacy-tagged signal set

The baseline privacy signals to add when the overlay is flagged:

- Cross-scope leakage detection (rule-based plus SME spot-check).
- Retrieval-source distribution audit per data category; sudden drift in retrieval from a sensitive-category corpus is a leading indicator of access-control issue or query-distribution shift.
- Output-content sampling for personal-data leakage in summary or generated content (regex plus LLM-judge for unstructured leakage).
- For systems with persistent memory or long-context caching, memory-content sampling for personal-data persistence beyond the purpose.
- For HIPAA-scope corpora, audit-log review on minimum-necessary compliance at a defined cadence.

### Incident response names the privacy-notification triggers

The `incident_response[]` entries (where this skill carries them through to the prompt-injection-risk review for cyber-prompt-injection events) and the `recommended_actions[]` entries name the privacy-notification triggers per the loaded sector overlay:

- GLBA Safeguards Rule notification (16 CFR §314.5(d)): FTC notification of unauthorised acquisition of unencrypted customer information of 500 or more consumers.
- HIPAA Breach Notification Rule (45 CFR §164.400 et seq.) for PHI breaches.
- State breach laws per the firm's state-by-state matrix.
- GDPR Article 33 (notification to supervisory authority within 72 hours) and Article 34 (notification to affected data subjects) for EU-touch.
- Sector-specific notifications carried by the loaded sector overlay.

## Recommended actions add the privacy-specific items

The standard privacy-tagged recommended-actions items the overlay surfaces:

- Confirm minimum-necessary determination at the retrieval layer for each data category indexed; document the determination basis.
- Confirm the data-protection-impact-assessment (DPIA) or the firm-equivalent privacy-impact-assessment is on file and is current as of the review date.
- Confirm the retention schedule on retrieval logs and on output caches matches the firm's record-retention schedule and the relevant regime.
- For systems generating outputs containing personal data, confirm the de-identification approach is documented and the residual re-identification risk is named in residual-risk.
- Confirm the third-party risk register entries cover the foundation-model provider, the embedding-model provider, and the retrieval-platform provider with current data-processing-agreement coverage.

## Privacy-specific output additions

In the structured object (`schemas/rag-evaluation-review.schema.json`):

- `corpus_fitness[]` entries with sensitivity and the privacy-tagging convention applied.
- `mitigations[]` entries with privacy-tagged owner (privacy officer or privacy sub-function).
- `monitoring[]` entries with privacy-tagged escalation path.
- `cross_cutting_overlay_notes.privacy` carries the privacy-specific fields: minimum-necessary determination per corpus, DPIA status, retention posture per output category, named regulator-notification triggers per applicable regime.
- `recommended_actions[]` entries with privacy-tagged owner role.

## Common pitfalls in privacy-flagged RAG reviews

- Treating sensitivity as a single label on the corpus (e.g., "confidential") when the corpus contains documents of mixed regimes (NPI in some, PHI in others, MNPI in still others). Per-document data-category tagging is the spine.
- Asserting minimum-necessary at the prompt layer. Retrieval-layer enforcement is the load-bearing control.
- Omitting the privacy officer from the reviewer attestation when the corpus contains regulated personal data. The privacy officer co-signs the residual-risk acceptance.
- Treating cross-scope leakage as a hallucination. It is a privacy incident; the framing changes the response posture and the notification-trigger evaluation.
- Not refreshing the DPIA when the use case scope expands (new corpus added, new query types supported, new downstream consumer of outputs). DPIA is point-in-time; scope changes invalidate it.
- Treating retention on retrieval logs and output caches as an engineering question. Retention is a privacy and records-retention question; the privacy officer and records-retention owner are the decision-makers.
