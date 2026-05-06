# section1071-readiness — Phase 1 spec sheet

Date: 2026-05-06
Plugin: consumer-compliance-fair-lending
Phase: 1 (per-skill scoping; no SKILL.md content)

## Activation-tuned description

Drafts a Section 1071 small-business lending data readiness assessment: covered financial institution determination, covered application / covered credit transaction scoping, data-point inventory against 12 CFR 1002.107, firewall and data isolation review, firewall-trained personnel design, applicant demographic data collection mechanics, recordkeeping, and reporting timeline preparation. Produces a second-line readiness memo and gap list.

Best for:
- Pre-compliance-date readiness check for a covered financial institution (Tier 1, 2, or 3 depending on the litigation-revised compliance schedule [verify current schedule]).
- Annual operating-state readiness refresh post-go-live.
- Vendor / loan-origination-system readiness assessment (where 1071 data capture is vendor-supplied).
- Re-scoping after a change in originated credit volume that changes Tier classification.

Not the right tool when:
- The question is HMDA / Reg C readiness (different rule, different population — refer the reviewer elsewhere).
- The question is fair-lending testing on the originated 1071 portfolio (use fair-lending-test-plan; 1071 data feeds into fair-lending testing once it exists).
- The question is the adverse action notice for a small-business application (use adverse-action-review; Reg B applies).
- The question is the firm's overall CMS (use risk-compliance-core / compliance-testing).

Anchored to: ECOA Section 1071 (15 U.S.C. §1691c-2 added by Dodd-Frank §1071); CFPB Section 1071 final rule (Small Business Lending under the Equal Credit Opportunity Act, March 30, 2023; codified at Regulation B Subpart B, 12 CFR 1002.101–1002.114); 12 CFR 1002.107 — compilation of reportable data; CFPB Filing Instructions Guide for small business lending data [verify current edition]; CFPB Section 1071 litigation status and revised compliance dates [verify current schedule — the compliance dates have been revised by court order and bureau response; phase 2 must pin the current dates accurately]; Interagency Fair Lending Examination Procedures (FFIEC, current edition) for fair-lending intersection.

## Source anchors

- ECOA 15 U.S.C. §1691c-2 — Section 1071 statutory authority.
- 12 CFR 1002.103 — definitions (covered financial institution, covered application, covered credit transaction, small business).
- 12 CFR 1002.104 — covered applications.
- 12 CFR 1002.105 — covered financial institutions.
- 12 CFR 1002.106 — covered credit transactions.
- 12 CFR 1002.107 — compiled data points (the canonical data-point list to align structured output fields against; phase 2 must enumerate completely).
- 12 CFR 1002.108 — firewall (limiting access by underwriters / others to demographic information).
- 12 CFR 1002.109 — reporting (annual filing; modified data published).
- 12 CFR 1002.110 — recordkeeping (three-year retention).
- 12 CFR 1002.111 — enforcement.
- 12 CFR 1002.112 — bona fide errors and safe harbors.
- 12 CFR 1002.114 — compliance dates [verify current — court-revised dates].
- CFPB Filing Instructions Guide (FIG) for small business lending data [verify current edition / version].
- CFPB Section 1071 small business lending rule page — https://www.consumerfinance.gov/rules-policy/final-rules/small-business-lending-under-the-equal-credit-opportunity-act-regulation-b/
- 12 CFR 1002.107 rule text — https://www.consumerfinance.gov/rules-policy/regulations/1002/107
- Section 1071 Sample Data Collection Form [verify CFPB-published version and date].
- Subsequent CFPB amendments and Section 1071 court-ordered timeline adjustments [verify].
- Interagency Fair Lending Examination Procedures (FFIEC, current edition) [verify edition] — fair-lending intersection.

## Data points to enumerate against 12 CFR 1002.107

The structured output schema and templates must enumerate all 1002.107 data points. The list includes (non-exhaustive — phase 2 verifies completeness against current rule text):

