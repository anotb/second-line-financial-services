---
name: adviser-exam-readiness
description: |
  Produces the substantive readiness pack an SEC-registered investment adviser, broker-dealer, dual registrant, fund adviser, or private-fund adviser carries through an SEC Division of Examinations or FINRA examination cycle. Walks the firm through Form ADV / Form CRS / Form BD cross-check, the Rule 206(4)-7 written compliance program, the Rule 204A-1 code of ethics lane, the Rule 206(4)-2 custody lane, the Rule 206(4)-1 Marketing Rule lane, Rule 204-2 books-and-records, Form PF (Rule 204(b)-1) where applicable, Reg BI and Form CRS for BDs and dual registrants, FINRA 3110 / 3120 / 3130 / 3310 supervision, and the cyber / Reg S-P slice that EXAMS now reaches for routinely. Audience is the chief compliance officer, the chief executive officer, general counsel, the designated FINRA supervisor for a BD or dual registrant, the BSA officer where AML is in scope, and the firm's external counsel.

  Best for:
  - An adviser, BD, or dual registrant has been notified of an SEC EXAMS routine, focused, for-cause, or sweep examination and needs a 2-6 week readiness sprint with a gap matrix, evidence index, mock-interview prep, and remediation list.
  - A CCO is preparing the annual mock-exam exercise as part of the Rule 206(4)-7 / Rule 38a-1 / FINRA Rule 3110 / 3130 review cycle.
  - A new CCO is doing a 90-day baseline assessment of the compliance program against current EXAMS priorities and Risk Alerts.
  - A consulting team is performing a pre-exam diagnostic for an adviser or BD client and needs the SEC-specific readiness lattice (not the generic exam-engagement playbook).
  - A private-fund adviser is reading the firm's posture against the post-PFA-Rule landscape (the PFA Rule was vacated June 5, 2024 and is not in force) and the operative Form PF 2023 / 2024 amendments (which remain in force as a separate rulemaking).
  - A registered-fund adviser is feeding readiness evidence into the Rule 38a-1 CCO annual report cycle for the fund board.

  Not the right tool when:
  - The work is the engagement-side scaffolding (entry-meeting choreography, document-handling, privilege posture, request-list mapping, interview-prep) for any FS exam. Use `regulatory-change-management/skills/exam-brief`; this skill chains with that skill, it does not duplicate it.
  - The work is mapping a specific new rule into firm policy (use `regulatory-change-management/regulatory-impact-assessment` or `rule-to-obligation-extraction`).
  - The work is the substantive Marketing Rule evidence pack itself (use `marketing-rule-evidence` in this plugin; this skill consumes that pack as an evidence pin).
  - The work is fund-board reporting or the §15(c) advisory-contract approval / renewal package (use `fund-board-reporting`).
  - The institution is a US bank, a non-bank consumer-finance entity, an insurer, or a payments/fintech firm not also SEC- or FINRA-registered. Use the matching sector-plugin readiness skill.
argument-hint: "[firm registration class, exam type, examining body, document-request scope and due date, prior-exam findings posture]"
---

# Adviser exam-readiness pack

The readiness pack is the artifact the firm's CCO, CEO, GC, designated FINRA supervisor, and BSA officer carry through an SEC EXAMS or FINRA examination. It is not the engagement playbook (who-routes-what, document-handling, privilege posture); that lives in `exam-brief`. It is the substantive readiness sprint: which IA Act / ICA / Exchange Act / FINRA rule lanes the exam reaches, what evidence the firm has against each lane, where the gaps sit, and what the senior officers need to be able to say in the mock interview.

The spine is the rule lattice for the firm's registration constellation — IA, BD, dual registrant, fund adviser, private-fund adviser. The pack is firm-confidential by convention; prior supervisory letters and prior deficiency letters constrain what can carry forward into a pack reading at a lower access population. The named lead attests; the pack is a draft until that step. The skill stops short of speaking for the firm to the regulator.

## Ask first

Settle these before drafting. Most exam cycles answer them in the first conversation; default and flag where they do not.

