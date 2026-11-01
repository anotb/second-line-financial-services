# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Sector overlay: banking

Loaded when `scope.sector_overlay_set` includes banking. Carries the bank-vendor-specific frame for foundation-model evidence-pack review: the supervisory perspective bank examiners take on third-party model evidence, the entity-level wrapper that the interagency third-party guidance imposes, and the specific evidence asks that bank-vendor reviews surface in addition to the cross-cutting baseline.

#### Supervisory frame

Bank model risk programmes interpret the federal interagency model risk guidance (Federal Reserve SR 11-7 and the parallel OCC bulletin) as carrying expectations for vendor and third-party models. Where the firm's MRM programme treats the foundation-model use case as in scope of model risk, vendor evidence-pack review becomes part of meeting the third-party model expectations: documentation and validation evidence sufficient to support the firm's own validation work, with awareness that proprietary vendor methods may limit the depth of validation evidence available.

The 2026 revised interagency model risk guidance refreshes these expectations for AI/ML and generative AI; section references for the AI/ML and third-party model passages are tracked in `references/source-anchors.md` with `[verify section]` flags pending confirmation.

The interagency third-party risk-management guidance (June 2023) is the entity-level wrapper. The vendor-diligence record under `vendor-diligence` in `third-party-operational-resilience` carries the entity-level diligence; this evidence-pack review is the model-evidence layer that chains from `eval_evidence_status = deferred-to-evidence-review`.

The FFIEC IT Examination Handbook applies as the IT-and-information-security frame for the bank-vendor relationship; relevant booklets are Information Security and Architecture, Infrastructure, and Operations. For NY-footprint subsidiaries, 23 NYCRR Part 500 §500.11 (third-party service-provider security) layers on; the cyber overlay carries that detail.

#### Sector-specific evidence asks

The bank-vendor frame surfaces the following beyond the cross-cutting baseline:

- **Examination evidence rights.** The vendor evidence pack should be readable in a bank examination. Where the vendor restricts evidence to NDA-only, the contract should preserve the firm's ability to share specified evidence with examiners under examiner-confidentiality protections. Record the contract clause status here, not in the entity-level diligence.

- **Audit and assessment rights covering the model layer.** The interagency third-party guidance expects audit rights to extend to the activities the vendor performs on behalf of the bank. For a foundation-model vendor, this includes the right to receive evidence on adversarial robustness, evaluation methodology, and red-team scope at the depth the bank's model risk function needs. Where vendor practice limits audit-right depth (typical for major foundation-model providers' published-evidence model), record the residual reliance and the entity-level mitigations the firm has accepted.

- **Sub-contractor and fourth-party visibility for the model supply chain.** Foundation-model vendors typically depend on cloud infrastructure, training-data brokers, evaluation contractors, red-team contractors. The evidence pack should support the firm's understanding of the material fourth-party dependencies the model layer relies on. Record gaps; the entity-level fourth-party register sits in `vendor-diligence`.

- **Regulator-engagement history specific to AI/ML.** Where the vendor has engaged with banking regulators (OCC, FRB, FDIC) on AI/ML matters, comments to interagency RFIs, briefings, named participation in regulator pilots, the engagement-history field captures it. This is informational; it is not, by itself, a sufficiency criterion.

- **Model risk programme touchpoints.** The vendor's published model-card and system-card documentation should be sufficient for the firm's MRM function to perform its independent review work. Where vendor documentation falls short of MRM documentation expectations under the interagency guidance, the gap routes to a supplemental-evidence ask and to in-firm validation work under `validation-plan`.

- **Change-of-version notice with sufficient lead time.** Vendor model-version swap is a material change for the bank's MRM programme. The evidence pack should establish the vendor's notice cadence and the practical re-validation runway it leaves. The change-and-version-control criterion in `sufficiency_view[]` reads against this.

#### Sector-specific co-reviewer expectations

