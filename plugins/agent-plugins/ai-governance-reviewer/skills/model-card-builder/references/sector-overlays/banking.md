# Banking sector overlay for model-card-builder

When the engagement-scope record names sector `banking`, this overlay adds banking-specific fields and review demands to the card. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-sector elements.

Loaded by: `model-card-builder/SKILL.md` when `engagement_scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, bank holding company, foreign banking organization with US operations).

## Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

## What changes for banking model cards

### 1. SR 11-7 is binding for federally regulated banks

SR 11-7 §V sets the documentation expectation for banks; the model card is the firm-side artifact that satisfies (in part) that expectation. For banks, the card is not optional governance polish; it is a prudential expectation under the Fed/OCC/FDIC interagency model risk guidance, refreshed in 2026 (OCC Bulletin 2026-13 and parallel FRB/FDIC issuances).

For non-bank registrants under the same parent (e.g., a sister broker-dealer or asset manager subsidiary), SR 11-7 reaches by extension only when the bank inherits model risk through transactions, services, or balance-sheet exposure. Card-writer should not over-claim SR 11-7 reach to non-bank entities.

### 2. OCC Heightened Standards (12 CFR Part 30 Appendix D)

For OCC-supervised large banks (currently set by asset-size threshold; see source-anchors), the Heightened Standards add a board-level risk-governance frame: independent risk management, risk-appetite statement, and compliance-program elements that reach into model risk. The model card supports the inventory and governance evidence that those board obligations rely on.

Card-side implications:

- Tier-1 models in scope of a category-I/II/III bank typically appear in the risk-appetite statement; the card section "Tier" should reference the firm's appetite statement classification.
- The Heightened Standards' independence requirement maps to the validator/second-line-reviewer fields in card metadata; for tier-1 cards, the second-line reviewer must be independent of model development.

### 3. ECOA / Reg B adverse action surface for credit-decisioning models

Where the model influences a credit decision (origination, pricing, line management, collections triggers, fraud-driven adverse action), Regulation B requires a specific, accurate adverse action notice. The card's fairness and explainability section, and the controls section, must address adverse action notice generation and quality.

Specifically reference:

- The CFPB Circular 2022-03 expectation that adverse action reasons must be specific and accurate even when the model is complex (the so-called black-box defence is rejected).
- The CFPB Circular 2023-03 expectation that creditors cannot rely on illegitimate reasons such as the algorithm not surfacing a permitted reason; reasons given must be the actual principal reasons.
- The firm's adverse action notice generation method (typically SHAP-based or reason-code-mapped) and any sampling/quality control for notice accuracy.

Sign-off questions (banking, credit-decisioning):
- What is the method of adverse action reason generation, and how is its accuracy sampled?
- How does the firm handle a proxy variable identified post-deployment as fairness-sensitive?
- What is the integration with the firm's fair-lending test plan, and at what cadence?

### 4. CCAR / DFAST overlap for stress-eligible banks

For banks subject to stress testing (currently DFAST and the Federal Reserve's CCAR for the largest bank holding companies), models used in stress projections, allowance methodology (CECL under ASC 326), and capital planning are in scope. The card for any such model needs:

- Stress-testing pedigree section in the source trace (was the model developed for, validated for, and currently approved for use in the relevant stress submission?).
- Cross-link to the firm's CECL methodology owner, where applicable.
- Re-validation trigger for the annual stress-testing cycle.

Card-writer flag: if the model touches stress, do not rely on this skill alone; the firm's CCAR/DFAST owner has additional model documentation expectations under SR 15-18 or successor guidance [verify SR letter].

### 5. AML, BSA, and fraud-model framing

For models supporting BSA/AML transaction monitoring, sanctions screening, customer risk rating, and fraud detection, the FFIEC BSA/AML Examination Manual sets the supervisory frame; the card should:

- Name the BSA officer or designee as a signoff reviewer when the card touches AML use cases.
- Record the model's role in the suspicious activity report (SAR) workflow without claiming the model files SARs (the firm files SARs; the model triages or scores).
- Treat threshold tuning as a controls-section item; threshold changes that materially shift alert volumes are change-management triggers.
- Avoid representing fraud-model performance metrics as AML-effectiveness evidence; the two are doctrinally distinct.

### 6. CRA-relevant models

For models that influence community-development assessment, low-and-moderate-income outreach, or branch-network analytics where they touch CRA performance, the card adds a CRA-context note. Firm policy may require the head of community reinvestment as a signoff reviewer.

### 7. Banking-specific monitoring expectations

In addition to the capability defaults, banking model cards typically include:

- Population stability index (PSI) monitoring on input features, with breach thresholds set against firm policy and against industry-typical breaches (PSI > 0.25 triggers re-fit consideration).
- Score drift monitoring (KS or PSI on score distribution) against a reference distribution.
- Decisioning-rate drift monitoring (approval rate, override rate, decline rate) by segment.
- Where applicable, complaint-rate drift from the CFPB complaint database plus internal complaint feed.

## Banking-specific output template additions

The following fields are added to the card (mapped to schema where present):

- `card_metadata.heightened_standards_inscope` — boolean, true for OCC large banks subject to 12 CFR Part 30 Appendix D.
- `card_metadata.bank_charter_type` — national bank / state member / state nonmember / savings association / BHC / FBO.
- `card_metadata.primary_federal_regulator` — OCC / FRB / FDIC / NCUA.
- `card_metadata.stress_testing_inscope` — boolean, with cross-reference to CCAR or DFAST submission.
- `data[].cra_relevance` — boolean flag for CRA-touching data sources.
- `controls[]` — adverse action notice generation control listed explicitly when the model is credit-decisioning.
- `signoff_questions[]` — banking-specific questions (adverse action method, fair-lending integration, CCAR/DFAST pedigree).

## Common pitfalls in banking model cards

- Treating CFPB authority as out of scope because the entity is OCC- or FRB-supervised; CFPB consumer-protection authority reaches large banks for ECOA, RESPA, EFTA, and UDAAP purposes.
- Reporting model performance only on a development holdout; SR 11-7 §V expectations include performance under deployment conditions.
- Omitting the proxy-variable post-deployment process; both CFPB and OCC fair-lending exam practice probe this seam.
- Citing "vendor system card" as standalone evidence for a foundation-model dependency; for banks, vendor evidence supplements but does not substitute for the firm's own validation and documentation.
- Omitting the stress-testing pedigree section when the model is in fact used in stress; auditors and examiners catch this in the cross-walk.
