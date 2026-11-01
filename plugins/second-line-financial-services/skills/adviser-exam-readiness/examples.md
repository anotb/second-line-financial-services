# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## sec-exams-mid-sized-ria-pre-exam-prep

### Example: SEC EXAMS pre-exam command-center stand-up at a mid-sized SEC-registered investment adviser

#### Scenario

A mid-sized SEC-registered investment adviser (~$10B regulatory AUM, growth-equity strategy focus, separately-managed-account business serving institutional and high-net-worth clients with two private funds that co-invest alongside the SMAs) receives an EXAMS notification letter for a routine examination from the regional office. The notification opens a four-week window before the first document-request production is due; fieldwork is scheduled six weeks out, virtual with two days of synchronous interviews on-site at the firm's headquarters. The CCO and the general counsel run the readiness sprint jointly. The firm has not had an EXAMS exam in five years (the prior exam closed with two non-significant deficiencies, both remediated); the most recent self-identified issue is an in-flight refresh of the firm's electronic-communications surveillance program following an internal review of off-channel-communications use among the institutional sales team.

The firm is IA-registered only — no broker-dealer affiliate, no Reg BI / Form CRS lane, no FINRA supervisor. The two private funds are 3(c)(7) qualified-purchaser vehicles; the firm is a private-fund adviser for Form PF purposes and files as a non-large hedge fund adviser. The SMA business is the bulk of regulatory AUM. No registered investment companies; no Rule 38a-1 lane.

Source posture: public-plus-firm-policy-plus-evidence (the firm provides Form ADV, the compliance manual, the Code of Ethics, the marketing-review log, the SLOA inventory, the Form PF filings, the electronic-communications policy, and the prior-exam deficiency-letter response file).

Persona: chief compliance officer plus general counsel. The CCO owns the request-list production and the substantive readiness; GC owns privilege posture, document-handling, and the response-routing rules. Outside counsel is engaged on retainer for advice and for any matter touching privilege but not for routine production.

Engagement type: pre-exam command-center stand-up (the four weeks between notification and first production), running into the substantive Part B readiness on the rule lanes the request list reaches.

#### Output sketch

The pack opens with the cover-and-engagement block: firm registration profile (legal-name placeholder; IA registration number placeholder; ~$10B regulatory AUM; institutional and HNW SMA business plus two co-investment private funds; US-only geography; no retail-brokerage business), exam context (routine; SEC EXAMS regional office; notification dated [date]; first document-request production due 14 days from notification with rolling-production negotiated for the larger items; fieldwork six weeks out with two days of synchronous interviews on-site), source posture (public-plus-firm-policy-plus-evidence), confidence label (`medium` until the in-flight electronic-communications surveillance refresh closes).

##### Part A — Document-request response matrix

The request list runs eighteen items across the IA lanes plus one item on private-fund matters. The matrix is a tab-per-domain workbook (Form ADV / 206(4)-7 / 204A-1 / 206(4)-2 / 206(4)-1 / 204-2 / Form PF / cyber-Reg S-P) with a status enum on each row: `received` (item is in the production folder, GC has cleared, CCO has signed off), `outstanding` (work remaining), `privileged` (under privilege review or withheld with privilege-log entry), `clarifying-question` (item text reaches matter the firm needs the EIC to clarify before producing).

Representative rows:

