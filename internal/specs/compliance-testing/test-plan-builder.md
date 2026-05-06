# test-plan-builder — spec sheet

Plugin: `compliance-testing`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Drafts a control test plan: scope, control objective, criteria, period, population, sampling reference, walkthrough plan, design-effectiveness procedures, operating-effectiveness procedures, evidence requests, pass/fail criteria, and downstream consumers. Output is the pre-fieldwork artifact that gets reviewer sign-off before evidence pulls and testing begin.

Best for:
- A compliance-testing or internal-audit team is scoping an annual test plan or a one-off targeted review and needs the planning workpaper before fieldwork.
- A second-line reviewer is responding to a regulatory-change-management trigger (a new rule, a new exam priority) by standing up a fresh test against an updated control set.
- An audit lead is rebuilding a test program after an issue, restating control objectives and procedures from first principles.

Not the right tool when:
- Controls have not been mapped yet (use `risk-compliance-core/skills/control-matrix` first).
- Sampling is the only piece needed (use `control-sampling` standalone).
- Testing is complete and the work is documenting results (use `workpaper-drafter`). The boundary: `test-plan-builder` is **pre-fieldwork**; `workpaper-drafter` is **during/post-fieldwork**; `qa-workpaper` is **review of the completed workpaper**. The three are sequential.

Anchored to: IIA Performance Standard 2200 (Engagement Planning), 2210 (Engagement Objectives), 2220 (Engagement Scope), 2240 (Engagement Work Program) [verify section]; AICPA AU-C 300, Planning an Audit [verify paragraph]; AICPA AU-C 330, Performing Audit Procedures in Response to Assessed Risks [verify paragraph]; FFIEC IT Examination Handbook, Audit booklet (April 2012) §III (audit planning) [verify section]; SR 08-8 (Federal Reserve, Compliance Risk Management Programs, October 2008) [verify section]; OCC PPM 5310-3 [verify exact reference and date]; CFPB Compliance Management System Review Procedures [verify section].

## Source anchors

Primary:
- IIA International Professional Practices Framework — Performance Standards 2200, 2210, 2220, 2240. Use for: engagement planning expectations, work-program structure. [verify section labels against current IPPF release]
- AICPA AU-C 300, Planning an Audit. Use for: methodology anchor on planning artifacts, scope, materiality, assignment of work. AU-C standards are external-audit standards; in second-line testing they are methodology anchors. [verify paragraph references]
- AICPA AU-C 330, Performing Audit Procedures in Response to Assessed Risks. Use for: linking assessed risk to the nature, timing, and extent of testing. [verify paragraph references]
- FFIEC IT Examination Handbook, Audit booklet, April 2012, §III (audit planning) and Appendix A (audit work-program elements). Use for: financial-services testing-program conventions. [verify section labels]
- SR 08-8 (Federal Reserve, October 16, 2008). Use for: compliance risk management program testing-cycle expectations and risk-based scope decisions. [verify section labels]
- CFPB Compliance Management System Review Procedures. Use for: monitoring and testing scoping in a CMS context. [verify section labels]

Secondary (overlay only):
- COSO 2013 Internal Control — Integrated Framework, Principle 16 (Selects, Develops, and Performs Ongoing and/or Separate Evaluations). [verify principle reference]
- OCC PPM 5310-3 (compliance management systems for OCC-supervised banks). [verify exact reference and current effective date]

## Sector overlays needed

