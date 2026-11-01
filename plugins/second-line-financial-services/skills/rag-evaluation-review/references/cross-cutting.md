# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Conduct cross-cutting overlay for rag-evaluation-review

When the scope record flags `conduct` for a RAG evaluation review, this overlay adds the fairness-of-retrieval framing and the customer-facing accuracy framing. The conduct overlay loads where the use case has a population dimension (customer segment, geography, line of business) or where outputs flow into customer-facing communications.

Loaded by: `rag-evaluation-review/SKILL.md` when `scope.cross_cutting_set` includes `conduct`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- CFPB UDAAP framework (Dodd-Frank Act §1031 / §1036; CFPB Consumer Financial Protection Circulars on UDAAP) for consumer-facing communications generated or assisted by AI.
- Fair-lending framework: ECOA (15 USC §1691) and Regulation B (12 CFR Part 1002), Fair Housing Act (42 USC §3601 et seq.), and CFPB Circulars on AI in credit decisioning where the use case touches credit decisions or credit-adjacent decisions.
- SEC Marketing Rule (17 CFR §275.206(4)-1) and SEC fiduciary-standard / Reg BI framings for adviser-facing or broker-facing client-facing content.
- State unfair claims-settlement-practices acts and state insurance-fairness frameworks (e.g., Colorado Reg 10-1-1, Connecticut Insurance Department guidance) for retrieval-driven decision-support use cases in insurance.
- FINRA suitability framework for any sales-practice-adjacent use case in BD entities.
- General consumer protection: state UDAP regimes per residency.

#### What changes when conduct is flagged

##### Retrieval-quality and grounding evaluation gain a fairness segmentation

Where the use case has a population dimension, the segmentation requirement on retrieval-quality and grounding-evaluation metrics extends to fairness segmentation:

- Customer segment (mass-market, mass-affluent, private-banking; consumer, small-business, commercial; etc.) where the segmentation is relevant to the use case.
- Geography (state, urban/rural, where regional content access or regional product availability matters).
- Line of business (auto, life, disability, P&C in insurance; retail, commercial, treasury in banking).
- Protected-class proxies for fair-lending-adjacent use cases, with the proxy basis documented and the analysis approach aligned to the firm's fair-lending programme methodology.

A single global metric number on a customer-facing or decision-support use case is incomplete without the fairness segmentation.

##### Customer-facing accuracy as a load-bearing failure-mode framing

The conduct framing for grounding-evaluation failure modes:

- Hallucination on a customer-facing communication is a UDAAP issue (deception by inaccurate statement) and a complaint-driver.
- Stale-content answer on a fee, rate, term, or product feature is a UDAAP issue (the customer is told something inconsistent with the current fact).
- Citation precision matters for any output where the customer might rely on the cited document; a wrong citation in a customer-facing communication is a UDAAP framing as well as a citation-quality framing.
- Refusal failure on out-of-scope (e.g., the assistant gives investment advice when the use case is operational support) creates suitability and Reg BI exposure for BD-affiliated use cases.

The grounding-evaluation thresholds for customer-facing or decision-support use cases are tighter than for analyst-facing or back-office use cases. The conduct overlay surfaces this in the recommended-actions section.

##### Mitigations expand to include the conduct control set

Beyond the standard set:

- UDAAP-relevant output controls on customer-facing communications (deception, unfairness, abuse).
- Marketing Rule output controls for adviser-facing entities; books-and-records preservation per Rule 17a-4 / 204-2.
- Fair-lending output controls for credit-adjacent or credit-decisioning use cases; the fair-lending function signs off on the control specification.
- Suitability and Reg BI output controls for sales-practice-adjacent BD use cases.
- For insurance decision-support, state insurance-fairness output controls aligned to the AIS Program testing-and-validation expectations.

##### Monitoring adds the conduct-tagged signal set

The baseline conduct signals to add when the overlay is flagged:

