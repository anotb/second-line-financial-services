# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for risk-committee-pack

When the scope record names sector `banking`, this overlay adds banking-specific structure and content expectations to the committee pack. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-sector elements.

Loaded by: `risk-committee-pack/SKILL.md` when `scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, BHC, FBO with US operations).

#### Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

#### What changes for banking committee packs

##### 1. Risk taxonomy follows the OCC Heightened Standards categories

The heat map for OCC-supervised covered banks uses the eight Risk Governance Framework categories named in 12 CFR Part 30 Appendix D Section II: credit, interest rate, liquidity, price, operational, compliance, strategic, and reputation. Most firms add at least three more in committee reporting (model risk, third-party risk, financial-crime risk), and most add cyber as a standalone category even though it sits under operational in the regulatory taxonomy. Climate is reported under strategic with documented rationale (see the climate cross-cutting overlay) unless the firm has elected a standalone climate cell.

For BHCs reporting under FRB SR 12-17, the risk taxonomy aligns to the LFI rating system components (capital, liquidity, governance and controls).

##### 2. Risk Appetite Statement is the centrepiece

12 CFR Part 30 Appendix D Section III requires a written RAS with both qualitative components and quantitative limits, and the framework must provide for monitoring and reporting against the limits. The committee pack:

- Reports each RAS metric with limit, trigger, tolerance, and current value.
- Shows the ladder from the RAS metric to first-line operating limits. A pack that reports RAS metrics without the operating-limit linkage does not demonstrably meet the Section III expectation.
- Names breach owners and recalibration requests as decision items, not as status updates.

For non-OCC banks (state member banks, FDIC-supervised state nonmembers), the RAS expectation comes through Regulation YY (12 CFR Part 252 — Subpart C §252.22 risk-committee at $50B; Subpart D §§252.31-252.36 enhanced prudential standards at $100B), FDIC Statement of Policy on Bank Risk Management, or the firm's own framework; the substantive shape is the same. (SR 11-7 was the model-risk anchor, **superseded by the Joint Interagency Revised Guidance on Model Risk Management — OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026** — and is not the RAS anchor.)

##### 3. MRA / MRIA aging and closure status is a standing section

OCC and FRB supervisory letters distinguish Matters Requiring Attention (MRA) and Matters Requiring Immediate Attention (MRIA). The Issues and Remediation section of the pack carries:

- Open MRA count and over-age count, with the firm's defined age threshold.
- Open MRIA count and over-age count.
- Each MRA / MRIA over the age threshold listed individually with regulator, finding date, action plan, owner (role), forward action, and slippage commentary.
- Closure status for items closed in the period, with the regulator's response (closed by examiner letter, in dispute, awaiting examiner confirmation).

A counter-only treatment is insufficient under SR 12-17 and Heightened Standards.

##### 4. Capital and liquidity content for stress-eligible BHCs

For BHCs subject to CCAR or DFAST, the pack carries:

- Most recent stress-test results (DFAST public results; CCAR objection / non-objection status; firm-side internal stress).
- Current capital ratios against the minimum, buffer, and management-buffer thresholds; movement against prior period.
- LCR and NSFR position for in-scope BHCs (Category I-IV per the FRB tailoring framework, with applicability varying by category); contingency funding plan test record; brokered-deposit and BaaS-deposit treatment for firms with material fintech-partner deposit relationships.
- Resolution-planning status for §165(d) covered companies.

Verify current CCAR / DFAST scope and tailoring-category applicability at pack-write time as the FRB tailoring framework (12 CFR §252.5) has been amended multiple times since 2019.

##### 5. Three-lines-of-defense and independent-risk-management evidence

Under 12 CFR Part 30 Appendix D Sections IV-VI, the board oversees compliance through an independent risk committee, the CRO is independent of front-line units, and internal audit is independent of both. The committee pack typically includes a brief on:

- CRO and head-of-internal-audit attestations on the independence of their respective functions.
- Front-line risk-management maturity (Section IV expectations on front-line unit responsibility).
- Any open issues affecting the framework itself (e.g., a structural independence gap surfaced by internal audit).

This content is light in routine quarterly packs and substantial in the annual pack ahead of a Heightened Standards horizontal review.

##### 6. CRA, fair-lending, and consumer-compliance roll-up

Where the BHC has consumer banking subsidiaries, the committee pack carries a brief on CRA performance status, fair-lending exam findings, and consumer-compliance issue posture. Depth varies by BHC structure; a holding-company-level pack typically references a separate compliance committee pack for detail.

CRA modernization rule (2023 final rule) has been subject to legal challenge; verify current effective state and the firm's posture at pack-write time.

##### 7. Cross-link to other capability skills

- KRI commentary for individual RAG-breached metrics: `kri-commentary`.
- Open-issue write-ups beyond the standing aging summary: `issue-writeup`.
- Management responses to open MRAs / MRIAs: `management-response`.
- BCBS 239 self-assessment for the data confidence appendix: `bcbs239-gap-assessment`.
- Cyber-disclosure-decision content (Item 1.05 8-K trigger analysis): `cyber-disclosure-readiness`.

#### Banking-specific output template additions

Added to the pack (mapped to schema where present):

- `pack_metadata.heightened_standards_inscope` — boolean, true for OCC large banks subject to 12 CFR Part 30 Appendix D.
- `pack_metadata.bank_charter_type` — national bank / state member / state nonmember / savings association / BHC / FBO IHC.
- `pack_metadata.primary_federal_regulator` — OCC / FRB / FDIC.
- `pack_metadata.tailoring_category` — FRB tailoring category (I, II, III, IV) for in-scope BHCs.
- `pack_metadata.stress_testing_inscope` — boolean, with cross-reference to CCAR or DFAST submission.
- `heat_map[]` — twelve-cell layout (eight Heightened Standards categories plus model, third-party, financial-crime, cyber); climate under strategic unless separately rated.
- `ras_status[]` — operating-limit-ladder column added; breach owner field required.
- `issues_summary` — MRA / MRIA buckets with regulator-letter dates and closure status.
- `forward_looking.regulatory_horizon[]` — named items (e.g., FRB stress test scenario publication; expected NYDFS Part 500 amendment effective date; Heightened Standards horizontal-review schedule).

#### Common pitfalls in banking committee packs

- Reporting RAS metrics without the operating-limit ladder. Section III expects monitoring and reporting against limits; the ladder is the reviewer's check that limits flow through to the front line.
- Treating MRA / MRIA as a counter rather than a manager. Each over-age item needs an owner, forward action, and slippage commentary; the standing aging summary is necessary but not sufficient.
- Stress-test summaries that report only the public DFAST result without the firm's internal stress posture and the implications for the management buffer. The committee owns the buffer policy; the pack supports that ownership.
- Cyber as a separate floating appendix rather than a heat-map cell or a documented sub-category. Cyber risk affects multiple Heightened Standards categories (operational, compliance, strategic, reputation) and the pack treats it as enterprise risk.
- Climate as bolt-on rather than mapped under strategic (or separately rated with documented rationale). The climate cross-cutting overlay covers the substantive content; the heat-map placement is a pack-architecture decision the chair should not have to make at the meeting.
- Carrying three years of stress-test detail in every quarterly pack. The standing pack carries the current cycle and a short trend; the annual pack carries the multi-cycle view.

## capital-markets

### Capital markets sector overlay for risk-committee-pack

When the scope record names sector `capital-markets`, this overlay adds adviser, broker-dealer, and asset-manager-specific structure and content expectations to the committee pack. Where there is conflict between the capability defaults and this overlay, the overlay governs the capital-markets-sector elements.

Loaded by: `risk-committee-pack/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`, or when the institution type is an SEC-registered investment adviser, FINRA-member broker-dealer, dual-registrant, asset-management group, or registered fund complex.

#### Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

#### What changes for capital-markets committee packs

##### 1. Adviser-level enterprise risk committee, distinct from the fund board

The committee pack scope is the adviser firm (and the broker-dealer where dual-registrant), not individual funds. Items material to the fund board may also be material to the adviser risk committee, but the audiences and the recommendations differ. Fund-board reporting lives in the separate skill `fund-board-reporting`; the committee pack flags any items that should be elevated to the fund board but does not duplicate the fund-board pack.

For dual-registrants (BD and IA) and integrated asset-management groups, the pack typically covers both regulated entities with a clear delineation of which risks roll up where.

##### 2. Capital-markets risk taxonomy

The heat map for advisers, BDs, and asset managers covers, at minimum: investment risk (portfolio risk, leverage, liquidity at fund and firm level); operational risk; technology risk; vendor risk; regulatory risk; conduct risk; financial-crime risk; cyber risk; fiduciary risk; and (for BDs) market-access and order-handling risk. Strategic and reputational risk are also standard. Climate is mapped under strategic unless the firm has elected a standalone cell or reports under EU SFDR / CSRD parent-group consolidation.

For BDs and dual-registrants, the heat map adds net-capital and customer-protection risk under Exchange Act Rules 15c3-1 and 15c3-3.

##### 3. Compliance-program reporting under Rule 206(4)-7 and FINRA 3120 / 3130

Investment Advisers Act Rule 206(4)-7 requires advisers to adopt and implement written policies and procedures, conduct an annual review, and designate a CCO. The annual review summary frequently lands in the committee pack. The pack carries:

- Annual-review status and any material findings from the most recent review.
- Material compliance program changes in the period (policy updates, control redesign, CCO transition).
- Any 206(4)-7-tagged exam findings or self-identified deficiencies.

For FINRA-member BDs, FINRA Rule 3120 (supervisory control system testing) and Rule 3130 (CCO certification) drive parallel content:

- Annual 3120 testing summary and the report submitted to senior management.
- 3130 CEO/CCO annual certification posture.
- Any 3120-driven supervisory-system change in the period.

##### 4. Form PF current-event triggers and large-trader reporting

For private fund advisers required to file Form PF, current-event triggers (Section 5 events: ARP advisers; Section 6 events: large hedge fund advisers; new triggers under 2023 amendments) feed the committee directly and on a same-business-day or 72-hour cadence, depending on the trigger. The pack carries:

- Any Form PF current-event filings made in the period and the underlying event detail.
- Pending or contemplated Form PF current-event analyses where the trigger threshold is approaching.
- Form 13F, 13D / 13G, and 13H (large-trader) reporting posture for in-scope filers.

Verify the current Form PF current-event-trigger framework at pack-write time as the 2023 amendments have phased compliance dates.

##### 5. Net capital, customer protection, and market access for BDs

For BDs and dual-registrants, the pack carries a brief on:

- Net capital position and movement; aggregate indebtedness ratio (where applicable); haircut and concentration deductions.
- Customer-protection reserve formula computation status under Rule 15c3-3.
- Market access controls under Rule 15c3-5 for BDs with exchange or ATS access; control-failure events in the period; pre-trade-risk-control breach summary.
- Best-execution governance status under Reg NMS and FINRA 5310.

Net capital and reserve-formula detail lives outside the pack; the pack carries the executive summary and any items requiring committee attention (e.g., a near-breach, a policy-driven buffer change).

##### 6. Marketing Rule, custody, and books-and-records risk

For advisers, the pack carries:

- Marketing Rule (Rule 206(4)-1) compliance posture: hypothetical performance, testimonials and endorsements, third-party ratings, performance presentation. Material findings or self-identified gaps belong in the issues section.
- Custody Rule (Rule 206(4)-2) status: surprise exam posture for advisers with custody; any custody-rule breach or change in custody posture.
- Books and records (Rule 204-2) status: any material gap that affects examination readiness.

For BDs, the parallel content covers Rules 17a-3 / 17a-4 books-and-records posture, with attention to electronic-communications retention given the SEC and CFTC enforcement focus on off-channel-communications.

##### 7. Liquidity risk for funds and the firm

Open-end-fund liquidity-risk-management posture under Rule 22e-4 lives primarily in fund-board reporting; the committee pack carries the firm-level rollup: any board-approved bucket changes, any swing-pricing or in-kind-redemption activation in the period, and any liquidity event that affected the firm. Money-market fund (Rule 2a-7) reform implementation status (where applicable) is included for affected complexes.

##### 8. Cross-link to other capability skills

- KRI commentary for individual RAG-breached metrics: `kri-commentary`.
- Open-issue write-ups beyond the standing aging summary: `issue-writeup`.
- Fund-board reporting: `fund-board-reporting`.
- Cyber-disclosure-decision content (Reg S-K Item 106; 8-K Item 1.05): `cyber-disclosure-readiness`.

#### Capital-markets-specific output template additions

Added to the pack (mapped to schema where present):

- `pack_metadata.entity_types` — array (RIA, BD, dual-registrant, registered-fund-complex, private-fund-adviser).
- `pack_metadata.primary_regulators` — array (SEC, FINRA, CFTC, NFA, state securities, NYDFS, FCA where applicable).
- `pack_metadata.public_company` — boolean for parent reporting issuer (drives SEC Item 106 cyber and other disclosure considerations).
- `heat_map[]` — capital-markets-taxonomy rows (investment, operational, technology, vendor, regulatory, conduct, financial crime, cyber, fiduciary, plus market-access and net-capital for BDs).
- `compliance_program_status` — object with 206(4)-7 annual-review summary; FINRA 3120 / 3130 status for BDs.
- `form_pf_current_events` — array of Form PF current-event filings or near-trigger items in the period for in-scope advisers.
- `bd_capital_status` — object with net capital, aggregate indebtedness ratio, customer-protection-reserve status for in-scope BDs.
- `marketing_rule_posture` — object summarizing Marketing Rule findings and remediation status for advisers.
- `liquidity_program_status` — object summarizing 22e-4 liquidity-program activity and any swing-pricing or in-kind-redemption activations for fund-complex packs.

#### Common pitfalls in capital-markets committee packs

- Conflating the adviser risk committee with the fund board. The pack scope is the firm; fund-specific items go to the fund board through a separate channel and are flagged here only when they affect the firm.
- Reporting Form PF current events as a counter rather than as a substantive brief. Each filing or near-trigger should have an explanation; the committee owns the policy choices that affect the trigger calibration.
- Net-capital reporting that shows the ratio without the buffer policy and the management-action triggers. The committee owns the buffer policy; the pack supports that ownership.
- Marketing Rule treated as a routine compliance matter when the SEC has surfaced enforcement on hypothetical performance and testimonials. Material findings belong in issues with named owner and forward action.
- Off-channel-communications enforcement risk under-reported. The SEC and CFTC have brought multi-firm enforcement actions on this surface; the pack carries the firm posture and the books-and-records remediation status.
- Liquidity items reported only at fund level for fund-complex packs. The firm-level rollup (any swing pricing, any in-kind redemption, any liquidity-bucket change board-approved in the period) is the committee-level view.
- Cyber-disclosure decisions reported in the pack as if they bind the disclosure committee. The disclosure-committee process is separate; the pack flags material cyber events and the disclosure-committee referral, not the disclosure decision itself.

## insurance

### Insurance sector overlay for risk-committee-pack

When the scope record names sector `insurance`, this overlay adds insurance-specific structure and content expectations to the committee pack so the artifact a state DOI examiner reviews reads as ORSA-aligned. Where there is conflict between the capability defaults and this overlay, the overlay governs the insurance-sector elements.

Loaded by: `risk-committee-pack/SKILL.md` when `scope.sector_overlay_set` includes `insurance`, or when the institution type implicates a state DOI (life and health insurer, P&C insurer, fraternal benefit society, captive, surplus lines insurer, reinsurer with US operations).

#### Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

#### What changes for insurance committee packs

##### 1. Pack architecture maps to the ORSA Summary Report

NAIC Risk Management and Own Risk and Solvency Assessment Model Act (#505) requires in-scope insurers to file an annual ORSA Summary Report with their lead state regulator, organized in three sections: Section 1 (Description of the Insurer's Risk Management Framework), Section 2 (Insurer's Assessment of Risk Exposure), Section 3 (Group Risk Capital and Prospective Solvency Assessment). The committee pack is the principal supporting document for Sections 1 and 2 and an input to Section 3.

Section-by-section mapping:

- ORSA Section 1 (Risk Management Framework) consumes: pack risk-governance-framework brief, three-lines-of-defense maturity, RAS overview, framework changes in the period.
- ORSA Section 2 (Risk Exposure Assessment) consumes: pack heat map, top risks, material risk events, KRI movement and breaches, RAS status, scenario commentary including normal and stressed conditions.
- ORSA Section 3 (Group Risk Capital and Prospective Solvency Assessment) consumes: pack capital and prospective-solvency commentary; deeper actuarial analysis lives outside the pack.

##### 2. Insurance risk taxonomy adds carrier-specific categories

The heat map for insurers covers, at minimum: pricing and underwriting risk; reserving risk (life, health, P&C as applicable); reinsurance and credit risk (counterparty exposure on ceded business); market and ALM risk (interest rate, equity, spread, FX); insurance operational risk including outsourced functions; compliance risk; financial-crime risk; cyber risk per NAIC Insurance Data Security Model Law (Model #668); strategic risk; reputational risk. AI risk is added per NAIC Bulletin Use of Artificial Intelligence Systems by Insurers (December 2023) where the carrier has material AI use cases. Climate risk is mapped under strategic unless the carrier reports under a regime requiring a standalone cell (e.g., EU CSRD parent-group consolidation).

Health insurers add medical-loss-ratio risk and benefit-design risk. Life insurers add longevity, mortality, and lapse risk. P&C insurers add catastrophe risk and casualty-development risk. The overlay does not enumerate every line-of-business breakdown; the firm's risk taxonomy drives the rows.

##### 3. Stress and prospective-solvency narrative is required

ORSA Section 2 expects forward-looking stress and capital-adequacy commentary under both normal and stressed conditions. The pack's Forward-Looking Commentary section carries:

- Scenario inventory used (own scenarios, NAIC catastrophe scenarios where applicable, regulator-prescribed scenarios for life insurers under principle-based reserving, climate scenarios where in scope).
- Result summary per scenario with breach flags against capital, liquidity, and risk-appetite metrics.
- Narrative on prospective solvency including capital actions contemplated or executed in the period.
- Ladder to ORSA Section 3 actuarial analysis (the pack does not duplicate the actuarial work).

##### 4. NAIC Corporate Governance Annual Disclosure cross-walk

NAIC Corporate Governance Annual Disclosure Model Act (#305) requires in-scope insurers to file annual governance disclosure with the lead state regulator. The committee pack frequently supports the CGAD filing as evidence of board-level risk oversight. The pack carries:

- Risk committee charter reference and current composition.
- Standing committee cadence and special-meeting count for the period.
- Key-person dependencies in the risk-governance framework (CRO, chief actuary, head of risk reporting, head of internal audit) and any vacancies.
- Self-assessment posture: most carriers refresh CGAD content annually; the committee pack supports the annual cycle.

Verify Model #305 state adoption status for the carrier's lead state at pack-write time.

##### 5. State DOI variation and lead-state framework

ORSA filing posture varies by state: some receive ORSA in narrative form, others receive it as an attachment to other filings, others have additional reporting demands (e.g., NY DFS Regulation 203 ERM reporting for in-scope NY-licensed entities). The committee pack flags the lead-state framework and any non-lead-state-specific demands the pack supports.

##### 6. AI risk content per NAIC Bulletin December 2023

For carriers with material AI use cases (accelerated underwriting, claims AI, marketing AI, agent / producer AI co-pilots), the pack carries a brief on:

- AIS Program element-by-element status: governance, risk management, testing and validation, third-party AI accountability, data practices, monitoring, transparency, fairness.
- Material AI use cases by tier with named owner.
- AI-related risk events in the period (model performance breach, vendor change-of-version, fairness-test exception, consumer-disclosure complaint).
- Cross-link to the AI-specific committee pack: `board-ai-risk-pack`.

##### 7. TPA / claims-administrator and outsourced-function exposure

For carriers with material outsourced functions (TPA, MGA, MGU, claims administrator, IT outsourcer, AI vendor, ECDIS data provider), the pack's third-party section carries the concentration view across these vendor types. NAIC Insurance Data Security Model Law §4.F third-party-service-provider obligations sit alongside the committee's third-party-risk-management oversight; the pack flags any §4.F gap that surfaced in the period.

Cross-link to insurance vendor-diligence overlays where present.

##### 8. Cross-link to other capability skills

- KRI commentary for individual RAG-breached metrics: `kri-commentary`.
- Open-issue write-ups beyond the standing aging summary: `issue-writeup`.
- AI-specific committee pack for material AI use cases: `board-ai-risk-pack`.
- Cyber-disclosure-decision content for material cyber events: `cyber-disclosure-readiness`.

#### Insurance-specific output template additions

Added to the pack (mapped to schema where present):

- `pack_metadata.lead_state_regulator` — state insurance department serving as lead-state regulator for the group.
- `pack_metadata.orsa_filer` — boolean, true for #505-in-scope insurers.
- `pack_metadata.cgad_filer` — boolean, true for #305-adopted-state-licensed insurers.
- `pack_metadata.business_lines` — array of LOBs (life, health, P&C, reinsurance, fraternal, surplus-lines, captive).
- `heat_map[]` — insurance-taxonomy rows (pricing/underwriting, reserving, reinsurance/credit, market/ALM, insurance operational, compliance, financial crime, cyber, AI where applicable, strategic, reputational).
- `forward_looking.scenario_results[]` — scenario inventory required; normal and stressed conditions both required for ORSA-filer packs.
- `orsa_section_map` — object mapping pack sections to ORSA Summary Report sections (1, 2, 3) for #505-in-scope insurers.
- `cgad_section_map` — object mapping pack sections to CGAD content for #305-adopted-state-licensed insurers.
- `ais_program_status` — object with element-by-element status for carriers with material AI use cases.

#### Common pitfalls in insurance committee packs

- Treating ORSA as the carrier's annual-cycle artifact and the committee pack as separate. The committee pack is the principal supporting document for ORSA Sections 1 and 2; the two should not contradict each other.
- Carrying generic enterprise risk taxonomy without insurance-specific categories (pricing/underwriting, reserving, reinsurance/credit). Examiners read for these by name.
- Reporting AI risk as a footnote when the carrier has material AI use cases. NAIC Bulletin December 2023 expects AIS Program status; committee-level visibility is part of the program.
- Treating the TPA's controls as out of scope. Under NAIC #668 §4.F the carrier remains accountable for the TPA's controls on the carrier's policies; the pack flags TPA-related gaps as carrier issues.
- Catastrophe-risk commentary in P&C packs that reports modeled PML without the assumption set and the validation status of the model. Examiners probe both.
- Climate as a standalone appendix rather than mapped into the risk taxonomy. The climate cross-cutting overlay covers placement and content.
- Reporting CGAD elements only annually when the underlying governance posture has changed in the period. Material changes (CRO turnover, framework restructure, new committee charter) belong in the standing pack.

## payments-fintech

### Payments-fintech sector overlay for risk-committee-pack

When the scope record names sector `payments-fintech`, this overlay adds payments and fintech-specific structure and content expectations to the committee pack. Where there is conflict between the capability defaults and this overlay, the overlay governs the payments-fintech-sector elements.

Loaded by: `risk-committee-pack/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`, or when the institution type is a money transmitter, payments processor, neobank, BaaS-sponsor bank, BaaS-end-platform, card program manager, payments-rail operator, or other nonbank payments / fintech entity.

#### Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

#### What changes for payments-fintech committee packs

##### 1. Two committee patterns: nonbank fintech and BaaS sponsor bank

Two distinct committee patterns sit under this overlay:

- **Nonbank fintech / money transmitter / payments processor**: the risk committee is typically a board-level or executive risk committee with no federal prudential regulator oversight. Audience is the board or executive committee; primary regulators are state DFI / DOB (for money transmitters), the CFPB (for §1024 larger participants and §1031 / §1036 enforcement reach), and (for some entities) the OCC under the SPNB charter. The pack should not assert a federal prudential supervisor where none applies.
- **BaaS sponsor bank**: the sponsor bank's risk committee is a federally regulated bank committee (national bank, state member, state nonmember, savings association). The pack inherits the banking sector overlay for the bank-side governance frame and adds the BaaS-specific content described below for the partner-relationship view.

The pack carries one or the other pattern; rarely both in a single artifact.

##### 2. Third-party concentration and BaaS partner roll-up

The Interagency Guidance on Third-Party Relationships (OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023, June 6, 2023) sets the bank-side risk-management expectations for third-party relationships including fintech partners. For sponsor banks, the committee pack carries:

- BaaS partner inventory with criticality tier, asset / deposit / volume share, and activity scope.
- Partner concentration metrics: top-N partner share of deposits, top-N share of transaction volume, geographic concentration, customer-base concentration.
- Partner-by-partner status on the lifecycle (planning, due-diligence, contract, ongoing-monitoring, termination phase) for any partner in active diligence or termination.
- Subcontractor and fourth-party visibility: processor, ledger, KYC, fraud-decision vendor; the four-party pyramid is a recurring exam topic.
- Partner-driven loss events, regulatory actions, customer complaints, and remediation status.

For nonbank fintechs, the inverse view applies: sponsor-bank concentration, processor concentration, BIN-sponsor concentration, payments-rail concentration. A nonbank fintech whose payments rail or sponsor bank exits has the same operational impact as a sponsor bank whose top BaaS partner exits.

##### 3. Money transmitter / nonbank payments-specific risk taxonomy

The heat map for nonbank payments / fintech entities covers, at minimum: financial-crime risk (BSA / AML, OFAC, fraud); payments-operations risk (rail outage, settlement failure, processor failure); third-party / sponsor-bank risk; technology and cyber risk; consumer-compliance risk (Reg E, Reg DD, Reg Z where applicable, UDAAP); state-licensing risk (NMLS posture, state exam findings); operational risk; strategic risk; reputational risk. For larger participants under CFPB §1024 supervisory authority, regulatory risk is its own category.

For sponsor banks, the heat map follows the banking taxonomy with explicit BaaS partner-driven cells under operational, third-party, financial-crime, and (for material partner exposure) strategic.

##### 4. NACHA Operating Rules and rail-specific content

For ODFI sponsor banks and Third-Party Senders, NACHA Operating Rules (current edition) set the program-operator and originator-management expectations. The pack carries:

- Return-rate posture against current NACHA thresholds (administrative-return, overall-return, unauthorized-return) for each Originator and aggregate.
- Third-Party Sender registration status for any in-scope counterparty and the Originator agreements that Third-Party Sender holds.
- Rule-violation events in the period (NACHA Rules Enforcement Panel actions, fines, member-bank-administered enforcement).

Verify current NACHA thresholds and Rules Enforcement framework at pack-write time.

For card-rail operators (issuers, acquirers, processors), the parallel content covers PCI DSS posture, dispute and chargeback rates against thresholds, and brand-network compliance program status.

For instant-payments entities (FedNow, RTP, Same Day ACH), the pack carries fraud-rate and authorization-failure posture; instant-payment fraud is a recurring committee topic.

##### 5. CFPB nonbank supervision and §1033 / §1071 implementation

For nonbank entities under CFPB §1024 supervisory authority (larger participants in defined markets), the pack carries CFPB exam status, MRA / MRIA-equivalent supervisory letter posture, and any §1031 / §1036 enforcement engagement. The pack should not represent CFPB authority as out of scope for nonbanks; that is a recurring committee misframing.

For in-scope entities, §1033 (open banking, final rule October 2024; **§1033 compliance dates stayed as of October 29, 2025 per Forcht Bank, N.A. v. CFPB; CFPB-initiated reconsideration with ANPR August 22, 2025**) and §1071 (small-business lending data collection; **§1071 revised final rule May 1, 2026 — 1,000 covered transactions, effective June 30, 2026, compliance January 1, 2028 — supersedes 2023 tiered schedule**) implementation status belongs in the regulatory-horizon section. Verify current effectiveness at pack-write time.

##### 6. State-licensing posture

Money transmitters and other state-licensed entities carry standing committee content on:

- NMLS license inventory by state and license type (money transmitter, lender, debt collector, mortgage, etc., as applicable).
- State exam status (open exams, recent exam findings, remediation status).
- License renewal and material-change-filing posture.
- Multi-State MSB Examination Program (MMET) coordination status for entities licensed in multiple states.

State-licensing-driven loss events (license suspension, license-revocation proceeding, surety-bond call) belong in material risk events, not as a footnote.

##### 7. Cross-link to other capability skills and to sector skills

- KRI commentary for individual RAG-breached metrics: `kri-commentary`.
- Open-issue write-ups beyond the standing aging summary: `issue-writeup`.
- Payments-specific risk assessment: `payments-risk-assessment`.
- Fintech partner controls (sponsor-bank-side review): `fintech-partner-controls`.
- Open-banking data controls: `open-banking-data-controls`.
- Payment-operations incident review (post-incident): `payment-operations-incident-review`.

#### Payments-fintech-specific output template additions

Added to the pack (mapped to schema where present):

- `pack_metadata.entity_pattern` — enum (nonbank-fintech / money-transmitter / payments-processor / baas-sponsor-bank / card-program-manager / instant-payments-operator).
- `pack_metadata.cfpb_larger_participant_status` — boolean for §1024 in-scope nonbanks.
- `pack_metadata.nmls_states` — array of states where licensed (for money transmitters and other state-licensed entities).
- `heat_map[]` — payments-taxonomy rows (financial-crime, payments-operations, third-party / sponsor-bank, technology / cyber, consumer-compliance, state-licensing, operational, strategic, reputational).
- `partner_concentration` — object with top-N partner share by deposits / volume / geography / customer base for sponsor banks; or top-N sponsor / processor / BIN-sponsor concentration for nonbank fintechs.
- `nacha_return_rates` — object with current return-rate posture against NACHA thresholds for ODFI and Third-Party Sender programs.
- `state_exam_status` — object with open and closed state exams, MRA-equivalent items, and aging.
- `cfpb_supervision_status` — object with §1024 exam status and §1031 / §1036 enforcement engagement for in-scope nonbanks.

#### Common pitfalls in payments-fintech committee packs

- Asserting a federal prudential supervisor for a nonbank fintech where none applies. State DFI / DOB and CFPB are the operative regulators for most nonbanks; the pack should not borrow the bank-style framing without earning it.
- Treating CFPB authority as out of scope for nonbanks. §1024 supervisory authority and §1031 / §1036 enforcement reach apply; the pack carries the posture.
- Reporting BaaS partner concentration without the subcontractor / fourth-party view. The processor, ledger, KYC, and fraud-decision vendor are the four-party pyramid; concentration on a single fourth-party vendor across multiple partners is a recurring committee topic that one-level-deep reporting misses.
- Missing the bank-fintech BSA / AML allocation question. Sponsor banks carry the BSA / AML program responsibility; the pack should be explicit about which entity owns which step (CIP, CDD, BO, transaction monitoring, SAR filing, OFAC screening) and how that allocation is monitored.
- Carrying a generic operational-risk view rather than payments-rail-specific posture. Rail outage, settlement failure, instant-payment fraud, and dispute / chargeback rates are the operative payments lens; the pack carries them by name.
- State-licensing items reported as compliance overhead. License suspension or surety-bond call are material risk events; the pack treats them accordingly.
- §1033 (open banking) and §1071 (small-business data) treated as future-state when they are implementation-active for in-scope entities. The regulatory-horizon section carries the implementation milestones with the verification-flag discipline.