| Item | Lane | Owner role | Status | Privilege posture | Note |
|------|------|------------|--------|-------------------|------|
| RL-01: Form ADV Parts 1, 2A, 2B, 3 currently in effect and at each annual amendment in review period | Form ADV | CCO | received | producible | IARD pull complete; Item 5.L. cross-check in flight |
| RL-02: Compliance manual and 206(4)-7 annual review reports for review period | 206(4)-7 | CCO | privileged | redacted-and-producible | Counsel-review sections redacted; privilege log entry drafted; GC sign-off pending |
| RL-03: Code of Ethics, personal-trading reports, violation log, enforcement evidence | 204A-1 | CCO | received | producible | Three violation-log entries in review period; enforcement-action evidence pulled for each |
| RL-04: Marketing materials disseminated in review period including pitchbooks, RFP responses, and one-on-one communications constituting advertisements | 206(4)-1 | head of marketing | outstanding | under-review | "One-on-one communications constituting advertisements" scope requires CCO/GC definitional read; chained to `marketing-rule-evidence` |
| RL-05: Performance composites and supporting data including hypothetical, predecessor, model, back-tested, and third-party-rating use | 206(4)-1 | head of marketing | outstanding | producible | GIPS-verified composites available; calculation worksheets pinned for the hypothetical-allocation deck flagged in self-identified issues |
| RL-06: Custody-rule documentation including qualified-custodian list, surprise-audit reports, account-statement-delivery evidence, SLOA inventory and authorisations, private-fund audit alternative evidence | 206(4)-2 | COO | received | producible | SLOA inventory current as of review-period end; surprise-verification reports issued within 120-day window in both years; private-fund audited financials delivered within 120 days for both funds |
| RL-07: Electronic-communications policy, off-channel-communications surveillance, personal-device attestation evidence, internal investigations | 204-2 / cyber | CCO + IT lead | privileged | under-review | Counsel-led internal investigation in flight; outside counsel consulting on privilege posture; high-stakes line |
| RL-08: Form PF filings and supporting calculations for review period | Form PF | COO | received | producible | Filings and supporting workbooks in production folder |
| RL-09: Trade allocation and aggregation policy and supporting evidence including IPO and limited-allocation deviations | 204-2 | head of trading | received | producible | Allocation-deviation log pulled; de-minimis posture documented |
| RL-10: Cybersecurity policy, incident log, Reg S-P customer-information safeguarding evidence | cyber | CCO + IT lead | outstanding | producible | Reg S-P 2024 amendments operative on December 3, 2025 (firm is larger entity); compliance build-out evidence being assembled |
| RL-11: Best-execution committee minutes and broker-evaluation analyses for review period | 204-2 | head of trading | received | producible | Quarterly committee minutes; recommendation chained to `best-execution-surveillance` |
| RL-12: Custodian-fee billing and adviser-fee billing reconciliation evidence | 206(4)-2 / 204-2 | COO | received | producible | Quarterly reconciliations pulled |
| RL-13: Side-letter inventory and most-favoured-nation election process for the two private funds | 204-2 / private-fund | GC + COO | clarifying-question | under-review | Item text scope reaches some material the firm reads as not within the routine-exam scope; clarifying question to EIC |
| RL-14-18: [additional items on AML — n/a, IA-only firm; valuation; affiliated-transactions; service-provider DDQs; insurance-and-bond] | various | various | mixed | various | |

The document-handling and privilege block (engagement-side scaffolding chained to `exam-brief`) sits at the front of the matrix: production channel is SEC EDS; privilege-review-lead role is GC; privilege log required; redaction workflow is counsel-supervised, burned-in, metadata stripped, reviewer named per document; deduplication hash-based at production-package level; production log on the compliance shared drive in the exam-cycle folder. CSI handling: the prior-exam deficiency letter is on file; the readiness pack reads at the firm's GC-and-CCO access population and is not carried at the lower production-team population.

##### Part B — Domain-by-domain readiness

Form ADV lane: item-by-item current-state read complete. One Item 5.L. inconsistency flagged — the firm's actual marketing inventory includes a third-party-rating logo on the website that the Form ADV response does not currently reflect; remediation path is an interim Form ADV amendment before production (severity `critical`).

Rule 206(4)-7 lane: 2024 and 2025 annual review reports on file. The 2025 report's testing methodology section is light on the off-channel-communications testing line; the in-flight surveillance refresh is referenced but not described. Reviewer-question prep for the CCO on the 206(4)-7 testing methodology pre-positions the talking point that the testing is in flight, the surveillance refresh is a self-identified issue, and the next annual review will carry the refreshed methodology.

