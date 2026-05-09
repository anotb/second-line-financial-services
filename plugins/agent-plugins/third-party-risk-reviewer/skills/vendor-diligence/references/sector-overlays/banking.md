# Banking sector overlay — vendor-diligence

When the scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the banking-only frame that the generic capability skill does not own.

## Operative supervisory frame

- **Interagency Guidance on Third-Party Relationships: Risk Management** (OCC Bulletin 2023-17, FRB SR 23-4, FDIC FIL-29-2023, June 6, 2023). The diligence lifecycle (planning, due diligence and selection, contract negotiation, ongoing monitoring, termination) is the spine. Apply on a risk-based basis; community-bank tailoring narrative in the guidance is the right anchor for smaller institutions.
- **OCC Bulletin 2013-29** is still cited as the predecessor frame in supervisory practice. Where examiners reference it, treat as supplemental, not operative.
- **FFIEC IT Examination Handbook — Outsourcing Technology Services booklet** is the examiner-facing detail for technology vendors. Pin the current edition.
- **Comptroller's Handbook — Third-Party Relationships: Risk Management** [verify current edition] is the OCC examiner playbook for national banks and federal savings associations.
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for covered banks ($50B+): vendor-diligence outputs feed the risk-governance framework and the board's third-party oversight. Diligence packs for important and critical vendors should be visible to the independent risk-management function and reflected in board reporting.
- **FRB SR 12-17** consolidated supervision framework for BHCs: where the vendor sits across legal entities or supports a consolidated activity, the diligence pack should reflect the BHC view, not just the depository view.

## Banking-only contract anchor

- **Bank Service Company Act, 12 USC §1867(c)** — the statutory examiner-access right over bank service providers. The contract must preserve regulator examination access and audit rights. This is a banking-only clause expectation; non-bank vendor frameworks do not include it. Flag any contract that lacks the clause as a finding regardless of vendor tier.

## Insider screen

- **Reg O, 12 CFR Part 215** — diligence on a vendor whose principals are insiders (directors, executive officers, principal shareholders) of the partner bank, or affiliates thereof, must include the Reg O screen. Most non-bank vendor-diligence frameworks do not consider this; the banking overlay always does for relevant ownership structures.

## BaaS and bank-fintech arrangements

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC, OCC, FRB, July 25, 2024) [verify exact title and date]: where the vendor is a fintech program operator or BaaS platform, the operative document for the diligence is this statement, not just the June 2023 interagency guidance. Specific elements the diligence must cover: end-customer reconciliation, FBO subledger posture, deposit-insurance representation review (and the customer-facing FDIC framing), program-operator operational resilience, and the fourth-party register (processor, KYC vendor, fraud-decision vendor, ledger provider).
- **OCC Bulletin on Bank-Fintech Arrangements** [verify bulletin number]: where present in the firm's source list, treat as supplemental detail.
- **FFIEC inter-agency joint statement on community-bank fintech due diligence** (August 2023) [verify exact title]: for community banks engaging fintech partners; carries an explicit due-diligence checklist.

## Cross-link inside the plugin

- **`exit-plan` banking overlay** carries the FBO-account wind-down sequence, Reg DD §1030.5 and Reg E §1005.8 customer-notification responsibilities on deposit-account or credit-account termination, and Bank Service Company Act §1867(c) examination-access continuity through wind-down.
- **`concentration-risk-review`**: hyperscaler region, BaaS sponsor-bank reach, and core-banking vendor concentration all feed back into the banking-overlay concentration calculation.
- **`contract-gap-review` banking overlay** carries the Bank Service Company Act clause set, the deposit-insurance-representation clauses for BaaS arrangements, and the OCC Heightened Standards board-visibility clauses.

## AI vendor mode at a bank

When `ai_vendor=true` and the firm is a bank:

- **Joint interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026)** applies where the vendor supplies a **traditional statistical, quantitative, or non-generative, non-agentic AI model** used in a credit, compliance, or fraud decision. The guidance is most relevant to banking organisations with total assets over $30B and is non-binding (does not set forth enforceable standards). For an in-scope traditional model, diligence must align to model-risk governance, not only third-party risk. Footnote 3 of the guidance text excludes generative and agentic AI from scope.
- **For GenAI or agentic AI vendors**, the model-risk diligence lens routes to NIST AI 600-1 (Generative AI Profile), the NIST AI Risk Management Framework, the EU AI Act where the EU subsidiary is in scope, and the firm's AI-governance framework rather than to 2026-13. Run the AI-vendor branch in the diligence workflow (system-card fit, deployment-context evals, training-data posture, shared-responsibility, prompt-as-customer-data, model-version pin, agent-tool posture for agentic vendors), and chain to `ai-governance-model-risk/llm-vendor-evidence-review` where the question is "is this evidence pack sufficient for our deployment context".
- **Bank Service Company Act §1867(c)** still applies to AI vendors (traditional or GenAI). The examiner-access clause must extend to AI-system audit logs, evaluation evidence, and incident-response records.
- **OCC and FRB supervisory letters on AI use in banking** where applicable [verify specific letters relevant on the date of analysis] — chase the specific letter cited by the firm's regulatory affairs team.
- Cross-link to `ai-governance-model-risk/llm-vendor-evidence-review` via `ai_specific_findings.eval_evidence_status = deferred-to-evidence-review` and the linked record ID.

## Output-template additions for banking

- Bank Service Company Act §1867(c) clause status as a named finding line.
- Reg O insider screen as a named diligence step (status: `not-applicable | clear | flagged`).
- BaaS and bank-fintech-arrangement applicability check, with the July 2024 joint-statement element status.
- OCC Heightened Standards board-visibility status (only for $50B+ covered banks).

## Common pitfalls in banking diligence

- Treating a non-bank-vendor TPRM checklist as adequate. The banking overlay adds Bank Service Company Act, Reg O, OCC Heightened Standards, and the BaaS / bank-fintech-arrangement layer. None of these are in a generic SaaS diligence template.
- Skipping the consolidated-supervision lens at a BHC.
- Treating the June 2023 interagency guidance as "compliance" rather than as a risk-governance framework with examiner reach. The pack feeds the risk committee, not just the third-party-risk forum.
