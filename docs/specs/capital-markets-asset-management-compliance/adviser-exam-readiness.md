# Spec: adviser-exam-readiness

Plugin: capital-markets-asset-management-compliance
Status: phase 1 spec sheet, pending phase 2 build
Date: 2026-05-06
Sector overlay: capital-markets (SEC-registered investment advisers, broker-dealers, dual registrants)

## Activation-tuned description

Builds an SEC Division of Examinations (EXAMS) exam-readiness pack for an SEC-registered investment adviser, broker-dealer, or dual registrant. Reconstructs the firm's posture against the document request list common to IA exams (Form ADV cross-check, Rule 206(4)-7 written compliance program, Rule 204A-1 code of ethics, Rule 206(4)-2 custody, Rule 206(4)-1 marketing, Rule 204(b)-1 Form PF where applicable, business continuity, cybersecurity, books and records under Rule 204-2). For BDs, mirrors common BD exam categories (Reg BI, Form CRS, FINRA 3110 supervision, FINRA 3120/3130 annual certifications, AML, books and records under Exchange Act Rule 17a-3 / 17a-4). Output is the readiness pack: gap matrix, evidence index, mock interview prep notes for senior officers, and a remediation list with owners.

Best for:
- A firm has been notified of an SEC EXAMS examination (routine, focused, or for-cause) and needs a 2-6 week readiness sprint.
- A CCO is preparing the annual mock-exam exercise as part of the Rule 206(4)-7 / 38a-1 / 3110 review.
- A new CCO is doing a 90-day baseline assessment of the compliance program against current EXAMS priorities.
- A consulting team is performing a pre-exam diagnostic for an adviser or BD client.

Not the right tool when:
- The objective is mapping a specific new rule into firm policy (use regulatory-change-management/regulatory-impact-assessment or rule-to-obligation-extraction).
- The objective is fund board reporting (use fund-board-reporting in this plugin).
- The objective is a generic regulator-agnostic exam brief (use regulatory-change-management/exam-brief — that skill covers banking-style exam scope; this skill is SEC EXAMS / FINRA-specific with the IA Act, ICA, Exchange Act, and FINRA rule lattice).
- The institution is not SEC- or FINRA-registered.

Boundary with regulatory-change-management/exam-brief:
- exam-brief (capability skill): generic exam brief shape, sector-agnostic, used for any regulator request (CFPB, OCC, FRB, FDIC, NYDFS, state DOI, FINRA, SEC, FinCEN). Output is the exam-engagement playbook.
- adviser-exam-readiness (this skill): SEC IA / BD / fund / dual-registrant specific exam-readiness pack with the IA Act and Exchange Act lattice, EXAMS document-request playbook, current-year EXAMS priorities, and Form ADV / Form CRS / Form BD cross-checks.
- The two skills chain: an SEC EXAMS notification triggers exam-brief for engagement playbook (entry, points of contact, document handling, privilege posture), then adviser-exam-readiness for the substantive readiness sprint.

Anchored to: Rule 206(4)-7 (compliance program for investment advisers); Rule 204A-1 (code of ethics); Rule 206(4)-2 (custody); Rule 206(4)-1 (Marketing Rule); Rule 204-2 (books and records); Rule 204(b)-1 (Form PF); Rule 204-3 (Form ADV Part 2 brochure delivery); SEC Form ADV instructions; SEC Form CRS / Form ADV Part 3 (Reg BI/IA disclosure); Reg BI (17 CFR 240.15l-1, effective June 30 2020); Exchange Act Rule 17a-3 and 17a-4 (BD books and records); FINRA Rule 3110 (supervision); FINRA Rule 3120 (annual supervisory control report); FINRA Rule 3130 (annual CEO certification); FINRA Rule 3310 (AML); SEC Division of Examinations Annual Examination Priorities (current year — 2026); SEC Division of Examinations Risk Alerts (current set).

## Source anchors

- 17 CFR 275.206(4)-7 — compliance program rule for IAs.
  - Annual review of adequacy and effectiveness; written policies and procedures reasonably designed to prevent violations; designated CCO.
