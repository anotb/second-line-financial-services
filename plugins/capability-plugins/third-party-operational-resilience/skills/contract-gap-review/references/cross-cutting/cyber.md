# Cyber cross-cutting overlay — contract-gap-review

When the engagement scope flags cyber, or whenever the contract touches NPI, PHI, PCI, customer prompts, or any control on the firm's important-business-service path, load this overlay. Cyber is in scope by default for AI vendors and for any contract supporting an IBS chain.

## Operative anchors

- **NYDFS 23 NYCRR Part 500.11** — Third-Party Service Provider Security Policy. §500.11(a) requires written contractual safeguards including multi-factor authentication, encryption, notification of cybersecurity events, access controls, and representations and warranties. §500.11(b) periodic assessment. Where the firm is a covered entity, the matrix must include a row per safeguard with the contract reference.
- **NYDFS §500.17(a)** — 72-hour cybersecurity-event-notification clock for covered entities. The contract-side vendor-notification clock must close upstream (vendor-to-firm in less than 72 hours minus the firm's internal triage time).
- **FFIEC IT Examination Handbook — Information Security booklet** [verify current edition] — examiner-facing detail on third-party security clause expectations, complementary-user-entity controls, incident-cooperation.
- **Bank Service Company Act, 12 USC §1867(c)** (banking only) — examiner-access continuity. The cyber overlay should ensure the contract preserves regulator examination access into the vendor's security records, not only into transaction records.
- **CISA shared-responsibility model for cloud** — for cloud IaaS / PaaS / SaaS vendors, the responsibility split must be evidenced in the contract. The vendor's "responsibility line" varies by service tier; the matrix must include a shared-responsibility-articulation row, not a single "cloud security" row.
- **SEC Reg S-P (May 2024 amendments)** [verify exact compliance dates by entity type and size] — for advisers, BDs, and funds: covered-institution safeguarding obligations, service-provider written-contract requirements, breach-notification timing.
- **SEC cyber-disclosure rule** (Item 1.05 Form 8-K and Reg S-K Item 106) — for publicly-listed registrants, the vendor sits on the disclosure path when an incident at the vendor is material to the firm. The matrix must surface the contract-side notification clock against the firm's four-business-day determination-and-disclosure window.

## Cyber clause cluster the matrix surfaces

- **Cybersecurity-event-notification clock.** Vendor-to-firm timing aligned upstream with the tightest applicable regulatory clock (NYDFS 72-hour, SEC four-business-day determination, GLBA Safeguards 30-day customer notice for the firm under amended 314, HIPAA 60-day breach-notification chain, SOX timing where the vendor sits on a material-control path). Aggregate any silence or "reasonable period" phrasing as `high`-severity for a critical vendor.
- **Incident-response cooperation.** Severity taxonomy alignment, customer-notification posture, regulator-notification cooperation, evidence preservation, post-mortem availability, contact-paths.
- **Encryption posture.** In-transit and at-rest commitments, key-management model (vendor-managed vs customer-managed vs BYOK / HYOK), HSM posture if applicable.
- **Identity and access.** SSO and SCIM support, privileged-access management, just-in-time access posture for vendor support staff, multi-factor authentication for vendor personnel.
- **Logging and monitoring.** Customer access to security logs, retention windows, integration to the firm's SIEM, anomalous-access alerting, log-tamper-resistance.
- **Vulnerability-management cooperation.** Scanning cadence, mean-time-to-remediate by severity, exception-register access, coordinated-disclosure posture.
- **Penetration-test rights.** Frequency, scope, cost-allocation, share-of-results, remediation-tracking.
- **Audit-and-access rights.** Scope, frequency, cost-allocation, on-site posture, third-party-auditor acceptability, regulator-access continuity.
- **Sub-contractor security flow-down.** Sub-processor identification, change-notification, rejection rights, security-floor flow-down, audit-rights flow-down.
- **Shared-responsibility articulation.** For cloud arrangements; explicit allocation by service tier; not a single "as per industry standard" row.

## AI-vendor cyber clause expansions

When `ai_vendor=true`, the cyber overlay extends to:

- **Prompt-injection defence.** Typically a shared-responsibility item; the contract must clarify the boundary and the cooperation posture on prompt-injection-related incidents.
- **Model-supply-chain integrity.** Model-version pinning, deprecation-notice clock, provenance evidence, change-management cooperation on model upgrades.
- **Tool-use sandbox commitments.** For agentic systems, the action-authorisation surface, audit-trail posture, and incident-cooperation on tool-misuse.
- **Eval-evidence access.** Where the vendor publishes evaluation evidence, the contract should include access posture and update-notification on material changes to evaluation evidence.

## Cross-link inside the plugin

- **`vendor-diligence` cyber overlay** carries the read-through on cyber evidence; the contract gap matrix is the input on whether the contract gives the firm the rights to obtain that evidence. Findings here flow upstream to the diligence pack via `contract_gap_summary`.

## Common cyber-overlay pitfalls

- "Within a reasonable period" for cybersecurity-event notification. This is a vendor-favourable phrasing that breaks the firm's upstream clock. Always a finding for a vendor touching NPI, PHI, PCI, or IBS controls.
- "Right to audit subject to reasonable cooperation" as audit rights. Reservation of vendor discretion; mark `partial` and surface the missing scope, frequency, cost-allocation, and remedy.
- Treating "encryption in transit and at rest" as the encryption row. Key-management model (vendor-managed vs customer-managed vs BYOK / HYOK) is a separate finding.
- Single "cloud security" row for an IaaS / PaaS / SaaS arrangement. Shared-responsibility articulation by service tier is a distinct row.
- Sub-processor flow-down conflated with visibility. Flow-down is a contractual mechanic; visibility, change-notification, and rejection rights are separate rows.
