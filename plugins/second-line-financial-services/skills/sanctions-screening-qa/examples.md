# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## list-event-review-regional-bank

### Example: list-event review at a regional bank

Public-source-derived. No named institution. The shape mirrors a standing pattern at regional banks following a hypothetical week of significant new SDN designations: a customer-base full re-scan, a payment-rail re-scan, and the cross-rail consistency-and-cyber-overlay checks that often fall through.

#### Input

- **Institution**: a regional bank with retail, commercial, correspondent, and trade-finance activity. Single-state footprint with a small set of correspondent respondents.
- **Engagement scope supplied**: institution = regional bank; primary regulators = OCC and FRB (per charter; assume OCC for this example); persona = second-line sanctions QA reviewer reporting to the BSA officer with the sanctions officer in the chain; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlays = banking; cross-cutting overlays = cyber (because a portion of the new designations are virtual-currency-adjacent typologies).
- **Review type**: `list_event_review`. Review window: 14 days after the OFAC publication date of the new SDN designations.
- **Evidence pulled**: list-update audit log; full-rescan completion log per system; trade-finance system feed-mapping configuration; cross-rail alert correlation extract; cyber-overlay assessment artifact (or lack thereof); sanctions officer post-event memo to the BSA officer.

#### Output sketch

The skill produces a Word memo (rendered via the `docx` skill). The alert-disposition workbook is light because this is an event review, not a sample QA. Headlines:

- **Sanctions risk posture summary** — list set: OFAC SDN, OFAC SSI, EU Consolidated, UK OFSI Consolidated. Event scope: SDN sweep with 47 new designations including 9 virtual-currency-adjacent designations; effective on the OFAC publication date.
- **List management governance for the event** — full re-scan against new designations completed within 24 hours of OFAC publication for the customer base. One trade-finance system relied on a delta-update batch and did not include a flagged designation type for 36 hours due to a feed mapping gap (the system did not map the "Digital Currency Address" record type from the SDN List). Delta-vs-full reconciliation evidence is current for the deposit and wire systems; absent for the trade-finance system.
- **Screening configuration delta** — no configuration changes during the window. Match-logic and fuzzy thresholds unchanged. Exclusion list re-reviewed against new designations; no exclusion-list entries hit the new designations.
- **Alert disposition QA (event-window only)** — workbook of 23 alerts raised against the new designations across the window. 18 dispositioned as `false_positive_closed` with documented rationale tying to specific list source and identifier mismatch. 4 escalated to the sanctions officer; 1 still pending at the time of QA. Decision-maker independence holds. 50%-rule assessed = `yes` on the 4 escalated alerts; `not_applicable` on the 18 closed alerts; `unknown` on the pending alert (the QA flags this as a documentation gap to close at disposition).
- **50 Percent Rule and sectoral sanctions handling** — methodology in place at program level (signed by the sanctions officer 8 months ago); evidence basis is corporate-registry plus commercial-database; chain-ownership reads documented for the 4 escalated alerts.
- **List-update event reviews**:
  - Event date: [OFAC publication date]. Designation type: SDN-add (mixed natural-person and entity, including 9 virtual-currency-adjacent). Institution response: full re-scan on customer base (24 hours), delta processing on rails (within 6 hours for deposit and wire; 36 hours for trade-finance with the feed-mapping gap). Cross-rail consistency check documented for deposit and wire only; not documented for trade-finance and not documented for card. Cyber-overlay assessment: not performed (the QA finding).
