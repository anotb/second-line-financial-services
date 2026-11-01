# Insurance sector overlay — contract-gap-review

When the scope flags insurance, load this overlay alongside `references/source-anchors.md`. The insurance overlay carries the clause expectations the bank-flavoured capability skill does not own.

## Vendor and contract types specific to insurance

The matrix must recognise the insurance-specific contract population: managing general agent (MGA) agreement, managing general underwriter (MGU) agreement, third-party administrator (TPA) agreement, claims-administrator agreement, underwriting-bureau agreement, actuarial-services agreement, IT outsourcing agreement, AI / ML vendor agreement, ECDIS data-provider agreement, illustration-software-vendor agreement, reinsurance-services-vendor agreement (distinct from a reinsurance treaty itself). Each pulls a different model-law clause set into the matrix.

## Operative model-law clause anchors

- **NAIC Insurance Data Security Model Law (Model #668), §4.F third-party service-provider obligations**: written-contract terms requiring information-security safeguards, monitoring, incident-response cooperation, and breach-notification chain. Distinct from federal interagency-guidance third-party expectations. State-by-state adoption; the NAIC adoption tracker is the public reference. Where adopted, the §4.F contract clauses are mandatory-by-source; absence is a `high`-severity finding.

- **NAIC Insurance Holding Company System Regulatory Act (Model #440)** [verify model number] and **Holding Company Model Regulation (Model #450)** [verify model number]: affiliate-services contracts (Form B, Form D) have prescribed content (cost-allocation methodology, term, termination, access to books and records by the domiciliary regulator). The contract gap matrix must evidence the prescribed clauses where the vendor is an affiliate.

- **NAIC Producer Licensing Model Act** [verify model number]: any vendor exercising binding or producer authority requires per-state producer licensing. The contract must reflect the per-state authorisation, including limitations on binding authority and termination triggers on licence loss.

- **NAIC Unfair Trade Practices Act (Model #880)** and the carrier's state-by-state unfair-claims-settlement-practices acts: where the vendor sits in a claims process, the contract must support the carrier's compliance with the acts (timing, customer-communication, fair-dealing standards). Pass-through accountability does not absolve the carrier; the contract clauses must enable the carrier's oversight.

- **State Department of Insurance bulletins** on specific outsourced functions where the carrier is licensed; pin the bulletins by state and date.

## ORSA and ERM fit

- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number]: critical outsourced functions belong in the ORSA Summary Report. Contracts for ORSA-fit vendors must include the information-access clauses that enable the carrier to populate the ORSA narrative (operational-resilience evidence, sub-contractor footprint, exit posture).

## AI vendor mode at an insurer

When `ai_vendor=true` and the firm is an insurer:

- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023)**: the carrier remains accountable for vendor and third-party AI used on its policies. The contract gap matrix must include rows for AIS-Program-aligned vendor obligations: governance access, validation evidence access, third-party-AI accountability flow-down, monitoring evidence access, documentation access, transparency to the carrier, fairness-testing cooperation. State-by-state adoption; consult the NAIC AI Working Group adoption tracker.

- **Colorado SB 21-169 implementing regulation** (3 CCR 702-10 §1 [verify section]) and parallel state regulations on ECDIS and predictive models in life-insurance underwriting: the contract must support governance, testing, validation, and consumer-recourse obligations the carrier holds. https://doi.colorado.gov/ [verify exact citation].

- **NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting** (January 2024) [verify exact circular number]: equivalent contract reach for NY-licensed life carriers.

## Cross-link inside the plugin

- **`exit-plan` insurance overlay** carries the in-force-policy-servicing wind-down sequence, the regulator-notification posture for an outsourced critical function, and the Form D filing implications for an affiliate-services exit. The contract gap matrix should evidence the contract clauses that enable each of those exit steps.

## Common insurance pitfalls

- Missing the §4.F clause set on a TPA or MGA contract because the federal interagency-guidance frame was applied alone. The federal frame does not cover §4.F third-party-service-provider contract terms.
- Missing the Form D clause set on an affiliate-services agreement. Affiliate-services contracts have prescribed content under Model #450; absence is a `high`-severity finding.
- Reading "AIS Program elements" as a single clause. The Bulletin lists multiple program elements; each translates into a distinct contract-row obligation on the vendor.
- Treating producer-licensing as procurement's problem. The contract must reflect per-state authorisation and the licence-loss termination trigger; it is a contract-row finding.
