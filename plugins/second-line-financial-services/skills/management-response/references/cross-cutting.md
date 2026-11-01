# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Conduct cross-cutting overlay for management-response

When the scope record flags `conduct` for a management-response engagement, this overlay sets conduct-specific evidence-of-effectiveness expectations and the customer-remediation strand for findings touching customer-conduct controls, fair-lending controls, retail-investor-protection controls, and unfair-deceptive-acts-or-practices.

Loaded by: `management-response/SKILL.md` when `scope.cross_cutting_overlay_set` includes `conduct`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- CFPB UDAAP authority under sections 1031 and 1036 of the Consumer Financial Protection Act (12 USC §§5531, 5536) and supervisory framework under 12 CFR Part 1090 (larger participants in defined markets) and the agency's general supervisory authority.
- Equal Credit Opportunity Act (Regulation B, 12 CFR Part 1002) and Fair Housing Act for fair-lending findings.
- Truth in Lending Act (Regulation Z, 12 CFR Part 1026), Real Estate Settlement Procedures Act (Regulation X, 12 CFR Part 1024), Fair Credit Reporting Act (Regulation V, 12 CFR Part 1022) and other consumer-protection regulations frequently cited in CFPB and federal banking agency conduct findings.
- FINRA Rule 2010 (Standards of Commercial Honor and Principles of Trade), FINRA Rule 2111 (Suitability), FINRA Rule 2210 (Communications with the Public), and SEC Regulation Best Interest (17 CFR §240.15l-1) for retail-investor-protection findings.
- State unfair-deceptive-acts-and-practices statutes (50-state landscape) and state attorney-general enforcement frameworks.
- FTC Act §5 (15 USC §45) authority for unfair or deceptive acts or practices, where the firm is in scope of FTC jurisdiction.

#### What changes for conduct-flagged management responses

##### 1. Customer-remediation strand

Conduct findings frequently turn on remediation the firm owes affected customers in addition to control redesign. The response carries the customer-remediation strand alongside the control strand:

- **Affected-population identification methodology** — how the firm identifies customers affected by the conduct (lookback period, criteria for inclusion, sampling vs full-population review, source-system queries used).
- **Restitution methodology** — what remediation is owed (refund of fees, interest adjustments, account-status corrections, credit-bureau corrections, reinstatement of products or services improperly denied or terminated).
- **Restitution delivery** — how restitution is delivered (account credit, check, electronic transfer, third-party administrator), the consumer-notice form, the timeline for completion.
- **Customer-remediation reporting** — how the firm reports completion to the supervisor, separately from control-redesign reporting; commonly periodic restitution-status reports with completion percentage and exception cases.

A conduct response with no customer-remediation strand on a finding where customers were affected reads as a defense of the control without acknowledgement of the harm; the supervisor will surface this gap.

##### 2. Evidence-of-effectiveness expectations

Conduct findings turn on whether the consumer-protection gap has been closed in customer outcomes, not just whether the policy or control was updated. The evidence-of-effectiveness plan section must distinguish:

- **Control-completion evidence** — the consumer-protection control is updated, training is delivered, attestations are collected.
- **Customer-outcome evidence** — the consumer-protection gap is closed in customer experience (complaint volume on the affected practice has reduced; outcome-testing or fair-lending statistical analysis shows the disparate impact has been addressed; mystery-shopping or sample testing shows the customer-facing process operates as designed).

The evidence-of-effectiveness method commonly used for conduct findings:

- **KRI trend** — two consecutive periods of GREEN on the relevant conduct KRI (complaint volume on the affected practice, fair-lending disparity ratio, suitability exception rate, communications-review exception rate).
- **Control test** — outcome testing or transactional sampling, with documented evidence of the consumer-facing process operating as designed and consumer harm not recurring.
- **External validation** — third-party review (commonly used for fair-lending findings where statistical analysis is required, or for consumer-product-design findings where independent assessment of the customer experience is appropriate).

##### 3. Fair-lending and disparate-impact analysis

For fair-lending findings (Regulation B, Fair Housing Act) and findings touching disparate-impact analysis, the response references:

- The firm's fair-lending statistical analysis methodology and any change committed.
- The protected-class analysis approach (race, ethnicity, sex, age, marital status, recipient of public assistance, exercise of consumer-protection rights).
- The remediation methodology where statistical analysis identified disparate impact or disparate treatment.
- The ongoing-monitoring approach post-remediation, typically including periodic statistical re-runs and exception-handling.

