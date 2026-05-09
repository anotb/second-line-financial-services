# Exception register

**Exception register ID**: [stable ID per firm naming convention; foreign key consumed by `workpaper-drafter` and source of `source_exception_id` handoffs into `risk-compliance-core/skills/issue-writeup`]
**Test ID**: [foreign key into `test-plan-builder` output]
**Workpaper ID**: [foreign key into `workpaper-drafter` output]
**Control ID**: [firm control register ID]
**Obligation ID**: [firm obligation register ID; may be multiple]
**Period under test**: [start date — end date]
**Business unit**: [name; role-level, not individual-level]
**Jurisdiction**: [primary; list secondary if multi-jurisdiction]
**Engagement ID**: [pointer to scope record, or "none — scope not formalised separately from test plan"]
**Source posture**: [public-only | public-plus-firm-policy | public-plus-firm-policy-plus-evidence | connector-aware]
**Preparer (role)**: [e.g., compliance-testing analyst]
**Preparer date**: [ISO date]
**Reviewer (role)**: [separate role from preparer; e.g., compliance-testing manager]
**Reviewer date**: [filled at sign-off]
**Confidence label**: [high | medium | low | unknown]

## Scope and source posture

- Scope statement, two to three sentences. Population, timeframe, what is in and out of scope.
- Workpaper reference: [workpaper ID and date].
- Scope changes carried forward from the workpaper: [none | named change with reference].

## Exception register

For each deviation, populate one row. Numbering is stable across the engagement.

### Exception X1

- **Sample ID**: [from workpaper sample-level results]
- **Population reference**: [stratum or segment label if stratified]
- **Criterion**: [rule, principle, policy section, or methodology, with section reference; cite by file path into `references/source-anchors.md` or loaded overlays]
- **Condition**: [dated, scoped, observable state — what the test actually saw]
- **Classification**: [control-failure | design-gap | evidence-gap | scope-disagreement | data-integrity | anomaly]
- **Severity**: [low | medium | high | critical]
- **Severity rationale**: [frequency, customer impact, regulatory exposure, materiality against firm thresholds, compensating controls]
- **Root-cause hypothesis**:
  - Category: [people | process | technology | data | governance]
  - Description: [specific control attribute that failed; "root cause analysis pending" if genuinely unknown, with an open action]
- **Repeat-issue flag**: [yes | no]
- **Prior issue ID**: [if repeat-issue flag is yes]
- **Disposition**: [elevated-to-issue | closed-at-exception | re-test-required | expanded-sample-required]
- **Disposition rationale**: [why this disposition; for closed-at-exception, the supplemental evidence reviewed; for re-test or expanded-sample, the criteria for what closes it]
- **Issue handoff package** (populate when disposition is `elevated-to-issue`):
  - Criterion: [carry-forward, with section reference]
  - Condition: [carry-forward, dated and scoped]
  - Cause: [from root-cause hypothesis, named control attribute]
  - Effect: [impact with unit and time window — financial, customer, regulatory, operational, reputational]
  - Recommendation seed: [declarative remediation direction — what the owner role would do; the issue writer refines]
  - Suggested rollup grouping: [issue rollup label if this exception groups with others into a single issue]

(Repeat for each exception. Numbering: X1, X2, X3 ...)

## Aggregation and projection

- Observed deviation rate: [X / N = Y%]
- Tolerable deviation rate (from test plan): [Z%]
- Anomaly versus systemic posture: [systemic | anomaly with positive evidence — name the evidence]
- Concentration commentary: [segment, channel, region, process step where deviations cluster]
- Sample-design implication: [none | the deviation rate suggests the population stratification was incorrect — see Reviewer questions]
- Stratum-level breakdown (if stratified):

| Stratum | Sample size | Deviations observed | Deviation rate | Tolerable | Notes |
|---|---|---|---|---|---|
| [label] | | | | | |

## Disposition summary

| Classification | Severity | Count | Disposition mix |
|---|---|---|---|
| control-failure | critical | | elevated: ; closed: ; re-test: ; expanded-sample: |
| control-failure | high | | |
| control-failure | medium | | |
| control-failure | low | | |
| design-gap | (per severity) | | |
| evidence-gap | (per severity) | | |
| scope-disagreement | (per severity) | | |
| data-integrity | (per severity) | | |
| anomaly | (per severity) | | |

## Handoff to issue write-up

For each exception with disposition `elevated-to-issue`, the handoff package above is the input `risk-compliance-core/skills/issue-writeup` consumes via `source_exception_id`. The writer does not re-discover criterion, condition, cause, effect, or recommendation seed; those are populated here. Where multiple exceptions roll up into a single issue (same root cause, different sample items), name the rollup grouping in the handoff.

| Exception ID | Disposition | Suggested issue rollup | Severity | Recommendation seed (one line) |
|---|---|---|---|---|
| X1 | elevated-to-issue | [issue rollup label] | high | |
| X2 | closed-at-exception | n/a | medium | |

## Reviewer questions

- [Cluster questions for the audience that decides them. Severity calibration, root-cause hypothesis confidence, scope-disagreement resolution, repeat-issue handling, sample-design implications. A reviewer question the preparer answers themselves is not a reviewer question.]

## Limitations and reliance

- What this register does not classify (separate test, separate population segment, different period).
- Reliance on prior testing or vendor SOC reliance carried in from the workpaper.
- Source posture limits on what the body can carry.

## Source trace and confidence label

- Source trace: every classification and severity rationale cites the criterion and the firm-overlay or source-anchor file path. `[evidence needed]` flags route to the engagement issue log.
- Confidence label: [high | medium | low | unknown] — reflects evidence sufficiency, sample size, source posture, reliance on second-hand evidence.

---

**Sign-off**

- Preparer: [role, date]
- Reviewer: [separate role, date]
- Human review required: yes (severity assignment and disposition always carry human review).
