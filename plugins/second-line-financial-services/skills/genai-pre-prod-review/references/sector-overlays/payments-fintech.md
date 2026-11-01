# Payments and fintech sector overlay for genai-pre-prod-review

When the scope record names `payments-fintech` as the sector, this overlay adds payments-and-fintech-specific gate considerations: sponsor-bank co-acceptance where applicable, payments-specific notification triggers, sector-specific monitoring expectations, and recommended-action items typical of payments and fintech GenAI gate reviews (customer-service assistants, fraud-detection augmentation, transaction-monitoring augmentation, dispute-handling assistants). Loaded by `genai-pre-prod-review/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- Joint Interagency Guidance on Third-Party Relationships (June 2023; OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023) for sponsor-bank / fintech relationships and BaaS arrangements.
- Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services (July 2024) and related interagency guidance for BaaS arrangements.
- Reg E (12 CFR Part 1005) for consumer electronic fund transfer dispute handling and provisional-credit obligations.
- Reg Z (12 CFR Part 1026) where the use case touches credit-product communications.
- CFPB UDAAP authority and CFPB circulars for AI-assisted customer communications and dispute handling.
- BSA/AML obligations for non-bank financial institutions registered with FinCEN; transaction-monitoring augmentation considerations.
- Card-network rules (Visa, Mastercard, Amex, Discover) for fraud and chargeback handling where applicable.
- State money-transmitter laws and state DFI / DBO supervision for licensed non-bank entities.
- Network rules for ACH (Nacha Operating Rules) and real-time payments where applicable.
- NYDFS 23 NYCRR Part 500 and the BitLicense framework for NY-licensed money transmitters and virtual currency businesses.

## Co-reviewers the gate review brings in

Beyond the standard sign-off set:

- **Sponsor bank** for any BaaS or sponsor-bank-relationship use case; the sponsor bank's own model risk and AI governance functions co-accept the gate decision per the relationship agreement.
- **Consumer compliance** for any consumer-facing or consumer-handling use case; UDAAP, Reg E, and Reg Z exposure on AI-generated or AI-assisted customer communication.
- **BSA officer** for non-bank financial institutions registered with FinCEN where the use case touches transaction monitoring, customer due diligence, or SAR drafting.
- **Fraud and disputes function** for any use case touching fraud detection, dispute handling, or chargeback processing.
- **Network compliance** for any use case touching card-network or ACH-network operations; network-rule conformance.
- **State money-transmitter compliance** for any multi-state licensed non-bank entity; state-by-state notification and licensing variation.

## Open conditions the overlay typically adds

- Sponsor-bank co-acceptance documented in the BaaS or sponsor-bank relationship file for any sponsor-bank-relationship use case; the sponsor bank's gate decision and the firm's gate decision align before go-live.
- Reg E provisional-credit-handling workflow documented for any AI-assisted dispute-handling use case; the 10-day provisional-credit clock runs regardless of AI handling decisions.
- UDAAP output-filter specification signed off by consumer compliance for any consumer-facing communication generated or assisted by the system.
- For transaction-monitoring augmentation: documented evaluation that the AI augmentation does not introduce false-negative bias against BSA-relevant patterns; BSA officer co-signs.
- For fraud-detection augmentation: documented baseline against the prior fraud-detection system; fraud and disputes function co-signs.
- For non-bank entities in state-money-transmitter scope: state-by-state licensing and notification matrix documented.

## Monitoring signals the overlay expects to see live before go-live

In addition to the standard signal set:

- UDAAP output-filter trip rate; escalation to consumer compliance.
- Reg E dispute-handling SLA tracking (10-day provisional-credit clock, 45-day resolution clock); escalation to consumer compliance and dispute function.
- For fraud-detection augmentation: false-negative-rate and false-positive-rate sampling against the prior system baseline; escalation to fraud and disputes function.
- For transaction-monitoring augmentation: alert-quality and alert-disposition-anomaly signals; escalation to BSA officer.
- Sponsor-bank notification feed throughput where applicable; escalation to vendor management with sponsor-bank relationship owner.
- Network-rule conformance signal where applicable (chargeback-processing accuracy, ACH-return-handling accuracy).

## Incident-response triggers the overlay adds

In addition to the cyber-overlay-named triggers:

- For sponsor-bank-relationship use cases: notification to the sponsor bank under the BaaS or sponsor-bank relationship agreement; the sponsor bank's notification obligations to its primary federal regulator (including the 36-hour banking computer-security incident notification rule under 12 CFR Part 53 / Part 225 / Part 304) flow back via the relationship.
- BSA programme-integrity event triggers for non-bank financial institutions in FinCEN scope where the use case touches transaction monitoring or SAR drafting; FinCEN reporting obligations apply.
- Reg E error-resolution-process integrity event triggers if AI-assisted dispute handling causes a procedural failure that affects a consumer's rights under Reg E.
- Card-network notification obligations where a fraud or chargeback handling AI failure crosses a network-rule notification threshold.
- State money-transmitter licensing notification obligations per state where applicable.

The IR drill scope before go-live should exercise at minimum one payments-or-fintech-specific incident class (e.g., confirmed Reg E timeline failure in AI-assisted dispute handling; confirmed UDAAP-relevant misleading communication; confirmed BSA programme-integrity issue in AI-assisted transaction monitoring; sponsor-bank-relationship-relevant confirmed event for BaaS use cases).

## Recommended-action items the overlay surfaces

- Where the use case is sponsor-bank-relationship-dependent, the BaaS or sponsor-bank relationship file is updated to reference the gate review and the sponsor bank's co-acceptance is recorded.
- Where the use case touches AI-assisted dispute handling, the Reg E error-resolution workflow and the provisional-credit clock are documented as not affected by AI handling latency.
- Where the use case touches UDAAP-relevant customer communications, consumer compliance signs off on the output-filter specification and on the complaint-channel readiness.
- Where the use case touches BSA-relevant transaction monitoring or SAR drafting, the BSA officer co-signs and BSA-relevant monitoring signals are live before go-live.
- Where the entity holds multiple state money-transmitter licences, the state-by-state notification matrix and the licensing-variation matrix are documented.

## Common pitfalls specific to payments-fintech gate reviews

- Treating a sponsor-bank-relationship use case as if the firm has unilateral gate decision authority. The sponsor bank's own AI governance and model risk functions co-accept by relationship agreement; an unaccepted gate decision in the sponsor bank is not a firm-side go.
- Omitting the Reg E error-resolution timeline analysis for AI-assisted dispute handling. The 10-day provisional-credit clock and the 45-day resolution clock are statutory and run independently of AI handling; AI latency or handling failure does not toll the clock.
- Treating UDAAP exposure on AI-generated customer communications as a downstream consumer-compliance review. UDAAP is the seat consumer compliance owns at the gate, not after; the gate decision is incomplete without consumer compliance sign-off.
- Treating a fraud-detection or transaction-monitoring augmentation as a control improvement without baseline-against-prior-system evidence. A new AI augmentation that improves alert quality while shifting false negatives in BSA-relevant patterns is a programme-integrity issue; the gate review records the regression test explicitly.
- Treating multi-state money-transmitter licensing as a uniform compliance posture. State licensing terms, notification obligations, and supervisory examination postures vary; the gate review records state-by-state status.
- Relying on sponsor-bank evidence as substituting for firm-side gate evidence. Sponsor-bank evidence is one input; the firm-side gate items are firm-side responsibilities.
