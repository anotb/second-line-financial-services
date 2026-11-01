# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## community-bank-baas-mid-sized-fintech-partner

### Example: community bank running a BaaS deposit program with a mid-sized fintech partner

Public-source-derived. No named bank or fintech. The shape mirrors a common pattern at a $2-5B community bank that runs one BaaS deposit-program relationship with a mid-sized fintech partner offering a deposit product (high-yield savings) and an ancillary unsecured consumer-loan product through the bank, with a middleware platform sitting between the fintech and the bank's core. The engagement is the annual partnership refresh review.

#### Input

- **Bank**: state non-member commercial bank, ~$3.4B in total assets, FDIC-supervised with state DFI as joint supervisor. Two BaaS sponsor-program relationships in production; the relationship under review is the larger of the two, contributing ~28% of the bank's deposit base and ~12% of fee income. Not a covered bank under 12 CFR Part 30 Appendix D; the OCC's framework does not apply directly. The BHC is privately held, no SEC reporting registrant status.
- **Fintech partner**: mid-sized US-incorporated fintech, founded 2018, ~$80M in last reported revenue, Series C funded. Customer-facing brand is fintech-front; the bank's name appears in disclosures, in the FDIC-insurance representation, and on customer statements. Two products through the bank: a high-yield savings deposit product (the deposit program, FBO-account structured) and an unsecured consumer-loan product (originated by the bank, serviced by the fintech).
- **Middleware platform**: a third-party BaaS middleware vendor sits between the fintech and the bank's core; the platform owns the end-user ledger, the daily reconciliation file feed to the bank, and the FBO-account-level settlement instructions to the bank's deposit-operations team.
- **Engagement type**: annual partnership refresh review under the bank's TPRM policy. Refresh cadence is annual for critical-activity relationships; the bank's prior-cycle classification was critical-activity and that classification is being re-tested as part of the refresh.
- **Persona**: head of TPRM at the sponsor bank, supported by the chief compliance officer, BSA officer, head of deposit operations, head of consumer compliance, general counsel, and CISO. The pack lands at the bank's third-party risk committee and at the bank's board independent risk committee at its standing third-party-risk topical session.
- **Source posture**: `public-plus-firm-policy-plus-evidence`. The bank has the contract draft, the most recent SOC 2 Type II covering both the fintech and the middleware platform, the BSA / AML independent-test report from the fintech's most recent cycle, the daily FBO reconciliation files for the trailing 13 months, the customer-complaint log, the marketing-review approval log, and the most recent simulated wind-down tabletop minutes (10 months prior to the refresh date).
- **Cross-cutting overlays loaded**: cyber (BaaS deposit program, fintech holds NPI, middleware platform sits in the authentication and ledgering path), conduct (deposit and consumer-loan products are customer-facing), privacy (consumer NPI flows to the fintech and to the middleware platform). Climate overlay does not load.
- **Engagement scope supplied**: institution profile, persona, source posture, cross-cutting overlay set, and access population (the bank's third-party risk committee and board independent risk committee plus the partnership-management team... wider than the bank's CSI access population, so verbatim CSI cannot appear in the body).

#### Output sketch

The skill produces the bank-side partnership pack against `templates/default-output.md`. Headlines:

- **Cover and partnership scope** — annual refresh, source posture public-plus-firm-policy-plus-evidence, access population wider than the bank's CSI population (so verbatim CSI references are summarised in the body, with restricted citations in the source trace), confidence label medium-high (the FBO reconciliation evidence is strong; the Reg O screen result and the Part 328 Subpart B evidence have gaps).

