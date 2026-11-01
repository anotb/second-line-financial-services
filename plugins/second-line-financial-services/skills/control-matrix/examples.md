# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## ai-governance-controls

### Example: model-risk control matrix for an internal-build credit-decisioning ML model

#### Input

A national bank's Model Risk Management Office is building the control matrix for a tier-1 retail credit-decisioning model used in unsecured personal-loan origination. The model is a gradient-boosted classifier developed in-house; it influences approve/decline and pricing tier. The persona is the Head of Model Risk (2-line, independent of model development); the audience is the Model Risk Committee, with the matrix later cited in the SR 11-7 / OCC Bulletin 2026-13 program documentation and in the model card. Source posture is mixed: SR 11-7, OCC Bulletin 2026-13, ECOA / Reg B (public) plus the firm's Model Risk Policy and the Adverse Action Notice Standard (firm-policy overlay). Sector overlay: banking. Cross-cutting overlay: cyber (the model's serving environment is in scope of the firm's NYDFS Part 500 program).

#### Why this scenario matters

This is the canonical model-risk application of the matrix and is the matrix that `model-card-builder` consumes for its controls section. It tests three things at once: obligation-anchoring across multiple regulator surfaces (model-risk supervisory guidance plus consumer-compliance rule plus cyber regulation), the control-type discipline (preventive / detective / response / compensating), and the seam where firm policy operationalises a principle-based supervisory expectation. The matrix has to be readable line-by-line by an examiner under SR 11-7 and by a CFPB exam team probing Reg B adverse-action specificity.

#### Output sketch