- **What is the firm's registration constellation.** SEC-registered investment adviser, FINRA-registered broker-dealer, dual registrant, fund adviser (registered investment company adviser), private-fund adviser, or some combination. Registration drives which rule lanes the pack walks: an IA-only firm runs Form ADV / 206(4)-7 / 204A-1 / 206(4)-2 / 206(4)-1 / 204-2; a BD adds Reg BI / Form CRS / FINRA 3110-3310 / 17a-3-4; a dual registrant runs both with the bridging conflicts; a private-fund adviser adds Form PF and reads the post-PFA-Rule landscape; a registered-fund adviser feeds into the Rule 38a-1 CCO annual report cycle.
- **What is the exam type, examining body, and document-request scope.** Routine, focused, for-cause, or sweep; SEC EXAMS, FINRA, or both; document-request item list and due date. Exam type calibrates the pack's depth: a focused exam reads as a thin spine on the topical lanes; a routine exam scopes broadly; a for-cause exam carries the for-cause-topic evidence first; a sweep exam tracks the EXAMS Risk Alert that triggered it.
- **What does the firm inherit at the start of the cycle.** Prior exam findings (open, partially-remediated, closed-pending-confirmation, closed); recent self-identified issues; recent enforcement themes from EXAMS or FINRA touching the firm's business. EXAMS revisits prior findings; the readiness check on prior-finding remediation status is high-priority.
- **What is the source posture and access population for the pack.** Public-only, public-plus-firm-policy, public-plus-firm-policy-plus-evidence, or connector-aware. Prior supervisory letters, prior deficiency letters, and Form ADV-NR responses constrain the pack's access population; do not carry CSI into a pack reading at a lower population.

When an `scope` record is supplied, consume it for firm registration constellation, persona, source posture, sector overlay (always capital-markets for this skill — see `references/sector-overlays/capital-markets.md`), and cross-cutting overlay set. When it is not supplied, ask the questions and default; flag the defaults in the pack.

## How the pack gets built

The pack has a four-part body around a cover. Walk it in the order the conversation surfaces evidence; the structured record sorts itself.

**Cover and engagement context.** Firm registration profile (legal name placeholder, SEC IA / FINRA BD registration numbers, retail-customer-serving status, AUM band, geographic footprint). Exam context (exam type, examining body, EXAMS region or FINRA district, notification date, document-request scope, due date, prior-exam findings status). Source posture and access population. Confidence label.

**Part A — Document-request response matrix.** Per requested item: request item, source location (system of record), evidence pin, reviewer role, status (`open` / `in-progress` / `ready-for-review` / `submitted`), due date, redaction-required flag. The matrix is the reviewer's working artifact; renderable as a tab-per-domain Excel workbook (Form ADV / 206(4)-7 / 204A-1 / 206(4)-2 / 206(4)-1 / 204-2 / Form PF / Reg BI-CRS / FINRA 3110-3310 / cyber-Reg S-P) so each domain reviewer works the slice they own.

**Part B — Domain-by-domain readiness.** One subsection per applicable rule lane; lanes the firm does not run drop out. Same internal shape: lane summary, public-criteria pin (citation by path to `references/source-anchors.md`), evidence inventory (system of record and named-role owner, not screenshots), open issues with trend, reviewer questions, confidence label. The lane structure is in `references/sector-overlays/capital-markets.md`. The Marketing Rule lane chains to `marketing-rule-evidence`; the best-execution lane (where in scope) chains to `best-execution-surveillance`; the fund-board side (where in scope) chains to `fund-board-reporting`.

**Part C — Mock-interview prep.** EXAMS reads for posture, not just paperwork; the mock interview is where firms underperform. For each interviewee role (CCO, CEO, CFO, head of trading, head of marketing, valuation designee chair, designated FINRA supervisor, BSA officer as applicable), the pack carries likely questions, prepared response anchors that pin to evidence (not scripted answers), and the rehearsal status. Conduct themes — IA Act §206 fiduciary duty, Reg BI care obligation, conflict disclosure, code-of-ethics escalation — sit across roles and load from `references/cross-cutting/conduct.md`.

**Part D — Gap and remediation list.** Per gap: gap ID, domain, severity (`critical` / `high` / `medium` / `low`), description, owner role, due date, evidence required, status. Severity calibrates to exam-exposure risk: `critical` for items the document-request submission would expose without remediation; `high` for items the mock interview would expose; `medium` for items routinely flagged in EXAMS Risk Alerts that the firm has not yet hardened; `low` for hygiene.

## Sector and cross-cutting overlays

This skill is capital-markets-only. The registration-class branching (IA / BD / dual registrant / private-fund adviser / fund adviser) lives in `references/sector-overlays/capital-markets.md`. There is no banking, insurance, or payments-fintech overlay file. Cross-cutting overlays load when the cycle scope implicates them.

