# sector-overlays

One section per sector. Read only the sections the scope calls for.

## capital-markets

### Sector overlay — capital markets and asset management

This skill is sector-unique. The capital-markets overlay is the only sector overlay; there is no banking, insurance, or payments analogue. The overlay carries the registration-class flavour: investment adviser, broker-dealer, dual registrant, fund adviser. The surveillance artifact's spine is constant; the rule lattice loaded into each section flexes by class.

#### Registration-class lens — which rule lattice loads

The first scope question for the surveillance review is which registration-class lens applies. The four classes are not interchangeable and the artifact must name which it is operating under.

- **Investment adviser (IA)** — the duty is the fiduciary duty of care under Advisers Act §206 as restated in IA-5248 (June 5, 2019). Best execution is a periodic governance review at the cadence the adviser's compliance program (Rule 206(4)-7) defines, typically quarterly with an annual deeper read. The factor analysis tracks the IA-side factor list (price, speed, likelihood of execution, size, market impact, accessibility of the market, total transaction costs, customer instructions). The artifact carries the documentation supporting the determination, not the determination's prose alone.
- **Broker-dealer (BD)** — the duty is FINRA Rule 5310 with Supplementary Material .01 through .09. The .09 "regular and rigorous review" is the doctrinal anchor for the venue-level surveillance; the .01 factor list applies in the trade-by-trade exception sampling. Cadence is firm-defined under WSP (FINRA Rule 3110); typical practice is monthly venue-level surveillance with a quarterly best-execution committee read.
- **Dual registrant (IA and BD)** — both lattices apply and the artifact must show both. Dual registrants commonly run one operational surveillance process and produce two sets of documentation (the IA-side review feeding the adviser's fiduciary file; the BD-side review feeding the WSP file and the FINRA exam record). Trying to collapse the two is the most-frequent finding pattern in dual-registrant exams.
- **Fund adviser** — the IA-side review is the substantive review. The output additionally feeds the fund's §15(c) board materials and (where affiliated brokerage or soft-dollars are in use) the §17(e) and §28(e) blocks of the fund-board pack. Cadence is typically quarterly into board meetings, with the §15(c) annual approval as the structural anchor.

The artifact's review-identification block carries `firm_registration` as one of `{IA, BD, IA_and_BD, fund_adviser}` and the workflow loads the matching rule lattice.

#### Asset-class flavour — what surveillance looks like per class

The factor analysis applies across asset classes but the operative metrics, data sources, and exception types differ.

- **Listed equities (NMS stocks)** — the consolidated tape supports NBBO-referenced metrics (price improvement, effective-over-quoted, at-or-better fills, NBBO trade-through, midpoint capture). Rule 605 venue disclosures and Rule 606 routing disclosures are the public reconciliation surfaces. Off-exchange routing to wholesalers under PFOF arrangements is the most-scrutinised sub-flavour; the surveillance must show the conflict was weighed in the determination, not just disclosed.
- **Listed options** — the National Best Bid and Offer applies but the dispersion across exchanges, the maker-taker fee schedule complexity, and the linkage rules under the Options Linkage Plan shape the analysis. Retail options PFOF is a current SEC and FINRA examination focus.
- **Fixed income (corporates, munis, governments)** — no consolidated tape; TRACE (corporate bonds), MSRB EMMA (munis), and dealer pre-trade quote infrastructure substitute. The surveillance reads competitive quote evidence, time-stamped quote logs, and dealer-axe inventory at the trade time, against the executed price. FINRA Regulatory Notice 15-46 is the cross-asset interpretive anchor; FINRA's fixed-income surveillance series has expanded the markup / markdown disclosure regime under Rule 2121.
- **Mutual funds and ETFs at the trade level** — for the mutual-fund creation / redemption side and for ETF authorised-participant flows the analysis differs from secondary-market trading. The skill covers secondary-market ETF execution under the equities rubric; the AP creation / redemption flow is out of scope here and routes to the fund-board-reporting skill.
- **Derivatives (cleared swaps, listed futures)** — clearing-broker selection sits underneath best execution; the analysis includes clearing fees, give-up arrangements, and the give-up bilateral relationship's terms. For SEFs, the request-for-quote vs central limit-order book mode shapes the evidence.
- **FX** — for advisers transacting FX as a principal counterparty (in-house FX) versus through agency execution at a custodian or third-party venue, the analysis differs sharply. The Global FX Code is the practice anchor; the surveillance reads price-versus-mid-at-execution, time-stamping integrity, and last-look practices. Custodian-FX practices have been a recurring litigation and enforcement focus.
- **Crypto** — where the firm trades crypto on behalf of clients, jurisdictional uncertainty (whether the asset is a security, a commodity, neither), venue regulatory status, custody arrangements, and lack of a consolidated tape all shape what evidence is even available. The surveillance documents the limitations of the evidence rather than claiming a coverage it cannot support.

The artifact's `asset_class_scope` field drives which asset-class lens loads. Multi-asset reviews stratify the sample by asset class and apply the matching evidence framework per stratum.

#### Sub-flavour — investment adviser flow

The IA-side review is anchored to §206 fiduciary duty and to Rule 206(4)-7. The adviser's compliance program defines the surveillance cadence, the sample method, the committee membership, and the escalation path. The surveillance materially feeds:

- The CCO's annual review under Rule 206(4)-7 (which covers all material aspects of the compliance program, including best execution).
- The Form ADV Part 2A item 12 (Brokerage Practices) disclosure, including soft-dollar and affiliated-broker disclosure consistency.
- The conflict disclosures under Form ADV Part 2A items 5 and 14 where brokerage and PFOF arrangements create conflicts.

The artifact records: which custodians and executing brokers the adviser uses, how brokerage is allocated (block trading, allocation methodology, partial-fill allocation), whether the adviser directs trades, the conflict-laden arrangements (PFOF received by the executing broker even if the adviser does not retain it; affiliated broker; soft-dollar; commission-sharing arrangements; principal trades under §206(3); agency cross trades under §206(3)).

#### Sub-flavour — broker-dealer flow

The BD-side review is anchored to FINRA Rule 5310 .09 regular-and-rigorous review and to Rule 3110 supervision. The artifact carries the venue-by-venue execution-quality table, the comparison against alternative venues the firm could have routed to, the PFOF treatment in the determination (not just the 606 disclosure), the order-type-by-order-type analysis (market orders, marketable limit, non-marketable limit, midpoint-pegged, retail-improvement orders), and the customer-segment analysis (retail vs institutional; held vs not-held).

The committee pack documents the venue inventory changes (added, removed, watchlist) with rationale, the watchlist exit / continued-watch decisions, and the actions taken on previously identified deficiencies. The Rule 605 reconciliation block compares the venue's published 605 metrics against what the firm observed as a router; material divergence triggers an investigation block.

#### Sub-flavour — fund-adviser flow

The fund-adviser variant produces the IA-side review as the substantive output and additionally produces the fund-board-facing materials. The fund-board read includes:

- The §15(c) brokerage-and-best-execution discussion (factual record of execution-quality outcomes and process used).
- The §17(e) affiliated-broker compensation review (reasonable-and-fair attestation supported by comparable-rate evidence; Rule 17e-1 procedures and quarterly board determinations).
- The §28(e) soft-dollar review (eligibility of products under the 2006 interpretive release; mixed-use allocation methodology and documentation; commission-sharing arrangement counterparty and terms).
- The directed brokerage analysis where applicable (no-PFOF directed brokerage; client-directed-brokerage arrangements at the underlying-shareholder level for sub-advised funds).

The fund's board has its own counsel and its own compliance officer; the surveillance feeds material into the board pack but the adviser's CCO is not the board's CCO. The artifact records the escalation routing into the board materials separately from the adviser-internal escalation.

#### Conflict-as-input — required treatment in the artifact

The skill's conflict-review block is structured against the conflict types the relevant rule set names. For each conflict type in scope, the block records: presence (yes / no); how the conflict was weighed in the best-execution determination (not how it was disclosed downstream); the supporting evidence; the residual conflict after mitigation. The conflict types are:

- **Payment for order flow (PFOF)** — for routed retail equity and options flow where the executing venue pays the routing broker per share, per contract, or per dollar. The disclosure under Rule 606 is necessary but not sufficient; the surveillance must show the conflict was a factor that the determination weighed.
- **Principal trades — Advisers Act §206(3)** — adviser purchasing a security from or selling a security to a client out of its own inventory. Requires written disclosure to and consent from the client per transaction (the prospective consent allowed by SEC No-Action Letter to SMC Capital, Inc. (Sep 5, 1995) is narrow and bookkeeping-intensive).
- **Agency cross trades — §206(3)** — adviser causing two of its client accounts to take opposite sides of a single trade. Requires written disclosure and prospective consent under Rule 206(3)-2.
- **Affiliated brokerage — ICA §17(e)** — fund routing brokerage to an affiliated broker. Requires §17(e)(1) reasonable-and-fair compensation supported by comparable-rate evidence and §17(e)(2) board procedures with periodic determinations.
- **Soft dollars — Exchange Act §28(e)** — paid-up commissions in exchange for research and brokerage services. Requires good-faith eligibility determination per the 2006 interpretive release and mixed-use allocation methodology with contemporaneous documentation.
- **Commission-sharing arrangements (CSAs)** — separate-pool arrangements where research is paid out of accumulated commission credits. The 2006 release addresses CSAs explicitly; the surveillance reviews the third-party-research provider list, the budget vs spend, and the controls on adviser-directed disbursements.
- **Inducements and prohibited transfers** — direct or indirect compensation flowing to the adviser or its personnel from venues or executing brokers, outside the §28(e) safe harbor and the §17(e) framework. These require separate review under §206 and Rule 204A-1 (code of ethics).

A conflict the artifact does not name is a finding pattern in itself.

#### Cadence and committee posture

Cadence variants the skill supports:

- **Quarterly + annual** — typical IA cadence: quarterly venue and exception read, annual deeper review feeding Rule 206(4)-7 and Form ADV.
- **Monthly + quarterly + annual** — typical BD cadence: monthly venue surveillance, quarterly committee read, annual review for FINRA exam record.
- **Quarterly into fund board** — fund-adviser cadence: quarterly best-execution surveillance feeding into quarterly fund-board materials, with §15(c) annual approval as the anchor.

Committee membership the artifact records: best-execution committee chair (typically head of trading or head of investments), participants (CCO, head of operations, head of legal, head of risk where the firm has a CRO), counsel attendance, and (where applicable) board-CCO sample attendance for fund-adviser flows. The artifact records dissents and follow-up assignments.

#### What this overlay does not carry

The overlay does not carry firm-specific brokerage allocation methodology, custodian relationship terms, sub-advised mandate structures, soft-dollar provider lists, or specific PFOF rates. Those live in `references/firm-overlay.md` when the firm has installed one; the overlay consumes them. The overlay also does not carry a TCA model — TCA is consumed as input from a vendor or in-house tool; the surveillance reads TCA outputs but does not build them.

The overlay does not carry the fund-board reporting cycle (that lives in `fund-board-reporting`); it carries the surveillance-to-board handoff fields that the fund-board pack consumes.
