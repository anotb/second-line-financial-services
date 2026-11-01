# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## overdraft-fee-disclosure-sampling

### Example: overdraft-fee-disclosure compliance-testing sample at a regional bank

Public-source-derived. No named institution. The shape mirrors a common annual operating-effectiveness test of an overdraft-fee disclosure control at a Tier-2 regional bank under the federal banking regulators' compliance-risk-management expectations.

#### Input

- **Test cycle**: annual operating-effectiveness test of the new-deposit-account overdraft-fee disclosure control, drafting the sampling memo before fieldwork.
- **Test plan reference**: pre-fieldwork test plan in flight (test ID `TP-CMP-OD-2026-Q1`); the sampling memo is being drafted in parallel because the sample design is non-trivial and the test-plan-builder needs the memo to anchor procedures.
- **Engagement scope supplied**: institution = regional bank (state-chartered Federal Reserve member), asset band $50-100B; primary regulators = FRB, CFPB, state DFI; persona = compliance-testing manager; source posture = public-plus-firm-policy-plus-evidence; sector overlay = banking; cross-cutting overlays = conduct (consumer-facing), with privacy not loaded as the test does not touch GLBA Safeguards.
- **Control under test**: control owner is the deposit-product compliance officer; control description is end-to-end disclosure delivery (account-opening packet content, in-branch verbal discussion script adherence, opt-in/opt-out election capture for overdraft protection, post-opening confirmation disclosure).
- **Population context**: roughly 38,000 new consumer checking accounts opened during Q1 across branch, online, and phone channels. Overdraft-protection enrollment is offered at account opening and post-opening; both election windows are in scope.

#### Output sketch

The skill produces a sampling memo. Headlines:

