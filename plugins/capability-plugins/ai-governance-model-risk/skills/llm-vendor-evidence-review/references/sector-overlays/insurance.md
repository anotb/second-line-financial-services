# Sector overlay: insurance

Loaded when `scope.sector_overlay_set` includes insurance. Carries the insurance-vendor-specific frame for foundation-model evidence-pack review: state-DOI supervisory visibility, NAIC Model Bulletin alignment, and the fairness-evidence and consumer-protection seams that insurance-vendor reviews surface in addition to the cross-cutting baseline.

## Supervisory frame

State Departments of Insurance are the binding supervisor; insurance regulation in the US is state-based. The NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023) is the converged industry frame; binding to the extent the insurer's domicile and material-state regulators have adopted or signalled adoption. The state-adoption tracker maintained by the NAIC AI Working Group is the public reference.

The Bulletin's AIS Programme elements set the supervisory expectation around vendor AI: the insurer's AIS Programme must address third-party AI systems with named accountability, vendor risk-management procedures, evidence on testing and validation, monitoring of vendor systems in production, and documentation. The vendor evidence-pack review feeds the AIS Programme's third-party-AI accountability and testing-and-validation elements.

State-specific AI rules (Colorado SB 21-169 and the Division of Insurance regulations on algorithmic discrimination, New York DFS Insurance Circular Letter on consumer protection in AI use, California Department of Insurance bulletins) layer on for in-scope insurers; the state-by-state binding-status check is part of every review.

The state Insurance Data Security Model Law (NAIC Model Law 668), where adopted in the relevant state, applies to information-security posture for insurer use of third-party providers; the cyber overlay carries the named provisions.

## Sector-specific evidence asks

The insurance-vendor frame surfaces the following beyond the cross-cutting baseline:

- **Fairness and bias evidence relevant to insurance uses.** Where the foundation model is consumed in underwriting, claims, marketing, or any use class within scope of state algorithmic-discrimination regulation, the evidence-pack review surfaces the vendor's published fairness evaluations and testing methodology. General-purpose fairness evaluations are starting context; insurance-domain fairness evaluation is firm-side responsibility under the AIS Programme.

- **Consumer-protection and explainability posture.** The vendor's published documentation on model-output interpretability, refusal behaviour around adverse-action-relevant outputs, and downstream-consequence-aware design feeds the insurer's compliance with adverse-action notice and reason-code obligations. The evidence-pack review surfaces the documentation; the insurer's compliance function performs the regulatory-fit assessment.

- **Sensitive-class and inference-risk posture.** Foundation-model behaviour around protected-class inference (race, ethnicity, health status, genetic information) is relevant to insurance use cases that touch underwriting or rating. The evidence pack should establish the vendor's awareness and any documented mitigations; firm-side controls under `prompt-injection-risk` and `validation-plan` carry the in-firm enforcement.

- **State-of-deployment posture for cross-border data flows.** Insurance regulation of data residency varies by state and by line of business (P&C, life, health). Where the vendor processes prompts or training-data-derivative artefacts in jurisdictions outside the deployment state, the vendor evidence pack should describe the data-flow posture; the privacy overlay carries the named state-by-state implications.

- **NAIC Model Bulletin AIS Programme element mapping.** For each named AIS Programme element (governance and risk management, AI vendor accountability, AIS testing and validation, AIS monitoring and oversight, documentation), the evidence-pack review surfaces the vendor evidence that supports the element. Element-by-element mapping is part of the structured-output `sector_overlay_notes`.

- **HIPAA business-associate posture for health-relevant lines.** For life and health lines where PHI may flow to the vendor (or be inferable from claims narratives), HIPAA business-associate considerations apply; the cyber and privacy overlays carry the named obligations.

## Sector-specific co-reviewer expectations

The state-regulated insurance entity's chief actuary or chief risk officer is a co-reviewer where the use case affects pricing, reserving, or solvency. The chief compliance officer co-reviews where the use case affects consumer-facing or producer-facing communications. For health-touching deployments, the privacy office (HIPAA-compliant officer) co-reviews. The evidence-pack review is filed only after the AI Governance Lead and named co-reviewers attest.

## Sector-specific re-review triggers

In addition to the baseline triggers, insurance adds:

- State-DOI feedback referencing the vendor or model.
- New or revised state algorithmic-discrimination regulation or NAIC Model Bulletin amendment materially affecting third-party AI expectations.
- Material change in the vendor's posture on fairness evaluations or sensitive-class inference.
- Material change in the line-of-business deployment scope (e.g., expansion from claims summarisation to claims decisioning).

## Sector-specific structured-output additions

The `sector_overlay_notes` block in the schema carries the insurance-specific findings:

```
"sector_overlay_notes": {
  "naic_ais_programme_element_mapping": {
    "governance_and_risk_management": "...",
    "ai_vendor_accountability": "...",
    "testing_and_validation": "...",
    "monitoring_and_oversight": "...",
    "documentation": "..."
  },
  "fairness_evidence_summary": "...",
  "sensitive_class_posture": "...",
  "state_doi_visibility": "...",
  "state_specific_rules_in_scope": [...]
}
```
