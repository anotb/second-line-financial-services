# Sector overlay — capital-markets

This skill is sector-only. The entire workflow is the capital-markets overlay; there is no banking, insurance, or payments-fintech overlay file. The capital-markets overlay carries the registration-class branching the readiness pack must do.

## Registration-class branching

The pack adapts to the firm's registration constellation. Most engagements run one of these flavors; multi-flavor firms run more than one branch in a single pack.

### Investment adviser (IA) flow

Anchors: Rule 206(4)-7, Rule 204A-1, Rule 206(4)-2, Rule 206(4)-1 (Marketing Rule), Rule 204-2, Rule 204-3, Form ADV Parts 1A / 2A / 2B / 3, IA Act §206 fiduciary duty.

Document-request lanes the pack walks:
- Form ADV cross-check (Item 9 custody vs the actual SLOA / qualified-custodian inventory; Item 11 disciplinary disclosure currency; Item 5 fee schedule consistency with contracts and Part 2A; Part 2A brochure currency and material-change interim delivery evidence; Part 2B supplements current for each supervised person providing advice; Part 3 Form CRS currency and delivery evidence for retail-investor clients).
- Rule 206(4)-7 written compliance program (annual review status and date; risk inventory; policy currency log; testing log; CCO empowerment evidence; CCO attestation).
- Rule 204A-1 code of ethics (access-person list; personal-trading reporting status; pre-clearance log for IPOs and limited offerings; violations log; CCO reporting to senior officers).
- Rule 206(4)-2 custody (qualified-custodian inventory; account-statement-delivery test; surprise-audit independent-public-accountant engagement and most recent verification report; SLOA / SPA inventory and Section 9 letter posture; private-fund audit alternative if relied on).
- Rule 206(4)-1 marketing (current ads inventory across channels — website, pitch decks, RFP responses, conference talks, social posts, podcast appearances; substantiation files; testimonials and endorsements posture; hypothetical-performance audience-appropriateness policy under (d)(6); third-party ratings; Marketing Rule books-and-records under Rule 204-2(a)(11)). Cross-skill: chain to `marketing-rule-evidence` for the substantive evidence pack.
- Rule 204-2 books and records (record type, system of record, retention through, electronic-records compliance under (g)).

### Broker-dealer (BD) flow

Anchors: Reg BI (17 CFR §240.15l-1), Form CRS, FINRA Rule 3110 / 3120 / 3130 / 3310 / 4530 / 2210 / 2111, Exchange Act Rule 17a-3 / 17a-4, 31 CFR Chapter X.

Document-request lanes:
- Reg BI four-obligation evidence (disclosure, care including reasonably-available alternatives analysis for material recommendations, conflict identification and mitigation including elimination of certain compensation conflicts, compliance — written policies and procedures reasonably designed to achieve compliance with Reg BI).
- Form CRS delivery evidence and update evidence; consistency with website and Reg BI disclosures.
- FINRA Rule 3110 written supervisory procedures, branch and OSJ inspections under 3110.12 / 3110.13 (inspection cycle, inspection reports, gap remediation).
- FINRA Rule 3120 supervisory-control report (annual, presented to senior management).
- FINRA Rule 3130 annual CEO certification (date, content, supporting senior-officer interviews).
- FINRA Rule 3310 AML program (CIP and CDD under 31 CFR §1023.220, BO under 31 CFR §1010.230, suspicious-activity monitoring, CTR, OFAC screening, BSA-officer attestation, most recent independent-testing report).
- FINRA Rule 2210 communications and FINRA Rule 2111 suitability (BD marketing distinct from IA Marketing Rule lane).
- Exchange Act Rule 17a-3 / 17a-4 books and records (record type, system of record, retention through, electronic-records compliance — note 17a-4 was amended Oct 12, 2022 to permit an audit-trail alternative to WORM).

### Dual-registrant flow

Both IA and BD branches run, with the bridging conflicts:
- Form ADV Part 3 / Form CRS for the same retail customers under both regimes; consistency required.
- Reg BI care obligation evidence vs IA Act §206 fiduciary-duty evidence for retail customers receiving advisory services.
- Conflict-of-interest documentation across both regimes (proprietary product recommendations, principal trading, cross-trading, soft-dollar arrangements).
- Supervision: FINRA Rule 3110 written supervisory procedures must reach the Reg BI care obligation; the IA-side Rule 206(4)-7 program must address the dually-regulated activity.
- Marketing: Rule 206(4)-1 governs IA-side communications; FINRA Rule 2210 governs BD-side communications. Materials sometimes carry both registrations and both regimes apply.

