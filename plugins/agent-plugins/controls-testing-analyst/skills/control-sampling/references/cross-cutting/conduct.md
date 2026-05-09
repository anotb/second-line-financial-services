# Conduct cross-cutting overlay — control-sampling

Loaded when `scope.cross_cutting_overlay_set` includes `conduct`, when the test addresses consumer-facing controls (UDAAP, fair-lending, sales-practices, complaint-handling), or when stratification by customer segment matters separately from the technical control conclusion. Supplements `references/source-anchors.md`.

## Population definition conventions for conduct-relevant sampling

Conduct-relevant sampling carries population conventions distinct from substantive-control sampling:

- **Populations are customer interactions, not transactions.** Disclosure-delivery events to customers in the period; complaints received in the period; customer-service calls handled in the period; sales recommendations made in the period; account-servicing communications sent in the period. The customer-experience artifact is the population item.
- **The disclosure population is the disseminated disclosure, not the master template.** Test-environment disclosures and pre-production disclosures are not the population; the population is the disclosure as the customer received it.
- **Complaint populations stratify by intake channel because routing differences embed risk.** DOI-routed, regulator-routed (CFPB consumer complaint database), social-media-escalation, branch-walk-in, call-centre, and direct-to-online routes carry different risk profiles and resolution clocks.
- **Call recordings and chat transcripts are populations in their own right.** Sampling pulls customer interactions with stratification by call type and disposition. Access controls on the recording library may constrain the sample (the memo names the access-control posture and any sample-size constraint that flows from it).

## Conduct-supervisory anchors (load by reference; do not restate)

- **CFPB UDAAP Examination Procedures** (CFPB Supervision and Examination Manual, UDAAP module) [verify section labels]. https://www.consumerfinance.gov/compliance/supervision-examinations/ .
- **Dodd-Frank §1031 (12 USC §5531) and §1036 (12 USC §5536)** — UDAAP authority. The "abusive" prong is statutorily distinct from FTC Act §5 unfair or deceptive prongs. https://www.law.cornell.edu/uscode/text/12/5531 .
- **FTC Act §5 (15 USC §45)** — unfair or deceptive acts or practices. https://www.law.cornell.edu/uscode/text/15/45 .
- **Reg B / ECOA — 12 CFR Part 1002**, especially §1002.4 and §1002.6 [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1002 .
- **Fair Housing Act (42 USC §3601 et seq.)** for housing-related credit testing. https://www.law.cornell.edu/uscode/text/42/3601 .
- **Servicemembers Civil Relief Act (50 USC §3901 et seq.)** for SCRA-relevant testing. https://www.law.cornell.edu/uscode/text/50/3901 .
- **NAIC Unfair Trade Practices Act (Model #880) and Unfair Claims Settlement Practices Act (Model #900)** [verify model numbers and state-by-state adoption]. State-adopted versions cite the state statute primarily.
- **FINRA Rule 2010 (Standards of Commercial Honor) and Rule 2111 (Suitability)** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/2010 .

## Conduct-control-area sampling notes

### UDAAP sampling

- Sampling conventions: UDAAP testing pulls multiple populations because the UDAAP frame covers consumer-facing materials, customer interactions, and complaint patterns. Disclosure-delivery events sample with stratification by disclosure type, channel, and product. Customer-experience populations (call recordings, chat transcripts, app screen flows) sample with stratification by interaction type. Complaint-pattern populations sample with theme and product stratification. Tolerable rates for UDAAP-relevant populations carry the customer-impact frame; the memo names the customer-impact rationale alongside the rate.

### Fair-lending sampling (ECOA, FHA)

- Sampling conventions: fair-lending sampling carries multiple populations across the lending lifecycle. Underwriting-decision sampling stratifies by product, prohibited basis variable (race, ethnicity, sex, marital status, age), and underwriting outcome; comparative-file analysis pulls matched-pair samples within strata. Pricing sampling stratifies by spread tier and prohibited-basis variable. Redlining analysis samples geographies with stratification by demographic composition. Marketing sampling stratifies by channel and language coverage. Disparate-impact analysis is statistical; the sampling memo carries the model design separately from the population definition.

### Sales-practices sampling (broker-dealer suitability and Reg BI)

- Sampling conventions: suitability sampling under FINRA Rule 2111 pulls recommendations made in the period with stratification by product complexity, customer type, and registered representative experience. Reg BI testing for retail customers pulls Care, Conflict, Disclosure, and Compliance Obligation evidence by sample. Tolerable rates for high-complexity-with-retail-customer combinations are typically lower per firm methodology because customer-impact framing concentrates risk.

### Complaint-handling sampling

- Sampling conventions: complaint-handling sampling pulls complaints received in the period with stratification by intake channel, complaint type, product, and resolution outcome. Reg E §1005.11 error-resolution overlap with complaint sampling: where the complaint is also a §1005.11 dispute, the case appears in both populations and the sample-design notes the dual-track tracking. Complaint-pattern review feeds the consumer-harm read independent of control-framework effectiveness; sample design supports the pattern read with theme stratification.

### Insurance unfair-trade-practices and unfair-claims-settlement sampling

- Sampling conventions: state-adopted UTPA and UCSPA sampling pulls populations against the state-specific statutory definitions. Multi-state samples carry per-state stratification because state-by-state variance drives the operative criterion. Claims-handling timing populations sample against state-statutory clocks (acknowledgement, investigation, decision, payment).

## Customer-impact framing in stratification

When the conduct overlay is loaded, stratification often carries a customer-impact dimension that is not a technical-control dimension:

- Vulnerable-population segments (servicemembers under SCRA, older customers, limited-English-proficiency customers, customers in financial hardship) get oversampled where firm methodology recognises the elevated impact of control failures on these segments.
- Low-balance or low-income customers in fee-related testing get oversampled because the dollar impact relative to account size concentrates harm.
- High-volume-low-dollar populations (small-amount fee testing, micro-transaction populations) get sampled with attention to the cumulative effect read, not just the per-item read.

The memo names these stratification choices explicitly; oversampling on customer-impact dimensions is a methodology call that a reviewer can challenge or affirm.

## Audience and tone

A sampling memo drafted for the firm's CCO and the conduct-risk committee reads heavier on the customer-impact stratification rationale and the complaint-pattern populations. A memo drafted with an upcoming CFPB exam in mind reads heavier on UDAAP module references, complaint-handling populations, and customer-experience populations (call recordings, chat transcripts) with attention to the customer-impact frame in tolerable-rate setting. A memo drafted for fund-board reporting on adviser conduct reads heavier on suitability and Reg BI populations with the customer-base distribution as context.
