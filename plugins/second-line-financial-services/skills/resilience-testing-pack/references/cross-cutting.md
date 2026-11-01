# cross-cutting

One section per topic. Read only the sections the scope calls for.

## cyber

### Cyber cross-cutting overlay — resilience-testing-pack

When the scope flags cyber, or whenever the testing pack covers a vendor or IBS where a cyber-event is in the scenario set, load this overlay. Cyber is in scope by default for AI vendors and for any IBS reaching NPI, PHI, PCI, customer prompts, or important-business-service controls.

#### Operative anchors

- **NYDFS 23 NYCRR Part 500.16** — incident-response-plan testing obligation. Periodic testing of the incident-response plan is an explicit obligation for Covered Entities.
- **NYDFS 23 NYCRR Part 500.11** — third-party-service-provider security policy; periodic-assessment expectation includes test posture.
- **FFIEC IT Examination Handbook — Information Security booklet** [verify current edition] — examiner-facing detail on incident-response testing.
- **SEC final rule on cybersecurity disclosure** — Item 1.05 Form 8-K and Reg S-K Item 106 (effective 2023). For publicly-listed registrants, a cyber-incident scenario in the testing pack should consider how a real-incident materiality assessment would run; the test is part of the firm's preparation for the four-business-day disclosure clock.
- **Reg S-P (May 2024 amendments)** [verify exact compliance dates by entity type and size] — for advisers, BDs, and funds, customer-information-safeguarding incident-response testing.
- **CISA shared-responsibility model for cloud** — for cloud-vendor scenarios, the responsibility split through an incident must be evidenced; the test rehearses both sides of the split.
- **TIBER-EU framework (ECB)** [verify current version] for TLPT methodology where the firm is in scope under DORA Article 26 [verify subarticle].
- **CBEST framework (Bank of England)** [verify current version] for advanced testing at UK firms in scope.
- **MITRE ATT&CK and CISA tabletop exercise packages** as scenario inputs.

#### Cyber-incident scenarios common across firms

