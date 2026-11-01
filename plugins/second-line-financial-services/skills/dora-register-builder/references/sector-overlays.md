# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — dora-register-builder

When the scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the banking-specific competent-authority and prior-register considerations the generic skill does not own.

#### Competent-authority routing

- **ECB direct-supervised significant institutions**. The ECB acts as the competent authority via the SSM for significant institutions; the register submission flows through the SSM channel under ECB technical reporting instructions [verify exact instruction reference]. National competent authorities still play a role for less-significant institutions and for non-banking subsidiaries within the SSM perimeter.
- **EBA-coordinated approach for less-significant institutions**. Less-significant institutions submit via the national competent authority following the EBA-coordinated approach. The technical channel and validation rules vary by NCA; pin the host-state instruction.
- **Cross-border-group considerations**. EU subsidiaries of a non-EU banking group report individually to their host-state NCA; the parent group's consolidated view is informational, not a substitute for the EU subsidiary's submission.

#### Pre-existing register and the EBA outsourcing register

- **EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02), §11 outsourcing register** [verify section number]. Most EU banks already maintain this register. The natural input to the DORA register is the existing outsourcing register plus the broader ICT-third-party arrangements that fall outside the EBA outsourcing definition. Map and reconcile, do not copy.
- **Mapping note**. The EBA outsourcing register is flatter and narrower than the DORA Register of Information. Critical fields that map cleanly: counterparty identity, contract reference, country of head office, sub-outsourcing flag. Fields that require new collection for DORA: ICT-service-type code (ITS taxonomy), location of data at rest and processing per service, function reference and criticality, sub-contractor visibility at deeper ranks for critical-or-important functions.

#### CTPP designation and the oversight framework

- **DORA Article 31 oversight framework** [verify article number]. Designated Critical ICT Third-Party Service Providers (CTPPs) sit under direct ESA oversight (the ECB, ESMA, and EIOPA acting through the Joint Examination Team mechanism). The register's `b_03.designated_as_critical_by_competent_authority` flag captures the designation where known. Hyperscaler arrangements at significant institutions are the predictable CTPP candidate set.

#### BHC and parent-group interplay

- A US BHC with EU banking subsidiaries: the EU subsidiary files the register; the BHC's own group risk-management framework consumes the register data for its consolidated third-party oversight. The BHC view is not a substitute for the EU subsidiary submission.
- A UK PRA-regulated bank with an EU subsidiary: PRA SS2/21 operational resilience and SS1/21 outsourcing and third-party risk apply at the UK entity; DORA applies at the EU entity. Two registers, two filing channels, one underlying truth in the firm's TPRM data.

#### Output-template additions for banking

- ECB SSM channel and NCA channel routing flagged in the source-data-posture section.
- EBA outsourcing register reconciliation as a standing reconciliation row (almost always required for EU banks).
- CTPP designation status in the `b_03` records for any provider that meets the candidate criteria (size, criticality, concentration), even where designation has not yet occurred.
- Bank-Service-Company-Act-equivalent posture note where the EU subsidiary's parent is a US bank holding company, for the parent's own consolidated TPRM (not for the DORA submission itself).

#### Common pitfalls in banking register builds

- Treating ECB Anacredit, BCBS 239 risk-data-aggregation work, or COREP/FINREP reporting as substitutes for the DORA Register of Information. Each is a separate regulatory artifact with its own schema and channel.
- Submitting the EBA outsourcing register as the DORA register because the data shapes look similar. They do not align column-for-column; the supervisor will reject.
- Missing the consolidation step for a banking group with multiple EU credit-institution subsidiaries that each have their own DORA-scoped activity.

## capital-markets

### Capital-markets sector overlay — dora-register-builder

When the scope flags capital markets (investment firms, trading venues, CSDs, CCPs, fund managers, depositaries), load this overlay alongside `references/source-anchors.md`. It carries the capital-markets-specific competent-authority and counterparty considerations the generic skill does not own.

#### DORA scope across capital-markets entity types

DORA covers MiFID II investment firms, regulated markets and MTFs and OTFs, CSDs (CSDR), CCPs (EMIR), AIFMs (AIFMD), UCITS management companies, data-reporting service providers, credit-rating agencies, securitisation repositories, trade repositories, administrators of critical benchmarks, and crypto-asset service providers under MiCA [verify exact entity-type list against Article 2 of Regulation (EU) 2022/2554]. The register applies to all in-scope entities; the host-state NCA varies by entity type.

#### Competent-authority routing

