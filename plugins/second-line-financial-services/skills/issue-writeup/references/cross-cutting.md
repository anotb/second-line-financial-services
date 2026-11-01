# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Conduct cross-cutting overlay — issue-writeup

Loads when the scope `cross_cutting_overlay_set` includes `conduct`. The overlay shapes the criteria block, the severity calibration, and the closure-evidence framing for issues whose underlying condition involves customer-facing harm, sales-practice deficiencies, market-conduct exposure, or culture-and-conduct-risk patterns.

#### Why the conduct overlay matters

Severity calibration shifts when customer harm is identifiable. A finding that the firm has a control gap in disclosure timeliness reads moderate at face value; the same finding with identifiable consumer harm (eroded customer benefit, restitution-eligible scope, repeated pattern) reads high or critical. The conduct overlay carries the discipline that makes that severity shift defensible: it names the harm, scopes the harm, identifies the population, and frames closure evidence around restitution and pattern remediation rather than around process fix alone.

#### Source basis

- **CFPB UDAAP Examination Manual** — the unfair, deceptive, or abusive acts or practices framework. The manual's UDAAP module sets the criteria for unfairness (substantial injury not reasonably avoidable; not outweighed by benefits), deception (representation, omission, or practice that misleads a reasonable consumer; materiality), and abusive (interferes with a consumer's ability to understand or take action; takes unreasonable advantage).
- **CFPB Compliance Bulletins and Circulars** — published positions on UDAAP, fair lending, debt collection, mortgage servicing, deposit products, and other consumer-finance topics. CFPB Circulars are formal interpretive guidance that supervisors and enforcement teams apply.
- **FINRA Rule 2010** — standards of commercial honor and just and equitable principles of trade. The conduct framing for broker-dealer findings.
- **FINRA Rule 2111** — suitability rule (and Reg BI for accounts where Reg BI applies).
- **SEC EXAMS Risk Alerts on conduct** — published priorities on adviser fiduciary duty, suitability, churning, breach of fiduciary duty, fee transparency, and similar conduct-focused categories.
- **FCA Conduct Risk framework (UK reference)** — sometimes referenced in US firms with UK affiliates; the FCA's five conduct outcomes are a useful taxonomy but are not US-binding.
- **Reg E error-resolution and unauthorized-transfer rules** — consumer-conduct findings on electronic-fund-transfer disputes carry conduct-overlay severity.
- **State unfair-trade-practice statutes** — vary by state; multi-state replication of UDAAP findings frequently triggers state-level enforcement risk.
- **NAIC Market Regulation Handbook** — for insurers, the market-conduct-finding convention covers sales practices, claims handling, advertising, and producer oversight.

#### What the overlay adds to the write-up

##### Criteria block additions

When the underlying condition involves customer-facing harm, the criteria block layers a conduct criterion onto the substantive criterion. Examples:

- A disclosure-control finding takes the substantive criterion from Reg Z or Reg E and the conduct criterion from CFPB UDAAP (deception or unfairness).
- A sales-practice finding at a broker-dealer takes the substantive criterion from FINRA Rule 3110 (supervision) and the conduct criterion from FINRA Rule 2010 and Rule 2111.
- A claims-handling finding at an insurer takes the substantive criterion from the state insurance code's claims-handling-timeliness section and the conduct criterion from the NAIC Market Regulation Handbook's claims module.

##### Harm-identification block

Conduct-tagged issues carry a distinct harm-identification block within the effect / impact section. The block names:
- **Population affected**: number of customers, customer segments, geographic distribution, time window.
- **Harm pattern**: financial (overcharge, missed credit, inappropriate fee), operational (denied service, delayed service, inappropriate adverse action), informational (disclosure deficiency, misleading communication), or relational (cancellation hurdle, dispute-resolution-friction).
- **Restitution scope**: dollars at stake, methodology for the calculation, third-party administrator (where applicable), and the consumer-notification path.
- **Pattern indicator**: whether the harm is one-off, intermittent, recurring, or systemic.

##### Severity calibration

Conduct severity calibration leans on (1) consumer-harm scope, (2) population size, (3) pattern indicator, (4) reasonably-avoidable test, and (5) regulatory-priority alignment.

