# Spec: rule-to-obligation-extraction

Plugin: regulatory-change-management
Status: phase 1 spec sheet, pending phase 2 build
Date: 2026-05-06
Renamed from: rule-to-obligation-map (v0.2)

## Activation-tuned description

Decomposes a discrete piece of new regulatory rule text (final rule, supervisory letter, circular, FIL, bulletin, industry letter, or adopting release) into atomic obligations. Each obligation is structured: requirement statement, applicability, frequency, who must act, what evidence proves it, and the source pin. Output is the input to obligation-mapping in risk-compliance-core, which then maps obligations onto firm policies, controls, and evidence.

Best for:
- A new final rule or supervisory letter has been published and the firm needs an atomic obligation list before mapping to existing controls.
- A regulator has updated a manual chapter or appendix and the obligation inventory needs the deltas, not a full re-mapping.
- A consent order has been published and its remediation requirements need to be parsed as obligations the firm should also satisfy.

Not the right tool when:
- The source is a firm policy, vendor contract, or any document other than a regulator-issued rule or guidance instrument (use risk-compliance-core/obligation-mapping).
- Firm impact has not been scoped yet (use regulatory-impact-assessment first).
- The objective is to compare existing policy text to a rule (use policy-diff).

Boundary with risk-compliance-core/obligation-mapping:
- This skill: input is a discrete piece of new rule text from a named regulator. Output is the atomic obligation list. No firm context required; output is portable across firms.
- obligation-mapping: input can be any source document (firm policies, vendor contracts, exam letters, board minutes, regulator letters). Output maps obligations onto firm-specific control objectives, evidence, and owners. Requires firm context.
- The two skills chain: extract first (regulator output, firm-agnostic), then map (firm-specific overlay).

Anchored to: 12 CFR / 17 CFR / 31 CFR rule citations as published in the Federal Register; OCC Bulletins; FRB SR letters; FDIC FILs; CFPB Circulars and Bulletins; NCUA Letters to Credit Unions; NYDFS Industry Letters; SEC adopting releases; FinCEN advisories.

## Source anchors

- Federal Register publications for SEC, CFPB, OCC, FRB, FDIC, FinCEN, NCUA final rules and adopting releases.
- OCC Bulletins (e.g., 2013-29, 2023-XX revised TPRM).
- FRB SR Letters (e.g., SR 11-7, SR 13-19).
- FDIC FILs as published.
- CFPB Circulars (e.g., 2022-03 [verify]) and Bulletins.
- NCUA Letters to Credit Unions.
- NYDFS Industry Letters and 23 NYCRR Part 500.
- SEC adopting releases (e.g., Reg S-P amendments, cyber disclosure final rule, marketing rule for advisers Rule 206(4)-1).
- FinCEN advisories and rules (e.g., 31 CFR 1010.230 beneficial ownership).
- For obligation atomicity rubric: ISO/IEC 42001:2023 Annex A control structure as a model for atomic-obligation shape (paraphrased pattern, not authority).

## Sector overlays needed

- banking.md — banking-rule citation conventions (12 CFR Part X §Y); recurrent extraction patterns for OCC/FRB/FDIC supervisory letters.
- insurance.md — NAIC Model Law adoption tracking; how to decompose a model law versus a state-adopted version.
- capital-markets.md — SEC adopting release structure (rule text + commentary); Investment Advisers Act citation conventions.
- payments-fintech.md — CFPB 1033, EFTA/Reg E, and money-transmitter rule structures; how to decompose cross-jurisdiction obligations.

## Cross-cutting overlays needed

- cyber.md — extracting incident-reporting timing obligations (e.g., 4-business-day SEC cyber, 72-hour NYDFS, 36-hour bank notification rule).
- privacy.md — extracting notice, consent, and disposal obligations from privacy rule text.
- climate.md — only when extracting from a climate-related disclosure rule.
- conduct.md — extracting prohibition vs. affirmative-act obligations from UDAAP-adjacent rules.

## Output template named sections

1. Source identification (regulator, instrument type, full citation, section ref, publication date, effective date, transition period)
2. Obligation extraction summary (count, distribution by section)
3. Atomic obligation list (one row per obligation)
4. Cross-references and dependencies (obligations that reference other obligations)
5. Defined terms used (regulator's defined terms that change scope)
6. Effective-date and transition table
7. Open extraction questions (ambiguities flagged for legal review)
8. Source trace

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| extraction_id | string | Stable ID for this extraction run |
| source_citation | object {regulator, instrument_type, citation, section, publication_date, effective_date, transition} | Source pin |
| obligations | array<obligation> | The atomic obligation list |
| obligation.id | string | Stable obligation ID, scoped to source |
| obligation.requirement_statement | string | Plain-language requirement |
| obligation.source_pin | object {section, paragraph, sentence_or_subsection} | Anchor inside the source |
| obligation.applicability | object {institution_types, products, geographies, thresholds} | Who is in scope |
| obligation.actor | string | Who must act (board, senior management, business line, second line, third line, third party) |
| obligation.action_type | enum {prohibition, affirmative_act, recordkeeping, notice_or_disclosure, reporting, governance, training, monitoring} | Shape of the obligation |
| obligation.frequency | enum {one_time, on_event, periodic, continuous} | When it operates |
| obligation.evidence_expected | array<string> | Evidence patterns (board minute, attestation, log, report, policy) |
| obligation.cross_refs | array<string> | Obligations referenced by this one |
| obligation.defined_terms_used | array<string> | Regulator-defined terms invoked |
| obligation.confidence | enum {high, medium, low, unknown} | Extraction confidence |
| open_questions | array<object {question, paragraph_ref, blocker_for}> | Ambiguities for legal review |
| handoff_targets | array<string> | Next skills (obligation-mapping; policy-diff; implementation-plan) |

## Example scenarios (public-source-derived)

1. SEC cybersecurity disclosure rule (Item 1.05 of Form 8-K, Reg S-K Item 106). Decompose into: incident materiality determination obligation; 4-business-day disclosure timing obligation; cybersecurity risk management process disclosure obligation (annual); board oversight disclosure obligation; cybersecurity governance disclosure obligation. Each with section pin, actor, action type, evidence pattern. [verify exact section numbers]
2. CFPB Section 1071 small business lending data rule under Regulation B (12 CFR 1002.107). Decompose: covered financial institution determination; covered application data points; firewall obligation between underwriter and demographic data; recordkeeping obligation; reporting obligation; effective-date and tier-based compliance posture.

## Common pitfalls

1. Compressing multiple obligations into one. If a paragraph says "the institution shall (i) document, (ii) test annually, and (iii) report to the board," that is three obligations with potentially different actors and frequencies, not one.
2. Skipping defined terms. A rule's defined term ("covered institution," "material," "senior management") changes applicability. Capture the definition with its citation.
3. Mixing extraction with mapping. This skill does not name firm policies or controls. That is risk-compliance-core/obligation-mapping. Crossing the boundary makes the output non-portable.
4. Ignoring transition language. An obligation with a 24-month phased applicability is a different obligation in month 1 than in month 25. Capture both states or note the phasing.
5. Treating commentary or Federal Register preamble as binding text. Preamble is interpretive; the operative text lives in the codified section. Pin to the codified section, with a separate note for preamble context if useful.
