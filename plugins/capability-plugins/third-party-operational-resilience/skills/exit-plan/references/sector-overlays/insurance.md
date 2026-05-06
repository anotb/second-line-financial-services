# Insurance sector overlay — exit-plan

When the engagement scope flags insurance, load this overlay alongside `references/source-anchors.md`. The bank-flavoured interagency-guidance termination frame is not the operative supervisory frame for state-regulated insurers.

## Operative supervisory frame

- **State insurance department oversight** — the operative regulatory relationship is state-by-state. The exit plan reflects the carrier's domiciliary regulator first, then material-state regulators where the transition affects in-force policyholders.
- **NAIC Insurance Holding Company System Regulatory Act (Model #440)** [verify model number] and **Holding Company Model Regulation (Model #450)** [verify model number]: where the vendor is an affiliate of the carrier, transition triggers Form B / Form D filings.
- **NAIC Insurance Data Security Model Law (Model #668), §4.F** — third-party service-provider obligations including transition data-handling. State-by-state adoption.
- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number] — critical outsourced functions sit in the ORSA. A vendor-transition affecting a critical outsourced function updates the ORSA Summary Report.

## Policyholder-facing transitions

- **Policy administration platform exit** — the most common high-impact insurance vendor transition. Considerations:
  - Portability of policy administration data, in-force-policy schedules, billing histories, and claims-in-flight state.
  - Customer-facing change-of-servicer notice. Required content and timing vary by state and product line; pin to the operative state insurance code on the day [verify state-by-state].
  - Producer-channel notice where the producer relationship rides on the platform (commission accruals, agent-of-record tagging).
- **Claims TPA transition** — claims-handling continuity is policyholder-facing on the day. Considerations:
  - In-flight claim handover with the seam dated for state-of-record purposes.
  - Reserve continuity (case reserves and IBNR) across the cutover; actuarial sign-off on the substitute TPA's reserve methodology.
  - Reinsurance reporting continuity — ceded-reinsurance reporting must cover both legs of the transition.
  - Statutory unfair-claims-practices clocks continue to run during transition.
- **Pricing and underwriting vendor transition** — for life and health, ECDIS / predictive-model vendor transitions trigger:
  - **Colorado SB 21-169** governance considerations (3 CCR 702-10 §1 [verify section]) for life-insurance underwriting models.
  - **NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting** (January 2024) [verify exact circular number] considerations.
  - The substitute model's diligence and validation belong to model-risk management; chain to `vendor-diligence` and to `ai-governance-model-risk/validation-plan` as appropriate.

## Guaranty-fund and policyholder-protection considerations

- State guaranty associations protect policyholders on insolvency of a carrier; vendor exit at a healthy carrier does not trigger guaranty-fund mechanics, but the customer-facing communications must avoid implying an insolvency posture.
- Where the transition is driven by carrier financial distress, the state insurance department leads and the exit plan becomes a sub-plan of the broader resolution work.

## Affiliate-vendor transition

- Where the vendor is an affiliate (Form B / Form D filings on the way in), termination requires Form D filings and may trigger state regulator review under the Holding Company Model Act.
- Affiliate cost-allocation arrangements and tax-sharing implications belong in the plan even when the operational migration is straightforward.

## AI vendor mode at an insurer

When `ai_vendor=true` and the firm is an insurer:

- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers** (December 4, 2023). Carrier accountability for vendor and third-party AI continues through transition. The substitute vendor's AIS Program elements (governance, risk management, testing, validation, third-party-AI accountability, monitoring, documentation, transparency, fairness) are part of the substitute-vendor viability read.
- **State adoption tracker** — the NAIC AI Working Group adoption tracker is the public reference. Transition timing must respect any state-specific notification or filing on AI use changes [verify state-by-state].
- Cross-link to `ai-governance-model-risk/llm-vendor-evidence-review` for the substitute model's evidence-pack review.
- For Annex III high-risk classification under the EU AI Act (insurance pricing and risk-assessment in life and health) where applicable, transition planning must address regulatory continuity for the substitute system [verify Annex III item number].

## Cross-link inside the plugin

- **`vendor-diligence` insurance overlay** carries the diligence depth the exit plan consumes.
- **`contract-gap-review` insurance overlay** carries the NAIC Model #668 §4.F clause set and the affiliate-vendor termination clauses.
- **`concentration-risk-review`** flags claims-TPA, policy-administration-platform, and ECDIS-vendor concentration that drives substitute-vendor viability.

## Output-template additions for insurance

- Domiciliary regulator and material-state regulator notification posture as a named line under regulator notice.
- Producer-channel notice as a named line under customer notice.
- ORSA-update trigger flag where the vendor supports a critical outsourced function.
- Form B / Form D filing trigger for affiliate-vendor termination.
- For claims TPA transitions, in-flight-claim handover with reserve-continuity and reinsurance-reporting lines.

## Common pitfalls in insurance exit planning

- Treating insurance vendor exit as a bank-style transition. The state regulatory lens, the policyholder-facing notice considerations, and the affiliate-vendor filing path are insurance-specific.
- Skipping the producer-channel notice. The producer relationship is part of the transition impact on a policy-administration-platform exit.
- Missing the in-flight-claim handover seam on a TPA transition. State-of-record continuity for unfair-claims-practices clocks, reserves, and reinsurance reporting must be dated.
- Treating an ECDIS or pricing-model vendor exit as a routine vendor exit. State AI governance and model-risk continuity are part of the plan.
- Missing the ORSA-update trigger on transition of a critical outsourced function.
