# Troubleshooting — control-sampling

Recurring pitfalls. Read before drafting the sampling memo and again before reviewer sign-off.

## Population definition discipline

### Defining the population as the source system

The population is the items the sample can draw from to answer the test question, not the database that holds those items. "The LAR data warehouse" is a source system; "LAR records reported during the calendar year" is a population. "The IAM platform" is a source system; "recertification packets generated for entitled users in the most recent quarter" is a population. The schema enforces the discipline: `population.description` is the items, `population.source_of_truth` is the system. Confusing them produces sample-design defects that surface in QA.

### Skipping the completeness basis

A population pull without a reconciliation to a control total or an independent extract sits unsupported. Every sample-level conclusion downstream rests on the completeness assertion. Name the reconciliation: extract row count to system-of-record count within tolerance; dual-extract comparison; system-of-record cut-off attestation by the data owner. The schema enforces it: `population.completeness_basis` is required.

### Treating cut-off as implicit

Period boundaries carry cut-off treatment. Are items in the period the items recorded with effective dates in the period, items processed in the period, or items reaching final state in the period? The three populations differ. The memo names the cut-off treatment so a reviewer can challenge it.

### Carrying exclusions without rationale

Excluding items from the population without naming the rationale buries the methodology call. Each exclusion carries a criterion (out-of-period; belongs to a different test; not reachable through available evidence) and a one-line rationale. The schema requires both fields on every exclusion.

## Stratification discipline

### Stratifying for stratification's sake

Stratification is a risk-based call. When the population is uniform on the dimensions the test cares about, the memo names the no-stratification choice and explains why. Stratifying a uniform population produces strata too thin to draw from and weakens the sample.

### Skipping stratification on a heterogeneous population

A population with known higher-risk segments (privileged versus standard access; high-dollar versus low-dollar transactions; high-risk versus low-risk customers; sponsor-bank end-customers within a deposit-program population) calls for stratification with oversampling of the higher-risk segment. Skipping stratification here treats the population as uniform and dilutes the sample's ability to surface concentrated risk.

### Stratifying without sizing the strata

Listing the factors without naming the bucket sizes leaves the actual sample design implicit. The schema requires `bucket_size` on each stratification entry.

## Sample method discipline

### Picking statistical for a small population

Statistical attribute sampling gives confident projection over a population large enough to support it. A population under a few hundred items typically does not produce a statistically efficient sample; full-population testing or a judgmental sample with a documented basis is more honest. The memo names the method and the reasoning; defaulting to statistical because "statistical sounds rigorous" produces oversampling and a misleading confidence claim.

### Picking judgmental without writing the basis

"Risk-based" alone is not a basis. The basis names the factors, the weights, and the floor or ceiling reference (firm methodology floor; regulator-handbook appendix conventions; prior-cycle benchmark). The schema requires `sample_size_rationale.qualitative_basis` and `floor_or_ceiling_reference` for judgmental samples.

### Defaulting to haphazard

