# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — resilience-testing-pack

When the scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the banking-only frame the generic capability skill does not own.

#### Operative supervisory frame

- **Interagency Guidance on Third-Party Relationships: Risk Management** (June 6, 2023) ongoing-monitoring section [verify section]. Vendor-performance and contingency-plan testing posture sits inside the ongoing-monitoring expectation. Apply on a risk-based basis.
- **FFIEC IT Examination Handbook — Business Continuity Management booklet** [verify current edition and section]. Testing-and-exercise section is the examiner-facing reference for tabletop, walkthrough, simulation, and full-functional exercise method definitions and for the test-result review expectation.
- **FFIEC IT Examination Handbook — Outsourcing Technology Services booklet** [verify current edition and section]. Vendor BCDR-test posture; firm review of vendor test results.
- **FFIEC inter-agency cloud joint statement** (Security in a Cloud Computing Environment, April 30, 2020) [verify exact title]. Cloud-services BCDR testing including failover validation and customer-data-portability rehearsals.
- **12 CFR Part 30 Appendix D (OCC Heightened Standards)** for $50B+ covered banks: the testing programme and outcomes feed the risk-governance framework. The board sees the testing cadence and outcomes for critical IBS and critical arrangements.
- **FRB SR 12-17 consolidated supervision framework** for BHCs: where the IBS spans legal entities, the testing pack reflects the BHC view, not just the depository view.

#### IBS-level testing at large banks

Large banks typically run a multi-year programme that mixes:

- Annual tabletop on every IBS at minimum.
- Walkthrough or partial-simulation on each IBS over a multi-year cycle.
- Full-live exercise on the highest-impact IBS over a longer cycle (every two-to-three years is common at programme maturity, with safety controls).
- Quarterly cadence on payments-rails failover for banks with material payments exposure.
- Annual industry-wide tabletop participation where invited by sector associations or supervisors.

#### Sponsor-bank programme testing (BaaS)

- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. For sponsor-bank arrangements, the testing pack should include:
  - End-customer reconciliation rehearsal: the bank's GL against the program operator's FBO subledger, with the seam dated.
  - Deposit-insurance-representation continuity in a program-operator distress scenario.
  - Customer-notice rehearsal under program-end conditions; the customer-notice obligation is a sponsor-bank responsibility that cannot be delegated only to the program operator.
  - Fourth-party register exercised: processor, KYC vendor, fraud-decision vendor, ledger provider all in scope.

#### OCC Heightened Standards considerations

- For $50B+ covered banks, the testing programme and outcomes feed the risk-governance framework. The independent risk-management function reviews the programme; the board sees the testing cadence and outcomes for critical IBS and critical arrangements.
- Material vendor-test failures are commonly inside the firm's risk-appetite reporting and need RAS-aligned escalation.

#### AI-vendor testing at a bank

When `ai_in_scope=true` and the firm is a bank:

- **Joint interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026)** applies where the AI vendor supplies a **traditional statistical, quantitative, or non-generative, non-agentic AI model** used in a credit, compliance, or fraud decision. The guidance is most relevant to banking organisations with total assets over $30B and is non-binding (does not set forth enforceable standards). For an in-scope traditional model, resilience testing must include a model-risk-continuity scenario: model regression, vendor model deprecation, training-data incident at the vendor. Footnote 3 of the guidance text excludes generative and agentic AI from scope.
- **For GenAI or agentic AI vendors**, the model-risk continuity scenario set routes to NIST AI 600-1 (Generative AI Profile), the NIST AI Risk Management Framework, the EU AI Act where the EU subsidiary is in scope, and the firm's AI-governance framework rather than to 2026-13. Add GenAI-specific scenarios alongside generic-vendor-outage scenarios: model regression on the deployed system (base + fine-tune + RAG + retrieval + carrier-side guardrails), eval drift, prompt-injection on the deployed agent, vendor model-version deprecation, training-data incident at the vendor, agent-tool sandbox compromise on agentic systems. The model-risk function reviews the GenAI scenario set.
- **Bank Service Company Act §1867(c)** examination access continues during and after a test (traditional or GenAI). Test artifacts and evidence are inside scope of examination access; preservation choreography is part of the evidence-collection plan.
- Cross-link to `llm-vendor-evidence-review` for substitute model evidence-pack readiness on a partial-simulation that exercises a substitute.

#### Cross-link inside the plugin