```yaml
matrix_id: CM-2026-MRM-RET-CR-04
as_of_date: 2026-05-06
engagement_id: ENG-2026-MRM-ANNUAL-12

scope:
  process_or_product: "Tier-1 retail credit-decisioning model lifecycle: development, validation, deployment, monitoring, change management, retirement"
  business_unit: "Retail Credit Underwriting (model owner: Retail Credit Risk; model developer: Decision Sciences)"
  jurisdiction: "US"
  lines_of_defense: ["1L", "2L"]

source_list:
  - {source_type: supervisory-letter, label: "SR 11-7 (interagency model risk management guidance, 2011)", section_reference: "§IV development, §V validation, §VI governance and controls"}
  - {source_type: interagency-guidance, label: "OCC Bulletin 2026-13 (revised interagency model risk management guidance, 2026)", section_reference: "§III.A control environment, §III.B third-party model controls"}
  - {source_type: rule, label: "Regulation B (12 CFR Part 1002)", section_reference: "§1002.9 adverse action notice"}
  - {source_type: examination-manual, label: "CFPB Circular 2022-03 (adverse action notice using AI/algorithms; withdrawn May 12, 2025; historical only)"}
  - {source_type: internal-policy, label: "Firm Model Risk Policy v6.1"}
  - {source_type: internal-standard, label: "Adverse Action Notice Standard v3.0"}

source_posture: mixed

obligations_in_scope:
  - OBL-SR11-7-IV     # Development soundness
  - OBL-SR11-7-V      # Independent validation
  - OBL-SR11-7-VI     # Governance, policies, controls
  - OBL-OCC-2026-13-IIIA  # Control environment refresh
  - OBL-RegB-1002.9   # Adverse action notice specificity

controls:
  - control_id: C-MRM-101
    obligation_id: OBL-SR11-7-IV
    control_objective: "Model development is performed against the firm's Model Development Standard, with documented design rationale, data sourcing decisions, and out-of-time backtest results before submission for validation."
    control_activity: "Decision Sciences submits the model development memo and reproducible build artefacts to the Model Inventory at development completion; sign-off by Head of Decision Sciences gates submission to validation."
    control_type: preventive
    frequency: event-based
    owner: "Head of Decision Sciences"
    evidence:
      - "Model Inventory entry MIN-2026-RET-CR-04"
      - "model development memo path"
      - "reproducible build artefact bundle"
    test_method: inspection
    last_test_date: 2026-02-14
    design_effectiveness: effective
    operating_effectiveness: effective

  - control_id: C-MRM-102
    obligation_id: OBL-SR11-7-V
    control_objective: "Independent validation runs before production deployment and at the firm's defined re-validation cadence; validator is independent of development."
    control_activity: "Model Validation team produces validation report covering conceptual soundness, data and design, performance, robustness, and limitations; report is signed by Head of Model Validation and tabled at Model Risk Committee."
    control_type: preventive
    frequency: "event-based plus annual re-validation"
    owner: "Head of Model Validation"
    evidence:
      - "validation report VAL-2026-RET-CR-04"
      - "Model Risk Committee minutes 2026-03-22"
      - "validator independence attestation"
    test_method: inspection
    last_test_date: 2026-03-22
    design_effectiveness: effective
    operating_effectiveness: effective

  - control_id: C-MRM-104
    obligation_id: OBL-SR11-7-VI
    control_objective: "Production performance is monitored against documented thresholds; threshold breaches trigger documented investigation, escalation, and (where warranted) re-validation."
    control_activity: "Model Performance Monitoring team produces monthly monitoring report covering AUC, KS, PSI on inputs, score-distribution drift, segment performance, and approval-rate drift. Threshold breaches escalate to Head of Model Risk and Head of Retail Credit Risk."
    control_type: detective
    frequency: monthly
    owner: "Head of Model Performance Monitoring (within MRMO)"
    evidence:
      - "monthly monitoring report MON-2026-04"
      - "threshold-breach escalation log"
      - "PSI breach investigation memo (when triggered)"
    test_method: data-analysis
    last_test_date: 2026-04-30
    design_effectiveness: effective
    operating_effectiveness: partially-effective
    open_issue_ids: [ISS-2026-MRM-09]

  - control_id: C-MRM-201
    obligation_id: OBL-RegB-1002.9
    control_objective: "Adverse action notices generated on declines from this model state the specific, accurate principal reasons for the credit decision, consistent with Regulation B §1002.9 (CFPB Circular 2022-03, which restated this point, was withdrawn May 12, 2025; the obligation survives on the regulation)."
    control_activity: "Reason-code mapping from model output to the firm's adverse-action reason library is maintained by the Adverse Action Standard owner; monthly sampling of adverse-action notices by Consumer Compliance to confirm specificity and accuracy."
    control_type: detective
    frequency: monthly
    owner: "Head of Consumer Compliance (sampling); Adverse Action Standard owner (mapping)"
    evidence:
      - "reason-code mapping table v3.0"
      - "monthly notice sampling report"
      - "exception log for notices flagged as non-specific"
    test_method: inspection
    last_test_date: 2026-04-30
    design_effectiveness: effective
    operating_effectiveness: effective

  - control_id: C-MRM-301
    obligation_id: OBL-OCC-2026-13-IIIA
    control_objective: "Material model changes (feature change, training-window shift, score-cutoff change, performance-breach-driven re-fit) trigger documented change-management review prior to deployment."
    control_activity: "Change Management Workflow in the Model Inventory routes material changes to Head of Model Risk for sign-off; deployment is gated on sign-off."
    control_type: preventive
    frequency: event-based
    owner: "Head of Model Risk"
    evidence:
      - "change-management workflow record"
      - "sign-off log in Model Inventory"
    test_method: walkthrough
    last_test_date: 2026-01-15
    design_effectiveness: effective
    operating_effectiveness: effective

  - control_id: C-MRM-401
    obligation_id: OBL-OCC-2026-13-IIIA
    control_objective: "Production-environment access to the model artefact, scoring service, and decisioning logs is least-privilege and logged."
    control_activity: "InfoSec maintains access-control matrix for the model serving environment; quarterly access review by Head of Model Risk and by InfoSec; logs reviewed for anomalies under the firm's NYDFS Part 500 program."
    control_type: preventive
    frequency: "continuous (logging) + quarterly (review)"
    owner: "CISO function (access logging); Head of Model Risk (model-side review)"
    evidence:
      - "access-control matrix"
      - "quarterly access-review attestation"
      - "audit log sample"
    test_method: inspection
    last_test_date: 2026-03-31
    design_effectiveness: effective
    operating_effectiveness: effective

coverage_gaps:
  - obligation_id: OBL-SR11-7-V
    gap_description: "Annual re-validation has been performed for this model, but the SR 11-7 §V expectation that validation address ongoing monitoring outcomes (not just point-in-time performance) is only partially evidenced. The validation report references the monitoring suite without independently testing the monitoring thresholds."
    recommended_action: "Validation team to independently test the monitoring thresholds in the next annual cycle; document in the validation report."

redundancies: []

confidence_label: high

reviewer_questions:
  - "ISS-2026-MRM-09 records a PSI breach on `debt_to_income` ratio that has been investigated but not closed; should the model carry a heightened-monitoring posture pending closure?"
  - "Adverse action notice sampling (C-MRM-201) is performed by Consumer Compliance, not by MRMO. Does the Model Risk Policy expect MRMO independent sampling on top of the Consumer Compliance sample?"
  - "C-MRM-401 is jointly owned (CISO function and Head of Model Risk). Is the joint ownership documented in the firm's RACI for the NYDFS Part 500 program, or only in this matrix?"

human_review_required: true

revisions:
  - {date: 2026-05-06, reason: initial matrix, delta: created during MRMO annual model inventory refresh, approved_by: "Head of Model Risk"}
```

