# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## bcbs239-risk-data-annual

### Example: annual BCBS 239 risk-data attestation pack from the Head of Risk Reporting

Public-source-derived. No named institution. Framing patterns from BCBS 239 Principle 1 (governance), the BCBS Progress Reports, and the firm's most recent self-assessment (which is the upstream artifact produced by `bcbs239-gap-assessment`). Source-anchor verification flags carried forward per the source-anchors discipline.

#### Input

- Institution: top-tier US bank holding company with an intermediate holding company (IHC) under regulatory capital reporting. G-SIB-equivalent in scope of supervisory expectations on risk data aggregation and reporting.
- Engagement scope supplied: primary regulators FRB and OCC; persona = Head of Risk Reporting, second line, reporting to CRO; sector overlay = banking; cross-cutting overlays = none beyond the BCBS 239 baseline; source posture = public-plus-firm-policy-plus-evidence.
- Attestation period: prior calendar year. Annual cadence underpinning the risk-data confidence label in the Risk Committee pack and the regulatory-capital-reporting attestation chain.
- Upstream artifacts on file: most recent BCBS 239 self-assessment from `bcbs239-gap-assessment` (fourteen-principle assessment with three Top-5 priority gaps); the firm's risk-data control matrix (22 controls organised by principle group); data-quality framework reports for the period; reconciliation logs between source systems and the regulatory-reporting layer; data-lineage documentation; internal-audit reports on risk data; risk-data committee minutes for the period; prior-period attestation pack with two carried-forward exceptions.

#### Output sketch

The skill emits a markdown pack and a structured record. Headlines:

- **Cover** — attestation period, scope (top-tier BHC plus IHC; named systems: credit-loss data warehouse, market-risk source systems, operational-risk loss database, regulatory-reporting layer; legal-entity perimeter), attesting role = Head of Risk Reporting, attestation type = bcbs239-risk-data, assertion-language version 2.1, source posture, scope ID linked.
- **Executive summary** — five bullets in attesting role's voice. Headline: risk-data aggregation and reporting infrastructure operating effectively subject to three named exceptions; one Principle 6 (adaptability) gap, one Principle 2 (architecture) gap, one Principle 3 (accuracy) gap.
- **Scope statement** — names the legal-entity perimeter, the four in-scope source systems and the regulatory-reporting layer, the time period, and the exclusions (out-of-scope: pre-trade data quality at the broker-dealer subsidiary, addressed under a separate attestation chain).
- **Source criteria** — BCBS 239 (January 2013), Principles 1 to 14; the firm's risk-data policy v4.0; the firm's data-quality framework v3.2; the most recent BCBS 239 self-assessment.
- **Control inventory** — 22 controls from the upstream risk-data control matrix, organised by BCBS 239 principle group (overarching governance: Principles 1-2; aggregation: Principles 3-6; reporting: Principles 7-11; supervisory and remediation: Principles 12-14). Each row carries owner role, principle reference, design and operating effectiveness ratings, linked evidence IDs.
- **Evidence index** — 47 rows. Data-quality framework reports (quarterly); reconciliation logs between each source system and the regulatory-reporting layer (monthly); data-lineage documentation refreshed in the period; the most recent BCBS 239 self-assessment; internal-audit reports on risk data (two issued in the period); risk-data committee minutes (four entries); the regulatory-capital-reporting reconciliation evidence; CDO sign-off logs for material restatements. Each row names producer role, system of record, period covered, and linked control IDs.
- **Exceptions** — three open exceptions. Exception 1 (severity high, Principle 6 adaptability): ad-hoc stress aggregation capability is 5 business days versus an internal target of 48 hours; compensating control = pre-computed stress aggregations run weekly to reduce delay risk during a stress event, evidenced by the weekly aggregation logs; status = open, target remediation date next year, linked issue ID and linked to the gap-assessment Top-5 priority gap. Exception 2 (severity medium, Principle 2 architecture): manual reconciliation between two market-risk source systems persists; compensating control = daily reconciliation reviews with documented sign-off, evidenced by the sign-off log; status = open, target remediation date end of next year, linked issue ID. Exception 3 (severity medium, Principle 3 accuracy): operational-risk loss database carries a known understatement of small-event losses below the $50k threshold; compensating control = the threshold-based exclusion is explicit in committee-pack commentary so consumers calibrate accordingly; status = pending-review, investigation ongoing, linked issue ID.
- **Prior-period remediation status** — two prior-period exceptions. The Principle 4 (completeness) gap on counterparty-data scope was remediated; closure memo cited. The Principle 7 (accuracy of reporting) gap on regulatory-capital-report reconciliation timing is carried forward as Exception 2 above (the manual reconciliation was the root cause and has not been resolved).
- **Sub-certification chain** — the Head of Risk Reporting's sub-certification feeds the CDO sub-certification (data-quality side) and the CRO sub-certification (risk-reporting side); both feed the regulatory-capital-reporting attestation chain owned by the CFO function. Chain is named in `sub_certification_chain[]`.
- **Reviewer questions** — five questions anticipating internal-audit and FRB horizontal-review posture: whether the compensating control for Exception 1 actually mitigates the underlying gap; whether the manual reconciliation in Exception 2 has a credible automation path; whether the threshold exclusion in Exception 3 materially affects committee-pack interpretation; whether the data-lineage refresh covers the perimeter assessed; whether the CDO function has independence and resourcing to sustain the program.
- **Assertion text** — firm BCBS 239 risk-data attestation language, version 2.1, with the three named carve-outs surfaced in the qualification clause.
- **Sign-off block** — Head of Risk Reporting (signature blank), CDO (witness role on data-quality side, signature blank), CRO (witness role on risk-reporting side, signature blank), General Counsel (legal review role, signature blank). Date fields blank until signed.
- **Confidence label** — medium. Three open exceptions; full evidence-index coverage of the 22 in-scope controls supports medium rather than low. Not high because BCBS 239 known limitations are non-empty.

