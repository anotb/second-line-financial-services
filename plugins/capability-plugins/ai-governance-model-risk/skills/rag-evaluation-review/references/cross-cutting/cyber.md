# Cyber cross-cutting overlay for rag-evaluation-review

When the engagement-scope record flags `cyber` for a RAG evaluation review, this overlay carries the corpus-access-control framing and the indirect-injection adjacency to `prompt-injection-risk`. The cyber overlay is not the primary lens for a RAG evaluation review (the primary lenses are corpus governance and grounding evaluation); it sits alongside the privacy overlay as a co-lens for the corpus access surface.

Loaded by: `rag-evaluation-review/SKILL.md` when `engagement_scope.cross_cutting_set` includes `cyber`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- NYDFS 23 NYCRR Part 500, especially §500.9 (risk assessment), §500.11 (third-party service-provider security), §500.16 (incident-response and BCDR plan), §500.17(a) (notice to superintendent), and the October 2024 AI Industry Letter for AI-deployment cyber risks including model-supply-chain considerations.
- FFIEC IT Examination Handbook, Information Security and AIO booklets, applied to corpus storage, retrieval-side access controls, and audit logging.
- NIST SP 800-53 Rev. 5 control families (AC, AU, IR, SI, SR) as the underlying control catalogue for cyber-side mitigations.
- The 36-hour banking computer-security incident notification rule (12 CFR Part 53 / Part 225 / Part 304) for bank-affiliated entities where a corpus-compromise event impairs operations.
- SEC cyber disclosure rules (8-K Item 1.05 and Reg S-K Item 106) for public registrants where corpus compromise contributes to a material cyber incident.
- Pointer to `prompt-injection-risk/references/cross-cutting/cyber.md` for the focused cyber overlay on the prompt-surface review.

## What changes when cyber is flagged

### Corpus-fitness gains corpus-access-control tagging

Each corpus row in the corpus-fitness section is tagged with the access-control posture: who can write to the corpus, who can update documents, who can change metadata, who can change retrieval-side scoping rules. The cyber question on a RAG corpus is structural integrity: a corpus a malicious or compromised insider can poison is a corpus the grounding evaluation cannot validate against.

The control-family mapping (AC for access, AU for audit, SI for integrity, SR for supply chain) ties the corpus-fitness rows to the firm's existing cyber control framework.

### Retrieval-side authentication and authorisation as load-bearing controls

The mitigation set expects retrieval-side authentication (the calling user or service is authenticated) and authorisation (the calling identity has rights to retrieve from the corpora the query touches). For systems where retrieval is mediated by a service account on behalf of an end user, the impersonation chain is documented and the principal-of-least-privilege framing applies.

Audit logging covers every retrieval with the calling identity, the corpus, the documents returned, and the retrieval-side scope filter applied. Retention aligns to the firm's cyber log-retention policy and to NYDFS Part 500 §500.6 audit-trail expectations.

### Indirect-injection adjacency through corpus content

This is the cyber overlay's load-bearing connection to `prompt-injection-risk`. Corpus content can carry adversarial instructions placed by an external counterparty (in customer correspondence, third-party intelligence feeds, vendor-supplied content) or by an insider (in policy documents, alert narratives, prior summaries). The grounding-evaluation work in this skill catalogues the failure mode (off-corpus answer, citation fabrication driven by injected content); the prompt-injection threat-surface review (in `prompt-injection-risk`) is the focused review.

The two skills work side-by-side for any RAG-using GenAI system. This skill records the corpus-content-injection failure mode and points to `prompt-injection-risk` for the threat-surface and tested-attack-class detail. The recommended-actions section confirms a `prompt-injection-risk` review is in flight or on file.

### Mitigations expand to include the cyber control set on the corpus surface

Beyond the standard set:

- Retrieval-side authentication and authorisation per the firm's identity and access management.
- Audit logging on retrieval, retained per the cyber log-retention policy.
- Corpus-write controls: who can ingest, who can update, who can delete; documented and enforced.
- Content-integrity controls on dynamic corpora: hash drift detection, last-modified tracking, source-of-truth reconciliation for vendor-supplied corpora.
- Vendor and supply-chain controls on the foundation-model provider, the embedding-model provider, and the retrieval-platform provider, captured in the third-party risk register.
- Network-layer controls on retrieval-platform and serving-environment connectivity.

