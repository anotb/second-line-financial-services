# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for kri-commentary

When the scope record flags `banking`, this overlay sets the KRI-commentary content for banks. It does not replace the SKILL.md workflow; it loads on top of it.

Loaded by: `kri-commentary/SKILL.md` when `scope.sector_overlay_set` includes `banking`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- 12 CFR Part 30 Appendix D (OCC Heightened Standards), Section III (Risk Appetite Statement). The KRI commentary is the running record of how the firm tracks against the RAS; `linked_ras_metric_id` is the load-bearing link.
- FRB SR 12-17 (Consolidated Supervision Framework for Large Financial Institutions, December 2012) and FRB SR 19-3 (Large Financial Institution Rating System); the KRI population the committee sees should reflect the rated-component frame.
- FRB SR 95-51 (Rating the Adequacy of Risk Management Processes), four-element framing (board oversight, policies and limits, risk monitoring and MIS, internal controls). The KRI commentary implicitly demonstrates the third element.
- FFIEC IT Examination Handbook (Information Security; Cybersecurity; Operations) for KRI examples in cyber and operational risk.
- For CCAR / DFAST cycle work: FRB SR 15-18 (capital planning) and the CCAR / DFAST instructions for the cycle. KRI commentary during a stress-test cycle carries forward the projected drift on key metrics.

#### What changes for banking-flagged KRI commentary

##### 1. RAS linkage is required, not optional

For Heightened Standards covered banks, every KRI block carries `linked_ras_metric_id` as required, not optional. A KRI without a RAS linkage (or with an explicit "no-link" rationale) is unfinished; the committee pack carries the RAS-status table that consumes this linkage. The link goes both ways: the KRI block names the RAS metric; the committee-pack RAS-status row points back to the KRI block.

##### 2. Operational-risk KRIs dominate the population

Most committee-pack KRI populations at banks are operational-risk-heavy: external fraud, internal fraud, execution-and-process loss events, business disruption, employment-practices, clients-products-business-practices, damage to physical assets. The Basel revised principles for the sound management of operational risk (March 2021) sets the taxonomy that `risk_subtype` should align to. The commentary on operational KRIs is the bulk of the block-writing time.

##### 3. CCAR / DFAST cycle posture

During a stress-test cycle, the KRI population the committee sees often includes the projected stress-driven drift on key metrics. Block commentary in a stress-test cycle:

- Names the stress scenario (severely adverse, alternative severe, firm-developed) where the KRI is being projected.
- Carries the projected breach trajectory and the assumed management actions (or absence thereof).
- Carries a `data_confidence_note` for KRIs where the stress projection rests on model output rather than realized data.

##### 4. Cyber and AI KRIs

For NYDFS-licensed bank subsidiaries, cyber KRIs commonly include security-awareness (phishing-test click-through rate), patching cadence, mean time to detect / respond, and CISO-program-maturity self-rating. The cyber overlay (`references/cross-cutting.md#cyber`) loads alongside the banking overlay when the scope flags both.

For AI-enabled processes, model-risk KRIs (model performance drift, fairness metrics, override rates, governance approvals overdue) are increasingly common. The deeper model-risk material lives in `ai-governance-model-risk`; the KRI commentary carries the metric-level commentary and references the upstream owner.

##### 5. Issue-log linkage

For banks under Heightened Standards or under FRB consolidated supervision, KRIs often share root causes with open MRAs, MRIAs, audit findings, or regulatory exam findings. The block's `linked_issue_ids` array picks up these foreign keys; the committee pack's issues section consumes the same IDs. Restating issue text in the block fails the no-repetition discipline.

#### Banking-specific output additions

- `linked_ras_metric_id` upgraded to required (not optional).
- `risk_subtype` populated against the firm's operational-risk taxonomy aligned to the Basel revised principles (March 2021).
- `data_confidence_note` populated for stress-cycle projections where the KRI value rests on model output.

#### Common pitfalls in banking-flagged KRI commentary

- KRI block omitting the `linked_ras_metric_id`. For Heightened Standards covered banks the linkage is required.
- Operational-risk KRI commentary that conflates loss events with control failures. The Basel taxonomy distinguishes the two; the commentary should follow.
- Stress-cycle KRI projection treated as a realized value. Projected metrics carry the stress-scenario tag and a data-confidence note; the committee pack must read the projection as a projection, not as outturn.
- Issue-log items restated in the KRI block. The block uses the foreign key; the issue text lives in the issue log and the committee-pack issues section.

## capital-markets

### Capital-markets sector overlay for kri-commentary

