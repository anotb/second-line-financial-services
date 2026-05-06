# control-matrix — spec sheet

Plugin: `risk-compliance-core`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Builds a risk-control matrix mapping obligations to control objectives, control activities, owners, frequency, evidence, test method, last test result, and open issues. Output is a named-row matrix that a control owner, internal audit lead, or examiner can read line-by-line.

Best for:
- Standing up or refreshing the control matrix for a process or product (lending, vendor management, model lifecycle, risk reporting, cyber disclosure governance).
- Translating a freshly mapped obligation set into the control structure that will be tested by compliance-testing or audit.

Not the right tool when:
- The obligations have not been extracted yet (use `obligation-mapping` first; this skill consumes its output).
- The work is a single-control test workpaper for an audit sample (use `compliance-testing/skills/control-test-workpaper`).
- The work is drafting a finding (use `issue-writeup`).

Anchored to: SR 11-7 (interagency model risk management guidance, 2011) §IV control framework expectations [verify section]; OCC Bulletin 2026-13 (revised interagency model risk management guidance, 2026) §III.A model controls [verify section]; FFIEC IT Examination Handbook, Information Security booklet (2016) §II Information Security Program control framework [verify section]; BCBS 239 (January 2013) Principles 3 and 4 (accuracy, integrity, completeness) for control coverage of risk data; U.S. interagency third-party risk management guidance (June 2023) §III.D ongoing monitoring controls.

## Source anchors

Primary:
- SR 11-7 — Federal Reserve and OCC supervisory letter on model risk management, April 4, 2011. Sections to cite: §IV (model development, implementation, and use), §V (model validation), §VI (governance, policies, controls). Use for: control-objective wording on model controls, segregation between development and validation, ongoing monitoring controls. [verify section labels]
- OCC Bulletin 2026-13 — revised interagency model risk management guidance, 2026. Sections to cite: §III.A (control environment), §III.B (third-party model controls). Use for: refreshed control expectations, third-party model controls, AI-system extensions. [verify section labels]
- FFIEC IT Examination Handbook, Information Security booklet, September 2016. Sections to cite: II.A (governance), II.C.7 (logical security), III (risk identification and assessment). Use for: cyber-control inclusion in the matrix when the process being mapped touches information security. [verify section labels]
- BCBS 239 — Basel Committee, Principles for Effective Risk Data Aggregation and Risk Reporting, January 2013. Principles 3 (accuracy and integrity), 4 (completeness), 6 (adaptability). Use for: data-quality control objectives in risk-reporting matrices.
- U.S. interagency third-party risk management guidance (final, June 2023). Sections to cite: III.A (planning), III.C (due diligence and selection), III.D (ongoing monitoring), III.E (termination). Use for: vendor-process control matrices.

Secondary (overlay only):
- COSO Internal Control – Integrated Framework (2013) for control taxonomy framing where firms anchor their own framework on COSO. Cite by component (Control Environment, Risk Assessment, Control Activities, Information and Communication, Monitoring Activities). [verify section labels]

## Sector overlays needed

