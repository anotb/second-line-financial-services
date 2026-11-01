# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## g-sib-supervisory-response

### Example: G-SIB FBO self-assessment ahead of an ECB SREP review

#### Input

A non-US G-SIB with significant US operations under FRB Y-7 reporting and an SSM-supervised EU subsidiary. The ECB has flagged risk data aggregation as a thematic SREP focus for the cycle. The engagement is run by the group CRO function with the EU-subsidiary head of risk reporting embedded. Source posture is `public-plus-firm-policy-plus-evidence`. The prior-year self-assessment carried an overall `largely-compliant` rating; the current cycle needs to address the ECB Guide on effective risk data aggregation and risk reporting (May 2024) incremental expectations distinct from the BCBS 239 baseline. Climate reporting reaches the EU subsidiary's management board, so climate-data lineage is in scope under Principles 3 and 6.

#### Why this scenario matters

It exercises the cross-border supervisory lens. Principle 14 (home/host cooperation) carries weight that a single-jurisdiction self-assessment never does. The ECB Guide overlay is distinguished from the BCBS 239 baseline in the per-principle blocks so the firm can read the same assessment from either supervisor's lens. The cross-cutting climate overlay loads, and the climate-data lineage finding lands inside the Principle 3 and Principle 6 blocks rather than in a separate appendix. A new gap surfaces under Principle 11 (distribution controls on the EU subsidiary's risk pack) that the prior-year assessment had missed.

#### Output sketch

