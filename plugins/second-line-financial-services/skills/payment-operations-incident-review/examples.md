# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## fednow-outage-payroll-on-demand-fallback-to-same-day-ach

### Example: FedNow instant-payout outage at a payroll-on-demand fintech

#### Input description

A program operator running a payroll-on-demand product on a newly-onboarded sponsor-bank stack runs its FedNow instant-payout path through the new sponsor's connection. During a peak payroll window, the FedNow path fails. The firm falls back to Same Day ACH but is past the cutoff for the next window; roughly 3,000 customers receive funds 24 hours late. Roughly 200 of those customers were debited at the funding step but not credited because the FedNow request-for-return-of-funds was initiated late and the recovery is incomplete. The program agreement names ACH as the in-scope rail; FedNow is named only by amendment that was still in legal review on the date of the incident.

The engagement was scoped at public-plus-firm-policy posture (no live system-of-record access at the time of the post-incident review). The audience is the sponsor-bank operating committee, with a parallel artifact for the state-MTL examiner via NMLS in the three states where the firm is licensed and where the operational-incident notification trigger is met.

#### Output sketch

The pack opens with an **incident summary** naming the rails (FedNow primary, Same Day ACH fall-back), the affected population (~3,000 late-credit; ~200 debited-not-credited), the contained-but-unreconciled status, the sponsor-bank notification clock posture (notification sent within the contractual clock), the named-rail notification clock posture (FedNow operational-incident report owed), and the contractual-vs-amended scope flag (the program agreement's rail set did not name FedNow at the time of the incident).

The **chronology** runs from the first FedNow path failure signal through the firm's escalation, the fall-back decision, the Same Day ACH cutoff miss, the FedNow request-for-return-of-funds initiation, the customer-impact reconciliation, and the ongoing remediation. The sponsor-bank operations team is named at the steps where it sits in the chain.

The **customer impact** block records the population in two segments (the ~3,000 late-credit population and the ~200 debited-not-credited population), the geographic breakdown (concentrated in the three NMLS-licensed states plus a long tail), and the segment breakdown (payroll-on-demand consumer only). The reconciliation method is named for each segment; the FBO subledger posture is recorded as "lagged the truth" during the incident window.

The **affected transaction population** has rows for FedNow (volume, value, status: in-flight pending request-for-return-of-funds resolution for the 200 debited-not-credited population) and Same Day ACH (volume, value, status: completed, with a delay-vs-cutoff note).

The **regulatory notification triggers** block fires on:

- The faster-payments sub-section: FedNow request-for-return-of-funds posture (initiated late; receiving-institution responses partially returned), ISO 20022 message-field handling (no bad-value field; the failure was at the path level), 24/7/365 operating-hours posture (firm staffing posture during the incident window recorded), operational-incident reporting under FedNow Service Operating Procedures (verify version and section).
- The NACHA sub-section: Same Day ACH cutover documentation (the firm used the next available window; the cutoff time and per-transaction limit are cited with the disclaimer applied).
- The Reg E sub-section: §1005.6 unauthorised-transfer-liability question on the 200 debited-not-credited population (the consumer was debited but the funds were not delivered; the legal characterisation is recorded as a counsel-routed open question), §1005.11 investigation-window posture for any consumer dispute claims arising from the incident.
- The sponsor-bank sub-section: program-agreement clause reference, clock-start basis (control event), notification sent within the contractual clock, supplementary notification on the customer-impact reconciliation, and the program-agreement amendment status flagged as a separate gap (FedNow was operating under an unsigned amendment).
- The state-track sub-section: three states with the operational-incident notification trigger met, NMLS notification posture per state, content requirements verified per state.
- No card-network, cyber-leg, or personal-data-leg sub-sections fire.

The **root cause** block names the trigger (FedNow path through the newly-onboarded sponsor failed during the peak payroll window), contributing factors (the firm's fall-back runbook did not account for Same Day ACH cutoff timing in a peak window; the FedNow request-for-return-of-funds initiation procedure was not staffed for the volume; the program-agreement amendment for FedNow was not signed before the rail was put into production), the subcontractor attribution (sponsor-bank operations was the immediate counterparty; FedNow itself is the named-rail authority and the firm has limited visibility into the path-level failure), and the control-design vs control-execution split (the fall-back runbook is a control-design gap; the request-for-return-of-funds staffing is a control-execution issue; the un-papered FedNow amendment is a governance gap that sits with legal).

The **remediation actions** block carries: immediate (request-for-return-of-funds escalation for the 200 debited-not-credited population; customer-facing communication drafted; provisional credit posture for the 200 affected consumers entered pending reconciliation closure), short-term (fall-back runbook rebuilt against Same Day ACH cutoff timing; FedNow request-for-return-of-funds staffing posture rebuilt; program-agreement amendment expedited through legal review and signed), structural (the firm's controls inventory in `fintech-partner-controls` updated against the named control families; the firm's `payments-risk-assessment` FedNow row's residual-risk reading and KRI dictionary updated).

The **sponsor-bank reporting** block records the in-clock notification, the supplementary notification, the FBO subledger reconciliation closure report owed, and the post-incident review report owed.

The **network or scheme reporting** block fires on FedNow Service Operating Procedures operational-incident reporting (verify version and section).

The **regulator-facing posture** block records the state-MTL notifications via NMLS for each of the three triggered states, with named human-review gates (head of payments compliance for content review; counsel for state-specific content requirements; sponsor-bank chief compliance officer counterpart for coordination).

The **customer-facing posture** block records the customer-notification language drafted for the late-credit population (3,000 consumers, in-app and email), the language drafted for the debited-not-credited population (200 consumers, individual outreach with provisional-credit posture and reconciliation-closure commitment), and the open consumer-EFT claim queue posture.

The **lessons learned and forward controls** block ties three control updates back to `fintech-partner-controls` (the fall-back runbook, the FedNow request-for-return-of-funds staffing, the program-agreement-amendment governance) and two risk-cell updates to `payments-risk-assessment` (the FedNow row's residual-risk reading and the cross-cutting operational-resilience row).

The **recommended disposition** is `open-remediation` with `escalate` flagged for the 200 debited-not-credited population pending reconciliation closure.

#### Why this scenario matters

The scenario tests the faster-payments-vs-card-rail recovery-mechanic discipline (the 200 debited-not-credited population requires request-for-return-of-funds, not chargeback; the artifact must not reuse the card-rail recovery template), the named-rail clock structure (FedNow Service Operating Procedures operational-incident reporting runs alongside the sponsor-bank contractual clock and the state-MTL notifications), the configuration-vs-engineering split (the un-papered FedNow program-agreement amendment is a governance gap that sits independently from the engineering failure of the FedNow path), and the multi-rail rail-by-rail attribution (the affected transaction population has FedNow and Same Day ACH rows, each with status detail).

The scenario also exercises the state-track row of the regulatory notification triggers block (three states with thresholds met; NMLS notifications recorded per state), which is a row that is frequently treated as default-to-USA and missed.

The scenario uses only public-source-derived material. FedNow Service Operating Procedures and CFPB themes on payroll-on-demand fee-and-tip presentation establish the conceptual fact pattern; no named institution is used in the artifact narrative.

## mis-applied-ach-return-batch-reg-e-timing-exposure

### Example: mis-applied ACH return batch causing consumer-EFT timing exposure at a BaaS-supported neobank

#### Input description

A program operator running a consumer neobank on a BaaS sponsor-bank stack discovers that its processor mis-applied a batch of unauthorised-return-code transactions into the operations queue rather than into the dispute-resolution queue. Roughly 120 consumer dispute claims tied to those transactions sat in a "pending" state for four business days. The named consumer-EFT investigation window is approaching breach for the affected claims, and the program-agreement clause-set requires sponsor-bank notification within 24 hours of any control event affecting the consumer-EFT timing posture. Notification was sent on day three. The processor has acknowledged the misapplication and provided a preliminary incident report.

The engagement was scoped at public-plus-firm-policy-plus-system-of-record posture. The audience is the sponsor-bank operating committee for the post-incident review, with a parallel artifact for the program operator's internal audit retrospective.

#### Output sketch

The pack opens with an **incident summary** naming the rail (ACH, consumer-account, with the unauthorised-return-code subset implicated), the affected population (~120 consumers; preliminary dollar magnitude pending reconciliation closure), the contained status, the sponsor-bank notification clock posture (sent day three, against a 24-hour contractual clock (overdue)), and the consumer-EFT clock posture (multiple claims at day eight or nine of the named investigation window).

The **chronology** runs from the processor's mis-application of the return batch through the firm's first detection signal (ops-team queue-volume alert), the queue investigation, the customer-impact reconciliation, the sponsor-bank notification, and the customer-facing remediation. Each row names the actor by role; the processor is named at the steps where it sits in the chain.

The **customer impact** block records the population (120 consumers, identified through full-population reconciliation against the dispute-claim system-of-record), the geographic breakdown (concentrated in two states), and the segment breakdown (consumer only, no SMB exposure). The reconciliation method is named.

The **affected transaction population** is one rail row (ACH consumer-account, with the unauthorised-return-code subset called out separately). Volume, value, status (the underlying transactions are completed; the disputes are open).

The **regulatory notification triggers** block fires on:

- The Reg E sub-section: §1005.11 investigation-window posture (10 business days from each consumer's notice; multiple claims at day eight or nine), §1005.11 provisional-credit posture (no provisional credit entered for the affected claims — gap), §1005.6 unauthorised-transfer-liability tier (consumer liability tier confirmed for each claim).
- The NACHA sub-section: return-reason-code mis-application root cause, no ODFI threshold posture change, no Same Day ACH or WEB Debit posture change. Disclaimer applied.
- The sponsor-bank sub-section: program-agreement clause reference, clock-start basis (control event), contractual deadline missed (sent day three against the 24-hour clock).
- The state-track sub-section: thresholds not met for the two states in scope; rows recorded as "not triggered" with the basis.
- No card-network, faster-payments, cyber-leg, or personal-data-leg sub-sections fire.

The **root cause** block names the trigger (processor mis-applied the return batch into the operations queue), contributing factors (the firm's queue-monitoring posture relied on the processor's own routing flags rather than on independent reconciliation against the system-of-record; the firm's sponsor-bank-notification runbook treated the notification clock as starting from confirmed customer impact rather than from control-event detection), the subcontractor attribution (processor-side root cause confirmed via processor incident report), and the control-design vs control-execution split (the queue-monitoring control is a control-design gap; the sponsor-bank-notification clock-start interpretation is a control-execution issue with a control-design implication for the runbook).

The **remediation actions** block carries: immediate (provisional credit entered for all affected claims; investigation-window extension noted; sponsor-bank supplementary notification sent), short-term (queue-monitoring posture rebuilt with independent reconciliation against the system-of-record; sponsor-bank-notification runbook updated to clock-from-detection; processor written notice issued with corrective-action commitment), structural (the firm's controls inventory in `fintech-partner-controls` updated against the named control families).

The **sponsor-bank reporting** block records the day-three notification, the supplementary notification, and the post-incident review report owed for the next operating-committee read-out.

The **lessons learned and forward controls** block ties two control updates back to `fintech-partner-controls` (the queue-monitoring control family and the sponsor-bank-notification runbook) and one risk-cell update to `payments-risk-assessment` (the ACH consumer-account row's residual-risk reading).

The **recommended disposition** is `open-remediation`.

#### Why this scenario matters

The scenario tests two of the most-frequent findings in this lane: clock-from-detection on the consumer-EFT investigation window (the artifact must run the clock from each consumer's notice, not from incident detection) and the missed sponsor-bank contractual notification clock (typically tighter than any named-rail clock, with the clock-start basis named explicitly). It also exercises the subcontractor-attribution discipline (processor-side root cause confirmed via incident report; firm's queue-monitoring posture is the control-design gap that allowed the processor's misapplication to persist) and the named-section structure under a single-rail incident.

The scenario uses only public-source-derived material. CFPB Supervisory Highlights and the 2023-26 sponsor-bank consent-order wave establish the conceptual fact pattern; no named institution is used in the artifact narrative.

## troubleshooting

### Troubleshooting: payment-operations-incident-review

Recurring pitfalls. Read before drafting if the engagement looks unfamiliar; consult after drafting if the artifact does not feel right to a senior payments-compliance reviewer or to a sponsor-bank operating-committee reader.

#### Engineering post-mortem framing

Symptom: the artifact reads as a chronology with a root-cause appendix. Customer impact, named-rail notification triggers, sponsor-bank reporting, and lessons-learned blocks are short or missing.

Why it fails: the named sections are the centre of gravity for a regulator-facing or sponsor-bank-facing reader, not the technical timeline. An engineering post-mortem is necessary input but not the artifact.

Fix: rebuild against the named-section spine. The chronology is one section among many; the customer-impact, regulatory-notification-triggers, and sponsor-bank-reporting blocks carry the load for the audience this artifact serves.

#### Clock-from-detection on the consumer-EFT investigation window

Symptom: the §1005.11 row of the regulatory-notification-triggers block runs the investigation-window clock from incident detection or from confirmed customer impact.

Why it fails: the consumer-EFT investigation-window clock runs from the consumer's notice of error, not from the firm's incident detection or from the confirmed-impact reconciliation. Mis-stating the basis is a near-automatic finding; the CFPB has pursued this in multiple Supervisory Highlights cycles.

Fix: record when each consumer's notice entered the queue, the queue's posture as of incident detection, and the timing exposure on each open claim. The §1005.11 sub-section names the clock-start basis explicitly.

#### Missed sponsor-bank contractual clock

Symptom: the sponsor-bank-reporting block names the notification sent date but does not name the contractual deadline or the clock-start basis.

Why it fails: the program-agreement notification clause is contractual, runs independently of any named-rail or regulator clock, and is typically the tightest. The clock-start basis matters: detection-based, control-event-based, and customer-impact-based clocks behave differently. Sponsor-bank TPRM reads this row first.

Fix: record the clause reference, the clock-start basis (per the program agreement), the contractual deadline, the actual notification (channel, addressee role, timestamp), and any supplementary notification. If the deadline was missed, the artifact records it as a finding with a named remediation rather than as an open item.

#### Reusing the card-rail recovery template for FedNow or RTP

Symptom: the FedNow or RTP rail row of the affected-transaction-population block carries a chargeback-status column. The faster-payments sub-section of the regulatory-notification-triggers block references chargeback windows.

Why it fails: settlement is final on receipt for FedNow and RTP. There is no chargeback. Recovery is request-for-return-of-funds plus monitoring escalation, and the response is at the receiving institution's discretion. The mechanics, the timing, and the artifact rows are different.

Fix: rebuild the FedNow and RTP rail rows and the faster-payments sub-section against the operative mechanics. Status columns: completed, returned-on-request, declined-on-request, in-flight. The faster-payments sub-section names request-for-return-of-funds posture, ISO 20022 message-field handling, and operating-hours coverage.

#### Categorical MSB-vs-not assertion

Symptom: the artifact contains a sentence asserting that "the firm is an MSB" or "the firm is not an MSB" without configuration-specific grounding.

Why it fails: MSB status is fact-pattern-specific against the FinCEN administrative-ruling library. Different configurations of the same product can fall on different sides of the line. A categorical assertion is an examiner-friendly target.

Fix: name the configuration as fact, the determination as a legal question that sits with counsel, and the operative posture (registration on file, written AML program, CIP applicability, SAR-filing chain, state-by-state operational-incident notification triggers) as evidence. The MSB / MTL status note in the artifact carries this discipline.

#### Default-to-USA on the state-track notification trigger

Symptom: the state-track row of the regulatory-notification-triggers block carries a single "USA" entry or is omitted because "this is a federal-rule incident".

Why it fails: many state money-transmitter regimes require notification of material operational incidents to the state regulator, often through NMLS. Notification thresholds, content, and timing vary state-by-state. A default-to-USA row hides the state-by-state triggers that an examiner reviewing through NMLS will look for.

Fix: one row per state where the firm is NMLS-licensed and the operational-incident notification trigger is met. Verify state-by-state on the analysis date. Where the trigger is not met, record the row as "not triggered" with the basis; do not omit it silently.

#### Closing the incident without forward-control updates

Symptom: the lessons-learned-and-forward-controls block is empty or carries generic language ("review controls in light of incident").

Why it fails: the lesson is the artifact's reason to exist. An incident review that does not produce updates to specific controls in `fintech-partner-controls` or specific risk cells in `payments-risk-assessment` has not closed. The next incident-retrospective cycle will read this gap as evidence the firm is not learning from incidents.

Fix: every closed incident produces at least one named control or risk-cell update. The block records the control reference, the recommended change, the control-design vs control-execution split, the owner role, and the target date.

#### Conflating cyber-leg disclosure clocks with payments-operational notification clocks

Symptom: the regulatory-notification-triggers block rolls the SEC Form 8-K Item 1.05 clock, the NYDFS 23 NYCRR Part 500 §500.17(a) clock, the federal banking agencies' 36-hour rule clock, the state breach-notification clocks, the sponsor-bank contractual clock, and the consumer-EFT clocks into a single "regulatory" timeline.

Why it fails: each clock runs independently, has its own clock-start basis, and is filed by a different entity through a different channel. A single timeline hides each clock's posture. The disclosure-track artifact (`cyber-disclosure-readiness`) handles the public-disclosure leg; the payment-operations-incident-review pack handles the payments-operational chain and flags the cyber leg.

Fix: one sub-section per regime in the regulatory-notification-triggers block. The cyber-leg sub-section carries the parallel cyber clocks separately and cross-references the disclosure-track artifact. The cross-cutting cyber overlay (`references/cross-cutting.md#cyber`) carries the parallel-clock detail.

#### Customer-impact population without an identification method

Symptom: the customer-impact block names a population count and dollar magnitude but does not name how the population was identified.

Why it fails: a population stated without an identification method is an assertion, not a finding. A sponsor-bank reviewer or an examiner cannot reconcile against the firm's system-of-record without knowing which method produced the count. A complaint-driven count under-counts; a sample-based count is statistical; a vendor-side report carries the vendor's reconciliation discipline rather than the firm's.

Fix: the customer-impact block names the identification method, the reconciliation method, the reconciliation cadence, the break-resolution log, and the FBO subledger posture during the incident window. A revised population count after reconciliation closure is normal; record both the preliminary and the final with the basis.

#### Drafting against the "current edition" of NACHA without the disclaimer

Symptom: the NACHA sub-section of the regulatory-notification-triggers block cites NACHA Operating Rules section numbers without the paywalled-disclaimer. Same pattern for the card-network sub-section against Visa Core Rules / Visa Product and Service Rules / Mastercard Rules.

Why it fails: NACHA Operating Rules and the card-network rulebooks are paywalled. Section numbers and threshold values shift between editions. Without the disclaimer, the citation reads as if it were verified against the current edition when it cannot be (the firm holds the licensed copy; the artifact cites against it conceptually).

Fix: every NACHA citation and every card-network citation carries the disclaimer "current edition; specific sections to be confirmed against the firm's licensed copy."

#### Drafting the cyber leg as a parallel artifact

Symptom: the artifact carries a full disclosure-decision workpaper, a Form 8-K Item 1.05 disclosure draft, and a 10-K Item 106 governance section.

Why it fails: the disclosure-track artifact lives in `cyber-disclosure-readiness`. Duplicating that work here pollutes the payments-operational pack and risks divergence between the two artifacts.

Fix: the cyber leg sits as a flagged row in the regulatory-notification-triggers block with the parallel cyber clocks, a cross-link to the disclosure-track artifact, and the named human-review gate (securities counsel, the disclosure committee). The cross-cutting cyber overlay carries the parallel-clock detail.

#### Vendor blame without basis

Symptom: the root-cause block assigns the trigger or the contributing factors to a named vendor (processor, ledger provider, KYC vendor, fraud-decision vendor) without naming the basis (vendor incident report, vendor-side log access, vendor post-incident review).

Why it fails: the artifact is a draft that the sponsor-bank reviewer and the firm's counsel will read. Unsupported vendor blame creates litigation exposure and breaks the program-vendor relationship. The risk-management discipline is to record the firm's visibility honestly.

Fix: subcontractor attribution is recorded only where the firm has visibility, with the basis named (vendor incident report on file, vendor-side log access reviewed, vendor post-incident review participated in). Where visibility is limited, the block records that as a gap and names the vendor-management ask. The program operator still owes the customer and the sponsor bank a coherent root cause and a corrective-action commitment from the vendor.

#### Engagement scope absent and not flagged

Symptom: the artifact reads as if a formal scope record were on file when it was not.

Why it fails: downstream skills key off the scope record (institution type, primary regulators, sector overlay set, persona, source posture). When scope was not formalised, the pack must say so; otherwise downstream consumers (`payments-risk-assessment` updating after the incident, `fintech-partner-controls` consuming the lessons-learned block) cannot calibrate.

Fix: when the practitioner did not supply a formal scope record, ask the four questions (rails affected, source posture, incident-clock stage, audience) and default to public posture if the practitioner declines. Note in the artifact that scope was not formalised; do not silently apply a default.
