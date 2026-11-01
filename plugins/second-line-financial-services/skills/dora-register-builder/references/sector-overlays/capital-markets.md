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

## National-supervisor outsourcing texts (alongside DORA)

DORA does not displace the national-supervisor outsourcing regimes that apply to UCITS management companies and AIFMs. For asset-management entities the register build sits alongside these texts and the practitioner reads both. Where a national text is more prescriptive than DORA on a particular field (sub-outsourcing notification windows, intra-group treatment, governance-body sign-off cadence), the more prescriptive obligation governs.

- **Luxembourg — CSSF Circular 22/806 on outsourcing arrangements** [verify section]. Applies to UCITS management companies, AIFMs, and other CSSF-supervised entities. Carries notification and authorisation expectations on outsourcing of "important operational functions" and on ICT outsourcing, with sub-outsourcing controls and intra-group treatment that read tighter than DORA in places. The circular references the EBA and ESMA outsourcing guidelines as background and applies the CSSF's own implementing detail. Register entries for CSSF-supervised management companies should reference the circular alongside DORA Article 28 [verify article] where the arrangement is dual-scope.
- **Germany — KAGB plus BaFin's MaRisk** [verify exact KAGB section and current MaRisk version]. KAGB §36 governs delegation of investment-management functions for German UCITS / AIFM management companies; MaRisk AT 9 carries the BaFin outsourcing expectations applied across BaFin-supervised entities, with ICT-specific overlays in BAIT and KAIT [verify current naming and version]. The dual-scope read for a German management company runs DORA plus MaRisk AT 9 plus KAIT; the more prescriptive obligation governs per arrangement.
- **France — AMF Position-Recommandation 2018-04 on outsourcing for asset-management companies** [verify section] and the AMF's general-regulation framework for outsourcing under the AMF General Regulation (Règlement général de l'AMF) Book III; the AMF instruction on operational risk for asset-management companies (DOC-2014-13) [verify exact section] also applies. Practitioners frequently note AMF expectations on governance-body sign-off and on intra-group outsourcing as tighter than the DORA general framework.
- **Ireland — Central Bank of Ireland Cross-Industry Guidance on Outsourcing (December 2021)** [verify exact title and any subsequent amendment]. Applies across CBI-supervised entities including UCITS management companies and AIFMs; carries governance, risk-assessment, and inventory expectations that overlap with DORA Article 28 [verify article] but with CBI-specific detail on outsourcing-register format and on the proportionality lens. The CBI's Operational Resilience guidance (December 2021) sits alongside the outsourcing guidance and is read together.

Where the engagement spans multiple national supervisors (a Luxembourg AIFM with a German distribution arm, an Irish UCITS with a French sub-adviser), the register build references each applicable national text per arrangement and flags the more prescriptive obligation in the register's `notes` or equivalent field. Do not collapse the national texts into a single "outsourcing guideline" reference.

## Common pitfalls in capital-markets register builds

- Treating funds as in-scope financial entities. The fund is a vehicle; the management company is the financial entity. Register at the management-company level.
- Recording AIFMD / UCITS regulatory outsourcing of investment management as ICT-third-party arrangements. The regulatory-outsourcing regime is distinct; ICT-third-party records cover the ICT services, not the investment-management function delegation.
- Missing the trading-venue and CSD relationships because they look like infrastructure rather than third parties. They are in scope where they supply ICT services to the financial entity.
- Forgetting that some counterparties are themselves DORA financial entities filing their own registers; the firm's register and the counterparty's register are independent filings.
- Treating DORA as the sole outsourcing reference for UCITS / AIFM entities. The national-supervisor outsourcing texts (CSSF 22/806, BaFin MaRisk and KAGB, AMF Position-Recommandation 2018-04 and DOC-2014-13, CBI Cross-Industry Guidance on Outsourcing) sit alongside DORA and the more prescriptive obligation governs per arrangement.
