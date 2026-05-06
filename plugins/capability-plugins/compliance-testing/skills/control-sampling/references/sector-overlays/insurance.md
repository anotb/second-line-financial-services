# Insurance sector overlay — control-sampling

Loaded when `engagement-scope.sector_overlay_set` includes `insurance` or when the test addresses NAIC or state-DOI rules. Supplements `references/source-anchors.md` with insurance-specific population, stratification, and tolerable-rate conventions.

## Population definition conventions insurance examiners expect

State DOI market-conduct examiners and NAIC-aligned internal auditors carry conventions beyond the general sampling baseline:

- **Populations are defined by transaction type and policy line.** Claims handled in the period (closed-without-payment, closed-with-payment, denied, reopened); underwriting decisions issued in the period (new business, renewal, declination, non-renewal, cancellation); complaints received in the period (DOI-routed, direct-to-carrier); policy forms in force during the period.
- **Multi-state populations stratify by state.** State-by-state variance in adopted statutes (UTPA, UCSPA, claims-handling clocks) drives stratification. Multi-state samples carry per-state buckets so per-state findings do not get lost in an aggregate read.
- **Population pulls reconcile to the policy administration system or claims management system control totals.** The memo names the system, the extract date, the cut-off treatment (claim-closed-date, policy-effective-date, complaint-received-date), and the reconciliation result.

## Insurance-supervisory anchors (load by reference; do not restate)

- **NAIC Annual Financial Reporting Model Regulation (Model Audit Rule, Model #205)** [verify section references for ICFR-relevant sampling conventions and adoption status by state]. https://content.naic.org/cipr-topics/topic-naic-model-laws-and-regulations [verify URL].
- **NAIC Market Conduct Examiners Handbook** (current edition) [verify section labels for the standardised data calls, sampling conventions, and tolerable-rate conventions on claims, underwriting, complaint, and policy-form populations]. https://content.naic.org/cmte_d_mceh.htm [verify URL].
- **NAIC Unfair Trade Practices Act (Model #880)** and **Unfair Claims Settlement Practices Act (Model #900)** [verify model numbers and state-by-state adoption]. State-adopted versions carry the operative statutory citation.
- **NAIC Corporate Governance Annual Disclosure Model Act (Model #305)** and **Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model numbers and adoption status]. ORSA-relevant testing samples carry the risk-assessment-driven scope from the firm's ORSA filing.

## Insurance-control-area sampling notes

### Claims-handling testing

- Sampling conventions: claims-handling testing samples closed claims with stratification by claim type (auto bodily injury, auto property damage, homeowners, commercial liability, life, health, workers' comp), claim outcome (paid, denied, closed-without-payment, reopened), claim severity (by reserve at close), and claim aging (within 30 days, 31-90 days, over 90 days). State-statutory clock tests (acknowledgement within X days, decision within Y days, payment within Z days) sample by claim-state and apply the state-specific tolerable rate. Tolerable rates for unfair-claims-settlement-practices populations are typically zero or near-zero in firm methodology because the regulatory frame is enforcement-oriented.

### Underwriting testing

- Sampling conventions: underwriting samples new-business and renewal decisions with stratification by product line, distribution channel (agent, broker, direct, MGA), state, and decision outcome. Rating-accuracy tests sample issued policies with stratification by rating territory, product, and rate-revision wave. Disparate-treatment testing under state-adopted ECOA-equivalents (where applicable) follows fair-lending stratification conventions.

### Complaint-handling testing

- Sampling conventions: complaint testing samples received complaints with stratification by complaint source (DOI-routed, direct-to-carrier, social-media-escalation), complaint type (claim, underwriting, billing, sales-practices), and resolution status. DOI-routed complaints typically carry a separate read because the DOI-response timing is a regulator-facing population with a state-specific clock.

### Policy-form testing

- Sampling conventions: policy-form-content testing samples policies issued in the period with stratification by product and state. Form-filing-status tests reconcile the policy-form library against the state-filed-form register; the population is forms in force during the period and stratification is by state.

### Producer-licensing testing

- Sampling conventions: producer-licensing testing samples policies sold in the period with stratification by producer state, producer type (individual, agency), and product. The control population is policies-with-an-unlicensed-producer-event; tolerable rate is typically zero per state law.

## ORSA-aligned sampling

When the test sits inside the ORSA risk-assessment scope:

- Population definition follows the ORSA-identified risk register; sampling targets controls mitigating the highest-rated risks per the ORSA filing. The memo references the ORSA filing year and the firm's risk-rating methodology.
- Tolerable rates for ORSA-relevant controls draw from firm methodology calibrated against the ORSA-identified risk appetite; the criterion source names the ORSA filing as well as the firm methodology.

## Audience and tone

A sampling memo drafted with an upcoming state DOI market-conduct examination in mind reads heavier on the state-statutory clock citations, the per-state stratification rationale, and the standardised-data-call alignment from the NAIC Market Conduct Examiners Handbook. A memo drafted for the firm's actuarial or financial reporting context (Model #205-relevant) reads heavier on the ICFR-control-effectiveness frame. ORSA-aligned reads carry the risk-rating context as a stratification driver.
