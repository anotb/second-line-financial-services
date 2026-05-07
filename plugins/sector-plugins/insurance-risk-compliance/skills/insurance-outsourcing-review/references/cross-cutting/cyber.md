# Cyber cross-cutting overlay — insurance-outsourcing-review

Load this overlay whenever the outsourced function touches the carrier's information systems, policyholder data, claims data, or any control on the carrier's cybersecurity-program perimeter. Cyber is in scope by default for any TPA, claims administrator, IT outsourcer, or data-processing outsourcer.

## Operative anchors

- **NAIC Insurance Data Security Model Law, Model #668**. The insurance-specific cybersecurity frame. The carrier's Information Security Program (ISP) under §4 carries through to its third-party service providers under §4.F: due diligence before contract, written-contract terms, ongoing monitoring, incident-response cooperation, breach-notification chain. Adoption state-by-state; consult the NAIC adoption tracker for the operating-footprint read.

- **NYDFS 23 NYCRR Part 500.11**. Where the carrier is a NYDFS Covered Entity, 500.11 reach extends to vendor diligence directly: identification, risk assessment, minimum cybersecurity practices, due diligence, periodic assessment. In the operating footprint, §500.11 may run alongside Model #668 or in place of it depending on state of license and entity type.

- **§4.F obligations against the counterparty**. Read in five layers: due-diligence-before-contract evidence; the operative written-contract clause set; ongoing monitoring posture; incident-response cooperation language; the breach-notification clock from the counterparty up to the carrier and onward to the carrier's regulators. Each layer takes a status (`present | partial | missing`) and a citation. Mark `[verify section]` where the exact subsection of §4.F is not confirmed.

## Insurance-specific cyber considerations

- **Cedent breach-notification chain**. The counterparty notifies the carrier; the carrier notifies its regulators. The carrier's downstream clocks (state DOI notification clocks, NYDFS 72-hour clock where applicable, SEC Item 1.05 8-K clock for publicly-listed insurers) drive the contract-side clock the counterparty owes. A counterparty's preferred clock that does not preserve the carrier's downstream clocks is a finding.

- **Sub-processor visibility**. Under §4.F the carrier is on the hook for the sub-processor's practices in many states. Notice-without-consent on sub-processor changes is a frequent contract gap; flag it as a control finding rather than a notification mechanic.

- **Information-system-access posture**. Where the counterparty has system access (claims systems, policy administration systems, data marts), identity and access controls (SSO, SCIM, PAM, JIT for support staff) and logging exportability into the carrier's SIEM are part of the §4.F monitoring obligation.

- **AI tool cyber posture**. Where the counterparty has deployed AI on the carrier's policies, model-supply-chain integrity (model-version pinning, deprecation notice, provenance), prompt-injection defence boundary, and tool-use sandboxing for agentic systems are part of the cyber read. Cross-cite the vendor-AI section in the sector overlay.

## Evidence the cyber overlay expects

- The counterparty's Information Security Program documentation, scoped against §4.F.
- SOC 2 Type II report with scope, period, exceptions, and complementary user-entity controls (CUECs) — relevant where the counterparty is a recognised auditable provider.
- Penetration-test summary current within the carrier's policy window.
- Vulnerability-management evidence (cadence, MTTR by severity, exception register).
- Incident-response runbook with the cedent-notification chain populated.
- Breach history including public disclosures, regulator actions, and aging.

## Common cyber-overlay pitfalls

- Reading the counterparty's SOC 2 as the §4.F evidence pack. Different audience, different scope; SOC 2 may inform §4.F but does not substitute.
- Setting the counterparty's breach-notification clock to the counterparty's preferred clock instead of to the carrier's downstream regulator clocks.
- Treating sub-processor change-notice as a sufficient §4.F control when the model law expects monitoring of the sub-processor's practices.
- Assuming Model #668 applies where the operating footprint includes a non-adopting state — confirm against the NAIC adoption tracker, and pivot to the state-specific cyber frame (often NYDFS 500 or a state DOI bulletin) where #668 is not adopted.
