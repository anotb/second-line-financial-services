# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## crypto-payments-fintech

### Example: crypto-adjacent unusual-pattern alert at a payments fintech with sponsor bank

Public-source-derived. No named institution. The shape mirrors a SAR-decision QA pattern at a payments fintech operating under a sponsor-bank arrangement, where customer-funded card disbursements pass through to a virtual-currency on-ramp showing indicators consistent with sanctions-evasion typologies in published OFAC and FinCEN advisories.

#### Input

- **Institution**: a US payments fintech operating consumer prepaid card and account-funding services through a sponsor bank. The fintech runs first-line transaction monitoring; the sponsor bank carries ultimate SAR-filing responsibility under 31 CFR §1020.320 for activity in the bank's accounts. The fintech's BSA officer (designated under the sponsor-bank program agreement) drafts the SAR; the sponsor-bank BSA officer reviews and files. SAR-filing-responsibility allocation is documented in the program agreement.
- **Alert**: an unusual-pattern scenario fires on a consumer customer who, over a 60-day window, funds the prepaid card from multiple low-value sources and disburses the bulk to a virtual-currency on-ramp connected to addresses flagged in commercial blockchain analytics as associated with a mixer service. Aggregate $42k. Customer geography is consistent with US footprint; counterparty addresses show indicators consistent with the typology in FinCEN's advisories on convertible virtual currency [verify advisory dates] and OFAC's sanctions compliance guidance for the virtual currency industry [verify date].
- **Investigation file (closed by the fintech BSA program before QA, prior to sponsor-bank handoff)**:
  - Investigator pulled funding-source detail and on-ramp counterparty detail.
  - Blockchain-analytics report attached: addresses tagged as mixer-adjacent; one hop from a sanctions-listed address per the analytics tool [verify tool's underlying source attribution].
  - Customer-segment refresh review: customer is consumer-grade with no business activity claimed; activity is materially outside profile.
  - Sanctions screening: clear at the customer-name level; no direct match.
  - Negative-news search: clean.
  - Disposition: SAR drafted, recommended for filing; cyber-event structured fields populated; FinCEN convertible-virtual-currency advisory cited in narrative; OFAC virtual-currency guidance cited in narrative; tipping-off considerations noted at program level.
- **Engagement scope supplied**: institution = payments fintech with sponsor-bank arrangement; primary regulators = FinCEN (MSB), state money-transmitter regulators, sponsor bank's prudential regulator indirectly via the program; persona = second-line BSA QA reviewer at the fintech; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlay = payments-fintech; cross-cutting overlays = cyber.

#### Output sketch

The skill produces a QA memo against the SAR draft and decision file. Headlines:

- **Alert summary** — unusual-pattern scenario; aggregate $42k over 60 days; convertible-virtual-currency on-ramp counterparty with mixer indicators; one-hop analytics flag to a sanctions-listed address.
- **Customer and account context** — consumer customer; activity outside profile; no prior SAR history at customer level; segment refresh on file but pre-dates the activity.
- **Investigation steps performed** — six dated, attributed steps with evidence pointers (funding-source pull, on-ramp counterparty pull, blockchain-analytics report, segment review, sanctions screen, negative-news search).
- **Disposition** — `escalated_pending` from the fintech side; the sponsor bank's BSA officer holds the file decision under the program agreement. Filing window: well inside 30 days of detection given the escalation date.
- **Decision rationale** — typology cited as "sanctions evasion via convertible virtual currency"; FinCEN convertible-virtual-currency advisory cited and dated; OFAC virtual-currency-industry guidance cited and dated; narrative ties on-ramp counterparty indicators to the cited typology and to the analytics evidence; `narrative_coherence_label = coherent`.
- **Confidentiality posture** — tipping-off considerations noted at program level only; not assessed for this specific decision (the customer is in dispute over a card-funding hold and there is an active customer-service interaction). `tipping_off_risk_assessed = false` is the QA finding here.
- **Continuing activity posture** — first SAR draft for this customer; cadence not yet set because disposition is `escalated_pending`.
- **QA reviewer findings**:
  - `criterion = confidentiality-tipping-off`, severity material. Tipping-off assessment specific to this decision is not in the file despite an active customer-service interaction; the program-level tickbox does not satisfy the case-specific assessment expected under 31 USC §5318(g).
  - `criterion = advisory-citation`, severity observation. Advisories are cited and dated; OFAC guidance cited but the SAR draft does not flag the OFAC sanctions-evasion path explicitly to the sponsor bank's sanctions officer in the handoff package. The QA recommends adding the sanctions-officer cross-reference; this is a process-change recommendation, not a SAR-filing directive.
  - `criterion = structured-field-completeness`, severity minor. Cyber-event structured fields populated; the cyber-event-indicator subfields could be more specific than the templated language used.
- **Material gaps** — case-specific tipping-off assessment artifact; sanctions-officer cross-reference in the sponsor-bank handoff package; specificity in cyber-event-indicator subfields.
- **Recommendation** — `process_change_recommendation` (case-specific tipping-off assessment must be evidenced in fraud-recovery-overlap and dispute-overlap cases); `escalate_to_sar_review_committee` to consider the sponsor-bank handoff template change (sanctions-officer routing). Explicit note: the QA does not recommend whether to file, decline to file, amend, or supplement the SAR. The sponsor bank's BSA officer holds the file decision; the fintech's BSA officer holds the draft.
- **Source trace** — anchors to `references/source-anchors.md` (FFIEC SAR section, 31 USC §5318(g) confidentiality, FinCEN MSB rules at 31 CFR §1022.320, FinCEN convertible-virtual-currency advisories, OFAC sanctions compliance guidance for the virtual currency industry), `references/sector-overlays.md#payments-fintech` (sponsor-bank SAR-filing-responsibility allocation), `references/cross-cutting.md#cyber` (cyber-typology SAR considerations and sanctions-evasion via virtual currency).
- **Confidence label** — `high` for the QA findings on tipping-off and on the handoff-package gap; `medium` for the structured-field-specificity observation pending sponsor-bank review preference.

#### Why this scenario matters

- **Sponsor-bank SAR-filing responsibility allocation is the operative facts pattern at payments fintechs**. The QA must know which entity files and where the handoff happens, and route findings accordingly. The fintech's QA does not direct the sponsor bank's filing decision.
- **The cyber overlay engages even when the alert is routed through a transaction-monitoring scenario, not a cyber-event referral**. Sanctions-evasion via virtual currency is the dominant cyber-typology overlap, anchored to OFAC and FinCEN public guidance.
- **Case-specific tipping-off assessments are the most common confidentiality-posture gap** in fraud-recovery-overlap, dispute-overlap, EDD-overlap, and law-enforcement-liaison cases. Program-level tickboxes do not substitute.
- **Advisory-citation discipline matters in two directions**. Citing an apt advisory is the floor; citing inapt advisories for window-dressing is a separate finding. Date the advisory; treat dated guidance as evidence the typology citation rests on.
- **The recommendation set explicitly excludes the SAR-filing decision itself**. The QA can recommend escalation to the SAR review committee for process change; it cannot direct the SAR-filing decision for this alert.

#### Anchors

- FFIEC BSA/AML Examination Manual — Suspicious Activity Reporting section.
- 31 CFR §1020.320 — Reports by banks of suspicious transactions (sponsor bank's filing rule).
- 31 CFR §1022.320 — Reports by money services businesses of suspicious transactions [verify section].
- 31 USC §5318(g) — statutory SAR authority and confidentiality (case-specific tipping-off).
- FinCEN advisories on convertible virtual currency [verify advisory dates].
- OFAC Sanctions Compliance Guidance for the Virtual Currency Industry (October 15, 2021) [verify date].

See `references/source-anchors.md` for full citations.

## structuring-pattern-bank

### Example: structuring pattern at a community bank

Public-source-derived. No named institution. The shape mirrors a standing typology pattern at small and mid-sized community banks: a small-business customer making cash deposits structured to sit just below the $10,000 currency-transaction-report threshold across a short window and across more than one branch.

#### Input

- **Institution**: a community bank with a regional footprint and one supervisory regulator (FDIC or state DBI plus FRB depending on charter; assume FDIC for this example).
- **Alert**: a structuring-detection scenario fires after a small-business customer makes nine cash deposits, each between $9,000 and $9,800, within a rolling 14-day window across two branches. Aggregate $80k+; expected monthly cash activity per the customer's CDD profile is $25k.
- **Investigation file (closed by the BSA program before QA)**:
  - Investigator pulled transaction history for the customer and the two related-party signers on the account.
  - Branch-staff interview notes attached: customer was asked about the deposits, gave a generic explanation about supplier prepayments, no supporting invoices produced.
  - Negative-news search: clean.
  - Sanctions screening: clear.
  - Disposition: SAR filed; structured fields on the SAR form populated for "structuring"; narrative attached.
- **Engagement scope supplied**: institution = community bank; primary regulator = FDIC; persona = second-line BSA QA reviewer reporting to the BSA officer; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlay = banking; cross-cutting overlays = none for this alert.

#### Output sketch

The skill produces a QA memo against the alert decision file. Headlines:

- **Alert summary** — structuring scenario; aggregate $80k+ across nine deposits in 14 days; two branches; small-business customer with consumer-grade CDD profile.
- **Customer and account context** — small-business segment; CDD on file is consumer-grade; expected monthly cash $25k vs observed $80k+ in two weeks; signers carry no prior SAR history at customer level.
- **Investigation steps performed** — five dated, attributed steps with evidence pointers (transaction pull, signer review, branch interview, negative-news, sanctions screen). Related-party search at the institution beyond the named signers is not evidenced in the file.
- **Disposition** — `filed`. Filing window: within 30 days of detection.
- **Decision rationale** — narrative cites "structuring" by name; structured fields on the SAR form populated; no FinCEN advisory referenced (none materially apt for vanilla structuring at this scale; observation, not finding).
- **Confidentiality posture** — `tipping_off_risk_assessed = true`; branch-staff training note in the file references customer-conversation script. Internal access controls on the SAR record: documented.
- **Continuing activity posture** — first SAR for this customer; 90-day continuing review scheduled with `next_review_due` populated. `review_cadence_status = current`.
- **QA reviewer findings**:
  - `criterion = related-party-search`, severity moderate. The investigator did not document a search for related-party accounts at the institution beyond the named signers; for a small-business customer, related-entity DBA accounts are a common adjacent vector. `finding_description` notes the gap; `evidence_pointer` cites the missing artifact.
  - `criterion = narrative-coherence`, severity minor. The narrative cites typology and is coherent against the timeline; the QA observation is that the narrative reads as templated rather than facts-specific. Observation, not finding.
- **Material gaps** — related-party search artifact missing; CDD-segment refresh is overdue per the firm's risk model (small-business activity has outgrown consumer-grade CDD). The CDD gap is flagged for cross-reference to the `cdd-risk-review` skill, not handled in this QA.
- **Recommendation** — `training_feedback` (related-party search documentation); `process_change_recommendation` (CDD-segment refresh trigger should fire on detected business-grade activity in a consumer-segmented account). Explicit note: the QA reviewer does not recommend SAR amendment, supplement, or any change to the filed SAR. The SAR is filed; the BSA officer and SAR review committee own any subsequent action on the filing itself.
- **Source trace** — anchors to `references/source-anchors.md` (FFIEC SAR section, 31 CFR §1020.320, 31 USC 5318(g) confidentiality, FFIEC continuing-activity expectation), `references/sector-overlays.md#banking` (bank-specific filing-window and continuing-review framing).
- **Confidence label** — `high` for the disposition QA; `medium` for the CDD cross-reference because the CDD review is happening separately.

#### Why this scenario matters

- **The QA tests decision quality, not the underlying SAR-file decision**. The SAR is filed. The QA finds a documentation gap and a CDD process gap. It does not say "the SAR should not have been filed" or "amend the SAR to add X". That separation is what the skill enforces.
- **Related-party search is the most common gap in structuring QA work** at community and mid-sized banks; the skill's `criterion = related-party-search` exists for this pattern.
- **Continuing-activity cadence shows up even on first SARs**: the 90-day continuing-review next-due date is part of the QA artifact, not just a finding triggered by an overdue review.
- **The boundary with `cdd-risk-review` is real**. The QA flags the CDD cross-reference but does not handle the CDD refresh itself; that is the other skill's job.
- **No FinCEN advisory citation for vanilla structuring**. The QA observation is that absence of an advisory citation is fine where no advisory is materially apt. Generic advisories cited for window-dressing are a different finding.

#### Anchors

- FFIEC BSA/AML Examination Manual — Suspicious Activity Reporting section.
- 31 CFR §1020.320 — Reports by banks of suspicious transactions.
- 31 USC §5318(g) — statutory SAR authority and confidentiality.
- FinCEN BSA E-Filing — current SAR form and instructions (filing-window posture).

See `references/source-anchors.md` for full citations.

## troubleshooting

### Troubleshooting: sar-decision-qa

Recurring pitfalls. Read before producing the QA artifact and again before sign-off.

#### Scope discipline

##### Drifting into the SAR-file decision

The QA produces findings, gaps, and recommendations against the decision file. It does not direct whether to file, decline, amend, supplement, or close the SAR. The named decisionmaker is the BSA officer (with the SAR review committee where the firm uses one). The skill outputs `recommendation`, not `decision`. A QA artifact that says "the SAR should not have been filed" or "amend the SAR to add X" has misread its scope.

##### Reviewing alert quality instead of decision quality

Whether the alert was a good alert (precision, recall, segmentation, threshold) belongs in `aml-model-monitoring`. Whether the decision file shows defensible work belongs here. The QA should not absorb model-monitoring work; cross-reference it instead.

##### Treating CDD or EDD posture as in-scope

Customer-segmentation and CDD-refresh work belongs in `cdd-risk-review`. EDD posture for high-risk customers belongs in `edd-escalation-pack`. The SAR-decision QA can flag a segment-mismatch finding (e.g., consumer-grade CDD on a customer showing small-business activity) and cross-reference; it does not handle the CDD refresh itself.

#### Evidence discipline

##### Free-text investigation paragraphs treated as steps

A free-text paragraph describing the investigation cannot be QA'd against the timeline. Each step needs a date, a performer role, and an evidence pointer. The structured `investigation_steps` field forces dated, attributed entries. Where the file is a paragraph, mark `investigation-completeness` and ask for the structured detail.

##### Negative-news and sanctions-screen searches stated without dates or sources

"Negative-news search: clean" with no date and no source-list is not evidenceable. The QA reads the search artifact (date, source list, search-term scope) or marks the gap.

##### Reading the structured-field SAR form completion as a green light

A SAR form with all required structured fields populated can still have templated narrative, generic typology language, missing advisory citation, and no case-specific tipping-off assessment. Structured-field completeness and decision-quality are separate criteria; the QA reads both.

#### Narrative discipline

##### Plain-language rationale without typology citation

A coherent, plain-language disposition rationale that does not name a typology and does not cite an apt FinCEN advisory passes the narrative-coherence test but fails the typology-citation and advisory-citation tests. The QA distinguishes the criteria.

##### Generic advisory citation as window-dressing

Citing a FinCEN advisory in narrative because the typology vaguely applies (without the indicators in the advisory matching the alert facts) is a separate finding from missing-citation. Date the advisory in the narrative; tie at least one named indicator from the advisory to the alert facts.

##### Templated narrative

A narrative that reads as a fill-in-the-blanks template scores `narrative_coherence_label = generic`. Coherent narratives reflect the specific facts, dates, and counterparties of the alert. Severity is a judgment call; templated narrative on a high-risk typology is more material than templated narrative on a routine structuring close.

#### Confidentiality discipline

##### Program-level tipping-off tickbox treated as case-specific assessment

The case-specific assessment under **31 USC §5318(g)(2)** is required where the decision intersects an active customer-service interaction (fraud-recovery, dispute, EDD-overlap, law-enforcement-liaison, cyber-insurance-claim). A program-level statement "tipping-off controls are in place" does not satisfy. Set `tipping_off_risk_assessed = true` only when the file evidences the case-specific work.

##### Need-to-know access control on the SAR record assumed rather than evidenced

The SAR record's internal access-control posture should be evidenced (system access log, named-role authorisations, exception register). Assumed posture is a `confidentiality-tipping-off` finding.

#### Continuing-activity discipline

##### Reviews documented only when a follow-on SAR is filed

Continuing-activity reviews concluding "no continuing activity" are still papered. A bank or fintech that papers reviews only when a follow-on SAR is filed leaves an evidence gap. The QA's `continuing_activity.last_continuing_review_date` and `next_review_due` apply regardless of outcome.

##### Continuing-activity cadence applied uniformly across all alerts

The 90-day cadence is the conventional supervisory expectation; the firm's program may set the cadence differently for routine versus high-risk typologies. The QA reads the program's cadence and the file against the program, not against an external default.

#### Sector-specific pitfalls

##### Applying the bank SAR rule to MSB or fintech activity

Bank SAR rule (`31 CFR §1020.320`) thresholds and posture are not the same as MSB SAR rule (`31 CFR §1022.320`) thresholds and posture. The QA scopes the operative rule before applying thresholds.

##### Applying the SAR rule to non-covered insurance products

`31 CFR §1025.320` covers permanent life with cash value, annuities, and other investment-type products. P&C, term life without cash value, group products, and health are generally outside scope. The QA scopes the product before applying the rule.

##### Treating an investment-adviser alert as in-scope of a stand-alone SAR rule

Until FinCEN's covered-investment-adviser SAR rulemaking is operative, advisers do not have a stand-alone SAR rule; the affiliated BD's program may carry the obligation. Track current state of the rulemaking on the date of analysis.

##### Importing FFIEC bank-flavoured frame to a BD or fund

The FFIEC manual SAR section informs but does not bind BDs and funds. SEC and FINRA examiners are the primary audience.

#### Cross-cutting pitfalls

##### Generic cyber-typology language when an apt advisory exists

"Cybercrime" or "cyber-fraud" in narrative when FinCEN has named the typology in an advisory (BEC, ransomware, convertible-virtual-currency sanctions evasion) is a `typology-citation` finding. Cite the advisory by name and date.

##### Templated cyber-event structured fields

The current FinCEN SAR form has cyber-event indicator fields. Templated populations score `structured-field-completeness` even when the fields are technically populated.

##### Missing sanctions-officer cross-reference on convertible-virtual-currency typologies

Sanctions-evasion via virtual currency is the dominant cyber-sanctions overlap. The SAR-decision file or the sponsor-bank handoff package must route to the sanctions function. Missing routing is a `process_change_recommendation` finding.

#### Output discipline

##### Citing without sections

Every regulator citation in the QA carries a section reference or a `[verify section]` placeholder. URL alone fails the source-anchor depth check. Use `references/source-anchors.md` for the canonical citation set; do not restate excerpts in the artifact body.

##### Marking unsupported claims silently

Use `[evidence needed]` explicitly. An inferred claim presented as evidenced is the failure mode.

##### Closing with too much certainty

The confidence label is `high` only when the source posture, the evidence set, and the QA criteria all line up. `medium` and `low` are normal for early-stage QA work; `unknown` is honest where the firm has not yet resourced the evidence ask. A `high` confidence label on a QA reviewing a decision file with material gaps is incoherent.
