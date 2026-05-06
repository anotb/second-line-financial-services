# Rule-to-obligation extraction — register template

Extraction ID: `RTOE-YYYY-<regulator>-<short-instrument>-NN`
As-of date: `YYYY-MM-DD`
Reviewer role: [legal | compliance | regulatory-change lead | external counsel] — attestation pending until named reviewer signs off.

## 1. Source identification

| Field | Value |
|---|---|
| Regulator | |
| Regulator office | |
| Instrument type | final-rule / interim-final-rule / proposed-rule / adopting-release / supervisory-letter / bulletin / circular / fil / letter-to-credit-unions / industry-letter / eu-regulation / eu-directive / eu-rts-its / fca-handbook-chapter / pra-rulebook-chapter / naic-model-law / advisory / consent-order-as-obligation-source / interagency-statement |
| Citation | e.g., `88 FR 51896`; `12 CFR 1002.107`; `Regulation (EU) 2022/2554, OJ L 333/1`; `SYSC 6.1.1R`; `SR 11-7`; `OCC Bulletin 2013-29` |
| Section reference | precise pin where the extracted body sits |
| Publication date | YYYY-MM-DD |
| Effective date | YYYY-MM-DD |
| Compliance dates | tier-by-tier; each row in transition table |
| Transition period | as the rule frames it |
| Operative URL | Federal Register / eCFR / EUR-Lex / FCA handbook / regulator publication page |

## 2. Extraction summary

- Obligation count: `N`
- Distribution by section: `<section ref>: <count>` rows.
- Distribution by action type: `affirmative_act: M; recordkeeping: M; reporting: M; governance: M; ...` (optional).

## 3. Atomic obligation list

| ID | Source pin | Action verb | Party obligated | Requirement statement | Condition / trigger | Deadline | Exception | Frequency | Action type | Evidence expected | Cross-refs | Defined terms used | Confidence | Status | Open questions |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OBL-001 | | | | | | | | one_time / on_event / periodic / continuous | prohibition / affirmative_act / recordkeeping / notice_or_disclosure / reporting / governance / training / monitoring | board minute / attestation / log / periodic report / policy artifact / training roster / regulatory filing / customer notice | OBL-NNN | term-A; term-B | high / medium / low / unknown | draft / in-review / approved / not-applicable / open-question | |

(One row per atomic obligation. Compressing multiple obligations into one row is the most common defect; a paragraph that says "the institution shall (i) document, (ii) test annually, and (iii) report to the board" is three rows.)

## 4. Cross-references and dependencies

| From OBL | To OBL | Relationship | Notes |
|---|---|---|---|
| | | depends_on / produces_record_for / reports_outcome_of / governs / is_exception_to / phases_into / cross_refs | |

## 5. Defined terms used

| Term | Source section | Definition (verbatim or close paraphrase) | Obligations using term |
|---|---|---|---|
| | | | OBL-001; OBL-NNN |

## 6. Effective-date and transition table

| Stage | Date | Applicable obligations | Description |
|---|---|---|---|
| effective-date | YYYY-MM-DD | OBL-... | rule becomes part of CFR / OJ |
| tier-1 compliance | YYYY-MM-DD | OBL-... | |
| tier-2 compliance | YYYY-MM-DD | OBL-... | |
| sunset / re-evaluation | YYYY-MM-DD | OBL-... | |

## 7. Open extraction questions

| Reviewer | Section ref | Obligation IDs | Question | Blocker for | Target resolution |
|---|---|---|---|---|---|
| legal / compliance / function-head / external-counsel / regulatory-change-lead | | | | obligation-mapping / policy-diff / implementation-plan | YYYY-MM-DD |

## 8. Source trace and confidence

- Overall confidence label: `high / medium / low / mixed`.
- Material claims and named-anchor citations (each tied to `references/source-anchors.md` or a loaded overlay):
  - `<claim>` — `<source>`, `<section>`, `<date>`, `<url>`.
- Items needing follow-up: `[evidence needed]`.
- Sections that could not be confirmed at extraction time: `[verify section]`.

## 9. Reviewer attestation

- Reviewer role:
- Review status: pending / in-review / attested / returned-for-revision
- Review date:

## 10. Handoff targets

- `obligation-mapping` (always) — firm-side overlay.
- `policy-diff` — when a firm policy text is in scope.
- `implementation-plan` — when staged remediation is needed.
- `regulatory-impact-assessment` — when impact assessment was the upstream skill.
