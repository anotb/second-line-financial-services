# Example: overdraft-fee-disclosure compliance-testing sample at a regional bank

Public-source-derived. No named institution. The shape mirrors a common annual operating-effectiveness test of an overdraft-fee disclosure control at a Tier-2 regional bank under the federal banking regulators' compliance-risk-management expectations.

## Input

- **Test cycle**: annual operating-effectiveness test of the new-deposit-account overdraft-fee disclosure control, drafting the sampling memo before fieldwork.
- **Test plan reference**: pre-fieldwork test plan in flight (test ID `TP-CMP-OD-2026-Q1`); the sampling memo is being drafted in parallel because the sample design is non-trivial and the test-plan-builder needs the memo to anchor procedures.
- **Engagement scope supplied**: institution = regional bank (state-chartered Federal Reserve member), asset band $50-100B; primary regulators = FRB, CFPB, state DFI; persona = compliance-testing manager; source posture = public-plus-firm-policy-plus-evidence; sector overlay = banking; cross-cutting overlays = conduct (consumer-facing), with privacy not loaded as the test does not touch GLBA Safeguards.
- **Control under test**: control owner is the deposit-product compliance officer; control description is end-to-end disclosure delivery (account-opening packet content, in-branch verbal discussion script adherence, opt-in/opt-out election capture for overdraft protection, post-opening confirmation disclosure).
- **Population context**: roughly 38,000 new consumer checking accounts opened during Q1 across branch, online, and phone channels. Overdraft-protection enrollment is offered at account opening and post-opening; both election windows are in scope.

## Output sketch

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

## Why this scenario matters

- **Boundary check on sample method**: statistical attribute over a high-volume uniform population, with firm methodology citing AU-C 530-derived inputs but not claiming AU-C 530 as a binding regulatory requirement.
- **Boundary check on population definition**: population is new-account-opening events, not source records in the deposit-account database; cut-off is account-opened-date with explicit treatment.
- **Boundary check on stratification**: channel-and-election-status stratification with explicit rationale; segment-level oversampling deferred as a reviewer question rather than silently assumed.
- **Boundary check on tolerable rate**: procedure-level breakouts (0% for missing-disclosure, 5% for content-deviation) with named criterion sources.
- **Boundary check on projection authority**: channel-stratum projection appropriate; opted-in-segment-specific projection flagged as not appropriate at this sample design.
- **Boundary check on limitations**: verbal-disclosure call-recording population flagged as out of scope for this test, surfaced for test-plan-builder.

## Anchors

- Reg E — 12 CFR Part 1005, including §1005.17 (overdraft services) [verify subsection labels].
- Reg DD — 12 CFR Part 1030, including §1030.11 (overdraft service disclosure) [verify subsection labels].
- AICPA AU-C 530 (Audit Sampling) — methodology anchor only.
- CFPB Compliance Management Review examination procedures (CFPB Supervision and Examination Manual, current edition) [verify section].
- SR 08-8 (Federal Reserve, October 16, 2008) — testing-program scope and population coverage [verify section].

See `references/source-anchors.md` and `references/sector-overlays/banking.md` for full citations; `references/cross-cutting/conduct.md` for the conduct-overlay stratification conventions used.
