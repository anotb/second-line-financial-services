# Source anchors — life-health-pricing-governance

Named, dated regulatory sources this skill anchors to. SKILL.md cites this file by path and does not restate excerpts. Sector flavour for insurance sits in `sector-overlays/insurance.md`; cross-cutting flavour sits in `cross-cutting/<topic>.md`.

NAIC Model Laws and Regulations are model text; what binds the carrier is the state's adoption (which may amend, defer, or replace the model). Cite the NAIC model and the state-specific adoption status separately. Use the NAIC AI Working Group adoption tracker for current state-by-state status; the state list in any artifact is dated and verified-on-engagement, not frozen.

## Unfair-discrimination spine — NAIC Model #880

- **NAIC Unfair Trade Practices Act, Model #880**. The historical spine of insurance unfair-discrimination law. §4(7) (or successor section per the current model edition — verify section labels against the live NAIC Model Laws & Regulations index) prohibits unfair discrimination in rates, premiums, and policy benefits between individuals of the same class and equal expectation of life or hazard. The test is actuarial-justification-driven: differences in rate are permitted where supported by sound actuarial principles applied to credible data; differences in rate not so supported are unfairly discriminatory. Permitted-vs-prohibited rating-factor lists are state-specific and live in the state insurance code, not in the model. Protected classes for insurance unfair-discrimination are state-defined and are not coterminous with the ECOA / Reg B protected-class list. https://content.naic.org/ . Verify exact section labels and the most-recent model revision date on the analysis date.

## NAIC AI frame

- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers, December 2023** (Model Bulletin). Sets the AIS Program structure: governance and risk management, third-party AI accountability, testing and validation, monitoring, documentation, transparency, and fairness. The Bulletin is model text adopted state-by-state; adoption status is tracked by the NAIC AI Working Group. https://content.naic.org/sites/default/files/inline-files/2023-12-4%20Model%20Bulletin_Adopted_0.pdf — verify URL on the analysis date and the current adoption tracker. The Bulletin is not federal law; bindingness is state-by-state.

- **NAIC Principles on Artificial Intelligence, August 2020**. Five principles — fair / ethical, accountable, compliant, transparent, secure / safe / robust. Carry as the upstream principles set; the December 2023 Bulletin is the operative document for carrier-level AIS Program design. https://content.naic.org/sites/default/files/inline-files/AI%20principles%20final.pdf — verify URL.

- **NAIC AI Working Group adoption tracker (current)**. Public-facing adoption status of the December 2023 Model Bulletin by state. https://content.naic.org/cmte_h_aiwg.htm — verify URL on the analysis date.

## State DOI bulletins on AI in insurance

- **Colorado SB 21-169** (2021) and the **Colorado Division of Insurance Regulation 10-1-1** implementing the Act. Regulation 10-1-1 covers governance and risk management of external consumer data and information sources (ECDIS) and predictive models in life-insurance underwriting; the regulation was amended October 15, 2025 [verify the current scope and any expansion to product lines beyond life-insurance underwriting on the analysis date]. The Colorado posture is the most prescriptive in the United States on ECDIS provenance, governance, monitoring, and consumer-recourse. https://leg.colorado.gov/bills/sb21-169 ; https://doi.colorado.gov/ — verify exact effective date of the October 15, 2025 amendment and the current scope.

- **NY DFS Insurance Circular Letter No. 7 (2024)** on the use of artificial intelligence systems and external consumer data and information sources (ECDIS) in insurance underwriting and pricing [verify final issuance date and any amendment — Circular Letter No. 7 issued in 2024 superseded the earlier proposal; the operative scope covers life-insurance underwriting and pricing and may extend further per subsequent NY DFS guidance]. Sets disclosure, fairness, governance, and consumer-recourse expectations. https://www.dfs.ny.gov/industry_guidance/circular_letters/ — verify URL.

- **California Department of Insurance bulletin on the use of artificial intelligence in insurance** (verify exact bulletin number and issuance date). Broader scope than the CO regulation and the NY DFS Circular Letter; covers multiple lines of business. https://www.insurance.ca.gov/ — verify URL.

- **Other state DOI bulletins on AI in insurance**. Multiple states have adopted or signalled adoption of the NAIC December 2023 Model Bulletin or analogous guidance. Verify state-by-state on the analysis date via the NAIC AI Working Group adoption tracker.

## Life-product-specific frame

- **NAIC Life Insurance Illustrations Model Regulation, Model #582**. Illustration-format requirements; self-support and lapse-support tests; illustration-actuary certification; the disciplined-current-scale standard. Applies to ordinary individual life insurance with non-guaranteed elements. https://content.naic.org/ — verify exact section labels and current model revision date.

- **NAIC Suitability in Annuity Transactions Model Regulation, Model #275**. Best-interest standard for annuity transactions; producer training, disclosure, and supervision requirements. Applies to annuity sales rather than rate filings, but bolts on where the change touches annuity-product disclosures or producer-facing illustration material. https://content.naic.org/ — verify exact model number against the live NAIC index (the suitability-in-annuity model has gone through revisions and renumbering; the model number is marked `[verify]` on first cite).

## Health-product-specific frame