- **Section 1 — Service description and risk classification.** High-yield savings as a sponsor-bank deposit product; consumer-loan product originated by the bank and serviced by the fintech. Brand presentation fintech-front; customer of record is the bank for the deposit product (FBO-account structured with pass-through coverage to the end user) and the bank for the consumer-loan product. Money flow: the middleware platform owns the end-user ledger and pushes daily reconciliation files; the bank holds the FBO account and processes settlement; reconciliation cadence is daily T+1 with a $5k variance threshold against a ~$960M deposit book. Criticality classification: **critical-activity**, driven by the 28% deposit-base share and the 12% fee-income share; the prior-cycle classification holds. BSA / AML risk classification: heightened across CIP (31 CFR §1020.220), CDD, beneficial-ownership (31 CFR §1010.230), suspicious-activity monitoring, and OFAC. Heightened Standards applicability: **not applicable** (the bank is FDIC-supervised and not at the $50B+ threshold; Part 30 Appendix D is OCC-only; the FDIC large-bank examination program is the analogue and is not yet binding at this asset band).

- **Section 2 — Risk-based diligence summary.** Status across the fourteen interagency-guidance categories. Headlines: SOC 2 Type II current and clean (covers both the fintech and the middleware platform); BSA / AML independent test current with two open low-severity findings tracked; financial condition `sound` based on most recent audited financials and Series C cash runway; resilience BCDR test report covers the primary region but the failover-region tabletop is partial; insurance posture confirms cyber, E&O, and fidelity coverage with the bank as additional insured.

  - **Reg O insider screen.** **Gap.** The screen identified one fintech executive (a senior leader) whose spouse is a director of an unaffiliated community bank in the bank's footprint; the spouse's directorship makes the fintech executive a related interest of a director under §215.2 in that bank's chain, but the relevant Reg O screen for **this** sponsor-bank's purposes is whether the fintech executive is an insider of **this** sponsor bank. The screen surfaced a different concern: one fintech board observer is a related interest of a director of the sponsor bank under §215.2(n) [verify section] (a passive minority equity interest in an investment vehicle that the director controls). The bank had not documented an exception or analysed whether any extension of credit, credit-equivalent transaction, or covered transaction is implicated. Section 5 records this as a Reg O finding; recommended owner action is to document the exception or restructure the relationship before the next renewal cycle.
  - **Reg W affiliate test.** Not applicable. The fintech is not an affiliate of the bank under §223.2 (no 25% control, no management interlock, no common control through a holding-company); the fintech and the bank are unrelated third parties. The Reg W row in section 5 reads "applicable: no" with the screen result documented; §223.41 / §223.42 exemptions are not cited.
  - **Bank Service Company Act notification.** §1867(c) notification was filed at original program go-live (3.5 years prior); the addition of the consumer-loan product as a new covered service 14 months ago did not trigger a fresh notification because the bank's filing is at the relationship level and the consumer-loan product fits within the original scope. **[Verify position]**: the bank's general counsel confirms the original filing covered "deposit and lending services through the fintech relationship"; if the original scope reads narrower, a fresh §1867(c) notification is required and the recommended owner action is to file within 30 days.

- **Section 3 — Contract gaps.** §1867(c) examination flow-down: present and adequate, covering the fintech, the middleware platform as a fourth-party, and any subcontractor of either. Information-security incident notification: the contract requires the fintech to notify the bank within 24 hours of any "material" incident; the bank's downstream 36-hour computer-security-incident notification clock under 12 CFR Part 304 (FDIC) means the 24-hour internal clock is workable but the materiality definition is left to the fintech, which is a control gap. Subcontractor governance: the contract requires the fintech to give the bank 30 days' notice of subcontractor changes but no consent gate; **gap, severity medium**, recommended action is to add a consent-with-rapid-objection-window provision before the next renewal. Data-return clauses on termination: format named (CSV plus a structured ledger extract), timeline 30 days, attestation required; verification rights present. Customer-data ownership and use restrictions: present and adequate. Limits on fintech use of bank brand and disclosures: present but the operative review-and-attestation cadence on customer-facing copy is not anchored in the contract; **gap, severity medium**.

