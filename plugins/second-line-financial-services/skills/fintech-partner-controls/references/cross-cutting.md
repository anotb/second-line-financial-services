# cross-cutting

One section per topic. Read only the sections the scope calls for.

## cyber

### Cross-cutting overlay — cyber

Default-on for substantively every payments program. The sponsor bank carries a 36-hour prudential cyber-notification clock and pushes a tighter contractual clock down to the program operator; the operator's cyber posture is therefore inspectable through the sponsor bank's TPRM file. The overlay carries the cyber-row content for the inventory and the sponsor-bank-cyber-notification-chain detail for the program-agreement control map.

The overlay does not substitute for the deep-dive in `cyber-disclosure-readiness` (with the payments-fintech overlay where the firm or its sponsor bank is a public registrant) or for the incident workflow in `payment-operations-incident-review`. The pack raises the flag and points to the deep-dive.

#### Anchor frame — the sponsor bank's cyber expectations

- **Computer-Security Incident Notification Rule** — 12 CFR Part 53 (OCC), 12 CFR Part 225 Subpart N (FRB), 12 CFR Part 304 Subpart E (FDIC), effective May 1, 2022. The sponsor bank must notify its primary federal regulator within 36 hours of determining that a notification incident has occurred. The program operator's incident-detection and notification posture is timed against this 36-hour window — the sponsor bank cannot meet its 36-hour clock if the operator does not deliver the determination in time. The program-agreement clause set typically pushes a tighter contractual notification clock onto the operator (often 24 hours or less). The pack confirms the contractual clock and the operational capability to meet it.
- **NYDFS 23 NYCRR Part 500** including §500.17(a) cybersecurity-event notification clock (72 hours). Applies to NYDFS Covered Entities. Many fintechs are Covered Entities by virtue of NY footprint; many sponsor banks are Covered Entities and require equivalent posture from the operator through the program agreement.
- **GLBA Safeguards Rule, 16 CFR Part 314** as amended (FTC, December 2021 amendments effective 2023). §314.4(f) service-provider obligations — the sponsor bank passes its GLBA obligation through to the operator under the program agreement. §314.4(h) incident-response.
- **GLBA Privacy Rule / Reg P, 12 CFR Part 1016**.
- **FFIEC IT Examination Handbook — Information Security booklet** (verify current edition and section). The sponsor bank's IT examiners read against this booklet; the operator's posture must be inspectable on the same terms.
- **FFIEC Authentication and Access to Financial Institution Services and Systems Guidance** (August 11, 2021) [verify section].
- **SEC cybersecurity disclosure** — Item 1.05 of Form 8-K and Reg S-K Item 106 (effective 2023 — verify exact compliance dates by registrant size). Applies where the firm or its sponsor bank is a public registrant.
- **State breach-notification statutes** — state-by-state; verify per state in the geographic footprint.

#### Sponsor-bank cyber-notification chain

This is the operative control on the operator side.

The sponsor bank's 36-hour clock starts at "determination that a notification incident has occurred". The operator's contractual clock to the sponsor bank typically starts at "detection" or "reasonable basis to believe". The operator's controls inventory carries:

- The contractual notification clock named (often 24 hours or less to the sponsor bank's incident-management contact).
- The operational capability to meet that clock — incident-classification playbook with sponsor-bank-notification trigger criteria; out-of-hours escalation; primary and backup contacts at the sponsor bank.
- The reconciliation between the operator's NYDFS clock (where applicable), the operator's state-breach clocks, and the sponsor-bank contractual clock — the sponsor-bank clock is typically the first to fire and drives the cascade.
- Tabletop-exercise cadence with the sponsor bank, evidenced by the most-recent exercise log.

#### What the overlay puts into the inventory

In the **cyber and resilience controls** row of the inventory: cyber-notification-clock control (with the contractual clock as the threshold and the most-recent test as the evidence); BCP / DR coverage control (with the most-recent tabletop log as the evidence); third-party / fourth-party register control (with the current vendor-inventory file as the evidence); vendor-stack SOC 2 currency control (with the most-recent SOC 2 report per critical vendor as the evidence).

In the **subcontractor and fourth-party register**: each material vendor's most-recent SOC 2 Type II report, audit period, qualified opinion or exceptions, and remediation status. The sponsor bank's TPRM team treats these as fourth parties to its relationship with the operator.

In the **sponsor-bank reporting cadence**: cyber posture report (monthly) and incident-history summary (rolling 12 months) feed the sponsor-bank operating committee and the sponsor bank's CISO function.

#### What evidence the sponsor bank's TPRM team will request

A short list, drawn from the sponsor-bank TPRM intake patterns observed in 2023-26:

- The operator's most-recent SOC 2 Type II report (audit period, opinion, exceptions, remediation status). Where the operator does not yet have a SOC 2, the equivalent third-party assurance report.
- The operator's vendor-stack SOC 2 currency map (each critical vendor's most-recent report).
- The operator's incident-response plan with the sponsor-bank-notification playbook attached.
- The operator's most-recent tabletop-exercise log including exercises run jointly with the sponsor bank.
- The operator's vulnerability-management cadence and the most-recent penetration-test report.
- The operator's customer-managed key posture and the encryption-in-transit and encryption-at-rest evidence.

Read SOC 2 as a baseline, not a substitute for evidence on incident-response cooperation terms or the operator's own customer-managed key posture; the sponsor bank's CISO function will ask for both.

#### Common pitfalls

