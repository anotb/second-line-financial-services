# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## bcbs239-completeness-exception

### Example: BCBS 239 risk-reporting completeness exception

#### Input

The internal audit team at a $40B regional bank (foreign banking organization, US IHC) has tested the monthly market-risk pack against BCBS 239 Principle 4 (completeness) for the period 2026-01 through 2026-03. Two material counterparty exposures totalling $187M notional were excluded from the consolidated counterparty view on three reporting cycles because the upstream feed cutoff time preceded the source-system close on the affected days. The internal audit team has confirmed the condition with the Credit Risk Reporting team and is writing up the issue. Persona is the Internal Audit Senior Manager (3-line independent), audience is the firm's Audit Committee with a copy to the Board Risk Committee. Source posture is mixed: BCBS 239 (public) and the firm's risk-data-aggregation policy (firm-policy overlay).

#### Why this scenario matters

This is the canonical CCCE construction on a risk-data finding. The condition is dated, scoped, and quantified. The criteria is BCBS 239 Principle 4 with a section reference, not "per BCBS 239 generally". The cause is the feed-orchestration cutoff time tied to a specific control attribute (the reconciliation control that did not catch the truncated population), not "feed timing issue". The effect quantifies the under-stated counterparty exposure and notes the downstream propagation into the executive risk pack distributed to the Board Risk Committee. The example also tests the discipline that severity is paired with rationale, that closure evidence is the artifact and not the verb, and that the source-source-anchors path is referenced rather than restated.

#### Output sketch