- **Section 4 — Customer-facing controls.**

  - **Reg E division of responsibility.** Bank is the financial institution under §1005.2(i) for the high-yield savings deposit product. The bank carries the §1005.11 timing obligation (10 business days for investigation, 45 calendar days with provisional credit, 90 calendar days for new accounts / POS / foreign-initiated transfers, 3 business days post-investigation to notify the consumer of results). The fintech is the front-line intake channel; the bank-fallback SOP exists and was tested in the prior quarter. Status: **adequate**. The pack tests the bank's fallback when the fintech misses an intake event; the most-recent test confirmed the fallback ran within tolerance.
  - **Reg DD division of responsibility.** Bank is the depository institution; the bank carries §1030.4 disclosure responsibility and §1030.8 advertising-rule risk on fintech-shipped marketing copy. The bank's marketing-review approval gate (head of consumer compliance and head of deposit operations as named approvers; 5-business-day SLA) is documented, but the bank's attestation cadence on fintech-shipped copy in production has slipped; the most recent attestation is 8 months stale against a 6-month cadence target. **Gap, severity medium.**
  - **UDAAP screen.** Customer-facing copy on the deposit product reviewed and adequate; consumer-loan product copy adequate; fee structure on the deposit product disclosed and consistent across surfaces; adverse-action and dispute customer journey reviewed.
  - **FDIC misrepresentation rule (12 CFR Part 328 Subpart B).** **Gap.** The "FDIC-insured" representation is consistent on the partner's web flow and on customer statements but is **inconsistent on the partner's mobile app**: the in-app onboarding flow names the bank as the insured depository institution clearly, but the in-app help-centre article and one push-notification template refer generically to "FDIC insurance" without naming the bank. Section 4 records the inconsistency; section 6 termination triggers includes a Part 328 Subpart B violation as a documented trigger; recommended owner action is to issue a remediation request to the partner with a 60-day target, with the bank's marketing-review approval gate widened to cover help-centre articles and notification templates.
  - **Pass-through deposit insurance recordkeeping under 12 CFR Part 330 §330.5 [verify section].** **Gap on the consumer-loan product side.** The deposit-product FBO recordkeeping is adequate (the middleware platform's ledger meets §330.5 conditions, the bank's reconciliation tests confirm, the bank's attestation is on file). The consumer-loan product flows funds through a separate FBO-style settlement account during originations and during repayments; the §330.5 recordkeeping at the platform for this account has not been independently tested in the most-recent reconciliation cycle. The bank's classification of this account as "settlement-only and not custodial" needs re-confirmation; if the classification holds, §330.5 does not apply; if the account holds end-user funds even briefly in a custodial posture, §330.5 does apply and the recordkeeping is `[evidence needed]`. Recommended owner action is a legal-and-operations review with a 90-day target.
  - **Complaint routing.** Front-line receiver is the fintech; forward-to-bank cadence is daily aggregated plus same-day for severe complaints; CFPB Consumer Complaint Database handling and FDIC consumer-complaint portal handling are documented. SAR-decision QA at the partner: the partner's BSA / AML independent test surfaced a SAR-decision QA backlog (~14% of in-cycle SAR decisions had a QA review aging beyond the partner's 30-day internal target); the bank's BSA officer raised this in the prior quarter and the partner committed to a remediation plan with a 90-day target. **Section 4 carries the open finding; section 6 carries the deterioration trigger; recommended owner action is to validate the remediation closure before the next refresh.**

- **Section 5 — Reg O / Reg W / Reg E / Reg DD applicability summary.**

  | Regulation | Applicable | Position | Gap description |
  |---|---|---|---|
  | Reg O (12 CFR Part 215) | yes | One fintech board observer is a related interest of a director of the sponsor bank under §215.2(n) [verify section]; no extension of credit currently identified; exception not documented | document exception or restructure the relationship before next renewal cycle |
  | Reg W (12 CFR Part 223) | no | Fintech is not an affiliate under §223.2 | n/a |
  | Reg E (12 CFR Part 1005) | yes | Bank is the financial institution under §1005.2(i) for the deposit product; bank carries §1005.11 timing; bank-fallback SOP tested | adequate; no gap |
  | Reg DD (12 CFR Part 1030) | yes | Bank is the depository institution; bank carries §1030.4 disclosure and §1030.8 advertising-rule risk | bank's attestation cadence on fintech-shipped copy 8 months stale against 6-month target |

