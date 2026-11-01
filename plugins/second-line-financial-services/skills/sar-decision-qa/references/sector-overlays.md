# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — sar-decision-qa

When the scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the bank-specific SAR-decision frame the generic capability skill does not own.

#### Operative SAR rule

- **31 CFR §1020.320** [verify section] — the bank SAR rule. Operative thresholds: $5,000 where a suspect is identified; $25,000 where no suspect is identified. Operative filing window: 30 days from initial detection of facts that may constitute a basis for filing; 60 days where no suspect can be identified at the 30-day mark. Continuing-activity reviews are an examination expectation rebuilt on top of the rule and the FFIEC manual, conventionally on a 90-day cadence. The QA reads the disposition file against the rule and the manual, not against any single internal SLA.

#### Examiner frame

- **FFIEC BSA/AML Examination Manual — Suspicious Activity Reporting section** is the examiner-facing detail. The QA reads the alert-management, case-investigation, decision-to-file, narrative-quality, structured-field-completeness, continuing-activity, confidentiality, and program-level-control expectations from this section.
- **OCC / FRB / FDIC / NCUA Joint Statement on Risk-Focused BSA/AML Supervision (July 22, 2021)** sets the risk-focused supervisory tone. QA depth should track risk: high-risk typology alerts (structuring, trade-based, layering, sanctions-adjacent, fraud-typology) get deeper QA than commodity false positives that closed routinely.
- **FinCEN / Federal Banking Agencies Joint Statement on Innovation in BSA/AML Compliance (December 3, 2018)** supports innovation. The QA does not penalise governed innovation in the detection or decision pipeline as long as the decision file shows the work.

#### Bank-specific typology population the QA encounters most

- Structuring against the $10,000 CTR threshold (single-customer and related-party patterns).
- Check kiting and on-us / cross-bank deposit float patterns.
- ACH origination fraud, including business-email-compromise-funded ACH and account-takeover ACH.
- Commercial wire fraud, including BEC pattern.
- Elder financial exploitation, anchored to the elder-financial-exploitation FinCEN advisory.
- BIN-attack / card-fraud patterns funnelling to deposit accounts.
- Trade-based money laundering on commercial customers.
- Insider-conduct typologies (employee, branch-manager schemes) — handled here, not under a separate conduct overlay.

#### Continuing-activity at a bank

The 90-day continuing-activity review is an examination expectation rebuilt on the FFIEC manual. Reviews concluding "no continuing activity" are still papered. The QA's `continuing_activity.last_continuing_review_date` and `next_review_due` fields apply regardless of outcome. A bank that papers reviews only when a follow-on SAR is filed has an evidence gap.

#### BSA-officer accountability

The bank's BSA officer is the named filer-of-record. The QA recommends; the BSA officer (with the SAR review committee where the firm uses one) decides on filing, amendment, supplement, or close. The QA does not direct the filing decision.

#### Cross-link inside the plugin

- **`cdd-risk-review`** carries the customer-segmentation and CDD-refresh work. Where the alert decision file flags a segment-mismatch (e.g., consumer-segment CDD on a small-business customer), the QA cross-references but does not handle the CDD refresh.
- **`edd-escalation-pack`** carries EDD posture for high-risk customers. Where the alert sits on an EDD-trajectory customer, the QA cross-references.
- **`aml-model-monitoring`** carries the alert-source model governance. The alert-decision QA notes whether the source scenario or rule has model-risk coverage on file; it does not re-do model-monitoring work.
- **`sanctions-screening-qa`** carries sanctions-screening alert-decision QA. Where the alert is sanctions-adjacent, the QA cross-references rather than absorbing both lenses.
- **`negative-news-triage`** carries adverse-media triage. A standalone negative-news triage that did not produce a SAR alert belongs there, not here.

#### Output-template additions for banking

- 31 CFR §1020.320 filing-window status as a named field (`within-30-day-window`, `within-60-day-window-no-suspect`, `late`).
- 90-day continuing-activity cadence status as a named field, regardless of disposition.
- BSA-officer-and-SAR-review-committee handoff status.
- Bank-specific typology label drawn from the bank typology list above.

