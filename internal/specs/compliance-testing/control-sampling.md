# control-sampling — spec sheet

Plugin: `compliance-testing`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Drafts a sampling approach for a compliance, control, or audit test: defines the population, picks a sample method (statistical or judgmental), sizes the sample, sets the tolerable deviation rate, and documents the rationale that a reviewer can defend in front of an examiner. Output is a sampling memo that drops into the test plan or workpaper.

Best for:
- A compliance-testing or internal-audit team is scoping a control test and needs a defensible sample method, size, and rationale before pulling evidence.
- A second-line reviewer is challenging a first-line control owner's self-attested testing because the sampling rationale is missing or thin.
- A walkthrough has confirmed control design and the next step is sizing operating-effectiveness testing across a defined population.

Not the right tool when:
- The control or obligation has not been mapped yet (use `risk-compliance-core/skills/control-matrix`).
- The test plan as a whole has not been scoped (use `test-plan-builder`; this skill produces the sampling section that test-plan-builder consumes).
- Exceptions have already been identified and need root-cause analysis (use `exception-analysis`).

Anchored to: IIA International Professional Practices Framework, Standard 2310 (Identifying Information) and Performance Standard 2320 (Analysis and Evaluation) [verify section]; AICPA AU-C 530, Audit Sampling [verify paragraph]; AICPA AU-C 330, Performing Audit Procedures in Response to Assessed Risks [verify paragraph]; FFIEC IT Examination Handbook, Audit booklet (April 2012) §IV (audit testing) [verify section]; SR 08-8 / SR 08-8-1 (Federal Reserve, Compliance Risk Management Programs and Oversight at Large Banking Organizations with Complex Compliance Profiles, October 2008) [verify section]; OCC PPM 5310-3 [verify exact reference and date].

## Source anchors

Primary:
- IIA International Professional Practices Framework — Standards. Cite Standard 2310 (Identifying Information) and 2320 (Analysis and Evaluation), and the implementation guidance on audit sampling. Use for: methodology framing for internal-audit-led testing. [verify section labels against current IPPF release]
- AICPA AU-C 530, Audit Sampling. Use for: conceptual rigor on sampling risk, tolerable rate of deviation, expected rate of deviation, sample size determination, projection of deviations. AU-C 530 is an external-audit standard; in second-line practice it is borrowed as a methodology anchor for control-test sampling, not as a direct legal requirement. [verify paragraph references]
- AICPA AU-C 330, Performing Audit Procedures in Response to Assessed Risks. Use for: linking risk assessment to nature, timing, and extent of testing. [verify paragraph references]
- FFIEC IT Examination Handbook, Audit booklet, April 2012. Use for: financial-services overlay on audit-program design, sampling, and testing. Cite §IV (audit testing) and the appendix on audit-test programs. [verify section labels]
- SR 08-8 (Federal Reserve, Compliance Risk Management Programs and Oversight at Large Banking Organizations with Complex Compliance Profiles, October 16, 2008). Use for: testing-program expectations within a compliance risk management program, including risk-based scope and population coverage. [verify section labels]

Secondary (overlay only):
- COSO 2013 Internal Control — Integrated Framework, Principle 16 (Selects, Develops, and Performs Ongoing and/or Separate Evaluations). Use for: situating sampling inside the monitoring component. [verify principle reference]
- OCC PPM 5310-3 (compliance management systems for OCC-supervised banks). [verify exact reference and current effective date] Use for: bank-specific compliance testing posture.
- CFPB Compliance Management System Review Procedures (current Supervision and Examination Manual edition). Use for: CMS-context expectations on monitoring and testing populations. [verify section labels]

## Sector overlays needed

