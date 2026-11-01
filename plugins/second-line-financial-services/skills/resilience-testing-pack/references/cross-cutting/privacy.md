# Privacy cross-cutting overlay — resilience-testing-pack

When the scope flags privacy, or whenever the testing pack involves scenarios that may surface personal data exposure, load this overlay. Privacy is in scope by default for AI vendors and for any vendor or IBS holding NPI, PHI, PCI, or other regulated data.

## Operative anchors

- **GLBA Safeguards Rule, 16 CFR Part 314** as amended (FTC, December 2021 amendments effective 2023). §314.4(h) incident-response programme; the testing pack's incident-response scenarios feed Safeguards-Rule compliance evidence.
- **GLBA Privacy Rule, 12 CFR Part 1016 (Regulation P)** — customer-information-safeguarding obligations.
- **HIPAA Privacy Rule (45 CFR Parts 160, 164 Subpart E) and Security Rule (45 CFR Parts 160, 164 Subpart C)** — business-associate breach-notification obligations; testing scenarios involving PHI carry the BAA-incident-notification clock.
- **State privacy laws** with breach-notification statutes (CCPA / CPRA, Colorado, Connecticut, Virginia, Utah, Washington, others). State-by-state notification clocks are a test-design constraint where the scenario surfaces real cross-state customer impact.
- **NYDFS 23 NYCRR Part 500.17** — cybersecurity event notification (72-hour clock in many cases). For NYDFS Covered Entities, the testing scenario's notification rehearsal feeds Part 500.17 readiness.
- **EU GDPR (Regulation (EU) 2016/679)** Article 33 (notification to supervisory authority within 72 hours) and Article 34 (notification to data subjects). For EU-licensed entities and entities processing EU-resident data, the notification clocks are test-design constraints.
- **EU AI Act (Regulation (EU) 2024/1689)** Article 26 incident-reporting for high-risk AI systems [verify article number]. Where an AI scenario in the testing pack surfaces a high-risk AI-system incident, the EU AI Act notification path applies in addition to GDPR.

## Privacy-impact scenarios common in resilience testing

- Data-loss event during a vendor-side outage (vendor loses firm customer data).
- Accidental cross-border transfer during a failover (failover region routes data outside contractually permitted geographies).
- Vendor-side incident exposing customer prompts or model outputs (AI vendors specifically).
- Backup-restore incident: stale or incorrect data restored after a recovery action.
- Customer data leakage in a test artefact (test logs containing real customer data).
- Vendor-side abuse-monitoring incident exposing firm prompts to vendor staff (AI vendors).
- BAA-vendor incident at a covered entity (HIPAA scenario).

## Test-design constraints from privacy

- **Notification-clock rehearsal**: scenarios that simulate a real notification-clock decision (GLBA Safeguards, HIPAA, GDPR, NYDFS 500.17, state breach-notification statutes) carry the rehearsal as a test artefact, not as a real notification.
- **Data minimisation in test artefacts**: test artefacts (logs, screenshots, observer notes) must avoid real customer-PII to the degree possible. Where real PII is in scope (forensic-evidence rehearsal), preservation choreography respects data-minimisation.
- **Cross-border data flow during test**: a tested-failover that routes data to a region the contract does not permit must be flagged as a test-design defect, not papered over.
- **Test-artefact retention**: privacy obligations on test artefacts containing PII (deletion at end of retention, access controls, audit logs).
- **Customer-comms during test**: any customer-facing communication during a test that surfaces real customer impact must comply with the customer-comms standards in the operative regulation.

## Safety controls for privacy-scenario tests

- **PII redaction** in test prompts and inputs where AI-vendor scenarios are in scope.
- **Test-environment isolation** where possible (use a non-production tenant or sandboxed environment).
- **Real-incident exit trigger** if the test surfaces a real PII-exposure event.
- **DPO and counsel coordination** for any test that may surface real notification decisions.

## AI-vendor privacy considerations in testing

When `ai_in_scope=true`:

- Customer prompts as customer data — any scenario involving prompt-handling carries the data-handling obligations of the contained content (NPI, PHI, PCI as applicable).
- Vendor-side training-data posture — scenarios testing whether the vendor's training-data exclusions hold.
- Vendor-side abuse-monitoring posture — scenarios testing the abuse-monitoring exception's privacy posture.
- HIPAA business-associate posture — for AI vendors that may receive PHI through prompts, BAA-incident-notification rehearsal.
- Cross-border-AI-vendor scenario — where the AI vendor processes data outside contractually permitted geographies during failover.

## Cross-link inside the plugin

- **`vendor-diligence` privacy overlay** carries the diligence depth on vendor privacy posture that the testing pack consumes.
- **`exit-plan` privacy overlay** for privacy-cutover choreography on termination.

## Common privacy-overlay pitfalls in resilience testing

- Letting test artefacts capture real customer PII unnecessarily; data minimisation applies.
- Skipping the notification-clock rehearsal on a scenario that would have surfaced one in real life.
- Treating a tested-failover that crosses a contractually-prohibited region as a successful failover.
- Skipping DPO and counsel coordination on a test that may surface real notification decisions.
- Treating AI-vendor prompt-handling as outside privacy scope. Customer prompts are customer data.
- Skipping the BAA-incident rehearsal at a HIPAA-covered entity using an AI vendor that may receive PHI.
- Forgetting state breach-notification clocks in a multi-state customer-impact scenario; the operative state clock controls per the customer's state of residence.