When the scope record flags `capital-markets`, this overlay sets the KRI-commentary content for broker-dealers, registered investment advisers, fund complexes, and prime-brokerage / market-maker firms.

Loaded by: `kri-commentary/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- FINRA Rule 3110 (Supervision) and Rule 3120 (Supervisory Control System) for broker-dealer supervisory KRIs (trade surveillance alerts by type, customer-complaint volume, registered-representative attrition with open complaints).
- SEC Rule 15c3-1 (net capital) and Rule 15c3-3 (customer protection) for broker-dealer regulatory-capital and reserve-formula KRIs.
- SEC Market Access Rule 15c3-5 for KRIs on pre-trade risk controls (capital and credit limits, erroneous-order rejections, market-access controls effectiveness).
- For investment advisers: Investment Advisers Act §206 (anti-fraud) and Rule 206(4)-7 (compliance program); Form ADV disclosure-related KRIs; trading-error KRIs.
- For fund complexes: Investment Company Act §38(a) (compliance program) under Rule 38a-1, fund-board reporting KRIs (compliance violations, NAV errors, dilution events).
- For market-makers and prime brokers: liquidity-coverage and intraday-liquidity KRIs; concentration KRIs on prime-brokerage clients.

#### What changes for capital-markets-flagged KRI commentary

##### 1. Firm-level versus fund-level scope

For adviser-firm KRIs, the audience is the firm's risk committee (or equivalent management committee). For fund-level KRIs (NAV errors, compliance violations, distribution-related KRIs), the audience is the fund board (Rule 38a-1 reporting). Conflating firm-level and fund-level blocks is a recurring defect; the block names the entity scope and the receiving committee explicitly.

The committee pack at the adviser firm (per `risk-committee-pack`) is the firm-level enterprise view; fund-level reporting flows separately to fund boards. KRIs that materially affect both surface in both with cross-link, not collapse.

##### 2. Trade surveillance and customer-complaint KRIs

For broker-dealers, trade-surveillance alert KRIs (volume by alert type, alert-to-disposition cycle time, false-positive rate) and customer-complaint KRIs (complaint volume by theme, complaint-to-disposition cycle time, repeat-complaint rate) are FINRA Rule 3110 expectations. The commentary names the disposition cohort (open / closed / referred to enforcement / SAR-filed where relevant) and the disposition timeliness; counts alone are insufficient.

##### 3. Net-capital and reserve-formula KRIs

For broker-dealers, net-capital and Rule 15c3-3 reserve-formula KRIs are continuous-monitoring metrics. Breach commentary on these is regulator-attention-grade; the block carries:

- Specific basis for the breach (e.g., concentration deduction, haircut change, customer-asset reclassification).
- Notification status (Rule 17a-11 early-warning notices to FINRA / SEC).
- Remediation status (capital injection, position reduction, customer-asset reclassification reversal).

##### 4. Trading-error and operational KRIs at advisers

For RIAs, trading-error KRIs (error rate per million orders, error-cost-to-AUM ratio) and operational KRIs (NAV-error rate, custody-reconciliation breaks) commonly appear. The block carries the fiduciary-duty implication for trading errors that affect client returns and the corrective-action posture (client make-whole status).

##### 5. Concentration KRIs for prime brokers

Prime-brokerage and market-maker KRIs on client concentration, financing-mismatch, and intraday-liquidity carry an enterprise-risk implication. The block carries:

- Top-N client concentration with current headroom.
- Financing-tenor mismatch summary.
- Intraday-liquidity peak-usage versus available headroom.

#### Capital-markets-specific output additions

- `risk_subtype` populated against the firm's broker-dealer or adviser taxonomy.
- Wrapper-level entity-scope field where the engagement covers both firm-level and fund-level KRIs.
- `linked_material_event_ids` populated for trading errors, NAV errors, and net-capital breaches that meet the firm threshold for material-event reporting.

#### Common pitfalls in capital-markets-flagged KRI commentary

- Firm-level and fund-level KRIs collapsed into one block. Separate blocks; name the entity scope and the receiving committee.
- Trade-surveillance KRI commentary that reports counts without disposition cohorts. The Rule 3110 expectation is on supervision quality, not alert volume.
- Net-capital breach commentary without the Rule 17a-11 notification status. Examiners read for the notification status by name.
- Trading-error KRI commentary without the fiduciary-duty implication and client make-whole status. For RIAs the client-impact lens is binding.
- Prime-brokerage concentration KRI commentary without top-N detail and headroom. Aggregate concentration figures alone are insufficient.

## insurance

### Insurance sector overlay for kri-commentary

When the scope record flags `insurance`, this overlay sets the KRI-commentary content for insurers and insurance groups.

Loaded by: `kri-commentary/SKILL.md` when `scope.sector_overlay_set` includes `insurance`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505) and the ORSA Guidance Manual, Sections 1 (Description of the Insurer's Risk Management Framework), 2 (Insurer's Assessment of Risk Exposure), and 3 (Group Risk Capital and Prospective Solvency Assessment). KRI commentary on capital-adequacy, solvency, and key risk metrics rolls into the ORSA Summary Report Section 2.
- NAIC Insurance Data Security Model Law (Model #668) for state-licensed insurers; cyber KRIs.
- IAIS Insurance Core Principles (ICP) 16 (Enterprise Risk Management for Solvency Purposes) for international and group-supervised insurers.
- State DOI conduct supervision frames (market-conduct examinations) for conduct-KRI commentary; varies state by state.
- For property and casualty: catastrophe-loss KRIs run on the firm's catastrophe model output; the KRI is a model-output KRI and carries a model-risk caveat.
- For life: actuarial assumption KRIs (lapse, mortality, morbidity) often surface here; commentary references the firm's actuarial valuation cycle.

#### What changes for insurance-flagged KRI commentary

##### 1. ORSA roll-up

The KRI commentary set is consumed by the ORSA Summary Report Section 2 (insurer's assessment of risk exposure). The block-writing voice is the same; the consumer is different. A separate field in the wrapper or in the scope record names the receiving artifact (committee pack, ORSA Summary Report, both). Where the same block reads into both, the source-trace and confidence-label discipline is the binding constraint.

##### 2. Risk taxonomy

Insurance risk taxonomies typically include underwriting (P&C, life, health), market and credit, liquidity, operational, group risk, and (for groups) intra-group risk. The `risk_type` enum in the schema covers most; `risk_subtype` carries the taxonomy detail (e.g., "underwriting-pricing-adequacy", "underwriting-reserve-adequacy", "catastrophe-aggregation"). Where the firm uses an industry-specific taxonomy, the firm-overlay file maps the firm taxonomy onto the schema enum.

##### 3. Catastrophe and actuarial KRIs

Catastrophe-loss KRIs (e.g., 1-in-100 modelled annual aggregate loss) and actuarial assumption KRIs (e.g., lapse rate vs. assumed) are model-output KRIs in the sense that the value depends on model parameters. The block carries:

- The model identifier and model owner (cross-link to the model-risk inventory).
- A `data_confidence_note` describing the model-driven nature of the metric and the model-validation status.
- `contributing_factors` includes `model-driver` where the metric movement is materially driven by model recalibration rather than experience.

##### 4. Group versus solo KRIs

For insurance groups, KRIs at the group level (group SCR, group capital adequacy) and at the solo entity level (solo SCR, solo capital adequacy, lead-state regulatory metrics) need separate blocks. Conflating them is a common defect; block IDs name the entity scope explicitly.

##### 5. Conduct KRIs

For state-conduct-supervised lines, conduct KRIs (complaint volume by theme, claims-handling timeliness, replacement activity for life) carry a heavier audience expectation: the conduct supervisor, the line-of-business committee, and the enterprise risk committee may all consume the same KRI. The block names the audience and the source posture explicitly.

#### Insurance-specific output additions

- `risk_subtype` populated against the firm's insurance risk taxonomy.
- `data_confidence_note` populated for catastrophe and actuarial KRIs that rest on model output.
- Wrapper-level "receiving artifact" field where the engagement is dual-purpose (committee pack + ORSA).

#### Common pitfalls in insurance-flagged KRI commentary

- Group and solo metrics conflated in one block. Separate blocks; name the entity scope.
- Catastrophe-loss KRI treated as a realized number. The model-driven nature and validation status belong in the data-confidence note.
- Actuarial assumption movement attributed to "experience" without distinguishing experience from assumption recalibration. The contributing-factors enum disambiguates.
- ORSA Summary Report Section 2 consumed verbatim from the committee-pack KRI block. The two artifacts share the underlying source posture but write to different audiences; the second-line lead reviews each consumer separately.

## payments-fintech

### Payments-fintech sector overlay for kri-commentary

When the scope record flags `payments-fintech`, this overlay sets the KRI-commentary content for payments processors, money-services businesses, fintech-bank partnerships (BaaS), and non-bank payment service providers.

Loaded by: `kri-commentary/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- OCC Bulletin 2020-10 and the interagency third-party risk management guidance (June 2023) for bank-fintech relationships and bank-partner program KRIs.
- OCC, FRB, FDIC joint guidance on third-party risk management (2023) for monitoring KRIs on third-party providers, especially for BaaS bank partners.
- CFPB supervisory expectations for consumer-protection KRIs in the payments / digital-banking context (e.g., Reg E unauthorized-transaction KRIs, error-resolution timeliness, complaint volume).
- FinCEN BSA / AML KRI expectations: SAR filing volume and timeliness, CTR filing accuracy, transaction-monitoring alert disposition KRIs.
- Network operator (Visa, Mastercard, ACH operator) chargeback and exception KRIs; while not regulator-issued, these are commonly carried in committee packs.
- For state-licensed money transmitters: state-by-state operating expectations and the Conference of State Bank Supervisors' Money Transmitter Modernization Act framework; varies materially by state.

