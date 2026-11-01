# Conduct cross-cutting overlay — qa-workpaper

Loaded when `scope.cross_cutting_overlay_set` includes `conduct`, when the QA review covers a workpaper that sampled a consumer-impact population, or when the underlying control test touches a UDAAP-relevant area. Supplements `references/source-anchors.md`.

## Why conduct QA carries distinct conventions

Conduct workpapers fail QA on conclusion-language hygiene more often than other workpapers. The recurring patterns:

- **Legal-violation framing in conclusions.** A workpaper concluding "the firm engaged in unfair or deceptive practices under Dodd-Frank §1031" or "the bank did not comply with Reg E §1005.11(c)" is a QA finding regardless of the underlying evidence; that conclusion is for legal counsel and the regulator, not the second-line workpaper.
- **Customer-harm framing collapsed into technical control conclusion.** A control may operate effectively at the technical dimension while customer harm is identifiable from the population (e.g., the dispute-resolution control operated within the timing clocks, but the population shows customers were charged fees during the investigation period that the firm should have reversed). The QA reviewer challenges whether customer-harm framing is carried separately from control-effectiveness framing.
- **UDAAP-relevant findings without the customer-impact analysis.** UDAAP exam procedures examine customer impact distinct from technical compliance; a workpaper concluding on a UDAAP-relevant control without the customer-impact analysis is a recurring deficiency.

## QA conventions for conduct-relevant workpapers

- **Conclusion-language rewrite.** The QA reviewer rewrites legal-violation framing to control-effectiveness framing and elevates the legal question to legal counsel and the head of regulatory affairs as a separate routing, not a conclusion in the workpaper.
- **Customer-harm framing carried separately.** The QA reviewer confirms the workpaper carries a separate customer-harm read where the population shows identifiable harm, distinct from the control-effectiveness conclusion.
- **UDAAP-relevant tests carry the abusive-prong consideration.** Dodd-Frank §1031 includes the "abusive" prong distinct from FTC Act §5 unfair-or-deceptive prongs. The QA reviewer confirms UDAAP-relevant workpapers consider all three prongs (unfair, deceptive, abusive) where applicable, not just the unfair-or-deceptive subset.

## Conduct-supervisory anchors (load by reference; do not restate)

- **CFPB UDAAP Examination Procedures** (CFPB Supervision and Examination Manual, UDAAP module) [verify section labels]. https://www.consumerfinance.gov/compliance/supervision-examinations/ .
- **Dodd-Frank §1031 (12 USC §5531) and §1036 (12 USC §5536)** — UDAAP authority. https://www.law.cornell.edu/uscode/text/12/5531 .
- **FTC Act §5 (15 USC §45)** — unfair or deceptive practices authority for institutions outside CFPB's direct UDAAP authority. https://www.law.cornell.edu/uscode/text/15/45 .
- **Interagency Policy Statement on Discrimination in Lending** [verify exact title and date for the most recent statement applicable to the firm's regulator constellation]. Used as the framing anchor when the underlying test touches fair-lending posture.

## Conduct-relevant control-area QA notes

### Reg E error-resolution conclusion language — QA scope items

- The QA reviewer rewrites "the bank did not comply with Reg E §1005.11(c)" to "the dispute-resolution control did not operate within the §1005.11(c) timing clock for the [population] sample during the period". The legal-violation question routes to legal counsel separately.

### Complaint-handling testing — QA scope items

- The QA reviewer confirms the workpaper carries a customer-harm read distinct from the control-effectiveness read. Complaint-handling controls may operate at the technical dimension (acknowledgement, routing, response timing) while the population shows resolution outcomes that warrant customer-impact analysis (refunds, account corrections, restitution).

### Fee-disclosure and fee-application testing — QA scope items

- The QA reviewer confirms fee-disclosure testing carries the regulatory-model redline and the noted deviations as control-effectiveness findings; fee-application testing carries the customer-harm dimension where unauthorised or mistakenly-applied fees are identified in the sample. The customer-harm dimension is distinct from the technical fee-disclosure conclusion.

### Marketing-practices and disclosure testing — QA scope items

- The QA reviewer confirms marketing-practices testing carries the deceptive-prong consideration distinct from the unfair-prong; reliance on the firm's marketing-review approval evidence does not substitute for sampling marketing materials against the disclosure rules.

### Fair-lending and disparate-impact testing — QA scope items

- The QA reviewer confirms fair-lending testing distinguishes statistical disparities (which warrant further analysis) from disparate-treatment findings (which require evidence of intent or a substantially-similar-applicant comparison). The QA reviewer challenges any conclusion drifting toward "the firm engaged in disparate-treatment discrimination" without the underlying evidence; statistical-disparity findings route to the head of fair lending and legal counsel separately.

## Audience and tone

A QA review note drafted with an upcoming CFPB or DOJ exam in mind reads heaviest on conclusion-language hygiene, the customer-harm framing, and the UDAAP all-three-prongs consideration. A QA note for in-cycle testing-program closure reads operationally with the same dimensions but lighter on the examiner-prep posture. The conclusion-language rewrite is the most-recurring intervention; firms with strong conduct posture build the rewrite into the testing-template default rather than relying on the QA reviewer to catch it every cycle.
