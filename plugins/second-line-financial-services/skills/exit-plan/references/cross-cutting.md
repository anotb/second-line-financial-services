# cross-cutting

One section per topic. Read only the sections the scope calls for.

## cyber

### Cyber cross-cutting overlay — exit-plan

When the scope flags cyber, or whenever the vendor holds NPI, PHI, PCI, customer prompts, or any control on the firm's important-business-service path at termination, load this overlay. Cyber is in scope by default for AI vendors and for any termination of a vendor that reaches inside firm systems.

#### Operative anchors

- **NYDFS 23 NYCRR Part 500.11** — Third-Party Service Provider Security Policy. Periodic-assessment obligations carry through to the close-out of an arrangement; the exit plan must show the close-out-assessment posture.
- **FFIEC IT Examination Handbook — Information Security booklet** [verify current edition] — examiner-facing detail on third-party security expectations including transition.
- **Bank Service Company Act, 12 USC §1867(c)** (banking only) — examination-access continuity through wind-down. The cyber overlay must preserve regulator examination access into the vendor's security records (audit logs, incident-response records, evaluation evidence) through and after cutover, not only into transaction records.
- **CISA shared-responsibility model for cloud** — for cloud IaaS / PaaS / SaaS vendors, the responsibility split through transition must be evidenced; access-revocation choreography sits firm-side.
- **SEC Reg S-P (May 2024 amendments)** [verify exact compliance dates] — for advisers, BDs, and funds: customer-information-safeguarding obligations on transition; service-provider written-contract requirements including breach-notification posture.
- **SEC cyber-disclosure rule** (Item 1.05 Form 8-K and Reg S-K Item 106) — for publicly-listed registrants, a forced or contested termination triggered by a vendor incident can land on the disclosure path. The cyber overlay must surface the vendor's incident-notification clock against the firm's 8-K materiality clock.

#### Secure data extraction

- **Encrypted transit** — data in motion encrypted under firm-acceptable cipher suites; out-of-band key delivery; integrity verification on receipt.
- **Integrity verification** — checksum or hash verification at the file or record level; bit-level audit on extracted books-and-records material.
- **Volume and rate management** — large-volume extracts may require staged delivery; bandwidth cost and timing in the plan.
- **Format integrity** — vendor-proprietary formats may degrade on extraction; the plan should require an extraction-rehearsal where vendor-proprietary formats are in scope.

#### Key rotation and credential revocation

- **Customer-managed and shared keys** — keys the firm has shared with the vendor (KMS keys, BYOK, HYOK material) rotated on cutover and old keys destroyed per firm key-management policy.
- **Service credentials** — API keys, OAuth client secrets, SAML certificates, mTLS certificates revoked at the firm-side identity provider and at the vendor.
- **Privileged-access tokens** — vendor-side privileged accounts and just-in-time access grants disabled at cutover; vendor-personnel-side firm credentials disabled at firm IdP.
- **Network paths** — VPN tunnels decommissioned; private-link or PrivateLink endpoints torn down; firewall rules removed; DNS records updated.

#### Access-revocation choreography

- **Sequencing** — revocation is sequenced against cutover, not before. Premature revocation can strand in-flight data; late revocation extends the residual-access window.
- **Vendor-personnel access** — list of vendor personnel with firm-system access; offboarding choreography per role.
- **Firm-personnel access to vendor** — firm-personnel access to vendor systems revoked on cutover plus the agreed support tail.
- **Federated identity** — SSO and SCIM teardown; trust relationships removed.

#### Vendor-side destruction certification

- **Form** — signed certificate of destruction is the minimum; for higher-risk arrangements, expect log-evidence and a third-party-attestation option.
- **Scope** — the destruction obligation must cover all data categories in `data_access`, including derivative artifacts (cached data, indexes, vector embeddings for AI vendors, model fine-tune artifacts, abuse-monitoring retention windows, log archives).
- **Carve-outs** — lawful retention by the vendor (regulatory archive, fraud investigation, legal hold) carved out explicitly with the retention period and the post-retention destruction commitment named.
- **Firm-side retention** — the destruction certificate retained at the firm per the firm's vendor-record-retention policy.

#### SEC cyber-disclosure exposure on a forced or contested termination

- **Materiality** — where the firm is a publicly-listed registrant and the vendor incident driving exit is material to the firm's investors, Item 1.05 Form 8-K obligations attach. The cyber overlay must surface the firm's 8-K timing against the vendor's incident-notification clock.
- **Reg S-K Item 106** — annual disclosure of cybersecurity risk-management; a vendor exit driven by an incident may shift the firm's disclosure on third-party risk-management.
- **Coordination with the firm's disclosure committee** — the operational-resilience function and the disclosure committee must be in the same conversation on a forced or contested termination.

#### SIEM and DLP cutover