#### Common pitfalls in banking SAR-decision QA

- Treating a community-bank SAR-decision file with the same depth as a large-bank file regardless of typology and customer risk; the risk-focused supervisory frame asks for proportionality.
- Reading the FFIEC manual sections as binding rules rather than as examiner expectations layered on the SAR rule.
- Letting the QA drift into a comment on whether the SAR should have been filed; the QA reviews the decision file against criteria and does not direct the filing decision.
- Skipping the cross-link to CDD or EDD when the alert evidence reveals a segment-mismatch or an EDD-trajectory customer.
- Confusing model-risk coverage of the alert-source scenario with decision-quality of the closed alert; the former belongs in `aml-model-monitoring`.

## capital-markets

### Capital-markets sector overlay — sar-decision-qa

When the scope flags capital markets (broker-dealers, investment advisers running affiliated BD activity, mutual funds, futures commission merchants), load this overlay alongside `references/source-anchors.md`.

#### Operative SAR rules in scope

- **31 CFR §1023.320** — Reports by brokers or dealers in securities of suspicious transactions [verify section]. The BD SAR rule. Threshold $5,000; 30-day filing window; 60-day window where no suspect identified. **Per October 9, 2025 SAR FAQ posture: 90-day continuing-SAR cadence is firm-policy convention, not a rule requirement.**
- **31 CFR §1024.320** — Reports by mutual funds of suspicious transactions [verify section]. Open-end management investment companies registered under the Investment Company Act. The fund or the fund's transfer agent / principal underwriter, depending on the program design, files.
- **31 CFR §1026.320** — Reports by futures commission merchants and introducing brokers of suspicious transactions [verify section]. The FCM SAR rule.

Investment advisers do not currently have a stand-alone SAR rule; advisers may be reached through their affiliated BD's SAR program or through SEC-supervisory expectations. Track the FinCEN rulemaking on covered investment advisers as it evolves [verify current state of FinCEN IA AML and SAR rulemaking on the date of analysis].

#### SEC- and FINRA-supervised SAR program elements

- **FFIEC manual is not the operative examiner anchor for BDs and funds** — SEC examination staff and FINRA examiners are. The QA reads the BD's written supervisory procedures (WSPs) under **FINRA Rule 3110 (supervision)** and the fund's compliance program under **Investment Company Act Rule 38a-1**. The SAR program sits inside those frames.
- **FINRA Rule 3310** — AML compliance program. Independent testing, designated AML officer, ongoing training, CIP. The SAR program reports up through the firm's AML officer.
- **SEC Division of Examinations risk alerts on AML programs at advisers and BDs** [verify specific risk alerts current on the date of analysis] — read for current examination focus.

#### Capital-markets-specific typology population the QA encounters most

- Microcap pump-and-dump — coordinated buying activity in a low-float security followed by mass distribution.
- Match-trading and prearranged-trading patterns — wash-trade signatures, often crossing related accounts at the BD or across affiliated BDs.
- Insider trading-adjacent patterns — pre-news anomalous activity in a security subject to a known event; the SAR-decision file routes through legal and compliance and the BD's market-surveillance team.
- Spoofing and layering on equities or futures — order-book manipulation patterns.
- Late-trading and market-timing in mutual funds — mostly historical typology but still on the FFIEC and SEC radar.
- Securities-account funding from third-party sources unrelated to the customer — money-laundering-through-securities pattern.
- Sanctions-adjacent activity in custody or settlement chains.

#### Cross-link inside the plugin

- **`cdd-risk-review`** carries the BD's or fund's customer-segmentation work. SAR-decision findings on segment-mismatch (e.g., a retail brokerage account showing institutional-trading patterns) feed back.
- **`aml-model-monitoring`** carries the BD's transaction-monitoring and surveillance-system governance.
- **`sanctions-screening-qa`** carries sanctions-screening alert-decision QA.

#### Cross-link to other plugins