### Private-fund-adviser flow

Anchors: IA Act §206 antifraud, Rule 204-2 recordkeeping, Rule 204(b)-1 / Form PF, Rule 206(4)-2 custody (private-fund audit alternative), Rule 206(4)-1 marketing.

Document-request lanes:
- Form PF applicability and threshold class (large hedge fund adviser, large liquidity fund adviser, large private-equity adviser); last filing date; current-event filings count under the 2023 / 2024 amendments [verify operative current-event reporting effectiveness post-PFA-Rule vacatur context — the Form PF amendments are a separate rulemaking from the vacated Private Fund Advisers Rule].
- Private-fund-audit alternative under Rule 206(4)-2(b)(4): annual audit by a registered PCAOB-registered independent public accountant within 120 days of fiscal year-end and on liquidation.
- Side-letter inventory and most-favoured-nation analysis (relevant to antifraud reach under §206 even though the PFA Rule's preferential-treatment restrictions are not in force).
- Marketing Rule application to private-fund advertising including past-specific-performance, hypothetical performance, and third-party ratings in fund pitch decks.
- Books-and-records reach under Rule 204-2 covering investor communications, side letters, fund formation documents, and valuation methodologies.

### Registered-fund-adviser flow (cross-link to fund-board-reporting)

Anchors: ICA Rule 38a-1, Rule 22c-1, Rule 2a-5 valuation rule, Rule 17a-7 / 17a-8 / 17e-1 / 10f-3 affiliated-transaction rules, Names Rule 35d-1.

Document-request lanes:
- Rule 38a-1 fund and service-provider compliance program (CCO 38a-1 annual report to the board; service-provider compliance certifications; chief-compliance-officer interviews with the fund board).
- Rule 2a-5 fair-value-determination program (board designation of valuation designee; pricing-policy and exception-handling evidence; board reporting cadence).
- Rule 17a-7 / 17a-8 / 17e-1 / 10f-3 affiliated-transaction recordkeeping and approval predicates.
- Names Rule 35d-1 80% policy compliance for funds with names suggesting investment focus (including ESG-themed funds; verify operative compliance dates by fund size).
- Cross-skill linkage: `fund-board-reporting` carries the substantive 15(c) and 38a-1 board materials; this skill consumes the most recent 38a-1 report as evidence.

## SEC EXAMS region and supervisory office

The SEC Division of Examinations has regional offices (NY, Chicago, Atlanta, Boston, Denver, Fort Worth, LA, Miami, Philadelphia, Salt Lake City, San Francisco, Washington DC) [verify current office list]. Region drives examiner staffing and timing. Capture the responsible region, the exam-staff names if disclosed in the notification (roles only in narrative), and the document-request deadline in the engagement context.

## Exam-type calibration

The pack scales to exam type. A focused exam (one or two topics, e.g., Marketing Rule and custody) reads as a thin spine — Form ADV cross-check, the topical evidence inventory, the mock interview for the affected officers, and a tight remediation list. A routine examination scopes broadly across the IA Act / ICA / Exchange Act / FINRA lattice — full Parts A and B with all applicable rule lanes. A for-cause exam responds to a specific concern (often disclosed in the notification or the prior year's deficiency letter); the pack carries the for-cause-topic evidence first and the rest of the lattice second. A sweep exam tracks the EXAMS Risk Alert that triggered it; the pack maps the alert's specific concerns onto the firm's evidence and surfaces the exact gaps the sweep is designed to find.

## Verification flags carrying through

- SEC Cybersecurity Risk Management Rules for Advisers and Funds — current state [verify].
- SEC Predictive Data Analytics Rule — current state [verify].
- Form PF current-event reporting post-PFA-Rule context [verify].
- Reg S-P May 2024 compliance dates by entity type and size [verify].
- Names Rule amendments compliance schedule [verify].
- Rule 605 / 606 amendments compliance dates [verify].
- SEC EXAMS Annual Examination Priorities current year [verify at write time].
- FinCEN BO reporting rule under Corporate Transparency Act — current state given litigation history [verify].
