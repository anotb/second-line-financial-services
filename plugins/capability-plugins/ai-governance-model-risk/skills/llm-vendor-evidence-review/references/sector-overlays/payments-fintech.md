# Sector overlay: payments and fintech

Loaded when `engagement-scope.sector_overlay_set` includes payments-fintech. Carries the payments-and-fintech-specific frame for foundation-model evidence-pack review: sponsor-bank visibility, BSA programme coverage of vendor-driven decisions, money-transmitter licensing constellation, and the bank-fintech-shared-responsibility seams that surface in vendor-AI deployments.

## Supervisory frame

The payments-and-fintech supervisory constellation depends on the entity:

- **Bank-as-a-service sponsor banks** carry the underlying federal banking supervisory frame (OCC, FRB, FDIC) plus state-by-state implications for sponsored fintech activity. The interagency third-party risk-management guidance (June 2023) is binding; the bank's vendor-diligence record carries the entity-level frame.
- **Sponsored fintechs** are not directly federally supervised in most cases but carry obligations through the sponsor-bank relationship; the sponsor bank is the firm responsible for ensuring AI vendor evidence is sufficient. State-level supervisory regimes (state money-transmitter licences, state consumer-financial-services regulators) add layers.
- **Money transmitters and money-services businesses** are state-licensed plus federally supervised under FinCEN's BSA programme requirements; AI use in transaction monitoring, fraud, or sanctions is read against BSA programme expectations.
- **Card networks, processors, and PSPs** carry contractual obligations to issuers and merchants in addition to direct supervision; the network rules carry weight for AI use in fraud, dispute, or chargeback processing.

The CFPB has supervisory and enforcement authority over a defined set of nonbank financial-services participants (larger nonbank market participants under named CFPB rules, plus enforcement reach over any covered persons). For consumer-facing payments and lending, CFPB Circulars and interpretive rules affect AI-vendor-decision postures (e.g., adverse action notice circular).

The OCC's "true lender" framework and state-by-state UDAP regimes carry implications for bank-fintech lending models; AI-vendor-driven underwriting falls under existing fair-lending frameworks (ECOA, FHA, state analogues) that require vendor evidence to support the firm's compliance assessment. The conduct overlay carries the named obligations.

## Sector-specific evidence asks

The payments-and-fintech frame surfaces the following beyond the cross-cutting baseline:

- **Sponsor-bank visibility into vendor evidence.** For sponsored fintech relationships, the sponsor bank's vendor-diligence and model risk programme reach into the fintech's AI vendors. The evidence-pack review surfaces what the sponsor bank can see and what the fintech holds at fintech-level. Where the fintech is the firm running the review, the sponsor-bank reporting and notification posture is in scope.

- **BSA programme coverage of vendor-driven decisions.** Where the foundation-model use case touches transaction monitoring, sanctions screening, customer due diligence, or SAR-relevant decisioning, the BSA officer is a co-reviewer and the evidence-pack review records the BSA programme touchpoints. Vendor evidence on model behaviour around BSA-relevant outputs (false-positive profile awareness, explanation depth for SAR support) is part of the supplementary ask.

- **Fraud-model and dispute-model adjacency.** For deployments adjacent to fraud or dispute-handling, the vendor evidence pack should support the firm's understanding of the model's interaction with adversarial fraud actors. Generic vendor evals do not cover fraud-model adversarial postures; record the gap and route to `validation-plan` for the firm-side fraud-domain evaluation.

- **State licensing constellation.** For multi-state money-transmitter or sponsored-fintech entities, the binding-state list materially affects the regulator-engagement-history and rereview-trigger posture. The evidence-pack review captures the constellation; the entity-level diligence in `vendor-diligence` carries the licence-by-licence detail.

- **PCI scope and tokenisation posture.** Where the foundation-model deployment touches cardholder data or payment-card-relevant communications, PCI DSS scope considerations apply. The vendor evidence pack should establish the vendor's PCI-relevant posture (scope-in vs scope-out) and the firm-side tokenisation pattern that keeps PCI scope contained.

- **Network rules and assessor obligations.** For card-network-touching deployments, network rules (Visa, Mastercard, network-of-record) carry obligations on assessment cadence and incident notification; the cyber overlay carries the named provisions.

## Sector-specific co-reviewer expectations

The BSA officer is a co-reviewer for any deployment touching BSA-relevant decisioning. For sponsored fintech entities, the sponsor-bank's TPRM function and AI Governance Lead are informed and the contract-defined approval chain runs in parallel. The CCO is a co-reviewer for any consumer-facing deployment touching CFPB or state-UDAP scope. The AI Governance Lead retains the lead attestation; named co-attests are recorded in `reviewer_attestation`.

## Sector-specific re-review triggers

In addition to the baseline triggers, payments-and-fintech adds:

- CFPB enforcement action, supervisory highlight, or new circular materially affecting AI-vendor decisions in scope.
- Sponsor-bank-driven re-attestation cycle or sponsor-bank feedback on the vendor.
- New or revised state money-transmitter or fintech-specific regulation in a binding state.
- Material change in the BSA programme classification of the use case.
- Card network rule update materially affecting AI use in network-touching processes.

## Sector-specific structured-output additions

The `sector_overlay_notes` block in the schema carries the payments-and-fintech-specific findings:

```
"sector_overlay_notes": {
  "supervisory_constellation": "...",
  "sponsor_bank_visibility_summary": "...",
  "bsa_programme_touchpoints": [...],
  "fraud_or_dispute_adjacency": "...",
  "state_licensing_constellation": [...],
  "pci_scope_posture": "...",
  "network_rule_touchpoints": [...]
}
```
