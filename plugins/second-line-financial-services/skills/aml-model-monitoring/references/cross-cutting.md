# cross-cutting

One section per topic. Read only the sections the scope calls for.

## cyber

### Cyber cross-cutting overlay — aml-model-monitoring

When the scope flags the cyber cross-cutting overlay, load this file. It carries the cyber-typology lens for transaction-monitoring scenario coverage. The overlay is scoped to typologies that surface in transaction monitoring, not to general cyber controls (NYDFS Part 500 program-level, SEC cyber 8-K, cyber-resilience framework reviews) which sit elsewhere.

#### Scope of this overlay

Transaction monitoring is one of the points where cyber-enabled financial crime becomes visible to second-line review. Account takeover, ransomware-payment facilitation, BEC-payout patterns, virtual-currency conversion typologies, and synthetic-identity patterns generate transaction signal that the monitoring system either picks up or misses. The overlay focuses on whether the scenario inventory and the segmentation reflect this typology surface.

#### Anchoring sources

- **OFAC Updated Advisory on Potential Sanctions Risks for Facilitating Ransomware Payments (September 21, 2021)** [verify date and the most recent revision] — sanctions-risk frame for ransomware payments to designated parties; downstream signal that monitoring may surface (large-dollar virtual-currency conversions, third-party-payment patterns paying ransom-related counterparties).
- **FinCEN Advisory FIN-2021-A004 on Ransomware (November 8, 2021)** [verify advisory number and date] — typology indicators for ransomware-related financial activity.
- **FinCEN guidance on virtual-currency-related activity** for money services businesses and convertible-virtual-currency exchangers and administrators (FIN-2019-G001, May 9, 2019, and related) [verify the operative guidance set] — typology indicators and the BSA/AML expectations on VASP-adjacent activity.
- **FinCEN Advisory on BEC and Email Compromise** (FIN-2016-A003 and successor advisories) [verify advisory references] — typology indicators for BEC-driven payment patterns.
- **FinCEN Advisory on synthetic identity fraud and identity-related typologies** [verify the operative advisories].

#### Cyber-driven typologies the monitoring scope addresses

The QA reads whether the scenario inventory and segmentation address:

- **Account takeover (ATO) downstream payment patterns.** Push-payment-out events shortly after a credential-change or device-change signal; rapid drain to external accounts; P2P sends to first-time counterparties; mobile-channel-originated activity diverging from the customer's historical channel. The monitoring system needs the device, channel, and identity-event signal to detect this; the QA reads whether those feeds are integrated.
- **Ransomware-payment facilitation.** Large-dollar virtual-currency conversions; payments to known VASPs around incident dates; third-party-payment-processor patterns around incident windows; rapid funding-and-conversion sequences. The OFAC sanctions-evasion concern is loud: where the firm's monitoring surfaces these patterns, the QA reads whether the screening interlock with `sanctions-screening-qa` is documented.
- **BEC payout patterns.** Inbound wires to first-time business counterparties; rapid distribution to multiple accounts after receipt; correspondent-routed patterns from foreign jurisdictions; mule-account receipt patterns where the firm hosts the mule account.
- **Virtual-currency on-ramp and off-ramp typologies** for customers transacting with VASPs, mixers, or cross-chain bridges. Where the customer base shows VASP transaction patterns, the monitoring scope needs scenario coverage on conversion velocity, counterparty-of-counterparty exposure (where the firm has visibility), and rapid-cash-out sequences.
- **Synthetic-identity patterns.** Shell-customer identifiers (date-of-birth and SSN combinations that do not credential-history), thin-file customers acquiring credit and rapidly drawing cash, identity-cluster patterns (multiple customers sharing device, IP, or address fingerprints).
- **Mule-account receipt-and-forward patterns.** Inbound from one source, outbound to another within a short window, with no economic rationale tied to the customer's profile. Common across ATO, BEC, romance-scam, and government-benefit fraud.

