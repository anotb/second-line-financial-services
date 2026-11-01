# Capital-markets sector overlay — criticality-assessment

When the scope flags capital markets, load this overlay alongside `references/source-anchors.md`. It carries the capital-markets-only criteria the generic capability skill does not own.

## Operative supervisory frame

- **Investment Advisers Act Rule 206(4)-7** — adviser compliance-program rule. The criticality call frames whether the arrangement supports an adviser-required function.
- **Investment Company Act Rule 38a-1(a)(4)** — fund compliance-program rule, including service-provider compliance-program-adequacy assessment for transfer agent, custodian, fund accountant, principal underwriter, valuation designee, pricing services. A vendor in any of these roles is at minimum `important`; many are `critical`.
- **FINRA Rule 3110 (supervision)** for broker-dealer arrangements that supervise registered persons or carry trade-and-order-handling responsibility.
- **Investment Advisers Act Rule 206(4)-2 (Custody Rule)** — qualified custodian arrangements; the custody chain is critical by construction.
- **Reg SCI — 17 CFR §242.1000 et seq.** Substitutability and BCDR posture for SCI entities; where the arrangement sits on an SCI system path the criticality call reflects the SCI obligations [verify subsection].
- **17 CFR Part 248 (Reg S-P) as amended May 16, 2024** [verify exact compliance dates] — customer-information-safeguarding obligations affect the data-scope and customer-impact reads.

## Candidate IBS for capital-markets entities

Important business services typically include order management, execution and routing, clearing, settlement, custody, transfer-agency, fund-accounting, NAV calculation and pricing, market-data distribution where the firm operates an SCI system, regulatory-reporting (CAT, EBLM, Form 13F, ADV, N-CEN, N-PORT), and investor communications. The IBS list is the firm's; the candidate list above tracks BCBS Principles for Operational Resilience (March 2021) translated into the capital-markets setting and the named-service-provider construct under Rule 38a-1.

## Fund-board lens

- For registered funds, the named-service-provider arrangements (transfer agent, custodian, fund accountant, principal underwriter, valuation designee, pricing services, sub-adviser) carry an explicit fund-board-oversight obligation under Rule 38a-1. The criticality call routes through the fund-board secretariat; an annual recertification cycle is the norm.
- **Investment Company Act §15** — investment advisory contracts; sub-adviser additions and replacements need shareholder vote or interim-contract authority under Rule 15a-4. The criticality call for a sub-adviser is `critical` by construction.

## Cross-link inside the plugin

- **`vendor-diligence` capital-markets overlay** consumes the `tier` and the named IBS to set diligence depth, including 38a-1 service-provider compliance-program-adequacy where applicable.
- **`exit-plan` capital-markets overlay** consumes the `tier`, the supported IBS, and the customer-impact read to set transition mechanics, including books-and-records continuity (Rule 204-2, Rule 17a-4, Rule 31a) and fund-board notice timing.
- **`concentration-risk-review`** consumes the `concentration_considerations` flag for transfer-agent, custodian, fund-accountant, sub-adviser, and pricing-service concentration.

## AI vendor mode at a capital-markets entity

When `ai_vendor=true`:

- An AI vendor on the order-management, execution-routing, NAV-calculation, or pricing path is rarely below `important`. Where the AI system reaches an SCI-system function, the SCI substitutability and BCDR obligations frame the criticality.
- An AI vendor supporting an adviser's investment process (research summarisation, factor extraction, signal generation) requires an explicit fiduciary lens; the criticality call must reflect adviser fiduciary accountability.
- A `critical` AI-vendor call triggers parallel review by the model-risk and AI governance functions; record the cross-link.

## Output additions for capital markets

- IBS named explicitly and matched against the candidate list above.
- Named-service-provider-under-38a-1 check for any registered-fund arrangement.
- SCI-system-path applicability check for SCI entities.
- Sub-adviser interim-contract-authority check for adviser-arrangement scenarios.

## Common pitfalls in capital-markets criticality calls

- Treating a "vendor" as outside the named-service-provider framework when the function it provides is actually a 38a-1 service. Transfer agency, fund accounting, and valuation are named services regardless of how the vendor describes itself.
- Skipping the SCI-system-path test for venues, market-makers, and clearing entities.
- Setting the tier without considering the fund-board oversight cadence. A `critical` call drives a different fund-board reporting line than an `important` call.
- Allowing vendor commitment to set the recovery objective. Tolerance comes from the IBS impact analysis and, for SCI entities, from the SCI BCDR obligations as well.