- **Section 6 — Termination and wind-down readiness.** Triggers documented: financial deterioration, BSA / AML deterioration, cyber deterioration, regulator concern, contract breach, strategic exit, and **(added this cycle) Part 328 Subpart B violation**. Wind-down sequence: customer notification responsibility is the bank's, with a 30-day target; customer-account portability requires deconversion to an alternative bank for the deposit product, with the platform's ledger as the system of record for the deconversion file; FBO-account wind-down sequence is documented at the platform with the bank as the named-role owner of the final settlement step; pending Reg E disputes are inventoried weekly so the wind-down timeline is determinate; cyber-side wind-down covers audit-trail extraction and customer-NPI return-or-destruction with attestation. Most recent simulated wind-down tabletop: **10 months prior** to the refresh date; the prior tabletop covered the deposit product but not the consumer-loan product as it was added afterwards. Recommended owner action: run the next tabletop with the consumer-loan product included, target within 90 days.

- **Tail — Recommended owner actions, coverage gaps, source trace, sign-off.** Owner actions:

  - Document the Reg O exception for the fintech board observer or restructure the relationship before the next renewal cycle. Owner: general counsel. Target: 90 days.
  - Issue a Part 328 Subpart B remediation request to the partner covering the in-app help-centre article and notification template inconsistencies; widen the bank's marketing-review approval gate to cover those surfaces. Owner: head of consumer compliance. Target: 60 days.
  - Confirm or re-classify the consumer-loan settlement-account posture under 12 CFR Part 330 §330.5 [verify section]; if custodial, evidence the recordkeeping or remediate. Owner: head of deposit operations and general counsel. Target: 90 days.
  - Refresh the bank's marketing-attestation cadence on fintech-shipped copy to the 6-month target; document one missed-cycle remediation. Owner: chief compliance officer. Target: 30 days.
  - Validate closure of the partner's SAR-decision QA backlog remediation before the next refresh; until closed, the BSA / AML deterioration trigger remains warm. Owner: BSA officer. Target: 90 days.
  - Run the next simulated wind-down tabletop with the consumer-loan product included. Owner: head of TPRM. Target: 90 days.
  - Verify whether the original §1867(c) notification scope covers the consumer-loan product; if not, file a fresh notification within 30 days. Owner: general counsel. Target: 30 days.

  Coverage gaps: the failover-region resilience tabletop is partial; one fintech subcontractor (the dispute-management vendor) was added 4 months ago and the SOC 2 coverage on that subcontractor is pending the next audit cycle.

  Source trace anchors every material claim against `references/source-anchors.md`, `references/sector-overlays.md#banking`, and the loaded cross-cutting overlays. CSI references restricted to the bank's CSI access population per 12 CFR Part 309 (FDIC).

- **Recommended disposition: approve with conditions.** Conditions: the seven recommended owner actions tracked to closure with named owners and target dates; the partnership refresh holds at critical-activity classification; the next refresh runs at the 12-month mark, accelerated to 6 months if the Part 328 Subpart B remediation, the Reg O exception, or the SAR-decision QA backlog closure misses target. The named lead (the head of TPRM) attests; the chief compliance officer, BSA officer, and general counsel co-attest at the third-party risk committee. The pack is a draft until that step.

The pack stops at the recommendation. The board independent risk committee consumes separately.

#### Why this scenario matters