- 17 CFR 275.204A-1 — code of ethics.
  - Standards of conduct; reporting of personal securities transactions; reporting of access-person status; reporting of code violations; pre-clearance for IPOs and limited offerings.
- 17 CFR 275.206(4)-2 — custody rule.
  - Surprise verification by independent public accountant; account statements; "qualified custodian" definition; SLOA / SPA exceptions; private fund audit alternative.
- 17 CFR 275.206(4)-1 — Marketing Rule (see marketing-rule-evidence).
- 17 CFR 275.204-2 — books and records (full table of records, retention 5/2 years, electronic-records standards).
- 17 CFR 275.204(b)-1 — Form PF (private fund advisers; thresholds; current-event reporting under 2023 amendments [verify post-PFA-vacatur status of current-event reporting]).
- 17 CFR 275.204-3 — brochure delivery.
- Form ADV General Instructions (current); ADV Part 1A, Part 2A, Part 2B, Part 3 (Form CRS).
- 17 CFR 240.15l-1 — Reg BI (broker-dealer best interest standard for retail customers).
- 17 CFR 240.17a-3, 240.17a-4 — BD records.
- FINRA Rule 3110 (supervision); 3120 (supervisory control); 3130 (annual CEO certification); 3310 (AML); 4530 (reporting requirements); 2210 (communications with the public); 2111 (suitability, alongside Reg BI).
- 31 CFR Chapter X — BSA obligations for BDs.
- SEC Division of Examinations 2026 Examination Priorities. [verify current year publication date and contents]
- SEC Division of Examinations Risk Alerts (relevant set):
  - Marketing Rule (Sept 2022; Apr 2023). [verify Apr 2023]
  - Custody Rule (multiple).
  - Code of Ethics.
  - Branch office inspections (FINRA 3110.12, 3110.13).
  - Cybersecurity-themed alerts.
  - AI / predictive analytics-themed alerts. [verify current state of any AI-specific alert]
- SEC Cybersecurity Risk Management Rules for Advisers and Funds — [verify current state: proposed Feb 9 2022, status of any final rule].
- SEC Reg S-P amendments adopted May 16 2024 (data breach notice and customer information safeguarding for BDs, IAs, and funds). [verify exact citation]
- SEC Private Fund Advisers Rule (adopted Aug 23 2023, vacated by 5th Circuit National Association of Private Fund Managers v. SEC, June 5 2024) — [verify current state; the rule is not in force, but related obligations under existing antifraud and recordkeeping rules remain].

## Sector overlays needed

Only `capital-markets`. Skill is sector-unique. No banking/insurance/payments overlay file under `references/sector-overlays/`.

Sub-flavors inside the capital-markets overlay (handled in SKILL.md, not as separate sector files):
- IA flow (Form ADV, Rule 206(4)-7, 204A-1, 206(4)-2, 206(4)-1, 204-2).
- BD flow (Reg BI, Form CRS, FINRA 3110/3120/3130/3310, 17a-3/17a-4).
- Dual-registrant flow (both, with the bridging conflicts).
- Private fund adviser flow (Form PF; the vacated PFA Rule context; existing antifraud reach).

## Cross-cutting overlays needed

- `cyber.md` — Reg S-P (amended May 2024); the proposed/[verify final] Cybersecurity Risk Management Rule for advisers and funds; NYDFS Part 500 for NY-licensed entities; FINRA cybersecurity guidance for BDs.
- `privacy.md` — Reg S-P (initial-and-amended), GLBA financial privacy, state privacy laws affecting client data; privacy notice delivery evidence under Rule 204-2.
- `conduct.md` — code of ethics behavioural elements; Reg BI care obligation; conflicts management evidence trail.
- `climate.md` — only when ESG-labeled product disclosures are in exam scope (Names Rule 35d-1 revision); ESG strategy advertisement substantiation. [verify Names Rule revised compliance dates]

## Output template named sections