```yaml
issue_id: ISS-2026-IA-BCBS239-007
title: "Counterparty exposure feed truncation excludes material exposures from monthly market-risk pack on three cycles"
engagement_id: ENG-2026-IA-BCBS239-MarketRisk
as_of_date: 2026-04-22
status: under-review

source:
  source_type: internal-audit
  source_id: IA-WP-2026-MR-014
  # regulator omitted; not examiner-issued

date_identified: 2026-04-15
period_start: 2026-01-01
period_end: 2026-03-31

condition: |
  On three monthly reporting cycles (2026-01, 2026-02, 2026-03), two material counterparty
  exposures totalling $187M notional were excluded from the consolidated counterparty view in
  the monthly market-risk pack. The upstream feed cutoff time (T+1 04:00 ET) preceded the
  source-system close (T+1 06:00 ET) on those three cycles because of a quarterly batch-window
  shift the feed-orchestration team applied without adjusting the downstream cutoff. The two
  exposures appeared in the counterparty source system before the source-system close but after
  the feed cutoff. The reconciliation control between the source-system extract and the pack
  input did not catch the truncated population because the reconciliation runs against the post-cutoff
  feed file, not against the source-system close.

criteria: |
  BCBS 239 Principle 4 (Completeness) — risk data aggregation capabilities should capture and
  aggregate all material risk data across the banking group, with exceptions identified and
  explained. BCBS 239 Principle 7 (Accuracy) — risk reports should accurately and precisely
  convey aggregated risk data. Firm Risk Data Aggregation and Reporting Policy v4.2 §3.2 on
  data-completeness controls and §3.4 on reconciliation discipline.
criteria_source_anchor: "references/source-anchors.md#bcbs-239 and references/firm-overlay.md#rdar-policy-v42"

cause: |
  The reconciliation control (C-CRR-001) is designed to compare the pack input file against
  the post-cutoff feed file rather than against the source-system close-of-day position. When
  the feed cutoff and the source-system close diverge, the reconciliation control passes against
  a truncated population without flagging the truncation. The control's design assumes the feed
  cutoff equals the source-system close; that assumption became false when the feed-orchestration
  team shifted the batch window without coordinating with the reconciliation control owner.

impact: |
  Financial: counterparty exposure under-stated by $187M notional on three reporting cycles in
  Q1 2026; the under-statement propagated into the monthly market-risk pack distributed to the
  Board Risk Committee on 2026-02-05, 2026-03-05, and 2026-04-05. Regulatory: the firm's
  compliance posture on BCBS 239 Principle 4 is impaired for the affected period; the open
  point will surface in the next OCC continuous-monitoring review of risk-data aggregation.
  Operational: re-issuance of the affected packs is required for the audit committee's record;
  the firm's BCBS 239 self-assessment for 2026-H1 will reflect a partially-effective rating on
  Principle 4. No customer or reputational impact identified.

severity: high
severity_rationale: |
  High because the condition is recurring (three cycles), the materiality is above the firm's
  published market-risk reporting threshold ($100M notional), the affected pack is consumed by
  the Board Risk Committee, and there is no compensating control that would have surfaced the
  truncation before pack distribution. Not critical because the under-statement is identified
  and quantifiable, the source data was correct (only the feed was truncated), and remediation
  is straightforward (re-align the feed cutoff with the source-system close).
compensating_controls: []

# mra_mria_classification omitted; source is internal-audit, not examiner-letter

population_size: 3
sample_size: 3
exceptions_observed: 3
sampling_methodology: population-based

linked_obligation_ids: [OBL-BCBS239-P04, OBL-BCBS239-P07]
linked_control_ids: [C-CRR-001]
linked_evidence_ids: [EV-2026-IA-MR-014-A, EV-2026-IA-MR-014-B, EV-2026-IA-MR-014-C]

recommendation: |
  The Head of Credit Risk Reporting must (1) re-align the upstream feed cutoff with the
  source-system close-of-day position and document the re-aligned cadence, (2) redesign the
  reconciliation control C-CRR-001 to compare against the source-system close rather than
  against the post-cutoff feed file, and (3) re-issue the three affected monthly packs to the
  Board Risk Committee with a corrected counterparty view and a written explanation of the
  truncation and remediation.

remediation: |
  Three-part remediation: feed-cutoff re-alignment, control redesign, and pack re-issuance.
  The control redesign is the structural fix; the re-alignment is the immediate operational
  fix; the re-issuance is the audit-trail closure.

owner: "Head of Credit Risk Reporting"
target_date: 2026-07-15
remediation_milestones:
  - {date: 2026-05-15, milestone: "Feed cutoff re-aligned and one-cycle reconciliation evidenced", owner: "Head of Credit Risk Reporting"}
  - {date: 2026-06-15, milestone: "Reconciliation control C-CRR-001 redesign signed off by Head of Market Risk Reporting", owner: "Head of Credit Risk Reporting"}
  - {date: 2026-07-15, milestone: "Three affected packs re-issued to Board Risk Committee", owner: "Head of Credit Risk Reporting"}

closure_evidence:
  - "Feed-orchestration runbook with revised cutoff schedule and documented coordination with reconciliation control owner"
  - "Two consecutive months of reconciled feed output against source-system close, with sign-off log retained in GRC platform"
  - "Re-issued monthly market-risk packs (2026-01, 2026-02, 2026-03) with corrected counterparty view and committee acknowledgement"
  - "Updated control documentation for C-CRR-001 reflecting redesigned reconciliation boundary"

interim_mitigation: |
  Manual completeness check by Credit Risk Reporting analyst against source-system close-of-day
  counterparty position before each pack distribution, until the structural fix is signed off.
  Evidenced by analyst sign-off log retained in the GRC platform. The interim check is not the
  remediation; it keeps risk down while the redesign lands.

evidence_gap: false

confidence_label: high

reviewer_questions:
  - "Should the reconciliation control redesign also cover the credit-risk pack and the liquidity-risk pack, or are those packs sourced via different feeds with different cutoff alignment? The audit work scoped the market-risk pack only."
  - "Does the firm's BCBS 239 self-assessment process surface this issue automatically into the next semi-annual self-assessment, or does the Head of Credit Risk Reporting need to file a separate input?"
  - "Is the 2026-07-15 target date acceptable to the Audit Committee given the three-cycle re-issuance scope, or should the re-issuance be accelerated?"

human_review_required: true

revisions:
  - {date: 2026-04-22, reason: initial write-up, delta: created from IA-WP-2026-MR-014, approved_by: "Internal Audit Senior Manager"}
```

#### What the write-up surfaces

