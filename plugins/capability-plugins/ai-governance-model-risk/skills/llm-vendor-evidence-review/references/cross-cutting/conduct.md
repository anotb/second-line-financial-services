# Cross-cutting overlay: conduct

Loaded when `scope.cross_cutting_overlay_set` includes conduct. Carries the responsible-use, harmful-content, and customer-conduct frame for foundation-model vendor evidence-pack review. Scopes in for any deployment touching customer-facing communications, recommendation, or decisioning.

## Supervisory frame

The conduct framings most often in scope:

- **CFPB Circulars and supervisory highlights** for entities in CFPB scope. The adverse-action notice circular, the chatbot circular, and named circulars on AI-driven decisioning carry the CFPB's published views on AI-vendor decisions affecting consumers.
- **UDAAP** (Dodd-Frank §1031, §1036, FTC Act §5) reaches AI-driven content and decisioning that may be unfair, deceptive, or abusive. Foundation-model behaviour around hallucination, off-label financial advice, and refusal-around-restricted-content feeds the firm's UDAAP exposure assessment.
- **Fair-lending regimes** (ECOA / Reg B, FHA, state analogues) for any AI-vendor use in credit decisioning, marketing, or adverse-action determinations.
- **Telephone and electronic-communication regimes** (TCPA, CAN-SPAM, state anti-robocall) for AI-vendor use in customer outreach, where the model produces or selects message content.
- **State UDAP regimes** that layer on for state-licensed entities.
- **Sector-specific conduct regimes**: SEC Marketing Rule and FINRA Rule 2210 for capital-markets entities (carried in the capital-markets sector overlay); NAIC Unfair Trade Practices model and state insurance unfair-trade-practices acts for insurers; CFPB Regulation Z and Regulation E disclosures for consumer credit and electronic fund transfers.

The leading-practice references with weight in this scope: NIST AI 600-1 Manage subcategories on harmful-content management; vendor-published responsible-use policies and acceptable-use rules; vendor-published trust-and-safety pages on harm taxonomies and refusal behaviour.

## Conduct-specific evidence asks

The conduct overlay surfaces the following beyond the cross-cutting baseline in the responsible-use-policy, evaluation-coverage (harmful-content-specific), and dangerous-capability-evaluations criteria:

- **Vendor harmful-content evaluation depth.** Vendor's published evaluation methodology and results on harmful-content categories relevant to the firm's deployment: financial-services-specific harmful content (off-label investment advice, unauthorised regulated-product solicitation, fabricated terms), consumer-protection-relevant content (false promises, misleading product descriptions, misrepresentation), conduct-relevant content (harassment, discriminatory output, off-policy solicitation). General-purpose harmful-content evaluation is starting context; financial-services-specific or domain-specific coverage is firm-side responsibility under `validation-plan` if vendor coverage is partial.

- **Refusal-behaviour calibration around restricted-use categories.** Vendor's published refusal-behaviour around regulated activities the firm is exposed to (giving investment advice, making loan-eligibility determinations, medical claims, immigration claims, legal advice). Where vendor refusal-behaviour is calibrated to categories the firm wants the model to engage with, the firm-side prompting and downstream-control architecture carries the responsibility; record the gap.

- **Adverse-action and explanation-depth posture.** For AI-vendor use in or adjacent to credit, insurance underwriting, or consumer-financial-services decisioning, vendor evidence on output-explanation-depth and refusal-around-determinative-statements feeds the firm's adverse-action-notice and reason-code obligations. The CCO and consumer-compliance function carry the regulatory-fit assessment; the evidence-pack review surfaces the inputs.

- **Marketing and communications posture.** Vendor's posture on output-control around marketing-relevant content (testimonials, performance claims, recommendations), and the vendor's acceptable-use rules around the use of the model for marketing automation. For SEC/FINRA-scope entities, this routes to the capital-markets sector overlay; for retail consumer-financial-services entities, the firm's marketing compliance function is in the room.

- **Bias and fairness evidence relevant to the deployment.** Vendor's published bias evaluations and fairness methodology; in many cases generic and not domain-specific, in which case domain-specific evaluation under `validation-plan` carries the firm-side coverage. For insurance and consumer-credit deployments the sector overlays add specific elements.

- **Acceptable-use enforcement posture.** Vendor's process for monitoring and enforcing its acceptable-use policy: how the vendor identifies misuse, what enforcement actions are available, how disputes are handled. Material for the firm's understanding of vendor reliability around restricted-use categories and for the firm's own enforcement of its acceptable-use policy.

## Conduct-specific co-reviewer expectations

The CCO is a co-reviewer for any deployment touching consumer-facing communications, recommendation, or decisioning. For sector-specific conduct overlays (SEC Marketing Rule, FINRA Rule 2210, NAIC unfair trade practices), the relevant sector function is in the room. For BSA-relevant decisioning, the BSA officer is in the room (and is also a co-reviewer per the payments-fintech sector overlay where applicable).

The consumer compliance function (Fair Lending officer, ECOA-compliance officer where named) co-reviews where the deployment touches credit decisioning or fair-lending-relevant decisioning. The CCO and the AI Governance Lead jointly attest on `reviewer_attestation`; for fair-lending-touching deployments the consumer-compliance function joins the attestation gate.

## Conduct-specific re-review triggers

In addition to the baseline triggers, conduct adds:

- New or revised CFPB circular, FTC enforcement guidance, or sector-specific conduct rule materially affecting AI-vendor decisions in scope.
- Vendor change to acceptable-use policy, responsible-use policy, restricted-use enforcement, or harmful-content evaluation methodology.
- Vendor incident or supervisory action involving conduct-relevant outputs.
- Material change in the deployment scope towards consumer-facing communication or decisioning.

## Conduct-specific structured-output additions

The `cross_cutting_overlay_notes.conduct` block in the schema carries the conduct-specific findings:

```
"cross_cutting_overlay_notes": {
  "conduct": {
    "harmful_content_evaluation_summary": "...",
    "refusal_behaviour_calibration_summary": "...",
    "adverse_action_explanation_depth": "...",
    "marketing_and_communications_posture": "...",
    "bias_and_fairness_evidence_summary": "...",
    "acceptable_use_enforcement_posture": "...",
    "udaap_exposure_input": "...",
    "consumer_compliance_function_attestation_status": "..."
  }
}
```