- **Cyber-evasion exposure for the event** — virtual-currency exposure is limited at this institution (no on-ramp / off-ramp activity directly). The 9 virtual-currency-adjacent designations include digital-currency address records on the SDN List; the institution's screening engine does not ingest that record type. Address-level screening is `not-in-place`. Ransomware-payment exposure: limited (no incident-response payment paths in the window). Cyber-identity exposure: limited.
- **Material findings**:
  - `criterion = feed_mapping_completeness`, `framework_component = internal_controls`, severity material. Trade-finance system feed-mapping gap on the Digital Currency Address record type; 36-hour exposure on a flagged designation type.
  - `criterion = cross_rail_consistency`, `framework_component = testing_and_auditing`, severity moderate. Cross-rail consistency check documented for deposit and wire only; trade-finance and card not documented.
  - `criterion = cyber_evasion_exposure_assessment`, `framework_component = risk_assessment`, severity material. No standing cyber-overlay assessment as part of the list-event response process; the 9 virtual-currency-adjacent designations were not assessed for evasion-typology intersection.
  - `criterion = list_event_response_timing`, `framework_component = internal_controls`, severity moderate. Trade-finance 36-hour lag against OFAC publication.
- **Recommended gates**:
  - `feed-mapping-completeness-check-after-list-events` — required reviewer: sanctions officer with operations technology lead concurrence; stop condition: list-event sweep without a documented feed-mapping completeness check across all rails.
  - `cross-rail-consistency-check-artifact` — required reviewer: sanctions officer; stop condition: list-event response without cross-rail consistency artifact.
  - `designation-type-cyber-overlay-assessment` — required reviewer: sanctions officer with reference to `references/cross-cutting.md#cyber`; stop condition: list-event response without a designation-type cyber-overlay assessment when the event includes virtual-currency-adjacent designations.