```yaml
assessment_id: BCBS239-2026-ECB-SREP-02
scope_id: ENG-2026-ECB-SREP-02

scope:
  legal_entity_perimeter:
    - Group HoldCo (home jurisdiction)
    - US IHC (FRB Y-7 reporter)
    - EU Subsidiary (SSM-supervised)
  supervisory_context: multi-jurisdiction
  supervisory_context_notes: ECB SREP thematic on RDARR; FRB consolidated supervision; home supervisor as lead
  assessment_date: 2026-05-06
  prior_assessment_date: 2025-04-15
  prior_overall_rating: largely-compliant

methodology:
  lines_of_evidence:
    - document-review
    - system-tracing
    - reconciliation-test
    - interview
    - ad-hoc-aggregation-run
  interview_count: 31
  document_count: 124
  reconciliation_test_count: 6
  manual_workaround_inventory_status: captured
  ad_hoc_aggregation_evidence: recent-runs-evidenced

principles:
  - principle_number: 1
    principle_group: overarching
    principle_name: Governance
    rating: largely-compliant
    direction: improving
    evidence_summary: >
      Group Risk Data Council reviewed; charters of US IHC and EU subsidiary
      data councils reviewed; CDO direct line to group CRO confirmed at all
      three entities.
    ecb_overlay_delta: >
      ECB Guide expects an explicit data-quality-management framework reviewed
      annually by the management body; EU subsidiary framework was last
      reviewed thirteen months ago.
    per_entity_ratings:
      - legal_entity: Group HoldCo
        rating: largely-compliant
      - legal_entity: US IHC
        rating: largely-compliant
      - legal_entity: EU Subsidiary
        rating: largely-compliant
        rationale: >
          ECB Guide expectation on annual management-body review of the data-
          quality-management framework is currently overdue but has a near-term
          remediation date.
    gaps:
      - gap_id: P1-G1
        gap_description: >
          EU subsidiary's data-quality-management framework annual management-
          body review is overdue by one month against the ECB Guide expectation.
        severity: medium
        owner: EU Subsidiary Head of Risk Reporting
    recommended_actions:
      - action_description: >
          Schedule the EU subsidiary management-body review of the data-quality-
          management framework before the SREP submission.
        owner: EU Subsidiary Head of Risk Reporting
        target_date: 2026-06-30

  - principle_number: 3
    principle_group: aggregation
    principle_name: Accuracy and integrity
    rating: largely-compliant
    direction: stable
    evidence_summary: >
      Reconciliation tests across credit, market, liquidity, and operational
      risk evidenced; manual workaround inventory captured (29 entries);
      climate-data lineage reviewed, including vendor-supplied scenario data
      and sustainability-provider feeds.
    ecb_overlay_delta: >
      ECB Guide raises expectations on data-quality measurement and reporting
      to the management body; the firm's data-quality KPI set is current but
      the threshold framework is being refreshed against the ECB expectation.
    gaps:
      - gap_id: P3-G1
        gap_description: >
          Climate-data lineage from vendor-supplied scenario provider through
          to the EU subsidiary's climate stress aggregation is documented but
          not reconciliation-tested; vendor refresh cadence is unverified
          against the firm's quarterly stress cycle.
        severity: high
        owner: EU Subsidiary Head of Risk Data
    recommended_actions:
      - action_description: >
          Add a quarterly reconciliation test for climate-scenario vendor data
          aligned to the climate stress cycle; verify vendor refresh cadence
          before each cycle close.
        owner: EU Subsidiary Head of Risk Data
        target_date: 2026-12-31

  - principle_number: 6
    principle_group: aggregation
    principle_name: Adaptability
    rating: largely-compliant
    direction: improving
    evidence_summary: >
      Three ad-hoc stress aggregations run in the last six months; group-level
      runs delivered within 48 hours; EU-subsidiary runs delivered within 72
      hours; climate-stress run delivered within five business days.
    ecb_overlay_delta: >
      ECB Guide highlights climate-stress adaptability; the EU subsidiary's
      climate-stress timeframe sits behind the BCBS expectation and is the
      explicit ECB Guide finding.
    gaps:
      - gap_id: P6-G1
        gap_description: >
          Climate-stress aggregation timeframe (five business days) lags the
          general-stress timeframe; ECB Guide flags this for SSM-supervised
          entities.
        severity: high
        owner: EU Subsidiary Head of Risk Data
    recommended_actions:
      - action_description: >
          Reduce climate-stress aggregation timeframe to 48 hours through
          analytics-layer investment already approved at group level; deliver
          before the next ECB climate-stress exercise.
        owner: EU Subsidiary Head of Risk Data
        target_date: 2027-03-31

  - principle_number: 11
    principle_group: reporting
    principle_name: Distribution
    rating: materially-non-compliant
    direction: deteriorating
    evidence_summary: >
      Distribution-list controls reviewed; classification labelling sampled
      across three risk-pack cycles; redaction protocols evidenced for the
      group risk pack but not for the EU subsidiary risk pack.
    ecb_overlay_delta: >
      ECB Guide expects controlled distribution of risk reports including
      classification and need-to-know enforcement; EU subsidiary distribution
      practice falls short.
    per_entity_ratings:
      - legal_entity: Group HoldCo
        rating: largely-compliant
      - legal_entity: US IHC
        rating: largely-compliant
      - legal_entity: EU Subsidiary
        rating: materially-non-compliant
        rationale: >
          EU subsidiary risk pack was distributed beyond the SSM perimeter
          without classification controls in two of the last three cycles.
    gaps:
      - gap_id: P11-G1
        gap_description: >
          EU subsidiary risk pack distributed beyond the SSM perimeter without
          classification labelling in two of the last three quarterly cycles.
        severity: critical
        owner: EU Subsidiary Head of Risk Reporting
    recommended_actions:
      - action_description: >
          Apply classification labelling and need-to-know distribution controls
          to the EU subsidiary risk pack; remediate the two prior-cycle
          breaches with a documented retrospective analysis.
        owner: EU Subsidiary Head of Risk Reporting
        target_date: 2026-08-31

  - principle_number: 14
    principle_group: supervisory
    principle_name: Home/host cooperation
    rating: largely-compliant
    direction: stable
    evidence_summary: >
      Home/host data-sharing protocol reviewed; supervisory college submission
      for prior cycle reviewed; FRB Y-7 reporting and ECB SREP submission
      timelines deconflicted; cross-border issue-escalation path documented.
    ecb_overlay_delta: >
      ECB Guide stresses the supervisory-college role; the firm's protocol is
      consistent with the expectation.
    gaps: []
    recommended_actions: []

  # Principles 2, 4, 5, 7-10, 12, 13 omitted from sketch for brevity.

aggregate_rating_per_group:
  - group: overarching
    rating: largely-compliant
    rationale: ECB Guide annual-review delta on the EU subsidiary; otherwise stable.
  - group: aggregation
    rating: largely-compliant
    rationale: P3 climate-data finding and P6 climate-stress timeframe gap; otherwise stable.
  - group: reporting
    rating: materially-non-compliant
    rationale: P11 EU subsidiary distribution finding drives the group rating.
  - group: supervisory
    rating: largely-compliant
    rationale: P13 reflects no open MRAs at SSM; P14 stable.

overall_rating: largely-compliant

priority_gaps_top_5: [P11-G1, P3-G1, P6-G1, P1-G1]

linked_open_issues: []

cross_cutting_overlays_applied: [climate]

confidence_label: medium

human_review_required: true

sign_offs:
  - role: EU Subsidiary Head of Risk Reporting
    status: pending
  - role: EU Subsidiary Head of Risk Data
    status: pending
  - role: Group Head of Risk Reporting
    status: pending
  - role: Group CRO
    status: pending

reviewer_questions:
  - >
    Should the EU subsidiary's P11 finding be reported to the SSM ahead of the
    SREP submission as a self-disclosed issue, or surfaced through the
    submission?
  - >
    Does the climate-data reconciliation test under P3-G1 need to be coordinated
    with the model-validation team given the scenario-vendor model dependency?
  - >
    The confidence label is medium because some EU-subsidiary evidence is
    pending translation; should the assessment be re-rated to high after
    translation completes?
```

