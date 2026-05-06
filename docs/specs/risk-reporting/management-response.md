# management-response — spec sheet

Plugin: `risk-reporting`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Drafts the management response to a regulator finding, audit finding, or self-identified issue: acceptance posture, root cause acknowledgement, action plan with milestones, owner, target completion, evidence of effectiveness, and reporting cadence to the issuing party. Output is a named-section response a CRO, head of compliance, head of audit, or general counsel can take to the regulator or audit committee after qualified review.

Best for:
- Drafting the management response to an MRA (Matter Requiring Attention) or MRIA (Matter Requiring Immediate Attention) from FRB, OCC, FDIC, or NYDFS in the formal letter format the regulator expects.
- Drafting the management response to an internal audit finding for the audit committee response file.
- Drafting the management response to an external assessor finding (SOC auditor, IIA peer review, third-party regulatory engagement).
- Drafting the management response to a CFPB MRA or supervisory letter, an SEC examination deficiency, or a FINRA exam finding.
- Refreshing a prior management response where remediation has slipped or scope has changed and an updated commitment is required.

Not the right tool when:
- The artifact is the underlying issue write-up (use `risk-compliance-core/skills/issue-writeup`; this skill consumes its output).
- The artifact is the standing committee pack tracking issue ageing (use `risk-committee-pack`; the issues-and-remediation-status section there summarizes the response posture across all open issues).
- The artifact is a public regulator response that is part of a published enforcement action (these are securities-counsel-led; this skill is the second-line draft, not the final published response).
- The artifact is the annual SOX 404 management's report on internal control (out of scope; that is securities-counsel-led).
- The work is enforcement-action negotiation. Where the matter has escalated to a formal enforcement action, securities counsel and outside counsel lead; this skill is for second-line responses to MRAs/MRIAs and audit findings, not consent orders.

Anchored to: FRB SR 13-13 (Supervisory Considerations for the Communication of Supervisory Findings, June 2013) [verify] for the FRB MRA/MRIA framework; OCC Comptroller's Handbook on Bank Supervision Process [verify section]; OCC PPM 5310-3 (Bank Supervision Operations: Communicating Examination Findings) [verify]; FDIC Risk Management Manual of Examination Policies [verify section]; NYDFS Industry Letters and supervisory finding communications; IIA International Standards for the Professional Practice of Internal Auditing (Standard 2500.A1 — Monitoring Progress) [verify]; PCAOB AS 2201 paragraphs on management's response to identified deficiencies [verify pin cite].

## Source anchors

Primary:
- FRB SR 13-13 — Supervisory Considerations for the Communication of Supervisory Findings, June 17, 2013. Use for: the MRA/MRIA distinction, the communication framework, and the supervisory expectation on management response (timeliness, ownership, action plan with milestones). [verify section labels.]
- OCC PPM 5310-3 — Bank Supervision Operations: Communicating Examination Findings (or successor; verify current PPM number). Use for: OCC-specific findings communication framework and the management-response posture OCC expects.
- OCC Comptroller's Handbook on Bank Supervision Process. Sections to cite: chapters on findings communication and corrective actions [verify section labels]. Use for: the supervisory expectation chain.
- FDIC Risk Management Manual of Examination Policies. Sections to cite: examination findings and corrective actions [verify section labels]. Use for: FDIC-specific framework.
- NYDFS supervisory communications. Use for: NYDFS-specific MRA/MRIA-equivalent finding communication, especially under Part 500 examinations.
- IIA International Standards for the Professional Practice of Internal Auditing — Standard 2500 (Monitoring Progress) and 2500.A1 (CAE follow-up). Use for: internal-audit finding-response framework and follow-up reporting cadence.
- PCAOB AS 2201 — Audit of Internal Control Over Financial Reporting. Paragraphs on identified material weaknesses and significant deficiencies, and management's response. Use for: external-audit finding-response framing where the finding affects ICFR.

Secondary (overlay only):
- COSO ERM 2017 — Performance and Review and Revision components. Use for: framing how the management response integrates with ongoing risk monitoring.
- Three Lines Model (IIA 2020 revision). Use for: clarifying the three-lines roles in a management response (first line owns the action plan; second line provides challenge and oversight; third line monitors).

## Sector overlays needed

