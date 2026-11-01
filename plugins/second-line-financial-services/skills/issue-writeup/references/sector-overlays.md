# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — issue-writeup

Loads when the scope `sector_overlay_set` includes `banking`. The overlay shapes the criteria block, the severity calibration, the MRA / MRIA / MRBA classification field, and the closure-evidence framing for issues at federally regulated US banks (national, state-member, state-non-member, savings, holding companies, and US IHCs of foreign banking organizations).

#### Why the banking overlay matters

The federal banking supervisors (FRB, OCC, FDIC) have published, distinct frameworks for how findings are written, classified, and tracked. An issue write-up at a regulated bank that does not conform to the named framework is harder to defend in continuous monitoring and at the next examination cycle. The overlay is the contract between the CCCE artifact and the examiner's expected response register.

#### Source basis

- **Federal Reserve SR 13-13 / CA 13-10** — Supervisory Considerations for the Communication of Supervisory Findings. MRA and MRIA framework, the firm-side expectation that issues are tracked through closure with documented remediation evidence.
- **OCC Bulletin 2014-39** — Matters Requiring Attention. Defines MRA criteria, the OCC's expectation that MRAs name a corrective action and target date, and the convention that MRA closure is evidenced for OCC inspection.
- **FDIC Risk Management Manual of Examination Policies and FDIC Compliance Examination Manual** — MRBA framing (Matters Requiring Board Attention) as the FDIC parallel to OCC and FRB MRAs; addressed to the board rather than to management alone.
- **12 CFR Part 30, Appendix D — OCC Heightened Standards for Large Insured National Banks** — Standards on risk governance framework, three lines of defense, and front-line-unit responsibilities. Severity calibration shifts when the issue concerns a Heightened-Standards-covered bank.
- **Reg YY (12 CFR Part 252)** — Enhanced prudential standards for large bank holding companies; risk management and risk committee requirements that frame governance findings.
- **FFIEC Uniform Rating System (CAMELS for banks; ROCA for FBOs)** — composite-rating implications for severity calibration; findings that move a CAMELS component carry higher severity rationale weight.

#### What the overlay adds to the write-up

##### MRA / MRIA / MRBA classification

When the source type is examiner-letter and the regulator is FRB, OCC, or FDIC, the `mra_mria_classification` field is populated:

- **MRIA** (FRB only) — Matter Requiring Immediate Attention. The most severe category; reserved for matters that have caused or threaten to cause significant harm or that are violations of law. Severity rating is typically critical or high; closure evidence is detailed; target date is short.
- **MRA** (FRB and OCC) — Matter Requiring Attention. Significant deficiency that requires correction. Severity is typically high or moderate; closure evidence is named; target date is set with the regulator's expected response register in mind.
- **MRBA** (FDIC) — Matter Requiring Board Attention. Addressed to the board rather than to management alone; severity is typically high; closure evidence emphasises board-level oversight artifacts (board minutes, board-approved remediation plan).

Issues sourced from a state-member bank's FRB letter and a state non-member bank's FDIC letter use different fields even though the underlying condition may be the same; the overlay ensures the artifact carries the regulator-correct framing.

##### Severity calibration

Banking severity calibration leans on three axes the federal supervisors weigh: (1) impact on the bank's safety and soundness, (2) impact on consumers and the public, (3) violation-of-law dimension. Findings that touch CAMELS components (Capital, Asset quality, Management, Earnings, Liquidity, Sensitivity to market risk) carry severity-rationale weight tied to the specific component. A finding that would move the M (Management) rating is high or critical even if the operational impact is modest, because the rating consequence is itself the impact.

##### Closure-evidence framing