- **Identifiable systemic harm with restitution-eligible scope**: severity is critical or high.
- **Identifiable harm with limited population**: severity is high or moderate depending on the pattern indicator.
- **Disclosure or process deficiency without identified harm**: severity is moderate or low; the rationale notes that absence of identified harm does not foreclose harm and the firm's continuous-monitoring stance addresses the residual.
- **Cultural-pattern findings**: where multiple findings together suggest a culture-and-conduct-risk pattern (e.g., repeated UDAAP findings across product lines, repeated supervisory findings on sales-practice oversight), the issue write-up notes the pattern severity in the rationale even when the individual finding is moderate. The pattern dimension matters for fair-lending and CMS-program-effectiveness reviews.

##### Closure-evidence framing

Conduct-tagged closure evidence emphasises restitution and pattern remediation, not just process fix. Examples:
- **Restitution-eligible findings**: closure evidence names the restitution program (consumer-notification process, dollar amount per consumer, third-party administrator engagement, completion attestation), the look-back scope (period covered, methodology), and the consumer-notification template approval.
- **Pattern findings**: closure evidence names the pattern-remediation actions across the product or function, not just the immediate finding's fix. Cultural-pattern remediation typically runs longer than process-fix remediation.
- **Disclosure findings**: closure evidence names the corrected disclosure, the consumer-impact assessment for affected past disclosures, and the disclosure-review-control redesign that prevents recurrence.

##### Reasonably-avoidable test for unfairness

When the criteria block cites UDAAP unfairness, the reasonably-avoidable test is part of the analysis. The cause field on an unfairness finding ties to whether the consumer could have reasonably avoided the injury (typically not, when the firm controls the disclosure or process), whether the injury is outweighed by benefits to consumers or competition (typically the burden falls on the firm to evidence), and whether substantial injury is involved.

#### Common patterns and pitfalls

- **Severity deflation when no harm yet identified**. A finding without identified harm is not the same as a finding with no harm; the overlay's discipline is to name the population, scope the look-back, and only conclude no-harm after the look-back is evidenced.
- **Treating UDAAP as a catchall**. UDAAP applies to specific circumstances; the criteria block must specify whether the finding is unfairness, deception, or abusive, with the test elements.
- **Conflating fair-lending with UDAAP**. Fair-lending findings (ECOA, Fair Housing Act, HMDA) have a distinct framework from UDAAP; they often co-occur. The criteria block separates them.
- **Pattern blindness**. A single moderate finding that is the third in a series of UDAAP findings carries different severity than a first-time finding. The severity rationale should reference the prior findings; the firm's GRC platform's issue-history field is the source.
- **Compensating-controls argument for harm**. A compensating control reduces the residual risk; it does not unwind identified harm. Restitution and consumer-notification stay in the closure evidence even when a compensating control is in place going forward.

#### Joint-ownership patterns

Conduct-tagged issues often carry joint ownership between the substantive control owner and the consumer-compliance / fair-lending function (the CCO or Head of Compliance for UDAAP findings, the Fair Lending Officer for ECOA findings, the BSA Officer for AML / sanctions findings that carry consumer-impact). The owner field names the primary owner; the recommendation or remediation block names the joint owner.

#### Anchors used by this overlay

- CFPB Examination Manual, UDAAP module. https://www.consumerfinance.gov/compliance/supervision-examinations/
- CFPB Compliance Bulletins and Circulars. https://www.consumerfinance.gov/compliance/circulars/
- FINRA Rule Book, Conduct Rules (Series 2000). https://www.finra.org/rules-guidance/rulebooks/finra-rules
  - Rule 2010 (Standards of Commercial Honor and Just and Equitable Principles of Trade)
  - Rule 2111 (Suitability)
  - Rule 2210 (Communications with the Public)
- 17 CFR §240.15l-1 (Regulation Best Interest) and 17 CFR §275.211 (Investment Adviser fiduciary-duty interpretation).
- 12 CFR Part 1005 (Reg E) error-resolution and unauthorized-transfer rules.
- 12 CFR Part 1026 (Reg Z) closed-end credit and credit-card rules.
- 12 CFR Part 1002 (Reg B / ECOA) for fair-lending findings that intersect with conduct.
- NAIC Market Regulation Handbook, claims-handling and sales-practice modules. https://content.naic.org/cmte_d_mar.htm [verify current edition section labels.]
- State unfair-trade-practice statutes — vary by state; firm-overlay names the state-specific anchors.
- FCA Conduct Risk framework (UK reference; not US-binding but useful taxonomy). https://www.fca.org.uk/firms/culture-and-governance

## cyber

### Cyber cross-cutting overlay — issue-writeup

Loads when the scope `cross_cutting_overlay_set` includes `cyber`. The overlay shapes the criteria block, the severity calibration, and the closure-evidence framing for issues whose underlying condition touches information-security controls, customer-data exposure, or third-party-provided technology services.