Rule 204A-1 lane: three Code of Ethics violation-log entries in the review period; enforcement-action evidence on file for each (one written warning, one mandatory training and disgorgement, one supervisory letter). The CCO's mock-interview prep carries the enforcement narrative.

Rule 206(4)-2 lane: surprise-verification reports issued 87 and 94 days after test date in the two years — both within the 120-day window. SLOA inventory at review-period end has 47 authorisations, all classified as non-custody under the staff no-action framework with the authorisation language pinned per relationship. Private-fund audit alternative used for both funds; audited financials delivered to investors 89 and 102 days after fiscal-year end — both within the 120-day window. Qualified-custodian relationships pinned per account; one sub-custody arrangement in the EU is reviewed and the firm's classification is supported by the custodial agreement language. No `critical` gaps; one `medium` observation on the SLOA-inventory cadence (currently quarterly; EXAMS Risk Alert observations suggest monthly is the emerging expectation; remediation path is a cadence change rather than a finding response).

Rule 206(4)-1 lane: chained to `marketing-rule-evidence`. The substantive evidence pack reads against the September 2023 enforcement-sweep pattern. Two material gaps: (i) the hypothetical-allocation deck flagged in self-identified issues has the (d)(6)(i) audience-appropriateness procedure documented but light on the (d)(6)(iii) risks-and-limitations disclosure for the backtest-specific risks; remediation path is a disclosure refresh and a calculation-worksheet pin (severity `high`). (ii) the third-party-rating logo on the website lacks the rating-period and methodology disclosure under (d); remediation path is an immediate website update and the Form ADV Item 5.L. amendment above (severity `high`). The (c) ineligible-person screen for the testimonials on the website was run at agreement and the firm's continuing-basis cadence is annual; the most recent screen is within the cadence.

Rule 204-2 lane: books-and-records evidence index per item; calculation worksheets pinned for the performance composites and the hypothetical-allocation deck. The (a)(11) and (a)(16) recordkeeping for the hypothetical reaches the gap above. Electronic-records standards under §275.204-2(g) are met; the firm runs an audit-trail-alternative system rather than WORM.

Form PF lane: Filings on file; firm files as non-large hedge fund adviser (the two private funds are below the large-hedge-fund threshold). The 2023 amendments' current-event reporting framework is incorporated in the firm's Form PF triggering-event monitoring posture; no current-event reports filed in the review period.

Cyber and Reg S-P lane (`cross-cutting.md#cyber` overlay): firm is a larger entity for Reg S-P 2024 amendments (December 3, 2025 compliance date — past at exam time). Customer-information safeguarding policy refreshed for the operative amendments; incident-response posture documented; FTC-Safeguards-style reach addressed via the firm's vendor-management framework. Policy text scrubbed for any references to the withdrawn adviser-and-fund cyber proposal (Release IA-5956 / IC-34497, withdrawn June 12, 2025) and the withdrawn Predictive Data Analytics proposal (Release 34-97990 / IA-6353, withdrawn June 12, 2025); two policy paragraphs flagged for refresh and routed to the remediation list with `high` severity for closure before production.

Names Rule lane: not in scope (no registered investment companies; the private funds are not 35d-1 reach).

##### Part C — Mock-interview prep

Four interviewees:

- **CCO** — anticipated topics: 206(4)-7 annual-review methodology and testing depth; off-channel-communications surveillance posture and the in-flight refresh; Code of Ethics enforcement narrative; Marketing Rule definitional posture for one-on-one communications; tone-from-the-top on the firm's emerging-risk awareness. Counsel attending. Off-limits topics: any matter under outside-counsel privileged review (CCO redirects to GC). Prep session two weeks before fieldwork.

- **GC** — anticipated topics: privilege posture for the counsel-led off-channel investigation; document-handling and the production-log discipline; Form ADV material-change posture; side-letter and MFN administration for the two private funds; conflict-disclosure framework. Counsel attending. Off-limits topics: matters for which the firm has not received a clarifying response from the EIC on RL-13.

