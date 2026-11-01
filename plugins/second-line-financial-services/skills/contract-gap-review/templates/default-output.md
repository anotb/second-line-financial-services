# Contract gap matrix

**Vendor**: [legal entity; brand name if different]
**Contract identifier**: [MSA number, SOW number, order form reference, addenda]
**Arrangement ID**: [stable ID; reused with criticality-assessment, vendor-diligence, exit-plan]
**Engagement ID**: [pointer to scope record, or "none — scope not formalised"]
**As of**: [date]
**Review type**: [pre-signature | renewal | assignment-or-change-of-control | material-amendment | exit-triggered-re-review | post-incident-re-review | regulatory-change-driven-re-review]
**Owner (role)**: [e.g., third-party risk manager, contract owner]
**Approver (role)**: [per firm policy for this criticality tier]
**Counsel-of-record (role)**: [in-house or external counsel reviewing the redlines]
**Confidence label**: [high | medium | low | unknown]

## Arrangement and criticality

- Vendor service description.
- Business process supported; important business service (where the firm has an IBS map).
- Criticality tier (sourced from `criticality-assessment`; do not re-set here): [not-critical | important | critical | unknown].
- Data scope: [NPI | PHI | PCI | model-prompts | model-outputs | training-data | logs-only | metadata-only | other].
- Data locations and cross-border flows: [list].
- AI-vendor flag: [true | false].
- Digital-operational-resilience-act in-scope flag (critical-or-important-function ICT service): [true | false].

## Applicable regimes and overlay set

- Sector overlay(s) loaded: [banking | insurance | capital-markets | payments-fintech | multi-overlay (specify)].
- Cross-cutting overlay(s) loaded: [cyber | privacy | both | none — explain].
- Mandatory-clause overlay loaded: [true | false].
- Source posture: [public-only | public-plus-firm-policy | public-plus-firm-policy-plus-system-of-record-evidence | connector-aware].

## Clause-by-clause findings

| ID | Clause topic | Source criterion (path to anchor + section) | Contract reference | Coverage | Gap rationale | Recommended-amendment posture | Severity |
|---|---|---|---|---|---|---|---|
| 1 | Scope and performance | `references/source-anchors.md` — interagency contract negotiation [verify section] | §[X.Y] | present / partial / absent / not-applicable | | | low / medium / high |
| 2 | Compliance with applicable laws | | | | | | |
| 3 | Audit and reporting rights | | | | | | |
| 4 | Regulator examination access | | | | | | |
| 5 | Ownership and licences | | | | | | |
| 6 | Business resumption and contingency | | | | | | |
| 7 | Sub-contracting (identification, change-notice, rejection) | | | | | | |
| 8 | Confidentiality and information security | | | | | | |
| 9 | Indemnification | | | | | | |
| 10 | Limits on liability | | | | | | |
| 11 | Insurance | | | | | | |
| 12 | Dispute resolution | | | | | | |
| 13 | Default and termination | | | | | | |
| 14 | Service levels and performance reporting | | | | | | |

> Add rows for every clause topic the loaded overlays raise. Cite source by file path; do not restate excerpts.

## Mandatory-clause overlay (digital-operational-resilience act, critical-or-important-function ICT service)

> Populate this section only when the in-scope flag is true. Otherwise omit. Absence of any of these rows is a `high`-severity finding by source.

| ID | Mandatory-clause topic | Source criterion | Contract reference | Coverage | Gap rationale | Recommended-amendment posture | Severity |
|---|---|---|---|---|---|---|---|
| M1 | Termination rights tied to supervisory recommendation | `references/source-anchors.md` — Article 30 [verify subarticle] | | | | | high |
| M2 | Full description of services | | | | | | |
| M3 | Locations of data processing and storage | | | | | | |
| M4 | Sub-outsourcing notification timing and rejection rights | | | | | | |
| M5 | Exit-strategy and transitional support | | | | | | |
| M6 | Audit-and-access for the firm and the competent authority | | | | | | |

## Cyber clause cluster

| ID | Cyber-clause topic | Source criterion | Contract reference | Coverage | Gap rationale | Recommended-amendment posture | Severity |
|---|---|---|---|---|---|---|---|
| C1 | Cybersecurity-event notification clock (vendor-to-firm, aligned upstream with the tightest applicable regulatory clock) | `references/cross-cutting/cyber.md` | | | | | |
| C2 | Incident-response cooperation and evidence preservation | | | | | | |
| C3 | Encryption posture (in-transit, at-rest) | | | | | | |
| C4 | Key-management model (vendor-managed / customer-managed / BYOK / HYOK) | | | | | | |
| C5 | Identity and access (SSO, SCIM, PAM, JIT, MFA for vendor staff) | | | | | | |
| C6 | Logging, monitoring, customer access, retention | | | | | | |
| C7 | Vulnerability-management cooperation (cadence, MTTR, exception register) | | | | | | |
| C8 | Penetration-test rights (frequency, scope, share-of-results) | | | | | | |
| C9 | Shared-responsibility articulation (cloud arrangements) | | | | | | |
| C10 | AI-vendor only: prompt-injection defence, model-supply-chain integrity, agent-tool sandbox | | | | | | |