1. Engagement context (firm registration, exam type — routine / focused / for-cause / sweep, EXAMS region, prior exam date and findings, current document request scope, deadline)
2. Posture summary (max 5 bullets, RAG status by domain, top 3 residual risks)
3. Document-request response matrix (request item -> source location -> evidence -> reviewer -> status -> hand-off owner)
4. Form ADV cross-check (Part 1A items, Part 2A brochure currency, Part 2B brochure supplements, Part 3 Form CRS; consistency with website, marketing, contracts, and fee schedules)
5. Rule 206(4)-7 program adequacy (annual review status; risk inventory; policy currency; testing log; CCO empowerment)
6. Rule 204A-1 code of ethics (access-person list; personal trading reporting status; pre-clearance for IPOs and limited offerings; violations log)
7. Rule 206(4)-2 custody (qualified custodian; account statement delivery; surprise audit status; SLOA / SPA inventory and Section 9 letter posture; private fund audit if applicable)
8. Rule 206(4)-1 marketing (snapshot of current ads in market; substantiation files; recordkeeping; testimonial/endorsement and hypothetical performance posture; cross-reference to marketing-rule-evidence pack)
9. Rule 204-2 books and records inventory (record type -> system of record -> retention through -> e-records compliance)
10. Form PF (where applicable; large hedge fund / large liquidity fund / large private equity adviser thresholds; current-event filings posture)
11. Reg BI / Form CRS (BD or dual-registrant only): care, disclosure, conflict, compliance obligations; CRS delivery and update evidence
12. FINRA 3110/3120/3130/3310 (BD only): WSPs, branch inspections, supervisory control report, CEO certification, AML program, FinCEN beneficial-ownership posture
13. Cybersecurity / Reg S-P / [verify cyber rule] / NYDFS Part 500
14. Mock interview prep (CCO, CEO, CFO, head of trading, head of marketing, valuation designee chair as applicable: likely questions and prepared responses tied to evidence)
15. Gaps and remediation list (gap, severity, owner, due date, evidence required)
16. Source trace and confidence

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| readiness_id | string | Stable ID |
| firm.registration | enum {IA_only, BD_only, dual_registrant, fund_adviser, private_fund_adviser} | Drives applicable rules |
| exam_context | object {exam_type, region, notification_date, document_request_due_date, prior_exam_date, prior_findings_status} | Engagement context |
| posture_rag | object {form_adv, marketing, custody, code_of_ethics, books_and_records, cyber_privacy, regbi_crs, finra_supervision, form_pf, ai_use, esg_naming} | Domain RAG |
| doc_request_matrix | array<{request_item, source_location, evidence_pin, reviewer, status, due_date, redaction_required}> | Per requested item |
| form_adv_crosscheck | object {part_1a_currency, part_2a_brochure_date, part_2b_supplements_currency, form_crs_currency, website_consistency, marketing_consistency, contract_consistency, fee_schedule_consistency} | ADV consistency |
| compliance_program_206_4_7 | object {last_annual_review_date, risk_inventory_pin, policy_currency, testing_log_pin, cco_attestation} | Program adequacy |
| code_of_ethics_204a_1 | object {access_persons_count, personal_trading_status, preclearance_log, violations_log_summary} | Code of ethics |
| custody_206_4_2 | object {qualified_custodians, account_statement_delivery, surprise_audit_status, sloa_spa_inventory, section_9_letters, pf_audit_status} | Custody |
| marketing_206_4_1 | object {ads_inventory, substantiation_status, hypothetical_present, testimonials_present, third_party_ratings_present, cross_ref_to_evidence_pack} | Marketing snapshot |
| books_records_204_2 | array<{record_type, system_of_record, retention_through, e_records_compliance}> | Records inventory |
| form_pf | object {applicable, threshold_class, last_filing_date, current_event_filings_count, status_after_pfa_vacatur_assessment} | Form PF |
| regbi_crs | object {applicable, care_evidence, disclosure_evidence, conflict_evidence, compliance_evidence, crs_delivery_evidence, crs_update_evidence} | Reg BI / CRS |
| finra_supervision | object {wsp_currency, branch_inspections_log, rule_3120_report_date, rule_3130_certification_date, aml_independent_test_date, beneficial_ownership_posture} | FINRA supervision |
| cyber_privacy | object {reg_sp_program_pin, breach_notice_capability, cyber_rule_status_assessment, nydfs_500_status, vendor_security_posture} | Cyber/privacy |
| mock_interview_prep | array<{interviewee_role, likely_questions, prepared_responses, evidence_anchors}> | Mock interview |
| gaps | array<{gap_id, domain, severity, description, owner, due_date, evidence_required}> | Remediation list |
| confidence | enum {high, medium, low, unknown} | Reviewer confidence |
| open_questions | array<{question, blocker_for}> | Items needing legal/CCO input |

