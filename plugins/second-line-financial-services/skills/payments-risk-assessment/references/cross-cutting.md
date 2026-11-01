# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Cross-cutting overlay — conduct (UDAAP)

Default-on for any payments program touching consumers. Conduct exposure on a payments program is the highest-frequency examiner-finding lane: the CFPB's Supervisory Highlights and consent-order series have run continuously on these themes through 2023-26.

The overlay carries the theme list to read into the segment matrix and the cross-cutting UDAAP row. It does not substitute for the deeper review in `udaap-risk-review` (with the payments-fintech overlay); the assessment raises the flag and points to the deep-dive.

#### Anchor frame

- **Dodd-Frank Act §§1031, 1036** — UDAAP authority for the CFPB.
- **CFPB Supervisory Highlights (current cycles)** — verify which issues are current and which themes are flagged on the analysis date.
- **CFPB Circular series** — verify which circulars are current.
- **FDIC misrepresentation rule, 12 CFR Part 328 Subpart B** — standards for non-bank entities holding out deposit insurance.
- **Reg E (12 CFR Part 1005)** §1005.6 unauthorised-transfer liability and §1005.11 dispute-timing — failures here are pursued as both Reg E findings and UDAAP findings.
- **CFPB BNPL / Pay-in-Four Interpretive Rule** — **nullified by Pub. L. 119-11 (May 9, 2025); historical only.** **CFPB BNPL market-monitoring report** (verify current state for any successor data publications).
- **CFPB final rule on larger participants of digital consumer payment applications** (December 2024 — verify Federal Register citation and current state) — direct CFPB supervision over designated larger participants.

#### Theme list to read into the matrix

**Account closure and account hold without notice or recourse.** The most-frequent fintech UDAAP theme. Control families: notice timing and content; customer-recourse channel; complaint-routing-to-sponsor-bank loop; account-closure root-cause review; hold-release SLA; redress posture for wrongful holds. Read into the consumer segment row and into the cross-cutting UDAAP row.

**Reg E §1005.11 dispute-timing failures presented as UDAAP.** The CFPB has been pursuing both lanes simultaneously. Where the 10 / 45 / 90-day windows are missed, expect both Reg E findings and UDAAP findings. Read into every consumer-facing rail row carrying disputes (debit card, ACH consumer-account, FedNow / RTP consumer-account, P2P).

**Fee disclosure failures.** Junk-fee themes; surprise-fee patterns; NSF / overdraft framing on fintech accounts. CFPB has issued Circulars and supervisory guidance on overdraft and junk fees (verify current circular numbers and dates). Fee-disclosure-vs-actual reconciliation is the operative test.

**FDIC-insurance representation.** The Synapse-era enforcement and the **FDIC Part 328 final rule (December 2023) with effective-date extensions through 2024-2025** — verify current effective date for the engagement — require any "FDIC-insured" framing on fintech surfaces to be re-papered to the pass-through caveats. Marketing-claim review against 12 CFR Part 328 Subpart B.

**BNPL UDAAP themes.** Fee disclosure, dispute-rights presentation, comparative-shopping framing, late-fee policy. Anchored to the CFPB BNPL market-monitoring report (September 2022) and any subsequent CFPB BNPL actions. The CFPB BNPL / Pay-in-Four Interpretive Rule (which framed BNPL as a credit-card-like product subject to Reg Z dispute-resolution provisions) was **nullified by Pub. L. 119-11 (May 9, 2025); historical only** — Reg Z applicability now turns on the product structure under the regulatory text rather than through the nullified interpretive rule.

**Dark-pattern risk in onboarding and product-selection flows.** Pre-checked consents; choice-architecture nudges that bury opt-outs; comparative-shopping suppression. CFPB Circular on dark patterns [verify which circular and date]. FTC dark-pattern guidance.

**Larger-participant rule applicability.** Where the CFPB final rule on larger participants of digital consumer payment applications designates the firm (verify on the analysis date), direct CFPB supervision applies; the UDAAP-review posture changes from sponsor-bank-mediated to direct.

**Sponsor-bank UDAAP cross-pollination.** A fintech UDAAP finding can flow upstream to the sponsor bank's CFPB or prudential-supervisory file under the bank-fintech-arrangements lens. Read into the sponsor-bank-concentration sub-table.