- Unique identifier
- Application date
- Application method
- Application recipient
- Credit type (product type, guarantee, loan term)
- Credit purpose
- Amount applied for
- Amount approved or originated
- Action taken
- Action taken date
- Denial reasons
- Pricing information (interest rate; total origination charges; broker fees; initial annual charges; additional cost for merchant cash advance and other sales-based financing; prepayment penalty)
- Census tract (principal address)
- Gross annual revenue
- NAICS code
- Number of workers
- Time in business
- Number of principal owners
- Minority-owned business status
- Women-owned business status
- LGBTQI+-owned business status
- Ethnicity, race, sex of principal owners
- (with firewall-driven access discipline per 1002.108)

[verify schema completeness against the current rule text in phase 2]

## Sector overlays needed

- `references/sector-overlays/banking.md` — depository institution origination flow; small business lending lines (SBA 7(a) / 504 included where covered); credit-card to small business; trade finance interaction; covered-financial-institution origination-volume thresholds for Tier classification.
- `references/sector-overlays/capital-markets.md` — generally out of scope for retail / small-business lending; included only to flag scope boundary so reviewers do not over-extend.
- `references/sector-overlays/payments-fintech.md` — merchant cash advance (MCA) and sales-based financing in scope; sponsor-bank vs. fintech-of-record reporting attribution; vendor LOS readiness; BNPL-for-business edge cases [verify].
- `references/sector-overlays/insurance.md` — out of scope; included only to flag scope boundary.

## Cross-cutting overlays

- `references/cross-cutting/privacy.md` — applicant demographic data is sensitive; firewall under 1002.108 is the operative privacy-adjacent control; GLBA Safeguards 16 CFR 314 layer; state privacy implications [verify state-specific scope] particularly around explicit consent for race / ethnicity / sex collection mechanics; modified data publication and re-identification risk considerations.

Conduct not applicable as a primary overlay. Cyber not applicable as a primary overlay (Safeguards Rule sits under privacy here). Climate not applicable.

## Output template named sections

1. Covered financial institution determination (origination volume by year, Tier classification, compliance date)
2. Covered application / covered credit transaction scoping (product list with in / out / edge classification and rationale)
3. Data-point readiness against 12 CFR 1002.107 (per-data-point readiness, system of record, capture mechanics, gap)
4. Applicant demographic data collection mechanics (collection point, script / form, refusal handling, principal-owner identification)
5. Firewall and data isolation review per 12 CFR 1002.108 (system, role-based access, exception process, training)
6. Recordkeeping (12 CFR 1002.110; retention, disposition)
7. Reporting and filing readiness (FIG conformance, file formats, validation, test submission plan)
8. Vendor / LOS readiness (ownership, attestations, change-control)
9. Fair-lending testing readiness on 1071 data (cross-reference fair-lending-test-plan)
10. Bona-fide-error and safe-harbor approach (12 CFR 1002.112)
11. Gap list with owner, due date, severity
12. Open legal / interpretive questions
13. Source trace and confidence label

## Structured output fields

[Schema must be aligned to 12 CFR 1002.107 data points; phase 2 verifies completeness]

| Field | Type | Purpose |
|---|---|---|
| `assessment_id` | string | Unique reference. |
| `cfi_determination` | object | Origination counts, methodology, Tier, compliance date. |
| `scope[]` | array of objects | Product, in/out/edge, rationale, source citation. |
| `data_points[]` | array of objects | One entry per 12 CFR 1002.107 data point. |
| `data_points[].data_point` | string | Named per 1002.107. |
| `data_points[].rule_ref` | string | E.g., `1002.107(a)(13)`. |
| `data_points[].system_of_record` | string | LOS, CRM, deposit system, manual. |
| `data_points[].capture_method` | enum | `applicant_provided`, `firm_inferred`, `vendor_supplied`, `manual_entry`, `not_yet_captured`. |
| `data_points[].readiness` | enum | `ready`, `partial`, `gap`, `unverifiable`. |
| `data_points[].gap_description` | string | If not ready. |
| `data_points[].owner` | string | Accountable person. |
| `data_points[].due_date` | date | When ready. |
| `demographic_collection_mechanics` | object | Script, refusal handling, principal-owner identification, data-flow. |
| `firewall` | object | Per 1002.108: system, RBAC, exceptions, training, audit log. |
| `recordkeeping` | object | Per 1002.110. |
| `reporting_readiness` | object | FIG conformance, validation engine, test-file plan. |
| `vendor_readiness[]` | array of objects | Vendor, role, attestations, change-control. |
| `fair_lending_handoff` | object | How 1071 data feeds fair-lending testing. |
| `bona_fide_error_approach` | string | Per 1002.112. |
| `gap_list[]` | array of objects | Gap, severity, owner, due date. |
| `open_questions[]` | array of strings | For counsel and interpretation. |
| `source_trace[]` | array of objects | Claim, source, evidence, confidence. |