#### What the matrix surfaces

- Obligation-anchoring across three regulatory surfaces: SR 11-7 / OCC Bulletin 2026-13 (model risk), Reg B (consumer compliance), and the cyber overlay onto OCC Bulletin 2026-13 §III.A (control environment) via NYDFS Part 500 access controls. The matrix names each.
- Control-type discipline: C-MRM-101 (preventive: documentation gate on validator submission), C-MRM-102 (preventive: independence-tested validation), C-MRM-104 (detective: monthly monitoring with breach escalation), C-MRM-201 (detective: reason-specificity sampling), C-MRM-301 (preventive: change-management gate), C-MRM-401 (preventive: access controls). No response controls in this slice; if a model failure event triggers a response runbook, that goes in a separate row.
- Joint ownership is captured explicitly. C-MRM-401 names CISO function and Head of Model Risk; the reviewer question probes whether the joint ownership is papered in the firm's NYDFS RACI.
- The reviewer questions are specific. None of them ask generic "is the matrix complete"; each names a control or an obligation.
- Coverage gap is partial-mapping, not absent-mapping: SR 11-7 §V is mapped, but the validation expectation around monitoring-outcome testing is only partially evidenced. The matrix surfaces the partial seam rather than rating the obligation green.

#### Downstream uses

- `model-card-builder` consumes the controls list as the model card's controls section; control IDs in the card cross-reference back to this matrix.
- `compliance-testing` consumes the matrix to scope SR 11-7 compliance test work; the C-MRM-201 sampling cadence informs the test scope on Reg B notice quality.
- `issue-writeup` consumes ISS-2026-MRM-09 to ensure the open PSI-breach issue is properly papered with rating, owner, and remediation plan.
- `exam-brief` for an OCC safety-and-soundness or CFPB exam pulls this matrix as evidence of the firm's model-risk control framework for retail credit decisioning.
- The banking sector overlay (`references/sector-overlays.md#banking`) drives the inclusion of the Reg B obligation row (CFPB Circular 2022-03 was withdrawn May 12, 2025; historical only); without the overlay, the matrix would be SR 11-7-only and would miss the consumer-compliance surface that an exam will probe.

## credit-risk-controls

### Example: BCBS 239 risk-reporting matrix for a credit-risk monthly board pack

#### Input

