# Insurance sector overlay — test-plan-builder

Loaded when `engagement-scope.sector_overlay_set` includes `insurance` or when the test addresses NAIC, state DOI, or insurance-specific federal rules. Supplements `references/source-anchors.md`.

## Test-plan conventions insurance examiners expect

State DOI market-conduct examiners and NAIC accreditation reviewers read insurer test plans slightly differently from bank examiners. Two conventions matter most:

- **Statutory framework is the criterion, not the model.** State DOI examiners read against the state's adopted version of the NAIC model, not against the model itself. The plan cites the state-adopted citation (e.g., "N.Y. Ins. Law §X / 11 NYCRR §Y") with the NAIC model as a secondary reference. State-by-state adoption variance matters and the plan notes it where the test scope is multi-state.
- **Market-conduct sample design follows the NAIC Market Conduct Examiners Handbook** rather than AU-C 530 directly. The plan restates the sample-design rationale aligned to the Handbook's standards (file-review sample sizes, error-tolerance bands) and reconciles to AU-C 530 only where the firm's methodology has chosen it.

## Insurance-supervisory anchors (load by reference; do not restate)

- **NAIC Annual Financial Reporting Model Regulation (Model Audit Rule, Model #205)** [verify section references for the internal-control testing-program documentation expectation]. https://content.naic.org/cipr-topics/topic-naic-model-laws-and-regulations [verify URL].
- **NAIC Market Conduct Examiners Handbook** (current edition) [verify section labels]. https://content.naic.org/cmte_d_mceh.htm [verify URL].
- **NAIC Insurance Holding Company System Regulatory Act (Model #440) and Holding Company Model Regulation (Model #450)** [verify model numbers]. Form B and Form D filings carry plan-relevant disclosure for affiliated-vendor testing.
- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number]. ORSA testing posture for insurer programs; the plan references the ORSA section under review.
- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers** (December 4, 2023) [verify state-by-state adoption status]. AIS Program testing covers governance, risk management, validation, third-party AI accountability, monitoring, documentation, transparency, fairness. https://content.naic.org/sites/default/files/inline-files/2023-12-04%20Model%20Bulletin_Adopted_0.pdf [verify URL].

## Insurance-control-area test-plan notes

### Underwriting and pricing testing

- Test-plan conventions: criteria section names rate-filing-versus-applied-rate reconciliation as the substantive criterion; population is the policies issued during the period; design procedures cover the rate-engine configuration and the underwriting-rule mapping; operating procedures cover applicant-attribute reconciliation against the rate manual or rule engine output by sample.
- Predictive-model testing under state DOI bulletins (Colorado SB 21-169 implementing regulation [verify section], NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting [verify circular number]) uses the bulletin's required testing artifacts as the criteria list (governance documentation, fairness testing, third-party-AI accountability evidence).

### Claims handling testing

- Unfair Claims Settlement Practices Act state adoption [verify state citations], usually state-adopted versions of NAIC Model #900 [verify model number] or NAIC Model #902 [verify model number]. Test plan conventions: claims-handling test plans restate the acknowledgement-investigation-decision-payment timeline by sample with state-statutory clocks; the criteria section cites the state-adopted statute, not the NAIC model.

### Producer licensing and appointment testing

- Test-plan conventions: licensing-status reconciliation against the state DOI register (NIPR / SBS) by sample; appointment-status testing against the state DOI register; commission-payment testing against the licensed-and-appointed status as of transaction date. Criteria cite the state-adopted producer licensing act.

### Privacy and data-security testing

- NAIC Insurance Data Security Model Law (Model #668), §4.F third-party service-provider obligations [verify state-by-state adoption]. Plan conventions: criteria section names cybersecurity-program governance, incident-response testing, third-party-vendor diligence and monitoring evidence per the state-adopted version.
- NY DFS 23 NYCRR Part 500 applies to NY-licensed insurers as Covered Entities; cyber overlay applies in addition to insurance overlay where the firm holds a NY license.
- HIPAA Security Rule applies where the insurer is a covered entity (health, dental, vision); cyber and privacy overlays both load.

### ORSA Summary Report testing

- Test-plan conventions: ORSA-relevant test plans read risk-identification, risk-assessment, risk-monitoring, and group capital-adequacy sections; sample-level evidence is by risk type rather than by transaction. The plan limitations section flags that the ORSA itself is a management report; the testing plan concludes on the underlying control effectiveness, not on ORSA content.

## Multi-state and group-vs-entity scope

The plan is explicit about the legal entity under test and the states whose rules apply. A multi-state market-conduct test plan names primary state and concurrent states (where applicable under coordinated examinations). A group-level testing plan carries the holding-company structure and the parent-entity scope; the plan does not propose conclusions on legal-entity ICFR for non-tested entities.

## Audience and tone

A test plan drafted with an upcoming state DOI market-conduct exam in mind reads heavier on state-statutory citations, sample-design rationale aligned to the NAIC Market Conduct Examiners Handbook, and limitations on the period and lines of business covered. A plan drafted for the NAIC AIS Program reads heavier on third-party-AI accountability, validation, and fairness-testing evidence per the model bulletin's adopted text in the firm's domiciliary state.
