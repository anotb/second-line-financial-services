# resilience-testing-pack — Phase 1 spec sheet

Plugin: `third-party-operational-resilience`
Phase: 1 (per-skill scoping)
Plan: `docs/plans/2026-05-06-rationalized-plugin-map.md`

## Activation-tuned description

```
Drafts a resilience-testing pack for an important business service or a critical third-party arrangement: severe-but-plausible scenarios, test design (tabletop, walkthrough, partial simulation, full live exercise), success criteria tied to impact tolerance, evidence-collection plan, and the read-out template the operational-resilience committee will receive.

Best for:
- Annual or quarterly resilience-testing cycle planning for an important business service.
- A critical or important third-party arrangement where the diligence pack flagged untested exit posture or untested BCDR claims.
- DORA preparation for the digital operational resilience testing programme (Articles 24-26) [verify subarticle], including TLPT planning where in scope.
- A regulator-driven request following a sector-wide event (cloud outage, market-data disruption, payments-rails incident).

Not the right tool when:
- The IBS or arrangement has not yet been mapped or tiered (use criticality-assessment first).
- The work is exit-plan content rather than testing the exit (use exit-plan to draft, then this skill to design the test of the plan).
- The work is the test execution itself (this skill drafts the pack and the read-out template; execution is run by the firm's resilience function).

Anchored to: Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 2023) §V ongoing monitoring (testing posture) [verify section]; FFIEC IT Examination Handbook — Business Continuity Management booklet (testing-and-exercise section) [verify section]; FFIEC IT Examination Handbook — Outsourcing Technology Services (resilience-testing section) [verify section]; DORA Articles 24-26 (digital operational resilience testing programme; advanced testing including TLPT); BCBS Principles for Operational Resilience (March 2021) (mapping, scenario-testing, and tolerance-for-disruption principles); UK PRA SS2/21 (severe-but-plausible scenario testing) and SS1/21 (impact tolerances) for UK overlay reference.
```

## Source anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FRB/FDIC, June 6, 2023). Ongoing-monitoring section addresses testing of vendor performance and contingency plans [verify section].
- FFIEC IT Examination Handbook — Business Continuity Management booklet. Testing-and-exercise section covering tabletop, walkthrough, simulation, and full functional exercise [verify section]. Use for the test-method taxonomy.
- FFIEC IT Examination Handbook — Outsourcing Technology Services booklet. Vendor BCDR-testing expectations [verify section].
- DORA — Regulation (EU) 2022/2554, Articles 24-26 establish the digital operational resilience testing programme; Article 26 covers advanced testing including threat-led penetration testing (TLPT) for designated firms [verify subarticle]. Article 25 lists test types (vulnerability assessments, open-source analyses, network security assessments, gap analyses, physical security reviews, source code reviews, scenario-based tests, compatibility testing, performance testing, end-to-end testing, penetration testing) [verify subarticle].
- BCBS Principles for Operational Resilience (March 2021). Principles on mapping, scenario-testing, third-party dependencies, and ICT.
- UK PRA SS2/21 — Operational resilience: impact tolerances for important business services (severe-but-plausible scenarios as the testing frame); UK PRA SS1/21 — Outsourcing and third-party risk management. UK overlay only.
- TIBER-EU framework (ECB) for TLPT methodology where applicable [verify reference].
- FFIEC inter-agency cloud joint statement (April 2020) — testing of cloud-services resilience.

## Sector overlays needed

- `references/sector-overlays/banking.md` — interagency expectations on vendor and IBS testing; payments-related and core-banking exercises; large-bank heightened-standards testing programmes.
- `references/sector-overlays/insurance.md` — claims-handling and policy-administration scenario testing; NAIC outsourcing model expectations on testing; policyholder-protection considerations during a test that may surface real customer impact.
- `references/sector-overlays/capital-markets.md` — Reg SCI testing requirements (industry-wide test, business-continuity-and-disaster-recovery test, designated members) [verify section]; FINRA business-continuity testing notices; CFTC system-safeguards testing.
- `references/sector-overlays/payments-fintech.md` — payments-rails failover testing (FedNow/RTP/ACH/card-networks); BIN-sponsorship continuity testing; banking-as-a-service partner-bank disruption scenarios.

## Cross-cutting overlays

- `references/cross-cutting/cyber.md` — cyber-incident scenarios (ransomware on the vendor, vendor supply-chain compromise, cloud-control-plane outage, identity-provider outage); SEC cyber-disclosure rule interplay during a real or simulated incident; NYDFS 500.16 incident-response plan testing; CISA tabletop-exercise packages as input. TIBER-EU and CBEST methodology references for advanced testing.
- `references/cross-cutting/privacy.md` — testing scenarios involving personal data exposure (data-loss, accidental cross-border transfer during failover); GLBA Safeguards Rule incident-response testing 16 CFR 314.4(h); state-privacy-law breach-notification timing as a test-design constraint.

## Output template named sections

`templates/default-output.md`:

1. Subject of test (IBS or specific arrangement)
2. Mapping summary (the IBS, the dependencies in scope, the third parties and fourth parties touched)
3. Impact tolerance (RTO/RPO and customer-impact tolerance for the IBS; firm-defined)
4. Severe-but-plausible scenarios (scenario, rationale, source anchor for plausibility, expected stress on the system)
5. Test design (method per scenario: tabletop, walkthrough, partial simulation, full live; cadence; pre-conditions; safety controls)
6. Roles and observers (firm functions; vendor participation; regulator-observation posture)
7. Success criteria tied to impact tolerance
8. Evidence-collection plan (what is captured during the exercise; how it is preserved)
9. Communication plan (internal and external; customer-impact messaging if a real customer-affecting test)
10. Read-out template (post-exercise sections the operational-resilience committee will receive)
11. Findings-and-actions framework (how findings flow into the firm's issue-management cycle)
12. Programme-level integration (how this test relates to the firm's annual testing programme; DORA Article 24 programme alignment if applicable)
13. Reviewer questions
14. Source trace and confidence label

## Structured output fields

Top-level:

- `pack_id` (string)
- `subject_type` (enum: `ibs | arrangement | portfolio`)
- `subject_id` (string)
- `as_of_date` (string, ISO 8601)
- `impact_tolerance` (object: `rto`, `rpo`, `customer_impact_threshold`, `regulatory_impact_threshold`)
- `mapping_summary` (object)
- `scenarios` (array of object: `scenario_id`, `name`, `description`, `rationale`, `plausibility_anchor`, `expected_stress`, `severity`)
- `test_design` (array of object: `scenario_id`, `method` enum `tabletop|walkthrough|partial-simulation|full-live`, `cadence`, `preconditions`, `safety_controls`, `participants`)
- `success_criteria` (array of object: `scenario_id`, `criterion`, `metric`, `threshold`)
- `evidence_collection_plan` (array of object)
- `communication_plan` (object)
- `readout_template_sections` (array of string)
- `findings_actions_framework` (string)
- `programme_alignment` (object: `firm_programme_link`, `dora_article_24_link`, `reg_sci_link`)
- `reviewer_questions` (array of string)
- `confidence_label` (enum)
- `source_trace` (array of object)

## Example scenarios (two, public-source-derived)

1. **Annual resilience-testing pack for "card-payment authorisation" as an important business service at a US bank.** Inputs: the firm's IBS register, the criticality outputs for the card-network connection and the fraud-decisioning vendor, the prior-year test outcomes, the impact tolerance (no more than thirty minutes of authorisation outage). Anchored to: interagency guidance (June 2023) [verify section]; FFIEC BCM booklet testing section [verify section]; FFIEC inter-agency cloud joint statement (April 2020). Severe-but-plausible scenarios designed: card-network connectivity loss, fraud-decisioning vendor outage, identity-provider outage at the firm's core, hyperscaler-region failure on the firm's primary compute region. Test methods: a full live exercise on the network-failover (with the network partner), a partial simulation on the fraud-vendor failover, and a tabletop on the hyperscaler-region scenario. Success criteria tied to the thirty-minute tolerance.

2. **DORA resilience-testing pack for an EU subsidiary's customer-onboarding IBS, including TLPT scoping.** Inputs: the firm's IBS mapping, the criticality output for the AI-vendor used for ID-document verification (critical-or-important-function), the firm's DORA register, the prior-year basic-testing-programme summary. Anchored to: DORA Articles 24-26 [verify subarticle]; TIBER-EU methodology [verify reference]; EIOPA coordination on insurer testing where the parent is an insurer. Severe-but-plausible scenarios: ID-verification-vendor outage during peak onboarding window, AI-vendor model regression that drives a spike in false rejections (customer-impact tolerance breach scenario), ICT-third-party concentration scenario where the AI-vendor and the document-storage vendor share a fourth-party hyperscaler. Test methods: tabletop for the AI-regression scenario, partial simulation for the ID-verification outage, and TLPT scoping for the firm's customer-onboarding chain (subject to designation under DORA Article 26 [verify subarticle]; legal review needed). Success criteria align to the firm's customer-impact tolerance for onboarding.

## Common pitfalls

1. **Designing tests against vendor SLAs instead of firm impact tolerance.** SLAs are vendor commitments. The test asks whether the IBS holds within the firm's tolerance. These often differ.
2. **Skipping severe-but-plausible scenarios for "low likelihood".** Severe-but-plausible is a regulatory frame, not a probability judgment. A hyperscaler-region outage is plausible because it has happened.
3. **Tabletop everywhere.** Tabletop is the cheapest, lowest-fidelity method. A full programme mixes methods. A critical-or-important-function arrangement that has only ever been tabletop-tested has not been tested in supervisory terms.
4. **Excluding vendor participation from the test.** Vendor participation is the test of the partnership, not just the technology. A test the vendor declines to join is itself a finding.
5. **No safety controls on partial-simulation or live tests.** A live test that introduces real customer impact is a real incident. Safety controls (kill-switch, rollback, customer-impact threshold for early-termination) are mandatory.
6. **Producing a test design without a read-out template.** The committee needs the post-exercise narrative shape on day one, not on day of read-out. Lock the template at design time.
7. **Treating findings as ad-hoc.** Findings flow into the firm's issue-management cycle (cross-reference `risk-compliance-core/issue-writeup`). Without that flow, findings die in the post-exercise deck.
8. **Forgetting the regulator-observation posture.** Some tests have a regulator-observation expectation (Reg SCI industry-wide test, DORA TLPT). Build this in or call out the absence.
9. **Producing the pack as the test.** This skill drafts the design and the read-out template. The exercise itself is run by the firm's resilience function, with the second-line role limited to challenge and observation as appropriate.
