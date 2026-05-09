# Banking sector overlay for validation-plan

When the engagement-scope record names sector `banking`, this overlay adds banking-specific scope items to the validation plan. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-sector elements.

Loaded by: `validation-plan/SKILL.md` when `engagement_scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, bank holding company, foreign banking organization with US operations).

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for banking validation plans

### 1. The joint interagency revised guidance is the current binding frame

For federally regulated banks, the binding frame is the joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17 2026; supersedes SR 11-7 and SR 21-8). The three-pillar structure (conceptual soundness, ongoing monitoring, outcomes analysis) carries forward from SR 11-7 §IV; the plan does not invent an alternative. The bulletin expressly excludes generative AI and agentic AI from its scope (footnote 3); for GenAI use cases the plan's GenAI-overlay validation scope anchors to NIST AI 600-1, ISO/IEC 42001, EU AI Act Article 9 and Article 15 where applicable, and the cyber overlay rather than the bulletin.

For non-bank entities under the same parent (e.g., a sister broker-dealer or asset manager subsidiary), the bulletin reaches by extension only when the bank inherits model risk through transactions, services, or balance-sheet exposure. Plan-writer should not over-claim reach to non-bank entities; the substantive validation expectations are similar but the regulator constellation differs.

### 2. OCC Heightened Standards (12 CFR Part 30 Appendix D) — independence demand on tier-1

For OCC-supervised large banks subject to Heightened Standards, the validator function for tier-1 models in scope of the risk-appetite statement must be independent of model development. Plan metadata names the validator function and confirms independence at plan acceptance. The Heightened Standards' independent-risk-management expectation maps directly to SR 11-7 §IV.5 effective challenge.

Plan-side implications:

- Plan metadata flags `heightened_standards_inscope = true` for OCC large banks.
- For tier-1 models, the validator function is named with an explicit independence statement.
- Effective challenge questions for tier-1 models include a question on whether the development assumptions have been re-tested in this cycle (challenge to incumbency).

### 3. ECOA / Reg B fair-lending integration for credit-decisioning models

Where the model influences a credit decision (origination, pricing, line management, collections triggers, fraud-driven adverse action), the validation plan integrates with the firm's fair-lending test plan. The plan and the fair-lending test plan reference each other but stay distinct artifacts (the validator owns the model-risk lens; the consumer-compliance function owns the fair-lending lens).

Plan-side implications:

- Fairness scope includes ECOA / Reg B disparity testing across protected classes per the firm's fair-lending test plan; the plan cites the fair-lending test plan as a dependency.
- Adverse-action notice generation method (typically SHAP-based or reason-code-mapped) is a controls-section validation item, not a fairness-section item; the validator reviews the method and its sampling QC against CFPB Circular 2022-03 (specific-and-accurate reasons) and CFPB Circular 2023-03 (actual principal reasons).
- Effective challenge questions probe the proxy-variable post-deployment process (CFPB and OCC fair-lending exam practice probe this seam).

### 4. CCAR / DFAST overlap for stress-eligible banks

For banks subject to stress testing (DFAST and Federal Reserve CCAR for the largest BHCs), models used in stress projections, allowance methodology (CECL under ASC 326), and capital planning are in scope of additional validation expectations beyond SR 11-7. The plan:

- Flags `stress_testing_inscope = true` and identifies the relevant submission cycle.
- Includes stress-testing-pedigree review in conceptual soundness scope (was the model developed for, validated for, and currently approved for use in the relevant stress submission).
- Lists the annual stress-testing cycle as a re-validation trigger in monitoring scope.
- Cross-links to the firm's CCAR / DFAST owner and SR 15-18 or successor guidance [verify SR letter].

### 5. AML, BSA, and fraud-model framing

For models supporting BSA/AML transaction monitoring, sanctions screening, customer risk rating, and fraud detection, the FFIEC BSA/AML Examination Manual sets the supervisory frame. The plan:

- Names the BSA officer or designee as a sign-off reviewer when the model touches AML use cases.
- Includes above-the-line / below-the-line testing in outcomes-analysis scope (productivity testing for transaction monitoring).
- Treats threshold tuning as a controls-section validation item; threshold changes that materially shift alert volumes are change-management triggers and re-validation triggers.
- Avoids representing fraud-model performance metrics as AML-effectiveness evidence; the two are doctrinally distinct.

### 6. CRA-relevant models

For models that influence community-development assessment, low-and-moderate-income outreach, or branch-network analytics where they touch CRA performance, the plan adds a CRA-context note. Firm policy may require the head of community reinvestment as a sign-off reviewer.

### 7. Banking-specific validation tests and monitoring

In addition to the capability defaults, banking validation plans typically include:

- Population stability index (PSI) monitoring on input features in monitoring scope, with breach thresholds set against firm policy and against industry-typical breaches (PSI > 0.25 typically triggers re-fit consideration).
- Score drift monitoring (KS or PSI on score distribution) against a reference distribution.
- Decisioning-rate drift monitoring (approval rate, override rate, decline rate) by segment.
- Where applicable, complaint-rate drift from the CFPB complaint database plus internal complaint feed.

Each banking monitoring entry retains the validator's `revalidation_trigger` flag in addition to operational alerting.

## Banking-specific output template additions

The following fields are added to the plan (mapped to schema where present):

- `plan_metadata.heightened_standards_inscope` — boolean, true for OCC large banks subject to 12 CFR Part 30 Appendix D.
- `plan_metadata.bank_charter_type` — national bank / state member / state nonmember / savings association / BHC / FBO.
- `plan_metadata.primary_federal_regulator` — OCC / FRB / FDIC / NCUA.
- `plan_metadata.stress_testing_inscope` — boolean, with cross-reference to CCAR or DFAST submission.
- `data_review.scope_items[]` — CRA-relevance flag for CRA-touching data sources.
- `outcomes_analysis[]` — adverse-action-notice generation method validation when the model is credit-decisioning; above-the-line / below-the-line testing for AML transaction monitoring.
- `effective_challenge_questions[]` — banking-specific (adverse-action method, fair-lending integration, CCAR/DFAST pedigree, BSA officer sign-off where AML model).
- `monitoring[]` — PSI, score drift, decisioning-rate drift, complaint-rate drift entries with `revalidation_trigger` flagged.

## Common pitfalls in banking validation plans

- Treating CFPB authority as out of scope because the entity is OCC- or FRB-supervised; CFPB consumer-protection authority reaches large banks for ECOA, RESPA, EFTA, and UDAAP purposes.
- Reporting model performance only on a development holdout in outcomes analysis; SR 11-7 §IV expects performance under deployment conditions.
- Omitting the proxy-variable post-deployment process; both CFPB and OCC fair-lending exam practice probe this seam.
- Citing "vendor system card" as standalone evidence for a foundation-model dependency; for banks, vendor evidence supplements but does not substitute for the firm's own validation work.
- Omitting the stress-testing-pedigree review when the model is in fact used in stress; auditors and examiners catch this in the cross-walk.
- Setting validation depth as a single label across all three pillars; SR 11-7 §IV expects depth set per pillar, with justification.
