# QA review note — content spec

The QA review pack ships as two artifacts:

1. **Excel workbook** — review-markup tabs over the workpaper, rendered via the `xlsx` skill in `document-skills`.
2. **Word memo** — QA review summary, rendered via the `docx` skill in `document-skills`.

This file is the named-section spec for both. The skill emits the populated content; the rendering skills produce the practitioner-natural deliverable.

---

## Artifact 1: Excel workbook (QA markup)

A workbook with the tabs below. Each tab is a review-markup overlay on the workpaper, not a re-creation of the workpaper itself. The QA reviewer fills the QA columns; the workpaper's original content sits in adjacent columns for reference.

### Tab 1: `QA-header`

Single-row header pinning the QA review to the workpaper.

| Field | Value |
|---|---|
| QA review ID | [stable ID per firm naming convention] |
| Workpaper ID | [foreign key into `workpaper-drafter` output] |
| Test ID | [foreign key into `test-plan-builder` output] |
| Control ID | [firm control register ID] |
| Period under test | [start date — end date] |
| Preparer (role) | [from workpaper] |
| Workpaper reviewer (role) | [from workpaper] |
| QA reviewer (role) | [separate from preparer and workpaper reviewer] |
| QA scope | full-review / targeted-re-review / post-issue-re-qa / examiner-prep-sweep |
| QA date | [ISO date] |
| Engagement ID | [pointer to scope record, or "none — scope not formalised separately from test plan"] |
| Decision | accept / return-for-rework / conditional-accept (filled at sign-off) |
| Confidence label | high / medium / low / unknown |

### Tab 2: `QA-criteria`

The QA methodology references this review applied. One row per reference.

| QA criterion ID | Source | Section | Excerpt or paraphrase | Use in this review |
|---|---|---|---|---|
| QC1 | AICPA AU-C 230 | §08-§14 [verify] | experienced-auditor sufficiency standard | evidence sufficiency dimension |
| QC2 | AICPA AU-C 530 | §A18-§A22 [verify] | evaluating sample results | sample integrity and exception evaluation dimensions |
| QC3 | IIA Standard 1300 [verify] | QAIP | quality assurance and improvement program | QA scope and reviewer challenge dimensions |
| QC4 | IIA Standard 2340 [verify] | engagement supervision | review-before-issuance | reviewer separation dimension |
| QC5 | AICPA AU-C 265 | [verify] | severity hierarchy | severity calibration dimension |
| QC6 | Firm methodology | [section] | severity floors and reviewer-separation policy | severity calibration and reviewer separation dimensions |

### Tab 3: `Deficiencies` (the load-bearing tab)

One row per deficiency the QA reviewer found. The named-dimension columns let the QA review note read by category.

| Deficiency ID | Section affected | Category | Severity | Observation | Methodology reference | Required action | Original-workpaper text (if reproducing) | QA reviewer initials | Status |
|---|---|---|---|---|---|---|---|---|---|
| D1 | sign-off block | reviewer-separation | critical | preparer and reviewer roles are the same on the sign-off block | firm methodology, IIA Standard 2340 | return workpaper; reassign reviewer to a separate role; re-sign | | | open |
| D2 | sample S12-S14 | evidence-reliability | major | three sample items show "investigation completed" with no evidence ID; exception register did not flag them as evidence gaps | AICPA AU-C 500 [verify], firm methodology | preparer to attach evidence ID per sample item or reclassify as evidence-gap exceptions | | | open |
| D3 | conclusion section | conclusion-support | major | conclusion language reads "the bank did not comply with Reg E §1005.11(c)" — legal-violation framing | firm methodology, conduct overlay | rewrite to control-effectiveness language; route legal question to legal counsel separately | | | open |
| D4 | population definition | criteria-sufficiency | minor | missing population reconciliation total | firm methodology | add population reconciliation row to scope section | | | open |
| D5 | evidence inspected E2 | evidence-reliability | minor | missing reliance classification on case-management system extract | firm methodology, AICPA AU-C 500 [verify] | classify as system-of-record extract; add extract date and run-by role | | | open |
| D6 | aggregation section | exception-classification | minor | aggregation section missing stratum-level breakdown though sample was stratified | firm methodology | add stratum-level breakdown table | | | open |

Category enum (one of):

- `scope-alignment` — workpaper scope diverges from test plan without sign-off
- `criteria-sufficiency` — source criteria missing, miscited, or unsupported
- `evidence-reliability` — evidence reliance classification missing, weak, or unjustified
- `procedure-execution` — procedure not executed as designed without sign-off on workaround
- `exception-classification` — exception register treatment fails the workpaper's classification standard
- `conclusion-support` — conclusion not supported by evidence and procedures
- `severity-calibration` — severity ratings inflated, deflated, or not against firm methodology floor
- `reviewer-separation` — preparer-reviewer-QA role overlap
- `remediation-handoff` — issue handoff package incomplete or absent
- `formatting` — readability, table integrity, missing IDs (minor by default)

