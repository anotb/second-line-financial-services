# Example: QA review of a Reg E error-resolution workpaper at a regional bank

Public-source-derived. No named institution. Mirrors the standard QA pass over a completed Reg E §1005.11 error-resolution testing workpaper.

## Input

- **QA scope**: full-review, in-cycle QA before workpaper closure.
- **Workpaper under review**: completed Reg E error-resolution workpaper for Q1 2026 testing cycle (workpaper ID `WP-2026-Q1-RegE-001`, test ID `TP-CMP-RegE-2026-01`, control ID for the dispute-resolution control). Workpaper concluded design effective and operating partially-effective.
- **Engagement scope supplied**: institution = regional state member bank; primary regulators = FRB, CFPB, state DFI; persona = QA reviewer (independent of the workpaper reviewer); source posture = public-plus-firm-policy-plus-evidence; sector overlay = banking; cross-cutting overlays = conduct (consumer-facing).
- **Inputs to the QA reviewer**: the workpaper, the underlying exception register (`ER-CMP-RegE-2026-01` from `exception-analysis`), the test plan, the firm CMS testing methodology, source-anchor file pointers (AICPA AU-C 230 / 530 / 265, IIA Standard 1300 and 2340, CFPB CMS examination procedures, conduct cross-cutting overlay).

## Output sketch

The skill produces an Excel workbook (review-markup tabs) plus a Word QA memo. Headlines from the memo:

### Executive summary

- **Decision: return for rework.** Six deficiencies identified: one critical, two major, three minor. Critical deficiency on reviewer-separation returns the workpaper.
- Severity recalibration requested on three exceptions; firm methodology floor for §1005.11(c) timing is high, preparer rated medium.
- Conclusion language requires rewrite from legal-violation framing to control-effectiveness framing; legal question routes to legal counsel and head of regulatory affairs separately.

### Deficiency findings

- **D1 (critical, reviewer-separation).** Section: sign-off block. Observation: preparer and workpaper reviewer roles are the same on the sign-off block; both signed as "compliance-testing analyst". Methodology reference: firm methodology, IIA Standard 2340 [verify section] engagement supervision. Required action: return workpaper; reassign reviewer to a separate role (compliance-testing manager); re-sign.
- **D2 (major, evidence-reliability and exception-classification).** Section: samples S12-S14. Observation: three sample items in the workpaper's sample-results table show "investigation completed" with no evidence ID; the underlying exception register did not flag them as evidence gaps (no exception X-flagged for these samples). Methodology reference: AICPA AU-C 500 [verify paragraph], firm methodology evidence-reliance posture. Required action: preparer to attach evidence ID per sample item or reclassify as evidence-gap exceptions in the register; re-aggregate deviation rate accordingly.
- **D3 (major, conclusion-support).** Section: conclusion. Observation: conclusion language reads "the bank did not comply with Reg E §1005.11(c)" — legal-violation framing. Methodology reference: firm methodology, conduct cross-cutting overlay. Required action: rewrite to control-effectiveness language: "the dispute-resolution control did not operate within the §1005.11(c) timing clock for [population] sample items during the period". Route legal question to legal counsel and the head of regulatory affairs separately.
- **D4 (minor, criteria-sufficiency).** Section: scope and source posture. Observation: missing population reconciliation total. Methodology reference: firm methodology, banking sector overlay (population definition convention). Required action: add population reconciliation row showing the count of disputes received during the period reconciled against the case-management system extract.
- **D5 (minor, evidence-reliability).** Section: evidence inspected E2. Observation: missing reliance classification on case-management system extract; the extract is the population basis but is not classified. Methodology reference: firm methodology, AICPA AU-C 500 [verify paragraph]. Required action: classify as system-of-record extract; add extract date and run-by role to the evidence-inspected table.
- **D6 (minor, exception-classification).** Section: aggregation and projection. Observation: aggregation section missing stratum-level breakdown though sample was stratified by dispute type. Methodology reference: firm methodology. Required action: add stratum-level breakdown table.