- **Header** — sampling ID `SM-CMP-OD-2026-Q1-001`, test ID `TP-CMP-OD-2026-Q1` (test plan in flight; the sampling memo precedes the final test plan), control ID for the overdraft-fee disclosure control, obligation IDs for Reg E §1005.17 (opt-in for overdraft services) and Reg DD §1030.11 (overdraft service disclosure) [verify subsection labels], period under test (Q1), source posture public-plus-firm-policy-plus-evidence, preparer role (compliance-testing analyst), reviewer role (compliance-testing manager — separate role).
- **Scope and source posture** — annual operating-effectiveness test of the overdraft-fee disclosure control across new consumer checking accounts opened in Q1; test objective is operating effectiveness with a walkthrough-only design read because the control design was tested in the prior cycle and there have been no design changes.
- **Population definition** — population is new consumer checking accounts opened during Q1 (account-opening packets generated and accounts opened in the period). Source of truth: deposit account-opening system extract `DDA-CORE:NEW_ACCT_Q1` run on the second business day after quarter-end by the deposit-product analytics role. Period boundaries: account-opening date within Q1; cut-off treatment is account-opened-date (not application-date). Completeness basis: extract row count reconciled to the daily new-account reporting feed control total within tolerance (variance under firm policy threshold). Exclusions: account-conversion events (existing-customer relationship changes that generate a new account record but not a new disclosure event) excluded with rationale (different control); business and trust accounts excluded (different disclosure regime). Population size after exclusions: approximately 38,000.
- **Risk-based stratification** — stratified by channel (branch, online, phone) and by overdraft-protection election status (opted-in at opening, opted-out at opening, no election at opening). Rationale: conduct risk concentrates on the opted-in segment because the disclosure must support an informed opt-in decision; channel matters because the verbal-discussion-script adherence is a branch-and-phone-only sub-procedure.
- **Sample method** — statistical attribute sampling. Why: high-volume uniform population on dimensions the test cares about; operating-effectiveness-only test objective; firm methodology supports projection at this confidence level.
- **Sample size rationale** — confidence level 95%; tolerable deviation rate 5% (firm methodology); expected deviation rate 1% (prior-cycle observed rate); resulting sample size 95 per the firm's adopted attribute-sampling table (firm methodology references the AICPA AU-C 530-derived inputs without claiming AU-C 530 as a binding regulatory requirement). Stratification allocation: 60 to branch, 25 to online, 10 to phone, with internal stratification by election status proportional to the opted-in segment's risk concentration.
- **Selection method** — PRNG (firm-standard NumPy mt19937) with seed `2026-Q1-OD-001`; population sorted by account number ascending before draw. Reproducibility note: the sample list can be rebuilt from the source extract, the seed, and the sort key.
- **Tolerable deviation rate** — 5% overall per firm methodology; criterion source is firm consumer-compliance testing methodology, anchored to public guidance. Procedure-level breakouts: 0% tolerable on missing-disclosure (no disclosure delivered at all) per firm policy because the regulatory consequence is absolute; 5% tolerable on disclosure-content-deviation (disclosure delivered but with content variances from the firm-approved template).
- **Sample drawn** — 95 sample IDs (pointer to sample-list file `SL-2026-Q1-OD-001.csv`), draw date second business day after quarter-end, drawer role (compliance-testing analyst, also the preparer; the firm's policy does not require draw-and-evaluate separation at this risk tier), control-total reconciliation: 95 sample IDs all appear in the population list; sample size matches planned 95.
- **Limitations and assumptions** — sample addresses only the new-account-opening disclosure population; does not cover post-opening fee-change disclosures (different control); does not cover verbal disclosures captured only on call recordings (the call-recording library is in scope for a separate test; the limitation is flagged for test-plan-builder). Period coverage limited to Q1; cross-quarter trend reads require subsequent-cycle samples. Projection authority: appropriate to project at the channel-stratum level given the random selection within strata; not appropriate to project to the opted-in segment specifically because the segment internal allocation was proportional rather than oversampled (a reviewer question).
- **Reviewer questions** — one reviewer question for the compliance-testing manager: whether the opted-in segment justifies a separate test (with its own sample) rather than a stratum within this test, given the conduct-risk concentration; the question names the decision (next-cycle scope or in-cycle expansion). One reviewer question for the head of regulatory affairs: whether the recently-published interagency guidance on overdraft fees [verify exact citation and date if any new guidance applies in the period] changes the criterion source for the tolerable rate.
- **Confidence label** — high (source posture public-plus-firm-policy-plus-evidence; population pull reconciled to the daily reporting feed; criterion source for the tolerable rate is firm methodology with explicit anchoring to public standards; sample size adequate for the channel-stratum-level projection).

The memo stops at sample drawn and the reviewer question about segment-versus-stratum scope.

#### Why this scenario matters

- **Boundary check on sample method**: statistical attribute over a high-volume uniform population, with firm methodology citing AU-C 530-derived inputs but not claiming AU-C 530 as a binding regulatory requirement.
- **Boundary check on population definition**: population is new-account-opening events, not source records in the deposit-account database; cut-off is account-opened-date with explicit treatment.
- **Boundary check on stratification**: channel-and-election-status stratification with explicit rationale; segment-level oversampling deferred as a reviewer question rather than silently assumed.
- **Boundary check on tolerable rate**: procedure-level breakouts (0% for missing-disclosure, 5% for content-deviation) with named criterion sources.
- **Boundary check on projection authority**: channel-stratum projection appropriate; opted-in-segment-specific projection flagged as not appropriate at this sample design.
- **Boundary check on limitations**: verbal-disclosure call-recording population flagged as out of scope for this test, surfaced for test-plan-builder.

#### Anchors

- Reg E — 12 CFR Part 1005, including §1005.17 (overdraft services) [verify subsection labels].
- Reg DD — 12 CFR Part 1030, including §1030.11 (overdraft service disclosure) [verify subsection labels].
- AICPA AU-C 530 (Audit Sampling) — methodology anchor only.
- CFPB Compliance Management Review examination procedures (CFPB Supervision and Examination Manual, current edition) [verify section].
- SR 08-8 (Federal Reserve, October 16, 2008) — testing-program scope and population coverage [verify section].

See `references/source-anchors.md` and `references/sector-overlays.md#banking` for full citations; `references/cross-cutting.md#conduct` for the conduct-overlay stratification conventions used.

## quarterly-access-recertification-sampling

### Example: quarterly logical-access-recertification sample for a critical core-banking application

Public-source-derived. No named institution. The shape mirrors a quarterly second-line technology-risk test of a logical-access-recertification control at a NYDFS Covered Entity using a critical core-banking application.

#### Input

- **Test cycle**: quarterly operating-effectiveness test of the logical-access-recertification control for a critical core-banking application, drafting the sampling memo before fieldwork.
- **Test plan reference**: pre-fieldwork test plan (test ID `TP-TECH-IAM-2026-Q2`) names the population (quarterly recertification packets generated for entitled users on the application), the procedures (packet-completeness reperformance, recertifier-role validation, removed-entitlement-effective-date reperformance, terminated-employee timeliness reperformance), and the procedure-level conclusions.
- **Engagement scope supplied**: institution = state-chartered bank with NYDFS Covered Entity status; primary regulators = FRB, NYDFS, CFPB; persona = head of technology risk (second line); source posture = public-plus-firm-policy-plus-evidence; sector overlay = banking; cross-cutting overlays = cyber (Part 500), with privacy not loaded as the test does not touch consumer-financial-information access patterns specifically.
- **Control under test**: control owner is the IAM platform owner; control description is quarterly recertification of all entitled users on the application, with packet-based attestation by line-manager-and-application-owner with segregation-of-duties review for privileged entitlements.
- **Population context**: approximately 2,400 recertification packets generated in the quarter across roughly 1,800 distinct users (some users have multiple packets across roles); the application is in the firm's tier-1 production list and supports core deposit and lending operations.

#### Output sketch

The skill produces a sampling memo. Headlines:

- **Header** — sampling ID `SM-TECH-IAM-2026-Q2-001`, test ID `TP-TECH-IAM-2026-Q2`, control ID for the IAM-recertification control on this application, obligation IDs for NYDFS 23 NYCRR §500.7 (access privileges and management) [verify subsection labels] and the firm's IT-GCC policy on access recertification, period under test (Q2), source posture public-plus-firm-policy-plus-evidence, preparer role (technology-risk testing analyst), reviewer role (technology-risk testing manager — separate role).
- **Scope and source posture** — quarterly operating-effectiveness test of the recertification control on the named application; test objective is operating effectiveness; design read carried separately by reference to the prior-cycle design walkthrough (no design changes during the quarter per change-management evidence).
- **Population definition** — population is recertification packets generated for entitled users on the application during the quarter (not entitled users; a single user can have multiple packets across roles). Source of truth: IAM platform extract from the recertification module run on the first business day after quarter-end by the IAM platform owner role. Period boundaries: packet-generated-date within Q2; cut-off treatment is packet-generated-date (not packet-completed-date because the test reads packet completion within the quarterly cycle). Completeness basis: extract reconciliation against the IAM platform's recertification-event log for the quarter, plus an independent count of entitled-user records on the application as of the cycle start date. Exclusions: service accounts and break-glass identities excluded from this population per firm policy and tested under separate populations (service-account-recertification test runs annually; break-glass-identity-use test runs monthly). Population size after exclusions: approximately 2,400 packets.
- **Risk-based stratification** — stratified by privilege tier (privileged, standard) with oversampling of privileged packets; secondary stratification by recertifier role (line manager, application owner, segregation-of-duties reviewer for privileged entitlements). Rationale: privileged-access risk concentration is asymmetric (privileged-not-revoked-after-termination scenarios carry tier-1-application impact); the cyber overlay's IAM convention oversamples privileged packets accordingly.
- **Sample method** — judgmental, with a documented basis. Why: the privileged subpopulation is small (approximately 180 packets) and statistical attribute sampling at firm methodology's standard inputs would not produce a defensible projection at the privileged-segment level; full-population testing of privileged packets is appropriate per the firm's IT-GCC methodology floor for tier-1 applications; standard packets sampled judgmentally with a documented basis.
- **Sample size rationale** — qualitative basis: full-population coverage of the 180 privileged packets; 30 standard packets sampled judgmentally by recertifier-role distribution and packet-status (completed-on-time, completed-late, returned-for-rework). Floor or ceiling reference: firm IT-GCC methodology floor of 25 standard packets for tier-1-application quarterly recertification testing; FFIEC IT Examination Handbook Audit booklet appendix conventions [verify section] cited as the external benchmark for the methodology floor. Resulting sample size: 210 packets total (180 privileged + 30 standard).
- **Selection method** — privileged: full-population (no selection technique; all 180 packets pulled). Standard: judgmental criteria — proportional to recertifier-role distribution, with explicit selection of 5 returned-for-rework packets, 5 completed-late packets, and 20 completed-on-time packets distributed across recertifier roles. Reproducibility note: the judgmental criteria are documented in the memo so a reviewer can rebuild the sample from the population list and the criteria.
- **Tolerable deviation rate** — 0% for privileged packets per firm policy on tier-1-application privileged-access testing; criterion source is firm IT-GCC policy, anchored to NYDFS §500.7 [verify subsection] and the firm's adopted zero-tolerable convention for privileged populations. 5% for standard packets per firm IT-GCC methodology; criterion source is firm methodology benchmarked against the FFIEC IT booklet appendix conventions [verify section]. Procedure-level breakouts: removed-entitlement-effective-date reperformance carries a 0% tolerable rate (an entitlement that should have been removed but was not removed by the cycle's effective date is a finding regardless of overall rate).
- **Sample drawn** — 210 sample IDs (pointer to sample-list file `SL-2026-Q2-IAM-001.csv`), draw date first business day after quarter-end, drawer role (technology-risk testing analyst, also the preparer; firm policy does not require draw-and-evaluate separation at this risk tier given the small judgmental component), control-total reconciliation: 210 sample IDs all appear in the population list; privileged subset reconciled to the IAM platform's privileged-entitlement count.
- **Limitations and assumptions** — sample addresses only the recertification-packet population for this application; does not cover entitlement-provisioning at onboarding (different control, different test); does not cover service-account or break-glass populations (excluded with rationale; tested separately). Period coverage limited to Q2; cross-quarter trend reads require subsequent-cycle samples. Projection authority: appropriate to conclude on privileged-population operating effectiveness at the population level (full-population coverage); appropriate to conclude on standard-population operating effectiveness at the firm-methodology-floor confidence level only (judgmental sample); not appropriate to project a population-level rate from the standard sample.
- **Reviewer questions** — one reviewer question for the technology-risk testing manager: whether the firm's adopted zero-tolerable convention for privileged-access populations should be tightened further (current convention permits one administrative remediation event per cycle without escalation; the question names the decision for next-cycle methodology revision). One reviewer question for the IAM platform owner: whether service-account-recertification scope should be added to this test cycle given a recent change-management event that introduced new service accounts on the application (the question names the scope-expansion decision).
- **Confidence label** — high on documentation of method (full-population for privileged; judgmental with documented basis and floor reference for standard); medium on the standard-sample size (firm methodology floor is not externally benchmarked beyond the FFIEC IT booklet appendix conventions, which are general not application-specific).

