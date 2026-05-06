---
name: control-sampling
description: |
  Designs the sample for a control test before fieldwork starts. Defines the testable population, picks a sampling method (statistical or judgmental), sizes the sample, sets a tolerable deviation rate, names the selection technique, and documents the rationale a reviewer can defend in front of an examiner. Output is a sampling memo that drops into the test plan or workpaper as a referenceable artifact.

  Best for:
  - A second-line testing pod or internal-audit team is scoping a control test and needs a defensible sample method, size, and rationale before pulling evidence.
  - A reviewer is challenging a first-line control owner's self-attested testing because the sampling rationale is missing or thin and the sample needs to be redesigned.
  - A walkthrough has confirmed control design and the next step is sizing operating-effectiveness testing across a defined population.
  - A prior-cycle workpaper failed QA on sample-design grounds and the redraft starts at the sampling memo.

  Not the right tool when:
  - The control or obligation has not been mapped yet. Run `risk-compliance-core/skills/control-matrix` and come back with a control ID.
  - The full test plan has not been scoped. Run `test-plan-builder`; this skill produces the sampling section that test-plan-builder consumes by reference.
  - The evidence ask itself is the work. Run `evidence-request-builder`; sampling sets which items the request targets, but the request artifact is separate.
  - Exceptions have already been identified and need classification. Run `exception-analysis`.
  - The completed workpaper is being written. Run `workpaper-drafter`; this skill stops at the sample drawn.

  Anchored to: external-auditing standards on sampling and on responding to assessed risk; internal-audit professional standards on planning and documentation; bank-supervisory testing-program guidance and the federal financial regulator IT examination handbook; bank consumer-compliance management examination procedures; and the COSO internal-control framework. Citations and excerpts live in `references/source-anchors.md`.
argument-hint: "[control ID, population description, prior testing, or risk-based stratification factors]"
---

# Control sampling

A control test concludes on a population. The sampling memo is what tells a reviewer (and later an examiner) what population was tested, why this sample method fits the test objective, how big the sample is, why that size, how items were selected, what deviation rate the reviewer will tolerate before calling the control not-effective, and what the sample cannot conclude on. Without that memo, the workpaper conclusion sits on an unsupported population and a defensible challenge collapses it.

This skill produces the memo before fieldwork. It does not pull evidence, run procedures, or classify exceptions. It produces the markdown artifact in `templates/default-output.md` shape and a structured record conforming to `schemas/sampling.schema.json` for downstream consumers (`test-plan-builder` references the sampling memo by ID; `workpaper-drafter` consumes the population definition and tolerable rate; `qa-workpaper` reads the rationale when it tests the workpaper for sufficiency). The skill stops at sample drawn and reviewer sign-off on the memo; the test itself runs downstream.

## Ask first

Before drafting, get plain answers. Most engagements answer them in the test plan or the walkthrough notes; if not, default and flag.

- **What is the test objective.** Design effectiveness, operating effectiveness, or both. Sample design follows the objective. A walkthrough-only test does not get a population sample; an operating-effectiveness test does. A combined test may need two samples (a small judgmental design-effectiveness sample plus a statistical operating-effectiveness sample).
- **What is the testable population, not the source system.** The population is the items you could draw a sample from to answer the test question, not the database that holds them. Account-opening packets opened in the period, error-resolution case files closed in the period, recertification packets generated in the period, alert dispositions completed in the period. State the population in items, not in tables.
- **What does the source of truth look like and how do you know the population is complete.** Name the system, the report or query, the period boundaries, and the reconciliation that supports the completeness assertion. A population without a reconciliation to a control total is unsupported.
- **What risk concentrations matter.** If the test sits over a population with known higher-risk segments (privileged access in an IAM population, high-dollar transactions in a payments population, high-risk customers in a CDD population, sponsor-bank end-customers in a deposit-program population), stratify. The stratification rationale is part of the memo, not implicit.
- **What method does the test objective support.** Statistical attribute sampling sizes against confidence and tolerable rate; monetary-unit sampling targets dollar coverage; judgmental sampling rests on a documented basis; haphazard is rarely defensible and should be flagged when proposed; full-population testing is appropriate for small populations or zero-tolerable scopes. The method choice is part of the memo, with the reasoning.
- **What is the tolerable deviation rate, and where does it come from.** Firm methodology, professional standard, regulator expectation, or a population-specific zero-tolerable convention (privileged access, sanctions screening, customer-funds segregation). The criterion source is named; the number alone does not pass.

