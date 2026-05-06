# Capital-markets sector overlay — resilience-testing-pack

When the engagement scope flags capital markets, load this overlay alongside `references/source-anchors.md`. It carries the capital-markets-only frame the generic capability skill does not own.

## Operative supervisory frame

- **Reg SCI — 17 CFR §242.1000 et seq.** SCI entities (national securities exchanges, registered clearing agencies, certain ATSs, plan processors, FINRA, MSRB) carry a defined testing programme: business-continuity-and-disaster-recovery (BCDR) test with the participation of designated members; industry-wide test obligations; testing-of-system-changes; reporting and review of test results [verify subsection numbering]. For SCI entities, the resilience-testing pack reads against Reg SCI test obligations directly.
- **CFTC system-safeguards rules** (17 CFR §38.1051 for DCMs; 17 CFR §39.18 for DCOs; 17 CFR §49.24 for SDRs) [verify section]. Testing-and-exercise expectations on covered entities; participation of key third parties.
- **FINRA business-continuity testing notices and Rule 4370** [verify reference]. Member-firm BCP testing expectations; vendor and third-party participation in test posture.
- **Investment Advisers Act Rule 206(4)-7** — adviser compliance-program rule; the operational-resilience programme of an adviser sits inside the compliance program for compliance-program-purposes.
- **Investment Company Act Rule 38a-1(a)(4)** — fund compliance-program rule; service-provider compliance-program adequacy includes the service provider's BCDR testing posture.
- **DORA — Regulation (EU) 2022/2554, Articles 24-26** [verify subarticle]. EU investment firms, MTFs, OTFs, fund managers in scope of DORA carry the digital operational resilience testing programme; this overlay is the EU capital-markets cut.

## SCI-entity testing programme

For SCI entities specifically, the testing pack carries:

- Annual industry-wide test (designated members participate; SEC observation posture); the pack reads against Reg SCI subsection numbering [verify subsection].
- BCDR test with designated members; the designated-members list is reviewed with each cycle.
- Testing-of-system-changes per Reg SCI [verify subsection]; resilience testing covers material changes to SCI systems.
- Notice-and-reporting of test results to the SEC [verify subsection]; the read-out template feeds the regulatory submission.

## Adviser, BD, and fund testing

For non-SCI investment advisers, broker-dealers, and registered funds:

- **Adviser testing** — operational-resilience testing usually sits inside the Rule 206(4)-7 compliance-program review with annual testing of the adviser's BCP.
- **Broker-dealer testing** — FINRA Rule 4370 [verify reference] BCP testing; vendor-participation expectations.
- **Fund testing** — Rule 38a-1(a)(4) service-provider BCDR-adequacy assessment; the fund's CCO reviews the service-provider testing posture; material findings escalate to the fund board.

## Books-and-records continuity during a test

- **Rule 17a-4 (BD)**, **Rule 204-2 (adviser)**, and **Rule 31a (fund)** preservation requirements continue through a test. Test artifacts that include books-and-records material are subject to the same preservation rules; preservation choreography is part of the evidence-collection plan.

## AI-vendor testing in capital markets

When `ai_in_scope=true` and the firm is in capital markets:

- **SEC Risk Alert on outsourced CCO arrangements** (2022) [verify exact title and date] for advisers using AI-augmented compliance vendors.
- **Reg S-P (May 2024 amendments)** [verify exact compliance dates] — service-provider testing posture on customer-information safeguarding for advisers, BDs, and funds.
- **NIST AI Risk Management Framework 1.0** Govern function [verify subsection] — vendor-AI continuity reads alongside the operational-resilience programme.

## Cross-link inside the plugin

- **`vendor-diligence` capital-markets overlay** carries the diligence depth the testing pack consumes (transfer agent, fund accountant, custodian, sub-adviser, claims TPA equivalents in capital markets).
- **`exit-plan` capital-markets overlay** carries fund-board notice timing and ICA §15 considerations on service-provider transitions tested.
- **`concentration-risk-review`** for the firm's exposure across critical infrastructure providers (clearing-and-settlement, market data, custody, primary-broker concentration).
- **`contract-gap-review` capital-markets overlay**: where a test surfaces a contract gap (BCDR-testing flow-down, vendor-participation in firm BCP testing), chain to the contract-gap review.

## Output-template additions for capital markets

- Reg SCI subsection citation under programme alignment for SCI entities, including industry-wide test status.
- Fund-board reporting line under findings-and-actions framework where the firm is a registered fund or its adviser.
- Books-and-records preservation line under evidence-collection plan with the operative rule (17a-4 / 204-2 / 31a).
- DORA-programme alignment line for EU entities in scope.

## Common pitfalls in capital-markets resilience testing

- Treating Reg SCI obligations as a one-off compliance line rather than the spine of the SCI-entity testing pack.
- Skipping designated-member coordination on the BCDR test for SCI entities; designated-member participation is the test.
- Skipping fund-board reporting for material findings at a registered fund; the fund's CCO and the fund board are in the read-out path.
- Treating books-and-records preservation as separate from the testing pack; test artifacts that include preserved-record material are inside the rule.
- Skipping vendor participation on critical-infrastructure dependencies (clearing-and-settlement, market data); a test where the critical vendor is not in the room is a partial test.
- Treating an EU subsidiary as outside DORA scope when its parent is non-EU; DORA scope reaches the EU entity directly.
