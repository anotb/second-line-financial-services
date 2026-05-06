# obligation-mapping — spec sheet

Plugin: `risk-compliance-core`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Converts source documents (rules, guidance, exam manuals, exam request lists, internal policies, supervisory letters) into a structured obligation register with applicability, control objectives, evidence required, owner, and open questions. Output is a register, not prose; one row per obligation, traced to source by section.

Best for:
- Standing up or refreshing the obligation register for a process, product, or regulatory domain.
- Converting an exam manual or exam request list into an internal obligation set the firm can respond to.

Not the right tool when:
- Input is a discrete piece of new rule text being absorbed for change-management purposes (use `regulatory-change-management/skills/rule-to-obligation-extraction`; that skill is tuned for net-new rule deltas, this one is tuned for any source).
- The mapping is from obligation to control (use `control-matrix`; this skill ends at the obligation, that skill begins from it).
- The work is a gap analysis between policy and obligations (use `policy-gap-review`).

Anchored to: U.S. interagency third-party risk management guidance (final, June 2023) §III.A planning [verify section]; SR 11-7 §VI governance, policies, controls [verify section]; CFPB Section 1071 final rule (12 CFR 1002.107) and the broader Regulation B obligation set; FFIEC BSA/AML Examination Manual (2024 update) — Customer Due Diligence and Beneficial Ownership sections [verify section]; BCBS 239 Principles 1–11 (January 2013) for risk-reporting obligation extraction.

## Source anchors

Primary:
- U.S. interagency third-party risk management guidance, June 2023. §III.A planning, §III.B due diligence, §III.D ongoing monitoring, §III.E termination. Use for: TPRM obligation extraction. [verify section labels]
- SR 11-7, April 4, 2011. §IV development, §V validation, §VI governance. Use for: model-risk obligation set. [verify]
- CFPB Section 1071 final rule, 12 CFR 1002.107. Use for: small-business lending data-collection obligations.
- FFIEC BSA/AML Examination Manual, current edition. CDD section, Beneficial Ownership section, SAR section. Use for: financial-crime obligation extraction. [verify section labels]
- BCBS 239, January 2013. Principles 1 through 11 with named principle text. Use for: risk-data-aggregation and risk-reporting obligation extraction.

Secondary (overlay only):
- OCC Bulletin 2026-13, 2026 — refreshed model risk guidance. Use as the current OCC anchor for model-risk obligations alongside SR 11-7.
- DORA (Regulation (EU) 2022/2554) Articles 5–14 (ICT risk management framework) and Articles 28–30 (ICT third-party risk) [verify], when input is EU-anchored.
- EU AI Act (Regulation (EU) 2024/1689), full obligation set for high-risk AI systems (Articles 6–29).
- NYDFS Part 500 §500.2 through §500.17, when input is NYDFS-anchored.

## Sector overlays needed

- `banking.md` — Covers Reg O insider lending, Reg W affiliate transactions [verify], OCC heightened standards [verify], FRB SR letters as obligation source.
- `insurance.md` — Covers state-by-state insurance code obligations (model laws as starting point), NAIC model laws, ORSA obligations.
- `capital-markets.md` — Covers SEC adviser rules (Investment Advisers Act of 1940 and rules thereunder), FINRA rule book, SEC EXAMS priorities as scoping input.
- `payments-fintech.md` — Covers Reg E, Reg Z, Reg DD obligations; OCC fintech bank-partnership expectations [verify]; CFPB Section 1033 (open banking) when applicable.

## Cross-cutting overlays needed

- `cyber.md` — Optional, when source is cyber-anchored (NYDFS Part 500, SEC cyber rules, FFIEC IT booklet).
- `privacy.md` — Optional, when source is privacy-anchored (GLBA, state privacy laws).
- `climate.md` — Optional, when source is SEC climate disclosure rule [verify status post-2025] or TCFD-aligned reporting.
- `conduct.md` — Optional, when source is CFPB UDAAP exam manual or fair-lending rules.

## Output template named sections

Top of artifact:
- Scope (process, product, business unit, jurisdiction, period)
- Source list (each source named with edition / date)
- Source posture (public-only, firm-policy overlay, mixed)
- Confidence label