- Ransomware on the vendor (vendor-side encryption of data the firm relies on).
- Vendor supply-chain compromise (vendor's upstream software-component compromise affecting the vendor's services).
- Cloud-control-plane outage (hyperscaler-vendor's control plane disrupted).
- Identity-provider outage (SSO vendor's IdP outage).
- DDoS on the vendor's customer-facing infrastructure.
- Insider-threat at the vendor (vendor-side privileged-access misuse).
- Cryptographic-key exposure at the vendor (HSM-vendor or KMS-vendor incident).
- Vendor-side privacy incident exposing firm customer data.

#### Test design choices for cyber scenarios

- **Tabletop**: most cyber-event scenarios run as tabletop in the first cycle. Scenarios that require coordination with the firm's CSIRT, the supervisor, the disclosure committee (for publicly-listed registrants), and external counsel run well as tabletop.
- **Walkthrough**: incident-response plan walkthrough cycles step-by-step through the IRP for a defined scenario. NYDFS 500.16 IRP testing usually runs as a walkthrough at minimum.
- **Partial-simulation**: tested-failover for IdP cutover or for a tested-substitute KMS-vendor cutover. Partial-simulation requires safety controls to avoid stranding live workloads.
- **TLPT / red-team**: under TIBER-EU or CBEST, advanced testing runs as a red-team exercise against the firm's threat model. Legal-and-supervisory engagement is a precondition.
- **Industry-wide tabletop**: sector associations and supervisors run periodic industry-wide tabletop exercises (FS-ISAC and the like). Participation is part of the programme.

#### Safety controls for cyber-scenario tests

- **Real-incident exit trigger**: a test in progress while a real incident is detected gets terminated cleanly.
- **CSIRT confusion control**: the testing notification chain is distinct from the real incident-notification chain to avoid CSIRT confusion.
- **Customer-impact threshold**: any test that may surface real customer-impact (a tested-failover that fails to fail-over cleanly) gets terminated below a defined threshold.
- **Disclosure-committee coordination**: for publicly-listed registrants, the disclosure committee is briefed on test scope so a real incident during the test does not get conflated with simulated artefacts.
- **External-counsel coordination**: any test that may surface privilege issues (incident-response privilege, attorney-client privilege over forensic findings) is pre-coordinated with counsel.

#### Evidence-collection plan additions for cyber scenarios

- Telemetry from the SIEM, the EDR, the firewall, the WAF, the IdP, the KMS where in scope.
- Vendor-side incident-status feeds where the vendor is in the test (vendor's status page, the vendor's incident-notification message).
- Comms-bridge transcript with timestamps.
- IRP-step completion log: for each step in the firm's IRP, time-to-execute and observer note.
- Decisioning log for any disclosure-decision rehearsal (publicly-listed registrants).
- Forensic-evidence preservation choreography rehearsal where the scenario involves a forensic event.

#### Substitute-vendor cyber posture

For partial-simulation scenarios that exercise a substitute vendor:

- The substitute vendor's diligence pack including cyber posture (SOC 2 Type II, pen-test summary, vulnerability-management evidence, incident-history) is a precondition.
- The substitute vendor's incident-response cooperation posture is tested in the scenario, not assumed.

#### AI-vendor cyber considerations in testing

When `ai_in_scope=true`:

- Prompt-injection attack scenario on the deployed agent (where the firm uses an agentic vendor).
- Vendor-side training-data incident exposing firm content (if the firm's prompts or RAG content were used in training, this is a real exposure).
- Model-evasion scenario where adversarial inputs cause the deployed model to misclassify in a high-impact way.
- Vendor-side abuse-monitoring incident exposing firm prompts to vendor staff.

#### SEC cyber-disclosure rehearsal

For publicly-listed registrants, the testing pack should include at least one scenario that rehearses the materiality-assessment cycle:

- The vendor reports a cyber-incident.
- The firm's disclosure committee assesses materiality against Item 1.05 Form 8-K standards.
- The four-business-day clock is tracked.
- The disclosure draft is prepared (in test) and reviewed by counsel.
- Reg S-K Item 106 implications for the next periodic filing are noted.

The rehearsal is a tabletop. Real disclosure decisions are not made in the test.

#### Cross-link inside the plugin

- **`vendor-diligence` cyber overlay** carries the diligence depth on vendor cyber posture that the testing pack consumes.
- **`exit-plan` cyber overlay** for the cyber-cutover choreography on a forced or contested termination.

#### Common cyber-overlay pitfalls in resilience testing

- Treating cyber tests as separate from operational-resilience tests. They are the same tests, with cyber-specific scenarios.
- Skipping the disclosure-committee rehearsal at a publicly-listed registrant.
- Letting a tabletop scenario become a real CSIRT activation; testing notification chains must be distinct from real notification chains.
- Skipping the substitute-vendor cyber-posture precondition on a partial-simulation that exercises a substitute.
- Treating TLPT as substitutable for tabletop on cyber scenarios; TLPT is its own workstream with its own approver path.
- Treating an AI-vendor cyber scenario as identical to a non-AI scenario. Prompt-injection, model-evasion, training-data incident, abuse-monitoring incident are AI-specific.

## privacy

### Privacy cross-cutting overlay — resilience-testing-pack

When the scope flags privacy, or whenever the testing pack involves scenarios that may surface personal data exposure, load this overlay. Privacy is in scope by default for AI vendors and for any vendor or IBS holding NPI, PHI, PCI, or other regulated data.

#### Operative anchors

- **GLBA Safeguards Rule, 16 CFR Part 314** as amended (FTC, December 2021 amendments effective 2023). §314.4(h) incident-response programme; the testing pack's incident-response scenarios feed Safeguards-Rule compliance evidence.
- **GLBA Privacy Rule, 12 CFR Part 1016 (Regulation P)** — customer-information-safeguarding obligations.
- **HIPAA Privacy Rule (45 CFR Parts 160, 164 Subpart E) and Security Rule (45 CFR Parts 160, 164 Subpart C)** — business-associate breach-notification obligations; testing scenarios involving PHI carry the BAA-incident-notification clock.
- **State privacy laws** with breach-notification statutes (CCPA / CPRA, Colorado, Connecticut, Virginia, Utah, Washington, others). State-by-state notification clocks are a test-design constraint where the scenario surfaces real cross-state customer impact.
- **NYDFS 23 NYCRR Part 500.17** — cybersecurity event notification (72-hour clock in many cases). For NYDFS Covered Entities, the testing scenario's notification rehearsal feeds Part 500.17 readiness.
- **EU GDPR (Regulation (EU) 2016/679)** Article 33 (notification to supervisory authority within 72 hours) and Article 34 (notification to data subjects). For EU-licensed entities and entities processing EU-resident data, the notification clocks are test-design constraints.
- **EU AI Act (Regulation (EU) 2024/1689)** Article 26 incident-reporting for high-risk AI systems [verify article number]. Where an AI scenario in the testing pack surfaces a high-risk AI-system incident, the EU AI Act notification path applies in addition to GDPR.

#### Privacy-impact scenarios common in resilience testing

- Data-loss event during a vendor-side outage (vendor loses firm customer data).
- Accidental cross-border transfer during a failover (failover region routes data outside contractually permitted geographies).
- Vendor-side incident exposing customer prompts or model outputs (AI vendors specifically).
- Backup-restore incident: stale or incorrect data restored after a recovery action.
- Customer data leakage in a test artefact (test logs containing real customer data).
- Vendor-side abuse-monitoring incident exposing firm prompts to vendor staff (AI vendors).
- BAA-vendor incident at a covered entity (HIPAA scenario).

#### Test-design constraints from privacy

- **Notification-clock rehearsal**: scenarios that simulate a real notification-clock decision (GLBA Safeguards, HIPAA, GDPR, NYDFS 500.17, state breach-notification statutes) carry the rehearsal as a test artefact, not as a real notification.
- **Data minimisation in test artefacts**: test artefacts (logs, screenshots, observer notes) must avoid real customer-PII to the degree possible. Where real PII is in scope (forensic-evidence rehearsal), preservation choreography respects data-minimisation.
- **Cross-border data flow during test**: a tested-failover that routes data to a region the contract does not permit must be flagged as a test-design defect, not papered over.
- **Test-artefact retention**: privacy obligations on test artefacts containing PII (deletion at end of retention, access controls, audit logs).
- **Customer-comms during test**: any customer-facing communication during a test that surfaces real customer impact must comply with the customer-comms standards in the operative regulation.

#### Safety controls for privacy-scenario tests

- **PII redaction** in test prompts and inputs where AI-vendor scenarios are in scope.
- **Test-environment isolation** where possible (use a non-production tenant or sandboxed environment).
- **Real-incident exit trigger** if the test surfaces a real PII-exposure event.
- **DPO and counsel coordination** for any test that may surface real notification decisions.

#### AI-vendor privacy considerations in testing

When `ai_in_scope=true`:

- Customer prompts as customer data — any scenario involving prompt-handling carries the data-handling obligations of the contained content (NPI, PHI, PCI as applicable).
- Vendor-side training-data posture — scenarios testing whether the vendor's training-data exclusions hold.
- Vendor-side abuse-monitoring posture — scenarios testing the abuse-monitoring exception's privacy posture.
- HIPAA business-associate posture — for AI vendors that may receive PHI through prompts, BAA-incident-notification rehearsal.
- Cross-border-AI-vendor scenario — where the AI vendor processes data outside contractually permitted geographies during failover.

#### Cross-link inside the plugin

- **`vendor-diligence` privacy overlay** carries the diligence depth on vendor privacy posture that the testing pack consumes.
- **`exit-plan` privacy overlay** for privacy-cutover choreography on termination.

#### Common privacy-overlay pitfalls in resilience testing

- Letting test artefacts capture real customer PII unnecessarily; data minimisation applies.
- Skipping the notification-clock rehearsal on a scenario that would have surfaced one in real life.
- Treating a tested-failover that crosses a contractually-prohibited region as a successful failover.
- Skipping DPO and counsel coordination on a test that may surface real notification decisions.
- Treating AI-vendor prompt-handling as outside privacy scope. Customer prompts are customer data.
- Skipping the BAA-incident rehearsal at a HIPAA-covered entity using an AI vendor that may receive PHI.
- Forgetting state breach-notification clocks in a multi-state customer-impact scenario; the operative state clock controls per the customer's state of residence.