- The condition is dated, scoped, and quantified ("three monthly cycles", "$187M notional", "T+1 04:00 ET feed cutoff vs T+1 06:00 ET source-system close"). It reads as the observable state, not as a conclusion about the control.
- The criteria names BCBS 239 Principles 4 and 7 with section references and points back to `references/source-anchors.md` for the citation excerpt; the firm-policy criterion names the policy version and section and points to `references/firm-overlay.md`. The reviewer can read the criterion, not just take the author's word for it.
- The cause names the specific control attribute that failed (the reconciliation control's comparison boundary). It is not "feed timing issue" or "human error".
- The effect quantifies the under-statement, names the downstream pack, identifies the regulatory exposure (next OCC continuous-monitoring review), and explicitly notes no customer or reputational impact. The effect is not inflated past the evidence.
- Severity is paired with rationale referencing materiality (against the firm's $100M threshold), frequency (three cycles), audience (Board Risk Committee consumption), and the absence of compensating controls. The "not critical" reasoning is also given, which keeps the severity calibration defensible.
- Closure evidence is the artifact: the runbook, the reconciliation output, the re-issued packs, the updated control documentation. "Remediated" does not appear.
- Interim mitigation is named separately. The manual completeness check is the mitigation; it is not the remediation.
- Reviewer questions are tied to specific elements (scope of the redesign, BCBS 239 self-assessment seam, target-date defensibility), not generic prompts.
- The structured record consumes the upstream `obligation-mapping` IDs (OBL-BCBS239-P04, OBL-BCBS239-P07) and the `control-matrix` ID (C-CRR-001), so downstream skills (exception-analysis, risk-committee-pack, control-matrix) can pick the issue up by foreign key.

#### Downstream uses

- The exception-analysis chain in `compliance-testing` consumes `severity`, `linked_control_ids`, and `closure_evidence` to ladder this exception into the testing program; control C-CRR-001 moves to the top of the next test cycle until the redesign is evidenced.
- `risk-committee-pack` reads `severity`, `mra_mria_classification`, `evidence_gap`, and `target_date` for the open-issues section of the next Board Risk Committee pack.
- `control-matrix` reads `linked_control_ids` to surface ISS-2026-IA-BCBS239-007 against the C-CRR-001 row in the credit-risk-reporting matrix; the open issue's severity downgrades the control's operating-effectiveness rating until closure.
- The Audit Committee response file references `issue_id`, `condition`, `criteria`, and `target_date` directly when responding to the audit committee's standing question on open material findings.

## tprm-vendor-soc2-finding

### Example: TPRM critical-vendor SOC 2 qualified-opinion finding

#### Input

The Vendor Risk Management team at a mid-sized broker-dealer (registered with the SEC and FINRA, also state-licensed in 38 states) has received the most recent SOC 2 Type II report for its critical fraud-screening vendor (the vendor screens 100% of new account openings and a sample of high-risk transactions). The SOC 2 Type II report covers the period 2025-04-01 through 2026-03-31 and carries a qualified opinion on Trust Services Criterion CC6.1 (logical access). The qualifying paragraph notes that during the audit period the vendor's privileged-access reviews were not performed at the contractually committed quarterly cadence on two of four quarters. The firm has no documented compensating control on its side. The Head of Vendor Risk has confirmed the condition with the vendor's customer-success team and is writing up the issue. Persona is the Head of Vendor Risk Management (2-line independent), audience is the Vendor Risk Committee with a copy to the Operational Risk Committee. Source posture is mixed: Interagency Guidance on Third-Party Relationships and NYDFS Part 500 (public), and the firm's third-party policy (firm-policy overlay).

#### Why this scenario matters

Vendor-monitoring exceptions are the most common second-line finding in many firms; the SOC 2 qualified-opinion case is the canonical version. The example tests the discipline that vendor findings name the specific Trust Services Criterion, that the firm-side compensating control is itself a control attribute under review, and that severity is calibrated against vendor criticality, customer-data exposure, and the absence of a compensating control. It also tests the cyber cross-cutting overlay: the criterion is a cyber-tagged finding, and the criteria section pulls from both the TPRM source anchors and the cyber overlay.

#### Output sketch

```yaml
issue_id: ISS-2026-VRM-Vendor-Atlas-014
title: "Critical fraud-screening vendor SOC 2 Type II qualified opinion on logical access (CC6.1) without firm-side compensating control"
engagement_id: ENG-2026-VRM-Q2-Critical-Vendor-Review
as_of_date: 2026-04-28
status: under-review

source:
  source_type: vendor-monitoring
  source_id: VRM-MON-2026-Q2-Atlas-001
  # regulator omitted; not examiner-issued

date_identified: 2026-04-25
period_start: 2025-04-01
period_end: 2026-03-31

condition: |
  The SOC 2 Type II report for fraud-screening vendor [vendor codename Atlas] covering
  2025-04-01 through 2026-03-31 carries a qualified opinion on Trust Services Criterion CC6.1
  (logical access). The qualifying paragraph notes that during the audit period the vendor's
  privileged-access reviews were not performed at the contractually committed quarterly cadence
  on Q3 2025 and Q1 2026. The firm has reviewed the qualified opinion and confirmed with the
  vendor's customer-success team that the cadence gap occurred. The firm has no documented
  compensating control on its side: there is no firm-performed review of the vendor's privileged-
  access roster, no firm-side requirement that the vendor evidence quarterly review prior to
  contract renewal, and no firm-side detective control to flag missed reviews between SOC report
  cycles.

criteria: |
  Interagency Guidance on Third-Party Relationships: Risk Management (OCC / FRB / FDIC, June
  2023) §III.D ongoing monitoring — the firm should monitor critical third parties' performance
  against contractual and risk-management expectations on a basis commensurate with the criticality
  of the relationship. NYDFS 23 NYCRR §500.11(a) — third-party service-provider security policy,
  including periodic assessment based on the risk presented and the continued adequacy of the
  third party's cybersecurity practices. Firm Third-Party Risk Management Policy v3.5 §4.3
  (critical-vendor monitoring) and §4.7 (compensating-control matrix for critical vendors with
  qualified or adverse SOC opinions).
criteria_source_anchor: "references/source-anchors.md#interagency-tprm-2023, references/cross-cutting.md#cyber, references/firm-overlay.md#tprm-policy-v35"

cause: |
  The firm-side ongoing-monitoring control (C-VRM-007) requires review of received SOC 2 reports
  for qualified opinions, but the control's design does not include a downstream step to compare
  the qualified opinion against a firm-side compensating-control matrix and trigger a remediation
  workflow when no compensating control is documented. The control's review step ends at
  receipt-and-noting; the gap is the missing trigger from "qualified opinion received" to
  "compensating control evaluated, documented, or scheduled." The vendor's own privileged-access
  review cadence is the vendor's control, not the firm's; the firm's control is the monitoring
  workflow that should have surfaced the absence of a compensating response.

impact: |
  Operational and cyber: residual risk on customer-data access at the vendor for the period the
  vendor's privileged-access review cadence slipped, with no firm-side detective or compensating
  control mitigating the residual risk. Customer: the vendor screens 100% of new account openings
  and a sample of high-risk transactions; nonpublic customer information is in scope of the
  vendor's privileged access. No identified customer-data exposure event during the period; the
  vendor reports no incident, but the firm has limited visibility absent the compensating control.
  Regulatory: NYDFS continuous-supervisory expectation on §500.11 third-party programs; SEC OCIE
  attention on broker-dealer vendor oversight via Reg S-P (customer-information safeguards) is
  in scope. Reputational: low; no public-facing event identified.

severity: high
severity_rationale: |
  High because the vendor is critical (100% of new account openings; high-risk transaction
  screening), nonpublic customer information is in the vendor's privileged-access scope, the
  cadence slip persisted across two of four quarters of the SOC audit period, and there is no
  firm-side compensating control. Not critical because no customer-data exposure event has been
  identified and the vendor has now committed to and evidenced corrective action on cadence;
  the firm-side control gap is the structural weakness, not a confirmed harm event.
compensating_controls: []

# mra_mria_classification omitted; source is vendor-monitoring, not examiner-letter.
# The cyber cross-cutting overlay is loaded; see references/cross-cutting.md#cyber.

# population/sample fields omitted; this is not a sample-based test
linked_obligation_ids: [OBL-TPRM-IIID-OngoingMon, OBL-NYDFS-500-11]
linked_control_ids: [C-VRM-007]
linked_evidence_ids: [EV-2026-VRM-Atlas-Q2-A, EV-2026-VRM-Atlas-Q2-B]

recommendation: |
  The Head of Vendor Risk Management must (1) document a compensating control for the period
  the vendor's cadence slipped and for any future periods where vendor SOC reports carry a
  qualified or adverse opinion on logical-access criteria, (2) redesign control C-VRM-007 to
  include a downstream trigger from qualified-opinion-noted to compensating-control-evaluated,
  with a named approver and documented decision, and (3) initiate a vendor remediation tracking
  record for Atlas covering the cadence slip and the firm's expectation of evidenced quarterly
  reviews going forward.

remediation: |
  Three-part remediation: compensating-control documentation, control redesign, and vendor
  remediation tracking. The control redesign is the structural fix that prevents recurrence
  across the vendor portfolio; the compensating-control documentation closes the specific Atlas
  exposure; the vendor remediation tracking is the firm's leverage on the vendor.

owner: "Head of Vendor Risk Management"
target_date: 2026-07-31
remediation_milestones:
  - {date: 2026-05-15, milestone: "Compensating control for Atlas documented and approved by Vendor Risk Committee", owner: "Head of Vendor Risk Management"}
  - {date: 2026-06-30, milestone: "Control C-VRM-007 redesign signed off by Head of Operational Risk", owner: "Head of Vendor Risk Management"}
  - {date: 2026-07-31, milestone: "Vendor remediation tracking record opened with Atlas; first cadence-evidence cycle delivered by vendor", owner: "Head of Vendor Risk Management"}

closure_evidence:
  - "Compensating-control documentation for Atlas with named approver, retained in GRC platform vendor record"
  - "Updated control documentation for C-VRM-007 with downstream qualified-opinion trigger workflow"
  - "Two consecutive quarters of vendor-evidenced privileged-access reviews from Atlas, retained in vendor monitoring record"
  - "Vendor remediation tracking record with status, owner, and target dates, retained in GRC platform"

interim_mitigation: |
  Firm-side ad-hoc privileged-access roster review against vendor-provided current-state list,
  performed by Vendor Risk Analyst with named approver, until the structural redesign is signed
  off. Evidenced by analyst sign-off log retained in the GRC platform. The interim check is the
  mitigation while the redesign and the vendor's evidenced cadence land.

evidence_gap: true
evidence_gap_note: |
  Vendor has not yet provided firm-side visibility into the privileged-access roster as of the
  cadence slip period; the firm cannot independently verify the slip's customer-data exposure
  scope. Routed to engagement issue log as item ENG-2026-VRM-Q2-IL-003.

confidence_label: medium

reviewer_questions:
  - "Should the redesigned C-VRM-007 trigger workflow apply to all vendor SOC report qualified opinions across logical-access, change-management, and incident-response criteria, or only to logical-access? Scope expansion adds work but covers more failure modes."
  - "Is the 2026-07-31 target date acceptable to the Vendor Risk Committee given the customer-data exposure scope, or should the compensating-control documentation milestone (2026-05-15) move forward?"
  - "Does the firm need to refresh its NYDFS §500.11 third-party annual assessment of Atlas to reflect the qualified opinion, or does the SOC report itself satisfy the assessment requirement until the next annual cycle?"
  - "Should the firm's broker-dealer Reg S-P safeguards-rule program incorporate this finding into the next safeguards-program review, or is the TPRM track sufficient?"

human_review_required: true

revisions:
  - {date: 2026-04-28, reason: initial write-up, delta: created from VRM-MON-2026-Q2-Atlas-001, approved_by: "Head of Vendor Risk Management"}
```

#### What the write-up surfaces

- The condition names the specific Trust Services Criterion (CC6.1), the qualified-opinion period (2025-04-01 through 2026-03-31), the cadence slip (Q3 2025 and Q1 2026), and the absence of a compensating control. The firm's confirmation step with the vendor's customer-success team is named, so the reviewer can trace the confirmation pathway.
- Criteria pulls from three sources: Interagency TPRM Guidance §III.D, NYDFS §500.11(a), and the firm's TPRM policy. Each is named with section. The criteria_source_anchor field points at the source-anchors entry, the cyber cross-cutting overlay (because §500.11 is a cyber criterion), and the firm-overlay. The reviewer can read all three.
- The cause names the specific control attribute that failed: control C-VRM-007 ends at receipt-and-noting and lacks the downstream trigger to compensating-control evaluation. The cause is not "vendor failed" or "monitoring weakness". The vendor's failure is named separately as the upstream condition that the firm-side control should have caught.
- The effect identifies operational, cyber, customer, regulatory, and reputational impact distinctly. Customer impact is "no identified exposure event" rather than "no impact" because the firm has limited visibility absent the compensating control; the honesty matters for severity defensibility.
- Severity rationale references vendor criticality, customer-data exposure scope, frequency (two of four quarters), and the absence of compensating controls. The "not critical" reasoning ties to the absence of a confirmed harm event; that is the boundary the firm will defend if the severity is challenged at the Vendor Risk Committee.
- Compensating controls field is the empty array. The empty array carries the signal explicitly; it is not omission.
- Evidence gap is yes: the vendor has not yet provided privileged-access roster visibility for the slip period. The gap routes to the engagement issue log with a specific item ID.
- Closure evidence is the artifact across all three remediation lines: documentation, redesigned control, evidenced quarters from the vendor, opened remediation record. None of the closure evidence reads as the verb.
- Reviewer questions tie to specific decision points (scope of redesign, target-date defensibility, NYDFS §500.11 assessment cycle, Reg S-P seam) rather than generic "is this complete?" prompts.

#### Downstream uses

- `compliance-testing` consumes `severity`, `linked_control_ids`, and `closure_evidence` to schedule a focused test of C-VRM-007 once the redesign is evidenced.
- `risk-committee-pack` for the next Vendor Risk Committee and Operational Risk Committee references this issue's `severity`, `evidence_gap`, and `target_date` in the open-critical-vendor-issues section.
- `control-matrix` reads `linked_control_ids` to surface ISS-2026-VRM-Vendor-Atlas-014 against the C-VRM-007 row in the vendor-lifecycle matrix; the open issue's severity drops the control's operating-effectiveness rating to partially-effective until closure.
- `vendor-diligence` (when the firm runs an Atlas re-diligence) consumes the issue and the closure evidence as a precondition for vendor re-tier or contract renewal decisions.
- The cyber cross-cutting overlay is loaded; the next CISO-led continuous-monitoring readout reads this issue as a cyber-tagged finding via the cross-cutting overlay path.

## troubleshooting

### Troubleshooting: issue-writeup

Recurring failure modes when an issue write-up looks complete but is not. The reviewer pass should catch these; the builder pass should preempt them.

#### 1. Condition reads as a conclusion

Symptom: the condition field reads "the control failed" or "the control is ineffective" or "vendor oversight is weak". The reviewer cannot tell what was actually observed.

Why it happens: practitioners write what they have concluded because it is the bottom line. The CCCE structure asks for the observable state first, the conclusion later (it ends up split across cause and effect).

Fix: the condition is the dated, scoped, observable state. "On three monthly reporting cycles between 2026-01 and 2026-03, two material counterparty exposures totalling $187M notional were excluded from the consolidated counterparty view." That is the condition. "The control failed" is the cause analysis sitting in the wrong field. The schema validates that condition is non-empty; the discipline is to write the observation in present-tense observable terms.

#### 2. Criteria reads as "per firm policy" without citation

Symptom: the criteria field reads "per firm policy", "per applicable regulation", or "per industry best practice". The reviewer cannot read the criterion.

Why it happens: the practitioner knows the firm has a policy on this and has not yet gone back to the policy or the regulation to pull the section reference.

Fix: criteria is a named source with a section. If the criterion is regulatory, name the rule and section and reference `references/source-anchors.md` or a loaded overlay file by path. If the criterion is the firm's own policy, name the policy version and section and reference `references/firm-overlay.md` by path. "Per firm policy" without citation is a placeholder; the criteria_source_anchor field carries the path the reviewer can follow. Multiple criteria are allowed and common; list each with its source.

#### 3. Cause reads as "human error" or "training gap" or "system limitation"

Symptom: the cause field is a one-line surface label that does not name the control attribute that failed.

Why it happens: surface labels are easy to write and feel correct because the underlying behaviour did involve a person, a training opportunity, or a system constraint. The control-design or operation weakness underneath is the part that has not yet been thought through.

Fix: name the control attribute that failed. "Human error" is replaced by "the reconciliation control's design assumes the feed cutoff equals the source-system close; that assumption became false when the feed-orchestration team shifted the batch window without coordinating with the reconciliation control owner". "Training gap" is replaced by "the SOC-report-review workflow does not include a downstream trigger from qualified-opinion-noted to compensating-control-evaluated". "System limitation" is replaced by "the population query in the controls-testing platform truncates records older than the 90-day window without flagging the truncation in the test result". If root cause analysis is genuinely pending, write "root cause analysis pending" and add an open action; do not invent a cause to fill the field.

#### 4. Effect is generic ("significant impact")

Symptom: the effect / impact field reads "significant impact", "material implication", or "meaningful exposure" without quantification or specific identification.

Why it happens: the practitioner writes the effect as commentary because the quantification is hard or the harm is not yet quantified.

Fix: the effect names the unit, the time window, and the population where applicable. "$X under-stated counterparty exposure on three reporting cycles, propagated into the executive risk pack distributed to the Board Risk Committee" is an effect. "Significant impact" is commentary. Where the effect is across multiple dimensions (financial, customer, regulatory, operational, reputational), name each separately. Where a dimension genuinely has no impact (e.g., reputational impact on an internal-control finding with no public-facing element), say so explicitly rather than omitting the dimension.

#### 5. Severity without rationale

Symptom: severity is set to "high" or "critical" with no rationale field, or a rationale field that reads "given the nature of the finding".

Why it happens: severity assignment under time pressure tends to default to high or critical, and the rationale gets deferred.

Fix: severity is paired with rationale referencing materiality, frequency, customer impact, regulatory exposure, and any compensating controls in place. The rationale is also defensible against the next-lower severity ("not critical because [...]") and the next-higher severity ("higher than moderate because [...]"). Severity assignment carries human review; the unattested severity is not yet a severity.

#### 6. Closure evidence is the verb, not the artifact

Symptom: closure evidence reads "remediated", "control updated", "policy revised", or "issue closed".

Why it happens: the closure evidence field is filled at write-up time when remediation has not yet happened; the practitioner writes the verb because the artifact does not yet exist.

Fix: closure evidence names the artifact the firm will inspect to confirm closure. "Two consecutive months of reconciled feed output reviewed by the Head of Market Risk Reporting with sign-off log retained in the GRC platform" is closure evidence. "Remediated" is not. The artifact may be a system-of-record output, a sample report, a sign-off log, a board minute, a tabletop after-action report, a third-party administrator's restitution-completion attestation, or any other inspectable record. The closure evidence is testable; the closure verb is not.

#### 7. Owner is a team, not a role

Symptom: owner field reads "Risk Team", "Compliance", "Operations", or a person's name.

Why it happens: the engagement has not yet pinned down the named accountable role, or the owner was filled in with the person who happened to be in the room.

Fix: the owner is a named role with accountability: Head of Market Risk Reporting, Head of Vendor Risk Management, Head of Model Risk, BSA Officer, Chief Privacy Officer, Chief Compliance Officer. "Risk team" is not an owner; "Risk Director" is, even though the role exists across multiple individuals over time. The role outlives the incumbent; the issue follows the role.

#### 8. MRA / MRIA classification missing on examiner-issued findings

Symptom: source_type is examiner-letter and the regulator is FRB, OCC, or FDIC, but the mra_mria_classification field is empty or set to n/a.

Why it happens: the practitioner does not know whether the regulator labelled the finding as MRA, MRIA, MRBA, or as a comment / suggestion.

Fix: read the supervisory letter or examination report for the explicit label. The federal banking supervisors are explicit in their letters; CFPB also uses the MRA label (with regulator field set to CFPB). For SEC EXAMS deficiency letters, FINRA findings, and state DOI findings, mra_mria_classification is set to n/a because those regulators do not use the MRA / MRIA framework. The schema enforces that examiner-letter source types name a regulator; the classification field should be populated when the regulator uses the framework.

#### 9. Linked artifact IDs are missing

Symptom: linked_obligation_ids, linked_control_ids, and linked_evidence_ids are empty arrays.

Why it happens: the upstream `obligation-mapping`, `control-matrix`, and `evidence-binder` outputs were not consulted, or the linkage step was skipped.

Fix: each issue write-up should link to at least one obligation (the criterion the condition violates) and at least one control (the control whose design or operation weakness is the cause). Evidence IDs link to the evidence the source-test relied on. A standalone issue write-up that does not link to upstream artifacts is a stranded artifact; downstream consumers cannot pick it up by foreign key. If the upstream artifact does not yet exist, flag in the evidence-gap field and route to the engagement issue log.

#### 10. Severity inflation on cyber-tagged issues

Symptom: a cyber-tagged finding with no identified customer-data exposure is rated critical or high without rationale support.

Why it happens: cyber issues attract reflexive high severity because cyber breaches have visible reputational tail.

Fix: cyber severity calibration overlays on the substantive calibration; it does not replace it. A logging gap on a non-production system with no customer data is moderate even though it is a cyber issue. The severity rationale must specify the cyber-specific weight (identifiable exposure, privileged-access scope, vulnerability dwell time, etc.). The cyber overlay's severity-calibration section is the reference; pull the specific weight, do not generalise.

#### 11. Customer-harm severity deflation

Symptom: a UDAAP finding with population-level scope is rated moderate because the firm is uncomfortable with the harm framing.

Why it happens: identifying customer harm has restitution and supervisory implications; the practitioner under-weights the harm to keep the severity at a level the firm is more comfortable with.

Fix: severity calibration on customer-impact issues weighs the population, the pattern, and the reasonably-avoidable test. A UDAAP finding with identifiable systemic harm and restitution-eligible scope is high or critical. The conduct cross-cutting overlay's severity-calibration section is the reference; the severity rationale must specify the consumer-harm weight.

#### 12. Closure evidence that closes the verb without closing the structural fix

Symptom: closure evidence names a manual workaround (the interim mitigation) as the primary closure evidence; the structural fix is deferred.

Why it happens: the manual workaround is in place and feels closure-shaped; the structural fix takes longer.

Fix: interim mitigation is named separately from closure evidence. The interim mitigation reduces residual risk while the structural fix is built; the structural fix is what the closure evidence inspects. An issue closed on interim mitigation alone reopens the next time the workaround lapses. Where remediation runs longer than 90 days, milestones are set; the closure evidence inspects the milestone artifacts.

#### 13. The write-up tries to be the test workpaper, the binder, and the committee narrative

Symptom: the write-up runs to multiple pages of test sample listings, evidence file contents, and committee-pack-style executive summary.

Why it happens: the issue write-up gets stretched because adjacent skills' outputs are not yet built and the team puts everything in the issue as a stopgap.

Fix: the issue write-up lives downstream of `compliance-testing` (the test workpaper) and `evidence-binder` (the binder), and upstream of `risk-committee-pack` (the narrative). It carries the issue-level summary; the upstream artifacts carry the test depth and the evidence depth; the downstream artifact carries the committee narrative. Cross-references via `linked_evidence_ids`, `linked_control_ids`, and `linked_obligation_ids`. Pulling everything into the write-up breaks the contract with adjacent skills.

#### 14. The write-up is signed off without an independent severity reviewer

Symptom: sign-off block names the practitioner who built the write-up and the owner accepting remediation; no independent severity reviewer is named.

Why it happens: smaller engagements compress the review machinery; the owner often functions as the de-facto severity reviewer because they are the most-named role in the room.

Fix: severity assignment always carries human review by a reviewer independent of the author. For 1.5-line-built write-ups, the 2-line function reviews. For 2-line-built write-ups, internal audit, the chief compliance officer, or an independent peer reviews. For advisory-built write-ups, the engagement partner reviews. The owner concurs with remediation accountability but is not the severity reviewer; an owner who rates the severity on their own issue fails the independence test.

#### 15. The write-up stops too late

Symptom: the skill produces a write-up with severity asserted as final, status set to in-remediation, and closure evidence claimed as in-flight, without evidence.

Why it happens: builder over-runs the human-review gate.

Fix: the write-up is a draft until the named reviewer attests. The skill stops at draft and surfaces the reviewer questions; it does not assert sign-off, distribute, post to the GRC system, or move the status past under-review. The `human_review_required` field is always true; severity attestation is the named gate.
