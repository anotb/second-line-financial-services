# Insurance sector overlay — workpaper-drafter

Loaded when `scope.sector_overlay_set` includes `insurance` or when the test addresses NAIC, state DOI, or insurance-specific federal rules. Supplements `references/source-anchors.md`.

## Workpaper conventions insurance examiners expect

State DOI market-conduct examiners and NAIC accreditation reviewers read insurer testing workpapers slightly differently from bank examiners. Two conventions matter most:

- **Statutory framework is the criterion, not the model.** State DOI examiners read against the state's adopted version of the NAIC model, not against the model itself. The workpaper cites the state-adopted citation (e.g., "N.Y. Ins. Law §X / 11 NYCRR §Y") with the NAIC model as a secondary reference. State-by-state adoption variance matters and the workpaper notes it where the test scope is multi-state.
- **Market-conduct sample design follows the NAIC Market Conduct Examiners Handbook** rather than AU-C 530 directly. The workpaper restates the sample-design rationale aligned to the Handbook's standards (file-review sample sizes, error-tolerance bands) and reconciles to AU-C 530 only where the firm's methodology has chosen it.

## Insurance-supervisory anchors (load by reference; do not restate)

- **NAIC Annual Financial Reporting Model Regulation (Model Audit Rule, Model #205)** [verify section references]. ICFR-relevant testing documentation conventions and auditor-management coordination expectations. https://content.naic.org/cipr-topics/topic-naic-model-laws-and-regulations [verify URL].
- **NAIC Market Conduct Examiners Handbook** (current edition) [verify section labels]. https://content.naic.org/cmte_d_mceh.htm [verify URL].
- **NAIC Insurance Holding Company System Regulatory Act (Model #440) and Holding Company Model Regulation (Model #450)** [verify model numbers]. Form B and Form D filings carry workpaper-relevant disclosure for affiliated-vendor testing.
- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number]. ORSA Summary Report content is itself the subject of testing for material risk areas; the workpaper for ORSA-relevant testing references the ORSA section under review.
- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers** (December 4, 2023) [verify state-by-state adoption status]. AIS Program testing covers governance, risk management, validation, third-party AI accountability, monitoring, documentation, transparency, fairness. https://content.naic.org/sites/default/files/inline-files/2023-12-04%20Model%20Bulletin_Adopted_0.pdf [verify URL].

## Insurance-control-area workpaper notes

### Underwriting and pricing testing

- Workpaper conventions: rate-filing-versus-applied-rate reconciliation by sample; pricing model governance testing reads model-version-pin against the date of policy effective; underwriting-rule application testing reconciles applicant attributes against the rate manual or rule engine output.
- Predictive-model testing under state DOI bulletins (Colorado SB 21-169 implementing regulation [verify section], NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting [verify circular number]) reads against the bulletin's required testing artifacts (governance documentation, fairness testing, third-party-AI accountability evidence).

### Claims handling testing

- Unfair Claims Settlement Practices Act state adoption [verify state citations], usually state-adopted versions of NAIC Model #900 [verify model number] or NAIC Model #902 [verify model number]. Testing reads acknowledgement timing, investigation timing, settlement timing, denial-letter content by sample.
- Workpaper conventions: claims-handling samples restate the acknowledgement-investigation-decision timeline by sample with state-statutory clocks; the criteria section cites the state-adopted statute, not the NAIC model.

### Producer licensing and appointment testing

- Workpaper conventions: licensing-status reconciliation against the state DOI register (NIPR / SBS) by sample; appointment-status testing against the state DOI register; commission-payment testing against the licensed-and-appointed status as of transaction date.

### Privacy and data-security testing

- NAIC Insurance Data Security Model Law (Model #668), §4.F third-party service-provider obligations [verify state-by-state adoption]. Testing reads cybersecurity-program governance, incident-response testing, third-party-vendor diligence and monitoring evidence.
- NY DFS 23 NYCRR Part 500 applies to NY-licensed insurers as Covered Entities; cyber overlay applies in addition to insurance overlay where the firm holds a NY license.
- HIPAA Security Rule applies where the insurer is a covered entity (health insurer, dental, vision); cyber and privacy overlays both load.

### ORSA Summary Report testing

- Workpaper conventions: ORSA-relevant testing reads risk-identification, risk-assessment, risk-monitoring, and group capital-adequacy sections; sample-level evidence is by risk type rather than by transaction. The workpaper limitations section flags that the ORSA itself is a management report; the testing concludes on the underlying control effectiveness, not on ORSA content.

## Multi-state and group-vs-entity scope

The workpaper is explicit about the legal entity under test and the states whose rules apply. A multi-state market-conduct test names primary state and concurrent states (where applicable under coordinated examinations). A group-level testing workpaper carries the holding-company structure and the parent-entity scope; the workpaper does not conclude on legal-entity ICFR for non-tested entities.

## Audience and tone

A workpaper drafted with an upcoming state DOI market-conduct exam in mind reads heavier on state-statutory citations, sample-design rationale aligned to the NAIC Handbook, and limitations on the period and lines of business covered. A workpaper drafted for the NAIC AIS Program reads heavier on third-party-AI accountability, validation, and fairness-testing evidence per the model bulletin's adopted text in the firm's domiciliary state.
