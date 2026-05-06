# Insurance sector overlay — resilience-testing-pack

When the engagement scope flags insurance, load this overlay alongside `references/source-anchors.md`. It carries the insurance-only frame the generic capability skill does not own.

## Operative supervisory frame

- **NAIC Insurance Data Security Model Law (Model #668), §4.F** third-party service-provider obligations. State-by-state adoption; firms operating in multiple states pin the operative state's adoption.
- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number]. Critical outsourced functions and their resilience posture are reflected in the ORSA Summary Report; material test failures may move ORSA conclusions.
- **NAIC Insurance Holding Company System Regulatory Act (Model #440)** [verify model number] and Holding Company Model Regulation (Model #450) [verify model number]. Form B / Form D considerations on affiliated-vendor arrangements that are tested.
- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers** (December 4, 2023). AIS Program elements include testing of third-party AI systems; resilience testing of AI-vendor arrangements feeds the AI-governance reporting line.
- **State-specific market-conduct expectations on claims-handling continuity**. Most states expect a documented BCDR posture for claims-handling; resilience testing demonstrates that posture.
- **EIOPA Guidelines on outsourcing to cloud service providers (2020)** [verify reference] for EU insurers; outsourcing-test posture similar in substance to the EBA cloud-outsourcing frame.

## IBS-level scenarios common at insurers

- Claims-handling outage during high-volume event (catastrophe, cyber-event, market dislocation).
- Policy-administration vendor outage during the renewal cycle for the affected lines.
- TPA outage on a high-claims-volume line (auto, home, health).
- Reinsurance-portal outage during the cession-and-claims cycle.
- AI-vendor regression on underwriting or claims-triage models (where AI is in the chain).
- Document-management-vendor outage during the renewal-and-statement cycle.

## Customer-impact considerations during a test

A test of claims-handling that surfaces real customer impact has direct policyholder consequences. Safety controls:

- Customer-impact-threshold for early termination set against the policyholder-protection statute in the operative state.
- Pre-positioned policyholder-comms templates for any test that may surface real claims-handling delay.
- Coordination with customer-experience and consumer-affairs functions before live tests on customer-affecting paths.

## ORSA reporting alignment

- Material test results on critical outsourced functions feed the ORSA Summary Report. Track which test outcomes meet the ORSA materiality threshold the firm has set; surface them to the ERM committee for inclusion in the next ORSA cycle.
- Material vendor-test failures and the remediation status are commonly inside the ORSA narrative on operational risk and outsourcing.

## AI-vendor testing at an insurer

When `ai_in_scope=true` and the firm is an insurer:

- **NAIC AI Bulletin** (December 2023) testing-and-validation expectations apply to third-party AI; the resilience pack covers vendor-AI continuity (model deprecation, regression, training-data incident) alongside the firm's own AI-governance-driven testing of model performance.
- **Colorado SB 21-169 implementing regulation** (3 CCR 702-10 §1 [verify section]) — for life-insurance underwriting using ECDIS or predictive models, governance-and-risk-management expectations apply, including vendor-AI test posture.
- **NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting** (January 2024) [verify circular number] — for NY-licensed life insurers, similar testing-of-AI expectations apply.

## Cross-link inside the plugin

- **`vendor-diligence` insurance overlay** carries the diligence depth the testing pack consumes.
- **`exit-plan` insurance overlay** carries policyholder-protection-aware exit-rehearsal design.
- **`concentration-risk-review`** for the insurer's outsourcing-vendor concentration (TPA, claims-platform, document-management vendors).
- **`contract-gap-review` insurance overlay**: where a test surfaces a contract gap (data-portability on the policy-admin vendor, claims-handling-continuity language), chain to the contract-gap review.

## Output-template additions for insurance

- ORSA-materiality flag on results above the firm's ORSA-narrative threshold.
- Policyholder-protection safety-control line under safety controls for live tests on claims-handling paths.
- AIS-Program reporting line under programme alignment where AI-in-scope is true.

## Common pitfalls in insurance resilience testing

- Treating policy-administration as out of scope because it is not customer-facing in the same way as banking channels. Renewal-cycle disruption and statement-cycle disruption are customer-impact events.
- Skipping the catastrophe scenario on claims-handling. Catastrophe events stress claims-handling capacity in ways that day-to-day failures do not.
- Setting tolerance from the carrier's customer-experience preference rather than from the policyholder-protection statute floor in the operative state.
- Treating vendor-AI testing as a model-risk-only matter. Vendor-AI continuity is operational-resilience too: deprecation, regression, vendor distress, training-data incidents at the vendor.
- Skipping coordination with consumer-affairs and customer-experience before a live test on customer-affecting paths.
