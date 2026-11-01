# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## cyber-phishing-amber-with-overlay

### Example: AMBER cyber phishing-test KRI commentary with disclosure-controls overlay

Public-source-derived. No named institution. Framing patterns from BCBS 239 (January 2013) Principles 7 and 9, the FFIEC IT Examination Handbook Information Security and Cybersecurity sections, and the SEC cyber disclosure framework (Item 1.05; 8-K disclosure controls and procedures discipline). The cross-cutting cyber overlay is loaded; the climate and privacy overlays are not in scope.

#### Input

- Institution: public-company bank holding company; SEC registrant; NYDFS-licensed at the bank-subsidiary level.
- Engagement scope supplied: primary regulators FRB, OCC, NYDFS, SEC; persona = head of risk reporting, second line, reporting to the CRO; sector overlay = banking; cross-cutting overlay = cyber; source posture = public-plus-firm-policy-plus-system-of-record-evidence.
- KRI: `CYB-007 / Phishing simulation click-through rate`. Threshold structure: limit = 15%, trigger = 10%, tolerance = 7%. Current value = 12.4%. Prior month = 11.7% (AMBER). Three consecutive months at trigger or breach.
- The CISO function has produced a first-line draft proposing to recalibrate the trigger from 10% to 13% in light of a Q2 change to the phishing-test template population (introduction of AI-assisted spear-phishing templates). Second-line is rewriting and challenging the recalibration.
- Linked feeds: the firm's phishing-simulation test population log, the test-design change record from Q1 to Q2, the secure-email-gateway efficacy reports, the training-completion records, and the most recent BCBS 239 self-assessment (no known limitations bearing on this metric, but a non-comparability flag from the test-design change).

#### Output sketch

The skill emits a per-KRI block. Headlines for this block:

- **Header table** — risk type = cyber; subtype = security-awareness; current = 12.4%; prior = 11.7%; direction = deteriorating (marginal); RAG current / prior = AMBER / AMBER; breach status = at-trigger; breach age = 3 periods; linked RAS metric = RAS-CYB-AWARENESS; owner = CISO (role).
- **Root cause (named)** — shift in phishing-test difficulty: Q1 used basic templates; Q2 introduced AI-assisted spear-phishing templates that raised the difficulty curve. The metric movement reflects test-design change, not a population control failure. The underlying control posture (mandatory training completion, multi-factor authentication coverage, secure-email-gateway efficacy) is unchanged across the three periods.
- **Contributing factors** — none `control-failure`; the underlying control posture is stable. `other` (test-design change) is the named driver.
- **Action taken in period** — communication to the workforce on AI-assisted phishing patterns (Owner: CISO; Completed: prior month; Evidence: workforce-communication record). Targeted retraining for the highest click-through cohort (Owner: CISO; Completed: prior month; Evidence: training-completion record).
- **Action planned** — refresh of the secure-email-gateway rules to detect AI-generated lures (Owner: CISO; Target: end of next month; Dependencies: vendor-rule-update ticket). Review of training content for AI-assisted phishing patterns (Owner: CHRO with CISO; Target: next quarter; Dependencies: none).
- **Residual-risk view** — Expected RAG next quarter: AMBER, trending toward GREEN once the gateway-rule refresh and training content land. Not yet evidenced; the residual-risk view is conservative on intent.
- **Linked items** — Issues: none (this is a metric movement attributable to test redesign, not a control issue). Material events: none.
- **Second-line challenge note** — first-line draft proposed recalibrating the trigger from 10% to 13% in light of the test-design change. The second-line view is that the trigger should remain at 10% pending two more periods of refreshed test-population data; recalibrating mid-stream would mask the metric movement and weaken the comparability of future commentary. The challenge note names this divergence and the rationale.
- **Threshold recalibration request** — first-line request named and surfaced for the RAS-owner: proposed change = trigger from 10% to 13%; rationale (first-line) = test-design change raised the difficulty curve; approver role = CRO with risk-committee acknowledgement. Second-line view (above) is to defer.
- **Data confidence note** — non-comparability flag: the Q2 test-population is not comparable with Q1 because of the template-difficulty change. The metric requires two more periods under the new template population to be reliable for trend.
- **Cyber overlay note** — three consecutive periods at trigger triggers the disclosure-controls leading-indicator review per the cross-cutting cyber overlay. Cross-reference `cyber-disclosure-readiness` Artifact C (DCP readiness map): the question for the disclosure-controls trace is whether sustained AMBER on a security-awareness KRI should feed the firm's leading-indicator monitoring under Item 106 disclosure-controls discipline. The pack carries the referral; the disclosure-process owner makes the call.
- **Source trace** — every material claim mapped to source (test-population log, test-design change record, training records, gateway efficacy reports). Confidence: medium across the block, driven by the non-comparability flag.
- **Confidence label** — medium. The test-design change introduces non-comparability with prior periods; the metric requires two more quarters under the new template population to be reliable.

