# Privacy cross-cutting overlay — insurance-outsourcing-review

Load this overlay whenever the outsourced function touches policyholder personal information, protected health information, or any consumer-information flow the carrier owes. Privacy is in scope by default for life and health TPAs, claims administrators handling medical records, and any data-processing outsourcer in the carrier's pipeline.

## Operative anchors

- **HIPAA Privacy Rule (45 CFR Parts 160, 164 Subpart E) and Security Rule (45 CFR Parts 160, 164 Subpart C)**. Where the outsourced function touches protected health information (PHI) — life and health TPAs, claims administrators reading medical records, OCR processors of claims documents, AI tools reading prescription or medical history — the counterparty is a business associate. The pack must confirm Business Associate Agreement (BAA) execution, the breach-notification chain (60-day clock), minimum-necessary access posture, and where the counterparty engages sub-processors, the corresponding subcontractor BAA. https://www.hhs.gov/hipaa/for-professionals/index.html .

- **NAIC Insurance Information and Privacy Protection Model Act, Model #670** [verify model number]. The state insurance information-and-privacy framework where adopted; covers consumer-information collection, disclosure authorisation, and pretext-interview restrictions in the delegated function. Adoption is uneven; cite by state when used.

- **State insurance privacy regulations under Gramm-Leach-Bliley**. State insurance regulators implement GLBA Title V for insurance; the counterparty handling NPI is on the §314 safeguards-equivalent obligation through state insurance privacy regulation. Pin the state regulation by citation when used.

- **State comprehensive privacy laws**. CCPA / CPRA, VCDPA, CTDPA, and the rolling list of state comprehensive privacy laws. Coverage and definitions vary; insurance-regulated data is partially exempted in some states (typically GLBA-covered data) but not all. Pin by state of the carrier's customer footprint and the counterparty's data location; the diligence reads the GLBA-exemption scope state-by-state.

## Evidence the privacy overlay expects

- **HIPAA business-associate posture** — BAA on file, currency of the BAA against the latest HIPAA amendments, the subcontractor BAA chain, breach-notification and minimum-necessary postures evidenced, workforce-training and access-log evidence at the counterparty.

- **Insurance-information consent and disclosure-authorisation posture** under Model #670 [verify section] where adopted, including disclosure-authorisation forms, opt-outs, and access-and-correction handling.

- **Data-processing register at the counterparty** — what policyholder data, what categories of data subject, what processing purposes, what retention windows, what cross-border flows.

- **Sub-processor list and the change-notice mechanism** — see also the cyber overlay for the §4.F sub-processor visibility read; here the privacy lens reads on data-flow.

- **Privacy-incident-response posture** — severity taxonomy, customer-notification clock, regulator-notification clock, evidence of past incidents.

- **Data-subject-rights handling** — how the counterparty processes policyholder access, deletion, correction, opt-out requests routed through the carrier; HIPAA-protected data has its own access-and-amendment regime distinct from state-comprehensive-privacy regimes.

## Insurance-specific privacy considerations

- **Closed-block claims administration** typically processes PHI and lands directly in HIPAA business-associate territory. The pack must read the BAA chain, including any OCR or document-AI sub-processor.

- **AI tools using PHI or NPI** at the counterparty (life and health underwriting AI using prescription-history; claims AI reading medical narratives; OCR on claims documents) inherit the privacy posture and the HIPAA business-associate posture. Cross-cite the vendor-AI section in the sector overlay.

- **ECDIS data flows** through the counterparty (for example, an MGA using a vehicle-history aggregator) trigger consumer-disclosure and recourse expectations under state DOI AI bulletins where the operating footprint includes those states (Colorado SB 21-169 implementing regulation; NY DFS Insurance Circular Letter on AI and ECDIS). Cite by state.

- **Producer-licensing intersection with consumer-data handling**. A counterparty with binding or producer authority that holds policyholder data carries both a licensing posture and a privacy posture; the two reads sit alongside each other and do not substitute.

## Common privacy-overlay pitfalls

- Skipping the HIPAA business-associate analysis on a "tech vendor" or "data processor" that incidentally touches PHI through claims documents.
- Treating GLBA-coverage as blanket exemption from a state comprehensive privacy law when the counterparty processes data outside the GLBA-covered scope.
- Missing the subcontractor BAA chain when the counterparty changes a downstream sub-processor.
- Setting the breach-notification clock to the counterparty's preferred clock instead of to the carrier's downstream regulator-notification clocks (HIPAA 60-day clock; state DOI clocks; SEC Item 1.05 8-K clock for publicly-listed insurers).
- Conflating insurance-information privacy under state insurance privacy regulation with state comprehensive privacy law; the two regimes have different scope, different consumer rights, and different regulators.
