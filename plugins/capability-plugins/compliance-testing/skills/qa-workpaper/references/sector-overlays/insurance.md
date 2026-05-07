# Insurance sector overlay — qa-workpaper

Loaded when `engagement-scope.sector_overlay_set` includes `insurance` or when the QA review covers a workpaper at an insurer or insurance holding company. Supplements `references/source-anchors.md`.

## QA conventions for insurance testing workpapers

Insurance second-line testing workpapers carry methodology distinct from bank consumer-compliance testing:

- **Model Audit Rule ICFR documentation review.** ICFR-relevant tests at insurers reportable under the NAIC Model Audit Rule (Model #205) carry documentation review by the firm's audit committee and external auditor; the QA reviewer challenges whether the workpaper's documentation supports the ICFR-attestation posture, not just the testing-program posture. Severity calibration on ICFR-relevant deficiencies carries Section-404-equivalent framing (deficiency / significant deficiency / material weakness) per AU-C 265.
- **Market-conduct workpaper review reads against state DOI examination standards.** State DOI market-conduct examiners apply the NAIC Market Conduct Examiners Handbook conventions when reading firm self-testing files. The QA reviewer confirms the workpaper's evidence inspection posture matches what the examiner would re-perform: claim-file sample reperformance, complaint-handling timeline reperformance, agent-licensing reconciliation.
- **Producer-licensing and appointment workpapers.** A recurring QA finding is reliance on the firm's producer-licensing system without an independent reconciliation against the NAIC State Producer Licensing Database (PLDB) or the state DOI license verification page. The QA reviewer challenges whether the reconciliation evidence is documented.

## Insurance-supervisory anchors (load by reference; do not restate)

- **NAIC Annual Financial Reporting Model Regulation (Model Audit Rule, Model #205)** [verify section references for ICFR documentation review and audit-committee oversight]. https://content.naic.org/cipr-topics/topic-naic-model-laws-and-regulations [verify URL].
- **NAIC Market Conduct Examiners Handbook** (current edition) [verify section labels for the workpaper-review conventions state DOI examiners apply]. https://content.naic.org/cmte_d_mceh.htm [verify URL].
- **NAIC Financial Condition Examiners Handbook** (current edition) [verify section labels for ICFR-relevant audit-quality conventions]. https://content.naic.org/cmte_e_ex_ws_handbook.htm [verify URL].

## Insurance-control-area QA notes

### Claim-handling timeliness and unfair-claims-settlement testing

- State Unfair Claims Settlement Practices acts (state-by-state) [verify state citations applicable to the firm's licensed states]. The QA reviewer challenges whether the claim-file sample carries the timing reperformance against the state's specified clocks (acknowledgement, investigation, decision, payment), and whether the sample stratification by claim type and state reflects the population.

### Producer-licensing and appointment testing

- State producer-licensing rules (state-by-state) [verify state citations]. NAIC PLDB. The QA reviewer confirms the producer-licensing extract reconciles against PLDB or the state DOI verification page, not just against the firm's internal CRM-licensing field.

### Underwriting and rating testing

- State rating-rule files and the firm's filed rate manual. The QA reviewer challenges whether the underwriting-file sample reperformance reads against the firm's filed rate manual (the version effective on the policy date), not the current version.

### ICFR-relevant testing under the Model Audit Rule

- The QA reviewer reads the workpaper against the AU-C 265 deficiency / significant deficiency / material weakness severity hierarchy and against the firm's ICFR-attestation posture. A workpaper severity-rated low on an ICFR-relevant control may still warrant a significant-deficiency communication if the control failure is reasonably possible to result in a material misstatement; the QA reviewer challenges the severity-to-ICFR-communication mapping.

## Audience and tone

A QA review note drafted for an insurance workpaper reads heavier on the ICFR-attestation posture when the test is ICFR-relevant, heavier on the state DOI market-conduct conventions when the test is market-conduct-relevant, and heavier on the producer-licensing reconciliation when the test touches producer activity. A QA note drafted with an upcoming state DOI market-conduct exam in mind reads heaviest on the claim-file sample reperformance posture.