#### Segmentation signal the cyber overlay informs

Cyber-typology coverage benefits when segmentation includes:

- **Channel and device features.** New-device-on-known-account events, device-fingerprint stability, IP geolocation drift, channel-mix changes.
- **Identity-event timeline.** Credential change, contact-info change, beneficiary-link change, payee-add events, and the activity following them.
- **Counterparty-graph features.** First-time counterparty events, shared-counterparty clusters across customers, repeated-counterparty patterns suggestive of mule networks.
- **VASP-counterparty exposure.** Customers with material VASP transaction volume isolated as a segment.

A segmentation that does not include channel, device, or identity-event signal will miss the cyber-typology surface entirely; the QA flags the gap.

#### Findings the cyber overlay surfaces

- Scenario inventory absent ATO, ransomware-facilitation, BEC-payout, or VASP-conversion scenarios where the customer base or transaction history shows the typology surface.
- Device, channel, and identity-event signal feeds not integrated into the monitoring system.
- VASP-counterparty exposure unaddressed in segmentation despite material customer volume.
- Sanctions-screening interlock with the monitoring system undocumented for ransomware-related typologies (cross-link to `sanctions-screening-qa`).
- BTL testing on ATO and BEC scenarios absent or under-sampled.
- Auto-closure rules in payments populations covering ATO-typical alert clusters without documented validation (a common loss point).
- FinCEN advisory coverage gaps — the firm's risk assessment names a typology covered by an active advisory, but the scenario inventory does not address it.

#### Boundaries of this overlay

This overlay is for transaction monitoring's cyber-typology coverage. Cyber controls at the program level (incident response, third-party cyber due diligence, NYDFS Part 500 program review, SEC cyber 8-K disclosure) are out of scope here; sanctions-screening interlock detail lives in `sanctions-screening-qa` and its `references/cross-cutting.md#cyber`; CDD intersection (KYC for VASP-counterparty customers, identity-verification controls) lives at `cdd-risk-review`.

## privacy

### Privacy cross-cutting overlay — aml-model-monitoring

Loads when the scope `cross_cutting_overlay_set` includes `privacy`, or when the monitoring evidence touches transaction-monitoring data, segmentation populations, alert-disposition narratives, or vendor-supplied analytics that carry NPI, PHI (rare but possible in covered-product insurance contexts), or other regulated personal data. Most AML monitoring evidence is regulated personal data on its face; the overlay should be considered the default for any monitoring memo not at public-only source posture.

#### Why privacy belongs in the monitoring memo

Transaction-monitoring data is NPI by definition under GLBA. Customer segmentation cuts on demographic, behavioural, and geographic attributes that interact with state privacy laws. Alert narratives quote customer behaviour and counterparty identity. Vendor-supplied scoring (segmentation engines, network analytics, blockchain analytics for VASP exposure) sits inside a service-provider relationship governed by §314.4(f) of the Safeguards Rule. The monitoring memo cannot assess whether the system is meeting design intent without naming the privacy posture on the data the system runs against, and the memo itself is regulator-readable evidence that needs the right sensitivity and custodian on its rows.

The discipline carries through to second-line work specifically: a memo that quotes alert narratives verbatim, names counterparty identities in the body, or prints segmentation cuts at customer-attribute level is not the artifact the firm wants the next examiner to read alongside the firm's privacy program.

#### Operative anchors

