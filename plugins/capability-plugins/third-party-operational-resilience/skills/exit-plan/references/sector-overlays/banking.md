# Banking sector overlay — exit-plan

When the engagement scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the banking-only frame the generic capability skill does not own.

## Operative supervisory frame

- **Interagency Guidance on Third-Party Relationships: Risk Management** (June 6, 2023) termination expectations are the spine. Apply on a risk-based basis; community-bank tailoring narrative is the right anchor for smaller institutions.
- **OCC Bulletin 2013-29** is still cited as the predecessor framing in supervisory practice; treat as supplemental.
- **FFIEC IT Examination Handbook — Outsourcing Technology Services and Business Continuity Management booklets** are examiner-facing detail. Pin the current edition for both.
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for $50B+ covered banks: the exit plan and its testing posture feed the risk-governance framework and the board's third-party oversight. The board should see the exit-plan testing cadence and outcomes for critical and important arrangements.
- **FRB SR 12-17 consolidated supervision framework** for BHCs: where the vendor sits across legal entities or supports a consolidated activity, the exit plan reflects the BHC view, not just the depository view.

## Banking-only termination clause anchor

- **Bank Service Company Act, 12 USC §1867(c)** — examiner-access right continues through wind-down. The contract must preserve regulator examination access and audit rights into the transition window; the plan must show the actual evidence-preservation choreography (which logs, by whom, with what retention) so that an examiner asking after cutover can still get the records.

## Customer-notice anchors (banking)

- **Reg DD, 12 CFR §1030.5** — change-in-terms notification on deposit accounts. Drives the customer-notice clock for any transition that changes the customer experience on a deposit account (statement format, fee structure, IVR or app behaviour, account-number reformatting).
- **Reg E, 12 CFR §1005.8** — change-in-terms notification on consumer-EFT services (debit, bill-pay, electronic transfers). Where the transition changes terms governing EFT services, the longer of the two clocks usually controls.
- **Reg Z, 12 CFR §1026.9** — change-in-terms on open-end consumer credit accounts where applicable [verify subsection].

## FBO-account wind-down (sponsor-bank arrangements)

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. Where the exit-plan covers a fintech program operator or BaaS platform, specific elements:
  - End-customer reconciliation through the cutover with a per-customer ledger reconciliation.
  - FBO subledger validation against the bank's GL, with the seam dated.
  - Deposit-insurance representation: the customer-facing FDIC framing must remain accurate through and after the transition.
  - Customer-notice: program-end notice to end-customers is a sponsor-bank responsibility that cannot be delegated only to the program operator.
  - Fourth-party register: processor, KYC vendor, fraud-decision vendor, ledger provider all in the transition scope.

## OCC Heightened Standards considerations

- For $50B+ covered banks, the exit plan and its test history feed the risk-governance framework. The independent risk-management function must see the plan; the board sees the testing cadence and outcomes for critical arrangements.
- Material vendor changes are commonly inside the firm's risk-appetite policy and need RAS-aligned reporting on transition.

## AI vendor mode at a bank

When `ai_vendor=true` and the firm is a bank:

- **Joint interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026)** applies where the vendor supplies a **traditional statistical, quantitative, or non-generative, non-agentic AI model** used in a credit, compliance, or fraud decision. The guidance is most relevant to banking organisations with total assets over $30B and is non-binding (does not set forth enforceable standards). For an in-scope traditional model, exit planning must address model-risk continuity (substitute model evaluation, transition-period decisioning posture, model-risk-committee approval of the substitute). Footnote 3 of the guidance text excludes generative and agentic AI from scope.
- **For GenAI or agentic AI vendors**, the model-risk continuity lens routes to NIST AI 600-1 (Generative AI Profile), the NIST AI Risk Management Framework, the EU AI Act where the EU subsidiary is in scope, and the firm's AI-governance framework rather than to 2026-13. The transition-engineering work (prompt-template portability, RAG migration, model-version pin handling, guardrail and eval porting, agent-tool offboarding) sits in the AI-specific transition section of the plan; the regulatory anchor for the substitute's evaluation is the AI-governance frame.
- **Bank Service Company Act §1867(c)** examination access still applies on AI-vendor exit (traditional or GenAI). Audit logs, evaluation evidence, and incident-response records must be preserved through the transition.
- **OCC and FRB supervisory letters on AI use in banking** where applicable [verify specific letters relevant on the date of analysis].
- Cross-link to `ai-governance-model-risk/llm-vendor-evidence-review` for the substitute model's evidence-pack review.

## Cross-link inside the plugin

- **`vendor-diligence` banking overlay** carries the diligence depth the exit plan consumes via the diligence record (subcontractors, data_access, residual_risk).
- **`contract-gap-review` banking overlay** carries the Bank Service Company Act clause set, the regulator-directed-termination clause expectation, and the BaaS deposit-insurance-representation clauses; the exit plan flags clause gaps and chains for the clause-by-clause read.
- **`concentration-risk-review`**: hyperscaler region, BaaS sponsor-bank reach, and core-banking vendor concentration drive the substitute-vendor viability read.
- **`resilience-testing-pack` banking overlay**: the exit-rehearsal scenario set sits inside the integrated test programme.

## Output-template additions for banking

- Bank Service Company Act §1867(c) examination-access continuity posture as a named line under supervisory readiness.
- Reg DD §1030.5 and Reg E §1005.8 lead-time calculation as named entries under customer notice.
- Joint-statement element status under fourth-party dependencies for sponsor-bank arrangements.
- OCC Heightened Standards board-visibility status (only for $50B+ covered banks).

## Common pitfalls in banking exit planning

- Treating the vendor's transition-assistance commitment as the plan. The clause is not the playbook.
- Skipping Bank Service Company Act §1867(c) preservation choreography. Examiner access continues through wind-down whether or not the contract says so.
- Missing the longer of the Reg DD and Reg E change-in-terms clocks on a transition that affects both services.
- Treating a sponsor-bank-program exit as a pure operational matter. End-customer reconciliation and deposit-insurance representation are bank-licensed responsibilities, not delegatable to the program operator.
- Skipping consolidated-supervision lens at a BHC.
- Treating an AI-vendor exit as just-another-vendor exit. The model-risk continuity and the substitute model's evaluation are part of the plan, not a separate workstream.