- **ESMA-coordinated approach**. For most capital-markets entities the technical reporting channel sits with the host-state NCA following the ESMA-coordinated approach. ESMA coordinates and (for some entity types) supervises directly: TRs, SRs, CRAs, and certain critical benchmark administrators sit under ESMA direct supervision and submit accordingly.
- **AIFM and UCITS dual filings**. An AIFM also acting as a UCITS management company holds dual scope under AIFMD and the UCITS Directive. Register the management company as the financial entity; the funds it manages are not separate financial entities for DORA register purposes (the funds are not in DORA scope).

#### Counterparties unique to capital markets

- **Depositaries (UCITS Article 22; AIFMD Article 21)**. Depositary services delivered to UCITS funds and AIFs are ICT-supported but the depositary relationship is a regulated function, not a vanilla ICT third party. Where the depositary relies on ICT services to deliver the depositary function, the ICT third-party arrangements behind the depositary are in scope as ICT third-party records of the management company; the depositary itself is a counterparty governed by its own regulatory regime.
- **Trading venues, CSDs, CCPs, market-data vendors**. ICT services consumed by an investment firm from a trading venue, CSD, CCP, or market-data vendor are ICT-third-party arrangements under DORA; record per the schema. Some of these counterparties are themselves DORA financial entities filing their own registers.
- **Administrators, transfer agents, fund accountants**. For asset-management and investment-firm registers, these counterparties are typically ICT-supported services; record the underlying ICT third-party (the administrator or transfer agent providing the platform), not just the administrator's commercial relationship.
- **Sub-advisers and outsourced portfolio management**. These are regulated outsourcing under AIFMD and the UCITS Directive, not (typically) ICT-third-party arrangements. Where the sub-adviser also supplies ICT services to the fund manager, register the ICT services here. The sub-adviser regulatory-outsourcing relationship is a separate regulatory artifact.

#### CTPP designation relevance

- DORA Article 31 [verify article number] CTPP oversight framework applies. Hyperscaler arrangements are the predictable CTPP candidates for asset managers and investment firms; market-data vendors at scale (especially the consolidated-tape and data-vendor concentrations that affect price discovery) are also candidates.

#### Output-template additions for capital markets

- Host-state NCA channel routing per entity type. ESMA direct submission for the few directly-supervised entity types.
- Depositary, trading-venue, CSD, CCP, and market-data-vendor counterparties each handled at the ICT-services layer (record the ICT services behind the regulated counterparty), not as a single-record commercial relationship.
- AIFMD / UCITS regulatory-outsourcing posture noted in `open_questions` for sub-adviser and portfolio-management arrangements, to confirm they sit outside or alongside DORA register scope.

#### National-supervisor outsourcing texts (alongside DORA)

DORA does not displace the national-supervisor outsourcing regimes that apply to UCITS management companies and AIFMs. For asset-management entities the register build sits alongside these texts and the practitioner reads both. Where a national text is more prescriptive than DORA on a particular field (sub-outsourcing notification windows, intra-group treatment, governance-body sign-off cadence), the more prescriptive obligation governs.

- **Luxembourg — CSSF Circular 22/806 on outsourcing arrangements** [verify section]. Applies to UCITS management companies, AIFMs, and other CSSF-supervised entities. Carries notification and authorisation expectations on outsourcing of "important operational functions" and on ICT outsourcing, with sub-outsourcing controls and intra-group treatment that read tighter than DORA in places. The circular references the EBA and ESMA outsourcing guidelines as background and applies the CSSF's own implementing detail. Register entries for CSSF-supervised management companies should reference the circular alongside DORA Article 28 [verify article] where the arrangement is dual-scope.
- **Germany — KAGB plus BaFin's MaRisk** [verify exact KAGB section and current MaRisk version]. KAGB §36 governs delegation of investment-management functions for German UCITS / AIFM management companies; MaRisk AT 9 carries the BaFin outsourcing expectations applied across BaFin-supervised entities, with ICT-specific overlays in BAIT and KAIT [verify current naming and version]. The dual-scope read for a German management company runs DORA plus MaRisk AT 9 plus KAIT; the more prescriptive obligation governs per arrangement.
- **France — AMF Position-Recommandation 2018-04 on outsourcing for asset-management companies** [verify section] and the AMF's general-regulation framework for outsourcing under the AMF General Regulation (Règlement général de l'AMF) Book III; the AMF instruction on operational risk for asset-management companies (DOC-2014-13) [verify exact section] also applies. Practitioners frequently note AMF expectations on governance-body sign-off and on intra-group outsourcing as tighter than the DORA general framework.
- **Ireland — Central Bank of Ireland Cross-Industry Guidance on Outsourcing (December 2021)** [verify exact title and any subsequent amendment]. Applies across CBI-supervised entities including UCITS management companies and AIFMs; carries governance, risk-assessment, and inventory expectations that overlap with DORA Article 28 [verify article] but with CBI-specific detail on outsourcing-register format and on the proportionality lens. The CBI's Operational Resilience guidance (December 2021) sits alongside the outsourcing guidance and is read together.

