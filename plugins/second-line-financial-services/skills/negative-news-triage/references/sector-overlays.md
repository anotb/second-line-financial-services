# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — negative-news-triage

When the scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the bank-specific adverse-media frame the generic capability skill does not own.

#### What banking adverse-media looks like in practice

Banking customer adverse media skews to four recurring shapes. The triage reads against the shape the hit fits, not against a generic "negative news" template.

- **Regulatory-enforcement coverage of a commercial customer.** A federal agency (CFPB, OCC, FRB, FDIC, FTC, SEC) or a state regulator publishes a press release or a consent order naming the customer or the customer's principals. Tier-1 source class by definition; identity confidence usually high (the press release names the entity); materiality depends on the typology framing of the underlying conduct (a bank customer hit with a CFPB UDAAP order is reputational and conduct-relevant but may not be financial-crime-typology-relevant).
- **Indictments and civil filings naming the customer's principals.** Federal-court or state-court filings naming a director, officer, or beneficial owner of a customer entity. Identity confidence requires the entity-to-principal linkage from the CDD file or the public ownership chain; common-name false matches on the principal are routine. Materiality depends on the alleged conduct's typology link (a fraud indictment routes differently from a non-financial-crime civil matter).
- **Cash-intensive-business adverse media.** Local and regional press coverage of a customer's storefront business naming structuring, money-laundering, or tax-evasion patterns. Source-class often tier-2 or tier-3; the triage reads back to a primary source (regulator action, court filing, indictment) before treating the hit as material.
- **Correspondent-banking and foreign-counterparty adverse media.** Foreign-press, regulator, or court coverage of a foreign FI the bank holds a correspondent relationship with, or a foreign counterparty to a customer's transactions. The foreign-language and foreign-jurisdiction read raises identity-confidence-bar and source-corroboration-bar; a single foreign-press tier-3 hit on a correspondent should not move materiality on its own.

#### Bank-specific identity-confidence drivers

The CDD file's matchable attributes do most of the identity-cut work. For banking:

- **Legal-entity customers** match on legal name, formation date, EIN where present, registered agent or registered address, principal place of business, and beneficial-ownership chain.
- **Individuals** match on legal name, date of birth, address (residence and any prior address on file), occupation, employer where on file, and known counterparties.
- **Common-name false-match patterns**: the dominant noise category in bulk re-scan output. The triage names common-name patterns explicitly in the `aggregated_themes` rather than dispositioning each hit individually when the false-match basis is the same.
- **Principal-versus-entity drift**: a hit where the customer entity is not named but a principal is named. The triage scopes the principal's role (control-prong individual under `§1010.230`; ownership-prong individual; signatory; non-named-on-file affiliate) before reading materiality at the entity level.

#### Typology-link patterns banking adverse-media triage attends to

- **Fraud (commercial loan fraud, deposit fraud, mortgage fraud, ACH and wire fraud, BEC).** Cite to FinCEN advisories on the relevant typology and to applicable enforcement actions in the source trace.
- **Structuring.** Cash-intensive customer adverse media frequently links to structuring patterns; tier-1 corroboration (regulator action, court filing) is the materiality threshold.
- **Trade-based money laundering (TBML).** Commercial customers with international counterparties; cite to FinCEN TBML advisory in the typology tag.
- **Sanctions evasion.** A correspondent-banking adverse-media hit implicating a foreign FI in sanctions evasion routes to `sanctions-screening-qa` for the screening overlap, not just to the CDD or EDD lane.
- **Public-corruption and PEP-adjacency.** A hit surfacing a customer's principal in a foreign-corruption matter routes to `edd-escalation-pack` against the FFIEC PEP and private-banking EDD frames.

#### Bank routing patterns

- A tier-1 hit with direct involvement on a financial-crime typology routes to `cdd-risk-review` for an event-driven refresh and to `edd-escalation-pack` if the customer is not already in EDD; an in-flight alert against the same customer also pulls a routing line to `sar-decision-qa`.
- A tier-1 hit with mention-only linkage routes as evidence input to a CDD refresh on cycle, not as an event-driven escalation.
- A tier-2 or tier-3 hit pending corroboration carries `[evidence needed]` and an open-question for the relationship owner to corroborate against the primary source; the triage does not escalate on uncorroborated tier-3 content.
- A bulk re-scan output dominated by tier-3 and common-name false matches surfaces a source-posture finding (the vendor or the query is producing high noise) that routes to the BSA program rather than to per-customer escalation.

#### Common pitfalls in banking adverse-media triage

