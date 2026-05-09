# Capital-markets sector overlay — dora-register-builder

When the scope flags capital markets (investment firms, trading venues, CSDs, CCPs, fund managers, depositaries), load this overlay alongside `references/source-anchors.md`. It carries the capital-markets-specific competent-authority and counterparty considerations the generic skill does not own.

## DORA scope across capital-markets entity types

DORA covers MiFID II investment firms, regulated markets and MTFs and OTFs, CSDs (CSDR), CCPs (EMIR), AIFMs (AIFMD), UCITS management companies, data-reporting service providers, credit-rating agencies, securitisation repositories, trade repositories, administrators of critical benchmarks, and crypto-asset service providers under MiCA [verify exact entity-type list against Article 2 of Regulation (EU) 2022/2554]. The register applies to all in-scope entities; the host-state NCA varies by entity type.

## Competent-authority routing

- **ESMA-coordinated approach**. For most capital-markets entities the technical reporting channel sits with the host-state NCA following the ESMA-coordinated approach. ESMA coordinates and (for some entity types) supervises directly: TRs, SRs, CRAs, and certain critical benchmark administrators sit under ESMA direct supervision and submit accordingly.
- **AIFM and UCITS dual filings**. An AIFM also acting as a UCITS management company holds dual scope under AIFMD and the UCITS Directive. Register the management company as the financial entity; the funds it manages are not separate financial entities for DORA register purposes (the funds are not in DORA scope).

## Counterparties unique to capital markets

- **Depositaries (UCITS Article 22; AIFMD Article 21)**. Depositary services delivered to UCITS funds and AIFs are ICT-supported but the depositary relationship is a regulated function, not a vanilla ICT third party. Where the depositary relies on ICT services to deliver the depositary function, the ICT third-party arrangements behind the depositary are in scope as ICT third-party records of the management company; the depositary itself is a counterparty governed by its own regulatory regime.
- **Trading venues, CSDs, CCPs, market-data vendors**. ICT services consumed by an investment firm from a trading venue, CSD, CCP, or market-data vendor are ICT-third-party arrangements under DORA; record per the schema. Some of these counterparties are themselves DORA financial entities filing their own registers.
- **Administrators, transfer agents, fund accountants**. For asset-management and investment-firm registers, these counterparties are typically ICT-supported services; record the underlying ICT third-party (the administrator or transfer agent providing the platform), not just the administrator's commercial relationship.
- **Sub-advisers and outsourced portfolio management**. These are regulated outsourcing under AIFMD and the UCITS Directive, not (typically) ICT-third-party arrangements. Where the sub-adviser also supplies ICT services to the fund manager, register the ICT services here. The sub-adviser regulatory-outsourcing relationship is a separate regulatory artifact.

## CTPP designation relevance

- DORA Article 31 [verify article number] CTPP oversight framework applies. Hyperscaler arrangements are the predictable CTPP candidates for asset managers and investment firms; market-data vendors at scale (especially the consolidated-tape and data-vendor concentrations that affect price discovery) are also candidates.

## Output-template additions for capital markets

- Host-state NCA channel routing per entity type. ESMA direct submission for the few directly-supervised entity types.
- Depositary, trading-venue, CSD, CCP, and market-data-vendor counterparties each handled at the ICT-services layer (record the ICT services behind the regulated counterparty), not as a single-record commercial relationship.
- AIFMD / UCITS regulatory-outsourcing posture noted in `open_questions` for sub-adviser and portfolio-management arrangements, to confirm they sit outside or alongside DORA register scope.

## Common pitfalls in capital-markets register builds

- Treating funds as in-scope financial entities. The fund is a vehicle; the management company is the financial entity. Register at the management-company level.
- Recording AIFMD / UCITS regulatory outsourcing of investment management as ICT-third-party arrangements. The regulatory-outsourcing regime is distinct; ICT-third-party records cover the ICT services, not the investment-management function delegation.
- Missing the trading-venue and CSD relationships because they look like infrastructure rather than third parties. They are in scope where they supply ICT services to the financial entity.
- Forgetting that some counterparties are themselves DORA financial entities filing their own registers; the firm's register and the counterparty's register are independent filings.