##### 4. Retail-investor-protection findings

For broker-dealer and investment-adviser findings on retail-investor protection (Regulation Best Interest, FINRA suitability rules, FINRA communications rules), the response references:

- Whether the finding affects the firm's Form CRS disclosures (Reg BI requires Form CRS for retail customers).
- Whether the finding affects the firm's care-obligation, disclosure-obligation, conflict-of-interest-obligation, or compliance-obligation under Reg BI.
- For FINRA suitability findings, whether the finding affects the reasonable-basis, customer-specific, or quantitative suitability obligations.

##### 5. Linkage to public-disclosure obligations

Conduct findings can give rise to public-disclosure obligations on the public-company parent (e.g., Form 10-K Item 103 legal proceedings; Form 8-K Item 8.01 other events; potential restatement implications where the finding affects financial-statement assertions). The response cross-links to the disclosure committee where applicable; the response does not make the disclosure decision.

##### 6. Cross-link to other capability skills

- Underlying issue write-up: `issue-writeup`.
- Standing committee pack: `risk-committee-pack` (issues-and-remediation-status section; conduct heat-map cell where the firm separately reports conduct).
- Privacy overlay where consumer-data handling is also implicated: `references/cross-cutting.md#privacy`.

#### Conduct-specific output additions

Added to the response (mapped to schema where present):

- `interim_mitigation` — conduct responses commonly carry the suspension of the affected practice as interim mitigation (e.g., "fee charge suspended pending remediation"; "product offering paused for affected segment"); the suspension is named with start date and sunset condition.
- `action_plan_milestones[]` — conduct responses commonly carry both control-redesign milestones and customer-remediation milestones; the schema accommodates both.
- `evidence_of_effectiveness_plan.evidence_method` — for conduct findings, commonly KRI-trend (complaint volume, exception rate) or control-test (outcome testing, transactional sampling).
- `linked_finding_ids` — conduct responses commonly cross-link to other consumer-protection findings sharing root cause (e.g., a customer-onboarding-system gap surfacing across multiple consumer-product findings).

#### Common pitfalls in conduct-flagged management responses

- Customer-remediation strand omitted on findings where customers were affected. The response must carry both strands; defense of the control without acknowledgement of harm reads poorly to consumer-protection supervisors.
- Affected-population identification methodology missing or unclear. The supervisor reads for whether the firm has identified the right population; vague language ("affected customers will be remediated") does not carry the response.
- Restitution methodology vague ("appropriate remediation will be provided"). The methodology must name what remediation is owed, how it is calculated, and how it is delivered.
- Evidence-of-effectiveness method limited to "training and policy updates". Conduct findings turn on customer outcomes; the evidence plan must address whether the customer experience has actually changed.
- Fair-lending statistical analysis methodology missing on Regulation B / Fair Housing Act findings. The response must reference the analytical methodology, not just the procedural change.
- Reg BI / FINRA suitability linkage missing on retail-investor-protection findings. The specific obligation should be named.
- Public-disclosure linkage missing on conduct findings with disclosure implications. The response cross-links to the disclosure committee referral status.

## cyber

### Cyber cross-cutting overlay for management-response

When the scope record flags `cyber` for a management-response engagement, this overlay sets the cyber-specific evidence-of-effectiveness expectations, the response-to-disclosure-process linkage, and the cyber-program reporting cadence.

Loaded by: `management-response/SKILL.md` when `scope.cross_cutting_overlay_set` includes `cyber`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- NYDFS 23 NYCRR Part 500, especially §500.04(b) (CISO report to senior governing body), §500.04(d) (board oversight), §500.17(a) (cybersecurity-event notification within 72 hours), and §500.17(b) (annual CISO certification, Form B). Current text reflects Second Amendment effective November 1, 2023, with phased compliance dates.
- SEC cyber disclosure rules: Regulation S-K Item 106 (cybersecurity risk management, strategy, and governance) for public-company issuers; Form 8-K Item 1.05 (material cybersecurity incident disclosure). Final rule July 2023; compliance dates phased.
- SEC Regulation S-P amendments (May 2024) for BDs, IAs, registered funds, and transfer agents: customer-information-safeguarding and breach-notice elements.
- Federal banking agencies' Computer-Security Incident Notification Rule (12 CFR 53 / 225 / 304), effective May 1, 2022, with the 36-hour notification clock running from determination of a notification incident.
- FFIEC IT Examination Handbook, Information Security and Cybersecurity sections.
- NIST Cybersecurity Framework 2.0 (February 2024) for governance and risk-management framing.