The Credit Risk function at a $40B regional bank (foreign banking organization, US IHC) is preparing for a regulator-driven BCBS 239 readiness review. The matrix scopes the monthly board credit-risk pack: data aggregation from the credit-loss data warehouse, manual reconciliation of stress-scenario inputs, narrative commentary by the Head of Credit Risk Reporting, and committee tabling. The persona is the Head of Credit Risk Reporting (1.5-line, embedded in the credit-risk function with a risk-reporting mandate); the audience is the firm's Data Management Committee and ultimately the board risk committee. Source posture is mixed: BCBS 239 (public) and the firm's risk-data-aggregation policy (firm-policy overlay).

#### Why this scenario matters

This is the canonical BCBS 239 application of the matrix. BCBS 239 is principle-based, not rule-based, so the obligation set is the principles themselves and the controls are firm-side responses tied to each principle. The example tests the discipline of mapping principle-by-principle and surfacing principles that the firm has not controlled. It also tests the seam between the 1.5-line author (the credit-risk reporting team owns the pack) and the 2-line reviewer (the independent risk-management function challenges it).

#### Output sketch

```yaml
matrix_id: CM-2026-CRR-BCBS239-01
as_of_date: 2026-05-06
engagement_id: ENG-2026-BCBS239-01

scope:
  process_or_product: "Monthly board credit-risk pack: data aggregation, reconciliation, narrative, committee tabling"
  business_unit: "Credit Risk Reporting"
  jurisdiction: "US"
  lines_of_defense: ["1.5L", "2L"]

source_list:
  - {source_type: industry-standard, label: "BCBS 239 — Principles for Effective Risk Data Aggregation and Risk Reporting", section_reference: "Principles 3, 4, 6, 7, 11", url: "https://www.bis.org/publ/bcbs239.htm"}
  - {source_type: internal-policy, label: "Firm Risk Data Aggregation and Reporting Policy v4.2"}

source_posture: mixed

obligations_in_scope:
  - OBL-BCBS239-P03  # Accuracy and integrity
  - OBL-BCBS239-P04  # Completeness
  - OBL-BCBS239-P06  # Adaptability
  - OBL-BCBS239-P07  # Accuracy of reporting
  - OBL-BCBS239-P11  # Distribution

controls:
  - control_id: C-CRR-001
    obligation_id: OBL-BCBS239-P03
    control_objective: "Source-system data feeding the credit-risk pack reconciles to the credit-loss data warehouse of record at month-end with documented variance disposition."
    control_activity: "Credit Risk Reporting team runs monthly reconciliation between credit-loss data warehouse `LGD_v3` extract and the pack input file; variances above firm-policy threshold are dispositioned with named approver."
    control_type: detective
    frequency: monthly
    owner: "Head of Credit Risk Reporting"
    evidence:
      - "credit-loss-data-warehouse:LGD_v3 monthly extract"
      - "reconciliation log path: /grc/crr/recon/<YYYY-MM>"
      - "variance disposition memo (approver named per disposition)"
    test_method: reperformance
    last_test_date: 2026-04-30
    design_effectiveness: effective
    operating_effectiveness: partially-effective
    open_issue_ids: [ISS-2026-CRR-04]

  - control_id: C-CRR-002
    obligation_id: OBL-BCBS239-P04
    control_objective: "All in-scope counterparty exposure data is captured before pack production; identified exclusions are documented with reason and impact."
    control_activity: "Pre-production completeness check against the counterparty master list; exclusions flagged in the pack appendix with reason and impact estimate."
    control_type: preventive
    frequency: monthly
    owner: "Head of Credit Risk Reporting"
    evidence:
      - "completeness check report"
      - "pack appendix exclusions table"
    test_method: inspection
    last_test_date: 2026-04-30
    design_effectiveness: effective
    operating_effectiveness: effective

  - control_id: C-CRR-004
    obligation_id: OBL-BCBS239-P07
    control_objective: "Narrative commentary in the pack reflects the underlying data and is not adjusted for tone after committee preview."
    control_activity: "Head of Credit Risk Reporting signs off on commentary prior to committee distribution; any post-distribution changes require committee chair countersignature."
    control_type: preventive
    frequency: monthly
    owner: "Head of Credit Risk Reporting"
    evidence:
      - "commentary sign-off log"
      - "version-control history on pack file"
    test_method: walkthrough
    last_test_date: 2026-03-31
    design_effectiveness: effective
    operating_effectiveness: not-tested

  - control_id: C-CRR-005
    obligation_id: OBL-BCBS239-P11
    control_objective: "Pack distribution is restricted to named recipients; out-of-cycle distribution requires documented justification."
    control_activity: "DLP-policy-tagged distribution from the document management system; out-of-cycle requests routed through Risk Reporting inbox with approver."
    control_type: preventive
    frequency: event-based
    owner: "Head of Credit Risk Reporting"
    evidence:
      - "DLP distribution log"
      - "out-of-cycle request inbox"
    test_method: inspection
    last_test_date: 2026-04-30
    design_effectiveness: effective
    operating_effectiveness: effective

coverage_gaps:
  - obligation_id: OBL-BCBS239-P06
    gap_description: "Adaptability principle is uncontrolled. Pack regenerates manually under stress scenarios; there is no pre-tested capability to produce ad-hoc cuts (geography, sector, vintage) inside the regulator's typical request window. The firm's stress-testing team can produce slices on request but not within the timing the principle implies."
    recommended_action: "Scope a stand-up of pre-defined ad-hoc cut templates with the Stress Testing team; assign accountable owner; build evidence pathway."

redundancies: []

confidence_label: medium

reviewer_questions:
  - "Does the firm have a documented data-quality threshold framework that names the variance bands and disposition authorities for control C-CRR-001? The reconciliation log references thresholds without an inspectable framework document."
  - "Should adaptability (Principle 6) coverage sit with Credit Risk Reporting or with the Stress Testing function? The gap is real; the owner is contested."
  - "ISS-2026-CRR-04 (recurring reconciliation variances on three counterparties) has been open since 2025-11. Is the operating-effectiveness rating on C-CRR-001 still `partially-effective` or has it slipped?"

human_review_required: true

revisions:
  - {date: 2026-05-06, reason: initial matrix, delta: created from BCBS 239 readiness review scope, approved_by: "Head of Credit Risk Reporting"}
```

