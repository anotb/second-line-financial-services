# Payments-fintech sector overlay — dora-register-builder

When the scope flags payments or fintech (payment institutions, e-money institutions, account information service providers, crypto-asset service providers under MiCA), load this overlay alongside `references/source-anchors.md`. It carries the payments-fintech-specific scope and counterparty considerations the generic skill does not own.

## DORA scope across payments-fintech entity types

DORA covers payment institutions (PSD2), e-money institutions (EMD2), account information service providers (PSD2 AIS), and crypto-asset service providers under MiCA, alongside the broader financial-entity list [verify exact entity-type list against Article 2 of Regulation (EU) 2022/2554]. Smaller payment institutions and e-money institutions still fall in scope where they meet the entity-type definition; the proportionality principle in DORA Article 4 [verify article number] modulates how the requirements apply, not whether they apply.

## Competent-authority routing

- **EBA-coordinated approach for payment institutions and e-money institutions**. Submission flows through the host-state NCA following the EBA-coordinated approach. The EU passporting regime under PSD2 means a payment institution authorised in one EU member state operates in others; the register sits with the home-state NCA, with passporting reflected in the in-scope-entities scope.
- **MiCA crypto-asset service providers**. Submission via the host-state NCA following the relevant ESA-coordinated approach. MiCA Article 67 [verify article number] sets governance expectations for CASPs that interact with the DORA ICT-risk requirements.

## Counterparties common in payments-fintech

- **Card-network counterparties (Visa, Mastercard, national schemes)**. Network connectivity, authorisation, clearing, and settlement services are ICT services from the card scheme; record per the schema. The scheme rules themselves are not register entries; the ICT services delivered under the scheme membership are.
- **Acquiring and issuing processors**. Where the firm uses a separate processor for acquiring or issuing, the processor's ICT services are register entries.
- **Open-banking infrastructure (PSD2 AIS / PIS)**. Aggregator infrastructure supplying account-information access or payment-initiation rails are ICT services; register the underlying ICT-services provider.
- **BIN sponsors and licensing partners**. Where a fintech operates under a BIN sponsor or partner-licence arrangement, the sponsor's ICT services may sit in scope; this overlaps with the regulatory relationship and is worth flagging in `open_questions` for legal review on whether the sponsor relationship is an ICT-third-party arrangement, a regulatory outsourcing, or both.
- **MiCA-relevant counterparties**. Custody-of-crypto-assets providers, blockchain-infrastructure providers, on-chain analytics vendors, and KYC/CIP vendors specialised in crypto. All are register candidates.

## US-parent considerations (where relevant)

- A US-headquartered fintech operating EU subsidiaries under PSD2 / EMD2 / MiCA: the EU subsidiary files the DORA register; the US parent's TPRM register, BSA program, and OFAC sanctions program operate alongside and consume the data but are not the DORA filer.

## CTPP designation in payments

- DORA Article 31 CTPP designation [verify article number]. Card networks, acquiring and issuing processor concentration, and hyperscaler concentration are the predictable CTPP candidate set in payments. The register's `b_03.designated_as_critical_by_competent_authority` flag captures the designation where known.

## Output-template additions for payments-fintech

- Card-scheme, processor, open-banking aggregator, and (where MiCA-applicable) crypto-infrastructure counterparties recorded explicitly with their ICT services in `b_05`.
- BIN-sponsor and licence-partner relationships flagged in `open_questions` for the regulatory-outsourcing-versus-ICT-third-party scope question.
- PSD2 passporting reflected in the in-scope-entities scope where the firm operates across multiple member states under a single home-state authorisation.

## Common pitfalls in payments-fintech register builds

- Treating the card-scheme membership as a single commercial relationship rather than a set of ICT services (authorisation, clearing, settlement, dispute) each supplied to the firm.
- Missing the BIN-sponsor or licence-partner ICT services because the relationship looks regulatory; the regulatory dimension and the ICT-third-party dimension can both apply.
- Treating proportionality (DORA Article 4) as a scope reducer for payment institutions; it modulates how the requirements apply, not whether the firm files.
- Forgetting the MiCA-applicable crypto counterparties when the firm is a payment institution that also offers crypto-asset services in EU jurisdictions where MiCA applies.
