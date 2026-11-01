# cross-cutting

One section per topic. Read only the sections the scope calls for.

## cyber

### Cyber cross-cutting overlay — insurance-outsourcing-review

Load this overlay whenever the outsourced function touches the carrier's information systems, policyholder data, claims data, or any control on the carrier's cybersecurity-program perimeter. Cyber is in scope by default for any TPA, claims administrator, IT outsourcer, or data-processing outsourcer.

#### Operative anchors

- **NAIC Insurance Data Security Model Law, Model #668**. The insurance-specific cybersecurity frame. The carrier's Information Security Program (ISP) under §4 carries through to its third-party service providers under §4.F: due diligence before contract, written-contract terms, ongoing monitoring, incident-response cooperation, breach-notification chain. Adoption state-by-state; consult the NAIC adoption tracker for the operating-footprint read.

- **NYDFS 23 NYCRR Part 500.11**. Where the carrier is a NYDFS Covered Entity, 500.11 reach extends to vendor diligence directly: identification, risk assessment, minimum cybersecurity practices, due diligence, periodic assessment. In the operating footprint, §500.11 may run alongside Model #668 or in place of it depending on state of license and entity type.

- **§4.F obligations against the counterparty**. Read in five layers: due-diligence-before-contract evidence; the operative written-contract clause set; ongoing monitoring posture; incident-response cooperation language; the breach-notification clock from the counterparty up to the carrier and onward to the carrier's regulators. Each layer takes a status (`present | partial | missing`) and a citation. Mark `[verify section]` where the exact subsection of §4.F is not confirmed.

#### Insurance-specific cyber considerations

- **Cedent breach-notification chain**. The counterparty notifies the carrier; the carrier notifies its regulators. The carrier's downstream clocks (state DOI notification clocks, NYDFS 72-hour clock where applicable, SEC Item 1.05 8-K clock for publicly-listed insurers) drive the contract-side clock the counterparty owes. A counterparty's preferred clock that does not preserve the carrier's downstream clocks is a finding.

- **Sub-processor visibility**. Under §4.F the carrier is on the hook for the sub-processor's practices in many states. Notice-without-consent on sub-processor changes is a frequent contract gap; flag it as a control finding rather than a notification mechanic.

- **Information-system-access posture**. Where the counterparty has system access (claims systems, policy administration systems, data marts), identity and access controls (SSO, SCIM, PAM, JIT for support staff) and logging exportability into the carrier's SIEM are part of the §4.F monitoring obligation.

- **AI tool cyber posture**. Where the counterparty has deployed AI on the carrier's policies, model-supply-chain integrity (model-version pinning, deprecation notice, provenance), prompt-injection defence boundary, and tool-use sandboxing for agentic systems are part of the cyber read. Cross-cite the vendor-AI section in the sector overlay.

#### Evidence the cyber overlay expects

- The counterparty's Information Security Program documentation, scoped against §4.F.
- SOC 2 Type II report with scope, period, exceptions, and complementary user-entity controls (CUECs) — relevant where the counterparty is a recognised auditable provider.
- Penetration-test summary current within the carrier's policy window.
- Vulnerability-management evidence (cadence, MTTR by severity, exception register).
- Incident-response runbook with the cedent-notification chain populated.
- Breach history including public disclosures, regulator actions, and aging.

#### Common cyber-overlay pitfalls

- Reading the counterparty's SOC 2 as the §4.F evidence pack. Different audience, different scope; SOC 2 may inform §4.F but does not substitute.
- Setting the counterparty's breach-notification clock to the counterparty's preferred clock instead of to the carrier's downstream regulator clocks.
- Treating sub-processor change-notice as a sufficient §4.F control when the model law expects monitoring of the sub-processor's practices.
- Assuming Model #668 applies where the operating footprint includes a non-adopting state — confirm against the NAIC adoption tracker, and pivot to the state-specific cyber frame (often NYDFS 500 or a state DOI bulletin) where #668 is not adopted.

## privacy

### Privacy cross-cutting overlay — insurance-outsourcing-review

Load this overlay whenever the outsourced function touches policyholder personal information, protected health information, or any consumer-information flow the carrier owes. Privacy is in scope by default for life and health TPAs, claims administrators handling medical records, and any data-processing outsourcer in the carrier's pipeline.

#### Operative anchors