#### Why this scenario matters

- Threshold-recalibration request is named, not buried. The first-line ask is surfaced; the second-line view is named; the approver role is identified. The skill does not adjudicate the recalibration; it routes it.
- Non-comparability of metric data is treated as a data-confidence issue. The block carries the explicit non-comparability flag.
- Cross-cutting cyber overlay drives the disclosure-controls referral. Sustained cyber-KRI deterioration is a leading indicator that should feed the firm's disclosure-controls monitoring; the block names the cross-reference rather than absorbing it.
- Action plan has owners and target dates. Both action items carry role-level owners and explicit target dates; dependency IDs are included where relevant.
- Confidence label is medium, not high, because the test-design change degrades comparability.

#### Anchors

- BCBS 239 (January 2013), Principles 7 (accuracy of the metric attribution) and 9 (clarity and usefulness).
- FFIEC IT Examination Handbook, Information Security and Cybersecurity sections, KRI examples for security-awareness programs.
- SEC cyber disclosure rule (Release Nos. 33-11216, 34-97989, July 2023) Item 1.05 trigger framework and Regulation S-K Item 106 disclosure-controls discipline; effectiveness verified at write time.
- Cross-link: `cyber-disclosure-readiness` Artifact C (DCP readiness map).

See `references/source-anchors.md` for full citations and verification flags.

## operational-loss-red-quarterly

### Example: RED operational-loss KRI commentary for the quarterly committee pack

Public-source-derived. No named institution. Framing patterns from BCBS 239 (January 2013) Principles 7 and 9, the Basel revised principles for the sound management of operational risk (March 2021), and OCC Heightened Standards (12 CFR Part 30 Appendix D) Section III on the risk appetite statement.

#### Input

- Institution: large covered bank under OCC Heightened Standards. Operational risk is the firm's largest non-credit risk type by economic capital and by management attention.
- Engagement scope supplied: primary regulators OCC and FRB; persona = head of operational-risk reporting, second line, reporting to the CRO; sector overlay = banking; cross-cutting overlay = none for this block (cyber and climate not relevant to this KRI); source posture = public-plus-firm-policy-plus-system-of-record-evidence.
- KRI: `OPS-001 / Operational loss events > $1m`. Threshold structure: limit = $10m gross loss in quarter, trigger = $7.5m, tolerance = $5m. Current value = $14.8m. Prior quarter = $9.2m (AMBER). Two consecutive periods at trigger or breach.
- First-line ORM has produced a draft commentary attributing the breach to "elevated external fraud activity". Second-line is rewriting.
- Linked feeds: the firm's loss-event log for the period, the post-event reviews on the three discrete loss events that drove the movement, the issue log, and the most recent BCBS 239 self-assessment (no known limitations bearing on this metric).

#### Output sketch

The skill emits a per-KRI block plus the wrapper headers. Headlines for this block:

