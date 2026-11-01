# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## fbo-account-ledgering-overlay

### Example: FBO-account ledgering control overlay for a sponsor-bank deposit program

Scenario type: anonymised, public-source-derived; no named institution; the fact pattern reflects recurring themes in the 2024 Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services and in published consent orders against sponsor banks for FBO-reconciliation failures.

#### Input

Institution: community bank, $5B avg total consolidated assets, FDIC-regulated state-non-member bank. Operates a sponsor-bank deposit program with three fintech partners: Partner A (consumer neobank, $300M end-user deposits), Partner B (SMB-payments fintech, $80M end-user deposits), Partner C (early-stage consumer wallet, $20M end-user deposits). The bank holds deposits in three FBO accounts, one per partner.

Trigger: the board's audit committee requested a second-line control-matrix overlay for the FBO-account ledgering process after a peer-bank consent order on FBO-reconciliation failures was published. Source posture: 2024 Joint Statement on Bank-Fintech Arrangements plus the bank's internal FBO-ledger SOP and the three program agreements.

#### Output emphasis

**Process area in scope**: reconciliation and ledgering, with FBO overlay sub-section. Plus advertising-review process area (deposit-insurance representation row) and exception-handling process area (periodic re-attestation row).

##### FBO overlay sub-section

| Field | Partner A | Partner B | Partner C |
|---|---|---|---|
| End-user deposits | $300M | $80M | $20M |
| Daily reconciliation control | yes | yes | yes |
| Variance threshold | $1k (firm-wide default — flagged) | $1k (firm-wide default — flagged) | $1k (firm-wide default — flagged) |
| Pass-through deposit-insurance recordkeeping (12 CFR Part 330 §330.5) | documented | documented | partial — no daily snapshot of end-user balances at the bank's level retained |
| End-user ledger governance | weekly attestation by fintech CFO | weekly attestation by fintech operations lead | weekly attestation by fintech CTO |
| Wind-down sequence tabletop | never tested | never tested | never tested |
| Customer-facing deposit-insurance representation review (12 CFR Part 328 Subpart B) | documented | partial — last review 14 months ago | gap — no review on file |

**Spotlight rows.**

**Pass-through deposit-insurance recordkeeping (Partner C)**: 12 CFR Part 330 §330.5 [verify section] establishes the recordkeeping conditions for pass-through coverage on fiduciary and custodial accounts. The bank's custodial-account agreement and the fintech partner's end-user ledger together must satisfy the recordkeeping requirements. For Partner C, the bank receives an end-of-day file from the fintech but does not retain daily snapshots for the required period. Gap flagged. Without the daily snapshots, Partner C's end-user depositors lose pass-through coverage. Severity: critical. Recommended action: deposit-operations director to retain daily end-user balance snapshots for Partner C within 30 days.

**Daily reconciliation variance threshold**: bank reconciles total FBO balance at the bank's level to total of fintech-reported end-user ledger daily; firm-wide variance threshold is $1k. Reviewer question on whether the variance threshold is risk-based per program. For Partner A ($300M deposits), the $1k threshold may be too tight (noise from rounding, settlement-cutover edge cases) and trigger reconciliation alerts that desensitise the team. For Partner C ($20M deposits), the $1k threshold is plausibly calibrated but would benefit from an aging analysis. Recommended action: risk officer to refresh variance thresholds on a risk-based basis per program within 60 days.

**End-user ledger governance**: each fintech provides weekly attestations on ledger accuracy. Reviewer question on whether attestations are signed by an officer with adequate authority and independence at the fintech. Partner A's CFO satisfies; Partner B's operations lead has unclear authority at the fintech to bind on ledger accuracy beyond operational scope. Recommended action: head of vendor management to confirm Partner B's attestation signatory has adequate authority within 45 days.

**Customer-facing deposit-insurance representation (Partner C)**: gap — no marketing-claim review on file against 12 CFR Part 328 Subpart B. The fintech surfaces refer to "FDIC insurance" without the pass-through caveats. Severity: critical. Recommended action: marketing-and-compliance team to complete the review within 30 days; periodic re-attestation cadence to be set at quarterly (sits in exception-handling process area).

**Wind-down sequence tabletop**: no documented tabletop for FBO wind-down across any of the three programs. The bank has not tabletop-tested an FBO deconversion. Cross-reference to `bank-fintech-partnership-review` recommendation. Recommended action: head of vendor management to schedule an FBO wind-down tabletop for at least one program within 90 days.

##### Cross-cutting findings

**Cyber overlay** (loaded): each fintech partner falls under the bank's third-party-cyber program. SOC 2 Type II reports received and reviewed within last 12 months for each partner; Partner B's SOC 2 carries an exception on logical-access reviews; issue-writeup linked. Sponsor-bank cyber-notification chain (12 CFR Part 304 Subpart E for FDIC) requires the bank to determine within 36 hours of a notification incident; the contractual notification clock on each fintech is 24 hours. Operational capability to meet the 24-hour clock confirmed for Partner A; not yet confirmed for Partners B and C.

