# Control test plan

**Test ID**: [stable ID per firm naming convention]
**Control ID**: [firm control register ID]
**Obligation IDs**: [firm obligation register IDs; one or more]
**Engagement ID**: [pointer to scope record, or "none — scope not formalised separately"]
**Prior-cycle test ID**: [where applicable]
**Trigger**: [annual-program-coverage | regulatory-change | examiner-request | prior-finding-followup | control-owner-request | incident-driven | other]
**Period under test**: [start date — end date]
**Business unit**: [name; role-level, not individual-level]
**Jurisdiction**: [primary; list secondary if multi-jurisdiction]
**Source posture**: [public-only | public-plus-firm-policy | public-plus-firm-policy-plus-evidence | connector-aware]
**Preparer (role)**: [e.g., compliance-testing analyst]
**Preparer date**: [ISO date]
**Reviewer (role)**: [separate role from preparer; e.g., compliance-testing manager]
**Reviewer pre-fieldwork sign-off date**: [filled at sign-off; precedes evidence-pull date]
**Confidence label**: [high | medium | low | unknown]

## Scope statement

Two to three sentences. What is in scope, what is out of scope, what triggered the cycle, and what changed since the prior cycle.

## Test objective

- **Read**: [design-effectiveness-only | operating-effectiveness-only | design-and-operating-combined].
- **Statement**: single statement of what the test concludes on. Not the procedure list; the read the cycle is set up to deliver.

## Source criteria

| Criterion ID | Source | Section | Excerpt or paraphrase | Why this applies |
|---|---|---|---|---|
| C1 | [regulator + instrument] | [section reference; use [verify section] if unknown] | [verbatim or tight paraphrase] | [why this criterion applies to the population] |

Cite by file path into `references/source-anchors.md` and the loaded sector and cross-cutting overlays. Do not restate full excerpts in the body.

## Population and sampling reference

- **Description**: [originations during period | accounts open during period | transactions executed | packets due in period | other].
- **Source of truth**: [system or report from which the extract is taken].
- **Period boundaries**: [open during period, action-taken during period, executed during period].
- **Stratification**: [planned stratification — privilege tier, action-taken type, customer risk tier].
- **Extract integrity check planned**: [what the workpaper will reconcile the extract against for completeness].
- **Sampling memo reference**: [sampling_id from `control-sampling`, or "inline below" for small tests].

If sampling is inline (small test):
- **Method**: [random | systematic | stratified | judgmental | 100-percent | haphazard].
- **Size**: [n].
- **Size rationale**: [tie to risk-based prioritization].
- **Tolerable deviation rate**: [n%; zero-tolerable subsets named explicitly].

## Walkthrough plan

- **Scope**: [full walkthrough | refresher walkthrough on system changes only — prior workpaper ID referenced | skipped — prior workpaper ID and rationale].
- **Roles to interview**: [role names, not individual names].
- **Processes to observe**: [named process steps].
- **Screens or systems to inspect**: [system-of-record names; configuration screens; report runs].
- **Evidence to capture during walkthrough**: [screenshots, attestation form templates, system-configuration exports, training records].

## Design-effectiveness procedures

| Procedure ID | Description | Expected evidence | Expected observable condition | Criteria addressed |
|---|---|---|---|---|
| DP1 | | [configuration screen / policy excerpt / form template / training record] | [what the preparer expects to observe to support a met or not-met read] | [criterion IDs] |

Design procedures are walkthrough-and-inspection methodology, not sample-based reperformance.

## Operating-effectiveness procedures

| Procedure ID | Description | Methodology | Expected evidence per sample | Expected observable condition | Criteria addressed |
|---|---|---|---|---|---|
| OP1 | | [reperformance | observation | inquiry | confirmation | inspection | recalculation | analytical-procedure] | [case file / system extract / attestation packet / reconciliation] | [what the preparer expects per sample to support success or exception] | [criterion IDs] |

Operating procedures are typically sample-based; the methodology per procedure is named so the workpaper later reads against the planned methodology.

## Evidence-request reference

- **Evidence request list**: [evidence_request_list_id from `evidence-request-builder`, or "inline below" for small tests].

If inline (small test):

| Request ID | Description | Owner role | Due date |
|---|---|---|---|
| ER1 | | | |

## Clear and fail criteria

- **Success criterion**: observable condition that supports an effective read. Calibrated in second-line vocabulary (control effectiveness, not legal compliance).
- **Fail criterion**: observable condition that supports a not-effective read.
- **Tolerable deviation rate**: [n% from sampling memo, or inline value]. Zero-tolerable populations (privileged access, sanctions screening, customer-funds segregation) named explicitly with severity-driven aggregation.

## Limitations and assumptions

- Period coverage: [the plan concludes only on the period named above; no coverage of {prior periods, future periods}].
- Scope exclusions: [a separate control, a separate process, a different period segment, a different population stratum].
- Reliance on prior testing: [none | prior workpaper ID; rationale; reviewer pre-sign-off reference].
- Dependencies on other in-flight reviews: [related test IDs or engagement references].
- Assumptions: [facts treated as fixed and what would invalidate them].

## Downstream consumers

- `workpaper-drafter` — for fieldwork documentation and the workpaper artifact.
- `qa-workpaper` — for review of the completed workpaper.
- `exception-analysis` — for classification of exceptions surfaced in fieldwork.
- `issue-writeup` — for any issues elevated from the cycle.

## Reviewer questions (for pre-fieldwork sign-off)

- [Question. Names the decision the reviewer is being asked to make before sign-off.]

A question the preparer answers in the plan is not a reviewer question. Cluster questions for the audience that decides them.

## Sign-off

| Role | Name (filled at sign-off; role appears here in the template) | Signature | Date |
|---|---|---|---|
| Preparer | | | |
| Reviewer | | | (precedes evidence-pull date) |

Preparer and reviewer must be different roles. Pre-fieldwork sign-off is a hard gate; evidence pulls happen after sign-off, not before.

## Source trace

| Claim | Source | Section | Date | URL or file ref |
|---|---|---|---|---|
| | | | | |

Cite `references/source-anchors.md` and the loaded overlays for canonical citations. Use `[verify section]` if the section reference is unknown; do not invent.

---

*Plan depth scales to control complexity, population size, and prior-cycle history.* A familiar low-volume control with a stable prior cycle reads short. A new control area, a regulatory-change-driven cycle, or a control with a recent finding reads longer with a heavier walkthrough plan and richer review and fail criteria.

*Audience shapes the plan.* A new pod reads heavier on procedure detail and methodology restatement. An experienced pod reads tighter with the procedure list as a contract rather than a tutorial.
