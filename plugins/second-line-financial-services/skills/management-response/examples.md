# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## category-iii-bhc-third-party-mria

### Example: management response to a federal banking agency MRIA on third-party risk management

Public-source-derived. No named institution. Framing patterns from FRB SR 13-13 (Communication of Supervisory Findings, June 2013), federal banking agencies' interagency third-party risk management guidance (June 2023), 12 CFR Part 30 Appendix D (OCC Heightened Standards), and FRB SR 12-17 (Consolidated Supervision Framework).

#### Input

- Institution: Category III bank holding company under the FRB tailoring framework. Mid-cap regional, predominantly commercial and consumer banking, with material reliance on a third-party-risk-management platform and an extended population of fourth-party sub-providers.
- Engagement scope supplied: primary regulators FRB and OCC; persona = head of regulatory affairs, second line, working with the head of TPRM and the CRO; sector overlay = banking; cross-cutting overlays = cyber (because two of the three sub-findings touch IT controls); source posture = public-plus-firm-policy-plus-system-of-record-evidence.
- Finding source: Matter Requiring Immediate Attention from the consolidated supervisor following a continuous-monitoring review of the firm's third-party risk management program. Finding text is provided to the firm in the SR-13-13-conformant communication and is to be quoted verbatim in the response.
- Finding sub-elements: (i) inadequate ongoing-monitoring controls for critical fourth-party dependencies; (ii) the absence of an exit-test record for two critical vendors; (iii) insufficient board reporting on third-party concentration.
- Linked artifacts on file: ISS-2025-0418 (TPRM ongoing-monitoring gap); ISS-2025-0427 (exit-test cadence slippage on two named vendors); ISS-2025-0511 (board-reporting third-party concentration gap).
- Acceptance posture: accept in full, settled with the responding role.

#### Output sketch

The skill emits a markdown response and a structured record. Headlines:

- **Cover and addressee** — response date; responding institution (BHC legal entity); addressee = the consolidated supervisor's named office; reference numbers (the supervisor's MRIA ID; internal issue IDs ISS-2025-0418, ISS-2025-0427, ISS-2025-0511); period covered; classification = regulator-confidential. Addressee paragraph follows formal supervisory-letter convention.
- **Executive summary** — five bullets in the head of regulatory affairs voice. Headline: full acceptance; root cause named per sub-finding; 11 milestones over up to 9 months; interim mitigation in place since 30 days post-MRIA receipt; monthly written progress reports to the supervisor until closure; firm-level signatory the General Counsel in addition to the CRO.
- **Finding restatement** — verbatim quotation of the supervisor's wording across the three sub-findings, with the supervisor's numbering preserved.
- **Acceptance posture** — accept for all three sub-findings; rationale brief (no contest).
- **Root cause** — named per sub-finding: (i) the firm's fourth-party identification process did not extend to non-critical-on-paper but operationally critical sub-providers (mechanism: the criticality rubric scored on direct contracted relationship rather than on operational-dependency mapping); (ii) exit-test cadence in policy was annual but had slipped to ad-hoc for the two named vendors (mechanism: exit-test scheduling lived in the vendor-management system as ad-hoc tasks rather than as recurring policy-driven obligations); (iii) the board pack's third-party section did not surface concentration metrics (mechanism: the board pack template was anchored to individual-vendor metrics rather than to portfolio-concentration metrics, and the concentration view existed in a separate management report not promoted to board level).
- **Materiality and impact** — quantified operational-risk exposure from the two named vendors; quantified fourth-party gap (number of operationally-critical sub-providers not covered by the existing identification process); concentration risk currently within RAS but trending toward the trigger; reasonably-foreseeable impact includes RAS breach within two quarters absent remediation. Source trace points to the loss-event log, the operational-risk capital model, and the latest RAS report.
- **Action plan** — 11 milestones across the three sub-findings:
  - Sub-finding (i): 5 milestones over 9 months. Owners: Head of TPRM, CRO, Head of Vendor Management. Dependencies: TPRM platform upgrade scheduled Q4 (named); fourth-party data feed from the platform vendor (named).
  - Sub-finding (ii): 3 milestones over 4 months. Owner: Head of Vendor Management. Dependencies: vendor cooperation on exit-test artifacts (named); business-continuity team availability for exit-test exercises (named).
  - Sub-finding (iii): 3 milestones over 6 months. Owners: Head of TPRM, Head of Risk Reporting, CRO. Dependencies: board-pack template change-control via the committee secretary (named); risk-committee approval of the revised template (named, target Q3 risk-committee meeting).