- **Recommendation**: `process_change_recommendation` with detail covering the three gates above. Cross-references: `aml-model-monitoring` for the trade-finance feed-mapping technical follow-up; vendor-diligence in `vendor-diligence` for the trade-finance system vendor read.
- **Source trace** — anchors to OFAC Framework May 2, 2019 (testing-and-auditing, internal controls, risk assessment), FFIEC OFAC section, OFAC Sanctions Compliance Guidance for the Virtual Currency Industry October 15, 2021 [verify date]. List citations carry date-as-of of the OFAC publication date.
- **Confidence label**: `high` for the documented findings (evidence is the institution's own audit log, completion logs, and feed configuration); `medium` on the cyber-overlay assessment finding because the institution may have an undocumented assessment that did not make it to the file the QA pulled.

#### Why this scenario matters

- **OFAC publication date is the benchmark for response timing**, not the institution's internal publication date. The trade-finance 36-hour lag is measured against OFAC, not against the institution's own delta cycle.
- **Feed-mapping gaps are foundational findings**. A system that does not ingest a designation type from the list source is not just slow; it is silent. The QA reads feed-mapping completeness as a discrete control, not an inference from response time.
- **Cross-rail consistency is part of the post-event sweep**, not a routine control. A customer hit on wire and cleared on ACH within the same window without documentation is the failure mode the cross-rail check catches.
- **The cyber-overlay assessment as a standing list-event step** is the operative read on virtual-currency-adjacent designations. The overlay is not optional when the designation set includes such records.
- **Address-level screening capability is a distinct program element**. The SDN List's Digital Currency Address records require ingestion at the screening engine; name-only screening does not reach them.

#### Anchors

- A Framework for OFAC Compliance Commitments (OFAC, May 2, 2019).
- FFIEC BSA/AML Examination Manual — Office of Foreign Assets Control section.
- OFAC Sanctions Compliance Guidance for the Virtual Currency Industry (October 15, 2021) [verify date].
- OFAC SDN List — Digital Currency Address identifier records.

See `references/source-anchors.md` for full citations, `references/sector-overlays.md#banking` for the bank-specific frame, and `references/cross-cutting.md#cyber` for the evasion-typology overlay and the address-level screening read.

## payments-fintech-enforcement-pattern

### Example: payments-fintech enforcement-pattern QA

Public-source-derived. No named institution. The shape mirrors a standing pattern in resolved OFAC enforcement matters against payments and fintech firms: list-update lag, generic FP rationale documentation, and 50 Percent Rule oversight gaps. The QA reads the firm's program against the OFAC Framework five components and the FFIEC OFAC section; it does not redo the enforcement matter.

#### Input

- **Institution**: a payments fintech operating under a sponsor-bank model with a card program, a wire and ACH rail, and a stablecoin on-ramp / off-ramp.
- **Engagement scope supplied**: institution = fintech (sponsor-bank); primary regulators = OFAC and the sponsor bank's primary federal regulator (FDIC for this example); persona = second-line sanctions QA reviewer; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlays = payments-fintech; cross-cutting overlays = cyber.
- **Review type**: periodic sample QA over a 12-month window across two payment rails (wire, ACH) and the on-ramp / off-ramp activity. Sample of 100 alert dispositions stratified by rail and list source.
- **Evidence pulled**: list-management runbook; list-update audit log against OFAC publication dates; screening-engine configuration export; fuzzy-threshold calibration memo; alert-disposition workpapers; 50 Percent Rule methodology document (or lack thereof); blockchain-analytics vendor evidence; sponsor-bank handoff package and re-attestation log.

#### Output sketch

The skill produces a Word memo (rendered via the `docx` skill) plus an Excel alert-disposition workbook (rendered via the `xlsx` skill) for the 100-alert sample. Headlines:

- **Sanctions risk posture summary** — list set: OFAC SDN, OFAC SSI, EU Consolidated, UK OFSI Consolidated; on-ramp / off-ramp activity carries virtual-currency exposure; sponsor-bank program agreement allocates screening responsibility (fintech detects; sponsor bank reviews and decides).
- **List management governance** — documented update cadence is "intra-day on OFAC publication". Audit log evidence shows lag of 2 to 5 business days for delta updates against OFAC publication date in 12% of in-window updates. Delta-vs-full reconciliation evidence is partial; full re-scans run weekly with no documented control preventing dropped designations between full cycles. Feed-mapping completeness: gap_identified — virtual-currency address designations from the SDN List's identifier records are not ingested into the screening engine.
- **Screening configuration** — match-logic summary: vendor edit-distance algorithm with phonetic supplement; fuzzy threshold set at 0.75 (vendor recommendation, last calibrated 18 months ago); exclusion list has 137 entries with no documented owner, refresh cadence, or re-review evidence.
- **Alert disposition QA (alert-by-alert)** — workbook of 100 alerts. FP-rationale documentation is generic ("reviewed, not a match"; "false positive") in 30 of 100 sampled dispositions. Decision-maker independence holds (relationship owners do not dispose). 50%-rule assessed = `no` on 18 alerts where the alert touched ownership / control of a designated person.
- **50 Percent Rule and sectoral sanctions handling** — aggregation methodology not documented at program level; aggregation handled case-by-case at analyst discretion. SSI handling collapsed into SDN-style blocking for 6 of 7 sampled SSI hits; directive-specific tenor logic not applied.
- **List-update event reviews** — three material events in the window (an SDN sweep, an SSI directive change, a virtual-currency mixer designation). Response-timing-vs-OFAC-publication: 24 hours, 36 hours, 9 days respectively. Cross-rail consistency check documented for the first event only. Cyber-overlay assessment performed for the mixer designation but not for the SDN sweep.
- **Cyber-evasion exposure** — virtual-currency exposure: material. Address-level screening not in place against OFAC-designated addresses; analytics-vendor outputs run in a parallel pipeline and feed disposition narrative but do not generate alerts. Ransomware-payment exposure: limited (no documented incident-response payment paths); pre-payment OFAC analysis playbook exists but is policy-only with no test evidence. Cyber-identity exposure: limited; IDV-to-screening pipeline carries name-and-DOB only with no anomaly-or-confidence signal.
- **Material findings**:
  - `criterion = list_update_timeliness`, `framework_component = internal_controls`, severity material. Lag of 2 to 5 business days against OFAC publication in 12% of in-window updates; the OFAC publication date is the benchmark.
  - `criterion = feed_mapping_completeness`, `framework_component = internal_controls`, severity material. Virtual-currency address-level designations not ingested.
  - `criterion = fp_rationale_documentation`, `framework_component = testing_and_auditing`, severity material. 30% of sampled dispositions carry generic rationale; tuning evidence becomes impossible.
  - `criterion = fifty_percent_rule_methodology`, `framework_component = internal_controls`, severity material. No program-level methodology; analyst-discretion handling.
  - `criterion = ssi_distinct_handling`, `framework_component = internal_controls`, severity moderate. Sectoral collapsed into SDN-style; directive-specific tenor logic missing.
  - `criterion = address_level_screening` (cyber overlay → `cyber_evasion_exposure_assessment`), `framework_component = internal_controls`, severity material. Mixer-address designations not screened.
  - `criterion = exclusion_list_governance`, `framework_component = internal_controls`, severity moderate. 137-entry exclusion list with no documented owner, refresh cadence, or re-review evidence.
- **Recommended gates**:
  - `list-update-SLA-evidence` — required reviewer: sanctions officer; stop condition: list deployed without delta-vs-full reconciliation evidence.
  - `fp-rationale-documentation-standard` — required reviewer: sanctions officer; stop condition: disposition closed without rationale category from the documented taxonomy.
  - `fifty-percent-rule-methodology-program-level` — required reviewer: sanctions officer with sanctions-counsel concurrence.
  - `address-level-screening-implementation` — required reviewer: sanctions officer with model-risk reviewer concurrence (cross-reference `aml-model-monitoring`).
  - `exclusion-list-attestation` — required reviewer: sanctions officer; refresh cadence and re-review evidence required.
- **Recommendation**: `escalate_to_sanctions_officer` with detail covering list-management remediation, FP-rationale taxonomy, 50 Percent Rule methodology, and address-level screening capability. The QA does not direct match-or-no-match decisions on any specific alert, and does not direct the sanctions officer's filing of blocking or rejection reports on the at-issue alerts.
- **Source trace** — anchors to OFAC Framework May 2, 2019 (five components), 50 Percent Rule guidance August 13, 2014 [verify date], FFIEC OFAC section, OFAC Sanctions Compliance Guidance for the Virtual Currency Industry October 15, 2021 [verify date]. List citations carry date-as-of.
- **Confidence label**: `high` for the documented findings (evidence is the firm's own audit log, configuration export, disposition workpapers); `medium` on the cyber-evasion typology read because parts of the analytics-vendor evidence are vendor outputs.

#### Why this scenario matters

- **The QA tests program evidence, not match decisions**. The findings are about list-management timeliness, configuration documentation, FP-rationale taxonomy, and methodology gaps. The QA does not propose that any specific at-issue alert should have closed differently or that the sanctions officer should have filed differently. That separation is what the skill enforces.
- **OFAC publication date is the benchmark for list timeliness**, not the institution's internal publication date. This is the most-common misframe.
- **Generic FP rationale documentation is itself a finding**. Without a rationale taxonomy, tuning evidence is impossible and the program cannot show its work to an examiner.
- **50 Percent Rule oversight gaps are program-level**. Analyst-discretion handling of multi-owner aggregation does not satisfy the rule; the program-level methodology has to be documented and signed.
- **The cyber overlay is sanctions-evasion-specific**, not generic cyber controls. Address-level screening against OFAC-designated wallet addresses is a discrete and citable obligation.

#### Anchors

- A Framework for OFAC Compliance Commitments (OFAC, May 2, 2019) — five components.
- OFAC 50 Percent Rule Revised Guidance (August 13, 2014) [verify date].
- FFIEC BSA/AML Examination Manual — Office of Foreign Assets Control section.
- OFAC Sanctions Compliance Guidance for the Virtual Currency Industry (October 15, 2021) [verify date].
- OFAC Updated Advisory on Potential Sanctions Risks for Facilitating Ransomware Payments (September 21, 2021) [verify date].

See `references/source-anchors.md` for full citations, `references/sector-overlays.md#payments-fintech` for the rail-specific reads, and `references/cross-cutting.md#cyber` for the evasion-typology overlay.

## troubleshooting

### Troubleshooting: sanctions-screening-qa

Recurring pitfalls. Read before producing the QA artifact and again before sign-off.

#### Scope discipline

##### Drifting into the match-or-no-match decision

The QA produces findings, gaps, and recommendations against the sanctions program evidence. It does not direct whether to release, block, reject, or report a transaction or relationship. Match decisions and OFAC reporting are regulated acts reserved to the sanctions officer (and the firm's escalation chain). The skill outputs `recommendation`, not `decision`. A QA artifact that says "the alert at row 47 should have been blocked" or "this customer should be reported" has misread its scope.

##### Reviewing the screening-engine model instead of program evidence

Whether the screening engine is well-tuned (precision, recall, BTL testing, threshold calibration) belongs in `aml-model-monitoring`. Whether the program evidence shows defensible work belongs here. The QA cross-references model-monitoring; it does not absorb tuning analysis.

##### Treating CDD or BO posture as in-scope

Customer beneficial-ownership work belongs in `cdd-risk-review`. The screening QA can flag a 50 Percent Rule aggregation gap that depends on BO evidence and cross-reference; it does not handle the BO refresh itself.

#### List-management discipline

##### Measuring list-update timeliness against the institution's internal publication

The OFAC publication date is the benchmark, not the institution's internal publication. A program that publishes internally 4 hours after OFAC and reports "0-hour lag" against its own publication has measured the wrong thing. The QA reads timing against OFAC publication.

##### Reading delta-update cadence without reading delta-vs-full reconciliation

A program can be fast on deltas and still drop designations between full re-scan cycles. The QA reads both the delta cadence and the reconciliation evidence; either alone is insufficient.

##### Treating feed-mapping completeness as inferred from response time

A system that does not ingest a designation type (e.g., the SDN List's Digital Currency Address records) is silent on that designation type, not slow. The QA reads feed-mapping completeness as a discrete control, not an inference from observed response time.

##### Missing list-as-of dates on every list citation in the artifact

OFAC lists move. Any sanctions QA artifact that does not date its list citations cannot be relied on after the next list update. Every list reference in the artifact carries a `date_as_of`.

#### Screening-configuration discipline

##### Match logic and fuzzy thresholds not papered

The reviewer cannot reproduce why a specific score crossed or did not cross threshold without configuration documentation. The `screening_configuration` field forces structured documentation; an undocumented configuration is a `match_logic_documentation` finding.

##### Exclusion lists / good-guy lists treated as operationally invisible

An undocumented exclusion list with no owner, refresh cadence, or re-review evidence is a material `exclusion_list_governance` finding. Exclusion lists are control instruments and have to be governed as such.

##### Fuzzy threshold set on vendor recommendation alone, no calibration

A fuzzy threshold inherited from the vendor without institution-specific calibration (BTL testing, false-positive-rate analysis, false-negative-rate analysis on a labelled sample) is a `fuzzy_threshold_calibration` finding. Vendor recommendations are starting points, not endpoints.

#### Disposition discipline

##### Generic FP rationale documented at the disposition level

"Reviewed, not a match" or "false positive" without a category from the documented rationale taxonomy is the most-common finding in alert-disposition QA. Without a taxonomy, tuning evidence is impossible. Set `fp_rationale_category` to `generic-or-boilerplate` and surface as a finding.

##### Decision-maker independence not evidenced

Where the relationship owner can dispose of a sanctions alert on a customer they own, structural independence has been broken. The QA reads `decision_maker_role` against the relationship-owner role for each sampled alert.

##### 50 Percent Rule applied case-by-case at analyst discretion

Aggregate ownership across multiple blocked persons is missed when the program has no documented aggregation methodology. The methodology has to be documented at program level and signed by the sanctions officer; analyst-discretion handling is a `fifty_percent_rule_methodology` finding.

##### SSI and other sectoral programs collapsed into SDN-style blocking

Sectoral and restriction programs carry directive-specific prohibitions (debt / equity tenor restrictions, restricted-securities handling, prohibited service categories) that are not the same as SDN blocking. A program that treats SSI hits like SDN hits has missed the directive-specific limb.

#### List-event response discipline

##### No standing cyber-overlay assessment for designation types that intersect virtual currency

When the event includes virtual-currency-adjacent designations (mixer-address adds, virtual-currency-related typology adds), the cyber overlay engages as a standing list-event step. A program that runs the customer sweep and the rail re-scan but skips the designation-type cyber-overlay assessment misses the dominant evasion typology of the last several years.

##### Cross-rail consistency check not documented

A customer that hits on wire and clears on ACH within the same window without documented investigation is the failure mode the cross-rail check catches. Cross-rail consistency is part of the post-event sweep, not a routine control.

##### Post-event customer-base sweep documented but post-event payment-rail re-scan missing

In-flight transactions against a new designation are the exposure. A bank that sweeps the customer base and not the payment rails has missed in-flight activity.

#### Cyber-evasion overlay discipline

##### Treating mixer-address designations as a name-match exercise

The SDN List's Digital Currency Address identifier records require ingestion at the screening engine for address-level screening. Name-only screening does not reach mixer-address designations. The QA reads `address_level_screening_capability_status` discretely.

##### Reading the analytics-vendor output as a primary source

Blockchain-analytics-vendor outputs are vendor outputs. Cite the vendor in the source trace and route vendor-diligence to `vendor-diligence`. Treating the vendor's clustering or attribution as primary evidence collapses the source-tier and inflates the QA's confidence.

##### Pre-payment OFAC analysis on ransomware-payment paths is policy-only

A program with a pre-payment-analysis policy and no test evidence (no example case showing the analysis actually happens before payment) carries the strict-liability exposure articulated in the OFAC ransomware advisory. The QA reads test evidence, not policy text.

##### Sanctions-officer routing missing on cyber-payment paths

Treasury or operations teams making time-pressure incident-response payments without sanctions-officer routing is the failure mode. The QA reads routing evidence at the case level, not the program-level statement.

##### Importing generic cyber-controls language into the sanctions-screening QA

NYDFS Part 500 program-level controls and SEC cyber 8-K disclosure are not in scope here; they sit elsewhere in the repo. The cyber overlay on this skill is tight to evasion typologies anchored in OFAC and FinCEN material.

#### Sector-specific pitfalls

##### Importing the FFIEC bank-flavoured frame to a BD or fund

The FFIEC OFAC section informs but does not bind BDs and funds. SEC and FINRA examiners are the primary audience. The QA reads against the firm's WSPs (FINRA Rule 3110) and the fund's compliance program (Rule 38a-1).

##### Scoping insurance sanctions screening to covered products only

The insurer's BSA / SAR program operates against covered products only. The OFAC obligation does not stop at covered products; OFAC reaches every US person across all lines. A program that scopes sanctions screening to covered products only has a foundational finding.

##### Reading payments-fintech screening as if the fintech were the obligor

Where the sponsor-bank program agreement allocates screening responsibility, the QA reads the allocation. Reviewing the fintech as if it were the sole obligor (or as if the bank's read were sufficient on its own) misses the dual read the program agreement requires.

##### Restricted-securities-list compliance treated as a customer-screen exercise

Lists like NS-CMIC carry transaction-level prohibitions on the security itself. The QA reads whether the order-management system applies a security-level block, not just whether the customer name screened clean.

#### Output discipline

##### Citing without sections

Every regulator citation in the QA carries a section reference or a `[verify section]` placeholder in the source-anchors file. URL alone fails the source-anchor depth check. Use `references/source-anchors.md` for the canonical citation set; do not restate excerpts in the artifact body.

##### Marking unsupported claims silently

Use `[evidence needed]` explicitly. An inferred claim presented as evidenced is the failure mode.

##### Closing with too much certainty

The confidence label is `high` only when the source posture, the evidence set, and the QA criteria all line up. `medium` and `low` are normal for early-stage QA work on a program where firm policy has not yet papered every control. A `high` confidence label on a QA reviewing a program with material findings is incoherent.

##### Missing date-as-of on list citations

Repeat from list-management discipline above because it is the most-common output defect: every OFAC list citation in the artifact carries a date-as-of.