#### What changes for payments-fintech-flagged KRI commentary

##### 1. Bank-partner BaaS KRIs

For BaaS programs, the KRI population the committee or BaaS oversight committee sees commonly includes:

- Program-level transaction volume and concentration on individual BaaS clients.
- Sponsor-bank exposure to BaaS-client failure (operational, reputational, prudential).
- BaaS-client onboarding and monitoring KRIs (unmitigated risk-rating distribution, time-since-last-review, open-issue load).
- BaaS-client complaint and dispute KRIs.

Block commentary names the sponsor-bank role and the BaaS-client role explicitly. For sponsor banks, the committee pack often consumes a roll-up of the BaaS-client KRI population (top-N concentration, watch-list count, exited-relationship summary). For the BaaS client, the committee pack consumes the KRI commentary that flows back from the sponsor.

##### 2. Consumer-protection KRIs

For consumer-facing payments and digital-banking firms, Reg E KRIs (unauthorized-transaction claim volume, provisional-credit timeliness, error-resolution timeliness) and complaint KRIs are CFPB-attention metrics. Block commentary names:

- The Reg E timing benchmark (10 business days for provisional credit; 45-90 days for resolution).
- The current performance against the timing benchmark.
- The disposition cohort and any patterns by channel, product, or customer segment.