- **`vendor-diligence` banking overlay** carries the diligence depth the testing pack consumes via the linked vendor-diligence records.
- **`exit-plan` banking overlay** carries exit-rehearsal scenario design; the testing pack hosts the rehearsal scenario inside the integrated programme.
- **`concentration-risk-review`**: hyperscaler region, BaaS sponsor-bank reach, and core-banking vendor concentration drive the portfolio scenarios in the testing pack.
- **`contract-gap-review` banking overlay**: where a test surfaces a contract gap (regulator-directed-termination, examination-access flow-down), chain to the contract-gap review.

#### Output-template additions for banking

- OCC Heightened Standards board-visibility line under programme alignment for $50B+ covered banks.
- Bank Service Company Act §1867(c) evidence-preservation line under evidence-collection plan.
- Sponsor-bank reconciliation rehearsal scenario where applicable, with the joint-statement element checklist as the evidence-collection scope.
- Payments-rails failover scenario where the firm has material payments exposure.

#### Common pitfalls in banking resilience testing

- Treating vendor-published BCDR-test summaries as the firm's test. The firm reviews and challenges; it does not borrow the vendor's testing as its own.
- Skipping examination-access continuity in the evidence-collection plan; supervisor inspection runs against test artifacts as well as production records.
- Setting tolerance from the IBS owner's preference rather than from the firm's IBS map. The map is the source.
- Treating sponsor-bank-program testing as the program operator's responsibility. The bank designs and approves; the operator participates.
- Skipping the consolidated-supervision lens at a BHC.
- Treating an AI-vendor scenario as just-another-vendor scenario. Model regression and deprecation are model-risk-continuity scenarios, not generic outage scenarios.

## capital-markets

### Capital-markets sector overlay — resilience-testing-pack

When the scope flags capital markets, load this overlay alongside `references/source-anchors.md`. It carries the capital-markets-only frame the generic capability skill does not own.

#### Operative supervisory frame

- **Reg SCI — 17 CFR §242.1000 et seq.** SCI entities (national securities exchanges, registered clearing agencies, certain ATSs, plan processors, FINRA, MSRB) carry a defined testing programme: business-continuity-and-disaster-recovery (BCDR) test with the participation of designated members; industry-wide test obligations; testing-of-system-changes; reporting and review of test results [verify subsection numbering]. For SCI entities, the resilience-testing pack reads against Reg SCI test obligations directly.
- **CFTC system-safeguards rules** (17 CFR §38.1051 for DCMs; 17 CFR §39.18 for DCOs; 17 CFR §49.24 for SDRs) [verify section]. Testing-and-exercise expectations on covered entities; participation of key third parties.
- **FINRA business-continuity testing notices and Rule 4370** [verify reference]. Member-firm BCP testing expectations; vendor and third-party participation in test posture.
- **Investment Advisers Act Rule 206(4)-7** — adviser compliance-program rule; the operational-resilience programme of an adviser sits inside the compliance program for compliance-program-purposes.
- **Investment Company Act Rule 38a-1(a)(4)** — fund compliance-program rule; service-provider compliance-program adequacy includes the service provider's BCDR testing posture.
- **DORA — Regulation (EU) 2022/2554, Articles 24-26** [verify subarticle]. EU investment firms, MTFs, OTFs, fund managers in scope of DORA carry the digital operational resilience testing programme; this overlay is the EU capital-markets cut.

#### SCI-entity testing programme

For SCI entities specifically, the testing pack carries:

- Annual industry-wide test (designated members participate; SEC observation posture); the pack reads against Reg SCI subsection numbering [verify subsection].
- BCDR test with designated members; the designated-members list is reviewed with each cycle.
- Testing-of-system-changes per Reg SCI [verify subsection]; resilience testing covers material changes to SCI systems.
- Notice-and-reporting of test results to the SEC [verify subsection]; the read-out template feeds the regulatory submission.

#### Adviser, BD, and fund testing

For non-SCI investment advisers, broker-dealers, and registered funds:

- **Adviser testing** — operational-resilience testing usually sits inside the Rule 206(4)-7 compliance-program review with annual testing of the adviser's BCP.
- **Broker-dealer testing** — FINRA Rule 4370 [verify reference] BCP testing; vendor-participation expectations.
- **Fund testing** — Rule 38a-1(a)(4) service-provider BCDR-adequacy assessment; the fund's CCO reviews the service-provider testing posture; material findings escalate to the fund board.