- **Interim mitigation** — enhanced manual fourth-party review for the highest-criticality vendors completed within 30 days of the MRIA receipt; weekly third-party concentration updates to the CRO from issuance until concentration metrics are in the board pack; restricted on-boarding of new critical vendors pending TPRM platform upgrade.
- **Evidence of effectiveness** — two-consecutive-quarter KRI trend on third-party concentration within RAS; documented exit-test runs for the two named vendors with after-action reports; supervisor walk-through of the upgraded TPRM platform 90 days post-implementation. Owner role = Head of TPRM; re-test cadence after closure = annual TPRM walk-through with the supervisor for two years.
- **Reporting cadence** — monthly written progress reports to the consolidated supervisor's named office until closure; reporting role = Head of TPRM. Closure trigger = two consecutive quarters at GREEN on the relevant KRIs and supervisor-confirmed walk-through completion.
- **Linked issues** — ISS-2025-0418, ISS-2025-0427, ISS-2025-0511. No prior response on this finding ID (this is the initial response; a refresh would carry the slippage commentary).
- **Sign-off block** — responding role = head of regulatory affairs; firm-level signatory = General Counsel (consistent with MRIA convention for the highest-severity supervisory tier); independent reviewer = head of internal audit (challenge function).
- **Confidence label** — high (issues are well-scoped; action plan is dependency-mapped; interim mitigation is in place; all milestones have named owner roles).
- **Reviewer questions** — five questions including: dependency-management for the TPRM platform upgrade; evidence-of-effectiveness method for sub-finding (i) given the platform-upgrade dependency; whether the supervisor walk-through would prefer to review the upgraded platform live or via a structured demonstration; the materiality basis on the fourth-party gap quantification; the closure-trigger negotiation.

The response stops at draft. The General Counsel and the head of regulatory affairs review before the response is sent to the supervisor.

#### Why this scenario matters

- The MRIA tier carries the highest-severity supervisory expectations: monthly written progress reports, board-level attention, a senior firm-level signatory in addition to the responding role. The skill applies these defaults; the responding role can adjust where the supervisor's communication specifies otherwise.
- Root cause is mechanism-anchored per sub-finding, not a paraphrase. Each sub-finding has a named mechanism (criticality-rubric scoring on contracted relationship rather than operational-dependency mapping; exit-test scheduling as ad-hoc rather than recurring; board-pack template anchored on individual-vendor rather than portfolio-concentration metrics).
- Action-plan milestones carry named dependencies. The TPRM platform upgrade is the load-bearing dependency; surfacing it explicitly is what the supervisor reads for. A milestone with a target date but no dependency surfacing reads as brittle.
- Evidence of effectiveness is distinct from evidence of completion. The KRI-trend, exit-test after-action reports, and supervisor walk-through together demonstrate the underlying risk has been reduced; documentation of the redesigned controls alone would be control-completion evidence, not residual-risk-reduction evidence.
- Interim mitigation is in place at the response date. For an MRIA, the supervisor reads for whether the firm has acted on the finding while the action plan completes; a response with no interim mitigation reads as deferral.
- Linked-issue consistency is validated. The schema requires the response root cause to match the linked issue write-up's cause field; mismatch surfaces as a reviewer question.

#### Anchors