When `engagement-scope` is supplied, consume it: `institution.type` and `institution.primary_regulators` set the citation focus and tone, `sector_overlay_set` selects which `references/sector-overlays/<sector>.md` loads, `cross_cutting_overlay_set` selects the `references/cross-cutting/<topic>.md` files. When it is not supplied, draft against what is on file (the test plan and the control description usually carry enough), default to the testing program's standing posture, and note in the memo that scope was not formalised separately.

## How the sampling memo gets built

The memo has the same spine across control types. A senior preparer fills it in roughly in the order the conversation runs, not in lockstep.

The header pins the memo to its test cycle: sampling ID, test ID (foreign key into `test-plan-builder` output), control ID, obligation ID, period under test, business unit, jurisdiction, source posture, preparer role and date, reviewer role and date placeholder. Reviewer separation is structural, not advisory: the same role cannot both prepare and review the memo. The header is the audit trail when the file is reopened later.

Scope and source posture restates the test plan's scope in two or three sentences and names the source posture the sampling will operate under (public-only, public-plus-firm-policy, public-plus-firm-policy-plus-evidence, connector-aware). The pointer to the test plan goes here. If the sampling memo is being drafted before the test plan is fixed (which happens when sampling drives the procedure design), that gets named explicitly so a reviewer can sequence the artifacts.

Population definition is the load-bearing section. It carries the population in items (not in source tables), the source of truth (system, report, query identifier with run date), the period boundaries, the completeness basis (reconciliation to control total, dual-extract comparison, system-of-record cut-off attestation), the exclusions with rationale (out-of-period items, items belonging to a different test, items the sample explicitly cannot reach), and the population size. A population without a completeness basis is a methodology defect; the memo stops and the reviewer is asked to authorise the gap before the sample is drawn.

Risk-based stratification names the stratification factors (transaction value, customer risk tier, product, channel, geography, privilege tier, action-taken type, recertifier role), the strata sizes, and the rationale tying stratification to the risk assessment. Stratification is not always required; when the population is uniform on the dimensions the test cares about, the memo says so explicitly so a reviewer can challenge that read. Over-stratifying a small population produces strata too thin to draw from; the memo addresses that trade-off where it matters.

Sample method names the method (statistical attribute sampling, monetary-unit sampling, judgmental, haphazard, full-population) and explains why this method fits the test objective. The reasoning is concrete: statistical attribute for high-volume operating-effectiveness over a uniform population; monetary-unit for dollar-coverage tests; judgmental for low-volume or design-focused tests; full-population for small populations or zero-tolerable scopes. Haphazard is flagged for reviewer challenge; in practice it is hard to defend and the memo recommends a documented alternative.

Sample size rationale carries the inputs. For statistical samples: confidence level, tolerable deviation rate, expected deviation rate, and the resulting size, with a reference to the method (firm methodology, AICPA AU-C 530-derived tables, or a named statistical package). For judgmental samples: the qualitative basis and the floor or ceiling reference (firm methodology floor, regulator-handbook appendix conventions, prior-cycle benchmark). The size alone is not the rationale; the inputs that produced the size are the rationale.

Selection method names the technique and the parameters that make the selection reproducible. For random selection: the random-number generator, the seed, and the sort key on the population list. For monetary-unit sampling: the interval and the starting point. For judgmental: the criteria the preparer applied (highest-dollar, highest-risk, longest-aged, most-recent). The reproducibility note matters for QA; a sample a reviewer cannot rebuild from the memo is a methodology defect.

Tolerable deviation rate is a number plus its criterion source. Three percent because firm methodology says three percent; zero percent because privileged access policy says zero; five percent because the AICPA-derived methodology table at this confidence level produces five for this population. The number alone does not pass; the criterion source is the methodology anchor. Population-specific zero-tolerable conventions get explicit treatment because they change how the conclusion will read downstream (severity-driven, not rate-driven).

Sample drawn names the sample IDs (or a pointer to the sample list when the sample is large), the draw date, the drawer role, and the control-total reconciliation between the sample-draw output and the population. A sample that cannot be reconciled to the population is a methodology defect; the memo names the discrepancy and stops for reviewer authorisation.