The pack stops at draft. The Head of Risk Reporting signs after the CDO and CRO review the carve-outs and after legal review.

#### Why this scenario matters

- Three named exceptions tied to specific BCBS 239 principles, with compensating controls evidenced or honestly labelled as pending. No clean attestation against an active self-assessment with priority gaps.
- The pack consumes the upstream `bcbs239-gap-assessment` output and feeds downstream consumers (the Risk Committee pack's data confidence label; the regulatory-capital-reporting attestation chain).
- Prior-period remediation status is explicit and traces a prior carry-forward to the current-period exception.
- Sub-certification chain shows the ladder explicitly; the Head of Risk Reporting sub-certifies, not the CFO.
- Confidence label is medium because BCBS 239 known limitations are non-empty; the label is the BCBS 239 voice, not a marketing decision.

#### Anchors

- BCBS 239, "Principles for effective risk data aggregation and risk reporting" (January 2013), Principle 1 (governance).
- BCBS Progress Reports on adoption (most recent thematic review applies; verify at pack-write time).
- COSO Internal Control — Integrated Framework (2013).
- OCC Heightened Standards (12 CFR Part 30 Appendix D), risk-data linkage.

See `references/source-anchors.md` for full citations and verification flags.

## vendor-management-annual

### Example: annual vendor-management attestation pack for a critical fraud-screening vendor

Public-source-derived. No named institution. Vendor named "Vendor V" only. Framing patterns from the U.S. interagency third-party risk management guidance (June 2023), AICPA SSAE 18 / SOC 2 management assertion, and the COSO 2013 Internal Control framework. Source-anchor verification flags carried forward per the source-anchors discipline.

#### Input

- Institution: large national bank, OCC-supervised, with a Heightened Standards-covered subsidiary; the attestation supports the firm's third-party reporting to the Risk Committee and feeds the OCC continuous-monitoring discussion.
- Engagement scope supplied: primary regulator OCC; persona = Head of Vendor Management, second line, reporting to Head of Operational Risk; sector overlay = banking; cross-cutting overlays = cyber (vendor-cyber posture is in scope), privacy (customer-data flow); source posture = public-plus-firm-policy-plus-evidence.
- Attestation period: prior calendar year. Annual cadence.
- Vendor V: critical third-party fraud-screening service used in real-time card-transaction screening. Service classified as critical under the firm's third-party criticality tiering.
- Upstream artifacts on file: third-party-risk control matrix (14 controls organised by lifecycle stage); the vendor's most recent SOC 2 Type II report; quarterly KRI reviews; ongoing-monitoring meeting minutes; contract amendments; exit-test record; financial-condition reviews; regulatory-watch updates; the firm's third-party-risk policy; prior-period attestation pack with three closed exceptions and one open at year-end.

#### Output sketch

The skill emits a markdown pack and a structured record. Headlines:

- **Cover** — attestation period, scope (Vendor V; real-time card-transaction fraud screening; integration points named; legal-entity perimeter), attesting role = Head of Vendor Management, attestation type = vendor-management, assertion-language version 4.2, source posture, scope ID linked.
- **Executive summary** — five bullets in attesting role's voice. Headline: vendor relationship operating effectively in all material respects subject to two named exceptions; one in active remediation, one pending architecture review next quarter.
- **Scope statement** — names the vendor (anonymised as "Vendor V"), the service, the system integration points (real-time API at the card-transaction-authorisation layer, batch reconciliation feed to fraud-data warehouse), the legal-entity perimeter (top-tier bank and subsidiary), and the time period.
- **Source criteria** — interagency third-party risk management guidance (June 2023); AICPA SSAE 18 AT-C 320 for the vendor SOC 2 reliance; firm third-party-risk policy v3.1; firm vendor-management framework v2.4.
- **Control inventory** — 14 controls from the upstream control matrix, organised by lifecycle stage (planning / due diligence / contract / ongoing monitoring / termination). Each row carries owner role, framework component, design and operating effectiveness ratings, linked evidence IDs, and linked exception IDs where relevant.
- **Evidence index** — 31 rows. Most recent SOC 2 Type II report (with carve-outs flagged); CUEC-evidence rows for each user-entity control the SOC report identifies; quarterly KRI reviews; contract amendments executed in the period; ongoing-monitoring meeting minutes (12 entries); exit-test record from the annual exercise; quarterly financial-condition reviews; regulatory-watch updates from the third-party-risk team. Each row names producer role, system of record, period covered, and linked control IDs.
- **Exceptions** — two open exceptions. Exception 1 (severity high): the most recent SOC 2 Type II carries a control gap on logical access reviews; compensating control = the firm's quarterly access-recertification overlay run by IAM, evidenced by the recertification logs in the system-of-record IAM tool, status = open, linked issue ID. Exception 2 (severity high): vendor outage in Q2 demonstrated insufficient resilience; compensating control narrative carries the dual-vendor architecture in-flight review, status = pending-review, target remediation date = end of Q3, linked issue ID. Both exceptions are reflected as a carve-out in the assertion text.
- **Prior-period remediation status** — three prior-period exceptions, all remediated; evidence pointers cite the closure memos in the issue-management system. One prior-period exception that was open at prior year-end (vendor financial-deterioration alert) is carried forward as remediated with the closure-memo evidence pointer.
- **Sub-certification chain** — the Head of Vendor Management's sub-certification feeds the Head of Operational Risk's roll-up sub-certification, which feeds the CRO's roll-up to the Risk Committee. The chain is named in `sub_certification_chain[]`.
- **Reviewer questions** — five questions anticipating OCC continuous-monitoring posture: dual-vendor architecture timeline, exit-plan testing cadence, contingency for sustained vendor outage, CUEC-control coverage of the SOC 2 carve-out, financial-condition trigger thresholds.
- **Assertion text** — firm vendor-management attestation language, version 4.2, with the two named carve-outs surfaced in the qualification clause.
- **Sign-off block** — Head of Vendor Management (signature blank), Head of Operational Risk (witness role, signature blank), General Counsel (legal review role, signature blank). Date fields blank until signed.
- **Confidence label** — medium. Two open exceptions with one in active remediation and one pending; full evidence-index coverage of in-scope controls supports medium rather than low.

The pack stops at draft. The attesting officer signs after legal review and after the Head of Operational Risk reviews the carve-outs.

#### Why this scenario matters

- Two open exceptions named with specifics rather than concealed in narrative. The qualified attestation reads cleanly to the OCC and the external assessor.
- SOC report is supplemented by CUEC-level evidence at the user firm, not taken at face value.
- Compensating controls are named and evidenced; the dual-vendor pending-review case is treated as `pending-review` not `remediated`.
- Sub-certification chain is explicit; the pack is the function-head sub-certification, not the executive certification.
- Confidence label is medium because exceptions are open; not "high" with carve-outs concealed.

#### Anchors

- Interagency third-party risk management guidance (June 2023), Section III.D ongoing monitoring.
- AICPA SSAE 18 / AT-C 320 (SOC 1) and AT-C 105 / 205 (SOC 2).
- COSO Internal Control — Integrated Framework (2013).
- OCC Heightened Standards (12 CFR Part 30 Appendix D).

See `references/source-anchors.md` for full citations and verification flags.

## troubleshooting

### Troubleshooting: attestation-pack

Recurring failure modes when an attestation pack reads as complete but is not. Reviewer pass should catch these; builder pass should preempt them.

#### Clean attestation while material exceptions exist elsewhere

Symptom: the assertion text reads "controls operated effectively in all material respects" while the firm carries open MRAs, audit issues, or known control gaps in the same scope.

Why it happens: builder treats the assertion as a procedural close-out and the exceptions as a separate workstream tracked in the issue log.

Fix: where exceptions exist in scope, name them in the exceptions section, link to the relevant control, and reflect the carve-out in the assertion text. A clean attestation with material open issues elsewhere is a frequent supervisory finding and an external-auditor exception in its own right. The schema requires `exceptions[]` to enumerate every exception with severity and status; "no exceptions" is itself a stated determination.

#### Evidence index by reference

Symptom: evidence index says "all evidence is in the SharePoint folder" or "see audit binder". No itemised list, no system of record, no period covered.

Why it happens: the attesting role works against a binder that lives somewhere else and points to it rather than itemising.

Fix: one row per piece of evidence. Each row carries description, evidence type, system of record, period covered, producer role, and linked control IDs. An external assessor cannot accept "see folder" as the evidence index; the pack draft enforces the row-level discipline up front so the binder is built right rather than reconstructed later.

#### Compensating-control hand-waving

Symptom: an exception narrative includes "compensated by management oversight" or "covered by quarterly review". No discrete control named, no evidence pointer.

Why it happens: builder accepts the narrative the control owner provided without pressing for the compensating control's identity.

Fix: where an exception has a compensating control, the compensating control is a named row in the control inventory with its own evidence and own owner role. The schema's `compensating_control_description` is rejected if it does not name a discrete control. A compensating control without evidence in the same period is no compensating control at all.

#### Stale assertion language

Symptom: the assertion text is the prior-period text rolled forward. The version field reads the same as the prior period. The underlying source criteria have been updated (PCAOB AS revision, SSAE update, BCBS 239 supervisory expectation update, NYDFS Part 500 amendment) and the text does not reflect it.

Why it happens: assertion text is treated as boilerplate; the year-over-year change check happens after sign-off, not before.

Fix: every cycle, check the source criteria for changes since the prior assertion-text version. If criteria have updated, the text updates and the version increments. The skill's source-anchors discipline carries the verification flags; the year-over-year check is part of the workflow, not a post-sign-off catch.

#### Process-owner sub-certification confused with executive certification

Symptom: a process-owner sub-certification pack reads as if it is the CEO/CFO certification under the executive-certification provisions. Securities counsel is named as the signing role; the assertion text borrows from the executive certification.

Why it happens: builder collapses the two layers; "attestation" reads as a single artifact.

Fix: this skill produces process-owner and function-head sub-certifications that ladder up to the executive certification. The executive certification under the relevant securities-law sections is securities-counsel-led work and out of scope. The sub-certification chain captures the ladder explicitly via `sub_certification_chain[]`. Where the engagement is the executive certification itself, route to securities counsel and stop.

#### Vendor SOC report taken at face value

Symptom: evidence index cites "Vendor V SOC 2 Type II report" against a control. No carve-out review noted, no complementary user entity controls (CUECs) listed, no CUEC-level evidence at the user firm.

Why it happens: builder treats the SOC report as evidence of the firm's controls when it is evidence of the service organisation's controls.

Fix: a SOC report is the service organisation's management assertion. Where it is cited, the user firm reviews carve-outs, identifies the CUECs, and provides CUEC-level evidence at the user firm. The schema's `evidence_type` includes `cuec-evidence` distinct from `soc-report`; both rows should appear when a SOC report is cited as evidence for an in-scope control.

#### Prior-period remediation skipped

Symptom: prior-period exceptions appear in the prior period's pack and disappear from the current period's pack, with no remediation status.

Why it happens: each cycle starts fresh; the prior-period log is treated as historical.

Fix: every prior-period exception carries a current-status row in `prior_period_remediation_status[]`. Items not remediated by the current attestation date are reportable and surface as current-period exceptions. The schema enforces the linkage via `current_period_exception_id` when a prior item rolls forward.

#### Confidence-label inflation

Symptom: confidence label reads "high" while in-scope controls have missing evidence rows or are marked `not-tested`.

Why it happens: label is treated as a brand statement on the substantive control posture.

Fix: the label reflects the strength of the evidence base, not the substantive control posture. `high` requires complete evidence-index coverage. Where evidence is missing on any in-scope control, the label drops to medium at best. The schema-level check is documented; the workflow enforces it.

#### Sector or cross-cutting overlay loaded but ignored

Symptom: insurance overlay loaded but no NAIC Model Audit Rule mapping in the pack; cyber overlay loaded but no CISO-program attestation slot; privacy overlay loaded but no Safeguards Rule annual-report linkage.

Why it happens: overlay treated as background reading rather than content that lands in the pack.

Fix: when the scope names an overlay, the matching content lands as named items in the pack (a section, an exception type, an evidence-row category, a sign-off question). Overlay-specific assertion language and sign-off questions go to the reviewer-question list.

#### Pack stops too late

Symptom: the skill produces and "files" the attestation, marks it as signed, asserts the attesting role's sign-off without evidence.

Why it happens: builder over-runs the human-review gate.

Fix: the pack is a draft until the attesting officer signs and the named legal or audit reviewer reviews. The skill stops at the draft, surfaces the reviewer-question list, and leaves the signature fields blank. It does not assert sign-off, distribute, or post to the certification system.