#### Why cyber belongs in most issue write-ups

Most issues that surface in second-line work touch information systems somewhere: a vendor SOC report covers logical-access controls, a model-risk finding touches inference-endpoint security, a risk-data finding covers data-protection in the warehouse, a complaint-handling finding covers data-handling in the intake system. Cyber issues are rarely standalone; they layer onto the substantive issue with cyber-specific criteria, severity weight, and closure-evidence patterns. The overlay is consultative, it does not duplicate the firm's CISO-owned cybersecurity issue log; it adds the cyber-specific framing that an examiner reading the issue will look for.

#### Source basis

- **NYDFS 23 NYCRR Part 500** — Cybersecurity Requirements for Financial Services Companies. November 2023 amendment introduced new tiering (Class A companies, covered entities, small businesses) and tighter incident-notice requirements. Operative for NYDFS-licensed entities.
- **FFIEC IT Examination Handbook** — Information Security booklet (governance, logical security, change management) and the Audit booklet (IT-audit reportable conditions). FFIEC is the inter-agency convention for federal banking-agency-supervised firms.
- **SEC Cybersecurity Rules** — Form 8-K Item 1.05 (material cybersecurity incident disclosure, effective December 2023) and 17 CFR §229.106 (Reg S-K Item 106 cybersecurity risk management, strategy, and governance) for public registrants.
- **Reg S-P** — 17 CFR §248.30, customer-information safeguards for SEC-registered entities. The 2024 amendment introduced incident-response and customer-notification requirements with named timelines.
- **Reg S-ID** — 17 CFR §248.201 / §248.202, Identity Theft Red Flags rules.
- **GLBA Safeguards Rule** — 16 CFR Part 314 (FTC version for non-bank financial institutions; functional-regulator equivalents for banks).
- **NIST Cybersecurity Framework 2.0** (February 2024) — used as a control taxonomy; the cause field on a cyber-tagged issue often maps to a CSF function (Govern, Identify, Protect, Detect, Respond, Recover).
- **NIST SP 800-53 Rev. 5** — security and privacy controls for information systems; granular control statements where the firm anchors on it.
- **CISA cross-sector cybersecurity performance goals (CPGs)** — voluntary baseline; sometimes referenced in supervisor expectations for critical-infrastructure entities.

#### What the overlay adds to the write-up

##### Criteria block additions

When the underlying condition touches information-security controls, the criteria block layers a cyber criterion onto the substantive criterion. Examples:

- A vendor SOC 2 qualified-opinion finding on logical access takes the substantive criterion from the Interagency Third-Party Guidance §III.D and the cyber criterion from NYDFS §500.11(a).
- A risk-data finding on data-warehouse access controls takes the substantive criterion from BCBS 239 (where applicable) and the cyber criterion from FFIEC IT IS Booklet §II.C.7 (logical security).
- A complaint-handling finding on data-handling in the intake system takes the substantive criterion from CFPB CMS guidance and the cyber criterion from GLBA Safeguards Rule §314.4 (the FTC version) or the functional-regulator equivalent.

##### Cyber-disclosure-process findings (public registrants)

For SEC public registrants, findings on the cyber-disclosure process itself are a distinct category. The criteria block cites Reg S-K Item 106 (annual disclosure on cybersecurity risk management, strategy, and governance) and Form 8-K Item 1.05 (material-incident disclosure within 4 business days of materiality determination). The cause field for these findings ties to the specific control attribute on the disclosure process: the materiality-determination control (who decides, against what threshold, with what documentation), the 8-K filing-timing control, the Reg S-K Item 106 annual-disclosure control. Severity calibration for cyber-disclosure-process findings is typically high because the SEC has prioritised cyber-disclosure enforcement.

##### Incident-notice readiness findings

Incident-notice readiness is a control, not an event. A finding that the firm's incident-notice readiness is impaired carries criteria from NYDFS §500.17 (72-hour notice for material cybersecurity events), Reg S-P amended customer-notification timing, SEC 8-K Item 1.05 (4-business-day disclosure for public-registrant material incidents), the GLBA Safeguards Rule's customer-notification provisions, and state breach-notification statutes (which vary by state). The closure evidence for incident-notice readiness findings includes:
- Documented materiality-determination workflow with named approver.
- Notification template library covering each applicable jurisdiction and regulator.
- Tabletop exercise evidence with named participants and lessons-learned tracking.
- Dispatch-path readiness across regulator portals, customer-channels, and counterparty channels.

##### Severity calibration

