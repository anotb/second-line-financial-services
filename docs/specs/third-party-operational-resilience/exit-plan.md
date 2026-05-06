# exit-plan — Phase 1 spec sheet

Plugin: `third-party-operational-resilience`
Phase: 1 (per-skill scoping)
Plan: `docs/plans/2026-05-06-rationalized-plugin-map.md`

## Activation-tuned description

```
Drafts an exit plan for a third-party arrangement: trigger events, transition target (substitute, in-house, hybrid), data extraction and return, knowledge transfer, regulatory notification posture, customer-impact mitigations, and the testing the firm will run to prove the plan is more than paper.

Best for:
- A new critical or important arrangement is being onboarded and the exit plan is required as part of pre-onboarding evidence.
- Annual recertification of an existing critical or important vendor where the prior exit plan is stale, untested, or absent.
- DORA preparation for critical-or-important-function arrangements where Article 28(8) requires an exit strategy.
- A concentration-risk-review or resilience-test surfaces a single point of failure and the firm needs to harden the exit posture.

Not the right tool when:
- The criticality tier has not been set (use criticality-assessment first).
- The arrangement is genuinely low risk and the firm's policy does not require a formal exit plan (record the rationale, do not produce a plan).
- The work is full diligence on the vendor (use vendor-diligence) or contract clause coverage (use contract-gap-review).

Anchored to: Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 2023) §V ongoing monitoring and §VI termination [verify section]; OCC Bulletin 2013-29 termination [verify section]; FFIEC IT Handbook — Outsourcing Technology Services exit and contingency sections [verify section]; FFIEC IT Handbook — Business Continuity Management booklet for testing posture [verify section]; DORA Article 28(8) exit strategies and Article 30(3) exit-related contractual provisions; EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02) §15 exit strategies [verify section]; UK PRA SS2/21 (operational resilience) for impact-tolerance framing.
```

## Source anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 6, 2023). Termination section, ongoing monitoring section [verify section]. Expectation: firms have plans for orderly transition or contingency in event of termination, including for unexpected termination.
- OCC Bulletin 2013-29 termination expectations [verify section] (predecessor framing).
- FFIEC IT Examination Handbook — Outsourcing Technology Services booklet, contingency planning and termination expectations [verify section].
- FFIEC IT Examination Handbook — Business Continuity Management booklet. Testing posture (tabletop, walkthrough, simulation, full live exercise), recovery-strategy considerations [verify section].
- DORA — Regulation (EU) 2022/2554, Article 28(8) requires firms have exit strategies for ICT services supporting critical or important functions; Article 30(3) lists exit-related mandatory contractual provisions for those arrangements [verify subarticle].
- EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02). Documented exit-strategy guideline [verify section number]. Includes scenarios for unexpected termination, transition-to-alternative-provider plans, and identification of indispensable functions.
- UK PRA SS1/21 (impact tolerances) and SS2/21 (operational resilience). Reference for the impact-tolerance frame the exit plan must withstand. UK overlay only.
- BCBS Principles for Operational Resilience (March 2021) — substitutability and exit posture for important business services.

## Sector overlays needed

- `references/sector-overlays/banking.md` — interagency guidance termination expectations; FRB SR letters on third-party risk management; community-bank vs large-bank proportionality on exit testing.
- `references/sector-overlays/insurance.md` — NAIC outsourcing model exit expectations; state guaranty-fund and policyholder-protection considerations; portability of policy administration data; claims-handling continuity.
- `references/sector-overlays/capital-markets.md` — Reg SCI substitutability for critical SCI systems; market-maker / clearing-member exit posture; books-and-records retention and migration.
- `references/sector-overlays/payments-fintech.md` — settlement-network access continuity; rails-failover (FedNow/RTP/ACH/card-network); BIN-sponsorship transition; banking-as-a-service partner-bank exit (FFIEC inter-agency joint statement August 2023).

## Cross-cutting overlays

- `references/cross-cutting/cyber.md` — secure data-extraction and key-rotation on exit; vendor-side certification of data destruction; access-revocation choreography; SEC cyber-disclosure exposure during a forced or contested termination; FFIEC IT Handbook information-security expectations on transition.
- `references/cross-cutting/privacy.md` — GLBA Safeguards Rule data-handling on transition; state-privacy-law deletion and return obligations (CCPA/CPRA service-provider deletion); cross-border data flows during transition; HIPAA business-associate transition where in scope.

## Output template named sections

`templates/default-output.md`:

1. Arrangement and criticality input
2. Trigger events (vendor-driven, firm-driven, regulator-driven, market-driven)
3. Exit scenarios and transition target options (substitute vendor, in-house, hybrid, retire service)
4. Time-to-transition and viability against impact tolerance
5. Data extraction, return, and destruction plan
6. Knowledge transfer plan
7. Customer-impact mitigations during transition
8. Regulatory notification posture (who, when, how — supervisory expectation, customer-disclosure)
9. Cyber considerations during transition
10. Privacy considerations during transition
11. Cost and resourcing estimate
12. Testing plan (tabletop, walkthrough, partial simulation, full live exercise) and last-test results if applicable
13. Open dependencies and risks
14. Owner (role) and accountable executive
15. Reviewer questions
16. Source trace and confidence label