#### Books-and-records continuity during a test

- **Rule 17a-4 (BD)**, **Rule 204-2 (adviser)**, and **Rule 31a (fund)** preservation requirements continue through a test. Test artifacts that include books-and-records material are subject to the same preservation rules; preservation choreography is part of the evidence-collection plan.

#### AI-vendor testing in capital markets

When `ai_in_scope=true` and the firm is in capital markets:

- **SEC Risk Alert on outsourced CCO arrangements** (2022) [verify exact title and date] for advisers using AI-augmented compliance vendors.
- **Reg S-P (May 2024 amendments)** [verify exact compliance dates] — service-provider testing posture on customer-information safeguarding for advisers, BDs, and funds.
- **NIST AI Risk Management Framework 1.0** Govern function [verify subsection] — vendor-AI continuity reads alongside the operational-resilience programme.

#### Cross-link inside the plugin

- **`vendor-diligence` capital-markets overlay** carries the diligence depth the testing pack consumes (transfer agent, fund accountant, custodian, sub-adviser, claims TPA equivalents in capital markets).
- **`exit-plan` capital-markets overlay** carries fund-board notice timing and ICA §15 considerations on service-provider transitions tested.
- **`concentration-risk-review`** for the firm's exposure across critical infrastructure providers (clearing-and-settlement, market data, custody, primary-broker concentration).
- **`contract-gap-review` capital-markets overlay**: where a test surfaces a contract gap (BCDR-testing flow-down, vendor-participation in firm BCP testing), chain to the contract-gap review.

#### Output-template additions for capital markets

- Reg SCI subsection citation under programme alignment for SCI entities, including industry-wide test status.
- Fund-board reporting line under findings-and-actions framework where the firm is a registered fund or its adviser.
- Books-and-records preservation line under evidence-collection plan with the operative rule (17a-4 / 204-2 / 31a).
- DORA-programme alignment line for EU entities in scope.

#### Common pitfalls in capital-markets resilience testing

- Treating Reg SCI obligations as a one-off compliance line rather than the spine of the SCI-entity testing pack.
- Skipping designated-member coordination on the BCDR test for SCI entities; designated-member participation is the test.
- Skipping fund-board reporting for material findings at a registered fund; the fund's CCO and the fund board are in the read-out path.
- Treating books-and-records preservation as separate from the testing pack; test artifacts that include preserved-record material are inside the rule.
- Skipping vendor participation on critical-infrastructure dependencies (clearing-and-settlement, market data); a test where the critical vendor is not in the room is a partial test.
- Treating an EU subsidiary as outside DORA scope when its parent is non-EU; DORA scope reaches the EU entity directly.

## insurance

### Insurance sector overlay — resilience-testing-pack

When the scope flags insurance, load this overlay alongside `references/source-anchors.md`. It carries the insurance-only frame the generic capability skill does not own.

#### Operative supervisory frame