Cyber severity calibration overlays on the substantive severity calibration. Specific weights:
- **Identifiable customer-data exposure**: severity is critical or high. The exposure scope (number of records, sensitivity of records) drives the calibration.
- **Privileged-access control gaps**: severity is high or critical depending on the systems in scope and the duration of the gap.
- **Logging or detection gaps**: severity is high or moderate; logging gaps are foundational because they impair the firm's ability to surface other findings.
- **Patch-management or vulnerability-management gaps**: severity ties to the vulnerability's CVSS score, the exposure window, and whether active exploitation is observed.
- **Third-party cyber gaps**: severity ties to the third party's criticality and the data scope.
- **Encryption-at-rest or in-transit gaps**: severity is high; the GLBA Safeguards Rule and NYDFS §500.15 set explicit expectations.
- **MFA gaps for privileged access**: severity is high; NYDFS §500.12 and the GLBA Safeguards Rule make MFA explicit.

##### Closure-evidence patterns

Cyber-tagged closure evidence reads as the artifact and runs at higher specificity than substantive closure evidence. Examples:
- "Privileged-access roster review evidence retained in IAM system audit log; sign-off by CISO and Head of [function]" rather than "privileged access reviewed".
- "Vulnerability-management dashboard exports for two consecutive monthly cycles, with critical-vulnerability dwell-time below firm SLA, retained in security-operations record" rather than "vulnerability management improved".
- "Tabletop exercise after-action report with named participants, identified gaps, and remediation tracking, retained in incident-response repository" rather than "tabletop exercise performed".

##### CISO joint-ownership pattern

Cyber-tagged issues often carry joint ownership between the CISO function and the substantive control owner (the Head of Vendor Management for vendor cyber issues, the Head of Model Risk for model-cyber issues, the Head of Operational Resilience for incident-response issues). The owner field names the primary owner; the issue write-up names the joint owner explicitly in the recommendation or remediation block.

#### Common patterns and pitfalls

- **Treating SOC 2 as universal third-party assurance**. A SOC 2 Type II covers what the auditor scoped; the issue write-up notes the scope of the SOC report and the gaps the firm covers via direct due diligence. A finding that references "the vendor has a SOC 2" without citing the specific Trust Services Criterion misses the actual control attribute.
- **Burying the cyber-disclosure process for public registrants**. For SEC public registrants, materiality-determination is itself a control. An issue that lists technical findings but does not address the disclosure-decision workflow misses the rows the SEC will probe after a material incident.
- **Conflating breach-notification statutes with regulatory-notification statutes**. State breach-notification statutes have distinct triggers, timelines, and content requirements from federal regulator-notification rules; a single finding can implicate both. The criteria block separates them.
- **Severity inflation on cyber issues**. Cyber issues attract reflexive critical or high severity; the rationale must be specific. A logging gap on a non-production system with no customer data is moderate, not critical, even though it is a cyber gap.

#### Anchors used by this overlay

- 23 NYCRR Part 500 — NYDFS Cybersecurity Requirements (post-November 2023 amendment).
  - §500.3 (cybersecurity policy)
  - §500.5 (penetration testing and vulnerability assessments)
  - §500.7 (privileged access)
  - §500.11 (third-party service-provider security policy)
  - §500.12 (multi-factor authentication)
  - §500.15 (encryption of nonpublic information)
  - §500.16 (incident response and business continuity)
  - §500.17 (notice of cybersecurity event; 72-hour reporting)
  https://www.dfs.ny.gov/industry_guidance/cybersecurity
- FFIEC IT Examination Handbook, Information Security booklet (September 2016). https://ithandbook.ffiec.gov/it-booklets/information-security/
- 17 CFR §229.106 — SEC Reg S-K Item 106 (cybersecurity disclosure).
- Form 8-K Item 1.05 — material cybersecurity incident disclosure (effective December 2023).
- 17 CFR §248.30 — Reg S-P (Safeguards Rule and 2024-amendment incident-response and notification).
- 17 CFR §248.201 / §248.202 — Reg S-ID (Identity Theft Red Flags).
- 16 CFR Part 314 — FTC Safeguards Rule (and functional-regulator equivalents for banks).
- NIST Cybersecurity Framework 2.0 (February 2024). https://www.nist.gov/cyberframework
- NIST SP 800-53 Rev. 5. https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final
- CISA Cross-Sector Cybersecurity Performance Goals. https://www.cisa.gov/cross-sector-cybersecurity-performance-goals
- State breach-notification statutes — vary by state; the firm-overlay names the statutes that apply to the institution's jurisdictional footprint.