- **Boundary check on the bank-side lens.** The pack is the bank's record of how it discharges principal-supervisory accountability, not the fintech's compliance program. Section 4's Reg E and Reg DD attribution (and section 5's applicability summary) keep the bank's residual obligations visible regardless of which entity does intake.
- **Boundary check on Reg O at intake and on refresh.** The Reg O screen runs every cycle; failure to run is a finding regardless of result. The screen surfaced a related-interest fact the prior cycle missed; the bank documents the exception or restructures.
- **Boundary check on FDIC Part 328 Subpart B across customer-facing surfaces.** The misrepresentation rule reaches every customer-facing surface where the bank is named as the insured depository institution; inconsistency across the mobile app, web, email, and in-app surfaces is the most common defect.
- **Boundary check on Part 330 FBO recordkeeping for both products.** Pass-through coverage attaches conditionally; the bank evidences §330.5 conditions per account, not per relationship. The consumer-loan settlement account needs its own classification decision.
- **Boundary check on Heightened Standards.** Part 30 Appendix D is OCC-only; for an FDIC-supervised state non-member bank below the $50B threshold, the citation is wrong on both supervisor and asset band. The substantive expectation can still be cited as the FDIC's large-bank-examination-program analogue once the bank approaches the threshold.
- **Boundary check on §1867(c) notification scope.** The original filing covers the original scope; product additions can fall inside or outside that scope depending on the original wording. The bank verifies rather than assumes.
- **Boundary check on wind-down tabletop coverage.** A tabletop that pre-dates a product addition does not cover the added product; the next cycle includes it explicitly.

#### Anchors

- Interagency Guidance on Third-Party Relationships: Risk Management (OCC / FRB / FDIC, June 6, 2023; OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023).
- 2024 Joint Agency Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services [verify exact title and bulletin reference].
- Bank Service Company Act, 12 USC §1867(c) (notification) and §1867(b) (examination authority).
- Reg O — 12 CFR Part 215 §§215.2 (definitions, related interest), 215.4 / 215.5 (general prohibitions and prior-approval), 215.8 (recordkeeping), 215.9 (reporting).
- Reg W — 12 CFR Part 223 §223.2 (affiliate definition); Reg W not applicable in this scenario.
- Reg E — 12 CFR Part 1005 §§1005.2(i), 1005.6, 1005.11.
- Reg DD — 12 CFR Part 1030 §§1030.3, 1030.4, 1030.8.
- 12 CFR Part 328 Subpart B — FDIC misrepresentation rule (effective 2022).
- 12 CFR Part 330 §330.5 [verify section] — pass-through deposit insurance recordkeeping.
- 31 CFR §1020.220 — CIP rule for banks; 31 CFR §1010.230 — beneficial-ownership rule for legal-entity customers.
- FFIEC BSA / AML Examination Manual (current edition).
- 12 CFR Part 304 — FDIC Computer-Security Incident Notification rule (36-hour clock).
- 12 CFR Part 309 — FDIC disclosure regime for CSI.

See `references/source-anchors.md` for full citations and `references/sector-overlays.md#banking` for the bank-side lens differentiators (loaded automatically). Cross-cutting overlays (`cyber.md`, `privacy.md`, `conduct.md`) load conditionally on the scope cross-cutting set; in this scenario all three apply.

## troubleshooting

### Troubleshooting: bank-fintech-partnership-review

Recurring defects in bank-fintech partnership packs and how to read past them. Read against `SKILL.md`, `references/source-anchors.md`, and `templates/default-output.md`. The lens here is sponsor-bank-side only; if the artifact reads as the fintech's compliance program, the wrong skill ran.

#### The pack reads as a fintech compliance program

Symptom: section 1 leads with the fintech's product roadmap; section 2 takes the fintech's SOC 2 report and Reg E procedures at face value; sections 4 and 5 attribute Reg E §1005.11 timing and Reg DD §1030.4 disclosure responsibility to the fintech without naming the bank's residual obligation.

Why it happens. The reviewer ran the diligence by reading the fintech's deck and policies in order, and the artifact follows the source ordering. Or the engagement was scoped against the fintech-side mirror skill (`fintech-partner-controls`) by mistake.

Fix. Hard-stop and re-spine. The pack is the bank's record of how it discharges principal-supervisory accountability under the June 2023 Interagency Guidance, the 2024 Joint Agency Statement, and the Bank Service Company Act §1867(c). Section 1 leads with what the fintech does for the bank's customers, where the fintech sits in the customer experience, and the criticality classification the bank assigns. Sections 4 and 5 attribute Reg E and Reg DD obligations to the entity that holds them under §1005.2(i) and §1030.2 respectively; in a sponsor-bank deposit program that is the bank, regardless of which entity does intake. Fintech materials are evidence pointers in section 2, not the spine of the pack.

