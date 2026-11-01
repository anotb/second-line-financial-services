# Sampling memo

**Sampling ID**: [stable ID per firm naming convention]
**Test ID**: [foreign key into `test-plan-builder` output, or "drafted ahead of test plan — pending"]
**Control ID**: [firm control register ID]
**Obligation ID**: [firm obligation register ID; may be multiple]
**Period under test**: [start date — end date]
**Business unit**: [name; role-level, not individual-level]
**Jurisdiction**: [primary; list secondary if test scope is multi-jurisdiction]
**Engagement ID**: [pointer to scope record, or "none — scope not formalised separately from test plan"]
**Source posture**: [public-only | public-plus-firm-policy | public-plus-firm-policy-plus-evidence | connector-aware]
**Preparer (role)**: [e.g., compliance-testing analyst]
**Preparer date**: [ISO date]
**Reviewer (role)**: [separate role from preparer; e.g., compliance-testing manager]
**Reviewer date**: [filled at sign-off]
**Confidence label**: [high | medium | low | unknown]

## Scope and source posture

- Scope statement, two to three sentences. What population, what timeframe, what test objective.
- Test plan reference: [test plan ID and date, or "this memo precedes the test plan"].
- Test objective: [design-effectiveness | operating-effectiveness | combined].

## Population definition

- **Population (in items)**: [account-opening packets opened in period | error-resolution case files closed in period | recertification packets generated in period | etc.]. State the population in items the sample can draw from, not in source tables.
- **Source of truth**: [system / report / query identifier with run date and run-by role].
- **Period boundaries**: [start date — end date with cut-off treatment].
- **Completeness basis**: [reconciliation to control total | dual-extract comparison | system-of-record cut-off attestation; name the reconciliation result].
- **Exclusions**:

| Criterion | Rationale |
|---|---|
| | |

- **Population size**: [n].

## Risk-based stratification

- **Stratification factors**: [transaction value | customer risk tier | product | channel | geography | privilege tier | action-taken type | recertifier role | none — population uniform on dimensions the test cares about].

| Factor | Bucket | Bucket size |
|---|---|---|
| | | |

- **Rationale**: [tie stratification to the risk assessment; concentrations of risk that justify oversampling; thinness considerations for small strata].

## Sample method

- **Method**: [statistical-attribute | monetary-unit | judgmental | haphazard | full-population].
- **Why this method fits the test objective**: [two to three sentences tying method choice to objective, population behaviour, and source posture]. If `haphazard` is proposed, flag for reviewer challenge and recommend a documented alternative.

## Sample size rationale

For statistical samples:

| Input | Value | Source |
|---|---|---|
| Confidence level | [e.g., 95%] | [firm methodology / professional standard] |
| Tolerable deviation rate | [e.g., 5%] | [see Tolerable deviation rate section] |
| Expected deviation rate | [e.g., 1%] | [prior cycle / firm methodology default] |
| Resulting sample size | [n] | [method or table reference] |

For judgmental samples:

- **Qualitative basis**: [factors and weights; named target items by category].
- **Floor or ceiling reference**: [firm methodology floor | regulator-handbook appendix conventions | prior-cycle benchmark].
- **Resulting sample size**: [n].

For full-population testing:

- **Justification**: [population size; zero-tolerable scope; all items reachable in available time].

## Selection method

- **Technique**: [PRNG with documented seed | MUS interval | judgmental criteria | haphazard].
- **Reproducibility note**: [the random-number generator used and the seed value | the MUS interval and starting point | the judgmental criteria the preparer applied].
- **Sort key on the population list**: [field used to order the population before drawing].

## Tolerable deviation rate

- **Threshold**: [n% or "0% for [segment]"].
- **Criterion source**: [firm methodology | professional standard table | regulator expectation | population-specific zero-tolerable convention].
- **Procedure-level breakouts** (where applicable): [data-point-level versus record-level rates; segment-specific rates].

## Sample drawn

- **Sample IDs**: [list, or pointer to sample list when large].
- **Draw date**: [ISO date].
- **Drawer (role)**: [role, separate from sample-evaluator role].
- **Control-total reconciliation**: [sample-draw output reconciled to population; named result].

## Limitations and assumptions

- Population coverage: [the sample addresses only the population defined above; named exclusions; segment limitations].
- Period coverage gaps: [items outside the period; items in the period not addressed; cut-off treatment limitations].
- Completeness caveats: [reliance on system-of-record extract; reliance on management-prepared schedule; dependencies on upstream feeds].
- Projection limitation: [where projection from sample to population is appropriate, and where it is not].

## Reviewer questions

- [Question. Names the decision it supports.]

A question the preparer answers in the memo is not a reviewer question. Cluster questions for the audience that decides them.

## Sign-off

| Role | Name (filled at sign-off; role appears here in the template) | Signature | Date |
|---|---|---|---|
| Preparer | | | |
| Reviewer | | | |

Preparer and reviewer must be different roles. Sample drawer is a third role where the firm's policy requires draw-and-evaluate separation; otherwise the preparer can draw and the reviewer signs the draw.

## Source trace

| Claim | Source | Section | Date | URL or file ref |
|---|---|---|---|---|
| | | | | |

Cite `references/source-anchors.md` and the loaded overlays for canonical citations. Use `[verify section]` if the section reference is unknown; do not invent.

---

*Memo depth scales to control complexity, population size, and the regulator the test was designed for.* A small judgmental sample over a low-volume control reads short. A stratified statistical sample over a high-volume consumer-facing control reads longer with the stratification rationale and the population-completeness basis carried in detail.

*Audience shapes the memo.* In-cycle QA reads operationally. Exam-facing reads heavier on the criterion sources for the tolerable rate and the population-completeness basis. Internal-audit reliance-facing reads heavier on the methodology anchor and the reviewer-separation evidence.