Where the engagement spans multiple national supervisors (a Luxembourg AIFM with a German distribution arm, an Irish UCITS with a French sub-adviser), the register build references each applicable national text per arrangement and flags the more prescriptive obligation in the register's `notes` or equivalent field. Do not collapse the national texts into a single "outsourcing guideline" reference.

#### Common pitfalls in capital-markets register builds

- Treating funds as in-scope financial entities. The fund is a vehicle; the management company is the financial entity. Register at the management-company level.
- Recording AIFMD / UCITS regulatory outsourcing of investment management as ICT-third-party arrangements. The regulatory-outsourcing regime is distinct; ICT-third-party records cover the ICT services, not the investment-management function delegation.
- Missing the trading-venue and CSD relationships because they look like infrastructure rather than third parties. They are in scope where they supply ICT services to the financial entity.
- Forgetting that some counterparties are themselves DORA financial entities filing their own registers; the firm's register and the counterparty's register are independent filings.
- Treating DORA as the sole outsourcing reference for UCITS / AIFM entities. The national-supervisor outsourcing texts (CSSF 22/806, BaFin MaRisk and KAGB, AMF Position-Recommandation 2018-04 and DOC-2014-13, CBI Cross-Industry Guidance on Outsourcing) sit alongside DORA and the more prescriptive obligation governs per arrangement.

## insurance

### Insurance sector overlay — dora-register-builder

When the scope flags insurance, load this overlay alongside `references/source-anchors.md`. It carries the insurance-specific competent-authority and prior-register considerations the generic skill does not own.

#### Competent-authority routing

- **EIOPA-coordinated approach**. For insurance and reinsurance undertakings, intermediaries (where in DORA scope), institutions for occupational retirement provision (IORPs, where in scope), and Solvency II groups, the technical reporting channel sits with the host-state NCA following the EIOPA-coordinated approach. EIOPA is not a direct-supervisor for filings; it coordinates.
- **Solvency II group register interplay**. A Solvency II insurance group with multiple EU undertakings: each in-scope undertaking files at its host-state NCA; the group's consolidated view is informational. The group supervisor coordinates but does not substitute for the per-undertaking submission.

#### Pre-existing register inputs

- **EIOPA Guidelines on outsourcing to cloud service providers (EIOPA-BoS-20-002)** [verify exact reference and section]. Many EU insurers maintain an outsourcing register under the EIOPA cloud guidelines and their national-supervisor outsourcing notification regime. The DORA register subsumes this and broadens scope to all ICT-third-party arrangements; map and reconcile, do not copy.
- **Solvency II Article 49 outsourcing notification** [verify article structure]. Outsourcing of critical or important functions under Solvency II requires NCA notification; the underlying data (function reference, criticality, counterparty identity) is the input to the DORA register's `b_04` and `b_03` records.

#### US-parent considerations (the cross-border dimension)