- Customer-complaint-rate and complaint-code drift as a downstream-acceptance signal; complaint codes mapping to RAG-output issues route to consumer compliance and to the AI risk committee.
- Fairness-segmented metric monitoring at a defined cadence (continuous for high-volume use cases, monthly or quarterly for low-volume), with drift alerting per segment.
- For decision-support use cases, disposition-rate fairness monitoring across protected-class proxies with annual reassessment at minimum.
- For insurance decision-support, alignment to the NAIC AIS Program monitoring elements per the loaded sector overlay.

##### Reviewer-coordination considerations

- Consumer compliance is a named co-reviewer for any customer-facing use case.
- The fair-lending function is a named co-reviewer for any credit-adjacent or credit-decisioning use case.
- The CCO is a named co-acceptor for residual risk on UDAAP, Marketing Rule, and Reg BI framings.
- The chief actuary or the head of underwriting is a named co-reviewer for insurance decision-support use cases per the sector overlay.

#### Recommended actions add the conduct-specific items

The standard conduct-tagged recommended-actions items the overlay surfaces:

- Confirm fairness-segmented evaluation is in place at the appropriate cadence.
- Confirm UDAAP-relevant output controls are documented and exercised for customer-facing communications.
- Confirm complaint-code mapping is in place to route RAG-output-related complaints to the AI risk committee.
- For credit-adjacent use cases, confirm the fair-lending function signs off on the residual-risk acceptance.
- For insurance decision-support, confirm the NAIC AIS Program documentation is current.

#### Conduct-specific output additions

In the structured object (`schemas/rag-evaluation-review.schema.json`):

- `retrieval_quality[]` and `grounding_evaluation[]` entries with `segmentation` populated to include the fairness segmentation where the use case has a population dimension.
- `mitigations[]` entries with conduct-tagged owner (consumer compliance, fair-lending function, CCO).
- `monitoring[]` entries with conduct-tagged escalation path.
- `cross_cutting_overlay_notes.conduct` carries the conduct-specific fields: fairness-segmentation scope, UDAAP-relevant output-control scope, complaint-code routing, named co-reviewers per use-case framing.
- `recommended_actions[]` entries with conduct-tagged owner role.

#### Common pitfalls in conduct-flagged RAG reviews

- Reporting a single faithfulness number on a customer-facing use case without the population dimension. A review on the global number can hide systematic failure on a customer segment; the fairness segmentation surfaces it.
- Treating UDAAP framing as compliance background reading rather than as a load-bearing seam on the evaluation. UDAAP exposure is the load-bearing risk on customer-facing AI output; the residual-risk section carries it explicitly.
- Omitting the fair-lending function from the reviewer attestation when the use case touches credit decisions. Fair-lending sign-off is a co-acceptance, not a referral.
- Treating customer-complaint signals as customer-service operational data rather than as AI-quality leading indicators. Complaint-code mapping to RAG-output issues is the routing question.
- For insurance decision-support, asserting AIS Program documentation is current when the corpus or the metric set has changed. The NAIC AIS Program testing-and-validation element is current point-in-time and changes invalidate it.
- Setting grounding-evaluation thresholds at back-office levels for customer-facing use cases. Customer-facing thresholds are tighter; the recommended-action item names the threshold change.

## cyber

### Cyber cross-cutting overlay for rag-evaluation-review

When the scope record flags `cyber` for a RAG evaluation review, this overlay carries the corpus-access-control framing and the indirect-injection adjacency to `prompt-injection-risk`. The cyber overlay is not the primary lens for a RAG evaluation review (the primary lenses are corpus governance and grounding evaluation); it sits alongside the privacy overlay as a co-lens for the corpus access surface.