- `banking.md` — Heightened-standards-bank context (12 CFR Part 30 Appendix D §III) [verify] for second-line testing rigor; OCC PPM 5310-3 [verify] for CMS testing scope; CRA / fair-lending testing scoping; deposit and lending product testing conventions.
- `insurance.md` — NAIC Model Audit Rule (Model #205) [verify section] internal-control testing program; ORSA testing posture; state DOI market-conduct testing scope conventions.
- `capital-markets.md` — FINRA Rule 3120 (Supervisory Control System) and 3130 (Annual Certification) [verify] testing program structure; SEC Reg SCI testing where applicable [verify]; trade-surveillance testing scope.
- `payments-fintech.md` — Sponsor-bank oversight test programs under interagency TPRM 2023 [verify section]; Reg E / Reg Z testing scope for payments products; BSA/AML testing scope under FFIEC BSA/AML manual [verify section].

## Cross-cutting overlays needed

- `cyber.md` — Required when test scopes cyber controls. Anchors: NIST SP 800-53 / SP 800-53A control-test methodology [verify], NYDFS Part 500 §500.7, FFIEC IT booklet, SEC Reg S-K Item 106 [verify section] for cyber-disclosure-process testing.
- `privacy.md` — Optional, for GLBA Safeguards Rule (16 CFR 314.4) testing [verify].
- `climate.md` — Not required at v1.
- `conduct.md` — Required when scoping consumer-impact testing. CFPB UDAAP exam manual [verify section]; SR 11-7-style fair-and-responsible posture for AI-driven decisions where applicable.

## Output template named sections

1. Scope and source posture
   - Test ID, related control ID, related obligation ID, jurisdiction, business unit, period under test, source posture (public-only / firm-policy-overlay / mixed).
2. Test objective
   - Statement of what the test concludes on (control existence, design effectiveness, operating effectiveness, or combined).
3. Criteria
   - Named source list (rule sections, policy sections, methodology references) the test compares evidence against.
4. Population
   - Population description, source of truth, period boundaries; pointer to `control-sampling` output if separate.
5. Walkthrough plan
   - Walkthrough scope, owner roles to interview, processes to observe, system screens to inspect; evidence captured during walkthrough.
6. Design-effectiveness procedures
   - Numbered procedures evaluating whether the control as designed addresses the criterion.
7. Operating-effectiveness procedures
   - Numbered procedures testing whether the control operated as designed during the period.
8. Sampling approach reference
   - Pointer to the sampling memo (output of `control-sampling`) or inline summary if the test is small.
9. Evidence requests reference
   - Pointer to the evidence request list (output of `evidence-request-builder`) or inline list if small.
10. Pass / fail criteria
    - Pass criterion (observable condition for design and operating effectiveness)
    - Fail criterion (observable condition for design or operating failure)
    - Tolerable deviation rate reference (from sampling memo)
11. Limitations and assumptions
    - Period coverage, scope exclusions, reliance on prior testing, dependencies on other in-flight reviews.
12. Downstream consumers
    - Workpaper (`workpaper-drafter`), QA (`qa-workpaper`), exception register (`exception-analysis`), issue write-up (`risk-compliance-core/skills/issue-writeup`).
13. Reviewer sign-off
    - Reviewer role, reviewer questions, sign-off date placeholder; pre-fieldwork sign-off required before evidence pulls begin.
14. Source trace and confidence label
    - Anchored standards, firm methodology references, confidence label.

## Structured output fields

Schema: extends `schemas/test-plan.schema.json` (existing). Phase 2 adds the missing fields below.

Existing fields (keep): `test_id`, `control_id`, `test_objective`, `population`, `sample_method`, `sample_size`, `procedures` (array of strings), `evidence_requests` (array of strings), `expected_outcome`.

Phase 2 additions:
- `obligation_id`: string. Foreign key.
- `period_start`, `period_end`: string (ISO date).
- `source_posture`: enum. `public-only` / `firm-policy-overlay` / `mixed`.
- `criteria`: array of objects with `source` (named rule/policy/methodology), `section`, `text` (excerpt or paraphrase).
- `walkthrough_plan`: object with `roles_interviewed`, `processes_observed`, `evidence_captured`.
- `design_procedures`: array of objects with `procedure_id`, `description`, `expected_evidence`.
- `operating_procedures`: array of objects with `procedure_id`, `description`, `expected_evidence`.
- `sampling_id`: string. Foreign key into `sampling.schema.json` (Phase 2 addition from `control-sampling` spec).
- `evidence_request_list_id`: string. Foreign key into `evidence-request.schema.json` (Phase 2 addition from `evidence-request-builder` spec).
- `pass_criteria`: string.
- `fail_criteria`: string.
- `limitations`: array of strings.
- `downstream_consumers`: array of enums (`workpaper-drafter`, `qa-workpaper`, `exception-analysis`, `issue-writeup`).
- `confidence_label`: enum. `high` / `medium` / `low` / `unknown`.
- `reviewer_questions`: array of strings.
- `human_review_required`: boolean. Always true.

## Example scenarios

### Scenario 1: Annual Reg E error-resolution test plan for a regional bank

Input: a regional bank's compliance-testing team is building the annual Reg E error-resolution test plan (12 CFR 1005.11) [verify section]. Scope is consumer dispute handling for the most recent calendar year. Source posture is public (Reg E and CFPB CMS exam manual) plus firm CMS testing methodology.

Output emphasizes:
- Test objective combines design and operating effectiveness.
- Criteria list cites Reg E §1005.11(c) (provisional credit timing) and §1005.11(d) (notice of resolution) [verify], plus the firm's dispute-handling policy section 4.
- Walkthrough plan covers dispute intake (call center and branch), case routing (case-management system), investigation (operations team), provisional credit (deposit operations), notice of resolution (output mailing).
- Design procedures test whether the case-management system enforces the 10-business-day provisional credit SLA at the workflow level.
- Operating procedures test 50 sampled disputes for adherence; sampling approach reference points to a separate sampling memo.
- Limitations section flags reliance on prior-year fraud-dispute test and lists Reg Z billing-error disputes as out of scope (separate test).
- Downstream consumers list `workpaper-drafter` and `qa-workpaper`.
- Confidence label high; reviewer question on whether the test should expand to include in-app dispute submissions launched mid-year.

### Scenario 2: BSA/AML CDD refresh control test plan against FFIEC manual expectations

Input: second-line BSA/AML testing is building a test plan for the periodic CDD refresh control on high-risk customers. Scope is high-risk personal and business customers due for refresh in the period. Source posture is public (FFIEC BSA/AML CDD manual section, 31 CFR 1010.230 [verify]) plus the firm's BSA/AML procedures.

Output emphasizes:
- Test objective is operating effectiveness only; design effectiveness was tested in the prior cycle (referenced).
- Criteria list cites FFIEC BSA/AML manual CDD section [verify] and the firm's high-risk customer refresh standard (12 months for personal, 18 months for business; firm policy).
- Walkthrough plan minimal because design was previously tested; refresher walkthrough only on system changes.
- Operating procedures test that refresh occurred within the policy window, that the refreshed customer risk profile reflects current activity, and that beneficial-ownership re-certification was obtained for entity customers under 31 CFR 1010.230 [verify].
- Sampling approach reference points to a stratified sample by risk tier (CDD-Tier-1, CDD-Tier-2) drawn separately under the `control-sampling` skill.
- Pass criterion: 100% of sampled refreshes within the policy window with current risk profile evidence; fail criterion: any refresh outside the window without escalation evidence.
- Limitations section: testing does not assess the accuracy of the customer risk rating itself (separate test against the CRR methodology).
- Confidence label high on procedures, medium on the firm-policy refresh windows (no external benchmark).

## Common pitfalls

1. Conflating design and operating effectiveness procedures. Walk-through and inspection of policy and system configuration evaluate design. Sample-based reperformance evaluates operation. The plan separates them.
2. Listing procedures without expected evidence. A procedure without an expected artifact cannot be passed or failed cleanly.
3. Skipping the walkthrough for "small" controls. The walkthrough is what tells the reviewer the control as documented matches the control as operated. Skipping it is the most common cause of a "design-gap" exception in testing.
4. Reusing a prior-year plan without restating criteria. Rules change. Reg sections renumber. Firm policies update. The criteria list must be the current period's criteria.
5. Letting first-line owners draft the test plan. The plan is second-line work product; first-line input is welcome but the plan is signed off by the testing reviewer, not the control owner.
6. Treating the plan as a one-off document. The plan is the contract for the workpaper. If the workpaper diverges from the plan, the divergence is a finding in QA review.