- `cross-cutting/cyber.md` loads when the document-request scope includes Reg S-P, cybersecurity, or information-security topics, or when the firm is NY-licensed and NYDFS Part 500 is in scope. The SEC's separately-proposed adviser-and-fund cyber rule (2022) was withdrawn in 2025 and is not in force; Reg S-P is the operative anchor.
- `cross-cutting/conduct.md` loads by default for retail-customer-serving firms and on demand for institutional firms with material conflict-of-interest topics in scope. Anchors: IA Act §206 fiduciary duty (SEC Commission Interpretation, June 5, 2019); Reg BI; Form CRS; FINRA Rule 2111 suitability.
- `cross-cutting/privacy.md` does not load. Privacy-specific obligations under Reg S-P and GLBA load through the cyber overlay.
- `cross-cutting/climate.md` loads only when ESG-labeled product disclosures or Names Rule 35d-1 amendments are specifically in exam scope; otherwise carry as a reviewer question and skip the overlay.

## Non-negotiables

- Every material claim cites a source from `references/source-anchors.md` or a loaded cross-cutting overlay by path. Mark unsupported items `[evidence needed]`. Mark unconfirmed section references or current-state items `[verify section]` or `[verify current state]`.
- Source evidence, firm management assertion, public-source obligation, generated inference, and open legal or compliance question stay distinguishable. The pack shows the seams.
- Roles only, never named individuals. No named institutions in narrative beyond a public defendant in a finalised SEC or FINRA enforcement action with a published order, and only for structural pattern.
- The pack stops short of speaking for the firm to the regulator. The CCO and the named lead attest; external counsel signs the privilege-confirmation block where engaged.
- The SEC rule pipeline 2023-2026 has been volatile. Confirm current state at write time. As of late 2025-early 2026: the PFA Rule was vacated (June 5, 2024) and is not in force; the SEC withdrew the proposed adviser-and-fund cyber rule and the Predictive Data Analytics Rule from its regulatory agenda (June 12, 2025) — neither is pending; Reg S-P amendments are the operative customer-information safeguarding rule, compliance December 3, 2025 (larger) / June 3, 2026 (smaller); Names Rule compliance dates were extended to December 11, 2025 (large fund groups) / June 11, 2026 (smaller groups); the Form PF amendments are operative and separate from the vacated PFA Rule. The Corporate Transparency Act BO reporting rule docket has been active across 2024-2025; verify the operative state. Verification flags carry through `references/source-anchors.md`.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors (IA Act / ICA / Exchange Act / FINRA / SEC EXAMS Priorities and Risk Alerts; Reg S-P 2024; SEC cyber rule [verify state]; PFA Rule vacatur context; Form PF amendments; Names Rule; Rule 605 / 606).
- `references/sector-overlays/capital-markets.md` — registration-class branching (IA, BD, dual registrant, private-fund adviser, fund adviser), document-request lane structure, exam-type calibration.
- `references/cross-cutting/cyber.md` — Reg S-P 2024 amendments, SEC cyber rule for advisers / funds [verify state], NYDFS Part 500, EXAMS cyber Risk Alerts, FINRA cyber guidance.
- `references/cross-cutting/conduct.md` — IA Act §206 fiduciary duty, Reg BI four obligations, Form CRS, FINRA Rule 2111 suitability, conflict-register structure, mock-interview conduct themes.
- `templates/default-output.md` — Word-memo named sections plus the Excel matrix tab structure.

## Output

Default to drafting against `templates/default-output.md`. Render as Word, Excel, PowerPoint, or Markdown when the audience or workflow asks for it; the typical pair is a Word memo via the `docx` skill plus the gap-and-evidence matrix as an Excel workbook via the `xlsx` skill (both in the `document-skills` plugin). The CCO and the named lead attest; the pack is a draft until that step.

Downstream consumers: `exam-brief` reads the engagement context and the document-request matrix to set the engagement-side scaffolding (request-list mapping, document-handling, interview-prep). `marketing-rule-evidence` reads the Marketing Rule lane gaps to refresh the substantive evidence pack. `best-execution-surveillance` reads the trading-and-execution evidence asks. `fund-board-reporting` reads the Rule 38a-1 lane for the fund-board cycle. `risk-committee-pack` reads the gap-and-remediation list and the open-finding posture for the standing committee section.