Haphazard is hard to defend in front of a reviewer or examiner. It is not random (the preparer's unconscious selection biases creep in) and it is not judgmental (no documented basis). The memo flags any haphazard proposal for reviewer challenge and recommends a documented alternative (PRNG with seed, or judgmental with basis).

### Mixing methods without naming the mix

A combined test (design plus operating effectiveness) may need two samples drawn under two methods. The memo names each sample and the method that produced it. A single-sample claim that conflates a design walkthrough sample with an operating-effectiveness sample produces a sample-evaluation defect downstream.

## Sample size rationale discipline

### Citing AU-C 530 sample-size tables as a regulatory requirement

AU-C 530 is an external-audit standard. In second-line testing it is borrowed as a methodology anchor; the criterion source is the firm's testing methodology, anchored to public standards. The memo cites the firm methodology's reference into AU-C 530, not AU-C 530 directly as a binding regulatory requirement.

### Quoting a number without the inputs

The sample size is the output of confidence level, tolerable deviation rate, and expected deviation rate (for statistical) or of a documented qualitative basis with a floor or ceiling reference (for judgmental). Quoting "60 records, per firm methodology" without the inputs that produced 60 leaves the rationale untestable. The schema requires the inputs in `sample_size_rationale`.

### Setting expected deviation rate at zero by default

An expected deviation rate of zero produces a small sample under attribute-sampling tables and a brittle one in practice. Use the prior-cycle observed rate where available; default to a low non-zero value (firm methodology typically sets the default) when no prior data exists; flag the default as a methodology assumption.

## Tolerable deviation rate discipline

### Confusing tolerable deviation rate with materiality

Materiality is an external-audit concept oriented to financial-statement misstatement. Tolerable deviation rate is the maximum rate of control deviation the reviewer will accept and still conclude operating effectiveness. They are not interchangeable; conflating them in the memo is a methodology defect.

### Using a tolerable rate without naming the criterion source

Three percent because firm methodology says three percent, or zero percent because privileged-access policy says zero. The memo names the source. The schema requires `tolerable_deviation_rate.criterion_source`.

### Treating zero-tolerable populations as rate problems

Privileged-access populations, sanctions-screening populations, customer-funds-segregation populations, and similar zero-tolerable scopes change how the conclusion will read downstream. A single exception is a finding regardless of overall sample deviation rate. The memo names the zero-tolerable convention and flags it for the workpaper-drafter to read severity-driven rather than rate-driven.

### Mixing record-level and field-level tolerable rates

A test that examines multiple data points per record may carry a record-level tolerable rate and a field-level tolerable rate separately. The memo names which tolerable rate applies to which procedure level. Conflating the two produces wrong projection commentary in the workpaper.

## Selection method discipline

### Naming "random" without naming the generator and seed

"Random selection" without the generator and seed is not reproducible. A reviewer or examiner who pulls the memo a year later cannot rebuild the sample. The schema requires `selection_method.seed_or_interval` for prng and mus techniques.

### Sorting the population implicitly

The sample-draw output depends on the order of the population list when the technique is systematic or sortation-sensitive. The memo names the sort key. A different sort produces a different sample.

### Letting the drawer also be the evaluator

Where firm policy requires draw-and-evaluate separation (typical for high-risk control tests), the drawer role and the evaluator role are different. The memo captures `draw_metadata.drawer_role` separately from preparer.

## Sample drawn discipline

### Skipping the control-total reconciliation

The sample-draw output should reconcile to the population (sample size matches the planned size; sample IDs all appear in the population list). A discrepancy is a methodology defect; the memo stops and the reviewer is asked to authorise the gap before fieldwork begins.

### Treating sample IDs as evidence inventory

Sample IDs name what the sample contains, not what evidence will be pulled for each item. The evidence ask is the work of `evidence-request-builder`; this skill stops at the sample drawn.

## Limitations discipline

### Skipping limitations

The limitations section is the reviewer's protection paragraph. It explicitly names what the sample cannot conclude on (a separate population segment, items outside the period, items excluded by design), the period coverage gaps, and the completeness caveats. A memo without a limitations section gives a reviewer nothing to push back on.

### Claiming projection authority the sample does not support

Projection from a sample to a population is appropriate when the sample design supports it (random selection within a defined population at adequate confidence). A judgmental sample, a haphazard sample, or a stratified sample without random selection within strata typically does not support population-level projection. The memo names the projection limitation honestly so the workpaper-drafter does not over-claim the conclusion's reach.

## Engagement-scope and overlay loading

### Drafting without a control ID or test plan

A sampling memo with no control ID and no test plan reference has nothing to anchor to. Stop and route to `risk-compliance-core/skills/control-matrix` for the control ID, and to `test-plan-builder` for the test plan. The sampling memo is not a place to invent test scope.

### Loading the wrong sector overlay

Institution type and the regulator the test was designed for drive the sector overlay. A consumer-compliance test at a state member bank pulls banking; an adviser compliance-program test pulls capital-markets; a sponsor-bank end-customer reconciliation test pulls payments-fintech and banking together (dual-overlay loading is normal for sponsor-bank arrangements).

### Skipping cyber overlay on IAM or vulnerability-management populations

Cyber overlay is default-on for any control test touching IAM, vulnerability management, or covered-entity-cybersecurity-mandated areas. Population definition gets unusual for these tests (tickets, alerts, identities, packets) and benefits from the overlay's worked patterns.

### Skipping conduct overlay on consumer-facing tests

Conduct overlay is default-on for consumer-facing tests where stratification by customer segment matters separately from the technical control conclusion. UDAAP, fair-lending, complaint-handling, and Reg E error-resolution all benefit from the overlay's stratification conventions.

## Output discipline

### Citing without sections

Every regulator citation in the memo carries a section reference or a `[verify section]` placeholder. URL alone does not pass the source-anchor depth check. Use `references/source-anchors.md` and the loaded overlays for the canonical citation set; do not restate excerpts in the memo body.

### Marking unsupported claims silently

Use `[evidence needed]` explicitly in the memo where a claim is not yet evidenced (a population reconciliation pending; a tolerable-rate criterion source unconfirmed against firm methodology). An inferred claim presented as evidenced is the failure mode and a reviewer-challenge surface.

### Closing with too much certainty

The confidence label is `high` only when source posture, evidence sufficiency for the population assertion, and criterion sourcing for the tolerable rate line up. `medium` and `low` are normal where the source posture is below evidence-aware, where the population pull rests on a single extract without an independent reconciliation, or where the tolerable rate criterion source is firm methodology not externally benchmarked. `unknown` is honest where the firm has not yet resourced the population reconciliation.

### Drafting evidence requests inside the memo

The sampling memo names the items the test will reach. The evidence ask is a downstream artifact in `evidence-request-builder`. Drafting evidence requests inside the sampling memo duplicates work and creates two versions to keep in sync.