#### What the matrix surfaces

- The matrix is principle-anchored. Each row points at a BCBS 239 principle and ties evidence to the source-system report (the LGD warehouse extract) and the reconciliation log path, not to the policy document.
- Principle 6 (adaptability) is the un-controlled principle. The matrix surfaces it explicitly in `coverage_gaps` rather than letting it sit silently.
- Confidence is medium because two of the four mapped controls have effectiveness ratings that flex (`partially-effective` on C-CRR-001 with an open issue, `not-tested` on C-CRR-004), and the data-quality threshold framework underneath C-CRR-001 has not been confirmed by the reviewer.
- Reviewer questions are specific to this matrix. They name the obligations, the controls, and the open issue rather than asking generic "is the matrix complete" prompts.
- The matrix consumes the upstream `obligation-mapping` output (the `OBL-BCBS239-*` IDs) and emits the `coverage_gaps[].obligation_id` references back into the obligation set, so the next obligation review knows the adaptability obligation is unmapped and stays open.

#### Downstream uses

- `compliance-testing` consumes the controls list to scope its test plan; controls with `last_test_date` older than 18 months go to the top of the test queue.
- `issue-writeup` consumes `open_issue_ids` to ensure each open issue is properly papered with rating, owner, and remediation plan.
- `risk-committee-pack` for the board risk committee references this matrix as the underlying control evidence for the BCBS 239 readiness narrative.

## troubleshooting

### Troubleshooting: control-matrix

Recurring failure modes when a control matrix looks complete but is not. The reviewer review should catch these; the builder review should preempt them.

#### 1. Controls listed without an obligation source

Symptom: the matrix has thirty rows; ten of them have no entry in the obligation-source column. The reviewer cannot tell why those controls exist.