#### Why the assessment shape matters downstream

- The ECB Guide overlay deltas are written into the per-principle blocks rather than as a separate appendix, so the SSM reviewer sees the SSM-relevant findings inside the principle they apply to.
- The per-entity rating array surfaces the EU-subsidiary-specific finding under Principle 11 without forcing the group rating down.
- The climate cross-cutting overlay is recorded in `cross_cutting_overlays_applied`, so downstream consumers (risk-committee-pack, the SREP submission file) inherit the overlay flag.
- The `confidence_label: medium` reflects the methodology constraint (pending translations); it is not a finding-driven rating, and the reviewer question makes the path to `high` explicit.

## regional-bank-self-assessment

### Example: D-SIB self-assessment ahead of an FRB horizontal review

#### Input

A US D-SIB (consolidated assets in the $100B-$700B band) is notified of an upcoming FRB horizontal review on risk data aggregation and risk reporting. The CRO and CDO are jointly running the self-assessment with internal audit shadowing. Source posture is `public-plus-firm-policy-plus-evidence`: the engagement has access to the policy library, the risk-data warehouse, the regulatory-reporting layer, and the issue register, and is scoped to run reconciliation tests across credit, market, liquidity, and operational risk. Two open MRAs from the prior FRB letter sit in the issue register, both touching risk data.

#### Why this scenario matters

It is the canonical large-bank exam-readiness use of the skill. The horizontal-review trigger forces a full fourteen-principle pass with reconciliation evidence, not a desk-review. The MRA posture forces Principle 13 to read against named open findings rather than as a generic statement. The asset-size band brings 12 CFR Part 30 Appendix D into Principle 1 and Principle 2. Principle 6 (adaptability) carries the heaviest gap commentary, mirroring the BCBS thematic-finding pattern.

#### Output sketch