- `banking.md` — Heightened-standards-bank context (12 CFR Part 30 Appendix D §III) [verify] on independent risk management and second-line testing rigor; OCC PPM 5310-3 [verify] for CMS testing scope; FFIEC IT booklet population definitions for IT-control samples.
- `insurance.md` — NAIC Model Audit Rule (Model #205) [verify section] internal-control testing posture; state DOI market-conduct examination sampling conventions for claims and underwriting populations.
- `capital-markets.md` — FINRA Rule 3120 (Supervisory Control System) and 3130 (Annual Certification) [verify] testing expectations; SEC Rule 17a-4 / FINRA 4511 recordkeeping populations [verify].
- `payments-fintech.md` — Reg E error-resolution and Reg Z billing-error populations; sponsor-bank oversight sampling for fintech partners under the U.S. interagency TPRM guidance (June 2023) ongoing-monitoring expectations.

## Cross-cutting overlays needed

- `cyber.md` — Optional, when sampling cyber controls (logical access reviews, vulnerability remediation tickets, NYDFS Part 500 §500.5 / §500.7 evidence). Population definition gets unusual here (tickets, alerts, identities) and benefits from a worked example.
- `privacy.md` — Optional, for GLBA Safeguards Rule (16 CFR 314.4) testing samples [verify] and consumer-facing data access populations.
- `climate.md` — Not required at v1.
- `conduct.md` — Optional, for UDAAP-related testing where the population is customer interactions, complaints, or call recordings (CFPB UDAAP exam manual [verify section]).

## Output template named sections

1. Scope and source posture
   - Test ID, related control ID, related obligation ID, jurisdiction, business unit, period under test, source posture (public-only / firm-policy-overlay / mixed).
2. Population definition
   - Population description, source of truth (system, report, query), period boundaries, completeness assertion, exclusions and rationale, population size.
3. Risk-based stratification
   - Stratification factors (transaction value, customer risk tier, product, channel, geography), strata sizes, rationale tied to risk assessment.
4. Sample method
   - Method (statistical attribute / monetary unit / judgmental / haphazard / 100% testing) and why this method fits the test objective.
5. Sample size rationale
   - Confidence level, tolerable deviation rate, expected deviation rate, resulting size; for judgmental samples, the qualitative basis and the floor/ceiling reference (e.g., FFIEC IT booklet appendix conventions [verify]).
6. Selection method
   - Random number generator and seed, MUS interval, judgmental selection criteria; reproducibility note.
7. Tolerable deviation rate
   - Numeric threshold and the criterion source (firm policy / methodology / external standard).
8. Sample drawn
   - Sample IDs (or pointer to sample list), draw date, drawer name, control total reconciliation to population.
9. Limitations and assumptions
   - What the sample cannot conclude on, period coverage gaps, completeness caveats.
10. Reviewer sign-off
    - Reviewer role, reviewer questions, sign-off date placeholder, downstream consumer (`test-plan-builder` / `workpaper-drafter`).
11. Source trace and confidence label
    - Anchored standards, firm policy references, confidence label (high / medium / low / unknown).

## Structured output fields

Schema: extends `schemas/test-plan.schema.json` with a `sampling` sub-object, plus a standalone wrapper for cases where sampling is documented separately from the test plan.

Wrapper object:
- `sampling_id`: string. Stable ID for the sampling memo.
- `test_id`: string. Foreign key into `test-plan.schema.json`.
- `control_id`: string. Foreign key into `control.schema.json`.
- `obligation_id`: string. Foreign key into `obligation.schema.json`.
- `population`: object.
  - `description`: string.
  - `source_of_truth`: string (system / report / query identifier).
  - `period_start`, `period_end`: string (ISO date).
  - `size`: integer.
  - `completeness_basis`: string.
  - `exclusions`: array of objects with `criterion` and `rationale`.
- `stratification`: array of objects with `factor`, `bucket`, `bucket_size`.
- `sample_method`: enum. `statistical-attribute` / `monetary-unit` / `judgmental` / `haphazard` / `full-population`.
- `confidence_level`: number (0-1) when statistical.
- `tolerable_deviation_rate`: number (0-1).
- `expected_deviation_rate`: number (0-1).
- `sample_size`: integer.
- `selection_method`: object with `technique` (enum: `prng`, `mus`, `judgmental-criteria`, `haphazard`), `seed_or_interval` (string), `criteria_description` (string).
- `sample_ids`: array of strings (or `sample_list_pointer` string).
- `limitations`: array of strings.
- `confidence_label`: enum. `high` / `medium` / `low` / `unknown`.
- `reviewer_questions`: array of strings.
- `human_review_required`: boolean. Always true.

Phase 2 should add to `test-plan.schema.json`:
- `sampling_id` (string, foreign key) so the test plan can reference a separately documented sampling memo.

## Example scenarios

### Scenario 1: SR 08-8 compliance-testing sample for a regional bank's overdraft-fee disclosure control

Input: a Tier-2 regional bank's compliance-testing team is testing an operating-effectiveness control over Reg E / Reg DD overdraft-fee disclosure clarity for new checking accounts. Population is new consumer checking accounts opened in Q1 (~38,000 accounts). Source posture is public guidance (CFPB CMS exam manual, SR 08-8) plus firm CMS testing methodology.

Output emphasizes:
- Population sourced from the deposit account-opening system (`DDA-CORE:NEW_ACCT_Q1`) with reconciliation to the daily new-account reporting feed.
- Stratification by channel (branch, online, phone) and by overdraft-protection enrollment (yes/no) because conduct risk concentrates on the OD-enrolled segment.
- Statistical attribute sample at 95% confidence, 5% tolerable deviation rate, 1% expected deviation rate, sample size 95.
- Selection by reproducible PRNG with documented seed.
- Limitations note: sampling does not address verbal disclosures captured only on call recordings (out of scope for this test; flagged as a coverage gap to test-plan-builder).
- Confidence label medium; reviewer question on whether OD-protection segment justifies a separate test rather than a stratum.

### Scenario 2: FFIEC IT booklet logical-access review sample for quarterly access recertification

Input: second-line technology risk is testing the quarterly logical-access recertification control for a critical core-banking application. Population is recertification packets generated for entitled users in the most recent quarter (~2,400 packets). Source posture is public (FFIEC IT booklet, NYDFS Part 500 §500.7 [verify]) plus firm IT GCC methodology.

Output emphasizes:
- Population is recertification packets, not users; documented as such because a single user can have multiple packets across roles.
- Stratification by privilege tier (privileged / standard) with oversampling of privileged accounts.
- Judgmental sample: 30 packets total (20 privileged, 10 standard) with rationale citing FFIEC IT booklet appendix conventions [verify section] and the firm's IT-GCC methodology floor.
- Tolerable deviation rate set at 0% for privileged packets (policy floor) and 5% for standard.
- Limitations note: sample does not test entitlement-provisioning at onboarding (different control); sample does not address service accounts (excluded with rationale).
- Confidence label high on documentation of method, medium on the judgmental floor (firm methodology not externally benchmarked).

## Common pitfalls

1. Defining the population as the source system rather than the testable items in scope. The population is what you could draw a sample from to answer the test question, not the database that holds those items.
2. Skipping reconciliation between the population pull and the system of record total. Without a reconciled control total, the population assertion is unsupported.
3. Confusing tolerable deviation rate with materiality. They are not interchangeable. Tolerable deviation rate is the maximum rate of control deviation the reviewer will accept and still conclude operating effectiveness.
4. Citing AU-C 530 sample-size tables as if they were a regulatory requirement. AU-C 530 is an external-audit standard; in second-line testing it is a methodology anchor. The criterion source is the firm's testing methodology, anchored to public standards.
5. Pulling judgmental samples without writing down the judgmental basis. "Risk-based" alone is not a basis. The basis names the factors, the weights, and the floor/ceiling reference.
6. Treating a sample exception as a finding before exception-analysis runs. The sampling memo stops at the sample drawn; conclusions live in the workpaper after exception-analysis classifies deviations.