- **SIEM integration** — vendor-side log feeds disconnected; substitute-vendor feeds connected; alert-rule baseline re-tuned for the substitute.
- **DLP rules** — DLP rules referencing the outgoing vendor's domains, IP ranges, and integration paths updated for the substitute.
- **SOC playbooks** — incident-response playbooks updated to the substitute vendor's incident-response contacts and clocks.
- **Threat-intelligence feeds** — vendor-specific TI feeds disconnected; substitute feeds (where applicable) connected.

#### AI vendor cyber considerations

When `ai_vendor=true`:

- **Prompt and completion log destruction** — vendor-side abuse-monitoring retention windows must be honoured first; destruction certified once the windows close.
- **Vector index and embedding destruction** — RAG-vendor exits must include destruction of vector indices and embeddings derived from firm content.
- **Fine-tune artifact destruction** — vendor-side fine-tune weights, adapter weights, and training-job artifacts must be destroyed unless contractually returned.
- **Model-version pin handling** — the deployed checkpoint at termination; whether a final-version export is contractually available and what cyber-control posture applies to the exported artifact at the firm.
- **Agent tool revocation** — for agentic vendors, revoking the action-authorisation surface (function-calling endpoints, tool whitelists, MCP-server connections) is part of the cutover.
- **Substitute-vendor cyber posture** — the substitute model vendor's diligence pack covers prompt-injection defence, data-handling posture, eval-coverage posture; the exit plan calls for the substitute pack as a precondition.

#### Common cyber-overlay pitfalls in exit planning

- Treating data extraction as solved by "we have an export API". Format integrity, volume, schema, and validation against firm-of-record are all part of the cyber-overlay read.
- Sequencing revocation before cutover and stranding in-flight data.
- Skipping fourth-party access. Vendor's subcontractors may also hold firm credentials or data; the destruction obligation should reach them.
- Treating the destruction certificate as the end of the work. Firm-side retention of the certificate, the destruction-evidence log, and the post-validation hold all matter.
- Skipping the SEC 8-K timing read on a forced or contested termination at a publicly-listed registrant.
- Skipping the SIEM, DLP, and SOC playbook cutover and discovering the gaps after a substitute-vendor incident.
- Treating an AI-vendor cyber cutover as identical to a non-AI cutover. Vector indices, embeddings, prompt logs, fine-tune artifacts, and agent-tool revocation are AI-specific.

## privacy

### Privacy cross-cutting overlay — exit-plan

When the scope flags privacy, or whenever the vendor processes nonpublic personal information, protected health information, biometric data, customer prompts, or any other regulated personal data at termination, load this overlay. Privacy is in scope by default for AI vendors processing customer prompts and for any vendor whose return-and-destruction obligations touch regulated data.

#### Operative anchors

