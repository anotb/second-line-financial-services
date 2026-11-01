# Sector overlay: payments-fintech

Loads when `sector_overlay_set` includes `payments-fintech`. Carries sponsor-bank oversight exception conventions and Reg E error-resolution exception treatment.

## Sponsor-bank oversight exception conventions

Bank-as-a-service / sponsor-bank programmes carry exception patterns that span the bank's oversight machinery and the fintech partner's operational execution. The interagency third-party-relationships guidance (June 6, 2023, OCC / FRB / FDIC) sets the supervisory expectation. [verify section labels under the published guidance.]

What this means for the register:

- The testing subject is the bank's oversight control, not the fintech partner's operational control. Classification reads against the bank-side criterion, even when the underlying observable condition was at the partner.
- A partner-side execution gap that the bank's oversight control did not surface reads as `control-failure` at the bank's oversight control. The severity rationale names the partner-side condition, the oversight criterion, and the gap in the bank's monitoring or escalation process.
- A partner-side execution gap that the bank's oversight control did surface and escalate reads as `closed-at-exception` on the bank's oversight, with the partner-side issue tracked in the firm's vendor-monitoring register (a separate artifact).
- A design-gap in the bank's oversight programme (no monitoring control exists for a partner risk the third-party guidance expects to be monitored) reads as `design-gap`, severity calibrated against the partner's criticality tier.

The handoff to issue write-up populates fields the bank's third-party-risk issue ladder consumes; severity calibration carries the partner criticality and the supervisory expectation that critical-vendor oversight is heightened.

## Reg E error-resolution exception treatment

Reg E (12 CFR 1005, Subpart A) error-resolution testing produces a high-volume exception population in payments and consumer-facing fintech. [verify current section labels at 12 CFR 1005.11 for error resolution and §1005.6 for liability.]

Classification calls:

- Provisional-credit timing deviations (the rule sets a 10-business-day deadline for provisional credit when the institution cannot complete investigation within that window) read as `control-failure` with timing as the load-bearing fact. Severity calibrates against frequency and the dollar pattern.
- Error-resolution-final-determination timing deviations read similarly; the rule sets a 45-day deadline (90 days for new accounts and certain transaction types). [verify the current deadline structure.]
- Investigation-quality deviations (no documented investigation steps, conclusion not supported by the investigation record) read as `evidence-gap` when the system shows the investigation occurred and as `control-failure` when there is no system or file record of the investigation at all.
- Liability-determination deviations (consumer assessed liability beyond the rule's caps, liability assessed without the conditions the rule requires) read as `control-failure`, severity calibrated against the liability amount and the consumer-harm pattern.

Conduct cross-cutting overlay loads automatically when the Reg E population is consumer-facing.

## Money-transmitter exception treatment

Money-transmitter testing carries state-by-state regulatory variation. [verify the relevant state money-transmitter act sections for the states where the entity is licensed.] Exception classification reads against the state-specific obligations the test was scoped to; the criterion field cites the state-specific rule with a section reference. The severity rationale field names the state-specific examination posture where it differs from federal expectations.

## Card-network and processor exception patterns

For testing scoped to card-network rules (Visa Core Rules, Mastercard Rules) or processor-side reconciliation controls, the criterion is typically the network rule with a rule-section reference and the firm's contractual obligation under the network agreement. [verify the network rule edition.] These are typically `control-failure` or `data-integrity` exceptions rather than `design-gap`; the design is the network's, not the firm's. The severity rationale field names the network-side fining or chargeback exposure.