**Complaint-data triangulation.** CFPB Consumer Complaint Database vs internal complaint data vs sponsor-bank-routed complaint data. Material discrepancies are an examiner signal.

#### What the overlay puts into the matrix

In the **risk universe by customer segment** row for each consumer-facing segment: top failure modes pull from the theme list above. Key controls cite the firm's named control families. KRIs include dispute-timing-breach rate, hold-release-SLA breach rate, complaint-volume vs peer benchmark.

In the **cross-cutting risks** layer: UDAAP row with risk owner (head of compliance / CCO), top three KRIs (pulled up from segment rows), deep-dive skill reference (`udaap-risk-review` with the payments-fintech overlay).

In the **risk-appetite posture**: red conditions for any segment cell where the dispute-timing-breach rate, the hold-release-SLA breach rate, or the complaint-volume signal sit beyond firm appetite. Where firm appetite is not on file, mark `[evidence needed]`.

## cyber

### Cross-cutting overlay — cyber

Default-on for substantively every payments program. The rails depend on processors, ledger providers, fraud-decision vendors, sanctions-screening vendors, and KYC vendors with cyber-incident exposure. The sponsor-bank construct adds a notification chain. The overlay carries the cyber-row content for the matrix and the sponsor-bank-cyber-notification-chain detail for the operational-resilience cross-cutting row.

The overlay does not substitute for the deep-dive in `cyber-disclosure-readiness` (with the payments-fintech overlay where the firm or its sponsor bank is a public registrant) or for the incident workflow in `payment-operations-incident-review`. The assessment raises the flag and points to the deep-dive.

#### Anchor frame

- **NYDFS 23 NYCRR Part 500** including §500.17(a) cybersecurity-event notification clock (72 hours). Applies to firms that are NYDFS Covered Entities; applies to many fintechs by virtue of NY footprint.
- **GLBA Safeguards Rule, 16 CFR Part 314** as amended (FTC, December 2021 amendments effective 2023). §314.4(f) service-provider obligations; §314.4(h) incident-response.
- **GLBA Privacy Rule / Reg P, 12 CFR Part 1016**.
- **FFIEC IT Examination Handbook — Information Security booklet** (verify current edition and section).
- **FFIEC Authentication and Access to Financial Institution Services and Systems Guidance** (August 11, 2021).
- **SEC cybersecurity disclosure** — Item 1.05 of Form 8-K and Reg S-K Item 106 (effective 2023 — verify exact compliance dates by registrant size). Applies where the firm or its sponsor bank is a public registrant.
- **State breach-notification statutes** — state-by-state; verify per state in the geographic footprint.
- **FFIEC Cybersecurity Assessment Tool (CAT)** [verify current state — CAT was sunset in August 2024 per FFIEC announcement; verify the current FFIEC cyber assessment guidance and its applicability date].

#### Sponsor-bank cyber-notification chain

The sponsor bank's prudential cyber-notification clock under the **Computer-Security Incident Notification Rule** (12 CFR Part 53 for OCC, 12 CFR Part 225 Subpart N for FRB, 12 CFR Part 304 Subpart E for FDIC, effective May 1, 2022) requires the sponsor bank to notify its primary federal regulator within 36 hours of determining that a notification incident has occurred. The program operator's incident-detection and notification posture must be timed against this 36-hour window — the sponsor bank cannot meet its 36-hour clock if the program operator does not deliver the determination in time.

The program-agreement clause set typically pushes a tighter contractual notification clock onto the program operator (often 24 hours or less). The assessment confirms the contractual clock and the operational capability to meet it.

#### What the overlay puts into the matrix

In the **cross-cutting risks** layer: cyber row with risk owner (CISO or head of information security), top three KRIs (incident-detection MTTD, incident-notification SLA breach rate, vendor-cyber-incident exposure rate), and the deep-dive skill reference (`cyber-disclosure-readiness` for the disclosure leg; `payment-operations-incident-review` for the incident workflow).

In the **operational-resilience** sub-view of the cross-cutting risks: vendor-stack cyber posture (processor SOC 2 Type II current, fraud-decision vendor SOC 2 current, sanctions-screening vendor SOC 2 current, KYC vendor SOC 2 current); sponsor-bank cyber-notification SLA against the contractual clock; tabletop-exercise cadence for the sponsor-bank-coordinated incident-response.

