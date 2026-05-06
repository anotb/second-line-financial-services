# Spec sheet: payment-operations-incident-review

Plugin: `sector-plugins/payments-fintech-compliance`
Status: v1 retained skill (sector-unique under strict overlay rule).
Phase: 1 (spec only; no SKILL.md content here).

## Why this is a sector-only skill

A payments incident is not a generic operational incident. The notification triggers are rail-specific (Reg E timing windows, NACHA return and reversal mechanics, card-network dispute clocks, FedNow / RTP irrevocability), the reporting chain is sponsor-bank-mediated, and the customer-impact metric is denominated in payment populations (failed posts, mis-routed transfers, double debits, stuck holds, mis-applied returns). The capability skill it does not duplicate is the generic incident / control-failure pattern that lives inside `risk-compliance-core` and `compliance-testing`. Those produce a generic incident write-up; this produces a payments-incident write-up that survives a sponsor-bank notification SLA and a CFPB or state-AG inquiry.

There is also overlap with `risk-reporting/cyber-disclosure-readiness` for the cyber-component of payments incidents (when a payments outage was caused by a cyber event). This skill defers to that one for the SEC 8-K / NYDFS Part 500 / sponsor-bank cyber-notification pieces and stays focused on the payments-operational chain.

## Activation-tuned description

```
Drafts a payments-incident review pack: chronology, customer-impact population, Reg E and NACHA and card-network and FedNow / RTP notification triggers, sponsor-bank notification posture, root cause, remediation, and reporting chain. Output is review-ready for the program operator's second line and for production to the sponsor bank, the network (where applicable), and the regulator-facing incident file.

Best for:
- An ACH return spike, mis-posted batch, double-debit, stuck FedNow / RTP transfer, faulty Reg E claim queue, card-network fraud-rate breach, or processor-side outage has occurred and second-line needs the review pack.
- A sponsor-bank annual review or examiner data request includes incident retrospectives and the team needs the structured artifact.
- A subcontractor (processor, ledger provider, KYC vendor) outage has cascaded into the program operator's customer-impact surface and the team needs the rail-by-rail attribution and notification map.
- A near-miss has been escalated and second-line wants the same structure even though no customer was impacted, to evidence the control catch.

Not the right tool when:
- The work is a top-down rail-and-segment risk assessment (use payments-risk-assessment).
- The work is a controls inventory or self-evidence pack (use fintech-partner-controls or open-banking-data-controls depending on scope).
- The incident is purely cyber with no payments-operational impact (use risk-reporting/cyber-disclosure-readiness).
- The work is a SAR-decision review (use financial-crime-governance/sar-decision-qa).

Anchored to: Reg E (12 CFR Part 1005), in particular §1005.11 error-resolution timing (10 / 45 / 90-day windows), §1005.6 unauthorized-transfer liability, §1005.18 prepaid; NACHA Operating Rules (current edition) — return reason codes, return / reversal timing, ODFI return-rate thresholds, Same Day ACH; Visa Core Rules and Mastercard Rules — chargeback / dispute timing, fraud-rate program escalations [verify current thresholds]; FedNow Service Operating Procedures (current); Interagency Guidance on Third-Party Relationships (June 2023) and OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements (July 2024) [verify exact date] for the sponsor-bank notification chain; SEC cybersecurity disclosure guidance and NYDFS Part 500 §500.17 cyber notification where the incident has a cyber leg.
```

## Source anchors (skill-specific)

Named US sources, with section references where stable.

- **Reg E (12 CFR Part 1005):**
  - **§1005.11** — error resolution. The 10-business-day investigation window, the 45-day extended window with provisional credit, the 90-day window for new accounts and POS / foreign-initiated transactions, written notification timing, and the recordkeeping period.
  - **§1005.6** — consumer liability for unauthorized EFTs (the 2-day / 60-day liability tiers).
  - **§1005.18** — prepaid-account error-resolution overlays.