The memo stops at sample drawn and the reviewer questions on zero-tolerable convention and service-account-scope expansion.

#### Why this scenario matters

- **Boundary check on population definition**: population is packets, not users; the memo names this explicitly because the user-vs-packet distinction is a recurring confusion.
- **Boundary check on sample method**: judgmental for the standard segment because statistical sampling would not produce a defensible projection at the firm methodology's inputs; full-population for the privileged segment because the firm's IT-GCC methodology floor for tier-1 applications calls for it.
- **Boundary check on tolerable rate**: zero-tolerable for privileged packets per firm policy and procedure-level zero-tolerable for the removed-entitlement-effective-date reperformance, with explicit criterion sourcing.
- **Boundary check on stratification**: privileged-vs-standard with privileged oversampling, plus recertifier-role secondary stratification driven by the cyber overlay's IAM conventions.
- **Boundary check on projection**: appropriate to conclude on the privileged population at population-level (full-population coverage); not appropriate to project a population-level rate from the judgmental standard sample.
- **Boundary check on exclusions**: service-account and break-glass identities excluded with rationale and pointer to the separate populations they live in.

#### Anchors

- NYDFS 23 NYCRR Part 500.7 (Access Privileges and Management) [verify subsection labels].
- FFIEC Information Technology Examination Handbook — Audit booklet (April 2012) [verify section labels].
- AICPA AU-C 530 (Audit Sampling) — methodology anchor only.
- NIST SP 800-53A Rev. 5 — assessment-object selection conventions.
- COSO 2013 Internal Control — Integrated Framework, Principle 16 [verify principle reference].