Loaded by: `rag-evaluation-review/SKILL.md` when `scope.cross_cutting_set` includes `cyber`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- NYDFS 23 NYCRR Part 500, especially §500.9 (risk assessment), §500.11 (third-party service-provider security), §500.16 (incident-response and BCDR plan), §500.17(a) (notice to superintendent), and the October 2024 AI Industry Letter for AI-deployment cyber risks including model-supply-chain considerations.
- FFIEC IT Examination Handbook, Information Security and AIO booklets, applied to corpus storage, retrieval-side access controls, and audit logging.
- NIST SP 800-53 Rev. 5 control families (AC, AU, IR, SI, SR) as the underlying control catalogue for cyber-side mitigations.
- The 36-hour banking computer-security incident notification rule (12 CFR Part 53 / Part 225 / Part 304) for bank-affiliated entities where a corpus-compromise event impairs operations.
- SEC cyber disclosure rules (8-K Item 1.05 and Reg S-K Item 106) for public registrants where corpus compromise contributes to a material cyber incident.
- Pointer to `prompt-injection-risk/references/cross-cutting.md#cyber` for the focused cyber overlay on the prompt-surface review.

#### What changes when cyber is flagged

##### Corpus-fitness gains corpus-access-control tagging

Each corpus row in the corpus-fitness section is tagged with the access-control posture: who can write to the corpus, who can update documents, who can change metadata, who can change retrieval-side scoping rules. The cyber question on a RAG corpus is structural integrity: a corpus a malicious or compromised insider can poison is a corpus the grounding evaluation cannot validate against.

The control-family mapping (AC for access, AU for audit, SI for integrity, SR for supply chain) ties the corpus-fitness rows to the firm's existing cyber control framework.

##### Retrieval-side authentication and authorisation as load-bearing controls

The mitigation set expects retrieval-side authentication (the calling user or service is authenticated) and authorisation (the calling identity has rights to retrieve from the corpora the query touches). For systems where retrieval is mediated by a service account on behalf of an end user, the impersonation chain is documented and the principal-of-least-privilege framing applies.

Audit logging covers every retrieval with the calling identity, the corpus, the documents returned, and the retrieval-side scope filter applied. Retention aligns to the firm's cyber log-retention policy and to NYDFS Part 500 §500.6 audit-trail expectations.

##### Indirect-injection adjacency through corpus content

This is the cyber overlay's load-bearing connection to `prompt-injection-risk`. Corpus content can carry adversarial instructions placed by an external counterparty (in customer correspondence, third-party intelligence feeds, vendor-supplied content) or by an insider (in policy documents, alert narratives, prior summaries). The grounding-evaluation work in this skill catalogues the failure mode (off-corpus answer, citation fabrication driven by injected content); the prompt-injection threat-surface review (in `prompt-injection-risk`) is the focused review.

The two skills work side-by-side for any RAG-using GenAI system. This skill records the corpus-content-injection failure mode and points to `prompt-injection-risk` for the threat-surface and tested-attack-class detail. The recommended-actions section confirms a `prompt-injection-risk` review is in flight or on file.

##### Mitigations expand to include the cyber control set on the corpus surface

Beyond the standard set:

- Retrieval-side authentication and authorisation per the firm's identity and access management.
- Audit logging on retrieval, retained per the cyber log-retention policy.
- Corpus-write controls: who can ingest, who can update, who can delete; documented and enforced.
- Content-integrity controls on dynamic corpora: hash drift detection, last-modified tracking, source-of-truth reconciliation for vendor-supplied corpora.
- Vendor and supply-chain controls on the foundation-model provider, the embedding-model provider, and the retrieval-platform provider, captured in the third-party risk register.
- Network-layer controls on retrieval-platform and serving-environment connectivity.

##### Monitoring adds the cyber-tagged signal set

The baseline cyber signals to add when the overlay is flagged:

