# Conduct cross-cutting overlay for genai-pre-prod-review

When the engagement-scope record flags `conduct` for a pre-prod gate review, this overlay adds conduct-specific gate considerations: consumer-compliance co-review, fairness and harmful-content posture, complaint-readiness, and recommended-action items typical of conduct-flagged GenAI gate reviews. Loaded for any use case generating or assisting customer-facing communications, or making or supporting decisions that affect consumer outcomes.

Loaded by: `genai-pre-prod-review/SKILL.md` when `engagement_scope.cross_cutting_set` includes `conduct`. Cited and section-referenced anchors live in `references/source-anchors.md`.

## Source basis

- CFPB UDAAP authority under the Consumer Financial Protection Act and the FTC Act §5 (12 USC §5531 and 15 USC §45) for unfair, deceptive, or abusive acts or practices.
- CFPB Circulars and Bulletins on AI-related consumer-compliance considerations (e.g., CFPB Circular 2022-03 on adverse-action notices and AI; CFPB Circular 2023-03 on adverse-action accuracy under ECOA; CFPB Bulletin and policy statements on AI in chatbots and customer service).
- ECOA / Reg B (12 CFR Part 1002) and the Fair Housing Act for credit-decisioning use cases; adverse-action accuracy and fair-lending exposure.
- Reg E (12 CFR Part 1005) for AI-assisted dispute handling on electronic fund transfers.
- Reg Z (12 CFR Part 1026) for credit-product communication exposure.
- SEC Investment Adviser Marketing Rule (Rule 206(4)-1) and Reg BI for investment-recommendation-adjacent use cases.
- FINRA Rule 2210 (communications with the public) for broker-dealer use cases.
- State unfair-discrimination statutes (NAIC Model #880 vocabulary) for insurance underwriting and pricing use cases.
- State insurance advertising rules and state suitability requirements for insurance customer-facing use cases.
- State consumer-protection laws (state UDAP analogues) for state-licensed non-bank financial entities.
- For NY-licensed insurers: NYDFS Insurance Circular Letter (January 2024) on ECDIS and underwriting fairness.
- For Colorado life insurance: SB 21-169 implementing regulation on unfair-discrimination governance for predictive models.

## Co-reviewer expectation

Consumer compliance is a co-signer on the gate decision for any conduct-flagged use case. For credit-decisioning use cases the fair-lending function (within consumer compliance or a separate fair-lending office) is also a co-signer. For insurance underwriting and pricing use cases the chief actuarial officer is a co-signer for the unfair-discrimination seam.

For tier-1 use cases the head of consumer compliance or chief compliance officer is named on the sign-off block; the gate decision does not proceed without that role.

## What changes when conduct is flagged

### Open conditions the overlay typically adds

- UDAAP output-filter specification signed off by consumer compliance for any consumer-facing communication generated or assisted by the system.
- Adverse-action notice quality review for any credit-decisioning use case where the AI affects the adverse-action reason or score; CFPB Circular 2022-03 and 2023-03 set the quality bar.
- Fair-lending integration: the consumer-compliance fair-lending test plan and the gate review reference each other; fair-lending residual risk is recorded in the gate residual-risk section with the fair-lending owner.
- For insurance underwriting and pricing: unfair-discrimination output-filter specification signed off by the underwriting actuary; the chief actuarial officer signs the residual-risk acceptance for unfair-discrimination exposure.
- Complaint-channel readiness: consumer-recourse channel covers AI-relevant complaints; complaint-coding includes AI-specific codes for downstream signal.
- Refusal and deflection-behaviour review: documented refusal posture for out-of-scope queries (e.g., legal advice, medical advice, regulated-product recommendations beyond Reg BI scope, financial advice beyond SR/IA fiduciary scope); appropriate to the audience.
- For multi-state operations: state consumer-protection-law alignment matrix.

### Monitoring readiness adds the conduct-tagged signal set

In addition to the standard signal set:

- Complaint-rate and complaint-code drift; specific AI-relevant complaint codes (e.g., misleading communication, refused or deflected legitimate request, harmful content); escalation to consumer compliance.
- UDAAP output-filter trip rate; escalation to consumer compliance.
- For credit-decisioning: adverse-action notice quality sampling; escalation to fair-lending function.
- For insurance underwriting and pricing: unfair-discrimination output-filter trip rate; escalation to chief actuarial officer.
- For investment-recommendation-adjacent: Marketing Rule output-filter trip rate; escalation to chief compliance officer.
- Refusal-rate sampling on out-of-scope queries; escalation to AI governance team with consumer compliance.

### Incident-response readiness names conduct-specific notification and remediation triggers

The `incident_response_readiness.regulator_notification_triggers` list adds:

- CFPB UDAAP-relevant event triggers if AI-assisted output causes an unfair, deceptive, or abusive practice with material consumer harm; the firm's consumer-complaint-handling and regulatory-affairs functions evaluate.
- Adverse-action notice integrity event triggers under ECOA / Reg B if AI-driven output causes an inaccurate or non-compliant adverse-action notice.
- For insurance: state DOI notification triggers for unfair-discrimination events affecting underwriting or pricing decisions.
- For investment recommendations: SEC self-reporting expectations under SEC Enforcement guidance where AI-assisted communications cause material misleading statements; FINRA Rule 4530 reporting where applicable.
- Reg E integrity triggers if AI-assisted dispute handling causes a procedural failure that affects a consumer's rights under Reg E.
- Customer remediation framework: for material consumer-impact events, the firm's customer remediation framework activates (file-and-resolve, restitution, regulator notification per the relevant overlay).

The IR drill scope before go-live should exercise at minimum one conduct-specific incident class (e.g., confirmed UDAAP-relevant misleading communication; confirmed adverse-action notice integrity issue for credit-decisioning; confirmed unfair-discrimination event for insurance underwriting).

### Recommended-action items the overlay surfaces

- UDAAP output-filter specification documented and signed off; consumer compliance co-signs.
- For credit-decisioning use cases: fair-lending integration explicit and documented; adverse-action notice quality sampling pipeline live before go-live.
- For insurance use cases: unfair-discrimination output-filter and the underwriting-actuary sign-off documented; state insurance advertising rule output-filter documented for customer-facing use cases.
- Complaint-channel readiness documented; complaint coding includes AI-relevant codes.
- For investment-recommendation-adjacent: Marketing Rule and Reg BI fiduciary-lens framing documented; chief compliance officer signs.
- For multi-state operations: state-by-state consumer-protection-law alignment matrix documented; consumer compliance signs off on per-state readiness.

## Conduct-specific output additions

In the structured object (`schemas/genai-pre-prod-review.schema.json`):

- `cross_cutting_overlay_notes.conduct` carries conduct-specific fields: UDAAP output-filter specification status, adverse-action notice quality review status, fair-lending integration status, unfair-discrimination output-filter status, complaint-channel readiness status, refusal posture documentation status.
- `signoff[]` array includes consumer compliance as a co-signer; fair-lending function for credit use cases; chief actuarial officer for insurance underwriting and pricing use cases.
- `monitoring_readiness[]` entries with conduct-tagged escalation path (consumer compliance, fair-lending function, chief actuarial officer where applicable).
- `incident_response_readiness.regulator_notification_triggers` populated with the named conduct-specific triggers.
- `overlay_signoffs[]` includes a conduct entry with named owner role.

## Common pitfalls in conduct-flagged pre-prod gate reviews

- Treating UDAAP exposure as a downstream consumer-compliance review. UDAAP is the seat consumer compliance owns at the gate, not after; the gate decision is incomplete without consumer compliance sign-off.
- Treating fair-lending as a separate workstream that runs after AI gate. For credit-decisioning use cases the fair-lending integration is a gate-time co-review; the gate review's residual-risk section names the fair-lending residual risk explicitly.
- Treating refusal behaviour as a vendor-side concern. The refusal posture is firm-side configuration (system prompt, guardrails, output filtering) and a firm-side gate decision; vendor refusal behaviour is one input.
- Recording adverse-action notice quality as compliant by assertion. CFPB Circular 2022-03 and 2023-03 set a substantive quality bar; the gate review records sampling evidence, not assertion.
- Treating complaint-channel readiness as a downstream concern. Complaint channels need AI-relevant codes live before go-live so the post-go-live signal exists; adding the codes after a complaint surfaces is too late.
- Omitting the chief actuarial officer co-signature on insurance underwriting and pricing use cases. The unfair-discrimination seam is the chief actuarial officer's seat; the gate decision is incomplete without it.
- Treating multi-state operations as having a uniform consumer-protection posture. State UDAP statutes and state insurance advertising rules vary; the gate review records state-by-state status.