- Treating tier-2 or tier-3 hits as material without primary-source corroboration.
- Collapsing identity confidence into "name matches"; the matchable-attribute discipline is what distinguishes a real hit from a common-name false match.
- Dispositioning each common-name false match individually instead of naming the pattern in `aggregated_themes`.
- Letting vendor self-tagging of source reliability stand in for the source-class read.
- Treating a CFPB UDAAP order on a commercial customer as a financial-crime-typology hit when the underlying conduct is conduct-risk only; the conduct overlay (when loaded) carries the parallel routing.
- Recommending the rating change, the EDD upgrade, the SAR filing, or the exit; the triage routes the artifact to the named decisionmaker, who decides.

## capital-markets

### Capital markets sector overlay — negative-news-triage

When the scope flags capital markets, load this overlay alongside `references/source-anchors.md`. It carries the broker-dealer, mutual-fund, and investment-adviser-specific adverse-media frame the generic capability skill does not own.

#### What capital-markets adverse-media looks like in practice

Capital-markets customer adverse media skews to securities-enforcement and securities-litigation surfaces. Tier-1 source classes (SEC press releases and litigation releases, FINRA disciplinary actions, CFTC press releases, federal court filings, state-securities-administrator actions) are densely populated and well-indexed; the identity-cut work is usually easier than in banking, but the typology-link work is harder because securities adverse media frequently does not map cleanly to BSA-AML typologies.