## Privacy clause cluster

| ID | Privacy-clause topic | Source criterion | Contract reference | Coverage | Gap rationale | Recommended-amendment posture | Severity |
|---|---|---|---|---|---|---|---|
| P1 | DPA coverage | `references/cross-cutting/privacy.md` | | | | | |
| P2 | Sub-processor list and change-notice | | | | | | |
| P3 | Deletion-and-return on termination | | | | | | |
| P4 | Retention windows aligned to firm policy | | | | | | |
| P5 | Cross-border-transfer mechanism | | | | | | |
| P6 | Data-subject-rights handling | | | | | | |
| P7 | Breach-notification chain (aligned upstream with regulator-and-customer-notice clock) | | | | | | |
| P8 | HIPAA business-associate-agreement (where PHI may appear) | | | | | | |
| P9 | AI-vendor only: training-data-use, prompt-as-customer-data treatment, abuse-monitoring exception scope | | | | | | |

## Subcontracting and fourth-party clauses

- Sub-processor identification: present / partial / absent.
- Change-notification timing: [days] / "reasonable period" / silent.
- Rejection rights: present / absent.
- Security and privacy floor flow-down: present / partial / absent.
- Audit-rights flow-down: present / partial / absent.
- Fourth-party register access (sponsor-bank programs): present / partial / absent.

## Termination, exit, and assignment clauses

- Termination for convenience.
- Termination for cause (and the trigger-set: SLA failure, security incident, change-of-control, regulatory-action, insolvency, supervisory recommendation where in-scope).
- Transitional-support obligation (period, scope, cost-allocation, evidence handover).
- Exit-strategy commitment.
- Data-portability on termination (form, format, timing, certification).
- Records-retention through wind-down.
- Assignment and change-of-control consent.

## Liability, indemnity, and insurance clauses

- Limit of liability (cap level versus firm's expected loss; carve-outs for IP infringement, breach of confidentiality, data breach, gross negligence, willful misconduct).
- Indemnification scope (third-party claims, regulatory penalties where allowed by law, IP infringement, breach of safeguards).
- Insurance coverage (lines, limits, evidence, additional-insured posture).

## Audit, reporting, and regulator-access clauses

- Audit scope, frequency, cost-allocation, on-site posture, third-party-auditor acceptability.
- Performance reporting (cadence, format, delivery).
- Problem reporting.
- Regulator examination access (Bank Service Company Act §1867(c) for banking, equivalent for other sectors).

## Open questions for legal and the contract owner

- [Each question names the row it relates to and the decision it supports.]

## Reviewer questions

- [Clustered for the forum that decides: TPRM forum / risk committee / AI risk committee / fund board.]

## Legal-review triggers

- [Specific clauses where counsel must redline before signature; tied to severity and to the firm's policy.]

## Summary severity

- Highest individual-clause severity: [low / medium / high].
- Aggregation lift (two or more `medium` findings concentrated in audit, termination, or incident-notification cluster): [yes / no].
- Summary severity: [low / medium / high].

## Recommended legal-review-and-decision posture

- **Recommended posture**: [redline-and-sign | redline-and-defer-decision | escalate-to-counsel | escalate-to-approver | decline].
- **Conditions**: [bulleted, specific, verifiable].
- **Decision checkpoints this matrix must clear**: scope, evidence, authority, impact, decision (counsel redline at scope and authority; approver sign-off at decision).
- **Decision forum and attestation block**: [counsel | TPRM forum | risk committee | AI risk committee | fund board]; owner (role) and approver (role) named.
- **Next-review trigger**: [renewal date, scope-change trigger, regulatory-change-driven trigger, model-version-change for AI vendors].
- The matrix does not approve the contract. Counsel drafts language; the named approver decides.

## Source trace

| Claim | Source | Section | Date | URL or file ref |
|---|---|---|---|---|
| | | | | |

Cite `references/source-anchors.md` for canonical citations. Use `[verify section]` if the section reference is unknown; do not invent.

---

*Matrix depth scales to vendor tier and to digital-operational-resilience-act in-scope flag.* For a not-critical vendor, the cyber and privacy clusters may collapse to fewer rows and the mandatory-clause overlay is omitted. A critical vendor or an in-scope arrangement gets full depth with reviewer questions clustered for the relevant forums.

*Audience shapes the matrix.* A TPRM forum reads it operationally. A risk committee reads it for severity rollup and conditions. A general-counsel-facing matrix reads as a redline-readiness brief. Lead with the decision the audience must make.