**Privacy overlay** (loaded): GLBA Reg P notice integration with each fintech. Reviewer question on whether the privacy notice issued to consumers correctly identifies the bank as the financial institution. Partner A's privacy notice confirmed; Partners B and C pending review.

**Conduct overlay** (loaded): account-closure and account-hold theme: the bank has received CFPB Consumer Complaint Database hits attributable to Partner A on hold-release-without-notice. Internal complaint data shows higher hold-release latency on Partner A than on Partners B and C. Recommended action: deposit-operations director to refresh the hold-release SLA for Partner A and to review the customer-recourse channel, within 60 days.

##### Coverage gaps

- No documented exit-sequence control for FBO wind-down across any program.
- Partner C: pass-through deposit-insurance recordkeeping gap (critical).
- Partner C: customer-facing deposit-insurance representation gap (critical).
- Partner B: end-user ledger attestation signatory authority unclear.
- All three programs: variance thresholds not risk-based per program.
- Partners B and C: privacy-notice review pending.
- Partners B and C: cyber-notification clock operational capability not confirmed.

##### Recommended owner actions

| Action | Owner role | Target date | Severity |
|---|---|---|---|
| Retain daily end-user balance snapshots for Partner C | deposit-operations director | 30 days | critical |
| Complete marketing-claim review for Partner C deposit-insurance representation | head of marketing and compliance | 30 days | critical |
| Confirm Partner B attestation signatory authority | head of vendor management | 45 days | high |
| Refresh variance thresholds on risk-based basis per program | chief risk officer | 60 days | high |
| Refresh hold-release SLA for Partner A | deposit-operations director | 60 days | moderate |
| Schedule FBO wind-down tabletop for at least one program | head of vendor management | 90 days | moderate |
| Confirm cyber-notification operational capability for Partners B and C | CISO | 60 days | high |
| Review privacy notice for Partners B and C | head of compliance | 60 days | moderate |
| Set quarterly re-attestation cadence on customer-facing deposit-insurance representation | head of compliance | 30 days | high |

##### Confidence and posture

- Confidence: high on §330 recordkeeping; medium on variance-threshold calibration; medium on end-user ledger governance pending Partner B and Partner C clarifications.
- Heightened Standards: not applicable (asset size below $50B).
- Public-source basis: anchored to 12 CFR Part 330 [verify section], 12 CFR Part 328 Subpart B (FDIC misrepresentation rule), 2024 Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services [verify exact title and date], FFIEC BSA / AML Examination Manual CIP and CDD sections, GLBA Safeguards Rule §314.4(f), GLBA Reg P. Anonymous; consent-order reference by docket only.

## reg-e-error-resolution-control-refresh

### Example: consumer-EFT error-resolution control refresh after an internal-audit finding

Scenario type: anonymised, public-source-derived; no named institution; the fact pattern reflects recurring CFPB Supervisory Highlights themes and prudential-regulator MRA patterns on dispute-timing breaches.

#### Input

Institution: midsize national bank, $12B avg total consolidated assets, OCC-regulated, retail and business deposit. Sponsor-bank programs: none. Prepaid products: none. Heightened Standards: not applicable. Internal audit found a 7% breach rate on the §1005.11(c) provisional-credit timing window (10 business days from receipt of a complete error notice for unauthorised-EFT claims; some POS / foreign-initiated cases use the 5-business-day window per §1005.11(c)(2)). Root cause: dispute reclassification cases reset the SLA clock incorrectly when escalated from one team to another.

