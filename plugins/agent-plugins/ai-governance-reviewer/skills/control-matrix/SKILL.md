---
name: control-matrix
description: |
  Builds the named-row risk-control matrix that maps obligations to control objectives, control activities, owners, frequency, evidence pointers, test methods, last-test results, and open issues. Foundational primitive: compliance-testing samples against it, vendor-diligence and exit-plan reference it, exam-brief reads it, model-card-builder pulls its controls section from it. Risk function and compliance function both consume the same matrix.

  Best for:
  - Standing up the matrix for a process, product, or function (lending, vendor lifecycle, model lifecycle, risk-data and risk reporting, cyber-disclosure governance, consumer-compliance management).
  - Refreshing an existing matrix after a regulatory change, an MRA, an audit finding, an incident, or a process redesign.
  - Translating a freshly mapped obligation set into the row structure that downstream testing and review will run against.

  Not the right tool when:
  - The obligations have not been extracted yet. Run `obligation-mapping` first; the matrix consumes its output.
  - The work is a single-control workpaper for an audit sample (use compliance-testing's control-test-workpaper).
  - The work is drafting a finding (use `issue-writeup`).
  - The work is portfolio-level coverage commentary across many matrices (the risk-committee pack, not this).

  Anchored to: COSO Internal Control Integrated Framework (2013), BCBS 239, SR 11-7 / OCC Bulletin 2026-13, FFIEC IT Examination Handbook, Interagency Guidance on Third-Party Relationships (June 2023), 12 CFR Part 30 Appendix D (OCC Heightened Standards), NYDFS 23 NYCRR Part 500, and CFPB Compliance Management System guidance. Citations and excerpts live in `references/source-anchors.md`.
argument-hint: "[process or product in scope, plus pointer to obligation set or extract]"
---

# Control matrix

A risk-control matrix is the obligation-anchored row structure that lets a control owner, an internal audit lead, a second-line tester, or an examiner read the firm's coverage of a process line by line. One row, one control. The row carries enough columns that the reader can see what the obligation says, what the control is doing about it, who runs it, how often, what evidence proves it ran, what the last test said, and which open issues it carries.

The matrix is a primitive. Compliance-testing samples against the row's evidence pointer and test method. Vendor-diligence reads the relevant rows when it asks the third-party question. Exit-plan reads the rows that govern a critical-vendor relationship. Exam-brief leans on the matrix to answer "what controls cover this rule." Model-card-builder pulls its controls section from the model-lifecycle rows of the same matrix. Both the CRO function (risk-data, model risk, op risk, third-party risk) and the compliance function (consumer compliance, BSA, fair lending) consume it; the row spine is identical, the source labels and overlays differ.

The skill produces a matrix as a markdown artifact in `templates/default-output.md` shape and a structured record conforming to `schemas/control-matrix.schema.json`. The artifact is a draft until a named reviewer attests.

## Ask first

Before drafting, settle a few things. Most of the answers are on the table by the time someone reaches for the matrix.

- What process, product, or function is in scope. The matrix is scoped tight: commercial real estate origination, vendor lifecycle for a critical fraud-screening service, monthly board credit-risk pack, model lifecycle for tier-1 retail credit models. "The risk program" is too wide.
- What obligation set is the matrix anchored on. Pointer into `obligation-mapping`'s output, or the obligation source list named directly. Without an anchored obligation set, the matrix is policy commentary, not a control matrix.
- Who reads it, and what decision it supports. A 1.5-line refresh for the BU controls tester reads differently from a 2-line matrix headed for an MRMO challenge session, an audit support file, an examiner-readiness pack, or a board-committee summary. Persona drives review-gate machinery; audience drives compression.
- What source posture the engagement runs at. Public-only sets the ceiling at obligation, control objective, and control-activity description. Firm-policy-overlay or mixed lets named owners, named systems of record, and last-test results land in the body.

When `engagement-scope` is supplied, the skill consumes it for institution, persona, source posture, sector overlay, and cross-cutting overlay. Otherwise it asks the four questions and defaults to public posture if the practitioner declines. The matrix notes scope was not formalised; it does not silently assume.

## How the matrix gets built

The matrix has the same spine across processes. A senior practitioner builds it in roughly the order below, but the conversation surfaces rows in whatever order the obligations and controls show up; the structured record sorts itself.

The frame opens with scope and source posture: process or product, business unit (named, not "the business"), jurisdiction, lines of defense the matrix serves, source posture, and the source list itself (regulator, rule, interagency guidance, supervisory letter, examination manual, internal policy, industry standard). Source list comes from the obligation set rather than being reinvented here.

Rows are obligation-anchored. Each row starts with the obligation source (foreign key into `obligation-mapping`'s output plus the named source label) and works left to right across the named columns:

- **Control objective.** The condition that must be true. "Vendor SOC 2 Type II is reviewed before each contract renewal and gaps are remediated or accepted by the vendor risk committee." Not "vendor oversight is effective."
- **Control activity.** Who does what, how often, using what system. "Vendor risk analyst reviews the SOC 2 Type II report in the GRC platform within 30 days of receipt; documents complementary user-entity controls, opinion qualifications, and gaps; routes gaps to the vendor risk committee for accept-or-remediate decisions logged in the same record." Objective and activity are distinct, and both are required. A row with one and not the other is not yet a control.
- **Control type.** Preventive, detective, response, or compensating. Compensating controls carry the original gap reference.
- **Control owner.** A named role with accountability: Head of Vendor Management, Chief Privacy Officer, Head of Model Risk, BU controls tester, BSA Officer, head of credit risk reporting. "Risk team" is not an owner. "Operations" is not an owner. Where the firm's role taxonomy is firm-specific, it lands in `references/firm-overlay.md`.
- **Frequency.** Event-based, daily, monthly, quarterly, annual, ad-hoc. Event-based controls name the trigger.
- **Evidence pointer.** A pointer to a system-of-record output, a sample report, a sign-off log, or a workflow record. The system name and the report or record identifier are what the tester pulls. A policy document is a control statement, not evidence of operation. RFP narrative, vendor marketing, and management memos are not evidence either.
- **Test method.** Inquiry, inspection, observation, reperformance, data-analysis, walkthrough, or a hybrid. Inquiry alone is rarely sufficient on a critical control; pair with at least one verification method.
- **Last test date and last test result.** Pass, fail, partial, or not-yet-tested. "Not-yet-tested" is a legitimate value on a new control; it is also a flag for the testing program.
- **Design effectiveness and operating effectiveness.** Effective, partially-effective, ineffective, not-tested. Both fields, separately. A well-designed control that nobody runs is partially-effective at best; a poorly-designed control that someone runs heroically is also partially-effective.
- **Open issues.** Foreign keys into the issue log. A row with three open issues against it is louder than the effectiveness ratings alone suggest; the tail of the matrix surfaces those.

The tail of the matrix earns its keep by what it surfaces, not by what it hides. Coverage gaps are obligations in scope with no mapped control or with a partial mapping (no owner, no evidence pathway, never tested). A clean-looking matrix with no gaps usually means the gaps were buried; the gap section is part of the deliverable. Redundancies are controls mapped to no obligation (hygiene controls misplaced into the matrix, or evidence the obligation set is incomplete) and duplicate coverage of the same obligation by multiple controls without a designed-for defense-in-depth rationale. Recommended owner actions name the role and the action and a milestone where one is in view; the actions feed back into the issue log when they merit one. Reviewer questions are tied to specific rows, gaps, or redundancies, not generic prompts.

The source trace block and sign-off block close the artifact. Material claims cite `references/source-anchors.md` or a loaded overlay by path. `[evidence needed]` flags route to the engagement issue log rather than living silent in the matrix body.

### Sector and cross-cutting overlays

The same row spine carries different source labels and different rigor expectations across sectors and across cross-cutting topics. Load only the overlays the engagement scope flags:

- `references/sector-overlays/banking.md` carries OCC Heightened Standards (12 CFR Part 30 Appendix D) and FFIEC IT Booklet flavour for large-bank governance and tech-control matrices, plus CRA and fair-lending hooks where the matrix scopes a lending process.
- `references/sector-overlays/insurance.md` carries NAIC Model Audit Rule and ORSA control coverage, plus state DOI conduct-of-business control flavour for claims and sales matrices.
- `references/sector-overlays/capital-markets.md` carries SEC 17a-3 / 17a-4 and FINRA 4511 recordkeeping, FINRA 3110 supervision, and the Rule 15c3-5 overlap for trading-process matrices.
- `references/sector-overlays/payments-fintech.md` carries Reg E and Reg Z control hooks for consumer-payment products and the OCC fintech bank-partnership control posture for sponsor-bank arrangements.
- `references/cross-cutting/cyber.md` is the most-loaded overlay. NYDFS Part 500, FFIEC IT Booklet, and SEC Reg S-K Item 106 disclosure-process controls land here. The cyber overlay fires whenever the scoped process touches information-security controls, which is most matrices in practice.

Privacy, climate, and conduct overlays follow the same pattern; this skill ships cyber as the only cross-cutting file at v1 because cyber is the most frequent cross-cutting trigger. Privacy hooks (GLBA Safeguards Rule §314.4, state-privacy equivalents) load from the broader plugin reference set when the scoped process touches NPI; climate sits with the committee-pack skills rather than here; conduct loads when the matrix scopes customer-facing decisions.

Where firm policy or taxonomy applies, it lives in `references/firm-overlay.md` (consumed when present) and never in the matrix directly. The matrix carries the obligation source from `references/source-anchors.md` and the firm's labelling from the overlay, distinct columns.

## What's load-bearing and what flexes

A handful of things do not flex:

- Every row carries an obligation source. A control without a source obligation is either a hygiene control mis-located into the matrix or evidence that the obligation extraction is incomplete; either way, it does not stay as an unsourced row.
- Control objective and control activity are distinct and both required. The objective is the condition that must be true; the activity is who does what, how often, using what system. Single-field rows are not yet controls.
- Evidence is a pointer to a system-of-record output, a sample report, a sign-off log, or a workflow record. The policy document is the control statement, not evidence. Vendor marketing and management assertion are not evidence either.
- Coverage gaps are surfaced. Obligations in scope with no mapped control land in the gaps section of the artifact; they do not get buried in a footnote or papered over with a generic policy reference.
- Owners are named roles with accountability, not collective nouns. Where the role taxonomy is firm-specific, it comes from `references/firm-overlay.md`.
- Material claims cite a source. `[evidence needed]` flags items needing follow-up and routes to the engagement issue log.
- The matrix is a draft until a named reviewer attests. The skill stops at draft.

Everything else adapts to context. Audience drives shape: a 1.5-line refresh reads operational, a 2-line matrix for committee challenge reads with reviewer questions clustered, an audit support file reads with the testing column to the front, a board distillation pulls coverage gaps and recommended actions to the front. Source posture drives what the body can carry; public-only matrices sit at obligation-and-objective level, mixed and firm-policy-overlay let owners, system-of-record names, and test results land. Sector and cross-cutting overlays are loaded from the engagement scope. Frequency, test method, and effectiveness ratings track the firm's testing taxonomy where one exists.

## Output

The matrix in `templates/default-output.md` shape and the structured record per `schemas/control-matrix.schema.json`. Downstream consumers: `compliance-testing` reads `controls[*].evidence` and `controls[*].test_method` to scope sample work; `vendor-diligence` reads the rows that touch the in-scope third-party process and uses `coverage_gaps` to flag pre-onboarding conditions; `exit-plan` reads the critical-vendor rows and the `open_issue_ids`; `exam-brief` reads `controls` and `coverage_gaps` against the rule the examiner is asking about; `model-card-builder` pulls the model-lifecycle rows for the card's controls section; `policy-gap-review` reads the source list and `coverage_gaps` to triangulate policy edits. The schema is the cross-skill contract; additive changes only, never silent renames. Breaking changes ship as a versioned migration with downstream skills told in advance.

## Pointers

- `references/source-anchors.md` — citations and excerpts for the named anchors.
- `references/sector-overlays/{banking,insurance,capital-markets,payments-fintech}.md` — sector overlays loaded from engagement scope.
- `references/cross-cutting/cyber.md` — cyber overlay; loaded whenever the scoped process touches information-security controls.
- `references/firm-overlay.md` — firm-installed taxonomy, named role labels, system-of-record names, internal policy pointers, review gates beyond the regulatory baseline; consumed when present.
- `templates/default-output.md` — matrix template.
- `schemas/control-matrix.schema.json` — structured-output contract.
- `examples/` — credit-risk reporting matrix anchored on BCBS 239; AI-governance controls matrix anchored on SR 11-7 and the AI overlay.