Check. The Reg O / Reg W / Reg E / Reg DD applicability summary in section 5 attests to the bank's position; the chief compliance officer or general counsel signs against it. If the summary cannot be signed without rephrasing every cell, the lens is still wrong.

#### Reg E §1005.11 timing mis-stated as 5 business days

Symptom: section 4 or section 5 cites "5 business days for Reg E error investigation" or conflates the 10 / 45 / 90-day windows into a single shorter clock.

Why it happens. Industry shorthand collapses the 10-business-day investigation window with the 5-business-day provisional-credit issuance window (which is the deadline after extending the investigation to the 45-day window, not a separate investigation clock). The error sneaks in when the pack is drafted from memory rather than against the regulation.

Fix. Cite §1005.11 as it reads: investigation completed within 10 business days of the consumer's notice of error, OR (if the institution provisionally credits the consumer's account) extended to 45 calendar days for the full investigation (90 calendar days for new accounts opened within 30 days of the error, point-of-sale debit-card transactions, and foreign-initiated transfers). Written notification of the investigation results is due within 3 business days after completion. The bank has no contractual route to shorten or contract around the 10-business-day clock; the pack tests the bank's fallback when the fintech misses an intake event so the consumer's notice of error reaches the bank in time to start the clock.

Check. The Reg E row in section 4 cites §1005.11 with the 10 / 45 / 90 windows named explicitly, and the bank-fallback row carries a named SOP and a tested cadence (not a contract clause). If the pack only carries the contract clause, that is a section-3 control statement, not section-4 evidence.

#### §1867(c) notification conflated with §1867(b) examination authority

Symptom: section 2 or section 3 cites "§1867(c) examination authority" and either skips the notification posture entirely or treats the contract's examiner-access clause as evidence the §1867(c) notification has been filed.

Why it happens. The Bank Service Company Act bundles examination, regulation, and notification into one section of the US Code, and practitioners refer to "§1867(c)" as shorthand for both the bank's 30-day notification obligation to its primary federal regulator and the agencies' examination authority over bank service providers. They are linked but separate.

