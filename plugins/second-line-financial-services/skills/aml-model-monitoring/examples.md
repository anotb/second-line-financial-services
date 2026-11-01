# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## annual-review-mid-size-bank

### Example: annual second-line monitoring memo, mid-size US bank

#### Scenario

Mid-size US national bank, total assets in the $20-50B band, AML transaction-monitoring system covers retail deposit, commercial deposit, ACH, wire, and check products. Engagement is the annual second-line monitoring memo for the trailing twelve-month review window. Sponsor is the CRO; audience is the AML governance committee with the BSA officer and head of model risk attending. Source posture is public-plus-firm-policy-plus-evidence; the engagement has access to the firm's monitoring documentation, the model inventory, the validation report from the prior cycle, the change-governance log, and segmentation refresh artifacts.

Engagement scope flags banking sector overlay. Cyber cross-cutting overlay is not flagged at the program level for this engagement.

#### Output sketch

The memo opens with program review framing: the system is in scope as a model under the named model-risk supervisory guidance, and the review is read against that frame, not as a "rules" review. Material findings:

- **Segmentation refresh overdue.** Last refresh was fourteen months ago against firm policy of twelve-month maximum cadence. Two retail and one small-business segment are affected. Recommendation routes to the AML governance committee for tuning-cycle sequencing decision; the next tuning cycle should not run on a stale segmentation base.
- **BTL testing coverage gap.** Below-the-line testing was performed for two of seven scenarios in the window; the five untested scenarios include rapid-movement-of-funds and structuring, both of which carry material productivity exposure. No documented rationale for the coverage gap. Recommendation routes to the head of model risk for BTL coverage planning before the next validation cycle.
- **Productivity decline without tuning hypothesis.** Alert productivity for the unusual-pattern-against-expected-activity scenario has declined four consecutive quarters without a documented tuning hypothesis or remediation plan on file. Recommendation routes to the BSA officer and the scenario owner for either a tuning hypothesis with documented baseline or a productivity-stabilisation plan.
- **Data-quality issue outstanding.** A deprecated wire-feed identifier issue was documented in the prior validation as a finding; remediation target dates have slipped through two cycles. Recommendation routes to the BSA officer for cross-functional escalation; data-quality issues outstanding past two cycles read as a governance gap, not a technical gap.
- **Threshold-change governance pattern observation.** Six threshold changes in the window; five carry approval evidence dated before the change effective date; one carries approval evidence dated after. Recommendation: align change-governance procedure to require pre-effective-date approval evidence on file at the change record.

The recommended human-review gates section names: segmentation refresh before next tuning cycle (gated by AML governance committee); BTL coverage plan before next validation (gated by head of model risk); productivity-decline scenarios reviewed at next monthly tuning forum (gated by BSA officer). The memo does not propose the new thresholds, the new segmentation cuts, the BTL sample sizes, or the validation scope itself; those are the change-governance machinery's calls.

The structured artifact (memo body) carries the BTL stats, productivity tables, threshold-change governance log summary, and segmentation drift indicators in named sections. The memo as a whole is the practitioner-natural Word output.

#### Why this scenario matters

This is the canonical annual review and exercises the four most-cited monitoring-governance failure modes: segmentation drift overdue, BTL coverage gaps, productivity decline without tuning hypothesis, and threshold-change governance discipline. The example shows the skill staying in review-artifact scope (it surfaces gaps and routes to gates) and not crossing into approval-of-change scope. The model-risk frame at the open is the load-bearing call: the same memo without that frame would land as a "rules check" and the model-risk supervisory expectations would not enter the analysis.

## post-tuning-review-structuring-scenario

### Example: post-tuning review of a structuring-scenario threshold change

#### Scenario

Regional bank, total assets in the $5-10B band. The structuring scenario was tuned in the prior quarter; the threshold was tightened from the prior baseline (the specific values are firm-confidential and do not appear in the memo). The engagement is a focused post-tuning review of the change evidence, not an annual review. Sponsor is the BSA officer; audience is the AML model risk subcommittee. Source posture is public-plus-firm-policy-plus-evidence with access to the tuning workpapers, the BTL sample, the change record in the change-governance log, the approver list, and the post-change alert volume and productivity data.

Engagement scope flags banking sector overlay. Cyber overlay not flagged.

#### Output sketch

The memo opens with the model-risk frame and the change-specific scope: this review is bounded to the structuring threshold change and the evidence supporting it. Findings:

- **BTL evidence at the prior threshold is on file.** Sample size is statistically defensible against the population in the BTL window. Escalation rate and sign-off are documented; the BTL reviewer is named and is independent of the tuning team. This is a clean line; the memo records it as a strength.
- **Productivity uplift hypothesis is stated and quantified.** The tuning workpaper sets out the productivity-uplift expectation against the prior baseline with a defined denominator. The denominator definition is consistent with the firm's program-level productivity definition.
- **Reproducibility gap.** The reviewer cannot independently reproduce the productivity calculation from the artifacts on file because the calculation script is not version-controlled. The numbers may be right; the evidence chain that supports them is incomplete. Recommendation routes to the head of model risk for a calculation-reproducibility evidence gate to be added to the standard tuning workflow.
- **Approver-independence documentation gap.** The change is approved and the approval is recorded; the approver's independence from the tuning team is not documented at the change record. Recommendation: add approver-independence documentation to the standard change-record template; the gap on this specific change can be remediated by a back-fill attestation if the approver was in fact independent.
- **Post-implementation review at 90 days recommended.** Standard practice; the memo names the gate and the criteria the post-implementation review will read against (productivity at the new threshold, false-positive rate trend, SAR conversion rate trend, BTL re-test at the new threshold).