- `banking.md` — Covers OCC heightened standards (12 CFR Part 30 Appendix D) [verify] influence on risk-and-control governance, FFIEC IT booklet expectations on technology controls, and CRA / fair-lending control coverage triggers when the matrix scopes a lending process.
- `insurance.md` — Covers NAIC Model Audit Rule (Model #205) [verify section] internal-control reporting, ORSA control coverage expectations, and state DOI conduct-of-business control flavors when the matrix scopes a claims or sales process.
- `capital-markets.md` — Covers SEC Rule 17a-4 / FINRA 4511 [verify] recordkeeping controls and FINRA 3110 supervision controls when the matrix scopes a trading or research process.
- `payments-fintech.md` — Covers Reg E / Reg Z controls for consumer protection in payment products and OCC fintech bank-partnership control expectations [verify] when the matrix scopes a sponsor-bank or payments process.

## Cross-cutting overlays needed

- `cyber.md` — Required. Cyber controls show up in nearly every matrix. Anchors: NIST SP 800-53 control families [verify], NYDFS Part 500 §500.3 cybersecurity policy and §500.5 vulnerability management, FFIEC IT booklet, SEC Reg S-K Item 106 [verify section] for disclosure-process controls.
- `privacy.md` — Optional, only when the scoped process touches consumer financial information. Anchors: GLBA Safeguards Rule (16 CFR 314.4) [verify], CCPA / CPRA where applicable.
- `climate.md` — Not required at v1 for this skill. Climate controls are committee-pack territory.
- `conduct.md` — Optional, only when the scoped process touches customer-facing decisions. Anchors: CFPB UDAAP exam manual [verify section].

## Output template named sections

Top of artifact:
- Scope and source posture
- Process or product in scope, business unit, jurisdiction
- Source list (regulators, rules, internal policies)
- Confidence label (high / medium / low / unknown)

Body — the matrix itself, one row per control, with these named columns:
- Obligation source
- Control objective
- Control activity
- Control owner (role, not person)
- Frequency
- Test method
- Evidence pointer (system of record, report ID, file location)
- Last test result
- Design effectiveness
- Operating effectiveness
- Open issues
- Human review required (yes / no)

Tail of artifact:
- Coverage gaps (obligations with no mapped control)
- Control redundancies (controls mapped to no obligation, or duplicate coverage)
- Recommended owner actions
- Source trace
- Sign-off block (reviewer name, date, reviewer questions)

## Structured output fields

Schema: `schemas/control.schema.json` (existing) plus matrix-level wrapper.

Wrapper object:
- `matrix_id`: string. Stable ID for the matrix instance.
- `scope`: object. Process, product, business_unit, jurisdiction (all string).
- `source_posture`: enum. Values: `public-only`, `firm-policy-overlay`, `mixed`.
- `obligations_in_scope`: array of obligation_id strings (foreign key into `obligation.schema.json`).
- `controls`: array of `control.schema.json` objects.
- `coverage_gaps`: array of objects with `obligation_id` (string) and `gap_description` (string).
- `redundancies`: array of objects with `control_ids` (array of strings) and `redundancy_description` (string).
- `confidence_label`: enum. `high` / `medium` / `low` / `unknown`.
- `reviewer_questions`: array of strings.
- `human_review_required`: boolean. Always true for v1.

Per-control fields (already in `control.schema.json`):
- `control_id`, `risk_id`, `control_objective`, `control_activity`, `frequency`, `owner`, `evidence` (array), `test_method` (enum), `design_effectiveness`, `operating_effectiveness`.

Phase 2 should add to `control.schema.json`:
- `obligation_id` (string, foreign key) — the matrix is obligation-anchored, not free-floating risk.
- `last_test_date` (string, ISO date).
- `open_issue_ids` (array of strings, foreign key into `issue.schema.json`).

## Example scenarios

### Scenario 1: BCBS 239 risk-reporting matrix for a Credit Risk monthly board pack

Input: a Credit Risk team is preparing for a regulator-driven BCBS 239 readiness review. Scope is the monthly board credit-risk pack, owner is the head of credit risk reporting, jurisdiction is US for a foreign banking organization. Source posture is public-only (BCBS 239) plus the firm's risk-reporting policy.

Output emphasizes:
- One row per BCBS 239 principle (3, 4, 6, 7, 11) mapped to a named data-quality, completeness, and timeliness control on the credit pack.
- Evidence pointer column names the source-system report (e.g., `credit-loss-data-warehouse:LGD_v3`) and the reconciliation log path.
- Coverage gaps section flags Principle 6 (adaptability) is not currently controlled — pack regenerates manually under stress scenarios.
- Confidence label is medium; reviewer questions list whether the firm has a documented data-quality threshold framework.
- Human review required is yes; the artifact is a draft for the data-management committee.

### Scenario 2: U.S. interagency TPRM control matrix for an outsourced fraud-screening service

Input: the second-line operational-risk team is refreshing the control matrix for a critical third-party fraud-screening service used in card transactions. Scope is the vendor lifecycle. Source posture is interagency TPRM guidance plus the firm's third-party policy.

Output emphasizes:
- Five rows aligned to TPRM lifecycle stages (planning, due diligence, contract, ongoing monitoring, termination) with discrete control activities under each.
- Cyber overlay row added: vendor SOC 2 Type II control mapping, NYDFS Part 500 §500.11 third-party service-provider security policy.
- Open issues column flags an unresolved finding from the most recent SOC 2 (control gap on logical access reviews) and links to the issue write-up.
- Coverage gap section flags missing exit-plan testing.
- Confidence label is high on planning and due diligence (firm has documented evidence), medium on ongoing monitoring (no quarterly KRI review), low on termination (no exit-test record).

## Common pitfalls

1. Listing controls without an obligation source. The matrix is obligation-anchored. A control with no source obligation is either a hygiene control that should be moved out of scope, or evidence that the obligation extraction is incomplete.
2. Confusing control objective with control activity. The objective is the condition that must be true. The activity is who does what, how often, using what system. Phase 2 SKILL.md should explicitly require both fields and reject single-field rows.
3. Treating "policy says X" as evidence. A policy is a control statement, not evidence of operation. The evidence pointer column must name a system of record output, a sample report, or a sign-off log — not the policy document.
4. Over-broad control owners. "Risk team" is not an owner. The owner field is a named role with accountability (e.g., Head of Model Risk, Chief Privacy Officer, Head of Vendor Management).
5. Silent coverage gaps. If an obligation has no mapped control, the matrix must surface it in the coverage gaps section. A clean-looking matrix with no gaps usually means the gaps were buried, not absent.