```yaml
assessment_id: BCBS239-2026-FRB-HRZ-04
scope_id: ENG-2026-FRB-HRZ-04

scope:
  legal_entity_perimeter: [Bancorp, lead bank, broker-dealer subsidiary]
  supervisory_context: FRB
  supervisory_context_notes: FRB horizontal RDARR review; OCC Heightened Standards covered bank
  assessment_date: 2026-05-06
  prior_assessment_date: 2025-03-31
  prior_overall_rating: largely-compliant

methodology:
  lines_of_evidence:
    - document-review
    - system-tracing
    - reconciliation-test
    - interview
    - ad-hoc-aggregation-run
  interview_count: 22
  document_count: 86
  reconciliation_test_count: 4
  manual_workaround_inventory_status: captured
  ad_hoc_aggregation_evidence: recent-runs-evidenced

principles:
  - principle_number: 1
    principle_group: overarching
    principle_name: Governance
    rating: largely-compliant
    direction: stable
    evidence_summary: >
      Risk Data Council charter reviewed; CDO direct line to CRO confirmed;
      board-level data-quality reporting evidenced quarterly; named risk-data
      issues escalated through the issue register.
    gaps:
      - gap_id: P1-G1
        gap_description: >
          Board reporting on data-quality KPIs lacks trend commentary; the pack
          presents current-quarter values without comparison or root cause.
        severity: medium
        owner: Head of Risk Reporting
        linked_issue_id: null
        evidence_pointer: Q1-2026 Risk Committee pack, section 6.3
    recommended_actions:
      - action_description: >
          Add trend commentary and root-cause attribution to the quarterly
          board-level data-quality KPI block.
        owner: Head of Risk Reporting
        target_date: 2026-09-30

  - principle_number: 2
    principle_group: overarching
    principle_name: Data architecture and IT infrastructure
    rating: materially-non-compliant
    direction: stable
    evidence_summary: >
      Architecture diagrams reviewed; lineage spot-checked across credit and
      market risk; manual reconciliation between two market-risk source systems
      observed; lack of automated lineage from credit-loss data warehouse to
      regulatory-reporting layer evidenced.
    gaps:
      - gap_id: P2-G1
        gap_description: >
          Manual reconciliation between two market-risk source systems persists
          eighteen months after the consolidation roadmap was approved.
        severity: high
        owner: Head of Risk Data (CDO)
        linked_issue_id: MRA-2025-04
      - gap_id: P2-G2
        gap_description: >
          No automated data lineage from the credit-loss data warehouse to the
          regulatory-reporting layer; lineage is reconstructed manually each
          reporting cycle.
        severity: critical
        owner: Head of Risk Data (CDO)
        linked_issue_id: MRA-2025-07
    recommended_actions:
      - action_description: >
          Complete the market-risk source-system consolidation per the approved
          roadmap; eliminate the manual reconciliation step.
        owner: Head of Risk Data (CDO)
        target_date: 2027-03-31
        dependency_ids: [P2-G1]
      - action_description: >
          Stand up automated lineage from the credit-loss warehouse through to
          the FR Y-9C and FR Y-14 layers.
        owner: Head of Risk Data (CDO)
        target_date: 2027-06-30
        dependency_ids: [P2-G2]

  - principle_number: 3
    principle_group: aggregation
    principle_name: Accuracy and integrity
    rating: materially-non-compliant
    direction: stable
    evidence_summary: >
      Reconciliation tests run for credit, market, liquidity, and operational
      risk; manual workaround inventory complete with 47 entries; data-quality
      framework reviewed with severity-rated issue trend.
    gaps:
      - gap_id: P3-G1
        gap_description: >
          47 manual workarounds catalogued, of which 12 are critical-severity
          and have been outstanding for more than two reporting cycles.
        severity: high
        owner: Head of Risk Data (CDO)
    recommended_actions:
      - action_description: >
          Burn down the 12 critical-severity manual workarounds against a
          time-bound retirement plan with quarterly reporting to the Risk Data
          Council.
        owner: Head of Risk Data (CDO)
        target_date: 2026-12-31

  - principle_number: 6
    principle_group: aggregation
    principle_name: Adaptability
    rating: materially-non-compliant
    direction: improving
    evidence_summary: >
      Two ad-hoc stress aggregations run in the last six months; both delivered
      in five business days against a target of 48 hours; recent investment in
      the analytics layer is in flight but not yet evidenced through a delivery.
    gaps:
      - gap_id: P6-G1
        gap_description: >
          Ad-hoc and stress-scenario aggregations consistently exceed the
          48-hour target; current best-case is five business days.
        severity: critical
        owner: Head of Risk Data (CDO)
    recommended_actions:
      - action_description: >
          Deliver the in-flight analytics-layer investment to enable ad-hoc and
          stress-scenario aggregation within 48 hours; evidence with a dry run
          before sign-off.
        owner: Head of Risk Data (CDO)
        target_date: 2026-12-31

  # Principles 4, 5, 7-14 omitted from sketch for brevity; full assessment carries all 14.

aggregate_rating_per_group:
  - group: overarching
    rating: materially-non-compliant
    rationale: P2 critical gap drives the group rating.
  - group: aggregation
    rating: materially-non-compliant
    rationale: P3 and P6 critical gaps; P4 and P5 largely-compliant.
  - group: reporting
    rating: largely-compliant
    rationale: P7, P8, P11 largely-compliant; P9 and P10 compliant.
  - group: supervisory
    rating: largely-compliant
    rationale: P13 reflects two open MRAs; P12 and P14 stable.

overall_rating: materially-non-compliant

priority_gaps_top_5: [P2-G2, P6-G1, P2-G1, P3-G1, P1-G1]

linked_open_issues: [MRA-2025-04, MRA-2025-07]

confidence_label: high

human_review_required: true

sign_offs:
  - role: Head of Risk Reporting
    status: pending
  - role: Head of Risk Data (CDO)
    status: pending
  - role: CRO
    status: pending
  - role: Chief Internal Auditor
    status: pending

reviewer_questions:
  - >
    Are we comfortable that the P2-G2 lineage gap is paced for the FRB horizontal
    review window, given the linked MRA's existing target date?
  - >
    Should the P6-G1 dry run be witnessed by the OCC examination team given the
    overlap with the heightened-standards thematic?
  - >
    Does the manual-workaround burn-down plan need a Risk Committee escalation
    trigger if the critical-severity count does not fall below six by Q3?
```