See `references/source-anchors.md` and `references/cross-cutting.md#cyber` for full citations; `references/sector-overlays.md#banking` for the bank-supervisory frame.

## troubleshooting

### Troubleshooting: control-sampling

Recurring pitfalls. Read before drafting the sampling memo and again before reviewer sign-off.

#### Population definition discipline

##### Defining the population as the source system

The population is the items the sample can draw from to answer the test question, not the database that holds those items. "The LAR data warehouse" is a source system; "LAR records reported during the calendar year" is a population. "The IAM platform" is a source system; "recertification packets generated for entitled users in the most recent quarter" is a population. The schema enforces the discipline: `population.description` is the items, `population.source_of_truth` is the system. Confusing them produces sample-design defects that surface in QA.

##### Skipping the completeness basis

A population pull without a reconciliation to a control total or an independent extract sits unsupported. Every sample-level conclusion downstream rests on the completeness assertion. Name the reconciliation: extract row count to system-of-record count within tolerance; dual-extract comparison; system-of-record cut-off attestation by the data owner. The schema enforces it: `population.completeness_basis` is required.

##### Treating cut-off as implicit

Period boundaries carry cut-off treatment. Are items in the period the items recorded with effective dates in the period, items processed in the period, or items reaching final state in the period? The three populations differ. The memo names the cut-off treatment so a reviewer can challenge it.