For bank-affiliated entities, the model-risk function (MRMO) is a co-reviewer alongside the AI Governance Lead; the evidence-pack review is filed only after both attest. Where the vendor's model is consumed across multiple business lines, the business-line model owners are informed but the central MRM function holds the attestation gate. For NY-footprint subsidiaries the CISO function co-reviews the security and privacy criteria; for any deployment touching credit decisioning or fair-lending-relevant decisioning, the consumer compliance function (CCO) is informed and the conduct overlay loads.

#### Sector-specific re-review triggers

In addition to the baseline triggers, banking adds:

- Bank examination feedback referencing the vendor or model.
- New or revised interagency guidance materially affecting AI/ML vendor expectations.
- Vendor or vendor-class supervisory action (consent order, CMP) by a federal banking regulator.
- Material change in the bank's own model risk programme classification of the use case.

#### Sector-specific structured-output additions

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

## capital-markets

### Sector overlay: capital markets

Loaded when `scope.sector_overlay_set` includes capital-markets. Carries the broker-dealer and investment-adviser-specific frame for foundation-model evidence-pack review: SEC and FINRA visibility, surveillance and execution adjacency, books-and-records and Marketing Rule reach into AI-generated content.

#### Supervisory frame

Capital-markets entities are dual-supervised in different combinations: broker-dealers by FINRA and SEC, registered investment advisers by SEC (or state for sub-threshold), exchanges and ATSs by SEC, swap dealers by CFTC, FCMs and IBs by NFA and CFTC. The evidence-pack review is read against the supervisory constellation the scope identifies.

The SEC's published staff statements and risk alerts on AI use by registrants set the practical supervisory expectation in this scope: AI used in advisory, broker-dealer, surveillance, or fund-management functions falls within existing supervisory frameworks (Investment Advisers Act, Securities Exchange Act, Investment Company Act) and the related rules. There is, as of this skill's authoring, no SEC AI-specific final rule; published proposals and staff guidance are watched and tracked in `references/source-anchors.md`.

For investment advisers, the Marketing Rule (17 CFR 275.206(4)-1) and Books and Records Rule (17 CFR 275.204-2) reach into AI-generated client-facing content; vendor evidence on output-control posture and refusal behaviour around marketing-relevant outputs feeds the firm's compliance assessment. For broker-dealers, FINRA Rule 3110 supervision and Rule 2210 communications-with-the-public obligations carry the analogous lens.

For any AI use in surveillance, trade execution, or order-handling, FINRA Rule 3110 supervision expectations and SEC Rule 15c3-5 (market access rule) carry direct relevance; the evidence-pack review supports the firm's assessment of whether vendor evidence is sufficient for a use case within those rules' scope.

For investment companies (mutual funds, ETFs, closed-end funds), the fund board's oversight of service providers under the Investment Company Act and Rule 38a-1 compliance programme touches vendor-AI considerations; fund-board visibility and reporting cadence are relevant for fund-touching deployments.

#### Sector-specific evidence asks

The capital-markets-vendor frame surfaces the following beyond the cross-cutting baseline:

- **Output-control evidence for marketing-relevant uses.** Where the foundation-model deployment produces or assists with content that may be subject to the Marketing Rule (for advisers) or Rule 2210 (for broker-dealers), the evidence pack should establish the vendor's output-control posture: refusal behaviour around performance claims, testimonial-handling, recommendation language. The firm's compliance function performs the regulatory-fit assessment; the evidence-pack review surfaces the inputs.

- **Surveillance and supervision adjacency.** Where the foundation model is consumed in or alongside surveillance systems (trade surveillance, communication surveillance, AML transaction monitoring), the evidence pack should establish the vendor's posture on output stability, false-positive and false-negative profile awareness, and explanation depth sufficient to support supervisory review under Rule 3110 or analogous frameworks. Record the gaps.

- **Books-and-records preservation reach.** AI-generated content used in regulated communications must be preserved per Rule 17a-4 (broker-dealers) or Rule 204-2 (advisers). The vendor's data-retention posture matters not only for privacy but for the firm's ability to meet preservation obligations. Where vendor default is short-window retention, the firm-side capture-and-preserve pattern carries the obligation; record the architecture in the evidence-pack review.