- **Header table** — risk type = operational; subtype = external-fraud; current = $14.8m gross; prior = $9.2m; direction = deteriorating; RAG current / prior = RED / AMBER; breach status = breach; breach age = 2 periods; linked RAS metric = RAS-OP-EXT-FRAUD; owner = head of operational-risk reporting (role, not name).
- **Root cause (named)** — three discrete loss events drove $11.2m of the $14.8m: (i) account-takeover fraud on the digital channel, single event $6.4m, in May; (ii) check-kiting ring, single event $3.1m, in June; (iii) wire-fraud impersonation on a corporate-banking customer, single event $1.7m, in June. The remaining $3.6m sits across a long tail of smaller events consistent with the prior-period mix.
- **Contributing factors** — `control-failure` (digital-channel step-up authentication did not trigger for two of the account-takeover sub-events; documented in the post-event review of event (i)); `external-driver` (industry-wide uptick in check-kiting reported by the federal financial-crime intelligence body covering the period); `vendor` (the third-party fraud-screening service had a 14-hour outage during the wire-fraud event window, see Material Event ME-2025-Q2-003).
- **Action taken in period** — digital-channel step-up authentication policy revised and deployed (Owner: CISO; Completed: July 11; Evidence: change-management ticket CHG-44218). Wire-fraud impersonation control retraining for corporate-banking RMs (Owner: head of corporate banking; Completed: July 22; Evidence: training-completion record).
- **Action planned** — review of the third-party fraud-screening service exit plan and dual-vendor architecture (Owner: head of vendor management; Target: end of Q3; Dependencies: ISS-2025-0723). Update of the operational-risk RAS metric on external-fraud loss tolerance (Owner: CRO; Target: presentation at the next risk committee).
- **Residual-risk view** — Expected RAG next quarter: AMBER, not GREEN. Rationale: three months is insufficient to establish trend; the check-kiting external driver persists per current threat intelligence; the dual-vendor architecture is not yet in place.
- **Linked items** — Issues: ISS-2025-0712 (digital-channel control-design issue), ISS-2025-0723 (vendor outage issue). Material events: ME-2025-Q2-003.
- **Second-line challenge note** — first-line attribution of "elevated external fraud activity" understates the control-failure component (specifically the digital-channel step-up authentication gap). The second-line view is that the breach is materially driven by control failure, not external environment alone; the RAS-recalibration request must reflect this.
- **Threshold recalibration request** — none from the second line; the first-line proposal to widen the trigger from $7.5m to $9m is being challenged on the same grounds as the root-cause attribution.
- **Data confidence note** — none; the loss-event evidence is well-documented at source.
- **Source trace** — every material claim mapped to its source (loss-event log, post-event reviews, change-management ticket, training-completion record, vendor incident report). Confidence: high across the block.
- **Confidence label** — high. The loss-event evidence is well-documented; the control-failure root cause is supported by the post-event review.

The wrapper aggregate counts and the cross-KRI correlations sit alongside the other KRI blocks for the period; for this set the operational-loss KRI is one of three RED blocks and shares no cross-KRI correlation.

#### Why this scenario matters

- Multi-period breach with named root cause. The skill rejects "investigation ongoing" for breach age > 1; this block resolves to three discrete events with named drivers.
- Second-line challenge is explicit. First-line attribution to "elevated external fraud activity" is weak; the second-line view names the control-failure component and the threshold-recalibration challenge.
- Action plans carry owners (roles, not names) and target dates. Action items missing owner or target date are rejected by the schema.
- Residual-risk view is grounded. Expected RAG = AMBER, not GREEN, because the action plan has not yet completed and the external driver persists.
- Linked issues and material events are populated by foreign key. Downstream the committee pack consumes these references.

#### Anchors

- BCBS 239 (January 2013), Principles 7 (accuracy of the loss attribution) and 9 (clarity and usefulness; the prior commentary was not actionable).
- Basel Committee, Revisions to the Principles for the Sound Management of Operational Risk (March 2021), KRI taxonomy in operational risk.
- 12 CFR Part 30 Appendix D Section III (Risk Appetite Statement), the linkage between the KRI breach and the RAS metric carried in the committee pack.
- COSO ERM (June 2017), Performance component, the residual-risk view framing.