#### Why the assessment shape matters downstream

- The Top 5 priority gaps drive the remediation roadmap that goes to the data-management committee and the Risk Committee.
- `linked_open_issues` ties the Principle 13 rating to the named open MRAs, so the supervisor reads consistency between the FRB letter, the issue register, and this assessment.
- The `confidence_label: high` is supportable because the methodology block evidences multiple lines of evidence per principle in groups B and C; a thinner methodology would not support `high`.
- The structured record feeds the BCBS 239 data-confidence appendix in `risk-committee-pack` for the next cycle, so the committee pack carries a consistent posture statement.

## troubleshooting

### Troubleshooting: bcbs239-gap-assessment

Recurring failure modes when a BCBS 239 gap assessment looks complete but is not. The reviewer pass should catch these; the builder pass should preempt them.

#### Rating without testing

Symptom: principle ratings draw on document review and interviews only. No reconciliation tests, no system tracing, no recent ad-hoc-aggregation evidence. Confidence label set to `high` regardless.

Why it happens: testing is expensive and the engagement timeline is short. Rating from documentation feels close enough.

Fix: at least one reconciliation test or system tracing per principle in Group B (Principles 3-6) and Group C (Principles 7-11). Methodology section names the lines of evidence per principle. The `high` confidence label requires multi-line evidence (document plus system plus reconciliation) on those groups; a single-line methodology fails the confidence-label gate.

#### Principle 6 lip service

Symptom: Principle 6 (adaptability) rated `largely-compliant` or above with no recent ad-hoc-aggregation evidence. The gap commentary is generic.

Why it happens: ad-hoc and stress-scenario aggregation runs are rare events; the engagement window may not include one.

Fix: any rating above `materially-non-compliant` on Principle 6 requires evidence of recent ad-hoc and stress-scenario aggregation runs within the required timeframe. Where no recent run is evidenced, the rating defaults to `materially-non-compliant` and the engagement carries an action to schedule and run an ad-hoc aggregation as part of the remediation plan. The BCBS thematic-finding pattern is clear; supervisors probe Principle 6 first.

#### Manual workarounds invisible

Symptom: Principle 2 (data architecture) and Principle 3 (accuracy) rated cleanly with no manual-workaround inventory. The risk-data layer is implicitly described as fully automated.

Why it happens: manual workarounds (Excel-based aggregations, off-system reconciliations, RPA bridging) live in operations and are rarely surfaced to the formal data-architecture inventory.

Fix: the methodology section requires an explicit manual-workaround inventory. An empty inventory at a large bank is implausible and triggers a reviewer question. The inventory names the workaround, the risk type and reporting it serves, the owner, and the remediation status.

#### Confusing risk reporting with financial reporting

Symptom: SOX 404 evidence cited as Principle 3 or Principle 7 evidence; financial-statement data-quality controls treated as risk-data controls.

Why it happens: the controls vocabulary overlaps and the same data warehouses sometimes serve both regimes.

Fix: BCBS 239 is risk-data-anchored. SOX 404 is financial-statement-anchored. The doctrines do not substitute. The assessment cites SOX 404 evidence only where the risk-data layer shares infrastructure with the financial-reporting layer, and even then the evidence is labelled as the financial-reporting view, not as Principle 3 or Principle 7 evidence on the risk side.

#### Open MRAs not linked

Symptom: Principle 13 (Remedial actions) reads as a generic statement of remediation discipline. Open MRAs, MRIAs, and 4(m) actions on the risk-data layer are not named.

Why it happens: the issue register lives in a separate system from the assessment workpapers; the linkage is left for later.

Fix: Principle 13 entries link to open supervisory findings on risk data by issue-register ID. The assessment's `linked_open_issues[]` field carries the named findings. An empty Principle 13 finding-set at a large bank is not credible; supervisors expect linkage to the firm's open-finding population on the risk-data layer.