## Example scenarios (public-source-derived, anonymous)

1. A community bank with mid-range origination volume to small businesses runs a readiness check 12 months ahead of its current compliance date [verify]. Findings: NAICS code captured today only at SBA-line origination, not at general commercial lending — gap. Census-tract field populated from the borrower's mailing address rather than the principal address — gap. Demographic-data collection script not yet built into the LOS — gap with vendor. Firewall design relies on role-based access in the LOS but the underwriting role currently has read access to a customer-360 view that includes self-reported demographics on the deposit side — material 1002.108 gap, escalation required. Recommended actions: vendor change-control ticket on LOS demographic capture; firewall remediation in customer-360 with named access exception process; bona-fide-error policy draft.

2. A fintech sales-based financing platform with sponsor bank checks readiness on merchant cash advance origination. Findings: Pricing data points for MCA include the additional-cost field per 1002.107 [verify field reference] but the system computes it post-funding from settlement data — capture method `firm_inferred` rather than `applicant_provided`, with downstream amendment reporting risk; principal-owner demographic collection is technically present in the application but applicant refusal is recorded as `null` rather than the rule's required refusal value — gap; sponsor bank is the covered financial institution per the agreement, with the fintech as data-collection agent; firewall design at the fintech needs to mirror the sponsor bank's 1002.108 expectations, which is not currently the case. Recommended actions: re-engineer pricing capture to reduce post-funding amendment volume; fix refusal coding; sponsor-bank firewall alignment workshop; vendor attestation on data flow.

## Common pitfalls

1. Compliance date treated as static. The Section 1071 compliance schedule has been moved by court order and bureau action; phase 2 must pin the currently effective date for each Tier and re-pin if it changes again. Mitigation: `cfi_determination.compliance_date` field carries the source-and-date citation, not just a value.
2. Scope built from the firm's product taxonomy without mapping to the rule's covered-credit-transaction definition (1002.106). Mitigation: per-product mapping with rule citation.
3. Demographic data collection treated as a UI question, not a firewall design question. Collecting demographic data is half the rule; isolating it from underwriting access is the other half. Mitigation: firewall section is mandatory and produces a 1002.108 attestation map.
4. Vendor LOS treated as if its readiness is the firm's readiness. The firm is the covered financial institution; the vendor is a data-collection agent. Mitigation: vendor_readiness array is mandatory with attestations and change-control identifiers.
5. Bona-fide-error and safe-harbor approach not documented before go-live. Mitigation: bona_fide_error_approach is mandatory in the readiness memo.
6. Modified data publication and re-identification risk not considered. The CFPB publishes a modified version of submitted data; firms with low-volume small-business lending in identifiable geographies need to think about re-identification before submission. Mitigation: privacy cross-cutting reference covers this and the readiness memo flags it.
7. Skill issues a sign-off or takes operational action. It does not. The skill produces a readiness memo and gap list for human decision.

## Guardrail (mandatory in SKILL.md)

This skill does not file Section 1071 data, sign off readiness, finalize covered-institution determinations, or take any operational action. It produces a readiness assessment and gap list for human decision by qualified compliance, fair-lending, data, vendor management, and legal reviewers.