#### What changes for cyber-flagged management responses

##### 1. Evidence-of-effectiveness expectations

Cyber findings frequently turn on whether a control redesign has actually reduced the residual risk, not just whether the control was reissued. The evidence-of-effectiveness plan section must distinguish:

- **Control-completion evidence** — the redesigned control is in place (control documentation, change-management record, training-completion record).
- **Residual-risk-reduction evidence** — the redesigned control has actually reduced the underlying risk (KRI trend showing reduction in incident rate, mean-time-to-detect, mean-time-to-respond, or relevant cyber metric; control-test results showing the control operating as designed; threat-emulation or red-team results showing the control resists realistic attack patterns).

The evidence-of-effectiveness method commonly used for cyber findings:

- **KRI trend** — two consecutive quarters of GREEN on the relevant cyber KRI (phishing-click rate, MTTR, patch-cadence compliance, vulnerability remediation cycle).
- **Control test** — independent re-test by the firm's testing function or an external party, with documented evidence of the control operating as designed.
- **External validation** — third-party assessment (penetration test, red-team engagement, control attestation) by a qualified party post-remediation.
- **Supervisor walk-through** — for findings from a supervisor who routinely conducts walk-throughs (NYDFS, OCC IT examination, FRB IT examination), a post-remediation walk-through demonstrating the control in operation.

A cyber response with an evidence-of-effectiveness method limited to "training completed" or "policy updated" is a control-completion claim, not a residual-risk-reduction claim; the response template flags this gap.

##### 2. Linkage to event-notification clocks

For cyber findings where the underlying event also triggered a regulatory notification clock, the response carries explicit linkage to:

- NYDFS Part 500 §500.17 72-hour notification (where applicable; current text reflects post-Second-Amendment requirements).
- Federal banking agencies' Computer-Security Incident Notification Rule (12 CFR 53 / 225 / 304) 36-hour notification.
- SEC Form 8-K Item 1.05 4-business-day disclosure clock for material cybersecurity incidents on public-company issuers (verify current effectiveness and any post-adoption staff guidance at write time).
- SEC Regulation S-P 30-day customer notice for individuals reasonably likely to have been affected (verify compliance dates by entity type and size at write time).
- State breach-notification laws — 50-state landscape, varies by jurisdiction.

The response identifies which notifications were made, when, and where the response's action plan addresses any notification-process deficiencies the supervisor identified.

##### 3. Linkage to disclosure process

For cyber findings on public-company issuers where the underlying event may have triggered or may trigger Form 8-K Item 1.05 disclosure, the response cross-links to the disclosure committee referral and to `cyber-disclosure-readiness`. The response does not make the disclosure decision; the disclosure committee owns that. The response flags:

- Whether the underlying event was referred to the disclosure committee.
- The disclosure-committee outcome (disclosed under Item 1.05; not material; deferred pending further information).
- Whether the response's action plan addresses any disclosure-process deficiencies (e.g., a finding that the firm's materiality determination process did not run on the timeline the rule requires; a finding that disclosure controls and procedures did not surface the event to the disclosure committee in time).

##### 4. Linkage to CISO program reporting

For NYDFS-covered entities under §500.04(b), the management response links to the CISO's annual written report to the senior governing body. The response identifies:

- Whether the finding was surfaced in the most recent CISO report; if not, why not.
- Whether the next CISO report will reflect the remediation; the cadence of CISO reporting on the response progress.
- Whether the finding implicates the §500.17(b) Form B annual CISO certification (the CISO certifies compliance with Part 500); a finding identifying a Part 500 compliance gap may affect the next certification.

##### 5. AI-related cyber findings

For findings touching AI-related cyber risk (prompt-injection on GenAI deployments, model-supply-chain attack surface, AI-enabled social engineering), the response references:

- The firm's AI risk management framework (NIST AI RMF 1.0; NIST AI 600-1 GenAI Profile).
- The cross-link to the AI committee pack (`board-ai-risk-pack`) where the AI-related cyber posture is reported at enterprise level.
- For NY-licensed entities, the NYDFS Industry Letter on Cybersecurity Risks Arising from Artificial Intelligence (October 2024).

##### 6. Cross-link to other capability skills

- Cyber-disclosure decision and 8-K Item 1.05 trigger analysis: `cyber-disclosure-readiness`.
- Standing committee pack carrying the cyber slice: `risk-committee-pack` (cyber heat-map cell and material-events section).
- Vendor cyber findings: `concentration-risk-review`.
- AI-specific cyber findings: `board-ai-risk-pack`.