- **`market-conduct-and-customer-outcomes/best-execution-surveillance`** [verify skill exists in current build] — where the SAR alert sits adjacent to a best-execution or market-manipulation pattern, cross-reference rather than absorbing both lenses.
- **`vendor-diligence`** for transfer-agent, fund-accountant, principal-underwriter, custodian SAR-program-handoff diligence.

#### Output-template additions for capital markets

- Operative SAR rule as a named field (`bd-1023-320`, `mutual-fund-1024-320`, `fcm-1026-320`).
- Surveillance-system source attribution (the BD's order-book surveillance, the fund's transfer-agent monitoring) as a named field.
- Market-manipulation-typology label drawn from the typology list above where applicable.
- Cross-reference to market-surveillance and best-execution work where the alert sits adjacent.

#### Common pitfalls in capital-markets SAR-decision QA

- Importing the FFIEC bank-flavoured frame as if it were operative for a BD or fund; the FFIEC manual SAR section informs but does not bind, and SEC / FINRA examiners are the primary audience.
- Treating an investment-adviser-only firm as if a BD SAR rule applied directly; the rule applies to the affiliated BD, not the IA, until FinCEN's IA SAR rulemaking is operative.
- Missing the route into market-surveillance work for spoofing, layering, microcap, and insider-trading-adjacent patterns; the SAR-decision file should reflect the surveillance-team handoff.
- Skipping the late-trading / market-timing typology read on mutual-fund alerts as "historical" when the customer activity matches the pattern.
- Confusing CIP findings (which sit in `cdd-risk-review`) with SAR-decision findings.

## insurance

### Insurance sector overlay — sar-decision-qa

When the scope flags insurance, load this overlay alongside `references/source-anchors.md`. The insurance overlay carries what the bank-flavoured capability skill does not.

#### Operative SAR rule

- **31 CFR §1025.320** — Reports by insurance companies of suspicious transactions [verify section]. Threshold $5,000. Filing window 30 days from initial detection (60 days where no suspect identified). The rule applies to **covered products** only:
  - Permanent life insurance with cash value, other than group life insurance.
  - Annuity contracts other than group annuities.
  - Other insurance products with features of cash value or investment.

  Property and casualty (P&C), term life without cash value, group products without individual ownership, health insurance, and reinsurance are generally outside the SAR rule's covered-products scope. The QA must scope the alert to whether the underlying product is a covered product before applying the rule.

#### Insurance-specific typology population the QA encounters most

- Early-surrender of permanent life or annuity contracts shortly after funding — money-laundering layering pattern using insurance as a value-store.
- Unusual funding sources for premium payment (third-party cheques, structured cash, foreign-jurisdiction wires) inconsistent with customer profile.
- Free-look-period cancellations after large premium funding — washing the funds through the insurer's cash management.
- Policy-loan abuse — large policy loans against newly-funded contracts as a value-extraction route.
- Beneficiary changes coincident with sanctions, PEP, or adverse-media events on the new beneficiary.
- Producer-driven schemes — agent-perpetrated fraud where the producer steers customers into transactions inconsistent with the customer's profile (insider-conduct typology).

#### Carrier-specific SAR program elements