The recommended human-review gates section names: post-implementation review at 90 days (gated by AML model risk subcommittee); calculation reproducibility evidence (gated by head of model risk); approver-independence documentation gate added to standard tuning workflow (gated by BSA officer and head of model risk jointly).

#### Why this scenario matters

This exercises the change-governance discipline the skill carries hardest. Tuning changes are the most-cited model-risk-touched activity in AML monitoring; the QA reads not whether the threshold is right (it is not in scope) but whether the evidence chain supporting the change is complete and the change-governance machinery functioned as designed. The reproducibility gap and the approver-independence gap are both common findings in real review work and both route to programmatic remediation, not to the specific change being un-done.

## troubleshooting

### Troubleshooting: aml-model-monitoring

Common defects in monitoring-review work product. Use this list to catch the recurring failure modes before sponsor sign-off.

#### "AML monitoring is rules, not a model"

The most common failure mode. The memo reads the system as a rules engine, applies BSA/AML examination expectations only, and skips model-risk discipline (development, implementation, use, validation, governance, ongoing monitoring, effective challenge). The named US model-risk supervisory guidance treats AML transaction monitoring as a model when it applies statistical, economic, financial, or mathematical theory to inputs (scenarios, thresholds, segmentation, and tuning all qualify). The program review at section one of the memo states the model frame explicitly. If the memo body does not read against the model-risk discipline, redraft.

#### Productivity figures without denominator definitions

A productivity number reported as "12%" is uninterpretable without the denominator. SARs / alerts? Escalations / alerts? SARs / investigations? Different programs use different denominators and the same word means different things across firms. The structured fields in the template force a denominator definition; if the source artifact does not define it, mark `[evidence needed]` and route to the BSA officer for definitional clarification before the figure goes in the memo.

#### BTL "performed" reported as a binary

"BTL was performed for this scenario" is not enough. The discipline lives in the sample size against the population, the escalation rate, the sign-off chain, and the reviewer's independence from the tuning team. If the source artifact reports BTL as performed without those, the BTL line in the memo carries `[evidence needed]` until the workpaper is on file.

#### Segmentation drift assessed only on population

Population per segment can be stable while behaviour per segment moves. A segmentation that looks stable on count is not stable in any monitoring-relevant sense if the volume, velocity, counterparty mix, or geography distribution per segment has shifted. The drift indicators table has rows for both; both should be filled.

#### Threshold-change approval evidence post-dates the change

A common change-governance gap. The change is made, the meeting that approves it happens later, and the meeting minute serves as the approval. The change-governance log should carry the approval evidence dated before the change effective date. The skill records the gap as an observation against the specific change and routes a programmatic remediation to the change-governance owner; the change itself is not unwound by the QA.

#### Reviewer drifts into proposing the new threshold or new scenario

Out of scope. The QA produces gate recommendations and routes findings to the change-governance machinery; the threshold value, the scenario design, the segmentation cuts, and the validation conclusions are made by the named decisionmaker. If the memo proposes a specific new threshold or specific new scenario language, redraft to a routing recommendation.

#### Validation findings outstanding past target dates without re-baselining

When validation findings sit open past their remediation target, the QA reads whether the firm has formally re-baselined the target with documented rationale or whether the date has slipped silently. Silent date-slip is a governance finding; documented re-baselining is a fact to record without flagging. The structured fields capture the distinction.

#### Scope creep into validation

The validation cycle is its own deliverable in the model-risk plugin. This skill consumes validation evidence (last date, scope, open findings, validator independence); it does not produce the validation. If the memo starts walking validation methodology in detail, the work has crossed scope. Hand off to the validation skill in the model-risk plugin.

#### Scope creep into SAR decisioning

QA over individual SAR decisions sits in `sar-decision-qa`. The monitoring memo reads the upstream signal (alert productivity, SAR conversion at the program level, scenario-level SAR conversion); it does not read the case-level SAR decision. Cross-link findings that require SAR-level QA to that skill.

#### Sector overlay not loaded

Reading a payments-fintech monitoring system through a deposit-bank lens (or a broker-dealer system through a deposit-bank lens) misses the typology surface that matters. The scope should name the sector overlay; if it does not, the QA asks the practitioner before drafting and notes the assumption in the memo. A memo that does not name the sector overlay it loaded has not engaged the question.

#### Cyber overlay not loaded when the typology surface implicates it

Customer base shows VASP transaction patterns, the firm has experienced ATO loss, BEC payouts have appeared in prior SAR filings, but the cyber cross-cutting overlay is not loaded and the scenario inventory carries no ATO, BEC, or VASP-conversion scenarios. The QA loads the cyber overlay (`references/cross-cutting.md#cyber`) when the typology evidence is on file, even if the scope did not explicitly flag it; the memo notes the load.

#### Source-anchor citations in the memo body

The memo body uses generic regulator language; specific section references and named-source citations live in `references/source-anchors.md`. A memo body that quotes section numbers is duplicating reference content and pollutes context for sponsors reading at lower posture than the engagement.

#### Confidence labels missing

Every material claim carries a source and a confidence label in the source-trace section. Customer self-attestation is not the same as corroborated evidence; firm policy assertion is not the same as observed control output. If the source-trace table is sparse or absent, the memo has under-evidenced its claims; redraft.