The deposit-operations director needs the second-line control-matrix refresh for the consumer-EFT and ATM operations process area, ahead of the audit-committee follow-up. Source posture: public-plus-firm-policy-plus-evidence (the engagement has access to the dispute-management system aging report and the firm's dispute SOP).

#### Output emphasis

**Process area in scope**: consumer-EFT and ATM operations (§1005.11). Eight rows, one per §1005.11 control activity:

1. Error-notice intake — control objective: every consumer notice (verbal or written) is logged within one business day with the §1005.11(b) information set captured.
2. Classification at intake — control objective: the dispute is classified at intake against the §1005.11(c) timing tier (10-business-day general window, 5-business-day POS / foreign window, 20-business-day extension for new accounts).
3. Provisional-credit determination — control objective: where investigation is not concluded within the applicable window, provisional credit is applied to the consumer's account.
4. Investigation — control objective: investigation completes within 45 calendar days (90 calendar days for POS / foreign-initiated transactions and for new-account claims).
5. Notification of results — control objective: consumer receives written notification of investigation result within 3 business days of completion (or, where the bank determines no error, with re-debit notice).
6. Consumer-liability application — control objective: liability applied per §1005.6 tiers based on timeliness of consumer notice ($50, $500, unlimited).
7. Recordkeeping — control objective: §1005.13 records retained 24 months from date of error notice or date the action is required.
8. Periodic-trend monitoring — control objective: aggregate dispute-timing-breach rate, classification-distribution, and reclassification-frequency reported monthly to the deposit-operations director and quarterly to the compliance committee.

**Spotlight on the §1005.11(c) provisional-credit row.**

- Control objective: bank credits the consumer's account within 10 business days (or 5 / 20 as applicable) when a complete error notice is received and investigation is not concluded.
- Control activity: deposit-operations dispute team uses the dispute-management system, which auto-classifies the claim category at intake and triggers the SLA. Manual override exists for cases reclassified after intake.
- Owner role: deposit-operations dispute manager.
- Frequency: per case; monthly aggregate review.
- Test method: dispute-management-system case-aging report; quarterly sample of 30 reclassified cases reviewed by compliance.
- Evidence pointer: dispute-management-system case-aging report; sample list and reviewer-signoff log.
- Last test result: internal audit found 7% breach rate; root cause was reclassification cases reset the SLA clock incorrectly when escalated.
- Design effectiveness: operating, with design weakness on the reclassification path (auto-classification works at intake; SLA-clock continuity on reclassification is the gap).
- Operating effectiveness: medium — pending the system fix.
- Open issues: linked to issue-writeup ID [placeholder].
- Human-review required: yes — quarterly sample review by compliance.

**Cross-cutting findings (conduct overlay)**: UDAAP exposure from delayed provisional credit. CFPB has pursued §1005.11(c) breaches as both Reg E and UDAAP findings. Recommended a customer-make-good policy for breach cases (interest reimbursement and fee reversal where the breach caused customer harm).

**Coverage gaps**: prepaid-account controls (§1005.18) absent from the matrix — out of scope (the bank does not issue prepaid accounts); flagged as not applicable, not as a gap.

**Recommended owner actions**:

- Deposit-operations director to ship a system fix for SLA-clock continuity on reclassification within 60 days.
- Second-line monitoring control to add weekly aging-by-classification view (rather than monthly aggregate only).
- Compliance to review the customer-make-good policy and present to the compliance committee within 30 days.

**Confidence label**: high on the control-objective wording (driven by §1005.11 text), medium on operating effectiveness pending the system fix.

**Heightened Standards posture**: not applicable (asset size below $50B). Forward-looking section not required at this asset band.

**Public-source basis**: anchored to 12 CFR §1005.11(c)–(e), §1005.6, §1005.13. Anonymous; no named institutions. CFPB Supervisory Highlights cited by cycle for the conduct overlay; Circular 2022-06 on unanticipated overdraft fees referenced for adjacent UDAAP framing [verify current state of cycle and circular numbering on the analysis date].

## troubleshooting

### Troubleshooting: deposit-operations-controls

Recurring defects in deposit-operations control matrices and how to fix them. Read against `SKILL.md` and `templates/default-output.md`.

#### Conflating dispute-timing rows with consumer-liability rows

The dispute-timing rows under §1005.11 (the 10 / 45 / 90 business-day windows for provisional credit, full investigation, and notification) and the consumer-liability rows under §1005.6 (the $50 / $500 / unlimited tiers based on timeliness of consumer notice) are separate obligations. The matrix must keep them in separate rows even when they surface in the same dispute case. A row labelled "Reg E dispute handling" that conflates both is the most common defect on this process area; examiners read each rule line-by-line.

#### Missing the §1005.18 prepaid sub-regime when the bank issues prepaid products

Prepaid is a discrete sub-regime with its own pre-acquisition disclosure (short form and long form), error-resolution adapted from §1005.11, and the credit-feature rules under §1005.18(g). Do not fold prepaid into general consumer-EFT controls; carve it out as a separate sub-section of the consumer-EFT process area. If the bank does not issue prepaid products, mark the §1005.18 row as not applicable and flag in the coverage-gaps section as "scoped out, not a gap."

#### Treating §1030.8 advertising review as a single control

Advertising controls split into ad-content review (the message), APY-accuracy review (the math), and triggering-term review (when an APY ad triggers additional disclosures under §1030.8(c)). The matrix needs all three rows. Add a fourth row for sponsor-bank-program advertising approval-gate where applicable, and a fifth for marketing-claim review against the FDIC misrepresentation rule (12 CFR Part 328 Subpart B).

#### Skipping pass-through deposit-insurance recordkeeping on FBO accounts

12 CFR Part 330 §330.5 [verify section] establishes the recordkeeping conditions for pass-through coverage on fiduciary and custodial accounts. Without compliant recordkeeping, the FBO depositors lose pass-through coverage, and the bank's reputational and operational-risk exposure spikes. The matrix must include a §330 row when the scope includes a sponsor-bank program. Status field with values `documented` / `partial` / `not-applicable` / `gap`.

#### Treating the deposit-insurance misrepresentation row as a one-place row

The FDIC misrepresentation rule (12 CFR Part 328 Subpart B) covers three control surfaces: the bank's marketing-claim review (advertising-review process area), the customer-facing surfaces of any sponsor-bank fintech program where the bank is named as the insured depository institution (FBO overlay), and the periodic re-attestation that customer-facing surfaces remain compliant (exception-handling process area). Carry the row in all three places, not just one.

#### Citing the CFPB small-entity compliance guide instead of the regulation

The Compliance Aid is a plain-language interpretive aid. The obligation source on the matrix is the underlying CFR section (12 CFR Part 1005, 1030, or the relevant Reg CC / CIP / BO / Part 330 / Part 328 section). Cite the regulation; the guide goes in the secondary anchor row only.

#### Citing the OCC Comptroller's Handbook as the obligation source

The Comptroller's Handbook booklets (Bank Operations, Internal Control, Deposit-Related Credit) are supervisory guidance. The obligation source is the federal regulation. The Handbook goes in the secondary anchor row to explain the OCC's expectation on segregation-of-duties, reconciliation, and exception handling beyond the regulation text.

#### Citing the FFIEC BSA / AML manual as the only CIP source

The manual is interpretive guidance built on top of 31 CFR §1020.220 and the BSA. Cite the regulation; the manual goes in the secondary anchor row.

#### Treating supervisory guidance as a regulation

The 2024 Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services is supervisory guidance, not a regulation. Phrase obligation-source as "supervisory guidance" and cite the underlying regulation (consumer-EFT regime, truth-in-savings regime, 12 CFR Part 330, Part 328 Subpart B) for the binding text.

#### Treating exception governance as a hygiene control

Override and exception logs are an examiner-favourite review point. The matrix must include aggregate-reporting cadence, override-authority matrix, and a UDAAP screen on overrides that affect customers. A row that reads only as "exceptions are logged" misses the aggregate reporting and the customer-impact screen.

#### Reading NSF and overdraft rows only as truth-in-savings disclosure

The conduct lane is where the recurring CFPB enforcement on representment fees, surprise overdraft fees, and the authorised-positive-settled-negative pattern sits. Read the NSF and overdraft rows through both the truth-in-savings disclosure lens and the UDAAP screen lens. A row that reads only as a disclosure check misses the conduct lane.

#### Using a single dollar variance threshold across heterogeneous FBO programs

Variance thresholds on FBO daily reconciliation are risk-based per program. A $1k threshold is too tight on a $300M-deposit program (noise) and too loose on a $20M-deposit program (signal hidden). The matrix must surface the threshold per program, not a single firm-wide value.

#### Defaulting to "USA" on garnishment and escheatment rows

Garnishment processing is federal (31 CFR Part 212 for federal-benefit-payment lookback, 26 USC §6332 for IRS levy) plus state-by-state for state garnishment and state-tax levy. Escheatment is state-by-state. Default-to-USA on these rows misses the operative obligations; cite per state in the firm-overlay file rather than restating per state in the matrix body, but flag the multi-state scope explicitly.

#### Treating dormant-account reactivation as a hygiene control

Vulnerable-customer protection is a recurring conduct theme. Dormant-account reactivation rows must include joint-action requirements on large reactivations and a customer-protection screen for reactivations that trigger fees or that occur without the customer's clear request.

#### Skipping the Heightened Standards tie-in for covered banks

12 CFR Part 30 Appendix D applies to covered banks ($50B+ avg total consolidated assets). The matrix tail must carry a sub-section tying the deposit-operations controls into the operational-risk and risk-governance framework: which process areas feed which named operational-risk drivers; aggregate-exception reporting cadence to the chief risk officer and to the board independent-risk-committee; three-lines-of-defense maturity over the matrix. For banks approaching the threshold (typically $40B+), carry the forward-looking row even where Appendix D is not yet binding.

#### Treating "current edition" sources as evergreen

Comptroller's Handbook booklets, the FFIEC BSA / AML manual, the FFIEC IT Examination Handbook, and the CFPB Supervisory Highlights / Circular series are revised periodically. Pin the edition / cycle date in the source-trace block. Mark `[verify current state]` where the engagement relies on a specific edition.

#### Carrying confidential supervisory information forward into a matrix at a lower access population

Prior supervisory letters, prior MRAs / MRIAs, and prior examination reports are CSI under 12 CFR Part 4 Subpart C (OCC), Part 261 (FRB), and Part 309 (FDIC). The access population for the matrix itself constrains what it can include. A matrix shared with a fintech partner cannot carry the bank's CSI on a prior examination finding even where the finding informs the control rationale.