In the **risk-appetite posture**: red conditions for any cell where the vendor-stack cyber posture has a critical SOC 2 exception open beyond firm appetite, where the incident-notification SLA breach rate exceeds appetite, or where the sponsor-bank-coordinated tabletop is overdue. Where firm appetite is not on file, mark `[evidence needed]`.

#### Common pitfalls

- Reading cyber as a vendor-stack tickbox rather than as an operational-resilience and sponsor-bank-notification posture.
- Missing the 36-hour sponsor-bank prudential clock and the implied contractual-clock-on-the-program-operator.
- Treating SOC 2 Type II as a substitute for the firm's own evidence on customer-managed key posture, vulnerability-management cadence, or incident-response cooperation terms.
- Omitting the public-registrant disclosure leg where the sponsor bank is a public registrant subject to SEC Item 1.05.

## privacy

### Cross-cutting overlay — privacy

Default-on where customer-data flows for fraud and AML monitoring extend beyond baseline (most programs once monitoring vendors are in the stack). The overlay carries the privacy-row content for the cross-cutting risks layer.

The overlay does not substitute for a state-by-state privacy-law inventory, which is its own work product. The assessment names the operative regimes and the controls and points to deeper review where the firm's footprint demands it.

#### Anchor frame

- **GLBA Safeguards Rule, 16 CFR Part 314** as amended (FTC, December 2021 amendments effective 2023). §314.4(a)-(h) program elements; §314.4(f) service-provider obligations; §314.4(h) incident-response.
- **GLBA Privacy Rule / Reg P, 12 CFR Part 1016**. Consumer-information privacy notice; opt-out mechanics; sharing limits.
- **CFPB Personal Financial Data Rights Final Rule under §1033** (October 22, 2024 — verify Federal Register citation, exact citation, implementation tier dates, and current docket status). Where the program operator is a data provider or data recipient, §1033 obligations include secondary-use limits, retention-and-deletion duties, and consent-revocation paths.
- **CCPA / CPRA — California Consumer Privacy Act as amended, Cal. Civ. Code §1798.100 et seq.** Consumer rights to know, delete, correct, opt-out of sale and sharing; sensitive-personal-information limits.
- **State privacy laws** — verify state-by-state per the geographic footprint. Active comprehensive privacy laws include (incomplete; verify currency on the analysis date) Virginia (VCDPA), Colorado (CPA), Connecticut (CTDPA), Utah (UCPA), Texas (TDPSA), Oregon (OCPA), Montana (MTCDPA), and others.
- **HIPAA Privacy Rule (45 CFR Parts 160, 164 Subpart E) and Security Rule (45 CFR Parts 160, 164 Subpart C)** — applies only where the program touches PHI (uncommon in payments but possible in healthcare-payment niches).
- **NYDFS 23 NYCRR Part 500** — privacy and security overlap.

#### What the overlay puts into the matrix

In the **cross-cutting risks** layer: privacy row with risk owner (head of privacy / CPO or general counsel where no dedicated CPO), top three KRIs (data-subject-access-request SLA breach rate, vendor-data-processing-agreement coverage rate, secondary-use exception rate), and the deep-dive skill reference where one exists in the firm's plugin stack.

In the **risk universe by customer segment** rows where regulated data crosses to processors and monitoring vendors: privacy-control posture as part of the key-controls column.

In the **risk universe by geography** rows: state-privacy-law applicability per US state in scope (the row already carries MTL / NMLS posture; privacy posture sits beside it).

#### §1033 status note

Repeat. Where the program operator is a data provider under §1033 (most consumer-account programs), the assessment names the data-provider obligations and the implementation tier date for the firm. Where the program operator is a data recipient (typically aggregator-fed analytics), the cross-link is to `open-banking-data-controls`. Verify the current docket status on each engagement and date-stamp the citation; the rule was finalised October 2024 but the docket has been active and tier dates may have shifted.

#### Common pitfalls

- Treating GLBA as the only privacy frame and missing the state regime in CA, VA, CO, and others where the program operator falls under the threshold.
- Defaulting the §1033 status to "we will be ready" without naming the firm's tier and implementation-date posture.
- Reading vendor data-processing agreements (DPAs) as evidence of operational compliance rather than as contractual baseline; DPA coverage and DPA-vs-actual reconciliation are separate questions.
- Missing secondary-use exception scope in monitoring-vendor contracts (model-improvement, benchmarking, anonymous-aggregate use).