Fix. The notification under §1867(c) is a bank-side filing obligation (notify the OCC, FRB, or FDIC within 30 days of entering into a contract for, or starting to receive, a covered service). The examination authority that lets the agencies examine the service provider directly sits at §1867(b) and (c) read together. The contract's examiner-access flow-down is the third element (the contractual seam that gives the bank a right to insist the fintech cooperates with the regulator's examination). The pack carries all three: notification status (filed yes / no / not-yet-required, with date), examination-authority recognition (the contract acknowledges the agencies' authority), and the flow-down clause (examiner cooperation, books-and-records access, subcontractor cooperation). A partnership without §1867(c) flow-down is a finding regardless of how strong the rest of the contract reads.

Check. Section 2 carries the notification posture as its own row in the Reg O / Reg W / §1867(c) cluster; section 3 carries the flow-down clause as the load-bearing first row of the contract-gap table. If both are not separately named, the pack is missing one of them.

#### Reg W §223.42 sister-bank reference applied to a non-sister relationship

Symptom: section 2's Reg W affiliate test concludes "covered transactions exempt under §223.42 sister-bank exemption" or words to that effect, when the fintech is not a sister bank but an unaffiliated third-party fintech.

Why it happens. The Reg W subpart structure is dense; §223.41 and §223.42 sit close together in the exemption subpart, and the sister-bank exemption (§223.41(a) [verify exact paragraph]) is the most-cited Reg W exemption in BHC-internal training material. Practitioners reach for it by reflex on any affiliate-styled question.

Fix. Run the Reg W screen in two steps. First, determine whether the fintech is an affiliate at all under §223.2 (the 25%-control test, management-interlock, or common control through a holding-company structure). A typical bank-fintech relationship where the fintech is an unrelated third party is not an affiliate; Reg W does not apply, and §223.41 / §223.42 exemptions are inapplicable because there is nothing to exempt. Mark Reg W "not applicable" with the screen result documented. Second, where the fintech is an affiliate (most often where the fintech is a BHC-subsidiary or shares common ownership), then run the §§223.11 / 223.12 covered-transaction analysis with the §223.13 collateral and §223.14 low-quality-asset screens, and only then reach for §223.41 / §223.42 exemptions if any apply. The sister-bank exemption requires that both entities be insured depository institutions under common control; a fintech is rarely both.

Check. The Reg W row in section 5 reads "applicable: no" with the screen result, OR "applicable: yes" with the affiliate determination basis named (control test, management interlock, or common control) and the covered-transaction inventory set out. Citation to §223.41 / §223.42 only appears where the affiliate determination is "yes."

#### BaaS deposit program reviewed without the FDIC Part 328 Subpart B misrepresentation lens

Symptom: section 4's UDAAP screen on customer-facing copy reads as a CFPB-only review; the FDIC misrepresentation rule at 12 CFR Part 328 Subpart B is absent from the contract-gap section, the customer-facing-controls section, and the recommended-owner-actions tail.

Why it happens. The misrepresentation rule moved into Part 328 Subpart B in 2022 and the practitioner muscle memory still reads "FDIC sign and advertising rules" as Subpart A only. On a sponsor-bank deposit program where the fintech surfaces "FDIC-insured" representations to end users, the operative rule is Subpart B.

Fix. Carry Part 328 Subpart B as a named row in three places. Section 3 contract-gap: the contract requires the fintech (and any middleware platform) to comply with FDIC misrepresentation requirements on customer-facing copy that names the bank as the insured depository institution; absence is a finding. Section 4 customer-facing controls: the bank's marketing-review approval gate covers the fintech's mobile-app, web, email, and in-app messaging surfaces; the inventory is named, the cadence is named, and the bank's attestation owner is named. Section 6 termination triggers: a Part 328 Subpart B violation by the fintech is a documented termination trigger, not just a remediation event.

Check. Section 4 lists each customer-facing surface (mobile app, web, email, in-app, statements) and the bank's most-recent attestation date for each. Inconsistency across surfaces (the most common defect) surfaces in the row, not in a separate footnote.

#### Pass-through deposit insurance reviewed without FBO recordkeeping under Part 330

Symptom: section 1 names pass-through deposit insurance as a feature of the deposit program; section 2 confirms the FBO-account structure; the Part 330 §330.5 [verify section] recordkeeping conditions go unexamined.

Why it happens. Pass-through coverage feels like a marketing-side feature ("deposits are FDIC-insured up to $250k per end user"), and reviewers confirm the FBO-account structure exists without testing whether the recordkeeping at the bank, at the fintech, or at the middleware platform actually meets the conditions for pass-through coverage to attach. Without compliant recordkeeping the pass-through coverage fails, end users are exposed to the bank's solvency rather than the FDIC fund, and the bank carries the reputational and operational-risk consequence.

Fix. Section 1's money-flow row names the ledgering location (bank, fintech, or middleware platform); section 2 carries a Part 330 §330.5 recordkeeping row that names the named-role owner of the recordkeeping at each location, the reconciliation cadence, the most recent independent reconciliation test, and the bank's attestation that the records meet the §330.5 conditions. A "documented" status without an attestation is a partial finding. Where the recordkeeping sits at the middleware platform, the platform is a fourth-party and the bank's program covers it; section 3 contract-gap carries a flow-down row to the platform on the §330.5 obligations.

Check. Section 1 names the ledgering location explicitly; section 2 carries the §330.5 row with status, evidence pointer, and most-recent reconciliation date; section 3 carries the platform flow-down row. If any of the three is missing, the pass-through claim has not been evidenced and the pack should mark it `[evidence needed]`.

#### OCC Heightened Standards (12 CFR Part 30 Appendix D) cited for a non-OCC-supervised sponsor bank

Symptom: section 1's Heightened Standards row cites Part 30 Appendix D as the operative framework for a $52B state non-member bank supervised by the FDIC, or for a state-member bank supervised by the FRB.

Why it happens. Part 30 Appendix D is the most-cited "large bank governance" framework in industry training, and reviewers apply it by asset-size reflex without checking the supervisor. The OCC owns Part 30 Appendix D and applies it to its own large national banks and federal savings associations. The FRB has its own large-bank governance framework (LFI rating, the SR-letter set on risk-management expectations); the FDIC supervises state non-member banks under its own large-bank examination program but does not have a direct Part 30 Appendix D analogue.

Fix. The Heightened Standards row in section 1 reads "applicable" only where the bank is OCC-supervised AND meets the $50B+ avg total consolidated assets threshold. For FRB-supervised state-member banks, cite the FRB's large-bank governance framework (LFI rating, SR letters) as the operative analogue and name the analogue rather than citing Part 30 Appendix D. For FDIC-supervised state non-member banks at the same asset band, cite the FDIC's large-bank examination program as the analogue. The substantive expectation (that third-party-risk integration into the risk-governance framework is examined alongside the partnership pack) holds across all three regulators; the citation does not.

Check. Section 1's Heightened Standards row carries the bank type and the primary federal regulator named alongside the asset band. If the bank is not OCC-supervised, Part 30 Appendix D is not the citation; the FRB or FDIC analogue is.

#### Section 6 wind-down reads as theoretical

Symptom: section 6 carries the wind-down sequence as a narrative ("in the event of termination, the bank would notify customers, return data, and reconcile the FBO account") with no test date, no named owner per step, and a "most recent simulated wind-down" field reading `none` or left blank.

Why it happens. The contract has wind-down clauses, the reviewer reads them, and the pack paraphrases them. The clauses are control statements; the wind-down sequence as evidenced is a different artifact (the most recent tabletop or simulated wind-down test record).

Fix. Section 6 carries the wind-down sequence with each step (customer notification, customer-account portability, FBO-account wind-down, resolution of pending Reg E disputes, Reg DD obligations, cyber-side wind-down) keyed to a named role at the bank and the fintech, and with the most-recent-test-date field populated. Where the field reads `none`, that is itself a finding; the recommended-owner-actions tail carries an action with a target date to run the first tabletop, not a narrative reassurance. For critical-activity classifications, examiners read the test-record field first; an unfilled field reads as not-ready.

Check. Section 6's most-recent-test-date row carries a date or `none`; section 6's wind-down sequence carries named roles for each step; the recommended-owner-actions tail carries a tabletop-cadence action where the test-record field reads `none`. If section 6 reads as a paraphrase of the contract, the spine has not been re-built against the test record.

#### CSI carried forward into a pack at a wider access population

Symptom: section 1 or the executive summary references a prior MRA or supervisory letter against the sponsor bank by verbatim text, including the regulator's findings language; the pack distribution list includes the partnership owner, the fintech relationship-management lead, and the head of vendor management (a wider access population than the bank's CSI access population).

Why it happens. Confidential supervisory information about the bank (prior MRAs, MRIAs, supervisory letters, examination reports) is often the most material context for the partnership review, and the reviewer pulls it forward to motivate the recommended actions. Without the access-population check, the pack carries CSI to recipients outside the bank's CSI population.

Fix. CSI under 12 CFR Part 4 Subpart C (OCC), Part 261 (FRB), or Part 309 (FDIC) is bound to the bank's CSI access population; verbatim text cannot leave that population without the regulator's written authorisation. Either summarise the finding without verbatim text (acceptable for a wider access population), or restrict the pack distribution to the CSI access population (named at the cover). The cover-block "Access population" field exists for exactly this constraint; if it reads "wide" or "partnership-team," verbatim CSI cannot appear in the body.

Check. The cover names the access population; section 1, the executive summary, and the source-trace cross-check that no verbatim CSI appears in the body where the access population is wider than the bank's CSI population. Where the substantive finding still needs to motivate the recommended actions, the body summarises (e.g., "the bank has an open supervisory finding on third-party-risk-management governance" without quoting the regulator's language) and the source-trace marks the underlying citation as restricted.