#### Cyber-specific output additions

Added to the response (mapped to schema where present):

- `evidence_of_effectiveness_plan.evidence_method` — for cyber findings, commonly KRI-trend or external-validation rather than control-test alone.
- `evidence_of_effectiveness_plan.evidence_period_post_remediation` — typically two consecutive quarters of GREEN on the relevant cyber KRI, or external validation by a named qualified party.
- `linked_finding_ids` — cyber responses commonly cross-link to disclosure-process referrals and to other cyber findings sharing root cause (e.g., shared identity-and-access-management gap surfacing across multiple cyber findings).
- `interim_mitigation` — cyber responses typically carry compensating controls in place pending full remediation (enhanced monitoring on affected systems; manual review of high-risk transactions; restricted access pending IAM redesign).

#### Common pitfalls in cyber-flagged management responses

- Evidence-of-effectiveness method limited to "training completed" or "policy updated". This is control-completion evidence, not residual-risk-reduction evidence. Cyber findings turn on whether the redesign actually reduced the risk; the evidence plan must reflect that.
- Disclosure-process referral status missing on findings touching events that may have triggered 8-K Item 1.05. The supervisor reads for whether the disclosure-process gate was respected; the response surfaces the referral status explicitly.
- Notification-clock linkage missing on findings where the underlying event triggered a regulatory notification. The supervisor reads for whether the firm's notification process performed as designed; the response surfaces the notification record.
- CISO-program linkage missing for NYDFS-covered entities. The §500.04(b) report and the §500.17(b) certification are the formal CISO-program touchpoints; findings should cross-link.
- AI-related cyber findings buried in general cyber response. For findings touching AI deployment, the response identifies the AI-specific element and cross-links to the firm's AI risk-management framework.
- SEC climate/cyber rule current effectiveness over-claimed. The SEC cyber disclosure rule final compliance dates are phased; verify by entity type and size at write time. Reg S-P amendments compliance dates are phased; verify at write time.

## privacy

### Privacy cross-cutting overlay for management-response

When the scope record flags `privacy` for a management-response engagement, this overlay sets privacy-specific evidence-of-effectiveness expectations and the linkage to customer-notification clocks for findings touching customer-information safeguarding, breach-notice procedures, and consumer-financial-data handling.

Loaded by: `management-response/SKILL.md` when `scope.cross_cutting_overlay_set` includes `privacy`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- Gramm-Leach-Bliley Act Safeguards Rule (FTC, 16 CFR Part 314), revised December 2021 with phased compliance dates including the June 2023 amendments adding the breach-notice provision (16 CFR §314.5).
- Regulation P (Privacy of Consumer Financial Information), 12 CFR Part 1016 (CFPB) and 12 CFR Part 332 (FDIC) and parallel federal banking agency rules.
- SEC Regulation S-P (17 CFR §248.30), as amended May 2024, with customer-information-safeguarding, breach-notice, and 30-day customer-notice requirements; phased compliance dates by registrant type and size.
- FTC Health Breach Notification Rule (16 CFR Part 318) for non-HIPAA-covered health-related entities including some fintech firms.
- State privacy laws including California Consumer Privacy Act / California Privacy Rights Act (CCPA / CPRA), and state breach-notification statutes (50-state landscape).
- HIPAA Privacy Rule, Security Rule, and Breach Notification Rule (45 CFR Parts 160, 162, 164) for HIPAA-covered entities (including some fintech firms operating in health-adjacent products).

#### What changes for privacy-flagged management responses

##### 1. Customer-notification clock reconciliation

Privacy findings frequently relate to events that also triggered customer-notification clocks. The response carries explicit linkage to:

- SEC Regulation S-P 30-day customer notice for individuals reasonably likely to have been affected (verify compliance dates by entity type and size at write time).
- GLBA Safeguards Rule notification provisions (16 CFR §314.5) requiring notification to the FTC within 30 days of discovery for security events involving the unauthorized acquisition of unencrypted customer information of 500 or more consumers.
- State breach-notification clocks (varies by state; many require notice "without unreasonable delay" or within specified day counts; some require simultaneous notice to state attorneys general or other state regulators).
- HIPAA Breach Notification Rule (60-day clock for HHS notice for breaches affecting fewer than 500 individuals; without unreasonable delay for breaches affecting 500 or more, plus media notice).