- **GLBA Safeguards Rule, 16 CFR Part 314 (FTC scope) and the interagency Safeguards rule for banks** — §314.4 program elements; §314.4(f) service-provider obligations cover the segmentation engine, scoring vendor, and analytics provider relationships in the monitoring stack; §314.5(d) FTC notification of notification events. Where a vendor in the monitoring stack handles NPI, the diligence chain (`vendor-diligence`) is the upstream artifact; the monitoring memo records the vendor coverage and routes any gap.
- **GLBA Privacy Rule, Regulation P, 12 CFR Part 1016** — privacy-notice and information-sharing posture; relevant where monitoring-data flows into a §314.4(f) service-provider chain or where joint-marketing exceptions to the sharing limits affect what data the monitoring stack consumes.
- **State comprehensive privacy laws** — CCPA / CPRA (California), VCDPA (Virginia), CTDPA (Connecticut), CPA (Colorado), and the rolling list. GLBA-covered data is excluded from many state privacy laws, but the GLBA-exemption scope is read state-by-state, and segmentation cuts that pull on data outside the GLBA-covered scope (publicly-sourced enrichment, vendor-derived attributes, social-graph features) lose the exemption.
- **FCRA, 15 USC §1681 et seq., and Regulation V, 12 CFR Part 1022** — where monitoring scenarios consume consumer-report data or where alert dispositions feed into adverse-action chains, FCRA reach attaches; Reg V §1022.74 risk-score disclosure considerations sit in `adverse-action-review`.
- **HIPAA, 45 CFR Parts 160 and 164** — narrow scope: covered-product insurers running AML monitoring on book-of-business data may surface PHI in narratives. The monitoring memo treats those rows as restricted and routes the BAA chain to the vendor-diligence artifact.
- **NYDFS 23 NYCRR Part 500** — Part 500 is named in the cyber overlay; the privacy overlay cross-references for §500.11 third-party security and §500.13 access controls on data the monitoring stack consumes.
- **FinCEN 314(b) information-sharing safe harbour** — where the monitoring memo quotes inbound 314(b) communications or names counterparties surfaced through 314(b) outreach, the privilege and confidentiality posture is anchored in 31 USC 5311 and the implementing regulation; the memo handles 314(b)-derived content under the firm's 314(b) program controls.
- **OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026 (April 17, 2026)** — joint interagency Revised Guidance on Model Risk Management; the in-perimeter components of the monitoring stack consume regulated personal data, and the validation chain includes the data-handling controls.

#### What changes when privacy is flagged

##### 1. Source-posture and data-class read open the memo

The opening **scope, source posture, and engagement context** section names the data classes the monitoring stack consumes (NPI, FCRA-covered data, third-party enrichment, vendor-derived attributes, BSA-restricted information including SAR-related references, 314(b) inbound) and the privacy posture for each. A memo that asserts findings on segmentation drift without naming whether the segmentation features include enrichment data outside the GLBA-covered scope cannot defend the read. The data-class read is one short paragraph; it sets the privacy frame for the rest of the memo.

##### 2. Segmentation drift gains a privacy-feature read

The segmentation section reads drift on the population-and-behaviour axes and adds a short feature-class read: which features in the segmentation methodology are GLBA-covered, which are publicly-sourced or vendor-derived enrichment, which are inferred (e.g., behavioural archetypes synthesised from raw transaction data). Drift on a publicly-sourced enrichment feature is a different finding from drift on a GLBA-covered feature: the former routes to a vendor / refresh-cadence question, the latter routes to a customer-data-quality question. Where a feature loses GLBA exemption from a state privacy law, the segmentation refresh cycle reads against the state-law refresh expectations, not against the BSA cycle.

##### 3. Vendor coverage in the monitoring stack reconciles to §314.4(f)

The model-identifier-and-inventory-linkage section names the vendors in the stack (segmentation engine, scoring vendor, analytics provider, screening engine) and records whether each vendor's diligence is current under §314.4(f). A vendor not in the diligence cycle is a finding routed to TPRM and to the BSA officer; the monitoring memo does not redo the vendor diligence. Blockchain-analytics vendors and social-graph vendors specifically: address-level enrichment data is regulated personal data under several state regimes even where the wallet-address data alone is not.

##### 4. Alert-volume and productivity sections handle narrative content carefully