## Example scenarios (public-source-derived)

1. **IA receives EXAMS notification — focused exam on marketing and custody.** A mid-size RIA receives a focused-exam letter with a 2-week document request covering Marketing Rule materials, custody arrangements (including SLOAs), and code of ethics personal trading. The skill maps the document request to source systems, runs the Form ADV cross-check (finds Item 9 custody response inconsistent with the actual SLOA inventory), reviews the marketing pack against the Sept 2022 and Apr 2023 risk alerts (finds two pieces with hypothetical performance lacking the (d)(6) audience-appropriateness policy pin), assembles the surprise-audit posture, and produces a 14-day remediation plan plus mock interview prep for the CCO. [verify Apr 2023 risk alert exact title]

2. **Dual registrant — Reg BI / Form CRS sweep readiness.** A dual-registered IA/BD prepares for a Reg BI focused exam following EXAMS' Reg BI sweep priorities. The skill assembles the four Reg BI obligation evidence (disclosure, care, conflict, compliance), reconciles Form CRS against the latest delivery evidence and the website, checks the FINRA Rule 3110 supervisory procedures against the Reg BI care obligation evidence, surfaces a gap on the conflict-of-interest documentation for proprietary product recommendations, and produces a mock interview script for the firm's designated supervisor and CCO. Pattern derived from publicly disclosed Reg BI exam findings and FINRA disciplinary themes.

## Common pitfalls

1. Treating exam readiness as a document-collection exercise. EXAMS reads for posture, not just paperwork. The mock interview is where firms underperform.
2. Form ADV inconsistency. Item 9 custody, Item 11 disciplinary, Item 5 fee schedule, and Part 2A brochure must hang together. The exam team will reconcile, and inconsistencies produce questions that turn into findings.
3. SLOA inventory understated. Standing letters of authorization are easy to miss when issued by the custodian rather than the adviser. Custody posture must reflect the full SLOA universe.
4. Code of ethics violations log treated as confidential. Violations must be reported to the CCO and the CCO must report to senior officers; the log is exam scope.
5. Marketing Rule scope drift. RFP responses, conference talks, social posts, and podcast appearances are advertisements. A "marketing inventory" limited to the website and pitch deck understates scope.
6. Form PF current-event filings under the post-PFA-Rule landscape. The 2023 Form PF amendments included new current-event triggers; the broader PFA Rule was vacated by the 5th Circuit in June 2024. The Form PF amendments are a separate rulemaking and have not been vacated [verify current state]; firms sometimes conflate the two.
7. Reg BI care obligation evidence treated as suitability paperwork. The care obligation is broader and includes a reasonably-available alternatives analysis for material recommendations.
8. Cybersecurity posture pinned to a proposed rule that has not been adopted. Reg S-P 2024 amendments are in force; the SEC cyber risk management rule for advisers and funds is — [verify current state]. Treat them separately.
9. Treating the prior exam's deficiency letter as closed because the firm responded. EXAMS revisits prior findings; status of remediation evidence is a high-priority readiness check.
10. Ignoring branch inspection logs (FINRA 3110.12 / 3110.13) for BDs and dual registrants. Branch inspection patterns are a recurring exam theme.
