# Sector overlay: banking

Loaded when `scope.sector_overlay_set` includes banking. Carries the bank-vendor-specific frame for foundation-model evidence-pack review: the supervisory perspective bank examiners take on third-party model evidence, the entity-level wrapper that the interagency third-party guidance imposes, and the specific evidence asks that bank-vendor reviews surface in addition to the cross-cutting baseline.

## Supervisory frame

Bank model risk programmes interpret the federal interagency model risk guidance (Federal Reserve SR 11-7 and the parallel OCC bulletin) as carrying expectations for vendor and third-party models. Where the firm's MRM programme treats the foundation-model use case as in scope of model risk, vendor evidence-pack review becomes part of meeting the third-party model expectations: documentation and validation evidence sufficient to support the firm's own validation work, with awareness that proprietary vendor methods may limit the depth of validation evidence available.

The 2026 revised interagency model risk guidance refreshes these expectations for AI/ML and generative AI; section references for the AI/ML and third-party model passages are tracked in `references/source-anchors.md` with `[verify section]` flags pending confirmation.

The interagency third-party risk-management guidance (June 2023) is the entity-level wrapper. The vendor-diligence record under `vendor-diligence` in `third-party-operational-resilience` carries the entity-level diligence; this evidence-pack review is the model-evidence layer that chains from `eval_evidence_status = deferred-to-evidence-review`.

The FFIEC IT Examination Handbook applies as the IT-and-information-security frame for the bank-vendor relationship; relevant booklets are Information Security and Architecture, Infrastructure, and Operations. For NY-footprint subsidiaries, 23 NYCRR Part 500 §500.11 (third-party service-provider security) layers on; the cyber overlay carries that detail.

## Sector-specific evidence asks

The bank-vendor frame surfaces the following beyond the cross-cutting baseline:

- **Examination evidence rights.** The vendor evidence pack should be readable in a bank examination. Where the vendor restricts evidence to NDA-only, the contract should preserve the firm's ability to share specified evidence with examiners under examiner-confidentiality protections. Record the contract clause status here, not in the entity-level diligence.

- **Audit and assessment rights covering the model layer.** The interagency third-party guidance expects audit rights to extend to the activities the vendor performs on behalf of the bank. For a foundation-model vendor, this includes the right to receive evidence on adversarial robustness, evaluation methodology, and red-team scope at the depth the bank's model risk function needs. Where vendor practice limits audit-right depth (typical for major foundation-model providers' published-evidence model), record the residual reliance and the entity-level mitigations the firm has accepted.

- **Sub-contractor and fourth-party visibility for the model supply chain.** Foundation-model vendors typically depend on cloud infrastructure, training-data brokers, evaluation contractors, red-team contractors. The evidence pack should support the firm's understanding of the material fourth-party dependencies the model layer relies on. Record gaps; the entity-level fourth-party register sits in `vendor-diligence`.

- **Regulator-engagement history specific to AI/ML.** Where the vendor has engaged with banking regulators (OCC, FRB, FDIC) on AI/ML matters, comments to interagency RFIs, briefings, named participation in regulator pilots, the engagement-history field captures it. This is informational; it is not, by itself, a sufficiency criterion.

- **Model risk programme touchpoints.** The vendor's published model-card and system-card documentation should be sufficient for the firm's MRM function to perform its independent review work. Where vendor documentation falls short of MRM documentation expectations under the interagency guidance, the gap routes to a supplemental-evidence ask and to in-firm validation work under `validation-plan`.

- **Change-of-version notice with sufficient lead time.** Vendor model-version swap is a material change for the bank's MRM programme. The evidence pack should establish the vendor's notice cadence and the practical re-validation runway it leaves. The change-and-version-control criterion in `sufficiency_view[]` reads against this.

## Sector-specific co-reviewer expectations

For bank-affiliated entities, the model-risk function (MRMO) is a co-reviewer alongside the AI Governance Lead; the evidence-pack review is filed only after both attest. Where the vendor's model is consumed across multiple business lines, the business-line model owners are informed but the central MRM function holds the attestation gate. For NY-footprint subsidiaries the CISO function co-reviews the security and privacy criteria; for any deployment touching credit decisioning or fair-lending-relevant decisioning, the consumer compliance function (CCO) is informed and the conduct overlay loads.

## Sector-specific re-review triggers

In addition to the baseline triggers, banking adds:

- Bank examination feedback referencing the vendor or model.
- New or revised interagency guidance materially affecting AI/ML vendor expectations.
- Vendor or vendor-class supervisory action (consent order, CMP) by a federal banking regulator.
- Material change in the bank's own model risk programme classification of the use case.

## Sector-specific structured-output additions

The `sector_overlay_notes` block in the schema carries the bank-specific findings:

```
"sector_overlay_notes": {
  "examination_evidence_posture": "...",
  "audit_rights_depth": "...",
  "fourth_party_visibility_gaps": [...],
  "regulator_engagement_history_summary": "...",
  "mrm_function_attestation_status": "..."
}
```

The fields are populated by the reviewer; the AI Governance Lead and MRMO sign off jointly.