- **NAIC Insurance Data Security Model Law (Model #668), §4.F** third-party service-provider obligations. State-by-state adoption; firms operating in multiple states pin the operative state's adoption.
- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number]. Critical outsourced functions and their resilience posture are reflected in the ORSA Summary Report; material test failures may move ORSA conclusions.
- **NAIC Insurance Holding Company System Regulatory Act (Model #440)** [verify model number] and Holding Company Model Regulation (Model #450) [verify model number]. Form B / Form D considerations on affiliated-vendor arrangements that are tested.
- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers** (December 4, 2023). AIS Program elements include testing of third-party AI systems; resilience testing of AI-vendor arrangements feeds the AI-governance reporting line.
- **State-specific market-conduct expectations on claims-handling continuity**. Most states expect a documented BCDR posture for claims-handling; resilience testing demonstrates that posture.
- **EIOPA Guidelines on outsourcing to cloud service providers (2020)** [verify reference] for EU insurers; outsourcing-test posture similar in substance to the EBA cloud-outsourcing frame.

#### IBS-level scenarios common at insurers

- Claims-handling outage during high-volume event (catastrophe, cyber-event, market dislocation).
- Policy-administration vendor outage during the renewal cycle for the affected lines.
- TPA outage on a high-claims-volume line (auto, home, health).
- Reinsurance-portal outage during the cession-and-claims cycle.
- AI-vendor regression on underwriting or claims-triage models (where AI is in the chain).
- Document-management-vendor outage during the renewal-and-statement cycle.

#### Customer-impact considerations during a test

A test of claims-handling that surfaces real customer impact has direct policyholder consequences. Safety controls:

- Customer-impact-threshold for early termination set against the policyholder-protection statute in the operative state.
- Pre-positioned policyholder-comms templates for any test that may surface real claims-handling delay.
- Coordination with customer-experience and consumer-affairs functions before live tests on customer-affecting paths.

#### ORSA reporting alignment

- Material test results on critical outsourced functions feed the ORSA Summary Report. Track which test outcomes meet the ORSA materiality threshold the firm has set; surface them to the ERM committee for inclusion in the next ORSA cycle.
- Material vendor-test failures and the remediation status are commonly inside the ORSA narrative on operational risk and outsourcing.

#### AI-vendor testing at an insurer

When `ai_in_scope=true` and the firm is an insurer:

- **NAIC AI Bulletin** (December 2023) testing-and-validation expectations apply to third-party AI; the resilience pack covers vendor-AI continuity (model deprecation, regression, training-data incident) alongside the firm's own AI-governance-driven testing of model performance.
- **Colorado SB 21-169 implementing regulation** (3 CCR 702-10 §1 [verify section]) — for life-insurance underwriting using ECDIS or predictive models, governance-and-risk-management expectations apply, including vendor-AI test posture.
- **NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting** (January 2024) [verify circular number] — for NY-licensed life insurers, similar testing-of-AI expectations apply.

#### Cross-link inside the plugin

- **`vendor-diligence` insurance overlay** carries the diligence depth the testing pack consumes.
- **`exit-plan` insurance overlay** carries policyholder-protection-aware exit-rehearsal design.
- **`concentration-risk-review`** for the insurer's outsourcing-vendor concentration (TPA, claims-platform, document-management vendors).
- **`contract-gap-review` insurance overlay**: where a test surfaces a contract gap (data-portability on the policy-admin vendor, claims-handling-continuity language), chain to the contract-gap review.

#### Output-template additions for insurance

- ORSA-materiality flag on results above the firm's ORSA-narrative threshold.
- Policyholder-protection safety-control line under safety controls for live tests on claims-handling paths.
- AIS-Program reporting line under programme alignment where AI-in-scope is true.

#### Common pitfalls in insurance resilience testing

- Treating policy-administration as out of scope because it is not customer-facing in the same way as banking channels. Renewal-cycle disruption and statement-cycle disruption are customer-impact events.
- Skipping the catastrophe scenario on claims-handling. Catastrophe events stress claims-handling capacity in ways that day-to-day failures do not.
- Setting tolerance from the carrier's customer-experience preference rather than from the policyholder-protection statute floor in the operative state.
- Treating vendor-AI testing as a model-risk-only matter. Vendor-AI continuity is operational-resilience too: deprecation, regression, vendor distress, training-data incidents at the vendor.
- Skipping coordination with consumer-affairs and customer-experience before a live test on customer-affecting paths.

## payments-fintech

### Payments-fintech sector overlay — resilience-testing-pack

When the scope flags payments-fintech, load this overlay alongside `references/source-anchors.md`. It carries the payments-and-fintech-only frame the generic capability skill does not own.

#### Operative supervisory frame

- **Interagency Guidance on Third-Party Relationships: Risk Management** (June 6, 2023) ongoing-monitoring section [verify section]. Vendor-performance and contingency-plan testing for payments arrangements.
- **Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services** (FDIC / OCC / FRB, July 25, 2024) [verify exact title and date]. For sponsor-bank arrangements, the testing pack covers end-customer reconciliation, FBO subledger validation, deposit-insurance-representation continuity, and program-operator-distress scenarios.
- **Joint statement on community-bank fintech due diligence** (FIL-59-2021, August 27, 2021) [verify exact title and date]. Community-bank-specific testing-of-fintech-vendor expectations [verify section].
- **NACHA Operating Rules (current edition)** Third-Party Sender risk-management rules [verify rule citations]. ACH-network testing-of-failover and customer-impact handling.
- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (December 2024) [verify Federal Register citation and current state including any litigation or congressional review]. Where the firm or the vendor is a larger-participant payments platform, supervisory expectations on resilience testing apply.
- **FedNow and RTP operating rules** [verify references for current versions] — instant-payment-rails failover testing.

#### Payments-rails scenarios

Payments-fintech testing pack scenarios commonly include:

- Card-network connectivity loss (Visa, MasterCard, Amex, Discover; or interchange-network equivalents).
- ACH-rail outage (FedACH, EPN); NACHA Operating Rules failover posture.
- Instant-payment-rail outage (FedNow, RTP); failover to alternative rail or to scheduled-rail with customer-experience consequences.
- Card-issuing-processor outage (the firm's processor or a fourth-party processor on the BIN-sponsorship chain).
- BIN-sponsor-bank distress scenario (program-operator perspective) and program-operator-distress scenario (sponsor-bank perspective).
- Fraud-decisioning vendor outage during peak transaction volume.
- KYC vendor outage during peak onboarding volume.
- Hyperscaler-region failure on the firm's primary compute region (and the firm's reliance on a single region for the payments platform).
- Wallet-vendor or BIN-card-controls vendor outage.

#### Sponsor-bank programme testing

For sponsor-bank-and-program-operator arrangements (BaaS):

- End-customer reconciliation rehearsal: the bank's GL against the program operator's FBO subledger, with the seam dated.
- FBO subledger validation against the bank's records.
- Deposit-insurance-representation continuity in a program-operator distress scenario.
- Customer-notice rehearsal under program-end conditions; the customer-notice obligation is a sponsor-bank responsibility.
- Fourth-party register exercised: processor, KYC vendor, fraud-decision vendor, ledger provider all in scope.

The sponsor bank designs and approves the testing pack for the program; the program operator participates. A program operator running its own pack independent of the sponsor bank has misallocated the responsibility.

#### Customer-impact safety controls

For payments-rails tests that may surface real customer impact:

- Customer-impact-threshold safety control set against the firm's policy and the operative consumer-protection clock (Reg E §1005.6 unauthorised-EFT, §1005.11 error-resolution clocks for the affected service).
- Pre-positioned customer-comms templates including IVR, mobile-banking-app banner, and statement-message framing.
- Fraud-monitoring sensitivity adjusted during the test window to avoid false-positive cascades.
- Settlement-cycle awareness: an exercise that runs across a cutoff window has settlement-cycle implications that need pre-coordination.

#### AI-vendor testing in payments-fintech

When `ai_in_scope=true`:

- Fraud-decisioning vendor model regression scenario (the most common AI-on-payments scenario).
- KYC vendor AI-driven document-verification regression.
- Generative-AI customer-support vendor outage (where the vendor sits on customer-facing dispute-handling paths).

#### Cross-link inside the plugin

- **`vendor-diligence` payments-fintech overlay** carries the diligence depth the testing pack consumes.
- **`exit-plan` payments-fintech overlay** carries program-operator-distress and sponsor-bank-distress exit-rehearsal design.
- **`concentration-risk-review`** for the firm's BIN-sponsor exposure, processor concentration, hyperscaler-region exposure across the payments platform.
- **`contract-gap-review` payments-fintech overlay**: where a test surfaces a contract gap (joint-statement element coverage, NACHA Third-Party-Sender risk-management terms), chain to the contract-gap review.

#### Output-template additions for payments-fintech

- Sponsor-bank-program element checklist under evidence-collection plan for BaaS arrangements.
- Settlement-cycle awareness line under safety controls for tests that may run across cutoff windows.
- Reg E error-resolution clock line under customer-impact safety controls.
- NACHA Operating Rules failover scenario where the firm has material ACH exposure.

#### Common pitfalls in payments-fintech resilience testing

- Treating multi-rail architecture as a free failover posture without tested rail-to-rail cutover. Architecture is the hypothesis; the test is the evidence.
- Skipping settlement-cycle coordination on a test that runs across a cutoff window. The test becomes a real settlement event.
- Letting the fraud-monitoring system trigger on test traffic. Pre-coordinate to avoid false-positive cascades and customer-experience consequences.
- Treating sponsor-bank-program testing as the program operator's job. The sponsor bank designs and approves; the operator participates.
- Setting tolerance from the program operator's preference rather than from the sponsor bank's IBS-map tolerance. The bank is the regulated entity.
- Skipping fourth-party-processor scenarios where the BIN-sponsorship chain has multiple processors.
- Treating community-bank fintech-vendor testing as a check-the-box exercise; FIL-59-2021 [verify] expects substantive due-diligence and ongoing-monitoring including testing.