- **Fiduciary-lens framing for adviser-side use.** For investment advisers, the foundation-model deployment is read against the adviser's fiduciary duty (duty of care, duty of loyalty). Vendor evidence on output reliability and known failure modes feeds the firm's fiduciary-fit assessment; the firm's CCO carries the assessment, but the evidence-pack review surfaces the inputs.

- **Trading-system adjacency posture.** For deployments adjacent to order-handling or execution (smart-order-routing assist, pre-trade compliance assist), the evidence pack should establish the vendor's awareness of latency, determinism, and failure-mode requirements that pure-text-summarisation use cases do not impose. Where the vendor's model card or evaluation report is silent on these dimensions, record the gap and route the in-firm requirement-fit assessment to `validation-plan`.

- **Cross-border and reciprocity considerations.** For dual-registered entities (US adviser plus UK FCA, EU firms with passporting, APAC affiliates), the binding regulator constellation is layered. Loaded with this overlay; the cross-cutting privacy overlay carries the data-flow specifics.

#### Sector-specific co-reviewer expectations

The CCO is a co-reviewer for any deployment touching marketing, communications, or recommendation-relevant outputs. For broker-dealer entities, the CSO or named supervisory principal under FINRA Rule 3110 is informed where the use case touches surveillance or supervision. For fund-touching deployments, the fund board's CCO under Rule 38a-1 receives the evidence-pack review summary as part of the periodic compliance reporting cycle (not as a primary attestation). The AI Governance Lead retains the lead attestation; the named function-level co-attests are recorded in `reviewer_attestation`.

#### Sector-specific re-review triggers

In addition to the baseline triggers, capital-markets adds:

- SEC, FINRA, or CFTC enforcement action or risk alert referencing the vendor, vendor class, or use-case class.
- Final rule or amendment to AI-relevant adviser or broker-dealer rules (Marketing Rule, Rule 2210, supervision rules).
- Material change in the use case scope towards execution-adjacent or surveillance-adjacent deployment.
- Fund-board feedback on the deployment for fund-touching use cases.

#### Sector-specific structured-output additions

The `sector_overlay_notes` block in the schema carries the capital-markets-specific findings:

```
"sector_overlay_notes": {
  "registration_constellation": [...],
  "marketing_rule_or_2210_reach": "...",
  "supervision_and_surveillance_adjacency": "...",
  "books_and_records_preservation_posture": "...",
  "fiduciary_lens_summary": "...",
  "trading_system_adjacency_posture": "..."
}
```

## insurance

### Sector overlay: insurance

Loaded when `scope.sector_overlay_set` includes insurance. Carries the insurance-vendor-specific frame for foundation-model evidence-pack review: state-DOI supervisory visibility, NAIC Model Bulletin alignment, and the fairness-evidence and consumer-protection seams that insurance-vendor reviews surface in addition to the cross-cutting baseline.

#### Supervisory frame

State Departments of Insurance are the binding supervisor; insurance regulation in the US is state-based. The NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023) is the converged industry frame; binding to the extent the insurer's domicile and material-state regulators have adopted or signalled adoption. The state-adoption tracker maintained by the NAIC AI Working Group is the public reference.

The Bulletin's AIS Programme elements set the supervisory expectation around vendor AI: the insurer's AIS Programme must address third-party AI systems with named accountability, vendor risk-management procedures, evidence on testing and validation, monitoring of vendor systems in production, and documentation. The vendor evidence-pack review feeds the AIS Programme's third-party-AI accountability and testing-and-validation elements.

State-specific AI rules (Colorado SB 21-169 and the Division of Insurance regulations on algorithmic discrimination, New York DFS Insurance Circular Letter on consumer protection in AI use, California Department of Insurance bulletins) layer on for in-scope insurers; the state-by-state binding-status check is part of every review.

The state Insurance Data Security Model Law (NAIC Model Law 668), where adopted in the relevant state, applies to information-security posture for insurer use of third-party providers; the cyber overlay carries the named provisions.

#### Sector-specific evidence asks

The insurance-vendor frame surfaces the following beyond the cross-cutting baseline:

- **Fairness and bias evidence relevant to insurance uses.** Where the foundation model is consumed in underwriting, claims, marketing, or any use class within scope of state algorithmic-discrimination regulation, the evidence-pack review surfaces the vendor's published fairness evaluations and testing methodology. General-purpose fairness evaluations are starting context; insurance-domain fairness evaluation is firm-side responsibility under the AIS Programme.

- **Consumer-protection and explainability posture.** The vendor's published documentation on model-output interpretability, refusal behaviour around adverse-action-relevant outputs, and downstream-consequence-aware design feeds the insurer's compliance with adverse-action notice and reason-code obligations. The evidence-pack review surfaces the documentation; the insurer's compliance function performs the regulatory-fit assessment.

- **Sensitive-class and inference-risk posture.** Foundation-model behaviour around protected-class inference (race, ethnicity, health status, genetic information) is relevant to insurance use cases that touch underwriting or rating. The evidence pack should establish the vendor's awareness and any documented mitigations; firm-side controls under `prompt-injection-risk` and `validation-plan` carry the in-firm enforcement.

- **State-of-deployment posture for cross-border data flows.** Insurance regulation of data residency varies by state and by line of business (P&C, life, health). Where the vendor processes prompts or training-data-derivative artefacts in jurisdictions outside the deployment state, the vendor evidence pack should describe the data-flow posture; the privacy overlay carries the named state-by-state implications.

- **NAIC Model Bulletin AIS Programme element mapping.** For each named AIS Programme element (governance and risk management, AI vendor accountability, AIS testing and validation, AIS monitoring and oversight, documentation), the evidence-pack review surfaces the vendor evidence that supports the element. Element-by-element mapping is part of the structured-output `sector_overlay_notes`.

- **HIPAA business-associate posture for health-relevant lines.** For life and health lines where PHI may flow to the vendor (or be inferable from claims narratives), HIPAA business-associate considerations apply; the cyber and privacy overlays carry the named obligations.

#### Sector-specific co-reviewer expectations

The state-regulated insurance entity's chief actuary or chief risk officer is a co-reviewer where the use case affects pricing, reserving, or solvency. The chief compliance officer co-reviews where the use case affects consumer-facing or producer-facing communications. For health-touching deployments, the privacy office (HIPAA-compliant officer) co-reviews. The evidence-pack review is filed only after the AI Governance Lead and named co-reviewers attest.

#### Sector-specific re-review triggers

In addition to the baseline triggers, insurance adds:

- State-DOI feedback referencing the vendor or model.
- New or revised state algorithmic-discrimination regulation or NAIC Model Bulletin amendment materially affecting third-party AI expectations.
- Material change in the vendor's posture on fairness evaluations or sensitive-class inference.
- Material change in the line-of-business deployment scope (e.g., expansion from claims summarisation to claims decisioning).

#### Sector-specific structured-output additions

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

## payments-fintech

### Sector overlay: payments and fintech

Loaded when `scope.sector_overlay_set` includes payments-fintech. Carries the payments-and-fintech-specific frame for foundation-model evidence-pack review: sponsor-bank visibility, BSA programme coverage of vendor-driven decisions, money-transmitter licensing constellation, and the bank-fintech-shared-responsibility seams that surface in vendor-AI deployments.

#### Supervisory frame

The payments-and-fintech supervisory constellation depends on the entity:

- **Bank-as-a-service sponsor banks** carry the underlying federal banking supervisory frame (OCC, FRB, FDIC) plus state-by-state implications for sponsored fintech activity. The interagency third-party risk-management guidance (June 2023) is binding; the bank's vendor-diligence record carries the entity-level frame.
- **Sponsored fintechs** are not directly federally supervised in most cases but carry obligations through the sponsor-bank relationship; the sponsor bank is the firm responsible for ensuring AI vendor evidence is sufficient. State-level supervisory regimes (state money-transmitter licences, state consumer-financial-services regulators) add layers.
- **Money transmitters and money-services businesses** are state-licensed plus federally supervised under FinCEN's BSA programme requirements; AI use in transaction monitoring, fraud, or sanctions is read against BSA programme expectations.
- **Card networks, processors, and PSPs** carry contractual obligations to issuers and merchants in addition to direct supervision; the network rules carry weight for AI use in fraud, dispute, or chargeback processing.