##### Carrying exclusions without rationale

Excluding items from the population without naming the rationale buries the methodology call. Each exclusion carries a criterion (out-of-period; belongs to a different test; not reachable through available evidence) and a one-line rationale. The schema requires both fields on every exclusion.

#### Stratification discipline

##### Stratifying for stratification's sake

Stratification is a risk-based call. When the population is uniform on the dimensions the test cares about, the memo names the no-stratification choice and explains why. Stratifying a uniform population produces strata too thin to draw from and weakens the sample.

##### Skipping stratification on a heterogeneous population

A population with known higher-risk segments (privileged versus standard access; high-dollar versus low-dollar transactions; high-risk versus low-risk customers; sponsor-bank end-customers within a deposit-program population) calls for stratification with oversampling of the higher-risk segment. Skipping stratification here treats the population as uniform and dilutes the sample's ability to surface concentrated risk.

##### Stratifying without sizing the strata

Listing the factors without naming the bucket sizes leaves the actual sample design implicit. The schema requires `bucket_size` on each stratification entry.

#### Sample method discipline

##### Picking statistical for a small population

Statistical attribute sampling gives confident projection over a population large enough to support it. A population under a few hundred items typically does not produce a statistically efficient sample; full-population testing or a judgmental sample with a documented basis is more honest. The memo names the method and the reasoning; defaulting to statistical because "statistical sounds rigorous" produces oversampling and a misleading confidence claim.

##### Picking judgmental without writing the basis

"Risk-based" alone is not a basis. The basis names the factors, the weights, and the floor or ceiling reference (firm methodology floor; regulator-handbook appendix conventions; prior-cycle benchmark). The schema requires `sample_size_rationale.qualitative_basis` and `floor_or_ceiling_reference` for judgmental samples.

##### Defaulting to haphazard

