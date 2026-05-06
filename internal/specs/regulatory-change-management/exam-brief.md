# Spec: exam-brief

Plugin: regulatory-change-management
Status: phase 1 spec sheet, pending phase 2 build
Date: 2026-05-06

## Activation-tuned description

Drafts a generic exam-prep brief usable across regulators and product lines. Pulls together scope, supervisory letter / first-day letter request items, actions taken since the last exam, evidence available with system-of-record pointers, open issues with current status, MRA/MRIA status if any, and reviewer questions the team should anticipate. Output is the package a chief compliance officer or chief risk officer takes into the opening meeting.

Best for:
- An exam window has opened (any regulator) and the team needs a structured pack from existing artifacts.
- A targeted review or limited-scope exam (cyber, AI/model risk, third-party, BSA/AML) where a generic exam-brief shape is the right starting point and a sector-specific package is not yet warranted.
- A pre-exam mock or self-assessment exercise where the deliverable should look like the real exam-brief.

Not the right tool when:
- The exam is a federal banking exam at a large bank — use sector-plugins/banking-risk-compliance/banking-supervision-readiness instead. That skill carries Heightened Standards, capital, CRA, BSA/AML, and supervisory-letter-style scaffolding specific to OCC/FRB/FDIC supervision.
- The exam is an SEC investment-adviser or asset-management exam — use sector-plugins/capital-markets-asset-management-compliance/adviser-exam-readiness instead. That skill carries IAA Rule 206(4)-7 cadence, marketing rule, custody rule, books and records, and Form ADV-specific scaffolding.
- The objective is to extract obligations or sequence remediation (use rule-to-obligation-extraction or implementation-plan).

Boundary with sector exam-readiness skills:
- exam-brief = generic exam-prep artifact, regulator-agnostic, product-agnostic. Use as the default when the sector skill does not apply or as a sub-package inside a sector readiness pack.
- banking-supervision-readiness = banking-specific exam package; carries OCC/FRB/FDIC supervisory framework expectations, Heightened Standards, capital and liquidity scaffolding, BSA/AML examination manual structure.
- adviser-exam-readiness = SEC adviser/asset-manager-specific exam package; carries IAA, ICA, custody, marketing, and Form ADV scaffolding.
- The sector skills can call exam-brief for a sub-topic where a generic shape is enough (for example, a cyber-targeted slice within a broader bank exam).

Anchored to: FFIEC BSA/AML Examination Manual; OCC, FRB, FDIC examination handbooks (public sections); SEC OCIE / Division of Examinations risk alerts; FINRA examination priorities letters; CFPB Supervisory Highlights; NCUA Letters to Credit Unions; NYDFS examination guidance.

## Source anchors

- FFIEC BSA/AML Examination Manual (manual structure, request-list language).
- OCC Comptroller's Handbook public booklets (e.g., Internal Controls; Compliance Management Systems; Model Risk Management).
- FRB Bank Holding Company Supervision Manual (public sections).
- FDIC Risk Management Manual of Examination Policies (public sections).
- SEC Division of Examinations risk alerts and annual examination priorities.
- FINRA examination priorities letters (annual).
- CFPB Supervisory Highlights (periodic public report).
- NCUA Letters to Credit Unions (e.g., on supervisory priorities).
- NYDFS examination guidance and Industry Letters where applicable.
- Public consent orders for MRA/MRIA-style language patterns (no firm-specific use of named institutions; structural pattern only).

## Sector overlays needed

- banking.md — only the sub-set relevant when exam-brief is called inside a non-banking-supervision-readiness scope (e.g., a CFPB exam at a bank). Larger banking exams should route to the sector skill, not stay here.
- insurance.md — state insurance department exam structure; market conduct exam prep; financial exam prep.
- capital-markets.md — only the sub-set relevant when exam-brief is called for a niche capital-markets review where adviser-exam-readiness is too broad.
- payments-fintech.md — CFPB non-bank supervision exam prep; state money-transmitter exam prep.

## Cross-cutting overlays needed

