# Testing workpaper

**Workpaper ID**: [stable ID per firm naming convention]
**Test ID**: [foreign key into `test-plan-builder` output]
**Control ID**: [firm control register ID]
**Obligation ID**: [firm obligation register ID; may be multiple]
**Period under test**: [start date — end date]
**Business unit**: [name; role-level, not individual-level]
**Jurisdiction**: [primary; list secondary if test scope is multi-jurisdiction]
**Engagement ID**: [pointer to scope record, or "none — scope not formalised separately from test plan"]
**Preparer (role)**: [e.g., compliance-testing analyst]
**Preparer date**: [ISO date]
**Reviewer (role)**: [separate role from preparer; e.g., compliance-testing manager]
**Reviewer date**: [filled at sign-off]
**QA reviewer (role)**: [placeholder; filled by `qa-workpaper`]
**QA date**: [placeholder]
**Confidence label**: [high | medium | low | unknown]

## Scope and source posture

- Scope statement, two to three sentences. What population, what timeframe, what is in and out of scope.
- Source posture: [public-only | public-plus-firm-policy | public-plus-firm-policy-plus-evidence | connector-aware].
- Test plan reference: [test plan ID and date].
- Scope changes from the test plan: [none | named change with pre-fieldwork sign-off reference].

## Source criteria

| Criterion ID | Source | Section | Excerpt or paraphrase | Notes |
|---|---|---|---|---|
| C1 | [regulator + instrument] | [section] | [verbatim or tight paraphrase] | [why this criterion applies to the population] |

Cite by file path into `references/source-anchors.md` and the loaded sector and cross-cutting overlays. Do not restate full excerpts in the body.

## Walkthrough summary

- Walkthrough date: [ISO date].
- Roles interviewed: [role names, not individual names].
- Processes observed: [named process steps].
- Screens or systems inspected: [system-of-record names; configuration screens; report runs].
- Walkthrough conclusion (design-effectiveness signal): [design appears effective | design gap surfaced — see Conclusion | design observation noted but not conclusive — supplemental procedures added].

## Evidence inspected

| Evidence ID | Description | System of record | Reliance classification | Request ID | Reliance test note |
|---|---|---|---|---|---|
| E1 | | | system-of-record-extract / system-generated-report / management-prepared-schedule / vendor-supplied / third-party-assurance | [from `evidence-request-builder`] | [completeness/accuracy check; CUEC posture if SOC reliance; prior workpaper ID if cross-period reliance] |

## Procedures performed

| Procedure ID | Description (per test plan) | Execution notes (what the preparer actually did) | Procedure-level conclusion |
|---|---|---|---|
| P1 | | | [met / partially met / not met / not applicable in fieldwork] |

Note: procedures added or substituted in fieldwork are flagged here with the pre-fieldwork reviewer sign-off reference. Silent additions or substitutions are a QA finding.

## Sample-level results

| Sample ID | Evidence reviewed (IDs) | P1 outcome | P2 outcome | ... | Exception flag | Exception ID |
|---|---|---|---|---|---|---|
| S1 | E1, E3 | pass | pass | | no | |
| S2 | E2, E4 | pass | exception | | yes | X1 |

Exceptions are surfaced here, classified in the exception register from `exception-analysis`, not classified here.

## Exceptions identified

- Exception register: [exception_register_id from `exception-analysis`].
- Summary by classification: [design: n; operating: n; documentation: n; data-integrity: n; not-an-exception-on-review: n].
- Summary by severity: [critical: n; high: n; medium: n; low: n].
- Repeat-issue posture: [n exceptions reference prior issues; cite issue IDs].
- Tolerable deviation rate (from test plan): [n%].
- Observed deviation rate: [n% calculated against the sample size, broken out by procedure where the test plan called for procedure-level tolerable rates].

## Aggregation and projection

- Anomaly versus systemic call: [anomaly | systemic | mixed — explain].
- Concentration commentary: [exceptions concentrated in {segment, region, process step, time period} — or distributed].
- Sample-design implication: [sample-size adequate | sample-size implies need for expanded testing | population stratification did not match observed behaviour — flag].
- Projection commentary: [appropriate to project to population at the procedure level | not appropriate — explain — e.g., 100% testing of a small population, judgmental sample].

## Conclusion

- **Design effectiveness**: [effective | partially effective | not effective | inconclusive]. Rationale, two to three sentences. Tie to walkthrough and any design exceptions.
- **Operating effectiveness**: [effective | partially effective | not effective | inconclusive]. Rationale, two to three sentences. Tie to sample-level results and aggregation.
- **Combined conclusion** (if test plan calls for it): [effective | partially effective | not effective | inconclusive].

Conclusion language stays in second-line vocabulary: "the control did not operate as designed for the [segment] population during the period," not "the firm violated [Reg X]." Legal-violation language is for legal counsel and regulator-led determinations, not for the workpaper.

## Issues elevated

| Issue handoff ID | Severity | Source exception IDs | Brief description (one line) |
|---|---|---|---|
| I1 | | | |

The handoff package (criterion, condition, cause, effect, recommendation seed) is built from the exception register's classification fields and is the bridge into `risk-compliance-core/skills/issue-writeup`. The workpaper does not draft the issue.

## Reviewer questions

- [Question. Names the decision it supports.]

A question the preparer answers in the workpaper is not a reviewer question. Cluster questions for the audience that decides them.

## Limitations and reliance

- Period coverage: [the workpaper concludes only on the period named above; no coverage of {prior periods, future periods}].
- Scope exclusions: [from the test plan; restate].
- Reliance on prior testing: [none | prior workpaper ID; rationale; reviewer sign-off on reliance].
- Reliance on management-prepared evidence: [list with reliance test notes].
- Reliance on vendor SOC 1 / SOC 2 / third-party assurance: [list with CUEC posture and any unaddressed CUECs].
- Other limitations: [data limitations; system access limitations; population not fully enumerated].

## Sign-off

| Role | Name (filled at sign-off; role appears here in the template) | Signature | Date |
|---|---|---|---|
| Preparer | | | |
| Reviewer | | | |
| QA reviewer | (filled by `qa-workpaper`) | | |

Preparer and reviewer must be different roles. The QA placeholder is filled downstream.

## Source trace

| Claim | Source | Section | Date | URL or file ref |
|---|---|---|---|---|
| | | | | |

Cite `references/source-anchors.md` and the loaded overlays for canonical citations. Use `[verify section]` if the section reference is unknown; do not invent.

---

*Workpaper depth scales to control complexity, sample size, and exception volume.* A clean, low-volume control test with no exceptions reads short. A high-volume test with classified exceptions across multiple severities reads longer with the exception summary clustered for the audience that decides next steps.

*Audience shapes the workpaper.* QA-facing reads operationally. Exam-facing reads heavier on criteria and limitations. Internal-audit reliance-facing reads heavier on the evidence reliance and reviewer-separation evidence.