- **31 USC §5318(h)** — AML program requirement for insurance companies (the operative AML compliance program rule). The SAR program is one element. The QA reads the SAR-decision file against the carrier's written AML compliance program and the FinCEN insurance-AML guidance and FAQs [verify current FinCEN insurance-AML guidance on the date of analysis].
- **NAIC Insurance Data Security Model Law (Model #668)** [verify model number] — adjacent cybersecurity frame. Where the alert involves account-takeover, claims fraud, or producer-perpetrated fraud, the cyber overlay engages and the carrier's incident-response posture under Model #668 may sit adjacent to the SAR-decision narrative.

#### Producer accountability and the insider-conduct lens

The insurance distribution model means the **producer** (agent, broker) is often the practical interface to the customer. SAR alerts on producer-perpetrated patterns require:

- Producer-licensing-and-appointment status check (NAIC Producer Licensing Model Act [verify model number]; per-state).
- Producer-level continuing-activity tracking, not only customer-level.
- Cross-link to the carrier's market-conduct examination posture and the producer-discipline track (which sits outside this skill).

#### Cross-link inside the plugin

- **`cdd-risk-review`** carries the carrier's covered-product CDD work and the producer-due-diligence frame.
- **`edd-escalation-pack`** carries EDD posture for high-risk customers (PEPs, foreign-jurisdiction premium funding, large face-amount contracts).
- **`aml-model-monitoring`** carries the carrier's transaction-monitoring (where deployed; many carriers monitor through case-management with rule-based detection rather than scenario-driven systems).

#### Cross-link to other plugins

- **`market-conduct-and-customer-outcomes`** plugin [verify skill availability in current build] — producer-perpetrated patterns and unfair-claims-handling overlap; SAR-decision QA cross-references rather than absorbing.
- **`vendor-diligence`** for TPA / claims-administrator / underwriting-bureau diligence where the alert source is a TPA system.

#### Output-template additions for insurance

- Covered-product scoping as a named field (`covered-product-confirmed`, `non-covered-product-out-of-scope`, `mixed-need-product-detail`).
- Producer-licensing-and-appointment status as a named field where the typology is producer-driven.
- ORSA-fit flag where the SAR-decision pattern points to a material outsourced or aggregated risk that belongs in the carrier's ORSA Summary Report.
- HIPAA-overlap note where claims-fraud alerts touch PHI.

#### Common pitfalls in insurance SAR-decision QA

- Applying the SAR rule to a non-covered-product alert (e.g., P&C claim, term life without cash value); the rule simply does not reach the activity.
- Treating producer-perpetrated patterns as customer-fraud and missing the producer-discipline and licensing-check track.
- Importing the FFIEC bank-flavoured continuing-activity cadence assumption without checking the carrier's own program; insurance SAR-decision files often have less-developed continuing-activity infrastructure than bank programs.
- Skipping the covered-product scoping at the start of the QA and discovering halfway through that the alert was out of scope.
- Confusing carrier insolvency / financial-condition triggers with SAR-decision triggers; those route through different supervisory channels.

## payments-fintech

### Payments-fintech sector overlay — sar-decision-qa

When the scope flags payments or fintech (sponsor-bank programs, BaaS platforms, money transmitters, MSBs, card-program operators, virtual-currency on-ramps), load this overlay alongside `references/source-anchors.md`.

#### SAR-filing-responsibility allocation

The threshold question for a payments-fintech SAR-decision QA is which entity owns the SAR filing. The allocation is documented in the sponsor-bank program agreement and is not optional QA scope.

- **Sponsor-bank arrangement (BaaS, program operator, fintech with bank in the chain)**: the sponsor bank typically holds ultimate SAR-filing responsibility for activity in the bank's accounts under **31 CFR §1020.320**. The fintech's BSA program detects, investigates, and drafts; the sponsor bank's BSA officer reviews and files. The QA reviews the fintech's draft and decision file and confirms the handoff package to the sponsor bank is complete. The QA does not direct the sponsor bank's filing decision.
- **Standalone MSB**: the MSB itself files under **31 CFR §1022.320** [verify section]. Operative threshold $2,000 (and $5,000 for issuers / sellers / redeemers of money orders or traveler's checks identified through a clearance review). Filing window 30 days. The QA reviews the MSB BSA officer's decision file directly.
- **Dual-posture (MSB with sponsor-bank deposit account)**: both rules can apply to different segments of activity. The QA must scope which rule covers which alerts.

#### Operative SAR rules in scope

- **31 CFR §1022.320** — MSB SAR rule (MSB own filing) [verify section].
- **31 CFR §1020.320** — bank SAR rule (sponsor-bank filing on behalf of activity in bank's accounts) [verify section].
- **31 CFR §1022.380** — MSB registration with FinCEN. Initial registration within 180 days of becoming an MSB; renewal every two years. Adjacent program-element check; not the BOI / CTA reporting rule at §1010.380, which is a separate obligation with its own legal status.

#### Fintech-specific typology population the QA encounters most

- Money muling — consumer-account funding from multiple low-value sources with rapid onward disbursement (P2P, virtual currency, prepaid card cash-out).
- Synthetic-identity onboarding rings — alert-decision files often connect to the CIP / identity-verification vendor's outputs, anchored to fraud-detection and CIP failures.
- Account-takeover (ATO) — credential-stuffing attacks; the alert may sit in fraud-system output and only later be re-routed for SAR consideration.
- Business-email-compromise (BEC) — commercial fintech / treasury-card customers; downstream wire or ACH or card disbursement.
- Convertible-virtual-currency on-ramp activity — anchored to FinCEN's convertible-virtual-currency advisories and OFAC's sanctions-compliance guidance for the virtual currency industry [verify dates]; the cyber overlay engages.
- Romance-and-investment-scam victim funding (consumer customer is the victim, not the suspect; SAR posture under the elder-financial-exploitation advisory and FinCEN guidance on scams).

#### Sponsor-bank handoff package

When the QA covers a fintech that drafts and hands off to a sponsor bank, the handoff package the QA must check for completeness:

- The drafted SAR (form fields and narrative).
- The investigation file (dated, attributed steps; evidence pointers).
- Cross-references to other functions (sanctions-officer routing where the typology is sanctions-adjacent; fraud-decision-vendor output where the alert is fraud-typology; CIP / identity-verification vendor output where synthetic-identity is in play).
- The fintech's tipping-off assessment specific to this decision.
- The fintech's recommendation (file, decline, supplement) — consultative only; the sponsor bank decides.

A handoff package missing the sanctions-officer cross-reference for a sanctions-adjacent typology, or missing the case-specific tipping-off assessment in a fraud-recovery / dispute case, is a `process_change_recommendation` finding.

#### Cross-link inside the plugin

- **`cdd-risk-review`** carries the fintech's customer-segmentation and onboarding-CDD work. Synthetic-identity findings from the SAR-decision file feed back to CDD-program tuning.
- **`sanctions-screening-qa`** carries sanctions-screening alert-decision QA. Sanctions-adjacent SAR alerts (especially convertible-virtual-currency typologies) cross-reference here.
- **`aml-model-monitoring`** carries the fintech's transaction-monitoring scenario governance and the fraud-decision vendor model-risk view.

#### Cross-link to other plugins

- **`vendor-diligence`** carries the sponsor-bank, processor, BIN-sponsor, KYC-vendor, fraud-decision-vendor, and sanctions-screening-vendor diligence. The SAR-decision QA cross-references vendor-diligence findings where a sub-processor's posture is material to the SAR rationale.
- **`llm-vendor-evidence-review`** carries the AI-vendor evidence-pack review for any AI tooling in the alert-decision pipeline (AI-driven KYC, AI-driven dispute decisioning, AI-augmented investigator workflows). The SAR-decision QA does not duplicate model-risk analysis.

#### Output-template additions for payments-fintech

- SAR-filing-responsibility allocation as a named field (`sponsor-bank-files`, `msb-files`, `dual-posture`).
- Sponsor-bank handoff package status (`complete`, `partial`, `missing-sanctions-routing`, `missing-case-specific-tipping-off-assessment`, `other-gap`).
- Fintech-specific typology label drawn from the typology list above.
- Cross-link to vendor-diligence findings where a sub-processor posture is material.

#### Common pitfalls in payments-fintech SAR-decision QA

- Reviewing the fintech's decision file as if the fintech were the filer; missing the sponsor-bank handoff package check.
- Applying the bank $5,000 threshold to MSB activity (the MSB threshold is $2,000).
- Treating the program-level tipping-off tickbox as satisfying the case-specific assessment in fraud-recovery, dispute, and customer-service-overlap cases.
- Skipping the sanctions-officer cross-reference on convertible-virtual-currency on-ramp typologies and other sanctions-adjacent fintech alerts.
- Conflating the alert-source-vendor (KYC, fraud-decision, sanctions-screening) governance with the SAR-decision quality; vendor-diligence and model-monitoring carry the source view.
- Treating "we are a fintech, not a bank" as a reason to apply lower decision-file rigour; the SAR rule the fintech operates under (own MSB or sponsor-bank-mediated) sets the rigour, not the firm's preferred narrative about itself.