- Authentication and authorisation anomalies on the retrieval-platform serving endpoint.
- Retrieval-source distribution audit; sudden drift in source distribution may indicate either content-pipeline issue or adversarial activity.
- Content-hash drift on dynamic corpora; off-cycle content changes are an investigation trigger.
- Vendor change-of-version signals for the foundation model, the embedding model, and the retrieval-platform; an unannounced version swap is a cyber signal.
- Cross-scope retrieval anomaly (the retrieval scope filter returning content outside the calling identity's authorised scope) as a privacy-and-cyber co-signal.

##### Incident response names the corpus-compromise classes

For a RAG evaluation review the incident-response framing centres on corpus integrity and corpus access:

- Suspected corpus poisoning (anomaly in citation precision plus retrieval-source-audit signal): cyber-and-AI joint runbook; vendor management notified for vendor-supplied corpora; corpus version freeze pending investigation.
- Confirmed unauthorised retrieval (cross-scope or beyond-authorised-scope): privacy-and-cyber joint runbook; notification trigger evaluation per the privacy overlay and the loaded sector overlay; off-switch criterion: pause the affected scope of the retrieval until remediation.
- Confirmed corpus tampering (insider or third-party compromise of corpus content): cyber incident runbook; vendor management notified for vendor-supplied corpora; corpus version freeze pending forensic; pointer to `prompt-injection-risk` for the tested-attack-class re-validation.

The off-switch criterion is the operational decision the runbook turns on. A confirmed corpus-compromise event with no defined off-switch is a finding.

#### Recommended actions add the cyber-specific items

The standard cyber-tagged recommended-actions items the overlay surfaces:

- Confirm a `prompt-injection-risk` review is on file or in flight for the same use case.
- Confirm retrieval-side authentication and authorisation are documented, exercised, and audited.
- Confirm vendor change-of-version notice and audit rights for the foundation-model, embedding-model, and retrieval-platform providers, captured in the third-party risk register.
- IR drill on corpus-compromise scenarios at a defined cadence (annual at minimum; quarterly for tier-1 use cases).

#### Cyber-specific output additions

In the structured object (`schemas/rag-evaluation-review.schema.json`):

- `corpus_fitness[]` entries with `access_controls` populated and the cyber-tagging convention applied.
- `mitigations[]` entries with cyber-tagged owner (CISO function or sub-function).
- `monitoring[]` entries with cyber-tagged escalation path.
- `cross_cutting_overlay_notes.cyber` carries the cyber-specific fields: control-family tagging on corpus-fitness entries, named cyber-side mitigations, cyber-tagged monitoring signals, and pointer to the `prompt-injection-risk` review.
- `recommended_actions[]` entries with cyber-tagged owner role.

#### Common pitfalls in cyber-flagged RAG reviews

- Treating retrieval-side authentication as the application's responsibility and asserting it is "in place" without confirming the impersonation chain. The principal-of-least-privilege framing on service-account-mediated retrieval is structural and is a finding when it is not documented.
- Treating audit logging as an engineering concern rather than a cyber-control concern. The retention cadence and the queryability by the cyber team are the decision points; absent these, the logs are operational telemetry not control evidence.
- Omitting the indirect-injection adjacency. This skill catalogues the grounding-side failure mode (off-corpus answer, citation fabrication driven by injected content); the focused threat-surface review lives in `prompt-injection-risk`. Not naming the adjacency leaves a coverage gap.
- Treating vendor-supplied corpora (regulatory-text databases, third-party intelligence feeds) as integrity-attested without a content-integrity control. Vendor self-attestation is not the same as firm-side integrity monitoring.
- Reporting an unannounced foundation-model version swap as a model-risk event without the cyber framing. Vendor change-of-version is also a cyber signal; both framings need to be in the review.

## privacy

### Privacy cross-cutting overlay for rag-evaluation-review

When the scope record flags `privacy` for a RAG evaluation review, this overlay sits as the primary cross-cutting lens. Most regulated-FS RAG systems retrieve over corpora containing NPI, PHI, MNPI, or other regulated personal data; the privacy overlay is the default cross-cutting overlay for these cases, the way cyber is the default for prompt-injection reviews.

Loaded by: `rag-evaluation-review/SKILL.md` when `scope.cross_cutting_set` includes `privacy`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- Gramm-Leach-Bliley Act and the Safeguards Rule (16 CFR Part 314) for FTC-scope financial institutions; the May 2024 notification provisions in 16 CFR §314.5(d) for events involving 500 or more consumers' unencrypted information.
- HIPAA Privacy Rule (45 CFR Part 164 Subpart E) and HIPAA Security Rule (45 CFR Part 164 Subpart C) for PHI; minimum-necessary at retrieval is the load-bearing control.
- State privacy laws and breach-notification regimes; the firm's privacy programme normally maintains a state-by-state matrix that the review references rather than restates.
- EU GDPR (Regulation (EU) 2016/679) Articles 5 (principles including purpose limitation, data minimisation, storage limitation), 25 (privacy by design), 32 (security of processing), 33-34 (notification) for EU-touch entities.
- California Consumer Privacy Act / CPRA for California-resident data.
- NYDFS 23 NYCRR Part 500 §500.11 (third-party service-provider security) and the October 2024 AI Industry Letter where corpus access controls are part of the cyber overlay seam.

#### What changes when privacy is flagged

##### Corpus-fitness gains a privacy-tagging convention

Each corpus row in the corpus-fitness section is tagged with the relevant data-protection regime and the data-minimisation posture. Sensitivity is one of the schema enums (public, internal, confidential, regulated-NPI, regulated-PHI, MNPI, privileged); the privacy overlay adds the regime-specific tagging:

- GLBA-NPI: customer financial information in scope of the Safeguards Rule.
- HIPAA-PHI: health information in HIPAA scope.
- State-private: residency-specific privacy law scope (CCPA, etc.).
- GDPR-personal-data: EU-scope personal data with controller-processor framing.

Per-document provenance tagging is the corpus-fitness spine; for privacy purposes, the per-document data-category tagging is what supports the minimum-necessary determination at retrieval.

##### Retrieval-side minimisation and purpose limitation

Per-customer, per-claim, per-policy, per-account, per-dispute scoping at the retriever is the minimum-necessary mechanism in operation. The review confirms the scoping is enforced at the retrieval layer (not the prompt layer) and confirms the purpose-limitation posture: the corpus is indexed for the use case's stated purpose and is not repurposable without a separate review.

Retention cadence on retrieval logs and on cached retrieval outputs aligns to the firm's record-retention schedule and to the relevant data-protection regime. Where the use case generates outputs that themselves contain personal data, the output-retention posture is part of the privacy overlay's review.

##### Cross-scope leakage as a privacy event class

The cross-scope leakage failure mode (cross-customer, cross-claim, cross-policy, cross-account) is the canonical privacy-event class for RAG systems. The overlay expects:

- A rule-based detection for cross-scope ID surfaces in retrieval output and in summary output.
- Continuous logging plus weekly SME spot-check on the detection.
- Any confirmed event triggers incident response and a regulator-notification trigger evaluation per the loaded sector overlay and the cyber overlay.

A confirmed cross-scope leakage event is a privacy incident, not a model issue. Treating it as a hallucination misses the framing.

##### Mitigations expand to include the privacy control set

Beyond the standard set:

- Retrieval-layer access enforcement aligned to the firm's identity and access management.
- Output-side de-identification where the use case generates outputs that flow downstream beyond the operator (e.g., outputs feeding analytics, training data for downstream models, exports to vendors); the de-identification approach is documented and the residual re-identification risk is named.
- Input-side de-identification or pseudonymisation where the use case retrieves over an over-broad corpus and the prompt-side data-category exposure exceeds the minimum-necessary posture.
- Audit logging on every retrieval, with retrieval-source and per-document access recorded, retained per the record-retention schedule, and queryable by the privacy officer.
- Vendor and supply-chain privacy controls where the foundation-model provider, the embedding-model provider, or the retrieval-platform provider is a third party; data-processing-agreement coverage is confirmed in the third-party risk register.

##### Monitoring adds the privacy-tagged signal set

The baseline privacy signals to add when the overlay is flagged:

- Cross-scope leakage detection (rule-based plus SME spot-check).
- Retrieval-source distribution audit per data category; sudden drift in retrieval from a sensitive-category corpus is a leading indicator of access-control issue or query-distribution shift.
- Output-content sampling for personal-data leakage in summary or generated content (regex plus LLM-judge for unstructured leakage).
- For systems with persistent memory or long-context caching, memory-content sampling for personal-data persistence beyond the purpose.
- For HIPAA-scope corpora, audit-log review on minimum-necessary compliance at a defined cadence.

##### Incident response names the privacy-notification triggers

The `incident_response[]` entries (where this skill carries them through to the prompt-injection-risk review for cyber-prompt-injection events) and the `recommended_actions[]` entries name the privacy-notification triggers per the loaded sector overlay:

- GLBA Safeguards Rule notification (16 CFR §314.5(d)): FTC notification of unauthorised acquisition of unencrypted customer information of 500 or more consumers.
- HIPAA Breach Notification Rule (45 CFR §164.400 et seq.) for PHI breaches.
- State breach laws per the firm's state-by-state matrix.
- GDPR Article 33 (notification to supervisory authority within 72 hours) and Article 34 (notification to affected data subjects) for EU-touch.
- Sector-specific notifications carried by the loaded sector overlay.

#### Recommended actions add the privacy-specific items

The standard privacy-tagged recommended-actions items the overlay surfaces:

- Confirm minimum-necessary determination at the retrieval layer for each data category indexed; document the determination basis.
- Confirm the data-protection-impact-assessment (DPIA) or the firm-equivalent privacy-impact-assessment is on file and is current as of the review date.
- Confirm the retention schedule on retrieval logs and on output caches matches the firm's record-retention schedule and the relevant regime.
- For systems generating outputs containing personal data, confirm the de-identification approach is documented and the residual re-identification risk is named in residual-risk.
- Confirm the third-party risk register entries cover the foundation-model provider, the embedding-model provider, and the retrieval-platform provider with current data-processing-agreement coverage.

#### Privacy-specific output additions

In the structured object (`schemas/rag-evaluation-review.schema.json`):

- `corpus_fitness[]` entries with sensitivity and the privacy-tagging convention applied.
- `mitigations[]` entries with privacy-tagged owner (privacy officer or privacy sub-function).
- `monitoring[]` entries with privacy-tagged escalation path.
- `cross_cutting_overlay_notes.privacy` carries the privacy-specific fields: minimum-necessary determination per corpus, DPIA status, retention posture per output category, named regulator-notification triggers per applicable regime.
- `recommended_actions[]` entries with privacy-tagged owner role.

#### Common pitfalls in privacy-flagged RAG reviews

- Treating sensitivity as a single label on the corpus (e.g., "confidential") when the corpus contains documents of mixed regimes (NPI in some, PHI in others, MNPI in still others). Per-document data-category tagging is the spine.
- Asserting minimum-necessary at the prompt layer. Retrieval-layer enforcement is the load-bearing control.
- Omitting the privacy officer from the reviewer attestation when the corpus contains regulated personal data. The privacy officer co-signs the residual-risk acceptance.
- Treating cross-scope leakage as a hallucination. It is a privacy incident; the framing changes the response posture and the notification-trigger evaluation.
- Not refreshing the DPIA when the use case scope expands (new corpus added, new query types supported, new downstream consumer of outputs). DPIA is point-in-time; scope changes invalidate it.
- Treating retention on retrieval logs and output caches as an engineering question. Retention is a privacy and records-retention question; the privacy officer and records-retention owner are the decision-makers.