- `banking.md` — Required and primary. The MRA/MRIA framework is banking-anchored. Covers FRB / OCC / FDIC nuance on findings communication, the connection to CAMELS / RFI ratings, and the FRB SR 12-17 Consolidated Supervision Framework expectations on issue tracking for LFIs.
- `insurance.md` — Covers state DOI examination findings communication (varies by state), NAIC peer review findings, and the linkage to the Insurance Holding Company System Regulatory Act risk-reporting expectations.
- `capital-markets.md` — Covers SEC OCIE / EXAMS deficiency letter responses, FINRA exam finding responses (under FINRA Rule 8210 information requests when they accompany), and CFTC examination finding responses for FCMs and SDs.
- `payments-fintech.md` — Covers CFPB supervisory finding communications (PARR — Potential Action and Request for Response), state money-transmitter examination findings, and OCC bank-partnership examination findings that may flow through to the fintech via the sponsor bank.

## Cross-cutting overlays needed

- `cyber.md` — Optional, frequently invoked. Cyber findings (NYDFS Part 500 examination findings, FFIEC IT booklet findings, federal-banking-agency cyber findings) are common subjects of management response. The overlay covers cyber-specific evidence-of-effectiveness expectations (e.g., evidence that a control redesign actually reduces the residual risk, not just that the control was reissued).
- `climate.md` — Not required at v1. Climate-specific regulator findings remain rare in the US; where the firm is in scope, climate findings are typically covered as part of risk-management or risk-reporting findings under existing supervisory frameworks.
- `privacy.md` — Optional. Privacy findings (GLBA Safeguards Rule, state privacy-law-related findings, Reg P findings) appear at firms with consumer-facing businesses.
- `conduct.md` — Optional. Conduct findings (CFPB UDAAP findings, fair-lending findings, FINRA conduct findings) appear at firms with consumer or retail-investor businesses.

## Output template named sections

The template is regulator-finding-shaped. Internal-audit and external-assessor variants reuse the same shape with different cover and addressee.

