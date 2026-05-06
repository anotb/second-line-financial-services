# Banking sector overlay — resilience-testing-pack

When the engagement scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the banking-only frame the generic capability skill does not own.

## Operative supervisory frame

- **Interagency Guidance on Third-Party Relationships: Risk Management** (June 6, 2023) ongoing-monitoring section [verify section]. Vendor-performance and contingency-plan testing posture sits inside the ongoing-monitoring expectation. Apply on a risk-based basis.
- **FFIEC IT Examination Handbook — Business Continuity Management booklet** [verify current edition and section]. Testing-and-exercise section is the examiner-facing reference for tabletop, walkthrough, simulation, and full-functional exercise method definitions and for the test-result review expectation.
- **FFIEC IT Examination Handbook — Outsourcing Technology Services booklet** [verify current edition and section]. Vendor BCDR-test posture; firm review of vendor test results.
- **FFIEC inter-agency cloud joint statement** (Security in a Cloud Computing Environment, April 30, 2020) [verify exact title]. Cloud-services BCDR testing including failover validation and customer-data-portability rehearsals.
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for $50B+ covered banks: the testing programme and outcomes feed the risk-governance framework. The board sees the testing cadence and outcomes for critical IBS and critical arrangements.
- **FRB SR 12-17 consolidated supervision framework** for BHCs: where the IBS spans legal entities, the testing pack reflects the BHC view, not just the depository view.

## IBS-level testing at large banks

Large banks typically run a multi-year programme that mixes:

- Annual tabletop on every IBS at minimum.
- Walkthrough or partial-simulation on each IBS over a multi-year cycle.
- Full-live exercise on the highest-impact IBS over a longer cycle (every two-to-three years is common at programme maturity, with safety controls).
- Quarterly cadence on payments-rails failover for banks with material payments exposure.
- Annual industry-wide tabletop participation where invited by sector associations or supervisors.

## Sponsor-bank programme testing (BaaS)

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. For sponsor-bank arrangements, the testing pack should include:
  - End-customer reconciliation rehearsal: the bank's GL against the program operator's FBO subledger, with the seam dated.
  - Deposit-insurance-representation continuity in a program-operator distress scenario.
  - Customer-notice rehearsal under program-end conditions; the customer-notice obligation is a sponsor-bank responsibility that cannot be delegated only to the program operator.
  - Fourth-party register exercised: processor, KYC vendor, fraud-decision vendor, ledger provider all in scope.

## OCC Heightened Standards considerations

- For $50B+ covered banks, the testing programme and outcomes feed the risk-governance framework. The independent risk-management function reviews the programme; the board sees the testing cadence and outcomes for critical IBS and critical arrangements.
- Material vendor-test failures are commonly inside the firm's risk-appetite reporting and need RAS-aligned escalation.

## AI-vendor testing at a bank

When `ai_in_scope=true` and the firm is a bank:

- **OCC Bulletin 2026-13 (revised interagency model risk management guidance, 2026)** [verify current title, date, and bulletin number] applies where the AI vendor supplies a model used in a credit, compliance, or fraud decision. Resilience testing must include a model-risk-continuity scenario: model regression, vendor model deprecation, training-data incident at the vendor.
- **Bank Service Company Act §1867(c)** examination access continues during and after a test. Test artifacts and evidence are inside scope of examination access; preservation choreography is part of the evidence-collection plan.
- Cross-link to `ai-governance-model-risk/llm-vendor-evidence-review` for substitute model evidence-pack readiness on a partial-simulation that exercises a substitute.

## Cross-link inside the plugin

- **`vendor-diligence` banking overlay** carries the diligence depth the testing pack consumes via the linked vendor-diligence records.
- **`exit-plan` banking overlay** carries exit-rehearsal scenario design; the testing pack hosts the rehearsal scenario inside the integrated programme.
- **`concentration-risk-review`**: hyperscaler region, BaaS sponsor-bank reach, and core-banking vendor concentration drive the portfolio scenarios in the testing pack.
- **`contract-gap-review` banking overlay**: where a test surfaces a contract gap (regulator-directed-termination, examination-access flow-down), chain to the contract-gap review.

## Output-template additions for banking

- OCC Heightened Standards board-visibility line under programme alignment for $50B+ covered banks.
- Bank Service Company Act §1867(c) evidence-preservation line under evidence-collection plan.
- Sponsor-bank reconciliation rehearsal scenario where applicable, with the joint-statement element checklist as the evidence-collection scope.
- Payments-rails failover scenario where the firm has material payments exposure.

## Common pitfalls in banking resilience testing

- Treating vendor-published BCDR-test summaries as the firm's test. The firm reviews and challenges; it does not borrow the vendor's testing as its own.
- Skipping examination-access continuity in the evidence-collection plan; supervisor inspection runs against test artifacts as well as production records.
- Setting tolerance from the IBS owner's preference rather than from the firm's IBS map. The map is the source.
- Treating sponsor-bank-program testing as the program operator's responsibility. The bank designs and approves; the operator participates.
- Skipping the consolidated-supervision lens at a BHC.
- Treating an AI-vendor scenario as just-another-vendor scenario. Model regression and deprecation are model-risk-continuity scenarios, not generic outage scenarios.