- Reading cyber as a vendor-stack tickbox rather than as an operational-resilience and sponsor-bank-notification posture.
- Missing the 36-hour sponsor-bank prudential clock and the implied contractual-clock-on-the-program-operator. The pack must name both.
- Treating SOC 2 Type II as a substitute for the firm's own evidence on customer-managed key posture, vulnerability-management cadence, or incident-response cooperation terms.
- Omitting the public-registrant disclosure leg where the sponsor bank is a public registrant subject to SEC Item 1.05.
- Naming a contractual clock that the operator's incident-classification playbook cannot meet. The capability evidence is the operative control, not the clock written in the agreement.

## privacy

### Cross-cutting overlay — privacy

Default-on where customer NPI flows for fraud and AML monitoring beyond baseline (most programs once monitoring vendors are in the stack). The lens here is the sponsor bank's GLBA posture on the customer data the operator handles on the bank's behalf, which the sponsor bank is on the hook for under its own GLBA obligations.

The overlay does not substitute for a state-by-state privacy-law inventory, which is its own work product. The pack names the operative regimes and the controls and points to deeper review where the firm's footprint demands it.

#### Anchor frame — the sponsor bank's privacy expectations on the operator

- **GLBA Safeguards Rule, 16 CFR Part 314** as amended (FTC, December 2021 amendments effective 2023). §314.4(a)-(h) program elements; §314.4(f) service-provider obligations — the sponsor bank's most direct hook into the operator's data-handling posture; §314.4(h) incident-response. The sponsor bank treats the operator as a service provider under §314.4(f) and pushes the program elements through the program agreement.
- **GLBA Privacy Rule / Reg P, 12 CFR Part 1016**. Consumer-information privacy notice; opt-out mechanics; sharing limits. Where the fintech surface presents the deposit-like product, the privacy notice runs through the sponsor bank as the FI of record; the operator's surface-level disclosure must be consistent.
- **CFPB Personal Financial Data Rights Final Rule under §1033** (October 22, 2024 — verify Federal Register citation, exact citation, implementation tier dates, and current docket status). Where the program operator is a data provider or data recipient, §1033 obligations include secondary-use limits, retention-and-deletion duties, and consent-revocation paths.
- **CCPA / CPRA — California Consumer Privacy Act as amended, Cal. Civ. Code §1798.100 et seq.** Where the operator has California consumers in its book.
- **State privacy laws** — verify state-by-state per the geographic footprint. Active comprehensive privacy laws include (incomplete; verify currency on the analysis date) Virginia (VCDPA), Colorado (CPA), Connecticut (CTDPA), Utah (UCPA), Texas (TDPSA), Oregon (OCPA), Montana (MTCDPA).
- **NYDFS 23 NYCRR Part 500** — privacy and security overlap.

#### Sponsor-bank GLBA flow-down

The sponsor bank's GLBA Safeguards obligation does not stop at the bank's perimeter. Under §314.4(f), the bank takes reasonable steps to select and retain service providers capable of maintaining appropriate safeguards and contractually requires service providers to implement and maintain such safeguards. The program agreement clause set carries this through to the operator. The pack evidences:

- The §314.4 program-element posture inside the operator (written information-security program, designated qualified individual, risk assessment, access controls, multi-factor authentication, encryption, incident-response, training, service-provider oversight on the operator's own subcontractors).
- The sponsor bank's right to review the operator's GLBA program annually.
- The flow-down of GLBA expectations to the operator's subcontractors (fourth parties from the bank's perspective).

#### What the overlay puts into the inventory

In the **customer-protection controls** row: privacy-notice consistency control (the operator's surface-level privacy framing consistent with the sponsor bank's GLBA notice; evidence is the rendered surface read against the bank's notice). DSAR / consumer-rights handling control where state regimes apply.

In the **subcontractor and fourth-party register**: each material vendor's data-processing agreement coverage, secondary-use exception scope (model-improvement, benchmarking, anonymous-aggregate use), and the operator's audit cadence on vendor data handling.

In the **program-agreement control map**: the customer-data ownership clause, the post-termination data-handling clause, the §1033 implications where the operator is a covered data provider, the GLBA flow-down clause.

#### §1033 status note

Repeat. Where the program operator is a data provider under §1033 (most consumer-account programs), the pack names the data-provider obligations, the implementation tier date for the firm, and the cross-link to `open-banking-data-controls` for the deeper review. Where the program operator is a data recipient (typically aggregator-fed analytics), the cross-link is to `open-banking-data-controls`. Verify the current docket status on each engagement and date-stamp the citation; the rule was finalised October 2024 but the docket has been active and tier dates may have shifted.

#### Common pitfalls

- Treating GLBA as the sponsor bank's problem because the depository is the bank. Under §314.4(f), the bank is on the hook for the operator's posture; the operator must be inspectable on the same terms.
- Treating vendor data-processing agreements as evidence of operational compliance rather than as contractual baseline; DPA coverage and DPA-vs-actual reconciliation are separate questions.
- Missing secondary-use exception scope in monitoring-vendor contracts (model-improvement, benchmarking, anonymous-aggregate use). The sponsor bank's privacy team will ask.
- Defaulting the §1033 status to "we will be ready" without naming the firm's tier and implementation-date posture.
- Missing the state regime in CA, VA, CO, and others where the program operator falls under the threshold and the sponsor bank does not (CCPA / CPRA applies to many fintechs by virtue of revenue and California-resident book even when the sponsor bank does not meet the same threshold).
