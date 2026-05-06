# bcbs239-gap-assessment — spec sheet

Plugin: `risk-reporting`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Drafts a BCBS 239 gap assessment against the 14 principles, organized by Overarching governance and infrastructure, Risk data aggregation, Risk reporting, and Supervisory review. Output is a principle-by-principle gap matrix a CRO, head of risk reporting, head of risk data, or examiner-prep team can take to the data-management committee after qualified review.

Best for:
- Standing up or refreshing a BCBS 239 self-assessment ahead of a regulator-driven review (FRB horizontal, ECB SREP, OCC Heightened Standards thematic).
- Diagnosing why a risk committee pack carries a non-high data confidence label (the gap assessment is the upstream artifact).
- Refreshing the BCBS 239 status after a material change (acquisition, system migration, source-of-record consolidation, taxonomy revision).
- Pulling the gap view across G-SIBs and D-SIBs where Principle 12-14 supervisory expectations apply.

Not the right tool when:
- The artifact is the committee pack itself (use `risk-committee-pack`; the BCBS 239 posture appears there as a data-confidence appendix).
- The artifact is a single KRI commentary (use `kri-commentary`).
- The artifact is a one-off data-quality issue write-up (use `risk-compliance-core/skills/issue-writeup`).
- The work is enterprise data governance generally (BCBS 239 is risk-data-anchored; non-risk data — e.g., financial statement data quality under SOX 404 — is out of scope here).

Anchored to: BCBS 239, Principles for Effective Risk Data Aggregation and Risk Reporting (January 2013); BCBS Progress Reports (2017, 2020, 2023, latest [verify date of most recent BCBS thematic review]); FRB SR 12-17 (Consolidated Supervision Framework for Large Financial Institutions, December 2012) for the supervisory expectation chain; OCC Heightened Standards 12 CFR Part 30 Appendix D §II (risk governance framework) [verify section] for large-bank risk-data infrastructure expectations; ECB Guide on effective risk data aggregation and risk reporting (May 2024) [verify date and current version] for SSM-supervised firms.

## Source anchors

Primary:
- BCBS 239 — Basel Committee on Banking Supervision, Principles for Effective Risk Data Aggregation and Risk Reporting, January 2013. The 14 principles are the structural backbone of this skill. The principles group as:
  - Overarching governance and infrastructure (Principles 1-2): governance; data architecture and IT infrastructure.
  - Risk data aggregation capabilities (Principles 3-6): accuracy and integrity; completeness; timeliness; adaptability.
  - Risk reporting practices (Principles 7-11): accuracy; comprehensiveness; clarity and usefulness; frequency; distribution.
  - Supervisory review, tools, and cooperation (Principles 12-14): review; remedial actions and supervisory measures; home/host cooperation.
- BCBS Progress Reports on the implementation of the principles for effective risk data aggregation and risk reporting (2017, 2020, 2023, and most recent). Use for: thematic findings on persistent gaps, especially Principles 2 (architecture), 3 (accuracy), and 6 (adaptability) where banks have repeatedly underperformed.
- FRB SR 12-17 — Consolidated Supervision Framework for Large Financial Institutions, December 2012. Use for: the US supervisory expectation that BCBS 239 capabilities are present at large BHCs.
- OCC Heightened Standards 12 CFR Part 30 Appendix D. Sections to cite: II (Risk Governance Framework, including risk-data and risk-reporting infrastructure expectations) [verify section labels]. Use for: large-bank-specific extension of BCBS 239 expectations.
- ECB Guide on effective risk data aggregation and risk reporting, May 2024 (final). [verify current version and pin cites.] Use for: SSM-supervised firms (US foreign banking organizations with EU subsidiaries; EU groups operating in the US).

Secondary (overlay only):
- Basel III monitoring exercise data templates [verify current version]. Use for: data-aggregation testing workpaper templates.
- COSO ERM 2017 — for the broader governance framing where the firm's risk data architecture sits inside the wider ERM model.