See `references/source-anchors.md` for full citations and verification flags.

## troubleshooting

### Troubleshooting: kri-commentary

Recurring defects in per-KRI commentary blocks. The skill should detect these at draft time; the head of risk reporting catches them at review.

#### 1. Commentary that restates the metric

The block reads "OPS-001 was RED at $14.8m, breaching the $10m limit." That is the metric, not commentary. The block must include a named root cause, contributing factors, action taken, action planned, and a residual-risk view. A block that fails this shape goes back to the drafter; the schema enforces it for status = red and for amber where breach age > 1.

#### 2. First-line voice in second-line commentary

The block reads as a first-line restatement: "The team is investigating the loss events and will report back next quarter." Second-line commentary is challenge, not narration. Either an explicit `second_line_challenge_note` or a documented rationale that the second-line view aligns with first-line is required.

#### 3. "Investigation ongoing" for multi-period breaches

A second consecutive period of breach with no named root cause is not credible. The schema requires a named root cause for `breach_age_periods > 1`. If the root cause is genuinely unknown after multiple periods, the named owner and target date for when the root cause will land are required instead, and the second-line challenge note carries the issue.

#### 4. Action planned without owner or target date

The block lists an action like "Review the vendor concentration" with no role-level owner and no target date. Schema rejects. Owners are roles, never named individuals; target dates are ISO dates, not "next quarter".

#### 5. Residual-risk view as wishful thinking

Expected RAG is GREEN next quarter on a multi-period breach where the action plan has not yet completed and the external driver persists. Schema rejects `expected_rag = green` where breach age > 1 and the action plan has not yet completed. The rationale must tie to the action plan and the external-driver outlook, not to optimism.

#### 6. Threshold recalibration buried in commentary

The first line is requesting a trigger or limit change in response to the breach, but the request is folded into the root-cause paragraph. The block must surface the recalibration request as a named item, with proposed change, rationale, and approver role. Recalibration in response to a breach is sometimes legitimate (the metric or population has changed) and sometimes masking; the committee, not the commentary, makes the call.

#### 7. Cyber KRI without disclosure-controls cross-reference

A cyber KRI has been at trigger or breach for two or more consecutive periods, and the block does not cross-reference `cyber-disclosure-readiness`. Sustained cyber-KRI deterioration is a leading indicator that should feed the disclosure-controls trace. The cross-cutting cyber overlay sets the cross-reference; the block carries it.

#### 8. Climate KRI without data-confidence caveat

A climate KRI relies on vendor-supplied scenario or emissions data, and the block does not carry a `data_confidence_note`. The cross-cutting climate overlay requires the BCBS 239 Principle 3 / Principle 6 caveat to be named on any climate KRI block. Without it, the block over-asserts the data quality the firm actually has.

#### 9. Cross-KRI correlation repeated in every block

Three KRIs share the same root cause (e.g., a vendor outage drove an operational-loss KRI, a third-party-availability KRI, and a customer-complaint KRI). The block-level commentary repeats the vendor outage narrative three times. The wrapper's `cross_kri_correlations` array exists to surface the shared root cause once; each block then references the correlation ID rather than restate.

#### 10. Owners as named individuals

Owner is "Jane Smith, VP of Cyber Operations". The skill rejects named individuals as owners; owner is "CISO" or "head of cyber operations". Named individuals belong in firm-internal artifacts and not in the commentary that may be shared upward, with the regulator, or with the auditor.

#### 11. Source trace empty for material claims

The block names a 14-hour vendor outage as a contributing factor; the source-trace table does not carry the vendor incident report as the evidence pointer. Every material claim needs a source-trace entry; unsupported items carry `[evidence needed]` and are routed to the engagement issue log, not silently into the block.

#### 12. Confidence label "high" with non-empty BCBS 239 known limitations on the metric

The block claims confidence = high; the metric is on the BCBS 239 self-assessment's known-limitations list (e.g., manual data extract, unreconciled source). The wrapper's aggregate confidence label is also constrained; high is unavailable while the metric is on that list. Medium at best.
