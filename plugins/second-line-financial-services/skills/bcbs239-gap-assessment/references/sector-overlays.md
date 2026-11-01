# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for bcbs239-gap-assessment

When the scope record names sector `banking`, this overlay adds banking-specific fields and review demands to the assessment. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-sector elements.

Loaded by: `bcbs239-gap-assessment/SKILL.md` when `scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, bank holding company, foreign banking organization with US operations).

BCBS 239 is the banking-anchored regime. This overlay is the primary one for the skill; it does the substantive work and the other sector overlays are lighter.

#### Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

#### What changes for banking BCBS 239 assessments

##### 1. Binding for G-SIBs and operative for D-SIBs / large LFIs

BCBS 239 binds G-SIBs by Basel Committee designation and reaches D-SIBs through national-supervisor adoption with a three-year implementation window from designation. In the United States, the operative supervisory expectations flow through FRB SR 12-17 (Consolidated Supervision Framework for LFIs), the OCC Heightened Standards (12 CFR Part 30 Appendix D) for OCC-supervised covered banks, and FRB horizontal-review practice on RDARR.

Assessment-side implications:

- For a US G-SIB, all fourteen principles are in scope at the consolidated level; the rating uses the BCBS vocabulary and is the artifact a horizontal-review team will read.
- For a US D-SIB or LFI under SR 12-17, the assessment is operative even where the firm is not a G-SIB; the FRB expectation chain and the OCC Heightened Standards (where applicable) supply the prudential reach.
- For a foreign banking organization, the parent's home-supervisor BCBS 239 posture is the consolidated frame; the US operations carry SR 12-17 and (where the IHC crosses thresholds) Heightened Standards expectations independently.
- For a community or regional bank below the SR 12-17 / Heightened Standards thresholds, BCBS 239 is best-practice rather than binding; assessments at this scale are typically scoped to risk-data layer maturity rather than full fourteen-principle ratings.

##### 2. FRB tailoring framework interaction

The FRB's tailoring framework (Categories I-IV under the 2019 final rule) sets prudential standards including capital, liquidity, stress-testing, and risk-management expectations by category. BCBS 239 expectations interact with the tailoring categories: Category I and II firms carry the heaviest BCBS 239 expectations (CCAR, daily liquidity reporting, FR 2052a granularity); Category III firms carry intermediate expectations (DFAST, less granular liquidity reporting); Category IV firms carry lighter expectations.

The assessment's supervisory-context block names the firm's tailoring category. The Principle 5 (timeliness) and Principle 6 (adaptability) ratings are read against the granularity and frequency expectations of the firm's category, not against a uniform G-SIB benchmark.

##### 3. OCC Heightened Standards extension

For OCC-supervised covered banks, 12 CFR Part 30 Appendix D §II (Risk Governance Framework) [verify section labels] sets independent risk management, board composition and oversight, risk-appetite statements, and supporting infrastructure expectations. The risk-data infrastructure that supports the risk-appetite statement and the risk reporting that flows to the board sits inside §II and connects to BCBS 239 Principles 1, 2, and 11.

Assessment-side implications:

- Principle 1 (Governance) carries the OCC §II independence expectation; the chief risk executive and the risk-data committee composition are evidenced at the §II depth.
- Principle 2 (Data architecture and IT infrastructure) carries the supporting-infrastructure expectation; the §II frame demands evidence that the risk-data layer can support the risk-appetite statement reporting.
- Principle 11 (Distribution) carries the board-reporting expectation; the §II frame demands evidence that the board receives risk reporting on the cadence the §II governance framework requires.

##### 4. CCAR / DFAST overlap on Principles 5 and 6

For banks subject to FRB stress testing (CCAR for Category I-II BHCs; DFAST for Category III-IV BHCs), the stress-testing data layer is the working evidence for Principle 5 (timeliness) and Principle 6 (adaptability). The assessment carries:

- Stress-testing data-aggregation cycle time as the working metric for Principle 5.
- Recent ad-hoc and stress-scenario aggregation runs (intra-cycle ad-hoc requests, ad-hoc capital actions, ad-hoc liquidity stress) as the working evidence for Principle 6.
- Cross-link to the firm's CCAR or DFAST submission cycle for evidence of working timeliness and adaptability.

##### 5. Open MRA / MRIA linkage on Principle 13

Principle 13 (Remedial actions and supervisory measures) reads at the firm as posture toward open supervisory findings on risk data. The assessment names every open MRA, MRIA, or 4(m) action touching risk data, with the issue-register reference, owner, target date, and current status. An assessment with an empty Principle 13 finding-set is not credible at a large bank; supervisors expect linkage to the firm's open-finding population on the risk-data layer.

##### 6. Home/host coordination on Principle 14

For a US G-SIB with material non-US operations, or for a foreign banking organization with material US operations, Principle 14 (Home/host cooperation) addresses the framework for sharing risk data with home and host supervisors. The assessment records:

- The home supervisor and the material host supervisors named.
- The data-sharing framework (supervisory college participation, information-sharing protocols, joint data requests).
- The firm's posture on cross-border consistency of risk-data definitions, lineage, and reporting.

For a US-domiciled G-SIB, the home supervisor is the FRB; the material host supervisors typically include the ECB (for SSM-supervised EU subsidiaries), the PRA (for UK subsidiaries), and others by footprint.

#### Banking-specific output template additions

The following fields are added to the assessment (mapped to schema where present):

- `scope.tailoring_category` — Category I / II / III / IV / not-tailored / FBO-IHC.
- `scope.heightened_standards_inscope` — boolean, true for OCC-supervised covered banks.
- `scope.bank_charter_type` — national bank / state member / state nonmember / savings association / BHC / FBO-IHC.
- `scope.primary_federal_regulator` — OCC / FRB / FDIC / NCUA.
- `scope.stress_testing_inscope` — boolean with cross-reference to CCAR or DFAST submission.
- `principle_results[].evidence_summary` — Principle 5 and 6 entries reference stress-testing cycle evidence and recent ad-hoc-aggregation runs.
- `principle_results[].gaps[].linked_issue_id` — Principle 13 entries link to open MRAs, MRIAs, or 4(m) actions in the issue register.
- `linked_open_issues[]` — open supervisory findings on risk data named explicitly.

#### Common pitfalls in banking BCBS 239 assessments

- Rating Principle 6 as `largely-compliant` without recent ad-hoc-aggregation evidence. The BCBS thematic-finding pattern reads this as not credible; supervisors probe Principle 6 evidence first.
- Treating CCAR / DFAST stress-testing capability as separate from BCBS 239 Principles 5 and 6. Stress testing is the working evidence for both principles at a CCAR/DFAST firm.
- Rating Principle 13 from a generic statement of remediation discipline without naming open MRAs / MRIAs. The Principle 13 evidence is the firm's open-finding population, not its policy.
- Treating the FBO IHC as a standalone perimeter without addressing parent-group BCBS 239 posture. The IHC inherits the parent's risk-data layer and the assessment's supervisory-context block must address both.
- Aggregating ratings across legal entities without a documented rationale. For multi-entity banking groups, per-entity ratings can vary; the aggregation rationale is part of the methodology section.
- Omitting the OCC Heightened Standards reach where the firm is OCC-supervised and crosses the threshold; supervisors catch the omission in the §II cross-walk.
- Importing financial-statement data-quality controls (SOX 404) as Principle 3 evidence. BCBS 239 is risk-data-anchored; SOX 404 is financial-statement-anchored. The doctrines do not substitute.

## capital-markets

### Capital markets sector overlay for bcbs239-gap-assessment

When the scope record names sector `capital-markets`, this overlay adds capital-markets-specific fields and review demands to the assessment. Where there is conflict between the capability defaults and this overlay, the overlay governs the capital-markets-sector elements.

Loaded by: `bcbs239-gap-assessment/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`. This is a light overlay. BCBS 239 applies at the BHC level; broker-dealer subsidiaries inherit it. The overlay covers the broker-dealer subsidiary view and the SEC / FINRA reporting data-quality interactions.

#### Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

#### What changes for capital-markets BCBS 239 assessments

##### 1. BCBS 239 reach to broker-dealer subsidiaries flows through the parent BHC

For a US BHC with a broker-dealer subsidiary, BCBS 239 binds at the consolidated parent level; the broker-dealer subsidiary inherits the parent's risk-data layer through consolidation and through the parent's risk-aggregation responsibilities. The assessment's supervisory-context section names the parent BHC and identifies the broker-dealer subsidiary as a child entity within the consolidated perimeter.

For a standalone broker-dealer that is not part of a BHC (typical at SEC-registered investment advisers and at standalone BDs), BCBS 239 does not directly apply. The assessment frames as voluntary internal benchmark and uses the BCBS 239 grammar without the BCBS supervisory rating posture.

##### 2. SEC Rule 17h overlap on Principles 3, 4, 5, and 7

For broker-dealers above the Rule 17h threshold (currently a tentative-net-capital threshold), 17 CFR §240.17h-1T and §240.17h-2T require risk-assessment recordkeeping and reporting on material associated persons. The data layer supporting 17h reporting overlaps with the consolidated risk-data layer that supports BCBS 239 at the parent.

Assessment-side mapping:

- Principle 3 (Accuracy and integrity) and Principle 7 (Accuracy of risk reporting) carry the 17h reporting accuracy as working evidence at the broker-dealer level.
- Principle 4 (Completeness) carries the 17h scope of material associated persons as working evidence on the BD-side of the consolidated perimeter.
- Principle 5 (Timeliness) carries the 17h reporting cycle as working evidence on the BD-side.

##### 3. FINRA reporting data quality

For FINRA-member broker-dealers, the data layer supporting FINRA-mandated reporting (FOCUS reports under Rule 17a-5; large trader reporting under Rule 13h-1; CAT under SEC Rule 613; OATS predecessor data; supervision-system reporting under FINRA Rule 3110) is the BD-level evidence for Principle 3 (accuracy), Principle 5 (timeliness), and Principle 7 (accuracy of reporting). The assessment names the in-scope FINRA reports and the data layer that supports them.

##### 4. Liquidity and concentration risk reporting at the BD

For broker-dealers carrying material customer or proprietary positions, liquidity and concentration risk reporting at the BD level is the operative working test for Principle 4 (completeness) on the BD-side. The assessment carries the BD's liquidity-stress-testing posture and the concentration-risk reporting cadence.

##### 5. CAT data quality is a Principle 3 and Principle 5 concern

The Consolidated Audit Trail (CAT) under SEC Rule 613 imposes data-quality and timeliness expectations on BD-side trade reporting. CAT data-quality issues are operative evidence for Principle 3 (accuracy) and Principle 5 (timeliness) on the BD-side.

##### 6. Asset-management subsidiary view

For a BHC with an asset-management subsidiary (1940 Act funds, separate accounts, alternatives), the asset-management subsidiary's risk-data layer (NAV calculation, performance reporting, holdings reporting under Form N-PORT and Form PF) inherits the parent BCBS 239 frame at the consolidated perimeter but operates under SEC reporting-data discipline on the subsidiary side. The assessment notes the subsidiary perimeter and the SEC reporting data layer without conflating the two regimes.

#### Capital-markets-specific output template additions

- `scope.legal_entity_perimeter` — names the BHC parent and the BD / IA / asset-management subsidiaries within the consolidated perimeter.
- `scope.broker_dealer_inscope` — boolean.
- `scope.rule_17h_inscope` — boolean.
- `scope.cat_reporter_inscope` — boolean.
- `principle_results[].evidence_summary` — Principles 3, 4, 5, 7 entries reference 17h, FOCUS, CAT, and N-PORT / PF data layers where applicable on the BD or asset-management subsidiary side.

#### Common pitfalls in capital-markets BCBS 239 assessments

- Asserting BCBS 239 binding reach to a standalone BD outside a BHC. It does not directly apply; the assessment frames as voluntary internal benchmark.
- Treating CAT data-quality issues as a separate operational matter. CAT is operative evidence for Principle 3 and Principle 5 on the BD-side; a clean BCBS 239 assessment with open CAT data-quality issues is not credible.
- Conflating SEC reporting-data discipline (1940 Act, Form N-PORT, Form PF) with BCBS 239 risk-data discipline. The two regimes are different; the assessment cites each in its proper section.
- Omitting the parent-BHC consolidation context for a BD subsidiary. The BD inherits the parent's BCBS 239 posture; the assessment must address both.
- Treating the broker-dealer's books-and-records discipline (Rule 17a-3 / 17a-4) as Principle 3 evidence. Books-and-records discipline is recordkeeping; Principle 3 is risk-data accuracy and integrity. The doctrines do not substitute.

## insurance

### Insurance sector overlay for bcbs239-gap-assessment

When the scope record names sector `insurance`, this overlay adds insurance-specific fields and review demands to the assessment. Where there is conflict between the capability defaults and this overlay, the overlay governs the insurance-sector elements.

Loaded by: `bcbs239-gap-assessment/SKILL.md` when `scope.sector_overlay_set` includes `insurance`. This is a light overlay. BCBS 239 does not directly apply to insurers. The overlay covers the case where an insurance group voluntarily applies BCBS 239 as an internal benchmark, and maps the BCBS 239 principles onto the operative insurance regimes (NAIC ORSA, IAIS ICPs, state Holding Company filings).

#### Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

#### What changes for insurance BCBS 239 assessments

##### 1. ORSA is the operative US analogue

NAIC Model #505 (Risk Management and Own Risk and Solvency Assessment Model Act) requires insurers above the premium threshold to maintain risk-management functions including risk identification, measurement, monitoring, and reporting [verify section]. The ORSA Summary Report is the firm-level artifact; the data layer that supports it carries the analogues to BCBS 239 Principles 3, 4, 5, 7, 8, and 10.

Assessment-side mapping:

- Principle 3 (Accuracy and integrity) maps to the ORSA risk-identification and measurement data quality.
- Principle 4 (Completeness) maps to the ORSA scope of risks identified across the enterprise.
- Principle 5 (Timeliness) maps to the ORSA reporting cadence (annual minimum; more frequent for material change).
- Principle 7 (Accuracy of risk reporting) maps to the ORSA Summary Report's risk-position accuracy.
- Principle 8 (Comprehensiveness) maps to the ORSA coverage of all material risk types (insurance, market, credit, operational, liquidity, strategic).
- Principle 10 (Frequency) maps to the ORSA cycle plus the insurer's internal management-reporting cadence.

The assessment names the ORSA cycle as the working evidence for the mapped principles and labels the ORSA Summary Report (or the supporting working files) as the evidence pointer.

##### 2. IAIS ICP 8 and ICP 16 frame the international view

IAIS ICP 8 (Risk Management and Internal Controls) and ICP 16 (Enterprise Risk Management for Solvency Purposes) [verify section] set the IAIS expectations that home and host supervisors of internationally active insurance groups apply. Where the insurance group operates across jurisdictions, the assessment carries the ICP frame as the international analogue to BCBS 239's banking-group view.

##### 3. State Holding Company filings (Form B and Form F)

NAIC Model #440 (Insurance Holding Company System Regulatory Act) and Model #450 (Insurance Holding Company System Model Regulation) require Form B (annual registration) and Form F (enterprise risk report) filings [verify section]. The Form F enterprise risk report is the operative reporting artifact for the holding-company-level risk view; the data layer that supports it is the assessment-relevant infrastructure.

##### 4. ComFrame and IAIG designation

For an Internationally Active Insurance Group (IAIG) under the IAIS Common Framework (ComFrame), the supervisory expectations carry additional weight on Principle 14 (Home/host cooperation). The home supervisor typically convenes the supervisory college; the assessment records the college framework and the data-sharing protocols.

##### 5. SOX 404 / NAIC Model #205 financial-reporting controls are not BCBS 239 evidence

Insurance financial-reporting controls (SOX 404 for SEC-registered insurance holding companies; NAIC Model Audit Rule #205 for statutory audit) are doctrinally distinct from the risk-data layer that BCBS 239 addresses. The assessment does not cite SOX 404 or Model #205 evidence as Principle 3 or Principle 7 evidence on the risk side.

##### 6. Voluntary-adoption framing

Where the insurance group has voluntarily adopted BCBS 239 as an internal benchmark (typical at IAIGs and at large internationally active groups), the assessment notes the voluntary status in the supervisory-context section and frames the rating vocabulary as internal benchmark rather than as a supervisory rating. The Principle 12 (Review) and Principle 13 (Remedial actions) sections read against internal review and internal-finding remediation, not against a supervisory review.

#### Insurance-specific output template additions

- `scope.supervisory_context` — `voluntary` is the default for insurance assessments unless the group is otherwise designated.
- `scope.iaig_designation` — boolean.
- `scope.orsa_inscope` — boolean.
- `scope.holding_company_filings` — Form B / Form F filing status reference.
- `principle_results[].evidence_summary` — Principles 3, 4, 5, 7, 8, 10 entries reference ORSA Summary Report and supporting working files.
- `principle_results[].evidence_summary` — Principle 14 entries reference the supervisory college framework where the group is an IAIG.

#### Common pitfalls in insurance BCBS 239 assessments

- Importing the BCBS 239 banking vocabulary verbatim without mapping to ORSA / ICP terminology. State DOI rate analysts and ORSA reviewers use the insurance vocabulary; the assessment translates.
- Treating SOX 404 financial-reporting controls as risk-data evidence. The doctrines do not substitute.
- Asserting that BCBS 239 is binding on the insurer. It is not; the assessment frames the rating as internal benchmark unless the group is otherwise designated.
- Omitting Form F as the operative holding-company reporting artifact. For Holding Company Act-regulated groups, Form F is the artifact the assessment's Principle 8, 9, and 11 evidence rests on.
- Treating Principle 14 as not applicable for an insurance group. For an IAIG with cross-border operations, the supervisory college and home/host data-sharing protocols are operative.
- Skipping the voluntary-adoption framing. A reviewer reading the assessment without this context misreads the rating vocabulary.

## payments-fintech

### Payments and fintech sector overlay for bcbs239-gap-assessment

When the scope record names sector `payments-fintech`, this overlay adds payments- and fintech-specific fields and review demands to the assessment. Where there is conflict between the capability defaults and this overlay, the overlay governs the sector elements.

Loaded by: `bcbs239-gap-assessment/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`. This is a stub overlay. BCBS 239 does not directly apply to non-bank payments and fintech firms. The overlay covers the case where a large nonbank payments firm voluntarily adopts BCBS 239 as a risk-data maturity benchmark, and the case where a sponsor-bank arrangement carries BCBS 239 reach into the fintech program through the sponsor bank.

#### Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

#### What changes for payments and fintech BCBS 239 assessments

##### 1. Direct reach is limited; voluntary adoption is the typical posture

For non-bank money transmitters, payments processors, and fintech apps, BCBS 239 does not directly apply. State money-transmission examiners, FinCEN under the BSA, and (for consumer-facing products) the CFPB are the operative supervisors; their data-quality expectations flow through state exam standards, the BSA program rule, and CFPB UDAAP / Reg E reach.

Where the firm voluntarily adopts BCBS 239 as a risk-data maturity benchmark, the assessment frames the rating vocabulary as internal benchmark and notes the voluntary status in the supervisory-context section. Principle 12 (Review) and Principle 13 (Remedial actions) read against internal review and internal-finding remediation rather than against a supervisory review.

##### 2. Sponsor-bank arrangements carry BCBS 239 reach indirectly

For a fintech program operating through a sponsor-bank arrangement (deposit, lending, or card products on a sponsor-bank balance sheet), the sponsor bank carries the BCBS 239 expectations on the consolidated risk-data layer that includes the fintech program's exposures. The fintech program inherits the sponsor bank's risk-data discipline through the bank-fintech contract and through the sponsor bank's third-party risk management framework (Joint OCC / FRB / FDIC Interagency Guidance on Third-Party Relationships, June 2023).

Assessment-side implications:

- The assessment perimeter names the sponsor bank as the BCBS 239-binding entity and the fintech program as the dependent entity.
- The sponsor bank's risk-data layer is the operative subject; the fintech program's data feed into the sponsor bank's risk aggregation is the working evidence on the program-side.
- A fintech-only BCBS 239 assessment without sponsor-bank framing is incomplete.

##### 3. BSA / AML transaction-monitoring data quality

For state-licensed money transmitters and for sponsor-bank-program fintechs with BSA/AML obligations, the transaction-monitoring data layer is the working evidence for Principle 3 (accuracy) and Principle 4 (completeness) on the BSA/AML side. The assessment carries:

- Transaction-monitoring data feed completeness (alert-population coverage by product, channel, geography).
- Transaction-monitoring data accuracy (data-quality issues affecting alert generation).
- SAR-workflow data lineage from alert to filing (or to dismissal).

##### 4. NYDFS Part 504 / Part 500 reach in the NY footprint

For NY-licensed fintechs and DFS-regulated money transmitters, NYDFS Part 504 imposes specific transaction-monitoring program expectations including the senior-officer certification; NYDFS Part 500 cyber expectations apply across the operation. Both reach the data layer the BCBS 239-style assessment evaluates.

##### 5. Consumer-product data quality and Reg E error resolution

For consumer-facing fintech products, Reg E error-resolution expectations (10-day provisional credit, 45-day investigation, 90-day extended investigation for new accounts and certain transaction types) impose timeliness expectations on the consumer-dispute data layer. Reg E timeliness is operative evidence for Principle 5 (timeliness) on the consumer-dispute side.

##### 6. State money-transmission examiner expectations

For state-licensed money transmitters operating across multiple states, the Conference of State Bank Supervisors (CSBS) coordinated examination program (Money Services Businesses Networked Supervision) sets multi-state exam standards that reach the data layer. The assessment names the state-licensure footprint and the strictest-applicable-state posture.

#### Payments and fintech-specific output template additions

- `scope.supervisory_context` — `voluntary` is the default for nonbank-fintech assessments unless a sponsor-bank framing applies.
- `scope.sponsor_bank_arrangement` — boolean; if true, sponsor-bank named as the BCBS 239-binding entity.
- `scope.state_licensure_footprint` — list of states with money-transmission or other licences.
- `scope.bsa_aml_obligations` — boolean.
- `principle_results[].evidence_summary` — Principles 3, 4, 5 entries reference transaction-monitoring data layer and Reg E dispute data layer where applicable.

#### Common pitfalls in payments and fintech BCBS 239 assessments

- Asserting BCBS 239 binding reach to a non-bank fintech. It does not directly apply; the assessment frames as voluntary internal benchmark or as sponsor-bank-inherited.
- Omitting the sponsor-bank perimeter for a fintech program operating on a sponsor-bank balance sheet. The sponsor bank carries the binding reach; the assessment must address both.
- Treating Reg E error-resolution timeliness as a separate consumer-protection matter. Reg E timeliness is operative evidence for Principle 5 on the consumer-dispute side.
- Treating BSA/AML transaction-monitoring data quality as a separate program matter. TM data quality is operative evidence for Principles 3 and 4 on the BSA/AML side.
- Skipping NYDFS Part 504 / Part 500 reach in the NY footprint. Both reach the data layer the assessment evaluates.
- Treating the state-licensure footprint as not assessment-relevant. State examiners review TM and consumer-product data quality; the strictest-applicable-state posture sets the bar.