- FRB SR 13-13 (Supervisory Considerations for the Communication of Supervisory Findings, June 2013).
- Federal banking agencies' interagency third-party risk management guidance (June 2023).
- 12 CFR Part 30 Appendix D (OCC Heightened Standards), Sections II, III, IV.
- FRB SR 12-17 (Consolidated Supervision Framework for Large Financial Institutions, December 2012).
- IIA International Standards, Standard 2500.A1 (CAE follow-up; informs the response's evidence-of-effectiveness plan and re-test cadence).
- COSO ERM 2017, Review and Revision component.

See `references/source-anchors.md` for full citations and verification flags.

## internal-audit-data-quality-finding

### Example: management response to an internal-audit high-rated finding on data-quality controls

Public-source-derived. No named institution. Framing patterns from BCBS 239 Principles 2 and 3 (Architecture; Accuracy and Integrity), IIA International Standards (2400 series, Standard 2500.A1), and COSO ERM 2017 Review and Revision component.

#### Input

- Institution: large regional bank with material reliance on a credit-loss data warehouse for regulatory reporting (Y-9C, FR Y-14 series, CCAR submissions). The bank is in scope of FRB BCBS 239 supervisory expectations and conducts an annual self-assessment.
- Engagement scope supplied: primary regulator FRB; persona = head of risk reporting, second line, working with the CDO and the head of risk-data engineering; sector overlay = banking; cross-cutting overlays = none (this finding is data-quality-anchored, not cyber, privacy, or conduct); source posture = public-plus-firm-policy-plus-system-of-record-evidence.
- Finding source: high-rated internal-audit finding from the bank's internal audit function, communicated via the audit-report convention with management response due to the audit committee. Finding cites manual reconciliation between two source systems, lack of automated lineage to the regulatory-reporting layer, and absence of a data-quality SLA with the source-system owners.
- Linked artifacts on file: ISS-2025-0301 (manual reconciliation gap); ISS-2025-0312 (lineage gap); the latest BCBS 239 self-assessment which lists these as Principle 2 and Principle 3 priority gaps.
- Acceptance posture: accept, settled with the responding role.

#### Output sketch

The skill emits a markdown response and a structured record. Headlines:

- **Cover and addressee** — response date; responding institution; addressee = Audit Committee of the Board (with copy to the Chief Audit Executive and the CRO); reference numbers (the audit report ID; internal issue IDs ISS-2025-0301, ISS-2025-0312); period covered; classification = internal. Addressee paragraph follows audit-committee memorandum convention.
- **Executive summary** — four bullets in the head of risk reporting voice. Headline: full acceptance; root cause named consistent with the BCBS 239 self-assessment Principle 2 and Principle 3 gaps; 7 milestones over 18 months with the data-platform-upgrade dependency surfaced explicitly; quarterly written progress reports to the audit committee until closure.
- **Finding restatement** — verbatim quotation of the audit-report wording, including the audit team's articulation of the three sub-elements (manual reconciliation, lineage, data-quality SLA).
- **Acceptance posture** — accept; rationale brief (no contest).
- **Root cause** — named consistent with the BCBS 239 gap-assessment Principle 2 (architecture) and Principle 3 (accuracy and integrity) gaps. Mechanism: (a) the credit-loss data warehouse was built on a star-schema design pre-dating the regulatory-reporting layer rebuild, and the manual reconciliation persisted because the two source systems were not integrated at the platform level; (b) lineage to the regulatory-reporting layer was documented in a separate data-catalog tool but not generated automatically from the warehouse build process, so lineage and warehouse drifted; (c) the data-quality SLA was treated as a service-management artifact rather than as a data-governance obligation, so the source-system owners had no data-quality-specific commitment in their service agreements. Cross-reference to ISS-2025-0301 and ISS-2025-0312 for the underlying issue write-ups.
- **Materiality and impact** — quantitative estimate of the risk-data restatements over the prior 12 months attributable to the manual reconciliation gap (number of restatements; aggregate restated value); reasonably-foreseeable impact on the BCBS 239 self-assessment rating if not remediated before the next FRB horizontal review (rating downgrade risk on Principles 2 and 3 from amber to red); reasonably-foreseeable impact on the regulatory-reporting attestation cycle. Source trace points to the restatement log and the BCBS 239 self-assessment.
- **Action plan** — 7 milestones over 18 months:
  - Reconciliation automation: 2 milestones (interim daily-batch reconciliation tool by month 6; full integration via the data-platform-upgrade by month 18). Owner: Head of Risk Data Engineering. Dependency: data-platform-upgrade scheduled completion month 16 (named).
  - Lineage automation: 2 milestones (lineage capture from the warehouse build by month 9; full automated lineage to the regulatory-reporting layer by month 14). Owner: CDO. Dependency: warehouse build-process refactor (named); data-catalog tool API enablement (named).
  - Data-quality SLA: 3 milestones (SLA template approval by month 3; SLA execution with the two named source-system owners by month 6; SLA monitoring dashboard live by month 9). Owner: Head of Risk Reporting. Dependency: source-system owner participation (named); service-management governance approval (named).
- **Interim mitigation** — daily reconciliation reviews with documented sign-off, in place for six months pre-finding (this is a pre-existing compensating control; the response surfaces it); weekly data-quality dashboard to the data-management committee; restricted regulatory-reporting attestation cycle pending automated lineage (manual lineage-pack assembled for each filing, with explicit second-line review).
- **Evidence of effectiveness** — post-implementation, two consecutive months at zero unreconciled items on the daily reconciliation; automated lineage report run weekly for two consecutive quarters with zero broken-lineage exceptions; documented data-quality SLA executed with each source-system owner with quarterly SLA-monitoring dashboard reviewed at the data-management committee. Owner role = head of risk reporting; re-test cadence after closure = annual data-quality-control re-test for two years.
- **Reporting cadence** — quarterly written progress reports to the audit committee until closure; reporting role = head of risk reporting. Closure trigger = two consecutive months at zero unreconciled items, two consecutive quarters of clean automated lineage, and SLAs in force with all source-system owners.
- **Linked issues** — ISS-2025-0301, ISS-2025-0312. **Linked findings** — cross-reference to the BCBS 239 self-assessment Top-5 priority gaps (Principles 2 and 3). No prior response on this finding ID (initial response).
- **Sign-off block** — responding role = head of risk reporting; firm-level signatory = CRO (audit-committee response convention does not require a CEO-level signatory for this severity); independent reviewer = head of internal audit (the issuing party signs off the response receipt at the audit-committee meeting).
- **Confidence label** — medium (the data-platform-upgrade dependency is a known programme risk; the action plan is dependency-mapped but the platform timeline could slip).
- **Reviewer questions** — five questions including: data-platform-upgrade timeline confidence; whether the audit committee would prefer a faster interim reconciliation tool ahead of the full integration; the materiality basis on the restatement-log quantification; the SLA-monitoring dashboard governance; the FRB horizontal review scheduling (whether the response timeline aligns with the expected horizontal review).

The response stops at draft. The CRO and the head of risk reporting review before the response is filed with the audit committee.

#### Why this scenario matters

- The internal-audit response convention is different from the regulator response convention: addressee is the audit committee (not a regulator office), the response is a memorandum (not a formal supervisory letter), the reporting cadence is quarterly to the audit committee (not monthly to a supervisor), and the firm-level signatory is the CRO (not the CEO or General Counsel). The skill applies these defaults.
- Root cause is mechanism-anchored and cross-references the BCBS 239 self-assessment. The response is consistent with the underlying issue write-ups; the schema validates `consistency_with_issue_writeup`.
- Action-plan milestones carry the data-platform-upgrade dependency explicitly. The platform timeline is a programme risk; the response surfaces it rather than burying it inside an aggregate target date.
- Evidence of effectiveness is distinct from evidence of completion. The two-consecutive-month zero-unreconciled-items target, the two-consecutive-quarter clean-lineage target, and the active SLA monitoring together demonstrate the underlying risk reduction; documentation of the redesigned controls alone would not.
- Interim mitigation includes pre-existing compensating controls. The response surfaces the daily reconciliation reviews already in place; this is normal practice when the gap predated the finding and the firm acted on it before formal communication.
- Confidence label is medium because the platform-upgrade dependency is a programme risk. A `high` label would require demonstrably-stable platform-upgrade timeline, which the firm cannot assert.

#### Anchors

- BCBS 239 (January 2013), Principles 2 (Data architecture and IT infrastructure) and 3 (Accuracy and integrity).
- IIA International Standards, Standards 2400 series (Communicating Results) and Standard 2500.A1 (CAE follow-up).
- COSO ERM 2017, Review and Revision component.
- 12 CFR Part 30 Appendix D (OCC Heightened Standards), where applicable to the bank's regulatory framework.
- FRB SR 12-17 (Consolidated Supervision Framework for Large Financial Institutions, December 2012), where the bank's BHC is in scope.

See `references/source-anchors.md` for full citations and verification flags.

## troubleshooting

### Troubleshooting: management-response

Recurring failure modes when a management response looks complete but is not. The reviewer review should catch these; the builder review should preempt them.

#### Finding text paraphrased rather than quoted

Symptom: the finding-restatement section reads as a clean summary of the issuing party's wording, with phrasing softened or simplified.

Why it happens: the builder treats the response as the firm's voice throughout and rewrites the finding for stylistic consistency.

Fix: the finding text is quoted verbatim, with the issuing party's numbering preserved. The schema requires `finding_text_verbatim`. Paraphrasing, even slight, reads as a softening attempt and frequently draws the issuing party's challenge. Where the firm wishes to articulate its understanding of the finding, it does so in the root-cause section, not in the restatement.

#### Root cause paraphrases the finding

Symptom: a finding that says "the firm's third-party-risk-management ongoing-monitoring controls are inadequate for critical fourth-party dependencies" is paired with a root cause that says "ongoing monitoring of fourth parties is inadequate".

Why it happens: builder treats root cause as a re-statement of the gap rather than as a mechanism-anchored explanation of why the gap occurred.

Fix: the root cause is named and mechanism-anchored. What in the firm's process produced the gap? The fourth-party identification process did not extend to operationally-critical sub-providers because the criticality rubric scored on direct contracted relationship. The exit-test cadence had slipped to ad-hoc because exit-test scheduling lived in the vendor-management system as ad-hoc tasks rather than as recurring policy-driven obligations. The board pack did not surface concentration metrics because the template was anchored on individual-vendor metrics. The schema validates `consistency_with_issue_writeup`; mismatch surfaces as a reviewer question.

#### Action-plan milestones with no dependencies

Symptom: a 12-month milestone with a single target date and no dependency surfacing. The supervisor reads it, asks "what does this depend on?", and the response cannot answer.

Why it happens: dependency-mapping requires conversation across functions and is often deferred; the builder lists target dates without surfacing the underlying dependencies.

Fix: every milestone carries either named dependency identifiers (other milestones, named system upgrades, named vendor cooperation, named regulatory approvals) or the explicit assertion `no_external_dependencies = true`. The schema enforces this. A milestone without dependencies is brittle and frequently slips.

#### Evidence of completion conflated with evidence of effectiveness

Symptom: the response treats "policy approved", "training delivered", "control documented", "attestation collected" as evidence the underlying risk has been resolved.

Why it happens: control-completion evidence is what the firm's testing function and project-management function track, and that material is at hand; residual-risk-reduction evidence requires post-implementation observation that the builder may not yet have.

Fix: the evidence-of-effectiveness plan is a separate object in the schema. It names the method (control-test, KRI-trend, external-validation, supervisor-walk-through), the period over which the evidence will be observed (commonly two consecutive quarters or two consecutive monthly readings), and the owner role for the evidence run. Completing an action is not the same as resolving the underlying risk; the evidence-of-effectiveness plan is the principal control on action-completed-without-risk-resolved closure.

#### Acceptance posture without rationale

Symptom: the response carries `partially-accept` or `contest` in the acceptance posture without naming who approved the partial acceptance or contest, on what basis, or with what evidence of approval.

Why it happens: the partial-acceptance or contest decision was settled informally and the formal risk-acceptance approval was not documented.

Fix: the schema requires `risk_acceptance` (with `decision_maker`, `rationale`, `approval_evidence`) when `acceptance_posture` is `partially-accept` or `contest`. The acceptance posture cannot be drafted around; it has to be settled with the responding role and documented before the response goes out. The skill stops if the posture is not settled.

#### Reporting cadence missing or vague

Symptom: the response says "we will keep the supervisor informed" or "we will report progress on a regular basis".

Why it happens: builder defers the cadence specification, expecting the issuing party to specify it.

Fix: the response names a specific frequency (monthly, quarterly, semi-annual, annual, event-driven), a specific form (written-progress-report, committee-update, supervisory-meeting, on-request), and a specific reporting role. Defaults flex by finding tier; the absence of a named cadence does not. The skill applies tier-specific defaults from the relevant sector overlay (e.g., monthly for the highest-severity supervisory tier).

#### Confidence-label inflation

Symptom: confidence label is `high` while the action plan has unresolved dependencies, milestones with personal names instead of role owners, or no interim mitigation in place.

Why it happens: confidence label is treated as a brand statement rather than as an executability statement.

Fix: confidence label reflects the executability of the action plan, not the desirability of the outcome. A `high` label requires named owner roles on every milestone, dependency-mapped milestones, and demonstrable interim mitigation. Where any of these is absent, the label is medium at best. The skill enforces this; the reviewer review catches it where the skill misses.

#### Stale prior-response history

Symptom: the response is a refresh of a prior response on the same finding ID, but the prior commitment, the slippage, and what changed are not surfaced. The supervisor reads the new commitment as a fresh start.

Why it happens: builder treats the new response as a clean draft, not as a continuation. The prior-response history lives in a separate file or in the regulatory-affairs team's notes.

Fix: where a prior response exists on the same finding ID, the current response surfaces the prior commitment, the slippage, and what changed. The schema enforces `prior_response_history` with the slippage description on refreshes. Silently revising the prior commitment fails the supervisor's expectation that the firm manages, not just counts, the open population.

#### MRA and MRIA treated identically

Symptom: an MRIA response carries the same reporting cadence, the same firm-level signatory, and the same action-plan envelope as an MRA response.

Why it happens: builder treats severity as a finding-text concern rather than as a workflow-defaults concern.

Fix: the banking sector overlay applies tier-specific defaults; MRIA carries monthly written progress reports, a senior firm-level signatory (typically CEO or General Counsel), board-level attention, a tighter action-plan envelope, and an evidence-of-effectiveness method that typically includes a supervisor walk-through. MRA defaults are quarterly cadence, CRO or process-owner signatory, risk-committee notification rather than board-level attention. The skill applies the defaults; the responding role can adjust where the supervisor's specification differs.

#### Personal names in the addressee or signatory blocks

Symptom: the addressee or signatory blocks name a specific examiner or a specific firm executive by personal name.

Why it happens: builder uses the most recent correspondence for context and pulls personal names directly.

Fix: the convention across all sectors is roles, not personal names. Personnel rotate; the response may be filed and read months or years after issue. The schema requires owner and signatory fields to be roles. The reviewer review catches personal-name leakage.

#### Linked-issue inconsistency

Symptom: the response root cause says one thing; the linked issue write-up says another. The supervisor reads both and asks why.

Why it happens: the issue write-up was authored separately and the response was drafted without re-reading it; the two artifacts drifted.

Fix: the schema requires `consistency_with_issue_writeup` to be set explicitly. Where it is `false`, the response surfaces the divergence as a reviewer question and the responding role decides whether the issue write-up needs revision or the response root cause needs adjustment.

#### Customer-remediation strand omitted on consumer-protection findings

Symptom: a CFPB or state-attorney-general finding response treats the matter as a control-redesign issue without addressing remediation owed to affected consumers.

Why it happens: builder treats the finding as a process gap rather than as a customer-impact event.

Fix: the conduct cross-cutting overlay (`references/cross-cutting.md#conduct`) and the payments-fintech sector overlay both flag this. Where customers were affected, the response carries both the control-redesign strand and the customer-remediation strand: affected-population identification methodology, restitution methodology, restitution delivery, customer-remediation reporting cadence.

#### Cyber evidence-of-effectiveness limited to "policy and training"

Symptom: cyber finding response evidence-of-effectiveness method is "training delivered to all affected staff" or "policy revision approved and disseminated".

Why it happens: builder reaches for the evidence that is in hand at the response date.

Fix: cyber findings turn on whether the redesign actually reduced the underlying risk. The evidence-of-effectiveness plan must distinguish control-completion evidence (policy, training, attestations) from residual-risk-reduction evidence (KRI trend showing reduced incident rate or improved MTTR; control-test results showing the control operating as designed; threat-emulation or red-team results showing the control resists realistic attack patterns). The cyber cross-cutting overlay covers the named methods.

#### Counsel review missing on enforcement-referral indicators

Symptom: the response is drafted and ready for submission on a deficiency letter that contains language signaling possible enforcement consideration. Securities counsel has not reviewed.

Why it happens: builder treats the response as a routine artifact when the underlying communication is not routine.

Fix: where the deficiency letter contains enforcement-referral indicators (typical SEC EXAMS or FINRA language; CFPB PARR letter convention; explicit statement of possible enforcement consideration), securities counsel review is typical and the skill flags this. The skill stops if the responding role has not engaged counsel.

#### Response stops too late

Symptom: the skill produces and files the response with the issuing party, marks the response as sent, asserts sign-off without evidence.

Why it happens: builder over-runs the human-review gate.

Fix: the response is a draft until the responding role and (where applicable) the firm-level signatory attest. The skill stops at the draft and surfaces the reviewer questions; it does not assert sign-off, send to the issuing party, or post to the response-file folder.
