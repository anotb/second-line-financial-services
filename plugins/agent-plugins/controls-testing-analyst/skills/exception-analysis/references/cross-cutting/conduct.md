# Cross-cutting overlay: conduct

Loads when `cross_cutting_overlay_set` includes `conduct`. Default-on for any control test sampling a consumer-impact population. Carries the consumer-harm framing that shifts severity calibration distinct from the technical control deviation, and the disposition language that the firm's customer-remediation track consumes.

## Consumer-harm framing distinct from technical deviation

Conduct exceptions split into two reads that the register carries separately:

- The technical control-deviation read. The control did or did not operate as designed against the rule, regardless of customer outcome.
- The consumer-harm read. Was a customer financially harmed, exposed to harm, denied a benefit they were entitled to, charged a fee they should not have been charged, given misleading information that could have affected a decision.

Both reads belong in the register. A control-failure exception with no identified consumer harm is a different finding from a control-failure exception with quantified consumer harm; severity rationale, remediation seed, and the issue-writeup handoff differ.

The CFPB UDAAP examination manual sets the underlying methodology for the consumer-harm read [verify section labels in the current edition]. The manual frames unfair, deceptive, and abusive practices in terms of consumer outcomes (substantial injury, reasonable avoidability, countervailing benefits), not in terms of technical rule compliance alone.

## Severity calibration shift for consumer-facing populations

Severity rationale for conduct exceptions carries an additional axis: the customer-harm pattern.

- `none-identified` — the control deviation did not reach a customer (e.g., the deviation was caught by a downstream control before customer impact).
- `identifiable-no-quantification` — the deviation reached a customer or a population of customers but the harm has not yet been quantified (the firm's restitution or impact analysis is open).
- `quantified-individual` — the deviation harmed identifiable customers in named amounts.
- `quantified-population` — the deviation harmed a population pattern with named aggregate impact.
- `regulatory-pattern-eligible` — the harm pattern matches a CFPB Circular, OCC enforcement theme, or other supervisory-pattern indicator. [verify the current circular set and enforcement themes for the entity's regulator constellation.]

The severity ladder shifts with the customer-harm read. A `control-failure` exception with `quantified-population` consumer harm reads at higher severity than the same `control-failure` with `none-identified`; the firm's published thresholds in the firm-overlay drive the exact ladder, but the methodology bar is that consumer harm is a severity input separate from frequency and regulatory exposure.

## Disposition language for consumer-remediation handoff

Where the disposition is `elevated-to-issue` and the consumer-harm read is anything other than `none-identified`, the recommendation seed in the issue-handoff package names the remediation track distinctly: control-side remediation (fix the control) and consumer-side remediation (restitution, fee reversal, file correction, customer notification, credit-bureau correction). The firm's consumer-remediation track is a separate workflow from the issue-tracking workflow; the register flags both.

The closure-evidence framing the issue writer carries forward names both tracks. The control-side closure evidence is what the firm inspects to confirm the control now operates; the consumer-side closure evidence is what the firm inspects to confirm the consumer remediation completed (restitution paid log, fee-reversal report, customer notification proof of delivery, credit-bureau update confirmation).

## UDAAP-touching exceptions

Where a conduct exception surfaces a UDAAP-analogue pattern (statement misleading, fee not adequately disclosed, practice unfairly limits consumer choice, abusive practice exploiting consumer vulnerability), the register flags it explicitly in the disposition rationale. The handoff to issue write-up populates the recommendation seed with the consumer-side remediation as well as the control-side remediation, and the issue writer's UDAAP framing pulls from the register's flagged classification.

The criterion field cites the UDAAP-relevant rule (CFPB UDAAP statutory authority, FTC Act §5 for non-CFPB-regulated entities, state-equivalent unfair-trade-practices acts where applicable) with a section reference [verify current citations].

## Conduct exception patterns by product family

Distinct product families carry distinct conduct exception patterns. Where the engagement scope flags the relevant product, the register reads against the product-family conventions:

- Deposit accounts (Reg E, Reg DD): fee-disclosure deviations, NSF / overdraft-disclosure deviations, error-resolution deviations.
- Lending (Reg Z, Reg B, fair-lending statutes): pricing-disclosure deviations, adverse-action notice deviations, redlining-pattern indicators in HMDA-adjacent populations.
- Mortgages (Reg X, RESPA): closing-disclosure deviations, escrow-handling deviations, servicing-transfer deviations.
- Investments (FINRA suitability rule, Reg BI for broker-dealer recommendations to retail customers): suitability-determination deviations, conflict-of-interest disclosure deviations.
- Insurance (state unfair-trade-practices acts, replacement-of-policy regulations): replacement-disclosure deviations, claims-handling deviations.

The criterion field cites the product-family rule with a section reference; the handoff to issue write-up loads the conduct-overlay framing for the issue writer.
