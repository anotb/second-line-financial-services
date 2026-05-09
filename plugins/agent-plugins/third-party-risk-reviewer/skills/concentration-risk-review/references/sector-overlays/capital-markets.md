# Capital-markets sector overlay — concentration-risk-review

When the scope flags capital markets, load this overlay alongside `references/source-anchors.md`. It carries the capital-markets-specific concentration framings the generic skill does not own.

## Reg SCI concentration on critical SCI systems

- **Reg SCI (17 CFR §242.1000-1007)** [verify rule subpart]. SCI entities (national securities exchanges, registered clearing agencies, certain ATSs, plan processors, exempt clearing agencies) must assess third-party concentration as part of the SCI policies-and-procedures framework. The dimension reads as `single-vendor` and `function-level` with the SCI-system criticality cutoff. Substitutability read names that SCI-system substitution is heavily regulated and rarely fast.

## Market-data and exchange-feed concentration

- A capital-markets firm may take consolidated tape, exchange feeds, and reference-data from a small set of vendors. Concentration on one consolidated-tape provider, one reference-data vendor for instrument identifiers, and one corporate-actions vendor is the standard pattern. The dimension reads as `technology-stack-shared-utility`; the substitutability read names that market-data vendor migration is contractually possible but operationally invasive (every downstream consumer must re-test).

## Central-counterparty and clearing-member concentration

- For firms that clear through central counterparties, concentration on a small set of CCPs and a small set of clearing members is a recognised structural feature. The operational-third-party dimension this skill covers is the technology and connectivity-vendor concentration that supports access to those CCPs and clearing members, not the CCP-credit concentration itself (which sits with treasury and credit-risk teams).

## Post-trade-processor and transfer-agent concentration

- A small set of post-trade processors and transfer agents covers most of the US capital-markets infrastructure. A firm whose recordkeeping, corporate-actions processing, and dividend-disbursement flows all sit on one transfer agent is concentration; the substitutability read names that transfer-agent migration is multi-year and disruptive to investor experience.

## Adviser and fund compliance-program dimension

- **Investment Advisers Act Rule 206(4)-7**. The adviser must adopt and implement compliance policies reasonably designed to prevent violation of the federal securities laws; service-provider concentration is part of that adequacy assessment.
- **Investment Company Act Rule 38a-1(a)(4)**. Fund CCO must oversee the compliance program of each service provider to the fund. Where one service provider supports multiple funds in the complex, concentration reads as a fund-board-level item; recommended actions cluster for the fund board.
- **Investment Advisers Act Rule 206(4)-2 (Custody Rule)**. Where the firm uses one qualified custodian across multiple advisory products, concentration reads against the adviser's surprise-examination and account-statement-delivery obligations [verify section]. Custody-vendor migration is contractually possible but operationally heavy.

## Reg S-P and the cyber lens

- **17 CFR Part 248 (Reg S-P) as amended May 16, 2024** [verify exact compliance dates by entity type and size]. Concentration in customer-information-safeguarding vendors (encryption, key-management, identity-and-access-management) reads in the cross-cutting cyber overlay.

## Output-template additions for capital markets

- SCI-systems-row in the function-level dimension where the firm is an SCI entity.
- Market-data-vendor row in technology-stack-shared-utility.
- Transfer-agent and post-trade-processor row in single-vendor.
- Fund-board reviewer-question cluster where the engagement supports a fund complex.

## Common pitfalls in capital-markets concentration reviews

- Conflating CCP-credit concentration with the operational-vendor concentration that supports CCP access. Two different reviews.
- Treating market-data-vendor concentration as a procurement question. It is an operational-resilience question because the downstream consumers are bound to the vendor's instrument-identifier and pricing conventions.
- Missing the fund-board-level reviewer cluster in fund-complex engagements. The fund board is a separate forum from the adviser's risk committee.
- Reading the SCI dimension narrowly as the named SCI systems without the third-party-vendor concentration that supports those systems.