- **ACA pricing rules — Public Health Service Act §2701 (codified at 42 U.S.C. §300gg) and 45 CFR Part 147**. Applies to non-grandfathered individual and small-group health insurance. §2701 sets the rating-factor restriction (only family size, geography, age within a 3:1 band, and tobacco use within a 1.5:1 band). §147.102 sets the geographic-rating-area structure (states define rating areas subject to federal default rules). §147.106 governs guaranteed renewability. Verify the most-recent CMS rule revisions on the analysis date. https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-147 .

- **CMS guidance on rate review** (CMS-CCIIO Rate Review and Disclosure final rule, 45 CFR Part 154). Applies the federal rate-review framework to non-grandfathered individual and small-group health plans. https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-B/part-154 .

- **NAIC Accident and Sickness Insurance Minimum Standards Model Act (Model #170 — verify model number against current NAIC index)**. Underwriting and rating standards for individual A&H. Applies to certain health products outside the ACA-regulated frame.

## HIPAA frame

- **HIPAA Privacy Rule, 45 CFR Part 164 Subpart E**. §164.502 uses and disclosures of PHI; §164.504 organizational requirements; §164.506 uses for treatment, payment, and health care operations; §164.508 authorization for non-routine uses; §164.514 de-identification standard. Applies wherever the pricing or underwriting model touches PHI. https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E .

- **HIPAA Security Rule, 45 CFR Part 164 Subpart C**. Applies where PHI is in electronic form (most pricing-governance contexts). https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-C .

- **HHS OCR guidance on HIPAA and underwriting**. HIPAA reach: applies wherever the carrier or its underwriting model is a covered entity (a health plan or a healthcare provider transmitting health information electronically) or where the carrier acts as a business associate of a covered entity. For pure life-insurance underwriting where the carrier is not a HIPAA-covered entity, HIPAA may not directly apply but the same PHI may be in scope of the GLBA Privacy Rule, state insurance information-and-privacy frameworks, and any vendor-supplied data subject to HIPAA at the source. Verify current state of any HHS OCR guidance and the carrier's coverage analysis on the analysis date.

## ORSA and prudential frame

- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act, Model #505** (ORSA). Applies to insurers above the premium threshold (or by group election). The ORSA Summary Report carries the carrier's prospective solvency assessment and risk-management framework; pricing-AI exposure that is enterprise-material belongs in the ORSA Summary Report. https://content.naic.org/ — verify exact section labels and current model revision date.

- **NAIC Corporate Governance Annual Disclosure Model Act, Model #305** (verify model number). Carries the governance-and-control narrative the CGAD reviewer expects; the AIS Program for pricing-AI feeds the CGAD where material. https://content.naic.org/ — verify model number against current NAIC index.

## Model-risk frame (analogous)

- **SR 11-7 — Supervisory Guidance on Model Risk Management** (OCC Bulletin 2011-12 / FRB SR 11-7, April 2011). Federal banking model-risk guidance. Cite as **analogous** model-risk expectation language for ML pricing models in insurance; state DOIs increasingly point to SR 11-7 as analogous, not directly applicable. https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm .

- **OCC Bulletin 2026-13 (revised interagency model-risk management guidance — verify final issuance date and bulletin number)**. The successor / revision to SR 11-7 in the federal banking frame. Same analogous-citation posture for insurance: cite as analogous model-risk expectation language, not as binding. Mark `[verify final OCC 2026-13 issuance date and bulletin number]` on the analysis date until confirmed.

## Privacy-of-insurance-information frame

- **NAIC Insurance Information and Privacy Protection Model Act, Model #670** (verify model number). State-by-state adoption variable; in adopting states, sets disclosure and consumer-rights obligations for insurance-information practices including underwriting. https://content.naic.org/ — verify exact model number against current NAIC index.

- **State-level insurance information privacy frameworks**. Most states have adopted a version of Model #670 or a related state-specific framework; verify state-by-state on the analysis date.

## EU overlay (see-also)

- **Solvency II Directive (Directive 2009/138/EC)** as amended. Pillar 1 (capital), Pillar 2 (governance, ORSA), Pillar 3 (disclosure). Cite as **see-also** where the carrier has EU branches or reinsurance with EU cedents; the operative US frame for life-and-health pricing governance is NAIC and state DOI, not Solvency II. https://eur-lex.europa.eu/eli/dir/2009/138/oj .

- **EU AI Act, Regulation (EU) 2024/1689**. Annex III names insurance pricing and risk-assessment in life and health as a high-risk AI use case. Cite as **see-also** where the carrier has EU exposure; the operative US frame for life-and-health pricing AI governance is the NAIC AI Bulletin December 2023 plus state DOI bulletins. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689 .

## Source disciplines

- Date every external source on retrieval. Bulletins and model laws are revised; an artifact citing a stale revision reads as not-ready.
- `[verify section]` markers are deliberate, not omissions. Resolve before final issuance, not by guessing.
- Distinguish model text from state adoption. NAIC models bind nothing on their own; the state's adoption is the binding instrument.
- Cite SR 11-7 and OCC 2026-13 as analogous, not binding. State DOIs use the language as analogous expectation.
- Public defendants in finalised state-DOI rate-filing rejections or unfair-discrimination consent orders may be cited by name; otherwise, do not name institutions.