## Sector overlays needed

- `banking.md` — Required and primary. BCBS 239 is the banking-anchored regime. Covers G-SIB and D-SIB application, the FRB tailoring framework's interaction with BCBS 239 expectations, and the OCC Heightened Standards extension.
- `insurance.md` — Light overlay only. BCBS 239 does not directly apply to insurers, but ORSA expectations (NAIC Model #505) [verify section] and IAIS ICP 8 (risk management and internal controls) [verify] carry analogous data-aggregation expectations that firms increasingly map to BCBS 239 as a maturity benchmark. The overlay covers when an insurance group voluntarily applies BCBS 239 as its internal benchmark.
- `capital-markets.md` — Light overlay. BCBS 239 applies at the BHC level; broker-dealer subsidiaries inherit it. The overlay covers SEC Rule 17h recordkeeping and FINRA reporting data-quality interactions.
- `payments-fintech.md` — Out of scope at v1. BCBS 239 does not apply directly. Some large nonbank payments firms voluntarily adopt the framework; phase 2 may add a stub overlay if demand materializes.

## Cross-cutting overlays needed

- `cyber.md` — Optional. Risk-data infrastructure inherits cyber-control obligations (NYDFS Part 500, FFIEC IT booklet); the overlay covers how cyber-control failures affect Principle 1 (governance) and Principle 2 (architecture) ratings.
- `climate.md` — Optional. Where the firm reports climate risk to the committee, the climate data lineage (often vendor-supplied scenario data, ESG providers, third-party emissions data) is a Principle 3 (accuracy) and Principle 6 (adaptability) concern. The overlay covers how to assess BCBS 239 posture on climate data specifically.
- `privacy.md` — Not required at v1.
- `conduct.md` — Not required at v1.

## Output template named sections

Top of artifact:
- Cover: assessment date, scope (legal-entity perimeter), supervisory context (FRB / OCC / ECB / multi-jurisdiction), prior-assessment date and rating (if any)
- Executive summary (5-7 bullets, CRO and CDO voice)
- Methodology (sampling approach, lines of evidence, interview list, document list)

Body — organized by the four BCBS 239 principle groups:

Group A: Overarching governance and infrastructure (Principles 1-2)
- Principle 1: Governance — board and senior management oversight of risk data aggregation and reporting capabilities; named committee, reporting cadence, escalation
- Principle 2: Data architecture and IT infrastructure — taxonomy, golden source mapping, controls over data flow, change management, BCM/DR for risk-data infrastructure

Group B: Risk data aggregation capabilities (Principles 3-6)
- Principle 3: Accuracy and integrity — automated reconciliation, manual workaround inventory, error rates, data-quality framework
- Principle 4: Completeness — coverage of risk types, lines of business, legal entities, geographies; on-balance-sheet vs off-balance-sheet
- Principle 5: Timeliness — production cycles for normal and stress conditions; lag from event to report
- Principle 6: Adaptability — ability to produce ad-hoc and stress-scenario aggregations within required timeframes (the Principle 6 gap is the most common BCBS thematic finding)

Group C: Risk reporting practices (Principles 7-11)
- Principle 7: Accuracy — reconciliation between risk reports and source data
- Principle 8: Comprehensiveness — coverage of all material risk types
- Principle 9: Clarity and usefulness — fitness for the audience (board, ExCo, committee, regulator)
- Principle 10: Frequency — alignment with audience needs and risk profile
- Principle 11: Distribution — controls over distribution lists, classification, redaction

Group D: Supervisory review, tools, and cooperation (Principles 12-14)
- Principle 12: Review — supervisory review expectation; firm's readiness for regulator-driven assessment
- Principle 13: Remedial actions — firm's track record on closing supervisory findings; current open MRAs / MRIAs related to risk data
- Principle 14: Home/host cooperation — for cross-border groups, the framework for sharing risk data with home and host supervisors

For each principle:
- Rating (compliant / largely compliant / materially non-compliant / non-compliant) — using the BCBS scoring vocabulary
- Direction since prior assessment (improving / stable / deteriorating / first assessment)
- Evidence summary (what was reviewed, what was tested)
- Gaps (named, with severity and owner)
- Recommended owner actions

Tail:
- Aggregate posture (per group; overall rating)
- Top 5 priority gaps (with owner, target date, dependency map)
- Linked open issues (MRAs, MRIAs, internal issues)
- Source trace per material claim
- Sign-off block (Head of Risk Reporting, Head of Risk Data / CDO, CRO, date)
- Reviewer questions

## Structured output fields

Schema to add in phase 2: `bcbs239-assessment.schema.json`.

Wrapper object:
- `assessment_id`: string. Stable ID.
- `scope`: object. `legal_entity_perimeter` (array of strings), `supervisory_context` (enum: FRB / OCC / FDIC / ECB / multi-jurisdiction / other), `assessment_date` (ISO date), `prior_assessment_date` (ISO date or null).
- `methodology`: object. `lines_of_evidence` (array of enums: document-review / system-tracing / reconciliation-test / interview / observation), `interview_count` (integer), `document_count` (integer).

Per-principle object (14 instances, one per principle):
- `principle_number`: integer. 1 to 14.
- `principle_group`: enum. `overarching` / `aggregation` / `reporting` / `supervisory`.
- `principle_name`: string. The BCBS 239 short name (e.g., "Governance", "Accuracy and integrity").
- `rating`: enum. `compliant` / `largely-compliant` / `materially-non-compliant` / `non-compliant`.
- `direction`: enum. `improving` / `stable` / `deteriorating` / `first-assessment`.
- `evidence_summary`: string.
- `gaps`: array of objects with `gap_id`, `gap_description`, `severity` (enum: low / medium / high / critical), `owner` (role), `linked_issue_id` (string or null).
- `recommended_actions`: array of objects with `action_description`, `owner`, `target_date` (ISO date), `dependency_ids` (array of strings).

Wrapper tail:
- `aggregate_rating_per_group`: array of objects with `group` (enum), `rating` (enum from the per-principle vocabulary).
- `overall_rating`: enum.
- `priority_gaps_top_5`: array of `gap_id` strings (foreign key into the per-principle gaps).
- `linked_open_issues`: array of strings (foreign key into `issue.schema.json`).
- `confidence_label`: enum. `high` / `medium` / `low` / `unknown`.
- `human_review_required`: boolean. Always true for v1.

## Example scenarios

### Scenario 1: D-SIB self-assessment ahead of an FRB horizontal review

Input: a US D-SIB has been notified of an upcoming FRB horizontal review on risk data aggregation and risk reporting. The CRO and CDO are jointly running the self-assessment, with internal audit shadowing. Source posture: BCBS 239, FRB SR 12-17, OCC Heightened Standards 12 CFR Part 30 Appendix D, the BCBS 2023 progress report's thematic findings, and the firm's prior-year self-assessment.

Output emphasizes:
- 14 principle ratings, with Principles 1, 7, 8, 11 rated `largely-compliant` and Principles 2, 3, 6 rated `materially-non-compliant`. Principle 6 (adaptability) carries the heaviest gap commentary, mirroring the BCBS thematic finding pattern.
- Methodology section names 22 interviews, 86 documents reviewed, and 4 reconciliation tests across credit, market, liquidity, and operational risk.
- Gaps under Principle 2 cite specific architecture issues (manual reconciliation between two market-risk source systems; lack of automated lineage from the credit-loss data warehouse to the regulatory-reporting layer) with named owners and severity.
- Recommended actions under Principle 6 propose an investment to enable ad-hoc stress aggregation within 48 hours (current capability is 5 business days under stress).
- Aggregate ratings: Group A `materially-non-compliant`, Group B `materially-non-compliant`, Group C `largely-compliant`, Group D `largely-compliant`. Overall: `materially-non-compliant`.
- Top 5 priority gaps drive the remediation roadmap and link to two open MRAs from the prior FRB letter.
- Confidence label: high (assessment evidence is well-documented).
- Human review required: yes; the assessment goes to the data-management committee and then the Risk Committee.

### Scenario 2: Foreign banking organization (FBO) self-assessment ahead of an ECB SREP review

Input: a non-US G-SIB with significant US operations under FRB Y-7 reporting and an SSM-supervised EU subsidiary. The ECB has flagged risk data aggregation as a thematic SREP focus. Source posture: BCBS 239, the ECB Guide on effective risk data aggregation and risk reporting (May 2024) [verify version], FRB SR 12-17, and the firm's prior-year self-assessment which carried an overall `largely-compliant` rating.

Output emphasizes:
- Principle 14 (home/host cooperation) takes a heavier section than Scenario 1, reflecting the cross-border supervisory context.
- The ECB Guide's incremental expectations (beyond the BCBS principles) are surfaced as supplementary criteria within Principles 1, 2, 3, 6, and 11; phase 2 must distinguish BCBS 239 baseline from ECB Guide overlay so the firm can read the assessment from either supervisor's lens.
- Climate-data lineage is addressed under Principle 3 (accuracy of vendor-supplied scenario data) and Principle 6 (adaptability for climate stress); the cross-cutting climate overlay supplies the criteria.
- Aggregate ratings show improvement on Principles 1, 2, 7 and a new gap surfaced on Principle 11 (distribution controls on the EU subsidiary's risk pack, which had been distributed beyond the SSM perimeter without classification controls).
- Overall rating: `largely-compliant`, but with Principle 11 newly surfaced as `materially-non-compliant` for the EU subsidiary.
- Confidence label: medium (some EU-subsidiary evidence pending translation and verification).
- Human review required: yes; the assessment goes to the EU subsidiary's management board, then to the group Risk Committee, then to the SSM as part of the SREP submission.

## Common pitfalls

1. Rating without testing. A BCBS 239 rating that relies only on document review and interviews is not credible. Phase 2 must require at least one reconciliation test or system tracing per principle in groups B and C.
2. Confusing risk reporting with financial reporting. BCBS 239 is risk-data-anchored. SOX 404 financial-reporting controls are a related but separate regime. Phase 2 must reject scope drift into financial-statement reporting.
3. Principle 6 lip service. Principle 6 (adaptability) is the most commonly underperforming principle across BCBS thematic reviews. A `largely-compliant` rating on Principle 6 is rarely defensible without evidence of recent ad-hoc and stress-scenario aggregation runs within the required timeframe. Phase 2 must require evidence of recent ad-hoc runs to support any rating above `materially-non-compliant`.
4. Manual workarounds invisible. Manual workarounds (Excel-based aggregations, off-system reconciliations) are a Principle 2 and Principle 3 risk. Phase 2 must require an explicit manual-workaround inventory; an empty inventory at a large bank is implausible and should trigger a reviewer question.
5. Climate data treated as out of scope. Where the firm reports climate to the committee, climate data lineage is in scope under Principles 3 and 6. Phase 2 must include climate as a covered domain when the firm has climate reporting; the cross-cutting climate overlay supplies criteria.
6. Cross-border ratings averaged. For G-SIBs and FBOs, ratings can vary by legal entity. Phase 2 must allow per-entity rating where applicable, with a documented rationale for any aggregation.
7. Open MRAs not linked. Where the firm has open supervisory findings on risk data, Principle 13 (remedial actions) must reflect them. Phase 2 must require linkage between Principle 13 findings and the issue register.
8. Confidence label inflation. The confidence label here is methodology-anchored, not finding-anchored. A `high` confidence label requires multi-line evidence (document + system + reconciliation) per principle in groups B and C. Phase 2 should reject `high` confidence labels with thin methodology.