Severity enum:

- `critical` — workpaper must be returned (reviewer-separation breaks, fundamental conclusion failures)
- `major` — rework required, can re-issue (evidence-reliability, conclusion-support, severity-floor violations)
- `minor` — note for future cycles (formatting, missing reconciliation totals, stylistic items)

### Tab 4: `Sample-re-perform`

Where the QA reviewer re-performed selected sample items, the comparison of QA finding to original finding. One row per re-performed item.

| Sample ID | Procedure ID | Original outcome (from workpaper) | QA outcome (re-perform) | Divergence flag | QA notes |
|---|---|---|---|---|---|
| S5 | P1 | pass | pass | no | re-perform confirmed |
| S12 | P2 | pass | exception | yes | preparer missed deviation; route to D2 |
| S18 | P1 | pass | pass | no | re-perform confirmed |
| S22 | P3 | exception | exception | no | re-perform confirmed; classification consistent |
| S29 | P1 | pass | pass | no | re-perform confirmed |

Notes: QA re-perform is the most credible QA dimension. Where re-perform identifies a deviation the preparer missed, the divergence is a deficiency on the sample-results tab and adds to the deficiency register on Tab 3.

### Tab 5: `Severity-calibration`

Comparison of preparer's severity ratings against firm methodology floors and against analogous prior workpapers.

| Exception ID (from workpaper) | Preparer severity | Firm methodology floor | Floor violation? | Analogous prior workpapers | QA proposed severity | QA commentary |
|---|---|---|---|---|---|---|
| X1 | medium | high (per firm methodology for §1005.11(c) timing) | yes | WP-2025-Q4-RegE rated high for similar timing deviation | high | severity inflation requested; reroute to D-severity deficiency |
| X2 | medium | medium | no | consistent with WP-2025-Q3 | medium | no change |
| X3 | low | low | no | consistent | low | no change |

### Tab 6: `Conclusion-support`

Statement on whether the conclusion is supported by the evidence and procedures, and the supporting trace.

| Conclusion element | Workpaper text (abbreviated) | Evidence trace (procedure IDs and evidence IDs) | QA assessment | QA rationale |
|---|---|---|---|---|
| Design effectiveness | effective | walkthrough, P1 design read | supported | walkthrough evidence and P1 procedure outcomes carry the design read |
| Operating effectiveness | partially-effective | sample S1-S60, P1-P3, exception register ER-2026-RegE | partially-supported | aggregation reads against tolerable rate, but conclusion language drifts to legal-violation framing — see D3 |
| Combined (if applicable) | not-effective | as above | partially-supported | rewrite required; underlying evidence supports a partially-effective finding once the language is corrected |

QA assessment enum: `supported` / `partially-supported` / `not-supported`.

### Tab 7: `Source-trace`

QA reviewer's own source trace. Distinct from the workpaper's source trace; this one carries the QA methodology citations applied to this review.

| QA claim | Source | Section | Date | URL or file ref |
|---|---|---|---|---|
| reviewer separation is structural | IIA Standard 2340 [verify] | engagement supervision | January 9, 2025 effective | references/source-anchors.md |
| severity floor on §1005.11(c) timing | firm methodology | [section] | [version effective] | references/firm-overlay.md |
| conclusion-language hygiene | conduct cross-cutting overlay | (this skill) | n/a | references/cross-cutting/conduct.md |

### Tab 8: `Reviewer-questions`

Questions for the workpaper reviewer (separate from the preparer and the QA reviewer) to address before re-submission. Each question names the decision it supports.

| Question ID | Question | Audience | Decision supported |
|---|---|---|---|
| Q1 | should the §1005.11(c) timing deviations elevate to issue, given the severity rebase to high? | workpaper reviewer | issue elevation per D2-related exceptions |
| Q2 | is the segment-level re-test a separate workpaper or a re-issue of this one? | workpaper reviewer plus testing manager | scope of rework |

---

## Artifact 2: Word memo (QA review summary)

The Word memo summarises the Excel workbook for an audience that will not open the workbook (the testing manager, internal-audit lead, the head of compliance). The memo carries the named sections below.

### Header

- QA review ID, workpaper ID, test ID, control ID, period, QA reviewer (role), QA date, decision (filled at sign-off).

### 1. Executive summary

Three to five bullets. The decision (accept, return for rework, conditional accept), the count of deficiencies by severity, the headline reason, and any examiner-prep posture if the QA scope is `examiner-prep-sweep`.

### 2. QA scope

Two to three sentences. What the QA covers (full workpaper, targeted re-review, post-issue re-QA, examiner-prep sweep), what it does not cover, and the methodology references (named QC criteria, link to Tab 2 of the workbook).