- **HIPAA Privacy Rule (45 CFR Parts 160, 164 Subpart E) and Security Rule (45 CFR Parts 160, 164 Subpart C)**. Where the outsourced function touches protected health information (PHI) — life and health TPAs, claims administrators reading medical records, OCR processors of claims documents, AI tools reading prescription or medical history — the counterparty is a business associate. The pack must confirm Business Associate Agreement (BAA) execution, the breach-notification chain (60-day clock), minimum-necessary access posture, and where the counterparty engages sub-processors, the corresponding subcontractor BAA. https://www.hhs.gov/hipaa/for-professionals/index.html .

- **NAIC Insurance Information and Privacy Protection Model Act, Model #670** [verify model number]. The state insurance information-and-privacy framework where adopted; covers consumer-information collection, disclosure authorisation, and pretext-interview restrictions in the delegated function. Adoption is uneven; cite by state when used.

- **State insurance privacy regulations under Gramm-Leach-Bliley**. State insurance regulators implement GLBA Title V for insurance; the counterparty handling NPI is on the §314 safeguards-equivalent obligation through state insurance privacy regulation. Pin the state regulation by citation when used.

- **State comprehensive privacy laws**. CCPA / CPRA, VCDPA, CTDPA, and the rolling list of state comprehensive privacy laws. Coverage and definitions vary; insurance-regulated data is partially exempted in some states (typically GLBA-covered data) but not all. Pin by state of the carrier's customer footprint and the counterparty's data location; the diligence reads the GLBA-exemption scope state-by-state.

#### Evidence the privacy overlay expects

- **HIPAA business-associate posture** — BAA on file, currency of the BAA against the latest HIPAA amendments, the subcontractor BAA chain, breach-notification and minimum-necessary postures evidenced, workforce-training and access-log evidence at the counterparty.

- **Insurance-information consent and disclosure-authorisation posture** under Model #670 [verify section] where adopted, including disclosure-authorisation forms, opt-outs, and access-and-correction handling.

- **Data-processing register at the counterparty** — what policyholder data, what categories of data subject, what processing purposes, what retention windows, what cross-border flows.

- **Sub-processor list and the change-notice mechanism** — see also the cyber overlay for the §4.F sub-processor visibility read; here the privacy lens reads on data-flow.

- **Privacy-incident-response posture** — severity taxonomy, customer-notification clock, regulator-notification clock, evidence of past incidents.

- **Data-subject-rights handling** — how the counterparty processes policyholder access, deletion, correction, opt-out requests routed through the carrier; HIPAA-protected data has its own access-and-amendment regime distinct from state-comprehensive-privacy regimes.

#### Insurance-specific privacy considerations

- **Closed-block claims administration** typically processes PHI and lands directly in HIPAA business-associate territory. The pack must read the BAA chain, including any OCR or document-AI sub-processor.

- **AI tools using PHI or NPI** at the counterparty (life and health underwriting AI using prescription-history; claims AI reading medical narratives; OCR on claims documents) inherit the privacy posture and the HIPAA business-associate posture. Cross-cite the vendor-AI section in the sector overlay.

- **ECDIS data flows** through the counterparty (for example, an MGA using a vehicle-history aggregator) trigger consumer-disclosure and recourse expectations under state DOI AI bulletins where the operating footprint includes those states (Colorado SB 21-169 implementing regulation; NY DFS Insurance Circular Letter on AI and ECDIS). Cite by state.

- **Producer-licensing intersection with consumer-data handling**. A counterparty with binding or producer authority that holds policyholder data carries both a licensing posture and a privacy posture; the two reads sit alongside each other and do not substitute.

#### Common privacy-overlay pitfalls

- Skipping the HIPAA business-associate analysis on a "tech vendor" or "data processor" that incidentally touches PHI through claims documents.
- Treating GLBA-coverage as blanket exemption from a state comprehensive privacy law when the counterparty processes data outside the GLBA-covered scope.
- Missing the subcontractor BAA chain when the counterparty changes a downstream sub-processor.
- Setting the breach-notification clock to the counterparty's preferred clock instead of to the carrier's downstream regulator-notification clocks (HIPAA 60-day clock; state DOI clocks; SEC Item 1.05 8-K clock for publicly-listed insurers).
- Conflating insurance-information privacy under state insurance privacy regulation with state comprehensive privacy law; the two regimes have different scope, different consumer rights, and different regulators.