- **Insider-trading allegations and enforcement.** SEC enforcement actions, criminal indictments, and civil filings naming a customer or a customer's principals. Identity confidence usually high (filings name the actor with corroborable attributes); typology link to AML is borderline (insider trading is not itself a BSA predicate offense in every framing, but the proceeds-of-insider-trading typology is).
- **Market-manipulation enforcement.** Pump-and-dump, spoofing, layering (trading-tactic, distinct from BSA layering), wash-trading enforcement. SEC and CFTC actions, FINRA arbitration awards, federal-court filings. The typology link to AML rests on the proceeds-of-manipulation read.
- **Microcap-promoter and stock-promotion exposure.** Adverse media on a customer who is a microcap-promoter, an issuer's affiliate, or a deposit-of-low-priced-securities customer. The FINRA Reg-Notice frame on low-priced securities and the FFIEC manual's broker-dealer-specific risk drivers are the read.
- **Expert-network and investment-research exposure.** Adverse media on a customer who participates in expert-network relationships that surface in insider-trading enforcement contexts. Identity confidence often requires the customer-file employment-history-and-affiliation join.
- **Investment-adviser fiduciary-duty and disclosure-failure enforcement.** SEC EXAMS risk-alert priorities and SEC enforcement actions against advisers. Adverse media on adviser customers (where the broker-dealer custodian holds the adviser's omnibus or where the fund has the adviser as service provider) carries program-level read.

#### Capital-markets-specific identity-confidence drivers

The CDD file's matchable attributes for capital-markets customers:

- **Broker-dealer customers (retail accounts)** match on legal name, date of birth, address, employment, occupation, professional licensing where collected, and known related-account holders.
- **Broker-dealer customers (institutional accounts)** match on legal name, formation, registered address, primary-place-of-business, beneficial-ownership chain, and service-provider relationships.
- **Mutual-fund and ETF customers (omnibus and intermediated)** are matched at the intermediary level; direct-shareholder identity-cut is bounded by the omnibus arrangement and the intermediary's CIP/CDD program.
- **Investment-adviser customers** match on adviser name, IARD/CRD number, registered address, key personnel, and affiliated entities. The IARD/CRD number is a high-confidence identity attribute that materially raises the identity cut.

#### Typology-link patterns capital-markets adverse-media triage attends to

- **Proceeds of insider trading and market manipulation.** A securities-enforcement hit is read for the proceeds typology (the customer's funds in the account include or imply proceeds of the alleged conduct). Cite to FFIEC SAR-section indicators on securities typologies and to the operative SAR rule for the institution.
- **Microcap and low-priced-security typologies.** Pump-and-dump, market-making schemes, deposit-of-low-priced-securities patterns. The FFIEC broker-dealer overlay and FINRA notices are the read.
- **Cross-border securities and foreign-issuer exposure.** Adverse media on a foreign issuer the customer holds, or on a customer with cross-border securities counterparties, layered with sanctions-screening and OFAC reads.
- **Layering through securities products.** Multi-jurisdictional, multi-account patterns where securities products are used to layer proceeds. The typology link is to BSA-layering, distinct from trading-tactic layering.
- **Adviser-side conduct and fiduciary-duty failures.** A SEC enforcement hit on an adviser customer carries a conduct-overlap (misappropriation, churning, undisclosed conflicts) that is conduct-relevant; the AML typology link runs through proceeds-of-the-conduct.

#### Capital-markets routing patterns

- A SEC or FINRA enforcement hit naming the customer routes to `cdd-risk-review` for an event-driven refresh and to `edd-escalation-pack` where the conduct implicates a heightened-risk-population read; in-flight or recent alerts on the same customer pull a routing line to `sar-decision-qa`.
- An indictment naming a customer's principals (insider-trading or market-manipulation) routes to `edd-escalation-pack` and to `sar-decision-qa`; the proceeds-typology read is what carries the SAR-decision evidence.
- A microcap-promoter or low-priced-security exposure routes to `cdd-risk-review` for the broker-dealer-overlay-specific reads and to `aml-model-monitoring` (cross-reference) where the customer's transaction-monitoring scenario set on file does not cover the low-priced-security typology.
- A foreign-issuer or cross-border counterparty hit with sanctions-evasion overlap routes to `sanctions-screening-qa`.

#### Common pitfalls in capital-markets adverse-media triage

- Treating insider-trading enforcement as not-AML-relevant. The proceeds-typology read is the link; do not collapse "insider trading is not a SAR typology" into a no-typology disposition.
- Letting tier-1 source class on a securities-enforcement hit substitute for identity-confidence work; common-name false matches on individual-customer hits still occur.
- Reading mutual-fund and ETF intermediated holdings as direct-shareholder hits; the omnibus arrangement is what scopes the identity cut.
- Under-reading microcap-promoter exposure; the FINRA notices and FFIEC broker-dealer overlay are not optional.
- Letting the SEC enforcement frame substitute for a typology tag when the underlying conduct is conduct-relevant only (a fiduciary-duty failure with no proceeds-typology link is conduct-overlay material, not AML-typology material).
- Recommending the rating change, the EDD upgrade, the SAR filing, the deposit-of-low-priced-securities restriction, or the exit; the triage routes the artifact to the named decisionmaker.

## insurance

### Insurance sector overlay — negative-news-triage

When the scope flags insurance, load this overlay alongside `references/source-anchors.md`. Scope is narrow: the BSA AML rule for insurers covers a defined set of investment-type products; adverse-media triage on insurers tracks that scope.

#### Scope reminder — covered products only

The FinCEN AML rule for insurance companies (31 CFR Part 1025) applies to insurers offering covered products: permanent life-insurance policies (other than group life-insurance policies), annuity contracts (other than group annuity contracts), and any other insurance product with cash value or investment features. Property and casualty (P&C), term life without cash value, group life and group annuity, and health insurance are generally outside the BSA AML rule's scope, though state-level insurance-fraud regimes and producer-conduct frames still apply.

Adverse-media triage on insurance customers is in scope when the customer holds (or is being onboarded for) a covered product. Adverse media on a P&C-only relationship is not generally a BSA AML triage; it may be a fraud-program triage or a conduct-overlay triage but does not feed `cdd-risk-review` or `sar-decision-qa` against the BSA frame.

#### What insurance covered-product adverse-media looks like in practice

- **Insurance-fraud-ring patterns naming the policyholder or a beneficiary.** State-regulator press releases, state-insurance-department enforcement, federal-court filings, and regional press coverage of insurance-fraud rings (faked deaths, structured-settlement fraud, premium-financing schemes). Tier-1 source class for regulator and court material; tier-2 for trade press; tier-3 for unverified content.
- **Premium-financing irregularities.** Adverse media on premium-financing arrangements that intersect with the customer's covered-product holdings (stranger-originated life insurance / STOLI patterns, unauthorised collateral assignments, premium-financing-vehicle insolvencies that link back to the customer).
- **Structured-settlement secondary-market adverse media.** Where a structured-settlement annuity has been sold or factored, adverse media on the secondary-market transaction or counterparty bears on the BSA frame (the funding-source typology).
- **Producer-conduct findings** that surface the customer in a sales-practice or churning context. The conduct overlay carries the producer-side discipline; the AML triage reads the customer-side typology link if any (proceeds, structuring through cash-value loans, surrender patterns).

#### Insurance-specific identity-confidence drivers

- **Individual policyholders** match on legal name, date of birth, address, and (where the insurer collects them) employer, occupation, and beneficiary information. The CIP rule for insurance (`§1025.220`) limits identifying-information collection to covered products; the matchable-attribute set is leaner than at a bank.
- **Legal-entity policyholders** (rare in covered-product context but present in business-owned life insurance, key-person and split-dollar arrangements) match on legal name, formation, registered address, and beneficial-ownership chain under `§1010.230`.
- **Beneficiaries** are not policyholders and are not customers under the BSA frame; an adverse-media hit naming a beneficiary may bear on the policy-funding-source or claim-typology read but does not flow through the customer-CDD lane the same way.
- **Structured-settlement annuitants** carry an identity-cut bound by the originating-court order and the funding-corporation's records; the matchable-attribute set is bounded.

#### Typology-link patterns insurance covered-product adverse-media triage attends to

- **Premium-payment-source typologies.** Cash or non-traditional-funding-source premium payments; cite to the FFIEC manual's insurance-section indicators (where they exist) and to FinCEN advisories on insurance typologies in the typology tag.
- **Cash-value loan and surrender typologies.** Patterns of cash-value-loan-then-surrender, or rapid surrender after a cash-value buildup, that imply a layering or structuring read.
- **STOLI and stranger-originated life-insurance typologies.** Adverse media on STOLI rings or premium-financing-vehicle insolvencies that link to the customer's covered-product holdings.
- **Structured-settlement-factoring typologies.** Adverse media on factoring counterparties or secondary-market arrangements that link to a customer's annuity.
- **Insurance-fraud predicate offences** (faked deaths, faked disabilities, faked claims) that surface the customer or beneficiary; cite to the relevant state-insurance-department action or federal indictment in the source trace.

#### Insurance routing patterns

- A tier-1 hit on a covered-product policyholder naming a financial-crime typology routes to `cdd-risk-review` for an event-driven refresh and to `edd-escalation-pack` if the customer carries a heightened-risk profile (PEP, foreign-correspondent, complex-structure entity).
- A premium-financing or STOLI-pattern hit routes to `cdd-risk-review` and may pull a `sar-decision-qa` routing line where an in-flight alert exists.
- A producer-conduct hit (sales-practice exposure, churning) without a financial-crime typology link routes through the conduct overlay (when loaded) to the consumer-compliance and producer-oversight functions, not through the AML triage lane.
- An adverse-media hit on a P&C-only customer surface area is generally out of scope for this triage; the scope and the institution's program may route it to a fraud-program lane separately.

#### Common pitfalls in insurance adverse-media triage

- Reading P&C-only relationships against the covered-product BSA frame; the rule's scope is the gate.
- Treating beneficiary-only hits as customer-CDD-lane hits; the BSA customer is the policyholder.
- Letting producer-conduct adverse media collapse into the AML triage when the underlying conduct is conduct-relevant only.
- Under-reading premium-financing and STOLI patterns; the typology link is real and the FFIEC and state-regulator references are not optional.
- Letting state-insurance-department enforcement substitute for a typology tag when the underlying conduct is regulatory only without a proceeds or layering link.
- Recommending the rating change, the EDD upgrade, the SAR filing, the policy lapse, the surrender, or the exit; the triage routes the artifact to the named decisionmaker.

## payments-fintech

### Payments / fintech sector overlay — negative-news-triage

When the scope flags payments-fintech, load this overlay alongside `references/source-anchors.md`. It carries the fintech-specific adverse-media frame the generic capability skill does not own.

#### What payments-fintech adverse-media looks like in practice

Fintech customer adverse media skews differently from banking. Volumes are higher, identity attributes are thinner (digital-only onboarding leaves less corroborable file evidence), and the customer base often includes smaller commercial sellers, marketplace participants, and gig-economy individuals whose adverse-media surface area is wider but whose materiality is harder to read.

- **Marketplace-seller fraud reporting.** Press, regulator, and consumer-complaint coverage of a marketplace seller (a customer of a payments processor or a marketplace platform under sponsor-bank arrangements). Consumer-complaint volume is itself a signal but is not a typology link by itself; the triage reads back to a primary source (regulator action, court filing, indictment, named class-action filing) before treating the hit as material.
- **Payment-processor and BIN-sponsor enforcement coverage.** Federal-agency actions against a customer that is itself a payment intermediary (a payment facilitator, a money services business, a small acquirer) raises a heightened-risk profile that flows through the sponsor-bank program. Tier-1 source class; identity confidence usually high.
- **Convertible-virtual-currency exchange and DeFi exposure.** Adverse media on a customer's CVC counterparty (an exchange, a mixer, a bridge protocol) implicating sanctions evasion, ransomware facilitation, or a named darknet-market linkage. The cyber-typology and sanctions-evasion-typology overlap is heavy in this segment.
- **Sponsor-bank-program adverse media.** Where the fintech operates under a sponsor-bank model, adverse media against the fintech itself (regulator actions, consumer-complaint patterns, BSA-AML-program enforcement) routes through the sponsor's program and is read against the program contract's CDD reliance arrangement.

#### Fintech-specific identity-confidence drivers

Digital-only onboarding leaves thinner identity attributes than banking does. The triage works with what the file holds:

- **Marketplace and small-commercial sellers** match on legal name, formation date or DBA, EIN where collected, registered address, principal place of business where collected, and the business-activity description on file. Common-name false matches dominate; the business-activity-and-jurisdiction join is often the only differentiator.
- **Gig-economy and individual customers** match on legal name, date of birth, address, and device-and-contact attributes (where the program collects them). A high-confidence individual-customer identity cut frequently requires combining a CDD-file attribute with a public-record join (court records, regulator press releases, professional licensing) that the file does not carry directly.
- **CVC counterparties** are matched on entity name, registered address, foreign-jurisdiction filings, and on-chain attribution where the program ingests blockchain-analytics evidence; the on-chain attribution is itself an identity-evidence stream the triage can carry.
- **Sponsor-bank-program reliance.** Where the fintech relies on the sponsor bank for parts of CDD, the operative identity attributes the triage matches against are the program's matched set, not just the fintech's. The triage scopes the program before reading identity confidence.

#### Typology-link patterns payments-fintech adverse-media triage attends to

- **Marketplace fraud (seller fraud, buyer fraud, account-takeover, friendly fraud).** Distinguish marketplace-fraud typologies from financial-crime typologies; a buyer-fraud surface is consumer-protection-relevant but is not a SAR-decision-evidence typology by itself unless it intersects with structuring, layering, or known-fraud-ring activity.
- **Convertible-virtual-currency obfuscation (mixers, chain-hopping, cross-chain bridges).** Cite to the FinCEN CVC advisory and the OFAC virtual-currency guidance in the typology tag. Routes to `sanctions-screening-qa` where a sanctions-evasion overlap is implicated.
- **Ransomware facilitation.** A CVC counterparty implicated in ransomware-payment facilitation (named in a public ransomware advisory's indicator list, or in a FinCEN or OFAC enforcement notice). Routes to `sanctions-screening-qa` and to `sar-decision-qa`.
- **BIN-sponsor abuse and prepaid-card schemes.** Adverse media on prepaid-card schemes routed through a customer's BIN sponsorship; cite to the FinCEN advisory on prepaid access (where applicable) in the typology tag.
- **Synthetic-identity fraud.** Press and regulator coverage of synthetic-identity rings; identity-confidence is bounded by how the customer file's identity attributes were collected (the synthetic identity is, by design, hard to disambiguate against a synthetic match).

#### Fintech routing patterns

- A tier-1 hit on a fintech customer that is itself an MSB or a payment intermediary routes to `cdd-risk-review` for an event-driven refresh and to `edd-escalation-pack` for the heightened-risk-population read.
- A CVC counterparty hit with sanctions-evasion or ransomware linkage routes to `sanctions-screening-qa` first; the CDD lane is secondary because the screening overlap is the load-bearing decision.
- A marketplace-seller adverse-media hit without primary-source corroboration carries `[evidence needed]` for the relationship owner to corroborate; the consumer-complaint volume goes into `aggregated_themes` rather than into per-hit materiality.
- A bulk re-scan output on a sponsor-bank-program portfolio routes program-level themes (high common-name noise, high vendor-tier-3 share, recurring counterparties across sellers) back to the sponsor program's BSA function; per-customer escalation is reserved for the material subset.

#### Common pitfalls in fintech adverse-media triage

- Treating consumer-complaint volume as a typology-link signal without primary-source corroboration.
- Reading CVC adverse media without consulting the on-chain attribution evidence the program may already hold.
- Letting the sponsor-bank-program and the fintech's own program collapse into one CDD-file read; the triage scopes which entity's CDD the hit bears on before routing.
- Under-reading sanctions-evasion overlap on CVC and DeFi hits; the routing line to `sanctions-screening-qa` is the load-bearing one in this segment.
- Letting digital-only-onboarding identity-attribute thinness justify a high identity-confidence call where the matchable evidence does not support it.
- Recommending the rating change, the EDD upgrade, the SAR filing, the seller suspension, the BIN-sponsor termination, or the exit; the triage routes the artifact to the named decisionmaker.