### 3. Deficiency findings (numbered)

Each deficiency expanded. For each:

- **Deficiency ID** (matches workbook Tab 3).
- **Section affected** (workpaper section or item).
- **Category** (one of the ten categories).
- **Severity** (critical / major / minor).
- **Observation** (what the QA reviewer saw, dated and scoped).
- **Methodology reference** (the criterion the workpaper failed against).
- **Required action** (declarative; what the preparer or workpaper reviewer must do).

Critical deficiencies sit at the top; the memo is read top-down by audiences who will stop reading once they see "return for rework".

### 4. Sample re-perform results

Where the QA reviewer re-performed selected sample items, a paragraph summary of the comparison: how many items re-performed, how many divergences identified, what the divergences imply for the workpaper's overall sample-results read.

### 5. Severity calibration

Statement on severity calibration: any floor violations identified, any analogous-prior-workpaper inconsistencies, the QA reviewer's commentary on calibration discipline this cycle. The workbook Tab 5 carries the row-level detail.

### 6. Conclusion support

Statement on whether the workpaper's conclusion is supported by the evidence and procedures: `supported` / `partially-supported` / `not-supported`, with the rationale. Where conclusion language requires rewrite, the memo carries the proposed rewrite or routes the rewrite to a deficiency.

### 7. Decision

- **Decision**: `accept` / `return-for-rework` / `conditional-accept`. Single sentence rationale.
- **Rework items** (populated when decision is conditional-accept or return-for-rework): bulleted list of specific items the preparer or workpaper reviewer must address before re-submission.
- **Issue closure approval status**: `approved` / `not-approved` / `not-applicable`. Statement that workpaper closure does not equal issue closure; issues identified in the workpaper carry their own remediation lifecycles in `issue-writeup` and downstream tracking.

### 8. Reviewer questions

Bulleted list of questions for the workpaper reviewer. Each question names the decision it supports. (Same content as workbook Tab 8, presented for the audience that reads the memo not the workbook.)

### 9. QA reviewer sign-off

- QA reviewer role and date.
- Escalation path if disagreement persists between QA and the workpaper reviewer (typically: testing manager, head of compliance testing, internal audit lead).
- Statement that human review is required: severity assignments, decisions, and conclusion-support assessments always carry human review by the QA reviewer's named role.

### 10. Source trace and confidence label

- Source trace: every material claim cites a source with section reference. `[verify section]` markers route to the next QA-methodology refresh.
- Confidence label: `high` / `medium` / `low` / `unknown`. Reflects evidence sufficiency for the QA review itself (sample re-perform completeness, methodology depth applied, time available for the review).

### Examiner-prep sweep variant

When QA scope is `examiner-prep-sweep`, the memo carries an additional section between sections 6 and 7:

### 6a. Population-level deficiency themes

Bulleted summary of common deficiencies across the workpaper population: methodology-drift patterns, recurring evidence-reliability failures, severity-floor violations across multiple workpapers. Names the recommendation seed for the next testing cycle (e.g., methodology refresh before next cycle, reviewer training, severity-floor reaffirmation).

The decision section then carries per-workpaper decisions in a small table:

| Workpaper ID | Decision | Rework items (if any) |
|---|---|---|
| WP-2026-Q1-TPRM-001 | accept | (minor noted) |
| WP-2026-Q1-TPRM-002 | conditional-accept | document KRI dashboard tie-out for critical-vendor monitoring |
| WP-2026-Q1-TPRM-003 | return-for-rework | rewrite critical-vendor monitoring conclusion; document SOC 2 reliance assessment |

---

## Rendering notes

- The Excel workbook tabs above map one-to-one to worksheet tabs. Column headers match the table headers above. Use freeze-pane on the header row of each tab. Conditional formatting on the `Severity` column (Tab 3) and the `Divergence flag` column (Tab 4) helps the workpaper reviewer scan.
- The Word memo follows the named sections above. Headings at H1 for the memo title, H2 for sections 1-10. Critical deficiencies bold-highlighted in section 3.
- Both artifacts emit together. The QA reviewer signs the Word memo; the workbook is the supporting documentation. Both are filed against the workpaper ID.

*QA depth scales to the workpaper depth and the QA scope.* A targeted re-review on a single section reads short; a full review of a high-volume workpaper with a high deficiency count reads longer. An examiner-prep sweep on a portfolio of workpapers reads as a portfolio QA review with population-level themes plus per-workpaper notes.

*Audience shapes the QA review pack.* A QA pack drafted for the testing manager reads operationally. A QA pack drafted with an examiner sweep in mind reads heavier on the population-level themes and the methodology-drift findings. A QA pack drafted for internal-audit reliance scoping reads heavier on the reviewer-separation evidence and the QA confidence label.