The CFPB has supervisory and enforcement authority over a defined set of nonbank financial-services participants (larger nonbank market participants under named CFPB rules, plus enforcement reach over any covered persons). For consumer-facing payments and lending, the regulatory text (Reg B §1002.9 adverse-action; UDAAP §1031; Reg E §1005.11) drives AI-vendor-decision postures; CFPB Circulars on adverse-action notices with complex algorithms (2022-03 / 2023-03) and the BNPL interpretive rule (May 2024) are **withdrawn / nullified (May 2025); historical only**, and the underlying regulatory text continues to apply on its own terms.

The OCC's "true lender" framework and state-by-state UDAP regimes carry implications for bank-fintech lending models; AI-vendor-driven underwriting falls under existing fair-lending frameworks (ECOA, FHA, state analogues) that require vendor evidence to support the firm's compliance assessment. The conduct overlay carries the named obligations.

#### Sector-specific evidence asks

The payments-and-fintech frame surfaces the following beyond the cross-cutting baseline:

- **Sponsor-bank visibility into vendor evidence.** For sponsored fintech relationships, the sponsor bank's vendor-diligence and model risk programme reach into the fintech's AI vendors. The evidence-pack review surfaces what the sponsor bank can see and what the fintech holds at fintech-level. Where the fintech is the firm running the review, the sponsor-bank reporting and notification posture is in scope.

- **BSA programme coverage of vendor-driven decisions.** Where the foundation-model use case touches transaction monitoring, sanctions screening, customer due diligence, or SAR-relevant decisioning, the BSA officer is a co-reviewer and the evidence-pack review records the BSA programme touchpoints. Vendor evidence on model behaviour around BSA-relevant outputs (false-positive profile awareness, explanation depth for SAR support) is part of the supplementary ask.

- **Fraud-model and dispute-model adjacency.** For deployments adjacent to fraud or dispute-handling, the vendor evidence pack should support the firm's understanding of the model's interaction with adversarial fraud actors. Generic vendor evals do not cover fraud-model adversarial postures; record the gap and route to `validation-plan` for the firm-side fraud-domain evaluation.

- **State licensing constellation.** For multi-state money-transmitter or sponsored-fintech entities, the binding-state list materially affects the regulator-engagement-history and rereview-trigger posture. The evidence-pack review captures the constellation; the entity-level diligence in `vendor-diligence` carries the licence-by-licence detail.

- **PCI scope and tokenisation posture.** Where the foundation-model deployment touches cardholder data or payment-card-relevant communications, PCI DSS scope considerations apply. The vendor evidence pack should establish the vendor's PCI-relevant posture (scope-in vs scope-out) and the firm-side tokenisation pattern that keeps PCI scope contained.

- **Network rules and assessor obligations.** For card-network-touching deployments, network rules (Visa, Mastercard, network-of-record) carry obligations on assessment cadence and incident notification; the cyber overlay carries the named provisions.

#### Sector-specific co-reviewer expectations

The BSA officer is a co-reviewer for any deployment touching BSA-relevant decisioning. For sponsored fintech entities, the sponsor-bank's TPRM function and AI Governance Lead are informed and the contract-defined approval chain runs in parallel. The CCO is a co-reviewer for any consumer-facing deployment touching CFPB or state-UDAP scope. The AI Governance Lead retains the lead attestation; named co-attests are recorded in `reviewer_attestation`.

#### Sector-specific re-review triggers

In addition to the baseline triggers, payments-and-fintech adds:

- CFPB enforcement action, supervisory highlight, or new circular materially affecting AI-vendor decisions in scope.
- Sponsor-bank-driven re-attestation cycle or sponsor-bank feedback on the vendor.
- New or revised state money-transmitter or fintech-specific regulation in a binding state.
- Material change in the BSA programme classification of the use case.
- Card network rule update materially affecting AI use in network-touching processes.

#### Sector-specific structured-output additions

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
