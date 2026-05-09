# Cyber cross-cutting overlay — vendor-diligence

When the scope flags cyber, or whenever the vendor touches NPI, PHI, PCI, customer prompts, or any control on the firm's important-business-service path, load this overlay. Cyber is in scope by default for AI vendors.

## Operative anchors

- **NYDFS 23 NYCRR Part 500.11** — Third-Party Service Provider Security Policy. Identification, risk assessment, minimum cybersecurity practices, due diligence, periodic assessment. Where the firm is a NYDFS Covered Entity, 500.11 reach extends to vendor diligence directly.
- **FFIEC IT Examination Handbook — Information Security booklet** [verify current edition] — examiner-facing detail on third-party security expectations, complementary user entity controls, and program-level coverage.
- **Bank Service Company Act, 12 USC §1867(c)** (banking only) — examiner-access continuity. The cyber overlay should ensure the contract preserves regulator examination access into the vendor's security records, not only into transaction records.
- **CISA shared-responsibility model for cloud** — for cloud IaaS / PaaS / SaaS vendors, the responsibility split must be evidenced. The vendor's "responsibility line" varies by service tier; treat the model as the read-through frame, not as a one-size answer.
- **SEC Reg S-P (May 2024 amendments)** [verify exact compliance dates by entity type and size] — for advisers, BDs, and funds: covered-institution safeguarding obligations, service-provider written-contract requirements, and breach-notification clock posture.
- **SEC cyber-disclosure rule** (Item 1.05 Form 8-K and Reg S-K Item 106) — for publicly-listed registrants, the vendor sits on the disclosure path when an incident at the vendor is material to the firm. The diligence pack must surface the vendor's incident-notification clock against the firm's 8-K timing.

## Evidence the cyber overlay expects

- **SOC 2 Type II report**: read scope, period covered, exceptions noted, complementary user entity controls (CUECs), and trust-services criteria addressed (Security at minimum; Confidentiality, Availability, Processing Integrity, Privacy as relevant). A clean opinion with critical CUECs unaddressed by the firm is not a green light.
- **ISO/IEC 27001 certificate and Statement of Applicability**: certificate alone is insufficient; the SoA shows scope and exclusions.
- **Penetration-test summary**: third-party-conducted; current within the firm's policy window; remediation status of medium-and-above findings.
- **Vulnerability-management evidence**: scanning cadence, mean-time-to-remediate by severity, exception register.
- **Encryption posture**: in-transit and at-rest, key-management model (vendor-managed vs customer-managed vs BYOK / HYOK), HSM posture if applicable.
- **Identity and access**: SSO and SCIM support, privileged-access management, just-in-time access posture for vendor support staff who can read customer data.
- **Logging and monitoring**: customer access to security logs, retention, integration to the firm's SIEM, anomalous-access alerting.
- **Incident-response**: severity taxonomy, customer-notification clock by severity, contact paths, post-mortem cadence and exportability.
- **Breach history**: public disclosures, regulator actions, civil settlements; aging.

## Resilience evidence the cyber overlay touches

- **BCDR test reports** — the vendor's RTO and RPO are claims; only evidenced recovery test reports demonstrate the claim. Where the vendor's RTO meets the firm's impact tolerance for the supported business service only on paper, mark `bcdr_meets_firm_tolerance = false` until evidenced.
- **Failover-region tabletop coverage** — single-region BCDR evidence does not cover failover scenarios.

## AI vendor cyber considerations

When `ai_vendor=true`, the cyber overlay extends to:

- **Prompt-injection defence** — typically a shared-responsibility item; the contract and the trust-and-safety pages should clarify the boundary. Use this in `ai_specific_findings.shared_responsibility_clarity`.
- **Model-supply-chain integrity** — model-version pinning, deprecation notice clock, and provenance evidence.
- **Tool-use sandboxing** for agentic systems — where the vendor's agents can take actions, the action-authorisation surface and audit-trail posture are part of the cyber read.
- **Eval-evidence security** — the published eval and red-team evidence is base-model evidence; deployed-system eval security is the carrier of the actual cyber claim, and most published evidence does not cover the deployed system.

## Common cyber-overlay pitfalls

- Reading SOC 2 Type II as a green light without the scope, period, and CUEC analysis.
- Treating an ISO 27001 certificate as if it were a SoA.
- Treating a clean pen-test summary as if it covered the firm's specific deployment when it covered only the vendor's platform.
- Setting RTO/RPO to the vendor's claim instead of the firm's tolerance for the supported important business service.
- Missing the SEC cyber-disclosure-path read-through where the vendor is material to the firm's public reporting.