- **GLBA Safeguards Rule (16 CFR Part 314 as amended)** — §314.4(f) service-provider obligations including secure data-handling on termination of the relationship. The financial-institution covered entity remains responsible for the lawful disposition of customer information regardless of which vendor holds it.
- **GLBA Privacy Rule (Regulation P, 12 CFR Part 1016)** — privacy-notice and information-sharing posture; on termination, the financial institution must continue to honour customer privacy elections (opt-outs, sharing limitations) at the substitute service provider.
- **HIPAA Privacy Rule (45 CFR Parts 160, 164 Subpart E) and Security Rule (45 CFR Parts 160, 164 Subpart C)** — business-associate-agreement transition. PHI return or destruction is a BAA term; the BAA must address transition. Where return is infeasible, the BAA continues to apply to the retained PHI.
- **HIPAA Breach Notification Rule (45 CFR Part 164 Subpart D)** — breach-notification chain continues to apply through transition; an incident discovered during or after transition that involves PHI held by the outgoing vendor still triggers the notification chain.
- **State privacy laws** — CCPA / CPRA (California), VCDPA (Virginia), CTDPA (Connecticut), and the rolling list of state comprehensive privacy laws. Service-provider deletion and return obligations on termination vary; pin by state of the firm's customer footprint.
- **NAIC Insurance Data Security Model Law (Model #668), §4.F** (insurance only) — for insurance carriers, transition data-handling expectations.
- **NYDFS 23 NYCRR Part 500.11** — third-party security covers privacy considerations within the cyber-program frame; close-out assessment posture applies.
- **SEC Reg S-P (May 2024 amendments)** [verify exact compliance dates] — for advisers, BDs, and funds: customer-information-safeguarding and treatment-of-customer-information obligations on termination of a service-provider arrangement; service-provider written-contract requirements including breach-notification.

#### Data return and destruction obligations

- **Return-then-destroy** — the standard pattern: vendor returns data in the agreed format and certifies destruction of remaining copies (and derivative artifacts). The destruction certificate is retained by the firm.
- **Destroy-only** — used where return is not in scope (vendor only processed transient data) or where the substitute already holds the data via a parallel feed.
- **Lawful retention carve-outs** — regulatory archive, fraud investigation, legal hold, anti-abuse retention windows. Each carve-out named, the retention period stated, and the post-retention destruction commitment carried in the contract.
- **Derivative artifacts** — caches, indexes, vector embeddings, model fine-tune artifacts, log archives, backup-to-tape rotations, BCDR-replication copies. The destruction obligation should reach all of these explicitly.

#### State-privacy-law deletion and return

- **CCPA / CPRA service-provider obligations** — a service provider must delete customer personal information at the business's direction on termination, subject to permitted retention exceptions. The exit plan must trigger the deletion direction at cutover and obtain the destruction confirmation.
- **VCDPA / CTDPA / and others** — similar deletion and return obligations; pin by state.
- **GLBA exemption interaction** — GLBA-covered data is excluded from many state privacy laws but not all; the privacy overlay reads the GLBA-exemption scope state-by-state for the vendor's scope of processing.

#### Cross-border data flows during transition

- **Region-pin continuity** — if the contract pins data residency, the transition must not move data across the pinned border. Where the substitute is in a different region, customer-notice and (potentially) regulatory-notification obligations attach.
- **EU / UK GDPR transfers** — where the firm is in the EEA / UK and the substitute is in a third country, the SCCs / IDTA / UK Addendum or other transfer mechanism re-papered.
- **FFIEC and bank-regulator considerations** — cross-border data flow changes on transition may require supervisory engagement at banks.

#### HIPAA business-associate transition

- **PHI return-or-destruction** — the BAA must address what happens to PHI on termination. Return-then-destroy is the default; destroy-only with retained BAA effect on the retained PHI is the alternate where return is infeasible.
- **Breach-notification chain** — the 60-day clock runs from discovery, not from termination; an incident discovered after termination affecting PHI held by the outgoing vendor is still a notifiable event.
- **Substitute BA** — the substitute vendor's BAA must be in place before PHI moves; the substitute's HIPAA Security Rule posture is part of the substitute's diligence.
- **Subcontractor-BA chain** — the outgoing vendor's subcontractor BAs continue to apply to retained PHI under any lawful retention.

#### Customer privacy elections continuity

- **Opt-out and sharing-limitation flags** — customer-elected privacy flags must carry over to the substitute or be re-collected. Re-collection without notice is itself a privacy violation under several state laws.
- **Data-subject-rights handling** — access, deletion, correction, opt-out request handling must continue through the transition; the substitute must accept the firm's existing rights-handling protocol.

#### AI vendor privacy considerations

When `ai_vendor=true`:

- **Prompts and completions** — destruction of prompt logs and completion logs at the vendor, including any abuse-monitoring retention windows once the windows close. Destruction certificate must cover the abuse-monitoring window explicitly.
- **Training and fine-tune data** — destruction of any data used in vendor-side fine-tuning unless contractually returned.
- **Vector embeddings and RAG indices** — destruction of any vector representations of firm content; embeddings can be reverse-engineered into source content under some conditions and are personal data where they encode personal information.
- **Output retention** — model outputs derived from PHI inherit PHI status under HIPAA. Output destruction is a HIPAA business-associate question on transition.
- **Right-to-deletion against an LLM** — implementing a deletion request against a model that has incorporated firm content is technically open. The contract should address how the vendor will support the firm's response to a deletion request when the data may have flowed through training, fine-tuning, or retention windows. Where the vendor cannot support deletion against the model, the customer-facing communication on the firm's side must reflect that.
- **Cross-border prompt-processing** — region-pinning enforcement on the substitute vendor; transition does not relieve the residency obligation.

#### Cross-link inside the plugin

- **`vendor-diligence` privacy overlay** carries the diligence inputs the exit plan reads via the diligence record (`data_access`, sub-processor list, BAA status).
- **`contract-gap-review` privacy overlay** carries the data-return and data-destruction clause set, the BAA terms, and the breach-notification clock language; gaps surfaced here flag the exit-readiness gap.

#### Common privacy-overlay pitfalls in exit planning

- Treating data return as solved by an export API. Customer privacy elections, derivative artifacts, and lawful retention carve-outs all need explicit handling.
- Skipping the BAA transition on a HIPAA arrangement. Return-or-destruction posture, breach-notification chain continuity, and substitute BA are all required.
- Treating vendor-side destruction as the end of the obligation. The destruction certificate, the firm-side retention of the certificate, and the post-validation hold all matter.
- Missing the cross-border read on a transition that moves data across a residency pin.
- Skipping customer-privacy-elections continuity. Opt-outs and sharing-limitation flags are operative consumer protections, not metadata.
- Treating AI-vendor data destruction as identical to non-AI. Prompts, completions, embeddings, fine-tune artifacts, and model output retention are AI-specific.
- Missing the right-to-deletion implementability question against an LLM.
- Treating GLBA exemption as blanket exemption from a state privacy law on a vendor-transition.