Body — the obligation register, one row per obligation, with these named columns:
- Obligation ID
- Source citation (regulator, document, section, date, URL)
- Requirement summary (concise, one-sentence)
- Applicability (institution type, product, activity, geography, threshold)
- Effective date (and any phase-in)
- Impacted process or function
- Control objective (what must be true; one-sentence)
- Evidence required (what proves operation)
- Owner (named role)
- Status (draft / in-review / approved / not-applicable / open-question)
- Open questions (items requiring legal or compliance review)
- Linked controls (foreign key into control-matrix output, optional at this stage)

Tail of artifact:
- Open-question summary (items requiring legal review before status moves off `open-question`)
- Applicability scoping notes (where the obligation does or does not apply, with rationale)
- Source trace and confidence label
- Sign-off block

## Structured output fields

Schema: `schemas/obligation.schema.json` (existing). Phase 2 should keep existing fields and add:
- `effective_date_phase_in` (string, optional, free-text describing phase-in stages).
- `applicability_thresholds` (object): `asset_threshold` (number, optional), `transaction_volume_threshold` (number, optional), `notes` (string).
- `open_questions` (array of strings).
- `source_section` (string) — distinct from `source` URL field; explicitly captures section reference, not URL.
- `linked_control_ids` (array of strings).
- `confidence_label` (enum).

Wrapper object:
- `register_id`: string.
- `scope`: object. `process`, `product`, `business_unit`, `jurisdiction`, `period_start`, `period_end`.
- `sources`: array of objects with `source_name`, `edition`, `date`, `url`.
- `obligations`: array of `obligation.schema.json` objects.
- `open_question_summary`: array of strings.
- `applicability_notes`: string.
- `confidence_label`: enum.
- `human_review_required`: boolean. Always true.

## Example scenarios

### Scenario 1: CFPB Section 1071 obligation register for a community bank

Input: a community bank under the CFPB Section 1071 covered-financial-institution threshold is mapping its obligations from the rule. Source posture is public-only (12 CFR 1002.107 plus the CFPB final-rule preamble).

Output emphasizes:
- Obligations grouped by lifecycle stage: covered-application identification, data-point collection, firewall, recordkeeping, reporting, error correction.
- Each row cites 12 CFR 1002.107 with subsection (e.g., §1002.107(a)(1)) and the relevant preamble paragraph.
- Applicability column states the bank's tier (compliance date wave) and threshold rationale.
- Open questions flag the protected-demographic firewall design where the bank has loan officers acting as both intake and underwriting.
- Status: most rows in-review (need legal sign-off on threshold scoping); firewall row in open-question.
- Confidence label medium overall, low on firewall (institution-specific design dependency).

### Scenario 2: FFIEC BSA/AML CDD obligation register for a payments fintech bank-sponsor

Input: a fintech with a bank-sponsor partnership for payments products is refreshing its CDD obligation register against the FFIEC BSA/AML Manual (2024 update) and 31 CFR 1010.230.

Output emphasizes:
- Obligations grouped by FFIEC manual section: customer identification, customer risk profile, beneficial ownership, ongoing monitoring, suspicious activity reporting.
- Each row cites the manual section with subsection and the corresponding CFR citation (e.g., 31 CFR 1010.230(b)(2) for beneficial-owner identification).
- Applicability column distinguishes fintech-side obligations (operational) from bank-sponsor-side obligations (regulatory).
- Open questions flag where the fintech relies on the bank sponsor's CDD program: requires written allocation memorialised in the sponsor agreement.
- Status: bank-side obligations approved; fintech-side obligations in-review pending sponsor program documentation.
- Confidence label high on bank-side obligations, medium on fintech-side allocation.

## Common pitfalls

1. URL without section. The source field cannot be a bare URL. Phase 2 must enforce that every row has both a URL and a section / paragraph reference.
2. Requirement summary that paraphrases away substance. "Firm must do CDD" loses the obligation. The summary should say what specifically must be done and on whom.
3. Applicability too broad. "All operations" is not applicability. Applicability must name institution type, product, activity, geography, and threshold where the source defines them.
4. Owner is a department. "Compliance" is not an owner. The owner is a named role (e.g., BSA Officer, Head of Vendor Management, Chief Privacy Officer).
5. Status pre-decided. An obligation cannot be `approved` straight from extraction. Status must enter at `draft` or `open-question` until reviewed.
6. Mixing rule and policy. The register is rule-anchored; firm policy goes into the policy-control library or `policy-gap-review`. Phase 2 should reject rows where the source is the firm's own policy without an external anchor.
