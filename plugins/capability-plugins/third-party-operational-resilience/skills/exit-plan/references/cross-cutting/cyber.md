# Cyber cross-cutting overlay — exit-plan

When the engagement scope flags cyber, or whenever the vendor holds NPI, PHI, PCI, customer prompts, or any control on the firm's important-business-service path at termination, load this overlay. Cyber is in scope by default for AI vendors and for any termination of a vendor that reaches inside firm systems.

## Operative anchors

- **NYDFS 23 NYCRR Part 500.11** — Third-Party Service Provider Security Policy. Periodic-assessment obligations carry through to the close-out of an arrangement; the exit plan must show the close-out-assessment posture.
- **FFIEC IT Examination Handbook — Information Security booklet** [verify current edition] — examiner-facing detail on third-party security expectations including transition.
- **Bank Service Company Act, 12 USC §1867(c)** (banking only) — examination-access continuity through wind-down. The cyber overlay must preserve regulator examination access into the vendor's security records (audit logs, incident-response records, evaluation evidence) through and after cutover, not only into transaction records.
- **CISA shared-responsibility model for cloud** — for cloud IaaS / PaaS / SaaS vendors, the responsibility split through transition must be evidenced; access-revocation choreography sits firm-side.
- **SEC Reg S-P (May 2024 amendments)** [verify exact compliance dates] — for advisers, BDs, and funds: customer-information-safeguarding obligations on transition; service-provider written-contract requirements including breach-notification posture.
- **SEC cyber-disclosure rule** (Item 1.05 Form 8-K and Reg S-K Item 106) — for publicly-listed registrants, a forced or contested termination triggered by a vendor incident can land on the disclosure path. The cyber overlay must surface the vendor's incident-notification clock against the firm's 8-K materiality clock.

## Secure data extraction

- **Encrypted transit** — data in motion encrypted under firm-acceptable cipher suites; out-of-band key delivery; integrity verification on receipt.
- **Integrity verification** — checksum or hash verification at the file or record level; bit-level audit on extracted books-and-records material.
- **Volume and rate management** — large-volume extracts may require staged delivery; bandwidth cost and timing in the plan.
- **Format integrity** — vendor-proprietary formats may degrade on extraction; the plan should require an extraction-rehearsal where vendor-proprietary formats are in scope.

## Key rotation and credential revocation

- **Customer-managed and shared keys** — keys the firm has shared with the vendor (KMS keys, BYOK, HYOK material) rotated on cutover and old keys destroyed per firm key-management policy.
- **Service credentials** — API keys, OAuth client secrets, SAML certificates, mTLS certificates revoked at the firm-side identity provider and at the vendor.
- **Privileged-access tokens** — vendor-side privileged accounts and just-in-time access grants disabled at cutover; vendor-personnel-side firm credentials disabled at firm IdP.
- **Network paths** — VPN tunnels decommissioned; private-link or PrivateLink endpoints torn down; firewall rules removed; DNS records updated.

## Access-revocation choreography

- **Sequencing** — revocation is sequenced against cutover, not before. Premature revocation can strand in-flight data; late revocation extends the residual-access window.
- **Vendor-personnel access** — list of vendor personnel with firm-system access; offboarding choreography per role.
- **Firm-personnel access to vendor** — firm-personnel access to vendor systems revoked on cutover plus the agreed support tail.
- **Federated identity** — SSO and SCIM teardown; trust relationships removed.

## Vendor-side destruction certification

- **Form** — signed certificate of destruction is the minimum; for higher-risk arrangements, expect log-evidence and a third-party-attestation option.
- **Scope** — the destruction obligation must cover all data categories in `data_access`, including derivative artifacts (cached data, indexes, vector embeddings for AI vendors, model fine-tune artifacts, abuse-monitoring retention windows, log archives).
- **Carve-outs** — lawful retention by the vendor (regulatory archive, fraud investigation, legal hold) carved out explicitly with the retention period and the post-retention destruction commitment named.
- **Firm-side retention** — the destruction certificate retained at the firm per the firm's vendor-record-retention policy.

## SEC cyber-disclosure exposure on a forced or contested termination

- **Materiality** — where the firm is a publicly-listed registrant and the vendor incident driving exit is material to the firm's investors, Item 1.05 Form 8-K obligations attach. The cyber overlay must surface the firm's 8-K timing against the vendor's incident-notification clock.
- **Reg S-K Item 106** — annual disclosure of cybersecurity risk-management; a vendor exit driven by an incident may shift the firm's disclosure on third-party risk-management.
- **Coordination with the firm's disclosure committee** — the operational-resilience function and the disclosure committee must be in the same conversation on a forced or contested termination.

## SIEM and DLP cutover

- **SIEM integration** — vendor-side log feeds disconnected; substitute-vendor feeds connected; alert-rule baseline re-tuned for the substitute.
- **DLP rules** — DLP rules referencing the outgoing vendor's domains, IP ranges, and integration paths updated for the substitute.
- **SOC playbooks** — incident-response playbooks updated to the substitute vendor's incident-response contacts and clocks.
- **Threat-intelligence feeds** — vendor-specific TI feeds disconnected; substitute feeds (where applicable) connected.

## AI vendor cyber considerations

When `ai_vendor=true`:

- **Prompt and completion log destruction** — vendor-side abuse-monitoring retention windows must be honoured first; destruction certified once the windows close.
- **Vector index and embedding destruction** — RAG-vendor exits must include destruction of vector indices and embeddings derived from firm content.
- **Fine-tune artifact destruction** — vendor-side fine-tune weights, adapter weights, and training-job artifacts must be destroyed unless contractually returned.
- **Model-version pin handling** — the deployed checkpoint at termination; whether a final-version export is contractually available and what cyber-control posture applies to the exported artifact at the firm.
- **Agent tool revocation** — for agentic vendors, revoking the action-authorisation surface (function-calling endpoints, tool whitelists, MCP-server connections) is part of the cutover.
- **Substitute-vendor cyber posture** — the substitute model vendor's diligence pack covers prompt-injection defence, data-handling posture, eval-coverage posture; the exit plan calls for the substitute pack as a precondition.

## Common cyber-overlay pitfalls in exit planning

- Treating data extraction as solved by "we have an export API". Format integrity, volume, schema, and validation against firm-of-record are all part of the cyber-overlay read.
- Sequencing revocation before cutover and stranding in-flight data.
- Skipping fourth-party access. Vendor's subcontractors may also hold firm credentials or data; the destruction obligation should reach them.
- Treating the destruction certificate as the end of the work. Firm-side retention of the certificate, the destruction-evidence log, and the post-validation hold all matter.
- Skipping the SEC 8-K timing read on a forced or contested termination at a publicly-listed registrant.
- Skipping the SIEM, DLP, and SOC playbook cutover and discovering the gaps after a substitute-vendor incident.
- Treating an AI-vendor cyber cutover as identical to a non-AI cutover. Vector indices, embeddings, prompt logs, fine-tune artifacts, and agent-tool revocation are AI-specific.