### Monitoring adds the cyber-tagged signal set

The baseline cyber signals to add when the overlay is flagged:

- Authentication and authorisation anomalies on the retrieval-platform serving endpoint.
- Retrieval-source distribution audit; sudden drift in source distribution may indicate either content-pipeline issue or adversarial activity.
- Content-hash drift on dynamic corpora; off-cycle content changes are an investigation trigger.
- Vendor change-of-version signals for the foundation model, the embedding model, and the retrieval-platform; an unannounced version swap is a cyber signal.
- Cross-scope retrieval anomaly (the retrieval scope filter returning content outside the calling identity's authorised scope) as a privacy-and-cyber co-signal.

### Incident response names the corpus-compromise classes

For a RAG evaluation review the incident-response framing centres on corpus integrity and corpus access:

- Suspected corpus poisoning (anomaly in citation precision plus retrieval-source-audit signal): cyber-and-AI joint runbook; vendor management notified for vendor-supplied corpora; corpus version freeze pending investigation.
- Confirmed unauthorised retrieval (cross-scope or beyond-authorised-scope): privacy-and-cyber joint runbook; notification trigger evaluation per the privacy overlay and the loaded sector overlay; off-switch criterion: pause the affected scope of the retrieval until remediation.
- Confirmed corpus tampering (insider or third-party compromise of corpus content): cyber incident runbook; vendor management notified for vendor-supplied corpora; corpus version freeze pending forensic; pointer to `prompt-injection-risk` for the tested-attack-class re-validation.

The off-switch criterion is the operational decision the runbook turns on. A confirmed corpus-compromise event with no defined off-switch is a finding.

## Recommended actions add the cyber-specific items

The standard cyber-tagged recommended-actions items the overlay surfaces:

- Confirm a `prompt-injection-risk` review is on file or in flight for the same use case.
- Confirm retrieval-side authentication and authorisation are documented, exercised, and audited.
- Confirm vendor change-of-version notice and audit rights for the foundation-model, embedding-model, and retrieval-platform providers, captured in the third-party risk register.
- IR drill on corpus-compromise scenarios at a defined cadence (annual at minimum; quarterly for tier-1 use cases).

## Cyber-specific output additions

In the structured object (`schemas/rag-evaluation-review.schema.json`):

- `corpus_fitness[]` entries with `access_controls` populated and the cyber-tagging convention applied.
- `mitigations[]` entries with cyber-tagged owner (CISO function or sub-function).
- `monitoring[]` entries with cyber-tagged escalation path.
- `cross_cutting_overlay_notes.cyber` carries the cyber-specific fields: control-family tagging on corpus-fitness entries, named cyber-side mitigations, cyber-tagged monitoring signals, and pointer to the `prompt-injection-risk` review.
- `recommended_actions[]` entries with cyber-tagged owner role.

## Common pitfalls in cyber-flagged RAG reviews

- Treating retrieval-side authentication as the application's responsibility and asserting it is "in place" without confirming the impersonation chain. The principal-of-least-privilege framing on service-account-mediated retrieval is structural and is a finding when it is not documented.
- Treating audit logging as an engineering concern rather than a cyber-control concern. The retention cadence and the queryability by the cyber team are the decision points; absent these, the logs are operational telemetry not control evidence.
- Omitting the indirect-injection adjacency. This skill catalogues the grounding-side failure mode (off-corpus answer, citation fabrication driven by injected content); the focused threat-surface review lives in `prompt-injection-risk`. Not naming the adjacency leaves a coverage gap.
- Treating vendor-supplied corpora (regulatory-text databases, third-party intelligence feeds) as integrity-attested without a content-integrity control. Vendor self-attestation is not the same as firm-side integrity monitoring.
- Reporting an unannounced foundation-model version swap as a model-risk event without the cyber framing. Vendor change-of-version is also a cyber signal; both framings need to be in the review.