Why it happens: hygiene controls (data-quality housekeeping, internal sign-offs, "we always do this") get ported in because the team performs them, not because an obligation requires them. Or the obligation extraction is incomplete and the controls drift in ahead of their parent obligations.

Fix: every row carries an `obligation_id`. If the control is a hygiene control, move it out of the matrix into the firm's procedure documentation. If the control is real and the obligation is missing, the upstream `obligation-mapping` work is incomplete; flag it in `coverage_gaps` rather than improvise an obligation. The matrix is obligation-anchored; that is the discipline.

#### 2. Control objective and control activity collapsed into one field

Symptom: the row's control objective reads "the team reconciles the warehouse extract monthly". That is not an objective; it is an activity.

Why it happens: practitioners write what the team does because it is concrete, and skip the underlying condition the activity is supposed to make true.

Fix: the objective is the condition that must be true ("source-system data feeding the credit-risk pack reconciles to the system of record at month-end with documented variance disposition"). The activity is who does what, how often, using what system. Both fields are required. Rows with one but not the other are not yet controls; they are placeholders. The schema enforces both fields on `control.schema.json`.

#### 3. Policy listed as evidence

Symptom: the evidence pointer column reads "Risk Reporting Policy v4.2". The reviewer cannot test from a policy.

Why it happens: the policy is the easiest artifact to point at and is already approved by the committee. Pointing at it feels safer than pointing at the operational record.

Fix: policy is a control statement, not evidence of operation. The evidence pointer is a system-of-record output, a sample report ID, a sign-off log path, a reconciliation log entry. "Risk Reporting Policy v4.2 §3.2" can appear as the obligation-source label or as the firm-policy citation; it does not appear in the evidence column. If no operational evidence exists, the row is `not-tested`; that surfaces the gap honestly.

#### 4. Control owner is a team, not a role

Symptom: owner column reads "Risk Team", "Compliance", "Operations".

Why it happens: the engagement has not yet pinned down the named accountable role, and the team-level label feels right at the level of generality the matrix was drafted at.

Fix: the owner is a named role with accountability: Head of Model Risk, Chief Privacy Officer, Head of Vendor Management, Head of Credit Risk Reporting, BSA Officer. "Risk team" is not an owner. If the role is genuinely contested or shared, name both ("Head of Decision Sciences for development; Head of Model Validation for validation") and add a reviewer question on the joint-ownership documentation.

#### 5. Coverage gaps section is empty

Symptom: every obligation in scope has a mapped control. The matrix looks clean.

Why it happens: gaps were buried (the partial mapping was rated effective rather than partially-effective), or obligations were dropped from scope rather than admitted as uncovered.

Fix: a control matrix without coverage gaps is rare in real engagements. Either obligation extraction was over-narrow, or partial mappings were over-rated, or hygiene controls were treated as substantive. Re-walk the obligation list and ask "is the operating evidence sufficient that an examiner reading this row would call it covered?" If no, the row is a coverage gap or a partial-mapping with a downgraded effectiveness rating. Empty `coverage_gaps` should trigger a sign-off question, not a confidence boost.

#### 6. Effectiveness ratings inflate over time

Symptom: third refresh of the matrix shows every control rated effective; the prior matrix showed three partially-effective rows. No remediation evidence appears in the revision log.

Why it happens: each refresh tends to refresh ratings without re-testing. The ratings drift to whatever the team thinks is reasonable rather than what the most recent test actually showed.

Fix: a rating change requires a test result that supports it. The `last_test_date` and the upstream test workpaper (from `compliance-testing` or internal audit) are the evidence. Without a refreshed test, the prior rating carries forward; the matrix does not invent improvements. The `revisions` section names what changed and why.

#### 7. Cyber overlay loaded but ignored

Symptom: the scope flags `cyber` in the cross-cutting overlay set; the matrix has no cyber-tagged rows. The cyber overlay was loaded but did not land in the matrix.

