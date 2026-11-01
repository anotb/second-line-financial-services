# Banking sector overlay for model-card-builder

When the scope record names sector `banking`, this overlay adds banking-specific fields and review demands to the card. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-sector elements.

Loaded by: `model-card-builder/SKILL.md` when `scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, bank holding company, foreign banking organization with US operations).

## Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

## What changes for banking model cards

### 1. Joint interagency model-risk guidance for federally supervised banks

The 2026 joint interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026) is the current model-risk supervisory expectation for OCC-, FRB-, and FDIC-supervised banks. It supersedes SR 11-7 (2011) and SR 21-8 (the 2021 BSA/AML model-risk interagency statement). The model card is the firm-side documentation artifact aligned to the principles in the joint guidance.

Practical reach. The joint guidance is most relevant to banking organizations with over $30 billion in total assets, and is non-binding (does not set enforceable standards). For mid-size and community banks below that threshold, treat the principles as leading-practice rather than as a prudential mandate; firm policy still drives card scope and depth. Generative AI and agentic AI are explicitly out of scope (footnote 3); for those use cases, anchor the card to the AI-specific frameworks (NIST AI RMF, NIST AI 600-1, ISO/IEC 42001) and the cross-cutting overlays. The joint guidance does not reference NIST AI RMF or NIST AI 600-1; do not cite the joint guidance as the controlling anchor for GenAI/agentic documentation.

For non-bank affiliates under the same parent (a sister broker-dealer or asset manager), the joint guidance reaches by extension only when the bank inherits model risk through transactions, services, or balance-sheet exposure. Card-writer should not over-claim reach to non-bank entities.

### 2. OCC Heightened Standards (12 CFR Part 30 Appendix D)

For OCC-supervised large banks (currently set by asset-size threshold; see source-anchors), the Heightened Standards add a board-level risk-governance frame: independent risk management, risk-appetite statement, and compliance-program elements that reach into model risk. The model card supports the inventory and governance evidence that those board obligations rely on.

Card-side implications:

- Tier-1 models in scope of a category-I/II/III bank typically appear in the risk-appetite statement; the card section "Tier" should reference the firm's appetite statement classification.
- The Heightened Standards' independence requirement maps to the validator/second-line-reviewer fields in card metadata; for tier-1 cards, the second-line reviewer must be independent of model development.

### 3. ECOA / Reg B adverse action surface for credit-decisioning models

Where the model influences a credit decision (origination, pricing, line management, collections triggers, fraud-driven adverse action), Regulation B requires a specific, accurate adverse action notice. The card's fairness and explainability section, and the controls section, must address adverse action notice generation and quality.

Specifically reference:

- The Reg B §1002.9 specific-reasons requirement and Comment 9(b)(2)-3 of the Official Staff Commentary, which require the cited reasons to relate to and accurately describe the factors actually considered or scored. CFPB Circulars 2022-03 (specific-and-accurate reasons even when the model is complex) and 2023-03 (reasons given must be the actual principal reasons, not sample-form artefacts) **were withdrawn May 12, 2025; historical only**. The regulatory text continues to apply on its own terms.
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
- Reporting model performance only on a development holdout; supervisory expectations look for performance under deployment conditions, not just lab metrics.
- Omitting the proxy-variable post-deployment process; both CFPB and OCC fair-lending exam practice probe this seam.
- Citing "vendor system card" as standalone evidence for a foundation-model dependency; for banks, vendor evidence supplements but does not substitute for the firm's own validation and documentation.
- Omitting the stress-testing pedigree section when the model is in fact used in stress; auditors and examiners catch this in the cross-walk.