Haphazard is hard to defend in front of a reviewer or examiner. It is not random (the preparer's unconscious selection biases creep in) and it is not judgmental (no documented basis). The memo flags any haphazard proposal for reviewer challenge and recommends a documented alternative (PRNG with seed, or judgmental with basis).

##### Mixing methods without naming the mix

A combined test (design plus operating effectiveness) may need two samples drawn under two methods. The memo names each sample and the method that produced it. A single-sample claim that conflates a design walkthrough sample with an operating-effectiveness sample produces a sample-evaluation defect downstream.

#### Sample size rationale discipline

##### Citing AU-C 530 sample-size tables as a regulatory requirement

AU-C 530 is an external-audit standard. In second-line testing it is borrowed as a methodology anchor; the criterion source is the firm's testing methodology, anchored to public standards. The memo cites the firm methodology's reference into AU-C 530, not AU-C 530 directly as a binding regulatory requirement.

##### Quoting a number without the inputs

The sample size is the output of confidence level, tolerable deviation rate, and expected deviation rate (for statistical) or of a documented qualitative basis with a floor or ceiling reference (for judgmental). Quoting "60 records, per firm methodology" without the inputs that produced 60 leaves the rationale untestable. The schema requires the inputs in `sample_size_rationale`.

##### Setting expected deviation rate at zero by default

An expected deviation rate of zero produces a small sample under attribute-sampling tables and a brittle one in practice. Use the prior-cycle observed rate where available; default to a low non-zero value (firm methodology typically sets the default) when no prior data exists; flag the default as a methodology assumption.

#### Tolerable deviation rate discipline

##### Confusing tolerable deviation rate with materiality

Materiality is an external-audit concept oriented to financial-statement misstatement. Tolerable deviation rate is the maximum rate of control deviation the reviewer will accept and still conclude operating effectiveness. They are not interchangeable; conflating them in the memo is a methodology defect.

##### Using a tolerable rate without naming the criterion source

Three percent because firm methodology says three percent, or zero percent because privileged-access policy says zero. The memo names the source. The schema requires `tolerable_deviation_rate.criterion_source`.

##### Treating zero-tolerable populations as rate problems

Privileged-access populations, sanctions-screening populations, customer-funds-segregation populations, and similar zero-tolerable scopes change how the conclusion will read downstream. A single exception is a finding regardless of overall sample deviation rate. The memo names the zero-tolerable convention and flags it for the workpaper-drafter to read severity-driven rather than rate-driven.

##### Mixing record-level and field-level tolerable rates

A test that examines multiple data points per record may carry a record-level tolerable rate and a field-level tolerable rate separately. The memo names which tolerable rate applies to which procedure level. Conflating the two produces wrong projection commentary in the workpaper.

#### Selection method discipline

##### Naming "random" without naming the generator and seed

"Random selection" without the generator and seed is not reproducible. A reviewer or examiner who pulls the memo a year later cannot rebuild the sample. The schema requires `selection_method.seed_or_interval` for prng and mus techniques.

##### Sorting the population implicitly

The sample-draw output depends on the order of the population list when the technique is systematic or sortation-sensitive. The memo names the sort key. A different sort produces a different sample.

##### Letting the drawer also be the evaluator

Where firm policy requires draw-and-evaluate separation (typical for high-risk control tests), the drawer role and the evaluator role are different. The memo captures `draw_metadata.drawer_role` separately from preparer.

#### Sample drawn discipline

##### Skipping the control-total reconciliation

The sample-draw output should reconcile to the population (sample size matches the planned size; sample IDs all appear in the population list). A discrepancy is a methodology defect; the memo stops and the reviewer is asked to authorise the gap before fieldwork begins.

##### Treating sample IDs as evidence inventory

Sample IDs name what the sample contains, not what evidence will be pulled for each item. The evidence ask is the work of `evidence-request-builder`; this skill stops at the sample drawn.

#### Limitations discipline

##### Skipping limitations

The limitations section is the reviewer's protection paragraph. It explicitly names what the sample cannot conclude on (a separate population segment, items outside the period, items excluded by design), the period coverage gaps, and the completeness caveats. A memo without a limitations section gives a reviewer nothing to push back on.

##### Claiming projection authority the sample does not support

Projection from a sample to a population is appropriate when the sample design supports it (random selection within a defined population at adequate confidence). A judgmental sample, a haphazard sample, or a stratified sample without random selection within strata typically does not support population-level projection. The memo names the projection limitation honestly so the workpaper-drafter does not over-claim the conclusion's reach.

#### Engagement-scope and overlay loading

##### Drafting without a control ID or test plan

A sampling memo with no control ID and no test plan reference has nothing to anchor to. Stop and route to `control-matrix` for the control ID, and to `test-plan-builder` for the test plan. The sampling memo is not a place to invent test scope.

##### Loading the wrong sector overlay

Institution type and the regulator the test was designed for drive the sector overlay. A consumer-compliance test at a state member bank pulls banking; an adviser compliance-program test pulls capital-markets; a sponsor-bank end-customer reconciliation test pulls payments-fintech and banking together (dual-overlay loading is normal for sponsor-bank arrangements).

##### Skipping cyber overlay on IAM or vulnerability-management populations

Cyber overlay is default-on for any control test touching IAM, vulnerability management, or covered-entity-cybersecurity-mandated areas. Population definition gets unusual for these tests (tickets, alerts, identities, packets) and benefits from the overlay's worked patterns.

##### Skipping conduct overlay on consumer-facing tests

Conduct overlay is default-on for consumer-facing tests where stratification by customer segment matters separately from the technical control conclusion. UDAAP, fair-lending, complaint-handling, and Reg E error-resolution all benefit from the overlay's stratification conventions.

#### Output discipline

##### Citing without sections

Every regulator citation in the memo carries a section reference or a `[verify section]` placeholder. URL alone does not clear the source-anchor depth check. Use `references/source-anchors.md` and the loaded overlays for the canonical citation set; do not restate excerpts in the memo body.

##### Marking unsupported claims silently

Use `[evidence needed]` explicitly in the memo where a claim is not yet evidenced (a population reconciliation pending; a tolerable-rate criterion source unconfirmed against firm methodology). An inferred claim presented as evidenced is the failure mode and a reviewer-challenge surface.

##### Closing with too much certainty

The confidence label is `high` only when source posture, evidence sufficiency for the population assertion, and criterion sourcing for the tolerable rate line up. `medium` and `low` are normal where the source posture is below evidence-aware, where the population pull rests on a single extract without an independent reconciliation, or where the tolerable rate criterion source is firm methodology not externally benchmarked. `unknown` is honest where the firm has not yet resourced the population reconciliation.

##### Drafting evidence requests inside the memo

The sampling memo names the items the test will reach. The evidence ask is a downstream artifact in `evidence-request-builder`. Drafting evidence requests inside the sampling memo duplicates work and creates two versions to keep in sync.