Top of artifact:
- Cover: response date, responding institution, addressee (regulator office / audit committee / external assessor), reference numbers (regulator finding ID, internal issue ID, audit report reference), period to which the finding relates, classification
- Addressee paragraph (formal salutation, regulator-letter convention)
- Executive summary (3-5 bullets, CRO or attesting role's voice)

Body:
- Finding restatement (the regulator's or auditor's wording, quoted exactly; deviation from the original wording is a frequent challenge from regulators)
- Acceptance posture (accept / partially accept / contest, with rationale; "accept" is the most common but not the only valid posture)
- Root cause acknowledgement (named root cause; not a paraphrase of the finding; consistent with the linked issue write-up)
- Materiality and impact statement (current and reasonably foreseeable)
- Action plan with milestones (one row per milestone: action description, owner, target date, dependency, evidence of completion expected)
- Interim mitigation (steps already taken before the formal response date; any compensating controls in place pending full remediation)
- Evidence-of-effectiveness plan (how the firm will demonstrate, post-remediation, that the action has actually closed the underlying risk; not just that the action has been completed)
- Reporting cadence to the issuing party (frequency and form of progress reports; named reporting role)
- Linked issues and dependencies (foreign keys to `issue.schema.json` and to other open findings that may share root cause or remediation actions)
- Risk acceptance (where partial acceptance or contest applies; named decision-maker, named rationale, named approval evidence)

Tail:
- Sign-off block (the responding role; the firm-level signatory if applicable, e.g., CEO or General Counsel for a regulator response; date)
- Source trace per material claim (especially the materiality and impact statements, which are often challenged on evidence)
- Confidence label (high / medium / low / unknown)
- Reviewer questions (questions the responding role expects from the regulator or audit committee follow-up)

## Structured output fields

Schema to add in phase 2: `management-response.schema.json`. Reuses `issue.schema.json` (existing) for finding linkage.

Wrapper object:
- `response_id`: string. Stable ID.
- `response_date`: string. ISO date.
- `responding_institution`: string.
- `addressee`: object. `addressee_type` (enum: regulator / audit-committee / external-assessor), `addressee_name` (string; e.g., "OCC Northeast District", "Audit Committee of the Board", "Internal Audit", "External Auditor"), `addressee_reference_number` (string).
- `finding_reference`: object. `finding_id` (string; the regulator's or auditor's identifier), `finding_type` (enum: mra / mria / audit-finding-high / audit-finding-medium / audit-finding-low / external-assessor-finding / parr / soc-exception / self-identified-issue / other), `finding_text_verbatim` (string; the regulator's or auditor's wording, quoted), `finding_communication_date` (ISO date).
- `acceptance_posture`: enum. `accept` / `partially-accept` / `contest`.
- `acceptance_rationale`: string. Required when posture is `partially-accept` or `contest`; optional when `accept`.
- `root_cause`: object. `root_cause_named` (string), `linked_issue_id` (foreign key to `issue.schema.json`; required), `consistency_with_issue_writeup` (boolean; phase 2 validates).
- `materiality_and_impact`: object. `current_impact` (string), `reasonably_foreseeable_impact` (string), `quantitative_estimate` (string or null).
- `action_plan_milestones`: array of objects with `milestone_id`, `action_description`, `owner` (role), `target_date` (ISO date), `dependency_ids` (array), `evidence_of_completion_expected` (string).
- `interim_mitigation`: array of strings. Steps already taken pending full remediation.
- `evidence_of_effectiveness_plan`: object. `evidence_method` (enum: control-test / kri-trend / external-validation / regulator-walk-through / other), `evidence_period_post_remediation` (string; e.g., "two consecutive quarters at GREEN"), `evidence_owner` (role).
- `reporting_cadence`: object. `frequency` (enum: monthly / quarterly / semi-annual / annual / event-driven / other), `form` (enum: written-progress-report / committee-update / supervisory-meeting / on-request), `reporting_role` (string).
- `linked_issue_ids`: array of strings.
- `linked_finding_ids`: array of strings.
- `risk_acceptance`: object or null. Present when `acceptance_posture` is `partially-accept` or `contest`. Subfields: `decision_maker` (role), `rationale` (string), `approval_evidence` (string).
- `signed_by_role`: string.
- `signed_date`: string or null. ISO date.
- `confidence_label`: enum. `high` / `medium` / `low` / `unknown`.
- `human_review_required`: boolean. Always true for v1.

## Example scenarios

### Scenario 1: Management response to an FRB MRIA on third-party-risk-management

Input: a Category III BHC has received an MRIA from the FRB on third-party-risk-management following a continuous-monitoring review. The MRIA identifies (i) inadequate ongoing-monitoring controls for critical fourth-party dependencies, (ii) the absence of an exit-test record for two critical vendors, and (iii) insufficient board reporting on third-party concentration. Source posture: FRB SR 13-13 (MRA/MRIA framework), U.S. interagency third-party risk management guidance (June 2023), the firm's third-party policy, and the linked internal issue write-ups. The firm accepts the MRIA in full.

Output emphasizes:
- Finding restatement quotes the MRIA verbatim across the three sub-findings.
- Acceptance posture: `accept` for all three sub-findings.
- Root cause is named per sub-finding: (i) the firm's fourth-party identification process did not extend to non-critical-on-paper but operationally critical sub-providers; (ii) exit-test cadence in the firm's policy was annual but had slipped to ad-hoc for the two named vendors; (iii) the board pack's third-party section did not surface concentration metrics, only individual-vendor metrics.
- Materiality and impact: the firm quantifies the operational-risk exposure from the two named vendors and the fourth-party gap, and flags the concentration risk as currently within the RAS but trending toward the trigger.
- Action plan milestones: 11 milestones across the three sub-findings, with named owners (Head of Vendor Management, Head of Third-Party Risk, CRO), target dates, dependencies (system implementation for fourth-party identification depends on the third-party-risk-management platform upgrade scheduled Q4), and evidence-of-completion expectations.
- Interim mitigation: enhanced manual fourth-party review for the highest-criticality vendors, completed within 30 days of the MRIA receipt; weekly third-party concentration updates to the CRO.
- Evidence of effectiveness: two-consecutive-quarter KRI trend on third-party concentration within RAS; documented exit-test runs for the two named vendors with after-action reports; and a regulator walk-through of the upgraded platform 90 days post-implementation.
- Reporting cadence: monthly written progress reports to the FRB Northeast District until closure, owned by the Head of Third-Party Risk.
- Linked issues: ISS-2025-0418, ISS-2025-0427, ISS-2025-0511.
- Confidence label: high (issues are well-scoped and the action plan is dependency-mapped).
- Human review required: yes; the response goes to the CRO, General Counsel, and the Risk Committee Chair before submission.

### Scenario 2: Management response to an internal-audit high-rated finding on data-quality controls

Input: internal audit has issued a high-rated finding on data-quality controls in the credit-loss data warehouse, citing manual reconciliation between two source systems, lack of automated lineage to the regulatory-reporting layer, and absence of a data-quality SLA with the source-system owners. Source posture: BCBS 239 Principles 3 and 4 [verify pin cites], the firm's risk-data policy, and the linked issue write-ups; the finding is consistent with the BCBS 239 self-assessment Top-5 priority gaps. The Head of Risk Reporting accepts the finding and is the responding role.

Output emphasizes:
- Finding restatement quotes the audit-report wording verbatim.
- Acceptance posture: `accept`.
- Root cause: named consistent with the BCBS 239 gap-assessment Principle 2 and Principle 3 gaps; explicit cross-reference to ISS-2025-0301 (manual reconciliation) and ISS-2025-0312 (lineage gap).
- Materiality and impact: quantitative estimate of the risk-data restatements over the prior 12 months attributable to the manual reconciliation gap; reasonably foreseeable impact on the BCBS 239 self-assessment rating if not remediated before the FRB horizontal review.
- Action plan milestones: 7 milestones over 18 months, with the data-platform-upgrade dependency surfaced explicitly. Owners: Head of Risk Reporting, CDO, Head of Risk Data Engineering.
- Interim mitigation: daily reconciliation reviews with documented sign-off, in place for six months pre-finding; weekly data-quality dashboard to the data-management committee.
- Evidence of effectiveness: post-implementation, two consecutive months at zero unreconciled items; automated lineage report run weekly for two consecutive quarters; documented data-quality SLA executed with each source-system owner.
- Reporting cadence: quarterly written progress reports to the Audit Committee until closure, owned by the Head of Risk Reporting; with status escalation to the FRB if not on-track when the horizontal review is scheduled.
- Linked issues: ISS-2025-0301, ISS-2025-0312.
- Linked findings: links to the BCBS 239 self-assessment Top-5 priority gaps as a cross-reference.
- Confidence label: medium (the platform-upgrade dependency is a known programme risk).
- Human review required: yes; the response goes to the CDO, the CRO, and the Audit Committee Chair before submission.

## Common pitfalls

1. Paraphrasing the finding. Phase 2 must require the finding text verbatim. Regulators and auditors are sensitive to subtle paraphrasing that softens the original wording.
2. Action plan without dependencies. A milestone with a target date but no dependency map (system upgrade prerequisite, vendor delivery, regulatory approval) is brittle and frequently slips. Phase 2 must require dependency identification or an explicit "no dependencies" assertion.
3. Root cause = restatement of finding. The root cause must be a named, mechanism-anchored statement of why the finding occurred. Phase 2 must reject root-cause statements that paraphrase the finding without identifying the underlying mechanism.
4. Evidence of completion ≠ evidence of effectiveness. Completing an action is not the same as resolving the underlying risk. Phase 2 must require an evidence-of-effectiveness plan distinct from the action-completion evidence.
5. Acceptance posture without rationale. `partially-accept` or `contest` postures must carry named rationale and a named risk-acceptance approval. Phase 2 must reject these postures without `risk_acceptance` populated.
6. Reporting cadence missing. Regulators expect named reporting cadence to closure, not "we will keep you informed". Phase 2 must require a named frequency and form of report.
7. Confidence-label inflation. The confidence label here reflects the executability of the action plan, not the desirability of the outcome. A `high` confidence label requires named owners, dependency-mapped milestones, and demonstrable interim mitigation. Phase 2 must reject `high` where any of these is missing.
8. Stale prior responses. Phase 2 must check for prior response history on the same finding ID; where a prior response exists and remediation has slipped, the current response must explicitly acknowledge the slippage and explain the changed commitment.
9. Treating MRA and MRIA as the same. MRIA carries a higher supervisory expectation (more rapid response, board-level attention). Phase 2 must enforce different defaults for MRIA vs MRA on reporting cadence (typically monthly for MRIA, quarterly for MRA) and on signed_by_role (typically CEO or General Counsel for MRIA, CRO or process-owner for MRA).
10. Linked-issue inconsistency. The response's root cause and the underlying issue write-up must be consistent. Phase 2 must validate `consistency_with_issue_writeup` and surface inconsistency as a reviewer question.
