# Conduct cross-cutting overlay — test-plan-builder

Loaded when `engagement-scope.cross_cutting_overlay_set` includes `conduct`, when the test addresses consumer-facing controls (UDAAP, fair-lending, sales-practices, complaint-handling), or when customer-harm framing matters separately from the technical control conclusion. Supplements `references/source-anchors.md`.

## Test-plan conventions for conduct-relevant testing

Conduct-relevant test plans carry a consumer-harm read distinct from the substantive control read. Two conventions matter:

- **Customer-harm framing is a separate conclusion lens that the plan sets up at planning time.** A control can be operating effectively as designed and still produce customer harm if the design embeds an unfair, deceptive, or abusive feature. The plan names the substantive control conclusion (effective / partially effective / not effective) and a separate consumer-harm read where applicable. The conduct overlay does not collapse the two reads.
- **Disclosure-content testing requires the production version.** Disclosure test plans target the disseminated disclosure (customer-facing) rather than the master template. Test-environment disclosures and pre-production disclosures are not the population; the plan defines population as the disclosure as the customer received it, by sample of customer interactions, and names the production-extract source.

## Conduct-supervisory anchors (load by reference; do not restate)

- **CFPB UDAAP Examination Procedures** (CFPB Supervision and Examination Manual, UDAAP module) [verify section labels]. https://www.consumerfinance.gov/compliance/supervision-examinations/ .
- **Dodd-Frank §1031 (12 USC §5531) and §1036 (12 USC §5536)** — UDAAP authority. The "abusive" prong is statutorily distinct from FTC Act §5 unfair or deceptive prongs; test plans covering abusive-act analysis cite §1031(d) directly. https://www.law.cornell.edu/uscode/text/12/5531 .
- **FTC Act §5 (15 USC §45)** — unfair or deceptive acts or practices. Applies to non-bank firms outside CFPB authority and to bank holding companies via FRB authority. https://www.law.cornell.edu/uscode/text/15/45 .
- **CFPB compliance bulletins on consumer-harm framing** [verify specific bulletin numbers and dates]. https://www.consumerfinance.gov/compliance/supervisory-guidance/ .
- **Reg B / ECOA — 12 CFR Part 1002**, especially §1002.4 (general rule against discrimination) and §1002.6 (rules concerning evaluation of applications) [verify subsection labels]. https://www.ecfr.gov/current/title-12/chapter-X/part-1002 .
- **Fair Housing Act (42 USC §3601 et seq.)** for housing-related credit testing. https://www.law.cornell.edu/uscode/text/42/3601 .
- **Servicemembers Civil Relief Act (50 USC §3901 et seq.)** for SCRA-relevant testing. https://www.law.cornell.edu/uscode/text/50/3901 .
- **NAIC Unfair Trade Practices Act (Model #880) and Unfair Claims Settlement Practices Act (Model #900)** [verify model numbers and state-by-state adoption]. State-adopted versions cite the state statute primarily.
- **FINRA Rule 2010 (Standards of Commercial Honor) and Rule 2111 (Suitability)** [verify subsection labels]. https://www.finra.org/rules-guidance/rulebooks/finra-rules/2010 .
- **SR 11-7 — Supervisory Guidance on Model Risk Management** (Federal Reserve / OCC Bulletin 2011-12, April 4, 2011) [verify section labels]. Referenced when the test plan addresses model-driven consumer-impact controls (e.g., AI-driven underwriting decisioning). https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm .

## Conduct-control-area test-plan notes

### UDAAP testing

- Test-plan conventions: criteria section cites the relevant CFPB bulletin or the Dodd-Frank §1031 / §1036 statutory text; population includes consumer-facing materials (disclosures, marketing, fee schedules, dispute responses, account-servicing communications), customer-experience evidence (call recordings, chat transcripts, app screen flows), and complaint-pattern evidence. The substantive control conclusion is on whether the firm's UDAAP control framework is operating; the consumer-harm read is whether observed practices show a substantive UDAAP risk regardless of control framework effectiveness.
- The "abusive" prong testing under §1031(d) reads against the four statutory tests (material interference with ability to understand a term or condition; taking unreasonable advantage of lack of understanding; taking unreasonable advantage of inability to protect interests; taking unreasonable advantage of reasonable reliance on a covered person to act in the consumer's interest) [verify exact statutory language]. The plan does not pre-judge the legal test; it surfaces evidence relevant to the test for legal review.

### Fair-lending testing (ECOA, FHA)

- Test-plan conventions: fair-lending test plans cover underwriting (disparate-treatment file review, comparative-file analysis), pricing (overage and underage analysis, spread distribution by prohibited basis), redlining (geography distribution), marketing (channel and language coverage), and steering (product-mix distribution). Disparate-impact analysis is statistical; the plan carries the model design, the variables included and excluded, and the limitations.
- The plan restates the prohibited bases (race, colour, religion, national origin, sex, marital status, age, public-assistance income, exercise of a right under the CCPA, ECOA-protected activity) [verify Reg B §1002.2(z)] and the protected classes under FHA where applicable.

### Sales-practices testing (broker-dealer suitability and recommendation)

- Test-plan conventions: suitability test plans under FINRA Rule 2111 cover the recommendation, the customer profile, and the rationale by sample; Reg BI test plans for retail customers cover the Care Obligation, Conflict of Interest Obligation, and Disclosure Obligation evidence. Customer-impact framing covers commission-overweight recommendations, complex-product placements with retail customers, and compensation-driven product-mix distortion.

### Complaint-handling testing

- Test-plan conventions: complaint-handling test plans cover complaint intake, classification, investigation, response, root-cause analysis, and trend reporting. Reg E §1005.11 error-resolution overlaps with complaint testing where the complaint is also a §1005.11 dispute; the plan tracks both regulatory clocks. Complaint-pattern review feeds the consumer-harm read independent of control-framework effectiveness.

### Insurance unfair-trade-practices and unfair-claims-settlement testing

- Test-plan conventions: state-adopted UTPA and UCSPA test plans cover the state-specific definitions of unfair practices; multi-state plans carry state-by-state variance. Claims-handling timing test plans cover the state-statutory clocks (acknowledgement, investigation, decision, payment) by sample.

## Customer-harm framing in the plan's pass and fail criteria

The plan's pass and fail criteria, when the conduct overlay is loaded, can carry an additional read: the substantive control criterion plus a consumer-harm signal criterion ("consumer-harm signal observed: yes / no / inconclusive" with rationale). This signal read is not a legal conclusion (legal conclusions sit with counsel); it is the testing-program's surfacing of evidence relevant to the legal-conduct dimension. The plan's reviewer-questions section flags any anticipated consumer-harm signal for legal review distinct from control-framework remediation.

## Distinctness from technical control conclusion

A test plan covering a fee-disclosure control may set up a substantive procedure on whether the disclosure is delivered as designed (a control-effectiveness read) and a separate procedure on whether the disclosure as designed is unclear, misleading, or abusive (a consumer-harm read). The two reads sit side by side; the plan does not collapse them. Issue-writeup downstream may produce two issues (a control-effectiveness finding and a consumer-harm finding) from the same workpaper.

## Audience and tone

A test plan drafted for the firm's CCO and the conduct-risk committee reads heavier on the consumer-harm read, complaint-pattern evidence, and the customer-experience evidence the cycle will inspect. A plan drafted with an upcoming CFPB exam in mind reads heavier on UDAAP module references, complaint-handling evidence, and customer-experience evidence (call recordings, chat transcripts). A plan drafted for fund-board reporting on adviser conduct reads heavier on suitability and Reg BI evidence with the customer-base distribution as context.