- **NACHA Operating Rules (current edition):**
  - **Return reason codes** (R01-R85 family) and **return timeframes** [verify against current edition].
  - **Reversal mechanics** — Originator-initiated reversals; the 5-banking-day window; reasons permitted [verify exact rule citation and window].
  - **ODFI return-rate thresholds** — administrative-return rate, overall return rate, unauthorized-return rate; ODFI obligations on threshold breach [verify current thresholds].
  - **Same Day ACH** — settlement windows, dollar-limit risk holds [verify current limits].
  - **WEB Debit account-validation rule** (effective March 19, 2021) [verify exact rule text and section reference].
- **Card-network rules, conceptual level:**
  - **Visa Core Rules and Visa Product and Service Rules** — chargeback rights, dispute timing windows, fraud-rate program escalations.
  - **Mastercard Rules** — equivalent.
  - **Both** — issuer / acquirer / processor allocations of dispute and chargeback duties; cardholder-facing notification timing where the program operator is acting on behalf of the issuer [verify; cite as conceptual].
- **FedNow Service Operating Procedures (current)** [verify version date] — settlement finality, request-for-return-of-funds mechanics (no chargeback), ISO 20022 message-field handling, fraud-hold posture options.
- **RTP (The Clearing House) Operating Rules (current)** [verify version date] — equivalent; treat as conceptual where the firm does not have a licensed copy.
- **ISO 20022 messaging** — conceptual reference; payment-incident triage often turns on which message field carried the bad value (e.g., creditor account, end-to-end ID, structured remittance information).
- **Interagency Guidance on Third-Party Relationships, OCC / FRB / FDIC, June 6, 2023** — sponsor-bank notification expectations and program-agreement notification SLAs.
- **OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements, July 2024** [verify exact date and title] — customer-impact reconciliation expectations.
- **SEC cybersecurity disclosure guidance** and **17 CFR §229.106 / §240.13a-11 (Item 1.05 of Form 8-K)** [verify exact citations] — where the program operator is a public registrant or its sponsor bank is, and the incident has a cyber leg with materiality reach.
- **NYDFS Part 500 §500.17(a)** — 72-hour cyber-incident notification; relevant where the program operator is a NYDFS-covered entity.
- **CFPB enforcement actions and supervisory highlights, 2023-26** [verify the specific actions current at the date of analysis] — public source for fact patterns on Reg E error-resolution timing failures, account-closure / hold UDAAP, and sponsor-bank reconciliation failures.
- **State Money Transmitter incident-reporting requirements** [verify state-by-state] — many MTL regimes require notification of material operational incidents to the state regulator, often through NMLS.

Treat every external source as an anchor, not a substitute for legal interpretation. Date every citation in the output.

## Sector overlays needed

Only `payments-fintech` (this is the sector skill).

## Cross-cutting overlays

- `cross-cutting/cyber.md` — required. NYDFS Part 500 §500.17(a) 72-hour notification, SEC cyber 8-K materiality assessment for public-registrant programs, sponsor-bank cyber-notification SLA, FFIEC incident-response expectations, and the cross-reference to `risk-reporting/cyber-disclosure-readiness` for the disclosure-track artifact.
- `cross-cutting/privacy.md` — required where the incident touched personal data. State breach-notification timing, GLBA Safeguards Rule incident-response posture (16 CFR §314.4(h)), §1033 implications where authorization flows or developer-interface tokens were involved.
- `cross-cutting/conduct.md` — recommended where the incident produced customer harm patterns (mis-applied holds, account closures, mis-disclosed fees) that map to UDAAP themes.

## Output template named sections

Practitioner headings on the default-output template. The named sections track the brief in the dispatch instructions.