- **NAIC Insurance Holding Company System Regulatory Act (Model #440) [verify model number]**. Form B and Form F at the US parent of a US-headquartered insurance group with EU underwriting subsidiaries: the EU subsidiary's DORA register data may flow into Form B (intercompany services) and Form F (enterprise risk report) at the US parent. Two regulators, two artifacts; the underlying truth is the firm's TPRM data.
- **NAIC Insurance Data Security Model Law (Model #668), §4.F** third-party service-provider obligations. Where the US parent has a §668-state subsidiary, the third-party service-provider obligations carry US-side reporting expectations distinct from the EU DORA register.
- **Group ORSA**. Critical outsourced functions identified in the DORA register's `b_04` entries map into the group ORSA Summary Report at the US parent. Pointer to the firm's `risk-committee-pack` and ORSA materials.

#### CTPP designation in insurance

- DORA Article 31 oversight framework [verify article number] applies to ICT third parties supplying insurers as well as banks. The designation criteria include criticality and concentration. EIOPA participates in the Joint Examination Team for insurance-relevant CTPPs.

#### Output-template additions for insurance

- Host-state NCA channel routing in the source-data-posture section. Multiple host-state NCAs may apply if the group has subsidiaries across EU jurisdictions.
- Solvency II outsourcing-notification reconciliation as a standing reconciliation row where applicable.
- US parent's Form B / Form F flow noted in `open_questions` for a US-headquartered group, for the parent's own consolidated outsourcing reporting (not for the DORA submission itself).

#### Common pitfalls in insurance register builds

- Treating the Solvency II Article 49 notification as the DORA register. Different schema, different scope (DORA covers all ICT third parties, not just outsourcing of critical or important functions), different submission channel.
- Missing the IORP scope question for occupational pension arrangements managed by the insurer.
- Confusing the EIOPA cloud guidelines outsourcing register with the DORA Register of Information; the cloud guidelines are narrower (cloud-only) and pre-DORA in vintage.
- Forgetting the US parent's Form B / Form F dimension where the EU subsidiary's outsourcing data flows back into US-side filings.

## payments-fintech

### Payments-fintech sector overlay — dora-register-builder

When the scope flags payments or fintech (payment institutions, e-money institutions, account information service providers, crypto-asset service providers under MiCA), load this overlay alongside `references/source-anchors.md`. It carries the payments-fintech-specific scope and counterparty considerations the generic skill does not own.

#### DORA scope across payments-fintech entity types

DORA covers payment institutions (PSD2), e-money institutions (EMD2), account information service providers (PSD2 AIS), and crypto-asset service providers under MiCA, alongside the broader financial-entity list [verify exact entity-type list against Article 2 of Regulation (EU) 2022/2554]. Smaller payment institutions and e-money institutions still fall in scope where they meet the entity-type definition; the proportionality principle in DORA Article 4 [verify article number] modulates how the requirements apply, not whether they apply.

#### Competent-authority routing

- **EBA-coordinated approach for payment institutions and e-money institutions**. Submission flows through the host-state NCA following the EBA-coordinated approach. The EU passporting regime under PSD2 means a payment institution authorised in one EU member state operates in others; the register sits with the home-state NCA, with passporting reflected in the in-scope-entities scope.
- **MiCA crypto-asset service providers**. Submission via the host-state NCA following the relevant ESA-coordinated approach. MiCA Article 67 [verify article number] sets governance expectations for CASPs that interact with the DORA ICT-risk requirements.

#### Counterparties common in payments-fintech

- **Card-network counterparties (Visa, Mastercard, national schemes)**. Network connectivity, authorisation, clearing, and settlement services are ICT services from the card scheme; record per the schema. The scheme rules themselves are not register entries; the ICT services delivered under the scheme membership are.
- **Acquiring and issuing processors**. Where the firm uses a separate processor for acquiring or issuing, the processor's ICT services are register entries.
- **Open-banking infrastructure (PSD2 AIS / PIS)**. Aggregator infrastructure supplying account-information access or payment-initiation rails are ICT services; register the underlying ICT-services provider.
- **BIN sponsors and licensing partners**. Where a fintech operates under a BIN sponsor or partner-licence arrangement, the sponsor's ICT services may sit in scope; this overlaps with the regulatory relationship and is worth flagging in `open_questions` for legal review on whether the sponsor relationship is an ICT-third-party arrangement, a regulatory outsourcing, or both.
- **MiCA-relevant counterparties**. Custody-of-crypto-assets providers, blockchain-infrastructure providers, on-chain analytics vendors, and KYC/CIP vendors specialised in crypto. All are register candidates.

#### US-parent considerations (where relevant)

- A US-headquartered fintech operating EU subsidiaries under PSD2 / EMD2 / MiCA: the EU subsidiary files the DORA register; the US parent's TPRM register, BSA program, and OFAC sanctions program operate alongside and consume the data but are not the DORA filer.

#### CTPP designation in payments

- DORA Article 31 CTPP designation [verify article number]. Card networks, acquiring and issuing processor concentration, and hyperscaler concentration are the predictable CTPP candidate set in payments. The register's `b_03.designated_as_critical_by_competent_authority` flag captures the designation where known.

#### Output-template additions for payments-fintech

- Card-scheme, processor, open-banking aggregator, and (where MiCA-applicable) crypto-infrastructure counterparties recorded explicitly with their ICT services in `b_05`.
- BIN-sponsor and licence-partner relationships flagged in `open_questions` for the regulatory-outsourcing-versus-ICT-third-party scope question.
- PSD2 passporting reflected in the in-scope-entities scope where the firm operates across multiple member states under a single home-state authorisation.

#### Common pitfalls in payments-fintech register builds

- Treating the card-scheme membership as a single commercial relationship rather than a set of ICT services (authorisation, clearing, settlement, dispute) each supplied to the firm.
- Missing the BIN-sponsor or licence-partner ICT services because the relationship looks regulatory; the regulatory dimension and the ICT-third-party dimension can both apply.
- Treating proportionality (DORA Article 4) as a scope reducer for payment institutions; it modulates how the requirements apply, not whether the firm files.
- Forgetting the MiCA-applicable crypto counterparties when the firm is a payment institution that also offers crypto-asset services in EU jurisdictions where MiCA applies.