Productivity and SAR-conversion figures are population-level numbers. Where the memo cites individual alerts by ID for evidence, the citation is the alert ID and a short typology tag, not the customer name, the counterparty name, or the narrative text. Where a typology pattern needs illustration, the memo redacts to the typology level and points to the case file rather than reproducing the narrative. The monitoring memo is not a SAR; it does not carry SAR-restricted content; it does not name the customer.

##### 5. Threshold-change and BTL workpapers handle test populations

BTL test populations are real customer cohorts. The BTL section names the population scope (size, segmentation cuts), the sampling method, and the evidence pointer; the memo does not enumerate sampled customers or print BTL output rows. A workpaper that prints tested customer IDs is firm-internal evidence with a custodian named in the BTL workpaper, not a memo-body item. The threshold-change governance section handles the change record at programme level; per-change effect figures aggregate across the affected population and do not call out customers.

##### 6. Confidentiality and tipping-off seam with the SAR program

Where the monitoring memo references SAR conversion, the references are aggregated (count, rate per scenario, SAR-conversion ratio) and never identify specific SARs. 31 USC 5318(g)(2)(A) prohibits disclosure of SAR existence outside the permitted chain, and §1020.320(e) (banks) and the parallel provisions for other institutions implement the prohibition. The monitoring memo's per-scenario SAR conversion is permissible because it is aggregated; row-level cross-references back to specific SARs are not.

##### 7. Cross-border data flows and residency

For institutions with cross-border processing (offshore monitoring teams, cloud-hosted analytics in a different region, vendor sub-processors outside the firm's region), the data-flow row carries the residency posture and the cross-border legal basis (intra-group transfer, processor agreement, GLBA carve-out where applicable). A monitoring memo that asserts findings on segmentation drift run in an offshore environment without naming the residency posture is silent on a relevant control.

##### 8. Memo-level handling and custodian

The memo itself is a privacy artifact: it cites alert IDs, typology distributions, and vendor outputs that together can reconstruct customer behaviour. Sensitivity defaults to `confidential` for the memo body and `restricted` for any appendix that quotes alert narratives, BTL output rows, or per-customer evidence. The custodian is a named role (Head of BSA Program, BSA Officer, Head of Financial-Crime Analytics, Head of Model Risk Reporting), not "BSA" as a function.

#### Privacy-tagged additions to the memo

When this overlay loads, the following items appear in the memo:

- A short data-class paragraph in `scope, source posture, and engagement context` naming GLBA-covered, FCRA-covered, third-party enrichment, vendor-derived inferred, BSA-restricted, and 314(b)-derived data classes.
- A feature-class read in the segmentation section distinguishing GLBA-covered features from enrichment and inferred features, with a refresh-cadence note where state privacy laws apply.
- A vendor-coverage row per vendor in the monitoring stack reconciling to the §314.4(f) diligence cycle.
- A residency posture note on cross-border data flows where the monitoring environment is offshore or cloud-hosted in a non-firm-permitted region.
- A custodian and sensitivity classification on the memo-level handling block.

#### Common pitfalls when privacy applies

- Naming customers, counterparties, or quoting alert narratives in the memo body. The monitoring memo cites alert IDs and aggregates, not narrative excerpts.
- Treating segmentation enrichment data as GLBA-covered by default; the GLBA-exemption scope under state privacy laws is feature-by-feature, not blanket.
- Skipping the vendor §314.4(f) coverage check on blockchain-analytics, social-graph, or scoring vendors because the relationship is read as "analytics" rather than "service provider".
- Treating BTL workpapers as memo-body content. BTL output rows live in the workpaper; the memo cites the workpaper.
- Defaulting the memo's sensitivity to `internal` and the custodian to "BSA" as a function.
- Cross-referencing specific SARs from the monitoring memo. Aggregation respects the §5318(g) tipping-off frame; per-SAR cross-reference does not.
- Cross-border processing handled silently; offshore monitoring environments and cross-region cloud deployments are named, not assumed.