- cyber.md — cyber-targeted exam scaffolding (NYDFS Part 500 exam, FFIEC IT exam booklet).
- privacy.md — privacy-program exam scaffolding (GLBA Safeguards exam).
- climate.md — climate-related supervisory engagement scaffolding for in-scope institutions.
- conduct.md — UDAAP-targeted exam, fair-lending exam scaffolding.

## Output template named sections

1. Cover sheet (regulator, exam type, scope window, lead examiner role, lead firm contact role)
2. Executive summary (no more than five bullets; key themes, evidence posture, known issues)
3. Scope and request-list mapping (request-list item → owner → status → artifact pointer)
4. Actions taken since last exam (changes in policy, control, technology, organization, third party)
5. Evidence inventory (artifact name, location/system-of-record, custodian role, last-refreshed date)
6. Open issues and MRA/MRIA status (item, source, due date, status, reviewer comments)
7. Self-identified gaps and management actions (gaps the firm wants to surface proactively)
8. Reviewer questions anticipated (drawn from current supervisory priorities and recent enforcement themes)
9. Talking points for the opening meeting
10. Document index (by request-list item)
11. Source trace and confidence labels

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| brief_id | string | Stable ID for the brief |
| regulator | string | Regulator name |
| exam_type | enum {full_scope, targeted, limited_scope, mock, self_assessment, follow_up} | Exam shape |
| scope_window | object {start, end, in_scope_products, in_scope_business_units, geographies} | Exam scope |
| lead_examiner_role | string | Role of lead examiner (do not name) |
| lead_firm_contact_role | string | Internal lead role |
| request_list_items | array<request_item> | First-day-letter items |
| request_item.id | string | Stable ID |
| request_item.text | string | Item text |
| request_item.owner_role | string | Owner role |
| request_item.status | enum {ready, partial, not_started, escalated} | Readiness status |
| request_item.artifact_pointers | array<string> | Pointers to evidence locations |
| request_item.confidence | enum {high, medium, low, unknown} | Confidence |
| actions_since_last_exam | array<object {area, change, date, owner_role}> | Material changes |
| open_issues | array<object {id, source, type ∈ {MRA, MRIA, deficiency, finding, self_id}, due_date, status}> | Open supervisory items |
| anticipated_reviewer_questions | array<object {question, source_pattern, talking_point}> | Anticipated questions |
| evidence_inventory | array<object {artifact, system_of_record, custodian_role, last_refreshed}> | Evidence pack |
| confidence | enum {high, medium, low, unknown} | Brief-level confidence |

## Example scenarios (public-source-derived)

1. Cyber-targeted exam (NYDFS Part 500 review) at a state-chartered bank. Exam-brief frames Part 500 §500.2 cybersecurity program, §500.3 cybersecurity policy, §500.4 CISO designation, §500.5 testing, §500.7 access privileges, §500.11 third-party SP security policy, §500.17 notification. Request-list mapping ties each section to firm artifact (program description, policy version, CISO charter, pen-test report, IAM evidence pack, vendor inventory, incident-notification log).
2. CFPB non-bank supervision exam at a fintech offering consumer credit. Exam-brief frames CFPB Supervisory Highlights themes from the most recent edition (UDAAP, fair-lending, consumer reporting), maps the firm's CMS to the manual, and surfaces self-identified gaps from the most recent monitoring cycle. [verify cite to recent Supervisory Highlights edition]

## Common pitfalls

1. Confusing exam-brief with a sector readiness package. If the exam is a full-scope OCC bank exam, this skill should hand off to banking-supervision-readiness, not produce the package itself.
2. Reusing last cycle's evidence pack without a refresh check. Evidence drift between exam cycles is a common finding source.
3. Anticipated reviewer questions that read like FAQs instead of grounded predictions. Each question should reference a current supervisory priority or a public enforcement theme.
4. Missing self-identified gaps. Self-identification is generally a credibility signal with examiners. Suppressing gaps because they look bad backfires.
5. MRA/MRIA status as "open" without a date and owner. An open item without a date and owner reads as drift; capture both.