Why it happens: the overlay is treated as background reading rather than as content that adds rows. Or the matrix author defers cyber to "the CISO's separate matrix" without surfacing the cyber-tagged rows the substantive process needs.

Fix: when `cyber` is in the cross-cutting set, the matrix carries cyber-tagged rows for the in-scope process: governance, identity-and-access, vulnerability, incident-response, third-party-cyber, data-protection. The CISO function is a co-owner or reviewer on those rows; it is not an excuse to leave them out of the substantive matrix. Same logic for the `privacy` overlay.

#### 8. Sector overlay loaded but ignored

Symptom: banking sector overlay loaded but the matrix has no Heightened-Standards rows for a Heightened-Standards-covered bank; insurance overlay loaded but no MAR §16 rows for an ICFR-in-scope insurer; capital-markets overlay loaded but no annual-review-cycle rows for an adviser.

Why it happens: the overlay is treated as background framing rather than as a directive on what rows the matrix carries.

Fix: when the scope names a sector, the matching `references/sector-overlays.md#<sector>` content lands as named rows in the matrix. The overlay's "what changes" content is the contract; the matrix author honours it. Sector-specific reviewer questions go to the reviewer-question list.

#### 9. Joint ownership left implicit

Symptom: a model-risk control row names "Head of Model Risk" as the owner; the underlying control is access-control on the model serving environment, which is operationally owned by the CISO function. The matrix does not surface the joint ownership.

Why it happens: the matrix author owns the matrix and writes the owner from their seat. The CISO function does not see the matrix until much later.

Fix: joint ownership is a row attribute. Name both roles when both are accountable; name the primary explicitly. Add a reviewer question on whether the joint ownership is papered in the firm's RACI or only in this matrix. Joint ownership is common; obscuring it is a finding waiting to happen.

#### 10. The matrix is signed off without independent reviewer

Symptom: sign-off block names the practitioner who built the matrix and the sponsor; no independent reviewer is named.

Why it happens: smaller engagements compress the review machinery; larger engagements over-rely on the sponsor as the reviewer.

Fix: the reviewer is independent of the author. For 1.5-line-built matrices, the 2-line function reviews. For 2-line-built matrices, internal audit or an independent peer reviews. For advisory-built matrices, the engagement partner reviews. The sponsor signs off as accountable, not as the independent reviewer; a single name in both seats fails the independence test.

#### 11. Test method is "inquiry" by default

Symptom: most rows show `test_method: inquiry`. Reviewer cannot tell whether the controls actually operate.

Why it happens: inquiry is the cheapest test method (talk to the owner, ask if it ran). It is also the weakest evidence on operating effectiveness.

Fix: inquiry alone is rarely sufficient for operating-effectiveness evidence on controls that produce inspectable artifacts. Match the test method to the control: inspection (sample artifacts), reperformance (re-run the control on a sample), observation (watch the control execute), data-analysis (population-level analytics), walkthrough (end-to-end transaction trace). Inquiry-only rows are flagged in reviewer questions.

#### 12. The matrix tries to be the model card, the test workpaper, and the binder

Symptom: the matrix carries ten columns of model documentation, test sample listings, and evidence file contents. It is unreadable.

Why it happens: the matrix gets stretched because adjacent skills' outputs are not yet built and the team puts everything in the matrix as a stopgap.

Fix: the matrix lives upstream of `compliance-testing` (the test workpaper), `model-card-builder` (the model card), and `evidence-binder` (the binder). It carries the row-level summary; the upstream artifacts carry the depth. Cross-references via `control_id` and `obligation_id`. Pulling everything into the matrix breaks the contract with downstream skills.

#### 13. The matrix stops too late

Symptom: the skill produces a "signed-off" matrix with effectiveness ratings asserted and remediation actions claimed as in-flight, without evidence.

Why it happens: builder over-runs the human-review gate.

Fix: the matrix is a draft until the named reviewer attests. The skill stops at the draft and surfaces the reviewer questions; it does not assert sign-off, distribute, or post to the GRC system. The `human_review_required` field is always true.
