# Payments and fintech sector overlay for prompt-injection-risk

When the engagement-scope record names `payments-fintech` as the sector, this overlay adds payments-fintech-specific carriers, mitigations, monitoring signals, and incident-notification triggers to the review. Loaded by `prompt-injection-risk/SKILL.md` when `engagement_scope.sector_overlay_set` includes `payments-fintech`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- Joint Interagency Guidance on Third-Party Relationships (June 2023; OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023) where the GenAI use case sits in a sponsor-bank / fintech (BaaS) arrangement; the sponsor bank retains accountability for the third-party AI risk.
- The 36-hour banking computer-security incident notification rule (12 CFR Part 53 / Part 225 / Part 304) where the fintech is bank-affiliated or operates under a sponsor-bank.
- CFPB UDAAP authority and CFPB consumer-financial-product expectations for fintechs in CFPB scope.
- Reg E (12 CFR Part 1005, Electronic Fund Transfers) and Reg Z (12 CFR Part 1026) for consumer-facing payments and credit products.
- FinCEN BSA expectations applied to money services businesses, virtual-currency businesses, and payments processors in BSA scope.
- State money-transmitter licensing regimes (state-by-state patchwork; the firm maintains the matrix).
- NYDFS 23 NYCRR Part 500 and the Part 200 virtual-currency regulation for NY-licensed entities.
- PCI DSS for cardholder-data-handling systems.

## Carriers and trust posture nuances specific to payments and fintech

The recurring payments-fintech GenAI use-case patterns and the carriers that usually drive the threat surface:

- **Customer-onboarding assistant** (KYC, identity verification, account opening): retrieves over identity-document content, third-party identity-verification responses, sanctions-screening hits, adverse-media. Highest-likelihood vector is indirect injection via document content (synthetic ID documents with embedded instructions) and via third-party identity-verification API responses; PII exfiltration risk is structural.

- **Dispute-handling assistant** (Reg E, chargeback): retrieves over customer-supplied evidence (photos, screenshots, written narratives), merchant correspondence, transaction records, fraud-detection signals. Highest-likelihood vector is indirect injection via customer-supplied evidence and merchant correspondence; the Reg E provisional-credit decision-support context is the consumer-protection seam (10-day provisional credit, 45-day investigation timeline).

- **Customer-service assistant**: similar pattern to banking customer-service assistant; account-takeover-fraud adjacency is the structural risk because customer-service interactions are an account-takeover entry point.

- **Transaction-monitoring and AML alert-triage assistant**: similar to banking AML overlay; in the fintech context, the BSA officer and the sponsor-bank BSA function (where applicable) are co-reviewers.

- **Merchant-onboarding and underwriting assistant**: retrieves over merchant application data, processor risk data, card-network watch lists. Risk-based pricing and adverse-action-notice considerations apply where the AI output supports adverse decisions.

- **Crypto/virtual-asset-specific assistants**: retrieves over wallet-screening data, blockchain-analytics output, sanctions-screening hits. NYDFS Part 200 and FinCEN MSB framings apply for in-scope entities.

## Mitigations the review should expect to see

Beyond the standard set:

- Consumer-facing output filtering aligned to UDAAP and Reg E / Reg Z disclosure requirements; consumer compliance signs off.
- Sanctions / OFAC screening on any output that could include third-party identifying information.
- Per-customer query scoping at the retrieval layer for any customer-handling assistant; account-takeover-relevant retrieval audit on top.
- Document-stage input sanitisation for synthetic-ID-resilient document handling in onboarding flows.
- BSA/AML output filtering where the system supports alert disposition or SAR drafting; the BSA officer signs off.
- For sponsor-bank BaaS arrangements, the sponsor-bank's third-party risk register is updated to reference the prompt-injection review and the sponsor-bank's review obligations are documented.
- PCI DSS-aligned controls on systems handling cardholder data.
- Foundation-model and vendor change-of-version notice and audit rights, captured in the third-party risk register; the sponsor-bank's interagency-guidance obligations apply.

