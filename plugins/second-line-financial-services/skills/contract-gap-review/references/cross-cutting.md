# cross-cutting

One section per topic. Read only the sections the scope calls for.

## cyber

### Cyber cross-cutting overlay — contract-gap-review

When the scope flags cyber, or whenever the contract touches NPI, PHI, PCI, customer prompts, or any control on the firm's important-business-service path, load this overlay. Cyber is in scope by default for AI vendors and for any contract supporting an IBS chain.

#### Operative anchors

- **NYDFS 23 NYCRR Part 500.11** — Third-Party Service Provider Security Policy. §500.11(a) requires written contractual safeguards including multi-factor authentication, encryption, notification of cybersecurity events, access controls, and representations and warranties. §500.11(b) periodic assessment. Where the firm is a covered entity, the matrix must include a row per safeguard with the contract reference.
- **NYDFS §500.17(a)** — 72-hour cybersecurity-event-notification clock for covered entities. The contract-side vendor-notification clock must close upstream (vendor-to-firm in less than 72 hours minus the firm's internal triage time).
- **FFIEC IT Examination Handbook — Information Security booklet** [verify current edition] — examiner-facing detail on third-party security clause expectations, complementary-user-entity controls, incident-cooperation.
- **Bank Service Company Act, 12 USC §1867(c)** (banking only) — examiner-access continuity. The cyber overlay should ensure the contract preserves regulator examination access into the vendor's security records, not only into transaction records.
- **CISA shared-responsibility model for cloud** — for cloud IaaS / PaaS / SaaS vendors, the responsibility split must be evidenced in the contract. The vendor's "responsibility line" varies by service tier; the matrix must include a shared-responsibility-articulation row, not a single "cloud security" row.
- **SEC Reg S-P (May 2024 amendments)** [verify exact compliance dates by entity type and size] — for advisers, BDs, and funds: covered-institution safeguarding obligations, service-provider written-contract requirements, breach-notification timing.
- **SEC cyber-disclosure rule** (Item 1.05 Form 8-K and Reg S-K Item 106) — for publicly-listed registrants, the vendor sits on the disclosure path when an incident at the vendor is material to the firm. The matrix must surface the contract-side notification clock against the firm's four-business-day determination-and-disclosure window.

#### Cyber clause cluster the matrix surfaces

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

#### AI-vendor cyber clause expansions

When `ai_vendor=true`, the cyber overlay extends to:

- **Prompt-injection defence.** Typically a shared-responsibility item; the contract must clarify the boundary and the cooperation posture on prompt-injection-related incidents.
- **Model-supply-chain integrity.** Model-version pinning, deprecation-notice clock, provenance evidence, change-management cooperation on model upgrades.
- **Tool-use sandbox commitments.** For agentic systems, the action-authorisation surface, audit-trail posture, and incident-cooperation on tool-misuse.
- **Eval-evidence access.** Where the vendor publishes evaluation evidence, the contract should include access posture and update-notification on material changes to evaluation evidence.

#### Cross-link inside the plugin

- **`vendor-diligence` cyber overlay** carries the read-through on cyber evidence; the contract gap matrix is the input on whether the contract gives the firm the rights to obtain that evidence. Findings here flow upstream to the diligence pack via `contract_gap_summary`.

#### Common cyber-overlay pitfalls

- "Within a reasonable period" for cybersecurity-event notification. This is a vendor-favourable phrasing that breaks the firm's upstream clock. Always a finding for a vendor touching NPI, PHI, PCI, or IBS controls.
- "Right to audit subject to reasonable cooperation" as audit rights. Reservation of vendor discretion; mark `partial` and surface the missing scope, frequency, cost-allocation, and remedy.
- Treating "encryption in transit and at rest" as the encryption row. Key-management model (vendor-managed vs customer-managed vs BYOK / HYOK) is a separate finding.
- Single "cloud security" row for an IaaS / PaaS / SaaS arrangement. Shared-responsibility articulation by service tier is a distinct row.
- Sub-processor flow-down conflated with visibility. Flow-down is a contractual mechanic; visibility, change-notification, and rejection rights are separate rows.

## privacy

### Privacy cross-cutting overlay — contract-gap-review

When the scope flags privacy, or whenever the contract touches nonpublic personal information, protected health information, biometric data, customer prompts, or any other regulated personal data, load this overlay. Privacy is in scope by default for AI vendors that process customer prompts.

#### Operative anchors

- **GLBA Safeguards Rule (Standards for Safeguarding Customer Information, 16 CFR Part 314 as amended)** — for FTC-jurisdiction financial-institution covered entities. §314.4(f) service-provider obligations: select capable providers, contractually require them to implement safeguards, and periodically assess them. The contract gap matrix must surface the §314.4(f) contract row distinct from generic confidentiality language.
- **GLBA Privacy Rule (Regulation P, 12 CFR Part 1016)** — joint-marketing and service-provider information-sharing exceptions and the contract terms required to use them.
- **HIPAA Privacy and Security Rules (45 CFR Parts 160, 164)** — where the vendor touches protected health information, the business-associate-agreement (45 CFR §164.504(e)) is a stand-alone contract that must run alongside the commercial agreement. The matrix surfaces a row for BAA execution, the breach-notification chain (60-day clock), minimum-necessary access, sub-business-associate flow-down, and termination obligations.
- **State privacy laws** — CCPA / CPRA (California), VCDPA (Virginia), CTDPA (Connecticut), CPA (Colorado), UCPA (Utah), TDPSA (Texas), and the rolling list of state comprehensive privacy laws. Service-provider, processor, and contractor contract clauses vary by state but converge on: purpose-limitation, confidentiality, sub-processor flow-down, deletion-and-return, audit-cooperation, and a prohibition on selling or sharing personal information. GLBA-covered data is excluded from many state privacy laws but not all; the matrix must read the GLBA-exemption scope state-by-state.
- **NAIC Insurance Data Security Model Law (Model #668), §4.F** (insurance only) — operative third-party-service-provider contract obligation set, additive to or overlapping with NYDFS 500.11.
- **NYDFS 23 NYCRR Part 500.11** — third-party security covers privacy considerations within the cyber-program frame.
- **SEC Reg S-P (May 2024 amendments)** [verify exact compliance dates by entity type and size] — for advisers, BDs, and funds: customer-information-safeguarding and breach-notice elements; 30-day customer notice posture; service-provider written contracts requiring breach notification.

#### Privacy clause cluster the matrix surfaces

- **Data-processing-agreement coverage.** A DPA or DPA-equivalent attached or incorporated by reference; coverage of purposes, categories of data, categories of data subjects, retention, processing locations, sub-processors, security floor, audit-cooperation, deletion-and-return.
- **Sub-processor list and change-notice.** Current sub-processor list, change-notification timing, rejection-rights mechanic. Flow-down clauses do not equal visibility; surface as separate rows.
- **Deletion-and-return on termination.** Form, format, timing, certification of destruction.
- **Retention windows.** Aligned to the firm's retention policy and to applicable books-and-records or regulatory-retention obligations; not the vendor's default.
- **Cross-border-transfer mechanism.** Where applicable: standard contractual clauses, adequacy-decision reliance, transfer-impact-assessment cooperation, data-localisation-compliance evidence.
- **Data-subject-rights handling.** How the vendor processes customer access, deletion, correction, opt-out, and data-portability requests routed through the firm; timing aligned to the firm's response window.
- **Breach-notification chain.** Vendor-to-firm timing aligned upstream with the firm's regulator-and-customer-notice clock (HIPAA 60-day, GLBA 30-day customer notice under amended 314, state-law 30-to-90-day variations, Reg S-P 30-day where applicable).
- **Privacy-impact-assessment cooperation.** Where the firm's PIA threshold is hit, the vendor's cooperation posture and information-access.

#### HIPAA business-associate-agreement clause expansions

Where PHI may be in scope (always check incidental-PHI scenarios for AI vendors processing free-text narratives):

- BAA execution as a stand-alone contract.
- Permitted-uses-and-disclosures definition tied to the underlying service.
- Safeguards (administrative, physical, technical) at HIPAA Security Rule equivalent.
- Sub-business-associate flow-down with the same content.
- Breach-notification chain (60-day OCR clock; vendor-to-firm timing must close upstream with margin).
- Minimum-necessary access posture for vendor personnel.
- Termination: return or destruction of PHI, or extension of safeguards if return or destruction is infeasible.

#### AI-vendor privacy clause expansions

When `ai_vendor=true`, the privacy overlay extends to:

- **Training-data-use commitment.** Vendor's contractual commitment that customer prompts and outputs are not used to train the vendor's models, with the abuse-monitoring exception explicitly scoped.
- **Prompt-as-customer-data treatment.** Where customer interactions may carry NPI, PHI, PCI, or biometric data, the contract must reflect the data-handling regime appropriate to the data category, not the vendor's default.
- **Retention windows for prompts and outputs.** Aligned to the firm's retention policy; not the vendor's default abuse-monitoring window.
- **Sub-processor list for the AI service.** Inference compute, retrieval components, evaluation pipeline, fine-tuning data flows.

#### Cross-link inside the plugin

- **`vendor-diligence` privacy overlay** carries the read-through on privacy evidence; the contract gap matrix is the input on whether the contract gives the firm the rights to obtain that evidence. Findings here flow upstream to the diligence pack via `contract_gap_summary`.

#### Common privacy-overlay pitfalls

- Treating a confidentiality clause as a DPA. A DPA is a distinct artifact with prescribed content; absence is a `high`-severity finding where the vendor processes regulated personal data.
- Skipping HIPAA business-associate analysis for an AI vendor processing free-text narratives. PHI may incidentally appear; the BAA row must be surfaced even where the vendor does not market itself as a healthcare vendor.
- Reading "we comply with applicable privacy laws" as compliance. The matrix surfaces the specific contract-content rows the laws require; generic compliance language does not satisfy the rule-specific contract-content expectations.
- Accepting vendor-default retention windows. Retention must align to the firm's policy and to applicable books-and-records or regulatory-retention obligations.
- Treating sub-processor flow-down as visibility. Flow-down is a contractual mechanic; current-list, change-notification, and rejection rights are separate rows.