- **Head of trading** — anticipated topics: trade allocation methodology including IPO and limited-allocation deviations; principal-trading and cross-trading posture (n/a in the review period — head of trading carries the firm's no-principal-trades evidence); best-execution evaluation framework; the recurring EXAMS theme on conflicted-routing flow (n/a for an institutional-only book with no PFOF or affiliated brokerage; the head of trading carries the documentation that establishes the absence). Counsel not attending. Off-limits topics: specific client names; counterparty-confidential terms.

- **Head of investment operations** — anticipated topics: SLOA classification methodology; valuation policy application for the SMA book and for the two private funds; Form PF triggering-event monitoring; custodian-fee and adviser-fee reconciliation; the firm's posture on digital-asset exposure (the SMA book has no direct digital-asset positions; the private funds have a small allocation to a tokenised-securities sleeve; the head of investment operations carries the custody-rule-application evidence for that sleeve, including the qualified-custodian determination, which is the recurring EXAMS theme on custody-rule application to digital assets). Counsel attending where the digital-asset line comes up. Off-limits topics: specific portfolio-company names in the private funds.

Conduct themes (`cross-cutting.md#conduct` overlay) sit across roles: IA Act §206 fiduciary duty framing; conflict-disclosure discipline; code-of-ethics escalation discipline; tone-from-the-top on Marketing Rule and on off-channel-communications.

##### Part C addendum — Anticipated reviewer questions tied to recent enforcement themes

- "Walk us through the firm's electronic-communications surveillance posture, what the firm has done about off-channel-communications use, and how the firm tests its surveillance is working." — Source pattern: sustained off-channel-communications enforcement line across BD and IA registrants 2021 onward; recurring EXAMS focus. Talking-point anchor: Electronic Communications Policy v3.2; personal-device attestation program; periodic surveillance reports; counsel-led internal investigation in flight (privilege posture set in advance); incident-response procedure for identified off-channel use.

- "How does the firm operationalise the Marketing Rule's books-and-records reach for one-on-one communications that constitute advertisements, and what is the firm's testimonial-substantiation file for the website testimonials?" — Source pattern: SEC Marketing Rule 206(4)-1; September 2023 enforcement sweep against nine advisers on hypothetical-performance violations; recurring EXAMS focus per the 2022 and 2023 EXAMS Risk Alerts. Talking-point anchor: the firm's definitional posture for one-on-one advertisements (CCO/GC scoping in flight); the calculation-worksheet retention; the (c) ineligible-person screen cadence; the third-party-rating disclosure remediation path.

- "For the small allocation to tokenised-securities in the private funds, what is the firm's custody-rule application — qualified-custodian determination, surprise-verification reach, account-statement-delivery — and how is that posture documented?" — Source pattern: emerging EXAMS focus on custody-rule application to digital assets; recurring questions in private-fund-adviser exams. Talking-point anchor: the firm's qualified-custodian determination memo for the tokenised-securities custodian; the surprise-verification scope including the tokenised positions; the audited-financials delivery for the funds covering the positions; the firm's posture on the staff no-action framework as it has been applied to the tokenised-securities space [verify operative state at exam time].

- "Describe the firm's AI-use posture in research, marketing, and client communications." — Source pattern: SEC EXAMS focus on AI / predictive-analytics use in advisory work; the Predictive Data Analytics proposal (Release 34-97990 / IA-6353) was withdrawn June 12, 2025 but EXAMS continues to read AI-use posture under existing IA Act §206 fiduciary-duty and Rule 206(4)-7 frameworks. Talking-point anchor: the firm's AI Use Policy; prohibited-use list; books-and-records protocol for AI-assisted outputs; CCO review for AI-generated marketing.

- "How does the firm's Reg S-P 2024 customer-information safeguarding posture map to the operative compliance dates, and how is the firm testing the incident-response notification framework?" — Source pattern: Reg S-P 2024 amendments (Release 34-100155, May 16, 2024); compliance December 3, 2025 (larger) / June 3, 2026 (smaller); operative compliance date past for this firm at exam time. Talking-point anchor: the firm's Reg S-P refresh; the incident-response runbook; the customer-notification template; the table-top exercise documentation.

##### Part C addendum — Strategy posture

Posture is cooperative: the firm produces what is asked, on time, with the privilege calls clean and the production log discipline tight. The firm does not produce documents the request list does not reach (document-only-when-asked); GC routes responses (no role other than the CCO and the GC corresponds with the EIC; substantive business-side roles speak only in the scheduled interviews). The firm does not interpret the request list expansively; clarifying questions are routed to the EIC where item text is ambiguous (the side-letter / MFN line on RL-13 is the named example).

##### Part D — Gap and remediation list

Per gap: gap ID, domain, severity (`critical` / `high` / `medium` / `low`), description, owner role, due date, evidence required, status. Calibrated to exam-exposure risk:

- **GAP-01 — `critical`** — Form ADV Item 5.L. inconsistency on third-party-rating use. Owner: CCO. Due: before first production (14 days from notification). Evidence required: interim Form ADV amendment filed; updated Item 5.L. response in the production folder. Status: in flight.
- **GAP-02 — `critical`** — two policy paragraphs in the cybersecurity policy reference the withdrawn 2022 adviser-and-fund cyber proposal and the withdrawn 2023 Predictive Data Analytics proposal. Owner: CCO. Due: before first production. Evidence required: refreshed policy text pinned to operative anchors (Reg S-P 2024; FINRA n/a; EXAMS Risk Alerts). Status: in flight.
- **GAP-03 — `high`** — hypothetical-allocation deck (d)(6)(iii) risks-and-limitations disclosure incomplete; (a)(11) and (a)(16) input-data trail partial. Owner: head of marketing; CCO as control owner. Due: before fieldwork (six weeks). Evidence required: disclosure refresh; calculation-worksheet pin with input-data source. Status: in flight; chained to `marketing-rule-evidence`.
- **GAP-04 — `high`** — third-party-rating logo on website lacks (d) rating-period and methodology disclosure. Owner: head of marketing. Due: immediate (before first production). Evidence required: website update; updated marketing-review-log entry; Form ADV amendment per GAP-01. Status: in flight.
- **GAP-05 — `high`** — off-channel-communications surveillance refresh in flight; counsel-led internal investigation privilege posture under outside-counsel consultation. Owner: CCO and GC jointly. Due: privilege posture before first production; surveillance-refresh build-out before fieldwork. Evidence required: privilege-log entries; refreshed surveillance methodology with the testing pattern documented. Status: in flight.
- **GAP-06 — `medium`** — SLOA inventory cadence quarterly against an EXAMS-Risk-Alert-implied monthly emerging expectation. Owner: COO. Due: post-exam. Evidence required: cadence-change memo to the file; the firm's testing methodology refresh in the next 206(4)-7 annual review. Status: scheduled.
- **GAP-07 — `medium`** — RL-13 side-letter / MFN scope clarifying question outstanding. Owner: GC. Due: response from EIC. Evidence required: clarifying-response correspondence; updated production posture. Status: clarifying question lodged with EIC.
- **GAP-08 — `low`** — 206(4)-7 2025 annual review report's testing-methodology section is light on the off-channel-communications testing line. Owner: CCO. Due: next annual review (post-exam). Evidence required: refreshed testing methodology in the 2026 report. Status: scheduled.

##### Exit-meeting prep and response posture

Exit meeting: anticipated findings include a possible deficiency on the Marketing Rule (d)(6)(iii) disclosure depth for the hypothetical-allocation materials and a possible recommendation on SLOA inventory cadence; the firm pre-positions a written response within the 30-day deficiency-letter window. Disagreement posture is limited; the firm intends to push back if the examiner suggests the off-channel-communications surveillance is inadequate without specific evidence (the firm's surveillance-refresh and the counsel-led internal investigation are the operative facts), with counsel-led written response if needed. Wells trigger is named as a contingency in the response-posture section but is not the operative track; outside counsel is on retainer for the contingent escalation if Wells signals appear.

Response posture: named response owner role is CCO for the cover letter and GC for any matter touching privilege or pointing toward Wells; response window 30 days from receipt of deficiency letter; remediation-plan template on the compliance shared drive; firm-board reporting per firm governance.

##### Post-exam follow-up

Lessons-learned session scheduled three weeks after exit; after-action record on the compliance shared drive in the exam-cycle folder; next-cycle preparation owner role is CCO. The post-exam refresh reaches the 2026 206(4)-7 annual review methodology, the SLOA inventory cadence change, and the Marketing Rule books-and-records reach for one-on-one communications.

Confidence label moves from `medium` to `high` once GAP-01 through GAP-05 close before production / fieldwork respectively.

#### Why this scenario matters

It tests the substantive readiness pack at the firm size and shape the bulk of SEC EXAMS routine adviser exams reach: a mid-sized SMA-plus-private-fund firm with no broker-dealer affiliate, a clean prior cycle, a self-identified issue in flight, and a request list that reaches every IA lane plus the operative cyber overlay. The example exercises:

- The Form ADV current-state cross-check catching a material-change inconsistency before production rather than after — the recurring failure mode that drives the `critical` severity calibration.
- The Code of Ethics enforcement-evidence pairing — violation-log entries plus the enforcement-action evidence on the file, not just the log.
- The Custody Rule predicate-by-predicate read — surprise-verification cadence, qualified-custodian relationships including a sub-custody arrangement, SLOA inventory with the authorisation language pinned, private-fund audit-alternative delivery within the 120-day window — with the digital-assets line as the emerging-EXAMS-theme overlay.
- The Marketing Rule chain to `marketing-rule-evidence` for the substantive evidence pack and the September 2023 enforcement-sweep pattern; the Form ADV Item 5.L. cross-check sitting in this lane.
- The privilege and CSI posture — the counsel-led off-channel-communications internal investigation as the high-stakes line, with the privilege call set before production rather than improvised at the production deadline.
- The cyber lane scrubbed of references to the withdrawn 2022 adviser-and-fund cyber proposal and the withdrawn 2023 Predictive Data Analytics proposal; Reg S-P 2024 as the operative anchor.
- The strategy posture — cooperative, document-only-when-asked, GC routes responses — pre-positioned in the pack rather than negotiated in flight.

#### Pattern derived from

Public sources include the SEC's published examination process overview at https://www.sec.gov/exams; the SEC Division of Examinations' annual examination-priorities documents; the September 2023 enforcement-sweep public materials on hypothetical-performance violations [verify exact release count and dates]; the EXAMS Risk Alerts on the Marketing Rule (September 2022; June 2023 [verify exact date and title]); the EXAMS Risk Alerts on the Custody Rule (including the 2017 SLOA-focused alert); off-channel-communications enforcement actions across BD and IA registrants 2021 onward; Reg S-P 2024 final rule release (Release 34-100155); the SEC's June 12, 2025 withdrawal of the proposed adviser-and-fund cyber rule (Release IA-5956 / IC-34497) and the Predictive Data Analytics proposal (Release 34-97990 / IA-6353) from the regulatory agenda; the SEC's March 14, 2025 Names Rule extensions and the February 2026 Form N-PORT extension. Verify exact public-source pins on the analysis date.

## troubleshooting

### Troubleshooting: adviser-exam-readiness

Recurring failure modes the readiness sprint should preempt. Each is a finding pattern EXAMS or FINRA staff are likely to surface; the pack is structured to make each visible rather than letting it clear into the document-request submission or the mock interview.

#### 1. Form ADV staleness against the firm's actual state

Form ADV Part 1A and Part 2A are the first things an EXAMS team reads. Material changes the firm did not amend — disciplinary disclosure (Item 11), business activities (Item 6 / 7), affiliated service providers (Item 7.A), regulatory AUM and account counts (Item 5), custody (Item 9), and the marketing inventory (Item 5.L.) — surface immediately when the request-list submission lines up against the current Form ADV. The "we will fix it on the next annual amendment" posture does not survive contact with the request list; the rule reaches material changes, not annual cycles.

Fix: Part B's Form ADV lane runs an item-by-item current-state read against the most recent filing and against the firm's actual operating state. Material-change inconsistencies route to the gap-and-remediation list with `critical` severity if the document-request submission would expose them, and a Form ADV-W or interim amendment is in the remediation path before submission.

#### 2. Code of Ethics violations on the log without enforcement evidence in the file

Rule 204A-1 requires the firm to receive personal-trading reports, identify violations, and address them. The recurring finding pattern is the violation-log column populated without a paired enforcement-action column: the personal-trading review caught the violation, the CCO logged it, and the file does not show what the firm did. EXAMS reads the gap as a tone-from-the-top issue and an internal-controls issue at once.

Fix: Part B's Code of Ethics lane pulls the violation log and the paired enforcement-action evidence (memo to file, escalation, training requirement, disgorgement, supervisory letter) for every entry. Entries without enforcement evidence route to the gap list with `high` severity. The mock-interview prep for the CCO carries the enforcement narrative for at least two recent violations as a talking-point anchor.

#### 3. Custody Rule misapplication — surprise-audit timing, qualified-custodian arrangements, related-party limits

Rule 206(4)-2 has multiple operational predicates that fail in routine ways: the surprise-verification was scheduled within the rule's annual cadence but the prior-year report was issued more than 120 days after the test date; the "qualified custodian" relationship for a particular account is a sub-custody arrangement that does not satisfy the rule; the SLOA inventory has authorisations the firm classified as non-custody under the staff no-action framework but the authorisation language reaches discretion that takes the relationship out of the no-action posture; the private-fund audit alternative was used but the audited financials were not delivered to investors within the rule's 120-day window. Each is a recurring EXAMS finding.

Fix: Part B's custody lane runs each predicate explicitly: surprise-verification cadence and report-issuance dates against the rule's 120-day window; qualified-custodian status per relationship pinned to the custodial agreement (not just the firm's classification); SLOA inventory with the authorisation language pinned and the no-action-letter classification justified per relationship; private-fund audit alternative with the audit-delivery evidence per fund. Predicate failures route to the gap list with `critical` severity.

#### 4. Marketing Rule pre-approval and substantiation gaps

Rule 206(4)-1(b) general prohibitions and (e) recordkeeping reach beyond the disclosure mechanics. The recurring patterns: pre-approval workflow missing for a sub-population of advertisements (a slide deck circulated by an institutional relationship manager bypassed the marketing-review queue); performance-presentation calculation worksheets cannot be produced for a hypothetical-performance series in a deck (the calculation lives in an analyst's working file, not in the books-and-records system); testimonial-substantiation file is incomplete (the (c) screen for ineligible persons was run at on-boarding but the continuing-basis cadence the firm's policy specifies has not been met); third-party-rating logos in the firm's website carry no rating-period or methodology disclosure. EXAMS reads against (b), (c), (d), and (e) at once.

Fix: Part B's Marketing Rule lane chains to `marketing-rule-evidence` for the substantive evidence pack; this lane reads the evidence index and the gap list back into the readiness pack. The Form ADV Item 5.L. cross-check sits in this lane. Gaps route to the remediation list with severity by the September 2023 enforcement-sweep pattern: `critical` on (d)(6) hypothetical-performance pre-conditions, `high` on (c) testimonial / endorsement disclosure clauses and on (e) recordkeeping, `medium` on (b) general prohibitions where the disclosure mechanics tick the boxes but the framing is materially misleading by implication.

#### 5. Privilege and CSI handling in document production

Two failure modes in opposite directions. (i) Over-claiming privilege — counsel-reviewed annual-review reports under Rule 206(4)-7 are produced with the entire counsel-review section redacted on a privilege theory the staff will not accept; the production log lists the redactions but not the basis, and the privilege log is itself producible. (ii) Under-claiming privilege — attorney-client material from a counsel-led internal investigation (off-channel-communications surveillance is the recurring example) is produced without redaction because the operations team owning the production-log workbook did not flag the document to GC. Either failure carries forward into the next regulatory cycle: over-claim erodes credibility on subsequent privilege calls, under-claim waives privilege over the underlying matter.

Fix: Part A's document-handling-and-privilege block is the engagement-side scaffolding; this skill chains to `exam-brief` for the operative process. The readiness pack pre-stages the privilege posture on each request-list item before production: `producible` / `redacted-and-producible` / `under-review` / `privileged-withheld`. GC owns the privilege call; the CCO owns the production log; outside counsel signs the privilege-confirmation block on items where engaged. Items in `under-review` posture at the production deadline route to the gap list with `critical` severity.

#### 6. Cyber and predictive-data-analytics policy posture written against withdrawn proposals

The SEC withdrew the proposed adviser-and-fund cyber rule (Release IA-5956 / IC-34497, proposed Feb 9, 2022) and the Predictive Data Analytics Rule (Release 34-97990 / IA-6353, proposed July 26, 2023) from the regulatory agenda on June 12, 2025. Firms that drafted policies in 2023-2024 against the proposed-rule frameworks now carry policy text referencing rule sections that do not exist. Reg S-P (May 16, 2024 amendments; compliance December 3, 2025 for larger entities, June 3, 2026 for smaller) is the operative customer-information safeguarding rule. EXAMS will read policy text against operative rules; references to proposed-rule frameworks read as either staleness or confusion about current state.

Fix: Part B's cyber lane (`cross-cutting.md#cyber` overlay) pins the operative anchors — Reg S-P 2024, NYDFS Part 500 where in scope, FINRA cyber guidance, EXAMS cyber Risk Alerts, the SEC Cybersecurity Risk Management / Form 8-K Item 1.05 rule for the listed parent if applicable. Policy text referencing the withdrawn 2022 cyber proposal or the withdrawn 2023 Predictive Data Analytics proposal routes to the gap list with `high` severity for refresh before submission. The pack does not prepare the firm to defend a posture against withdrawn proposals; it prepares the firm to defend the operative state.

#### 7. Names Rule (Rule 35d-1) compliance dates the firm has not tracked through extensions

The Sept 20, 2023 amendments expanded the 80% policy reach (including to ESG-themed names), extended the rule to closed-end funds, and tightened the deviation-and-correction framework. Compliance dates have moved twice: the SEC March 14, 2025 extension set large fund groups ($1B+ net assets) at June 11, 2026 and smaller groups at December 11, 2026; a February 2026 further extension moved the Form N-PORT Names Rule reporting (only) to November 17, 2027 (large) / May 18, 2028 (smaller). Firms preparing for an exam falling across these dates carry one of three failure modes: policy text written against the original December 11, 2025 / June 11, 2026 dates; 80% basket testing not yet stood up because the firm assumed the rule's reach to its name had been deferred; Form N-PORT reporting build-out treated as on the same compliance schedule as the underlying rule.

Fix: Part B's fund-adviser lane (where in scope) carries the per-fund-family Names Rule applicability call, the firm's compliance-date posture against the operative extensions, the 80% basket-testing methodology and current-period results, and the deviation-and-correction inventory. The Form N-PORT reporting build-out is tracked separately on the operative extended schedule. Items off the operative schedule route to the gap list with severity calibrated to the firm's nearest compliance date in the exam-review window.