##### 3. BSA / AML KRIs

For payments and money-services firms, BSA / AML KRIs (alert volume by typology, alert-to-disposition cycle time, SAR-filing timeliness, CTR-filing accuracy) are continuous-monitoring metrics. Block commentary names the typology mix (driver of the alert volume), the disposition cycle time, and the SAR-filing timeliness against the 30-day default deadline. Where the alert population is materially affected by a model recalibration (transaction-monitoring rule change, scenario tuning), the contributing-factors enum picks up `model-driver` and the data-confidence note carries the model context.

##### 4. Network-operator chargeback and exception KRIs

Card-network chargeback rate, ACH return rate, and other network-operator exception metrics carry network-imposed thresholds (above which the operator imposes monitoring or restrictions). Block commentary names:

- The network-operator threshold and current headroom.
- The chargeback-reason distribution.
- The first-line exception-management posture and any remediation in flight.

##### 5. Concentration KRIs

For payments processors, concentration on a single sponsor bank, a single BaaS client, a single network operator, or a single rail (card, ACH, wire, RTP) is an enterprise-risk metric. The block carries top-N concentration, headroom against any internal or contractual threshold, and the diversification trajectory.

#### Payments-fintech-specific output additions

- `risk_subtype` populated against the firm's payments / fintech taxonomy.
- Wrapper-level role-scope field (sponsor-bank role versus BaaS-client role).
- `linked_material_event_ids` populated for chargeback-rate breaches that trip a network-operator monitoring threshold and for BSA / AML model-recalibration events that materially shifted alert volume.

#### Common pitfalls in payments-fintech-flagged KRI commentary

- BaaS KRIs reported without sponsor / client scope distinction. For a sponsor-bank committee, the roll-up; for the BaaS client, the firm-level view; conflation fails both audiences.
- Reg E KRI commentary that reports volumes without the timing-benchmark performance. The CFPB lens is on timing and substance.
- BSA / AML alert volume reported without disposition cycle time and SAR-timeliness. Counts alone do not demonstrate program effectiveness.
- Chargeback-rate KRI without the network-operator threshold context. Headroom matters; absolute rate alone is insufficient.
- Concentration KRI without top-N detail and headroom. Aggregate figures alone are insufficient.
- Money-transmitter KRIs reported as a single national metric where the state-by-state variation is material. State-level breakdown belongs in the block where the firm's licence portfolio warrants.
