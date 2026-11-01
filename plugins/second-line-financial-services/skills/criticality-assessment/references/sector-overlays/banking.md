# Banking sector overlay — criticality-assessment

When the scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the banking-only criteria the generic capability skill does not own.

## Operative supervisory frame

- **Interagency Guidance on Third-Party Relationships: Risk Management** (OCC Bulletin 2023-17, FRB SR 23-4, FDIC FIL-29-2023, June 6, 2023). Criticality is risk-based and proportionate. Activities that pose higher risk warrant more rigorous oversight; community-bank tailoring narrative in the guidance is the right anchor for smaller institutions.
- **OCC Bulletin 2013-29** is still cited in supervisory practice as the predecessor framing for "critical activities".
- **FFIEC Information Technology Examination Handbook — Outsourcing Technology Services and Business Continuity Management booklets** [verify current edition and section structure] for the BIA frame that drives the firm's recovery objectives.
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for covered banks ($50B+): the criticality call feeds the risk-governance framework and the board's third-party oversight. A `critical` call belongs on the risk-committee agenda regardless of vendor spend.

## Candidate IBS for banks

Important business services at a bank typically include payments (retail, commercial, cards), deposit-account servicing, lending and loan-servicing, custody where in-scope, and credit-decisioning where the bank operates the model. The IBS list is the firm's, not a regulator's; the candidate list above tracks BCBS Principles for Operational Resilience (March 2021) and the supervisory expectations in interagency and PRA materials. Where an arrangement sits on the critical chain of any of these, the criticality call moves toward `critical`.

## BaaS and bank-fintech-arrangement applicability

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. Where the arrangement is a fintech program operator or BaaS platform, the criticality call must read end-customer reconciliation, FBO subledger, deposit-insurance representation accuracy, and the program-operator's own resilience as inputs to the tier. A BaaS program that touches the deposit-servicing IBS is critical-by-default; flag any other read for explicit rationale.

## Community-bank tailoring

- **FFIEC inter-agency joint statement on community-bank fintech due diligence** (August 2021, FIL-59-2021) [verify exact title]. Community banks may run a leaner criticality framework, but the IBS test still applies. The tier is set by impact on the IBS, not by the bank's size.

## Examiner-reach lens

- **Bank Service Company Act, 12 USC §1867(c)**. Statutory examiner-access right over bank service providers. Not a criticality-tier driver on its own, but a reminder that any arrangement at the bank must preserve examiner access; surfaces in `vendor-diligence` and `contract-gap-review` downstream.

## Cross-link inside the plugin

- **`vendor-diligence` banking overlay** consumes the `tier` and the named IBS to set diligence depth.
- **`exit-plan` banking overlay** consumes the `tier`, the supported IBS, and the customer-impact read to set transition mechanics, including FBO-account wind-down for BaaS arrangements.
- **`concentration-risk-review`** consumes the `concentration_considerations` flag to drive portfolio analysis on hyperscaler region, BaaS sponsor-bank reach, and core-banking vendor concentration.

## AI vendor mode at a bank

When `ai_vendor=true` and the firm is a bank:

- **Joint interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026)** applies where the arrangement supplies a **traditional statistical, quantitative, or non-generative, non-agentic AI model** used in a credit, compliance, or fraud decision. The guidance is most relevant to banking organisations with total assets over $30B and is non-binding (does not set forth enforceable standards). For an in-scope traditional model, the criticality call considers model-risk impact alongside operational impact; an AI vendor on the credit-decisioning IBS path is rarely below `important`. Footnote 3 of the guidance text excludes generative and agentic AI from scope.
- **For GenAI or agentic AI vendors**, the model-risk lens routes to NIST AI 600-1 (Generative AI Profile), the NIST AI Risk Management Framework, the EU AI Act where the EU subsidiary is in scope, and the firm's AI-governance framework rather than to 2026-13. The criticality call still considers AI-specific impact (decisioning influence, customer harm modes, model-version-pin volatility), but the regulatory anchor is different.
- A `critical` AI-vendor call (traditional or GenAI/agentic) triggers parallel review by the model-risk function downstream; record the cross-link.

## Output additions for banking

- IBS named explicitly and matched against the candidate list above.
- Recovery-objective gap (firm tolerance vs vendor commitment) called out as a finding line where present.
- BaaS or bank-fintech-arrangement applicability check included where the arrangement is a fintech program.

## Common pitfalls in banking criticality calls

- Setting tier on procurement category. "IT services" is not a tier; the IBS dependency sets the tier.
- Treating BaaS as a pass-through arrangement. The program operator sits on the deposit-servicing IBS path.
- Missing the consolidated-supervision lens at a BHC. Where the arrangement supports a consolidated activity, the criticality read should reflect the BHC view, not just the depository view.
- Allowing vendor commitment to set the recovery objective. Tolerance comes from the IBS impact analysis.