The federal supervisors expect closure evidence to be inspectable at the next continuous-monitoring touchpoint or at the next examination cycle. The closure-evidence field for banking-overlay issues names:
- The artifact (board minutes, committee minutes, system-of-record output, sign-off log).
- The retention location (GRC platform, board-portal, document management system).
- The retention period (banking exam files typically run a five-year rolling retention; firm-overlay specifies the firm's actual cadence).

##### Heightened Standards severity flavour

For OCC-Heightened-Standards-covered banks (12 CFR Part 30 Appendix D applicable, currently $50B+ at the OCC's discretion subject to the rule's threshold framework), findings on the risk-governance framework, three-lines-of-defense architecture, or independent risk management carry additional severity weight. The severity rationale references the specific Heightened Standard that the condition impairs.

##### Reg YY governance findings

For BHCs covered by Reg YY enhanced prudential standards (currently $100B+), findings on the risk committee, the CRO independence, or the risk-appetite framework carry additional severity weight. The criteria block references the specific Reg YY section.

#### Common patterns

- **Repeat MRA**. An MRA that has been issued twice on the same root cause moves to MRIA in the next exam cycle. The issue's severity rationale should reference any prior MRA on the same matter; the firm's GRC platform's MRA-history field is the source.
- **MRA closure with residual issues**. Closing an MRA with the regulator does not close the issue at the firm; the firm carries a residual issue at lower severity for the remediation tail. The issue write-up reflects the regulator-side closure and the firm-side residual separately.
- **Pre-emptive self-disclosure**. A bank that surfaces a deficiency to the FRB, OCC, or FDIC before the regulator finds it typically gets credit on severity calibration. The source type is `self-identified` rather than `examiner-letter`, but the regulator-engagement record is referenced in the source block.

#### Implications for the CCCE

- **Criteria** for banking-overlay issues cite the regulator's published framework first (FRB SR letter, OCC bulletin, FDIC manual section), then the firm's policy second. The order matters; reviewers expect the regulatory criterion to lead.
- **Cause** for governance findings ties to the specific lines-of-defense element that failed (CRO independence, board risk committee oversight, first-line-unit risk responsibility). For Heightened-Standards-covered banks, the cause references the specific Standard.
- **Effect** for banking issues quantifies safety-and-soundness implications where possible (capital impact, liquidity impact, asset-quality impact, earnings impact) and consumer/public-impact distinctly.
- **Closure evidence** for examiner-issued findings includes the artifacts the regulator named in the supervisory letter as the expected response, which usually exceed the firm's standard closure pattern.

#### Anchors used by this overlay

- FRB SR 13-13 / CA 13-10 — Supervisory Considerations for the Communication of Supervisory Findings. https://www.federalreserve.gov/supervisionreg/srletters/sr1313.htm
- OCC Bulletin 2014-39 — Matters Requiring Attention. https://www.occ.gov/news-issuances/bulletins/2014/bulletin-2014-39.html
- 12 CFR Part 30, Appendix D — OCC Heightened Standards (Standards I–V). https://www.ecfr.gov/current/title-12/chapter-I/part-30/appendix-Appendix%20D%20to%20Part%2030
- 12 CFR Part 252 (Reg YY) — Enhanced prudential standards for large BHCs. [verify current section labels for risk committee and risk-management requirements.]
- FDIC Risk Management Manual of Examination Policies. https://www.fdic.gov/regulations/safety/manual/
- FDIC Compliance Examination Manual. https://www.fdic.gov/resources/supervision-and-examinations/consumer-compliance-examination-manual/
- FFIEC Uniform Rating System (CAMELS / ROCA). [verify current edition references.]

## capital-markets

### Capital-markets sector overlay — issue-writeup

Loads when the scope `sector_overlay_set` includes `capital-markets`. The overlay shapes the criteria block, the severity calibration, and the closure-evidence framing for issues at SEC- and FINRA-regulated entities (broker-dealers, investment advisers, registered funds, transfer agents, exchanges, ATSs).

#### Why the capital-markets overlay matters

SEC EXAMS and FINRA each have a published deficiency-letter format and a follow-up convention that is distinct from the federal banking MRA / MRIA framework and from the state-DOI insurance examination convention. The criteria block, severity calibration, and closure-evidence framing for capital-markets issues need to fit the SEC EXAMS deficiency-letter / risk-alert pattern or the FINRA Letter of Caution / examination-finding pattern.

#### Source basis

- **SEC EXAMS Deficiency Letter** convention — the SEC Division of Examinations issues deficiency letters at the close of an examination listing observed deficiencies; the firm responds with a corrective-action plan within the time the letter specifies (typically 30 days). Severity calibration tracks to whether the deficiency is referred to the Division of Enforcement.
- **SEC EXAMS Risk Alerts** — published priorities and observed-deficiency categories that inform severity calibration even when the firm is not the subject of the alert.
- **SEC Rules cited in deficiency letters** — most frequently 17 CFR §240.15c3-1 (broker-dealer net capital), §240.15c3-3 (customer protection), §240.17a-3 / §240.17a-4 (recordkeeping), §240.15c3-5 (market access), §275.206(4)-7 (Investment Advisers Act compliance program), §275.204-2 (Investment Advisers Act recordkeeping), §270.38a-1 (Investment Company Act compliance program), Reg BI (broker-dealer best interest), Form CRS rules.
- **FINRA Letter of Caution** — informal disposition that closes an examination matter without formal disciplinary action; severity calibration is moderate; closure evidence is named but lighter than enforcement-track findings.
- **FINRA Examination Finding** — formal finding in the examination report; severity is high or moderate depending on the rule cited and the recurrence pattern; closure evidence is detailed and scheduled to the next exam cycle.
- **FINRA Cautionary Action and Acceptance, Waiver, and Consent (AWC)** — formal disciplinary dispositions; the issue write-up references the disposition but the full enforcement-track artifact lives outside the firm's internal issue log.
- **FINRA Rules cited in findings** — most frequently 3110 (supervision), 3120 (supervisory control system), 4511 (general books and records), 4512 (customer account information), 2010 (standards of commercial honor and just and equitable principles of trade), 2210 (communications), 2330 (variable annuities), and the Trade Reporting and Compliance Engine (TRACE) rules.
- **MSRB Rules** — for municipal-securities-active firms, MSRB Rule G-27 (supervision), G-8 (recordkeeping), G-9 (record retention), G-17 (fair dealing).

#### What the overlay adds to the write-up

##### SEC EXAMS deficiency-letter format

When the source type is examiner-letter and the regulator is SEC EXAMS, the criteria block follows the deficiency-letter format. A typical deficiency-letter line cites:
- The rule (e.g., "Section 206(4)-7 of the Investment Advisers Act and Rule 206(4)-7 thereunder").
- The deficiency observed (specific, with dates).
- The corrective action expected (often phrased as "the firm should").

The firm's internal issue write-up mirrors this structure: criteria carries the rule and section; condition carries the deficiency observed; recommendation carries the corrective action. The `mra_mria_classification` field is `n/a`. Severity calibration is high if the deficiency is referred to the Division of Enforcement, high or moderate if a remediation plan is requested with a short cure window, moderate if it is a no-further-action deficiency.

##### FINRA Letter of Caution / examination finding format

When the source is a FINRA Letter of Caution, severity is typically moderate; the criteria block cites the FINRA rule and the firm's WSP (written supervisory procedures) section that the rule maps to. Closure evidence emphasises WSP update, supervisory-control-system enhancement, and examiner-acknowledgement at the next cycle. When the source is a FINRA examination finding, severity is high or moderate; the criteria block cites the FINRA rule and the firm's compliance-policy citation.

##### Severity calibration

Capital-markets severity calibration weighs (1) customer-protection impact, (2) market-integrity impact, (3) capital adequacy / financial-stability impact, (4) supervisory-system impact, and (5) recordkeeping-and-disclosure-completeness impact. Findings that touch the customer-protection rule (Rule 15c3-3) or the net-capital rule (Rule 15c3-1) for broker-dealers carry severity weight tied to the regulatory threshold. Findings on the IA compliance program (Rule 206(4)-7) carry severity tied to the chief-compliance-officer's documented annual review.

##### Closure-evidence framing

Closure evidence for SEC EXAMS deficiency-letter findings names the corrective-action-plan response, the implementation evidence (system change, policy update, training delivered, supervisory enhancement), and the readiness for the next examination touchpoint. For FINRA findings, closure evidence names the WSP update, the supervisory-control-system update, and the readiness for the next FINRA cycle exam. Investment-adviser findings under Rule 206(4)-7 carry closure evidence in the chief-compliance-officer's annual review documentation.

##### Books-and-records-driven findings

Recordkeeping is the single most-cited category in SEC EXAMS deficiency letters and FINRA findings. The criteria block for recordkeeping findings cites 17 CFR §240.17a-3 and §240.17a-4 (broker-dealer), 17 CFR §275.204-2 (IA), or FINRA Rule 4511 directly. Cause for recordkeeping findings ties to the specific recordkeeping control that failed (preservation-format control, record-retention-period control, electronic-storage WORM-compliance control after the 2022 amendment).

#### Common patterns

- **Annual-review-cycle findings on Investment Advisers**. Rule 206(4)-7 requires advisers to adopt and implement policies and procedures and to review them no less frequently than annually. Findings on the annual review (no review performed, review performed but not documented, review documented but not actioned) are common SEC EXAMS deficiencies. Severity is typically moderate to high.
- **Form CRS findings on dual-registered firms**. Findings on Form CRS delivery, content, or filing carry customer-impact severity weight; the consumer-protection lens applies.
- **Regulation Best Interest findings**. Reg BI findings on care obligation, disclosure obligation, conflict-of-interest obligation, or compliance obligation carry customer-impact severity weight; the FINRA Reg BI Risk Monitoring Reports inform severity calibration.
- **Net-capital and customer-reserve findings**. 15c3-1 and 15c3-3 findings carry the highest severity in the broker-dealer space; closure-evidence emphasises the financial-impact remediation and the net-capital recomputation.

#### Implications for the CCCE

- **Criteria** for capital-markets-overlay issues cite the federal rule first (SEC, FINRA, MSRB), then the firm's WSP / compliance-policy section second. The order matters; SEC EXAMS and FINRA expect the regulatory criterion to lead.
- **Cause** for supervisory-system findings ties to the specific WSP element that failed (review-cadence control, escalation-path control, surveillance-output control). For recordkeeping findings, cause maps to the specific control attribute on preservation, retention, or accessibility.
- **Effect** for capital-markets issues quantifies customer-protection impact, market-integrity impact, capital-adequacy impact, and recordkeeping-and-disclosure-completeness impact distinctly. Customer-protection effects are typically named in customer-count and dollar-impact terms.
- **Closure evidence** for SEC EXAMS findings includes the corrective-action-plan response document; for FINRA findings, includes the WSP update and the supervisory-control-system update.

#### Anchors used by this overlay

- 17 CFR Part 240 — Securities Exchange Act rules. https://www.ecfr.gov/current/title-17/chapter-II/part-240
  - §240.15c3-1 (Net Capital)
  - §240.15c3-3 (Customer Protection)
  - §240.15c3-5 (Risk Management Controls for Brokers or Dealers with Market Access)
  - §240.17a-3 / §240.17a-4 (Recordkeeping; 2022 amendment to 17a-4 on electronic-storage standard)
- 17 CFR Part 275 — Investment Advisers Act rules. https://www.ecfr.gov/current/title-17/chapter-II/part-275
  - §275.206(4)-7 (Compliance Procedures and Practices)
  - §275.204-2 (Books and Records)
- 17 CFR Part 270 — Investment Company Act rules.
  - §270.38a-1 (Compliance Procedures and Practices of Investment Companies)
- Form CRS — 17 CFR §249.640 / §279.10. [verify current section labels.]
- Regulation Best Interest — 17 CFR §240.15l-1. [verify section labels.]
- FINRA Rule Book. https://www.finra.org/rules-guidance/rulebooks/finra-rules
  - Rule 3110 (Supervision)
  - Rule 3120 (Supervisory Control System)
  - Rule 4511 (General Books and Records)
  - Rule 4512 (Customer Account Information)
  - Rule 2010 (Standards of Commercial Honor)
  - Rule 2210 (Communications with the Public)
- MSRB Rule Book. https://www.msrb.org/rules-and-interpretations/msrb-rules
  - Rule G-27 (Supervision)
  - Rule G-8 (Books and Records)
  - Rule G-9 (Record Retention)
  - Rule G-17 (Fair Dealing)
- SEC EXAMS Risk Alerts. https://www.sec.gov/exams/risk-alerts (informs severity calibration when the firm's deficiency category is published).

## insurance

### Insurance sector overlay — issue-writeup

Loads when the scope `sector_overlay_set` includes `insurance`. The overlay shapes the criteria block, the severity calibration, and the closure-evidence framing for issues at US insurance companies (P&C, life, health, reinsurance) supervised by state DOIs and coordinated through the NAIC.

#### Why the insurance overlay matters

Insurance supervision in the US is state-led with NAIC coordination, which produces a different finding shape than the federal banking framework. State DOIs issue findings via market-conduct examination reports, financial examination reports, and supervisory letters; remediation is often documented through Memoranda of Understanding (MOUs), consent orders, or corrective action plans (CAPs). The criteria block, the severity calibration, and the closure-evidence framing all need to fit the state-DOI / NAIC convention, not the federal banking convention.

#### Source basis

- **NAIC Financial Condition Examiners Handbook** — convention for financial-examination findings. The handbook structures findings around significant deficiencies, control weaknesses, and recommendations; severity calibration is anchored on the audit-risk-model concepts the handbook adopts from AICPA AU-C 265.
- **NAIC Market Regulation Handbook** — convention for market-conduct examination findings. Findings track to standards on policy forms, claims handling, producer licensing, advertising, complaint handling, and unfair trade practices.
- **NAIC Model Audit Rule (MAR; Annual Financial Reporting Model Regulation, MDL-205)** — internal control over financial reporting framework adopted in most states. Findings on insurer internal control over financial reporting cite MAR §16 (notification of unremediated material weakness).
- **NAIC ORSA Guidance Manual** — Own Risk and Solvency Assessment framework. Enterprise-risk findings at ORSA-eligible insurers cite the relevant ORSA component (risk identification, risk-management framework, risk-appetite-and-tolerance, capital adequacy).
- **State DOI MOU and consent-order language conventions** — varies by state but most state DOIs publish enforcement actions; the language patterns in posted MOUs and consent orders inform the criteria-citation discipline. [verify specific state references against the state's actual language; New York DFS, California DOI, Texas DOI, and Florida OIR are frequently cited examples.]
- **NAIC AI Bulletin (Model Bulletin on the Use of Artificial Intelligence Systems by Insurers, December 2023)** — AI-system findings at insurers cite the bulletin's governance framework expectations.

#### What the overlay adds to the write-up

##### Examination finding format

When the source type is examiner-letter and the regulator is a state DOI, the criteria block follows the state DOI's examination-report format. State DOI examination reports typically structure findings as:
- **Comment** (an observation that does not rise to the level of a deficiency)
- **Recommendation** (a deficiency in policies, procedures, or controls that should be corrected)
- **Citation / violation** (a confirmed violation of statute, regulation, or department rule)

The firm's internal issue write-up mirrors this structure: a finding labelled as a recommendation in the DOI's report is typically severity moderate or high in the firm's calibration; a citation/violation is high or critical. The `mra_mria_classification` field is set to `n/a` because the federal banking MRA / MRIA / MRBA framework does not apply.

##### Severity calibration

Insurance severity calibration weighs (1) policyholder impact, (2) financial solvency impact, (3) market-conduct violation dimension, and (4) producer / distribution channel implications. Findings that touch financial reporting under MAR carry severity tied to the materiality framework AICPA AU-C 265 sets. Market-conduct findings carry severity tied to consumer-harm scope, repeated-pattern frequency, and unfair-trade-practice exposure.

##### Closure-evidence framing

State DOIs typically follow up via the next examination cycle (financial exams every three to five years; market-conduct exams on a state-by-state cadence). Closure evidence for state-DOI-issued findings names:
- The artifact (board minutes, committee minutes, system-of-record output, sign-off log).
- The retention location (insurer's GRC platform, board-portal, regulatory-filings system).
- The DOI's expected re-inspection touchpoint (next exam cycle, mid-cycle continuous-monitoring touchpoint, or specific follow-up letter).

When the finding has been remediated through an MOU or consent order, the closure evidence references the MOU / consent-order satisfaction terms specifically.

##### MAR §16 material-weakness pathway

For insurers subject to MAR (most insurers above the state-defined threshold), unremediated material weaknesses in internal control over financial reporting trigger §16 notification to the state DOI. An issue write-up on a control deficiency that is heading toward material-weakness classification carries the §16 implication in the severity rationale; the criteria block cites MAR §16 directly.

##### ORSA-driven enterprise-risk findings

For ORSA-eligible insurers, findings on the enterprise-risk-management framework, risk-appetite-and-tolerance, or capital-adequacy assessment carry severity weight tied to the ORSA component implicated. The criteria block cites the relevant ORSA Guidance Manual section.

#### Common patterns

- **Multi-state market-conduct finding**. A market-conduct finding identified by one state often replicates across other states where the insurer is licensed; the issue write-up names the state of identification and flags the other-state implication in the impact section.
- **MOU resolution shape**. Many state DOI findings are resolved via MOU rather than via consent order; the MOU is the closure-evidence anchor. The MOU specifies the corrective action, the milestone schedule, and the DOI's re-inspection terms.
- **NAIC accreditation continuity**. Findings on the state DOI's own performance against NAIC accreditation standards do not appear in firm-side issue write-ups, but findings on the insurer that affect the DOI's accreditation evaluation can carry an indirect severity weight; flag in the severity rationale where applicable.

#### Implications for the CCCE

- **Criteria** for insurance-overlay issues cite the state insurance code section first (or NAIC Model Law section if the state has adopted the model), then NAIC handbook section second, then firm policy third. State-specific deviation from the NAIC model carries a separate criteria entry where applicable.
- **Cause** for market-conduct findings ties to the specific operational control that failed (claims-handling timeliness control, producer-licensing-verification control, complaint-handling-tracking control). For financial-reporting findings, the cause maps to a COSO component or principle as MAR adopts the COSO framework.
- **Effect** for insurance issues quantifies policyholder impact distinctly from financial impact distinctly from market-conduct violation impact. Consumer-harm scope is typically named in policyholder-count terms and dollar-restitution terms.
- **Closure evidence** for state-DOI-issued findings references the DOI's expected re-inspection touchpoint, not just the firm-internal sign-off cadence.

#### Anchors used by this overlay

- NAIC Financial Condition Examiners Handbook (current edition). https://content.naic.org/cmte_e_fcrr.htm [verify current edition section labels.]
- NAIC Market Regulation Handbook (current edition). https://content.naic.org/cmte_d_mar.htm [verify current edition section labels.]
- NAIC Annual Financial Reporting Model Regulation (Model 205) — MAR. https://content.naic.org/cmte_d.htm [verify current model regulation section labels.]
- NAIC ORSA Guidance Manual. https://content.naic.org/cmte_e_orsa.htm [verify current edition section labels.]
- NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023). [verify current state adoption status; bulletin adoption varies by state.]
- State-specific examination report and consent-order language patterns vary by state DOI; the firm-overlay names the state-specific anchors that apply to the insurer.

## payments-fintech

### Payments and fintech sector overlay — issue-writeup

Loads when the scope `sector_overlay_set` includes `payments-fintech`. The overlay shapes the criteria block, the severity calibration, and the closure-evidence framing for issues at money transmitters, payments processors, sponsor-bank programs, fintech bank partners, and non-bank consumer-finance providers.

#### Why the payments-fintech overlay matters

Payments and fintech sit across multiple regulator constellations: the CFPB on consumer-protection, FinCEN on BSA / AML, OCC / FRB / FDIC on bank-partnership oversight, state regulators on money transmitter licensing, and (for some firms) the Federal Trade Commission on UDAAP through the Gramm-Leach-Bliley Safeguards Rule. Findings come in via CFPB supervisory recommendations, OCC fintech bank-partnership supervisory letters, state money-transmitter examination findings, and FinCEN examination findings (often delivered through the IRS or the federal banking agencies on behalf of FinCEN). The criteria block, severity calibration, and closure-evidence framing differ from the federal banking convention, the state-DOI insurance convention, and the SEC / FINRA capital-markets convention.

#### Source basis

- **CFPB Supervisory Highlights and supervisory recommendations** — published priorities and observed-deficiency categories. Severity calibration tracks whether a recommendation moves toward an enforcement matter.
- **CFPB Examination Manual** — module-by-module examination procedures; criteria citations frequently come from the Compliance Management Review module, the UDAAP module, the Fair Lending module, and the product-specific modules (mortgage origination, deposit-and-card products, debt collection, etc.).
- **OCC Fintech Bank-Partnership Supervisory Letters** — the OCC's published guidance on bank partnerships with non-bank fintech companies, including expectations on the bank's third-party risk management for the fintech relationship and the bank's responsibility for consumer-protection compliance through the partnership.
- **OCC Bulletin 2020-10 and 2024 fintech-related guidance** — bank-partnership supervisory framework. [verify current bulletin numbering for fintech-specific guidance; the OCC has updated its fintech framework multiple times.]
- **State money-transmitter examination conventions** — varies by state; the Conference of State Bank Supervisors (CSBS) coordinates the State Examination System (SES) for multi-state exams, but each state's examination report carries state-specific format.
- **FinCEN examination findings via the IRS or the federal banking agencies** — BSA / AML examination findings on money services businesses follow the FFIEC BSA / AML Examination Manual conventions when delivered through the federal banking agencies; FinCEN-direct enforcement actions follow the FinCEN consent order convention.
- **Reg E (12 CFR Part 1005)** — Electronic Fund Transfers; consumer-protection rules on prepaid accounts, P2P, ACH, and similar electronic transfers. Severity calibration ties to the unauthorized-transfer-resolution timing, error-resolution timing, and disclosure rules.
- **Reg Z (12 CFR Part 1026)** — Truth in Lending; consumer-protection rules on closed-end credit, open-end credit, credit cards, and HELOCs.
- **NACHA Operating Rules** — for ACH-active firms, NACHA findings on origination, returns, and risk-management.

#### What the overlay adds to the write-up

##### CFPB supervisory recommendation format

When the source type is examiner-letter and the regulator is CFPB, the criteria block follows the CFPB's supervisory recommendation format. CFPB findings typically structure as:
- A **Matter Requiring Attention (MRA)** — the CFPB uses the MRA label even though it is not a federal-banking MRA. CFPB MRAs name a corrective action and an expected completion date. The `mra_mria_classification` field is set to `MRA` and the regulator is recorded as CFPB.
- A **public enforcement action** — the artifact is the consent order; the issue write-up references the consent order but the public consent-order language often becomes the criteria citation in any related issue write-ups.

Severity calibration for CFPB MRAs is typically high because the CFPB's MRA is roughly comparable to a federal-banking MRA in seriousness, but the consumer-impact dimension is foregrounded.

##### OCC fintech bank-partnership findings

When the source is an OCC supervisory letter on a fintech bank-partnership relationship, the finding is typically directed at the bank but carries operational implications for the fintech partner. The issue write-up at the bank cites the OCC bulletin and the interagency third-party guidance; the issue write-up at the fintech partner cites the bank's contractual remediation requirement and the underlying consumer-protection rule.

##### State money-transmitter examination findings

For multi-state money transmitters, the same finding may surface via state-by-state examinations or via a coordinated CSBS-SES exam. The criteria block names the state-specific statute first (most states map to the Money Transmitter Modernization Act framework but with state-specific variations), then the firm's policy second. Severity calibration tracks state-specific consumer-protection severity ladders.

##### FinCEN BSA / AML findings

When the source is a BSA / AML examination finding (delivered through the IRS for non-bank money services businesses or through the federal banking agencies for bank-partnered fintechs), the criteria block cites the Bank Secrecy Act, the relevant FinCEN regulation (31 CFR Chapter X), and the FFIEC BSA / AML Examination Manual section. Severity calibration for BSA / AML findings is typically high or critical because of the AML statutory framework's severity ladder; the consumer-impact dimension is replaced by the financial-crime-exposure dimension.

##### Severity calibration

Payments-fintech severity calibration weighs (1) consumer-protection impact (UDAAP, Reg E, Reg Z, fair-lending), (2) AML / sanctions / financial-crime impact, (3) bank-partnership reputational impact for sponsor-bank programs, (4) state-licensing impact for multi-state operations, and (5) operational-resilience impact for payment processors. UDAAP findings with identifiable consumer harm carry critical or high severity; UDAAP findings without identified harm carry moderate or high severity.

##### Closure-evidence framing

Closure evidence for CFPB MRAs names the corrective action plan, the implementation evidence (consumer-disclosure update, system change, policy update, training delivered, restitution paid where applicable), and the CFPB's expected continuous-monitoring touchpoint. For OCC fintech bank-partnership findings, closure evidence references both the bank-side remediation and the fintech-side remediation that satisfies the bank's contract. For state money-transmitter findings, closure evidence references state-specific remediation language.

#### Common patterns

- **Multi-state replication**. A consumer-protection finding identified in one state often replicates across other states the firm is licensed in; the issue write-up names the state of identification and flags the multi-state replication scope.
- **UDAAP findings with restitution**. Restitution-eligible UDAAP findings carry customer-count and dollar-restitution closure evidence specifically; the closure-evidence field names the restitution program, the consumer-notification process, and the third-party restitution-administrator (where used).
- **Bank-partnership pass-through**. Consumer-protection findings at a fintech bank-partner often surface as an MRA at the sponsor bank rather than as a direct supervisory action against the fintech; the bank's MRA cascades into the fintech's contractual remediation. The fintech-side issue write-up references the sponsor bank's MRA and the contractual cascade.
- **Sanctions and OFAC findings**. OFAC findings on screening, blocking, or reporting violations carry critical severity; the criteria block cites 31 CFR Chapter V (OFAC regulations) and the OFAC FAQ guidance. Closure evidence names the corrective screening program, the look-back lookback file, and the OFAC submission where applicable.

#### Implications for the CCCE

- **Criteria** for payments-fintech-overlay issues cite the federal consumer-protection rule first (Reg E, Reg Z, UDAAP, BSA / AML), then state-licensing or NACHA rule second, then firm policy third.
- **Cause** for consumer-protection findings ties to the specific operational control that failed (disclosure-generation control, error-resolution-timeliness control, credit-decision control, dispute-resolution-tracking control). For BSA / AML findings, cause maps to the specific AML control attribute (KYC / CIP control, transaction-monitoring control, SAR-filing-timeliness control, OFAC screening control).
- **Effect** for payments-fintech issues quantifies consumer-protection impact (consumer-count, dollar-restitution-scope, UDAAP exposure), AML / sanctions impact (transaction-volume, dollar-volume, geographic-exposure), and state-licensing implication distinctly.
- **Closure evidence** for CFPB MRAs and OCC fintech bank-partnership findings includes the corrective-action-plan response, the consumer-impact remediation (where applicable), and the readiness for the regulator's continuous-monitoring touchpoint.

#### Anchors used by this overlay

- CFPB Supervisory Highlights. https://www.consumerfinance.gov/compliance/supervisory-highlights/
- CFPB Examination Manual. https://www.consumerfinance.gov/compliance/supervision-examinations/
- 12 CFR Part 1005 (Reg E — Electronic Fund Transfers). https://www.ecfr.gov/current/title-12/chapter-X/part-1005
- 12 CFR Part 1026 (Reg Z — Truth in Lending). https://www.ecfr.gov/current/title-12/chapter-X/part-1026
- OCC Bulletin 2020-10 — Third-Party Relationships: Frequently Asked Questions for fintech bank-partnership context. [verify currency; the OCC has issued FAQ updates and 2024 fintech guidance.]
- 31 CFR Chapter X — FinCEN regulations (BSA / AML for money services businesses). https://www.ecfr.gov/current/title-31/subtitle-B/chapter-X
- 31 CFR Chapter V — OFAC regulations. https://www.ecfr.gov/current/title-31/subtitle-B/chapter-V
- FFIEC BSA / AML Examination Manual. https://bsaaml.ffiec.gov/manual
- NACHA Operating Rules and Guidelines. https://www.nacha.org/rules
- State-specific money transmitter licensing acts; CSBS State Examination System. https://www.csbs.org/state-examination-system
- Money Transmitter Modernization Act framework — model legislation adopted (with variations) by participating states. [verify state-by-state adoption status.]