### Sample re-perform results

- QA re-performed five sample items (S5, S12, S18, S22, S29) selecting from across the dispute-type stratification. Re-perform identified one divergence: sample S12 re-perform showed a deviation the preparer recorded as "pass" on procedure P2 (investigation timeline). The divergence routes into D2 and adds to the workpaper's deviation count.
- Re-perform on S22 confirmed the preparer's exception identification and classification.

### Severity calibration

- Three exceptions in the workpaper rated medium for §1005.11(c) timing deviations. Firm methodology floor for §1005.11(c) timing is high (per firm policy version effective on the test period). Severity inflation requested: re-rate the three exceptions to high. Two analogous prior workpapers (Q4 2025 and Q3 2025) carried the same exceptions rated high; the rating drift in the Q1 2026 workpaper is inconsistent with the prior cycle.
- One exception (X4, evidence-gap on a single sample item) rated low. No floor violation; consistent with prior cycles. No change.

### Conclusion support

- Design effectiveness: supported. Walkthrough evidence and procedure outcomes carry the design read.
- Operating effectiveness: partially-supported. Aggregation reads against tolerable rate, but conclusion language drifts to legal-violation framing — see D3. Once the language is corrected and the severity rebase is applied, the underlying evidence supports a partially-effective operating finding.

### Decision

- **Decision: return for rework.** Critical deficiency on reviewer-separation returns the workpaper.
- **Rework items**: re-sign with separate reviewer role (D1); attach evidence ID or reclassify samples S12-S14 (D2); rewrite conclusion language to control-effectiveness framing (D3); add population reconciliation, evidence reliance classification, and stratum-level breakdown (D4-D6); rebase three exceptions to high severity per firm methodology floor.
- **Issue closure approval status**: not-applicable (the workpaper is not yet through closure, and any open issues identified in the workpaper carry their own remediation lifecycles).

### Reviewer questions

- Q1: should the §1005.11(c) timing deviations elevate to issue, given the severity rebase to high? — workpaper reviewer plus testing manager.
- Q2: is the segment-level re-test a separate workpaper or a re-issue of this one? — workpaper reviewer.

### QA confidence label

- High. Sample re-perform was completed for five items (one divergence identified), methodology references applied across all eight QA dimensions, deficiencies cross-checked against firm methodology and the analogous prior workpapers.

## Why this scenario matters

- **Boundary check on reviewer separation.** A critical deficiency that returns the workpaper. Reviewer separation is a structural QA dimension, not advisory.
- **Boundary check on severity calibration.** Severity inflation requested in this case (rebase up from medium to high); the same rationale-field discipline catches deflation in other cases.
- **Boundary check on conclusion-language hygiene.** Legal-violation framing is a recurring deficiency on consumer-facing workpapers; the QA reviewer rewrites and routes the legal question separately.
- **Boundary check on QA versus issue closure.** The QA decision (return for rework) is distinct from any issue closure decision; the workpaper carries open issues that have their own remediation lifecycles regardless of QA outcome.
- **Boundary check on QA re-perform.** QA re-perform on five sample items identified one divergence the preparer missed; the QA review note routes the divergence into a deficiency rather than letting it pass.

## Anchors

- AICPA AU-C 230 (Audit Documentation).
- AICPA AU-C 265 (Communicating Internal Control Related Matters).
- AICPA AU-C 530 (Audit Sampling) §A18-§A22 [verify paragraph references].
- IIA Standard 1300 [verify section labels] (QAIP) and Standard 2340 [verify section labels] (engagement supervision).
- Reg E — 12 CFR Part 1005, especially §1005.11.
- CFPB CMS examination procedures.
- Conduct cross-cutting overlay (this skill).

See `references/source-anchors.md`, `references/sector-overlays/banking.md`, and `references/cross-cutting/conduct.md` for full citations.