#### Cross-border ratings averaged

Symptom: a multi-entity G-SIB or FBO assessment carries a single set of ratings across all legal entities. Per-entity variation is not visible.

Why it happens: aggregation is easier than per-entity assessment, and the consolidated frame is the headline.

Fix: per-entity ratings where the entities differ materially. The aggregation rationale is part of the methodology section. For an FBO with a US IHC, the IHC carries its own ratings independent of the parent group; the assessment surfaces both.

#### Climate-data lineage out of scope

Symptom: a firm reporting climate risk to the committee carries no climate-data section in the assessment. Vendor-supplied climate-scenario data is treated as background.

Why it happens: climate is a newer reporting domain and the BCBS 239 assessment template does not natively prompt for it.

Fix: where the firm reports climate to the committee, climate-data lineage is in scope under Principles 3 and 6. The cross-cutting climate overlay (where loaded) supplies the criteria. Vendor-supplied scenario data is named, the lineage is traced, and the adaptability of the data layer to ad-hoc climate stress requests is evidenced.

#### Confidence label inflation

Symptom: confidence label set to `high` on an assessment with thin methodology (document review only, no reconciliation, no recent ad-hoc-aggregation evidence).

Why it happens: confidence-label setting is treated as a finding-quality statement rather than as a methodology-quality statement. A clean rating feels like high confidence.

Fix: the confidence label is methodology-anchored, not finding-anchored. `high` requires multi-line evidence (document plus system plus reconciliation) per principle in Groups B and C. `medium` is the default where the methodology is solid but one line of evidence is thin. `low` is the default where the engagement was scoped to desk review only. The label is set against the methodology, not against the rating.

#### Aggregate rating set before per-principle ratings settle

Symptom: the executive summary leads with an overall rating that does not reconcile to the per-principle ratings in the body. Group-level aggregations do not match the principle entries.

Why it happens: the executive summary is drafted first from a holistic read; the body is drafted later from the evidence; the two are never reconciled.

Fix: the aggregate ratings (per group and overall) are computed from the per-principle ratings, not asserted independently. The methodology section names the aggregation rule (e.g., a `materially-non-compliant` rating on any one principle drives the group rating to at least `materially-non-compliant`; or whatever rule the firm uses). The executive summary is reconciled against the body before sign-off.

#### Supervisory-context block too generic

Symptom: the supervisory-context block names the regulators (FRB, OCC, ECB) but does not name the operative letter or guide (SR 12-17, 12 CFR Part 30 Appendix D, ECB Guide May 2024). The reviewer cannot tell which expectations are operative.

Why it happens: the regulator-naming feels sufficient and the source-anchors file carries the detail.

Fix: the supervisory-context block names the operative letter or guide for each regulator in scope. The detail lives in `references/source-anchors.md`; the block names which anchor applies to this engagement and why.

#### ECB Guide overlay mixed into BCBS 239 baseline

Symptom: an ECB-supervised entity's assessment cites ECB Guide expectations as if they were BCBS 239 baseline. A reader cannot distinguish what BCBS 239 requires from what the ECB Guide adds.

Why it happens: the ECB Guide builds on BCBS 239 and the language overlaps.

Fix: the assessment distinguishes BCBS 239 baseline from ECB Guide overlay within each affected principle (typically Principles 1, 2, 3, 6, and 11). The principle entry carries a baseline statement and an ECB-overlay statement where the overlay applies. A reviewer reading the assessment from either supervisor's lens sees the relevant content.

#### Sector overlay loaded but ignored

Symptom: the assessment is on an OCC-supervised covered bank but Principle 1 and Principle 2 entries do not name the OCC Heightened Standards §II reach. Or the assessment is on an insurance group but the principles do not map to ORSA / ICP analogues.

Why it happens: the overlay file exists in references/ but the assessment-writer treated it as background reading.

Fix: when the scope names a sector, the matching `references/sector-overlays.md#<sector>` content lands as named items in the assessment. For banking, the OCC Heightened Standards §II reach lands in Principles 1, 2, and 11 where applicable. For insurance, the ORSA / ICP analogues land in the mapped principles. If the overlay is loaded but the assessment has no overlay-specific content, the loader did not run; rerun with the overlay reference in scope.