## Monitoring signals the overlay adds

- Per-customer retrieval audit; account-takeover-relevant patterns (off-hours queries, rapid sequential queries, queries from unusual originating IPs) added to the cross-customer audit.
- UDAAP-relevant output-filter trip rate; escalation to consumer compliance.
- Reg E / Reg Z disclosure-content output-filter trip rate where applicable; escalation to consumer compliance.
- BSA/AML alert-disposition anomaly where the system supports alert handling; escalation to the BSA officer and to the sponsor-bank BSA function (where applicable).
- 36-hour banking computer-security incident notification trigger evaluation for sponsor-bank-affiliated incidents.
- Sponsor-bank vendor-management reporting cadence: prompt-injection review status reported to the sponsor-bank per the contractual reporting cadence.

## Incident-response triggers the overlay adds

In addition to the cyber-overlay-named triggers:

- 36-hour banking computer-security incident notification (where sponsor-bank-affiliated): the sponsor bank notifies its primary federal regulator within 36 hours of determining that a notification incident has occurred. The fintech and the sponsor bank's incident-response chains coordinate.
- Reg E error-resolution timeline: an injection-driven event that affects dispute resolution (delays provisional credit, mishandles error claims) creates Reg E exposure with statutory timelines (10-day provisional credit, 45-day investigation) that the response must meet.
- UDAAP event triggers if customer-facing AI output causes a UDAAP-relevant communication or decisional issue.
- State money-transmitter regulator notification for in-scope entities; the firm's matrix of state-by-state notification obligations governs.
- NYDFS Part 500 §500.17(a) for NY-licensed entities (as in the cyber overlay) and Part 200 incident-handling for NY-licensed virtual-currency entities.
- FinCEN BSA programme-integrity considerations where the system supports alert handling.
- PCI DSS incident-response and card-brand notification for cardholder-data exposure.

## Recommended-action items the overlay surfaces

- For sponsor-bank BaaS arrangements, the sponsor-bank's review and approval is recorded; the residual-risk acceptance includes the sponsor-bank function as a co-acceptor or as a notification party per the contractual arrangement.
- For consumer-facing assistants, consumer compliance co-signs the residual-risk acceptance and the UDAAP / Reg E / Reg Z output-filter specifications are documented.
- For onboarding assistants, the synthetic-ID-resilience testing is included in the firm-internal red team scope.
- For dispute-handling assistants, the Reg E timeline integrity is documented in the incident-response section (an injection-driven delay in dispute handling is itself a Reg E violation).
- For crypto/virtual-asset assistants, the NYDFS Part 200 framing and the FinCEN MSB framing are mapped to the review's mitigations and incident-response sections.

## Common pitfalls specific to payments and fintech

- Treating the sponsor-bank as a downstream consumer of the prompt-injection review. Under the June 2023 interagency guidance, the sponsor bank retains accountability for the third-party AI risk; the bank is a co-reviewer or a co-acceptor depending on the contractual arrangement, not a downstream notification party.
- Omitting the 36-hour banking computer-security incident notification rule when the fintech is bank-affiliated. The rule applies to the bank, but the fintech's incident-response chain must support the bank's 36-hour determination timeline.
- Failing to surface Reg E timeline considerations in the dispute-handling-assistant review. An injection-driven event that delays provisional credit or mishandles error claims is a Reg E violation independent of the cyber and AI-governance lenses.
- Treating consumer-facing AI output as an AI-governance-only concern. UDAAP authority and Reg E / Reg Z disclosure requirements apply; consumer compliance is a co-reviewer.
- Omitting state money-transmitter and state-by-state regulator notification considerations. The state patchwork is the firm's responsibility to maintain; the review references the firm's matrix.
- Treating PCI DSS as out of scope because the AI system does not directly handle cardholder data. If the AI system is on the same network segment, can be reached from the cardholder-data environment, or processes content that includes cardholder data even incidentally, PCI DSS scope extends.