The action plan dates must reconcile with the customer-notification clock; a milestone for notice that lands after the regulatory clock has run is itself a finding the supervisor will surface.

##### 2. Customer-remediation strand

For privacy findings where customers were affected, the response carries the customer-remediation strand alongside the control-redesign strand:

- Customer-notification methodology (how the affected customer population is identified; what notice form is used; how notice is delivered).
- Customer-protection offerings (credit monitoring, identity-protection services, where applicable; the form, duration, and cost-to-firm).
- Customer-remediation reporting (how the firm reports customer-remediation completion to the supervisor, separately from control-redesign reporting).

##### 3. Evidence-of-effectiveness expectations

Privacy findings turn on whether the safeguarding gap has been closed, not just whether the policy was updated. The evidence-of-effectiveness plan section must distinguish:

- **Policy-completion evidence** — the safeguarding policy is updated, training is delivered, attestations are collected.
- **Control-effectiveness evidence** — the safeguarding control is operating as designed (access-review run with documented exception count and resolution; data-loss-prevention rule operating with documented detection-and-response evidence; vendor-information-handling attestation collected with documented evidence).

The evidence-of-effectiveness method commonly used for privacy findings:

- **Control test** — independent re-test by the firm's testing function, with documented evidence of the safeguarding control operating as designed.
- **KRI trend** — two consecutive periods of GREEN on the relevant privacy KRI (data-loss-prevention exception count, access-review exception count, vendor information-handling attestation completion).
- **External validation** — third-party assessment for higher-severity findings or where the supervisor specifies.

##### 4. Linkage to GLBA / Safeguards Rule program

For Safeguards Rule-covered entities, the management response links to:

- The qualified-individual designation (16 CFR §314.4(a)) and whether the finding implicates the qualified individual's program oversight.
- The risk-assessment requirement (16 CFR §314.4(b)) and whether the finding implicates the risk-assessment process or content.
- The continuous-monitoring requirement (16 CFR §314.4(c)) and whether the finding implicates monitoring effectiveness.
- The annual report to the board or governing body (16 CFR §314.4(i)) and whether the next report will reflect the remediation.

##### 5. Linkage to Reg P / Reg S-P privacy program

For Regulation P-covered entities (banks) and Regulation S-P-covered entities (BDs, IAs, registered funds, transfer agents), the response links to the privacy notice and the opt-out mechanism, where the finding implicates either.

##### 6. Cross-link to other capability skills

- Underlying issue write-up: `issue-writeup`.
- Standing committee pack: `risk-committee-pack`.
- Cyber overlay where the finding overlaps with cyber: `references/cross-cutting.md#cyber`.
- Conduct overlay where the finding overlaps with consumer conduct: `references/cross-cutting.md#conduct`.

#### Privacy-specific output additions

Added to the response (mapped to schema where present):

- `interim_mitigation` — privacy responses commonly carry the customer-notification step itself as an interim mitigation (where notification occurred before the full remediation was complete).
- `action_plan_milestones[].evidence_of_completion_expected` — for milestones touching customer notification, evidence is the notification log with delivery confirmation, not just the policy approval.
- `evidence_of_effectiveness_plan.evidence_method` — for privacy findings, commonly control-test or KRI-trend rather than external-validation alone (external validation is more commonly used for cyber).
- `linked_finding_ids` — privacy responses commonly cross-link to cyber findings on the same event and to consumer-conduct findings where the affected population is consumer-financial.

#### Common pitfalls in privacy-flagged management responses

- Action-plan dates that miss the customer-notification clock. The notification clock is set by statute or rule; the action plan must reconcile, with notice within the clock and the deeper remediation following.
- Customer-remediation strand omitted on findings where customers were affected. Privacy findings frequently turn on customer remediation; the response carries this strand alongside the control strand.
- Evidence-of-effectiveness method limited to "policy updated and training delivered". This is policy-completion evidence, not control-effectiveness evidence; the response must distinguish.
- GLBA / Safeguards Rule program linkage missing for Safeguards-covered entities. Findings should reference the qualified individual, the risk assessment, the continuous monitoring, and the annual report as applicable.
- Reg P / Reg S-P program linkage missing for entities subject to those rules. Privacy findings touching the privacy notice or opt-out mechanism should reference the rule.
- 50-state breach-notification landscape ignored. For events affecting consumers in multiple states, the response identifies the state-by-state notification posture, especially where state clocks differ from the federal clock.