1. **Incident summary** (one-paragraph; rail(s), product, customer-impact magnitude, status).
2. **Chronology** (timestamped, in the firm's local time and UTC; end-to-end from first signal through customer-facing remediation; identify which subcontractor or sponsor-bank touchpoint sits at each step).
3. **Customer impact** (population count, dollar magnitude, geographic breakdown, segment breakdown if relevant; how identified; how reconciled).
4. **Affected transaction population** (rail-by-rail breakdown: ACH originated / received, Same Day ACH, Wire, FedNow, RTP, card debit / credit; volume, value, status — completed / reversed / re-initiated / still in flight).
5. **Regulatory notification triggers** — explicit per source:
   - Reg E §1005.11 (was the customer-claim queue impacted; what is the timing posture on open claims).
   - NACHA (return / reversal mechanics, ODFI threshold posture, Same Day ACH limits implicated).
   - Card-network rules (chargeback / dispute timing windows, fraud-rate program implications).
   - FedNow / RTP (request for return of funds, message-field implications, irrevocability posture).
   - Sponsor-bank program-agreement notification SLA (the contractual clock; does it run from detection or from confirmed customer-impact).
   - State MTL / NMLS notification (where applicable).
   - Cyber leg, if any: SEC 8-K Item 1.05, NYDFS Part 500 §500.17, state breach-notification clocks (cross-reference `cyber-disclosure-readiness`).
6. **Root cause** (technical + control + governance; distinguish trigger from contributing factors; include any subcontractor-side root cause where the firm has visibility).
7. **Remediation actions** (immediate / short-term / structural; named owner role; target dates; control-design changes vs. control-execution fixes).
8. **Sponsor-bank reporting** (what was sent, when, by whom, against which program-agreement clause; what is still owed).
9. **Network / scheme reporting** (where applicable: NACHA, Visa, Mastercard, FedNow, RTP).
10. **Regulator-facing posture** (the regulator-facing artifact list; named human-review gates before any outbound).
11. **Customer-facing posture** (notification language, error-resolution status, provisional-credit posture, fee-reversal log).
12. **Lessons learned and forward controls** (which controls in `fintech-partner-controls` or `payments-risk-assessment` need updating).
13. **Source citations with date.**

## Structured output fields

| Field | Type | Purpose |
|---|---|---|
| `incident_id` | string | Internal identifier. |
| `rails_affected` | array of enum | ACH / Same_Day_ACH / Wire / FedNow / RTP / Card_debit / Card_credit / Card_prepaid / Check / Cross_border. |
| `customer_population` | object | Count, dollar magnitude, geographic split, segment split, identification method. |
| `chronology` | array of event | Each event: timestamp_local, timestamp_UTC, actor, action, system, evidence reference. |
| `transaction_population` | array of object | Each: rail, volume, value, status (completed / reversed / re-initiated / in_flight), source-system reference. |
| `reg_e_triggers` | array of finding | Each finding: trigger (§1005.11 / §1005.6 / §1005.18), state of compliance clock, action required, owner. |
| `nacha_triggers` | array of finding | Return-reason / reversal / threshold trigger, action required, owner. |
| `card_network_triggers` | array of finding | Visa / Mastercard chargeback / fraud-rate trigger, action required, owner. |
| `faster_payments_triggers` | array of finding | FedNow / RTP request-for-return / message-field issue, action required, owner. |
| `sponsor_bank_triggers` | array of finding | Program-agreement clause triggered, notification sent date, status. |
| `state_mtl_triggers` | array of finding | State, NMLS notification status, deadline, owner. |
| `cyber_triggers` | array of finding | Where a cyber leg exists: SEC 8-K Item 1.05 materiality status, NYDFS §500.17 clock, state breach clocks; cross-reference cyber-disclosure-readiness. |
| `root_cause` | object | Trigger, contributing factors, subcontractor attribution, control-design vs. control-execution split. |
| `remediation_actions` | array of action | Each: action, owner role, target date, status, control reference. |
| `sponsor_bank_reporting` | array of object | Each: report name, channel, date sent, against which clause, status. |
| `network_reporting` | array of object | Each: network, report name, date sent, status. |
| `regulator_artifact_list` | array of object | Each: artifact, regulator, status, human-review gate name. |
| `customer_facing_log` | array of object | Each: communication, channel, population, date, status. |
| `lessons_learned` | array of object | Each: control reference (in fintech-partner-controls or payments-risk-assessment), recommended change. |
| `gaps` | array of gap | Each: description, source citation with date, severity, owner, target close date. |
| `recommended_disposition` | enum (`closed`, `monitoring`, `open_remediation`, `escalate`) | Second-line recommendation. |
| `source_citations` | array of citation | Each: source name, section reference, retrieval date, URL where public. |

## Two example scenarios (public-source-derived, anonymous)

1. **Mis-applied ACH return batch causes 4-day delay in customer Reg E claim resolution at a BaaS-supported neobank.** Public anchor: Reg E §1005.11 (10-business-day window and provisional credit); NACHA Operating Rules return-handling articles [verify article and section]; Interagency Guidance on Third-Party Relationships (June 2023) sponsor-bank notification. Scenario: the program's processor mis-applied a batch of R10 (customer advises not authorized) returns into the operations queue, error-resolution claims tied to those transactions sat in a "pending" state for 4 business days, the §1005.11 10-business-day clock was about to breach for ~120 affected consumers, the program-agreement clause requires sponsor-bank notification within 24 hours of any control event affecting Reg E timing, and notification was sent on day 3. Skill output: chronology with the timeline mismatch, Reg E §1005.11 trigger and provisional-credit gap, NACHA mis-application root cause, sponsor-bank notification gap (24-hour clock missed), customer-facing log gap (no provisional credit entered), and a remediation map.
2. **FedNow instant-payout outage at a payroll-on-demand fintech.** Public anchor: FedNow Service Operating Procedures (current); NACHA Same Day ACH as the fallback rail; Reg E §1005.6 unauthorized-transfer-allocation question on funds that were debited but not credited; sponsor-bank program-agreement notification SLA. Scenario: the program's FedNow path through a newly-onboarded sponsor failed during a peak payroll window, the firm fell back to Same Day ACH outside the cutoff, ~3,000 customers received funds 24 hours late, ~200 customers were debited at the funding step but not credited (the FedNow request-for-return was initiated late), the program-agreement names ACH as the in-scope rail and FedNow only by amendment that was still in legal review. Skill output: chronology, customer-impact population by status, Reg E §1005.6 / §1005.11 implication on the 200 debited-not-credited cases, NACHA Same Day ACH cutoff documentation, FedNow request-for-return mechanics gap, sponsor-bank program-agreement amendment gap (FedNow not yet papered), state MTL notification map, and a forward control change tied back to `fintech-partner-controls`.

Both scenarios use only public sources. CFPB Supervisory Highlights and prudential-agency public statements on Reg E timing and reconciliation provide the conceptual fact pattern.

## Common pitfalls

- Letting the artifact look like an engineering post-mortem. The named sections (Customer impact, Regulatory notification triggers, Sponsor-bank reporting) are the centre of gravity for a regulator or sponsor-bank reader, not the technical timeline.
- Starting the Reg E §1005.11 10-business-day clock from confirmed-impact rather than from the consumer's notice. The clock runs from the consumer's notice; mis-stating that is a near-automatic finding.
- Missing the sponsor-bank program-agreement notification clock. It is usually shorter than any regulatory clock and is contractual, not regulatory.
- Treating a FedNow / RTP failure with ACH mechanics. Real-time rails do not have chargebacks; the recovery mechanic is request-for-return-of-funds, and the dispute pathway differs.
- Skipping the subcontractor-attribution piece. If the trigger is processor-side or KYC-vendor-side, the program operator still owes the customer and the sponsor bank a coherent root cause and a corrective-action commitment from the vendor.
- Forgetting Same Day ACH cutoff documentation when ACH is the fallback rail for a real-time outage. The "we used the next window" answer needs the exact cutoff cited.
- Conflating breach-notification clocks. SEC 8-K Item 1.05, NYDFS §500.17(a), state breach laws, sponsor-bank program-agreement clocks, and Reg E error-resolution clocks all run differently. The artifact has to keep them separate.
- Closing the incident without updating the forward controls in `fintech-partner-controls` or `payments-risk-assessment`. The lesson is the artifact's reason to exist.