Limitations and assumptions is the protection paragraph. What the sample cannot conclude on (a different population segment, items outside the period, items excluded by design), the period coverage gaps, the completeness caveats. A memo without a limitations section gives a reviewer nothing to push back on; absence is itself a defect.

Reviewer questions captures everything that could not be resolved in drafting and that the preparer wants the named reviewer to consider before sign-off. A reviewer question that the preparer answers themselves is not a reviewer question. Cluster questions for the audience that decides them; testing-management questions and internal-audit questions go in the same list when both apply.

The sign-off block carries preparer and reviewer (separate roles). Source trace and confidence label close the file: every material claim cites a source with a section reference, and the confidence label (high / medium / low / unknown) reflects evidence sufficiency for the population assertion, the criterion source for the tolerable rate, and the source posture under which the memo was produced.

## What's load-bearing and what flexes

Load-bearing across every sampling memo: the population is defined in items the sample can draw from, with a named completeness basis. The stratification rationale is documented when stratification is used, and the no-stratification choice is documented when it is not. The sample method name is paired with reasoning that ties to the test objective. Sample size carries the inputs that produced it (confidence and tolerable rate for statistical; documented basis with floor or ceiling reference for judgmental). The tolerable deviation rate carries its criterion source. The selection method is reproducible. The sample drawn reconciles to the population. Limitations name what the sample cannot conclude on. Preparer and reviewer are different roles. Citations carry section references or `[verify section]` markers; URL alone does not pass. No named institutions in the memo unless they are public defendants in a finalised enforcement action.

Flexes to the engagement: memo depth scales to control complexity, population size, and the regulator the test was designed for. A small judgmental sample over a low-volume control reads short; a stratified statistical sample over a high-volume consumer-facing control reads longer with the stratification rationale and the population-completeness basis carried in detail. Sector overlay loading follows engagement-scope plus the rule that the regulator the test was designed for drives the sector overlay. Cross-cutting overlay loading: cyber overlay is default-on for any control test touching IAM, vulnerability management, or covered-entity-cybersecurity-mandated areas, because population definition and stratification get unusual (tickets, alerts, identities, packets); conduct overlay is default-on for consumer-facing tests where stratification by customer segment matters separately from the technical control conclusion. Privacy overlay loads when the population touches consumer financial information under safeguards regimes. Audience drives shape: a memo for in-cycle QA reads operationally; a memo drafted with an upcoming exam in mind reads heavier on the criterion sources for the tolerable rate and the population-completeness basis.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/banking.md`, `insurance.md`, `capital-markets.md`, `payments-fintech.md` — sector-specific population, stratification, and tolerable-rate conventions loaded per engagement-scope.
- `references/cross-cutting/cyber.md`, `conduct.md`, `privacy.md` — cross-cutting flavour; cyber default-on for IAM and covered-entity-cybersecurity controls, conduct default-on for consumer-facing tests, privacy when safeguards regimes apply.
- `references/firm-overlay.md` — firm-installed methodology, sample-size tables, tolerable-rate floors, and template variants beyond the regulatory baseline; consumed when present.
- `templates/default-output.md` — sampling-memo template.
- `schemas/sampling.schema.json` — structured-output contract for downstream consumption.
- `examples/` — overdraft-fee-disclosure compliance-testing sample at a regional bank; quarterly logical-access-recertification sample for a critical core-banking application.
- `TROUBLESHOOTING.md` — recurring pitfalls (population defined as the source system, no completeness reconciliation, judgmental basis missing, tolerable rate without a criterion source, sample treated as projecting to a population it cannot project to).

The plugin-level shared references (`references/source-map.md`, `references/policy-control-library.md`, `references/review-gates.md`) sit at the plugin root and are consulted alongside the skill-level files.

## Output

The skill emits a sampling memo in `templates/default-output.md` shape and a structured record conforming to `schemas/sampling.schema.json`. Downstream consumers: `test-plan-builder` references the memo by `sampling_id`; `workpaper-drafter` consumes the population definition, the tolerable deviation rate, and the sample IDs; `qa-workpaper` reads the rationale when it tests the workpaper for sufficiency; `exception-analysis` reads the sample list and the tolerable rate when it classifies observed deviations. The schema is the cross-skill contract; additive changes only. Add fields, do not rename or repurpose them. A breaking change is a versioned migration with the downstream skills told in advance.