## Structured output fields

Anchor: `schemas/vendor.schema.json` `exit_plan_status` (enum); detailed exit-plan artifact extends as a separate object.

Fields (type, purpose):

- `arrangement_id` (string)
- `criticality_input` (enum)
- `dora_in_scope` (boolean)
- `triggers` (array of object: `category`, `description`, `lead_time_assumption`)
- `transition_target_options` (array of object: `option`, `viability`, `time_to_transition`, `dependencies`)
- `selected_target` (string) — the firm's primary exit target
- `data_extraction` (object: `format`, `volume_estimate`, `extraction_window`, `vendor_obligations`, `firm_obligations`, `destruction_evidence`)
- `knowledge_transfer` (object: `documentation_set`, `personnel_transition`, `vendor_obligations`)
- `customer_impact_mitigations` (array of object)
- `regulatory_notification_posture` (object: `notifiable_regimes`, `windows`, `customer_disclosure_posture`)
- `cyber_considerations` (object) — see cross-cutting/cyber.md
- `privacy_considerations` (object) — see cross-cutting/privacy.md
- `cost_estimate_range` (string)
- `testing_plan` (object: `cadence`, `methods`, `last_test_date`, `last_test_outcome`, `next_test_due`)
- `time_to_transition_vs_tolerance` (enum: `within | near | breach | unknown`)
- `exit_plan_status` (enum: `complete | draft | missing | not-applicable`)
- `owner` (string) — role
- `accountable_executive` (string) — role
- `reviewer_questions` (array of string)
- `confidence_label` (enum)
- `source_trace` (array of object)

## Example scenarios (two, public-source-derived)

1. **Core-banking SaaS exit plan for a community bank.** Inputs: criticality output (critical), the firm's RTO/RPO tolerance, the contract's termination clause (six-month transition assistance commitment), the firm's IBS register. Anchored to: interagency guidance (June 2023) termination section [verify section]; FFIEC BCM booklet [verify section]; FFIEC inter-agency cloud joint statement (April 2020). The output identifies the substitute-vendor option as primary, in-house as not-viable, retire-service as not-applicable. Time-to-transition is estimated at twelve months given core-data-migration realities, breaching the firm's stated impact tolerance. The plan recommends a tabletop in the next quarter and a partial-simulation in the next year. Surfaces this as a finding for the chief operating officer.

2. **DORA-in-scope critical AI vendor — foundation-model API used by an EU subsidiary for KYC narrative summarisation.** Inputs: criticality output (DORA critical-or-important-function = yes), the contract's exit clauses, the deployment architecture (vendor handles prompts containing customer name, narrative, and identifier excerpts). Anchored to: DORA Article 28(8) and Article 30(3) [verify subarticle]; EBA outsourcing guidelines exit-strategy section [verify section]; NIST AI RMF 1.0 Govern function for AI-vendor exit considerations. The output sets the transition target as "substitute model vendor with portable prompt-template library and sanitised RAG corpus", identifies that the prompt-template portability has not been tested, and notes that Article 30(3)(a) [verify subarticle] requires exit-strategy and transitional-support clauses currently absent from the contract — flag to `contract-gap-review`. Testing plan includes a quarterly tabletop with the model-risk function and an annual rehearsal of switching vendors for a low-risk subset of prompts.

## Common pitfalls

1. **Treating the contract's transition-assistance period as the exit plan.** The clause is a contractual commitment from the vendor; the plan is the firm's actual playbook. They are different things.
2. **Skipping the impact-tolerance test.** An exit plan that takes longer than the impact tolerance for the supported important business service is itself a finding, not an exit plan.
3. **Relying on a single transition target.** Vendor-driven termination, regulator-driven termination, and market-driven distress have different lead times and different available-substitute realities. Plan for each.
4. **Treating data extraction as solved by "we have an export API".** Exports need format compatibility with the substitute, schema mapping, validation against firm-of-record, and destruction evidence afterwards.
5. **Forgetting fourth-party dependencies.** The vendor's own subcontractors may be the bottleneck on transition. The plan must surface fourth-party constraints.
6. **Skipping the test.** A plan that has never been tested has unknown viability. Document the testing cadence and the last-test outcome — even if "no test yet" — and surface it as a reviewer question.
7. **Missing the regulator-notification posture.** Exit events for critical or important functions often require supervisory notification (DORA Article 28 [verify subarticle]; bank-regulator expectations on material vendor changes). The plan must include the notification clock, not be a surprise on the day.
8. **AI-vendor pitfall — assuming prompt templates and RAG corpora are vendor-portable.** Prompt behaviour is model-specific; templates and retrieval pipelines need rework when the underlying model changes. Build in an AI-specific transition-engineering line item.
9. **Treating "we use multi-cloud" as a free exit posture.** Multi-cloud architecture without tested failover is marketing, not resilience.
10. **Letting the exit plan owner be a procurement role only.** The accountable executive should be the IBS owner. Procurement supports execution, but the IBS owner owns the customer-facing impact.
