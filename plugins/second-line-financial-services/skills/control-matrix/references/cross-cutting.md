# cross-cutting

One section per topic. Read only the sections the scope calls for.

## cyber

### Cyber cross-cutting overlay — control-matrix

Loads when the scope `cross_cutting_overlay_set` includes `cyber`. The overlay adds cyber-tagged rows to the matrix when the scoped process touches information systems, customer data, or third-party-provided technology services.

#### Why cyber belongs in nearly every matrix

Most processes the matrix scopes touch information systems somewhere: a credit-decisioning model lives on an inference endpoint, a vendor-monitoring process pulls SOC reports from a vendor portal, a board-pack process distributes via a document-management system, a complaint-handling process accepts intake via web and email. Cyber controls are not a separate matrix; they are tagged rows inside the substantive matrix, surfaced so an examiner reading the matrix can see where the cyber surface is and what mitigates it.

The overlay is consultative. It does not duplicate the firm's CISO-owned information-security risk assessment; it ensures the substantive matrix carries the cyber rows the examiner will look for in the context of this process.

#### Source basis

- **NYDFS 23 NYCRR Part 500** — Cybersecurity Requirements for Financial Services Companies. November 2023 amendment introduced new tiering (Class A companies, covered entities, small businesses) and tighter incident-notice requirements. Operative for NYDFS-licensed entities.
- **FFIEC IT Examination Handbook** — Information Security booklet (governance, logical security, change management) and the Cybersecurity Assessment Tool (where the firm uses it).
- **SEC cybersecurity rules** — 8-K Item 1.05 (material cybersecurity incident disclosure, effective December 2023) and Reg S-K Item 106 (cybersecurity risk management, strategy, and governance) for public registrants.
- **Reg S-P** — 17 CFR §248.30, customer-information safeguards for SEC-registered entities. The 2024 amendment introduced incident-response and customer-notification requirements.
- **Reg S-ID** — 17 CFR §248.201 / §248.202, Identity Theft Red Flags rules.
- **NIST Cybersecurity Framework 2.0** (February 2024) — used as a control taxonomy where the firm anchors on it.
- **NIST SP 800-53 control families** — used for granular control statements where the firm anchors on it; commonly via the FedRAMP-style profile when the firm operates federal-tied services.
- **CISA cross-sector cybersecurity performance goals** (CPGs) — voluntary baseline; sometimes referenced in supervisor expectations for critical-infrastructure entities.

#### What the cyber overlay adds to the matrix

##### Governance rows

- Cybersecurity policy approval and review (NYDFS §500.3 for covered entities).
- CISO appointment and reporting line (NYDFS §500.4).
- Board-level cybersecurity oversight (Reg S-K Item 106(c) for public registrants; NYDFS §500.4 for covered entities).
- Cybersecurity risk assessment cadence (NYDFS §500.9, NIST CSF 2.0 Govern function).

##### Identity and access rows

- Logical access controls (FFIEC IT IS booklet §II.C.7).
- Privileged-access management (NYDFS §500.7 for privileged accounts).
- Multi-factor authentication where required (NYDFS §500.12, GLBA Safeguards Rule).
- Access-review cadence and evidence (typically quarterly for privileged accounts; the matrix names the frequency).

##### Vulnerability and threat rows

- Vulnerability management program (NYDFS §500.5; FFIEC IT IS booklet).
- Penetration testing cadence and scope (NYDFS §500.5(a)(2), typically annual for covered entities; NIST CSF 2.0 Identify and Protect functions).
- Threat-intelligence consumption controls.
- Patch-management controls.

##### Incident-response and continuity rows

- Incident-response plan and tabletop-exercise evidence (NYDFS §500.16; FFIEC IT IS booklet).
- Business-continuity and disaster-recovery integration with cyber (NYDFS §500.16(b) post-amendment).
- Incident-notice readiness (NYDFS §500.17 — 72-hour notice to NYDFS for material cybersecurity events; SEC 8-K Item 1.05 — 4-business-day disclosure for public-registrant material incidents; Reg S-P amended customer-notification timing).
- Ransomware-specific controls and reporting (post-amendment NYDFS §500.17 ransomware-payment notice; CISA reporting where applicable).

##### Third-party-cyber rows

- Third-party service-provider security policy and ongoing assessment (NYDFS §500.11).
- SOC 2 Type II review controls for vendor SOC reports.
- Subservice-provider transparency controls (the SOC report's CSOCs).
- Vendor cyber-incident notification controls (contractual, with named timing).

##### Data-protection rows

- Encryption in transit and at rest (NYDFS §500.15 for nonpublic information).
- Data-loss prevention controls (DLP).
- Data-classification controls feeding the right protective controls to the right data.

##### Public-registrant disclosure-process rows

For SEC public registrants, the matrix carries rows for the cyber-disclosure process itself: materiality-determination control (who decides, against what threshold, with what documentation), 8-K filing-timing control (4 business days from materiality determination, with documented exceptions for national-security or law-enforcement deferral), and Reg S-K Item 106 annual disclosure controls (governance, risk management strategy, board oversight).

##### Operational-tech and AI-system rows (when in scope)

When the matrix scopes a process touching AI inference endpoints, the cyber overlay adds:
- Model-artefact integrity controls (signing, attestation).
- Model-serving-endpoint authentication and rate-limiting controls.
- Prompt-injection and adversarial-input detection (where the firm has the layer; absence is itself recordable).
- Tool-and-agent-privilege boundary controls (when the scoped process uses agentic AI).

#### Implications for matrix construction

- **Cyber-tagged rows carry a `control_type` honestly.** Preventive (access controls, encryption), detective (logging, anomaly detection, monitoring), response (incident-response runbook, notice-readiness), compensating (where a primary control is not yet in place but a secondary monitors for the gap).
- **Joint ownership is common and explicit.** Cyber-tagged rows for AI models name the CISO function and the model owner together; cyber-tagged rows for vendor controls name the CISO function and the head of TPRM together.
- **Incident-notice readiness is a control, not a fact.** A row that says "we will notify within 72 hours if we determine an event is reportable" is not yet a control; the row is a control when the materiality-determination workflow, the named approver, the notification template, and the dispatch path are all evidenced.
- **The CISO function is a reviewer or a co-owner, not the matrix author.** The matrix lives with the process owner; the CISO reviews cyber-tagged rows.

#### Common pitfalls in cyber-overlay matrices

- **Treating SOC 2 as universal third-party assurance.** A SOC 2 Type II covers what the auditor scoped; the matrix row notes the scope of the SOC report and the gaps the firm covers via direct due diligence.
- **Conflating the firm's NIST CSF 2.0 self-assessment with the matrix.** The CSF self-assessment is a posture artifact; the matrix is the obligation-anchored control inventory. They reference each other; they are not the same artifact.
- **Burying the cyber-disclosure process for public registrants.** Materiality-determination is itself a control. A matrix that lists technical controls but omits the disclosure-decision workflow misses the rows the SEC will probe after a material incident.
- **Vendor cyber-incident-notification controls without contractual anchor.** A control that says "vendor will notify us within X hours" is not a control unless the contract obligates the vendor and the firm has a process for receiving and acting on the notice.

#### Anchors used by this overlay

- 23 NYCRR Part 500 — NYDFS Cybersecurity Requirements (post-November 2023 amendment) [verify section labels for amended provisions].
- FFIEC IT Examination Handbook, Information Security booklet (September 2016) [verify currently posted edition].
- 17 CFR §229.106 — SEC Reg S-K Item 106 (cybersecurity risk management, strategy, and governance disclosure).
- Form 8-K Item 1.05 — material cybersecurity incident disclosure (effective December 2023).
- 17 CFR §248.30 — Reg S-P (Safeguards Rule and 2024-amendment incident-response and notification).
- 17 CFR §248.201 / §248.202 — Reg S-ID (Identity Theft Red Flags).
- 16 CFR Part 314 — FTC Safeguards Rule (for non-bank financial institutions); functional-regulator equivalents for banks.
- NIST Cybersecurity Framework 2.0 (February 2024).
- NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations.
- CISA Cross-Sector Cybersecurity Performance Goals.

## privacy

### Privacy cross-cutting overlay — control-matrix

Loads when the scope `cross_cutting_overlay_set` includes `privacy`, or when the scoped process touches consumer financial information, NPI, PHI, biometric data, or other regulated personal data. The overlay adds privacy-tagged rows to the substantive matrix.

#### Why privacy belongs in matrices that touch consumer data

Most consumer-facing financial-services processes touch nonpublic personal information (NPI). Account-opening collects NPI; servicing transmits it; complaint-handling stores it; AI inference may consume and emit it. The privacy-control surface is not separate from the substantive matrix; it is a set of tagged rows the matrix carries when the process meets the threshold.

The overlay does not duplicate the firm's privacy-program documentation (privacy notices, data-protection-impact assessments, records of processing activities). It ensures the substantive matrix carries the privacy rows the regulator will read against when probing this specific process.

#### Source basis

- **GLBA Safeguards Rule** — 16 CFR Part 314 (FTC) for non-bank financial institutions; functional-regulator equivalents for banks (interagency Safeguards rule). The 2021 amendment added specific control elements; the 2023 amendment added breach-notification requirements (effective May 2024).
- **GLBA Privacy Rule** — 16 CFR Part 313 (FTC); Regulation P (12 CFR Part 1016) for federal financial agencies.
- **Reg S-P** — 17 CFR §248.30 for SEC-registered entities; 2024 amendment introduced incident-response and customer-notification requirements.
- **HIPAA** — 45 CFR Parts 160 and 164. Operative when health-related data appears (group-life and disability claims, certain credit-disability products, employer-group health plans).
- **State comprehensive privacy laws** — California (CCPA/CPRA), Virginia (VCDPA), Colorado (CPA), Connecticut (CTDPA), Utah (UCPA), Texas (TDPSA), Oregon (OCPA), Florida (FDBR), Montana (MCDPA), and others as enacted. State laws differ on consumer-rights mechanics, sensitive-data handling, and enforcement; the matrix anchors on the binding state's law for the data subject in scope.
- **FCRA / FACTA** — 15 USC §1681 et seq.; FCRA Disposal Rule (16 CFR Part 682) and the Red Flags Rule (16 CFR §681.1) for consumer-report data.
- **NAIC Insurance Information and Privacy Protection Act (Model #672)** — operative for insurance-side processes.
- **CCPA / CPRA** — Cal. Civ. Code §1798.100 et seq., implementing regulations at 11 CCR §7000 et seq.; sensitive personal information rules and right-to-limit mechanics.
- **GDPR / UK GDPR** — Regulation (EU) 2016/679 and the UK 2018 Data Protection Act, when the firm processes EU/EEA or UK data subjects' data.

#### What the privacy overlay adds to the matrix

##### Notice-and-choice rows

- Initial-privacy-notice control (GLBA §503 / Reg P / 16 CFR §313.4): timing of the notice at relationship initiation, content alignment, recordkeeping.
- Annual-privacy-notice control where required (the FAST Act exception removed annual-notice obligations for some firms; the matrix names the firm's posture).
- Opt-out-of-sharing controls (GLBA §502; 16 CFR §313.7 — non-affiliated-third-party sharing opt-out; 16 CFR §313.8 — affiliate-sharing notice).
- State-law-specific notice controls (CCPA notice at collection, CCPA notice of right to opt out of sale or sharing).
- Sensitive-personal-information notice and right-to-limit (CCPA / CPRA §1798.121; Colorado, Connecticut, and Virginia have related but distinct mechanisms).

##### Safeguards-program rows (GLBA §314.4 element-level)

- Designate qualified individual responsible for the information security program.
- Risk assessment (periodic, written).
- Implementing access controls, encryption, MFA (the 2021 amendment specifies these elements).
- Procedures and policies for change management and audit logs.
- Service-provider oversight (contract clauses, periodic assessment).
- Incident-response plan (the 2021 amendment requires a written plan).
- Annual report to the board on the program (for non-bank financial institutions covered by the FTC rule above the customer-information threshold).

##### Consumer-rights-fulfilment rows (state laws and FCRA)

- Right-to-know / right-to-access fulfilment workflow (CCPA §1798.110, VCDPA §59.1-577).
- Right-to-delete fulfilment (CCPA §1798.105, plus state-specific carve-outs).
- Right-to-correct fulfilment (CCPA §1798.106, VCDPA §59.1-577.A.3).
- Right-to-opt-out-of-sale-and-sharing fulfilment (CCPA §1798.120 / §1798.135; the Global Privacy Control honoring obligation).
- Right-to-limit-use-of-sensitive-PI fulfilment (CCPA / CPRA §1798.121).
- Authentication-of-requestor controls.
- Service-provider direction controls (sub-contracting the request to the right service provider with the right cooperation obligation).
- FCRA disclosure-and-disposal controls (FACT Act file disclosure, 15 USC §1681g; disposal rule 16 CFR Part 682).
- Red Flags Identity-Theft Prevention Program controls (16 CFR §681.1).

##### Breach-notification rows

- Materiality-and-notice determination workflow (state breach-notification laws are now uniformly adopted; the matrix names the binding state(s) and the timing).
- GLBA Safeguards Rule notification (post-2023 amendment, effective May 2024): notice to FTC for unauthorized acquisition of unencrypted customer information of 500+ consumers, within 30 days of discovery.
- Reg S-P customer notification (post-2024 amendment): timing and content.
- HIPAA Breach Notification Rule (45 CFR §§164.400-414): individual, HHS, and (for breaches of 500+ residents) media notification within 60 days.
- State-law notification timing (varies; 30 to 90 days is common, with some states tighter; the matrix names the binding state).

##### Recordkeeping and retention rows

- GLBA-aligned record retention.
- HIPAA documentation retention (six years from creation or last use, 45 CFR §164.530(j)(2)).
- State-specific retention (varies by data category and by state).
- Data-minimisation and storage-limitation controls (CCPA §1798.100(c) — collection-purpose limitation; GDPR Article 5(1)(c) and (e) for EU/EEA processing).

#### Implications for matrix construction

- **Sensitivity classification is a row attribute.** A privacy-tagged row references the data classification of the data the control protects (NPI, PHI, sensitive-PI, biometric, financial-account, etc.). Default-to-internal classification on data that is plainly NPI is not honest.
- **Notice-and-choice controls are operating-effectiveness-tested by sample.** The matrix's evidence pointer for notice controls names the sample (recent account-opening files, recent notice-distribution log) rather than the policy that says "we will provide a notice."
- **Joint ownership with the privacy office is common.** Privacy-tagged rows for consumer-rights fulfilment typically name the operational owner (the function that processes the request) and the privacy officer (responsible for the program).
- **Service-provider rows are bidirectional.** When the firm shares NPI with a service provider for a covered processing activity, the firm carries oversight controls; when the firm receives NPI from a controller as a service provider (or processor), the firm carries direction-respecting controls. The matrix names which side this firm is on for each row.

#### Common pitfalls in privacy-overlay matrices

- **Treating GLBA notice as a one-time control.** Notice obligations are continuing; relationship-initiation notice, change-of-policy notice, and (if the firm has not adopted the FAST Act exception) annual notice are separate operating events.
- **Ignoring the state-law layer.** A US-customer-facing matrix that anchors only on GLBA misses the CCPA / VCDPA / etc. layer that sits on top of GLBA for the same customer set. The matrix carries both layers where both apply.
- **Burying sensitive-PI handling.** Sensitive-PI obligations under state laws (CCPA's right-to-limit, Colorado's opt-in for sensitive data, Virginia's separate consent) require their own rows; bundling them under "general PI controls" misses the regulator-probable seams.
- **Missing the affiliate-sharing distinction.** Affiliate sharing is governed by §313.8 / FCRA §603(d)(2), not by the §313.7 third-party rules; the matrix distinguishes them.
- **Treating a vendor's privacy attestation as evidence the vendor's processing is compliant.** The attestation is a representation; the matrix's evidence pointer for vendor privacy controls is the vendor's actual processing artefacts (data-processing agreement, sub-processor list, recent audit reports), not the attestation alone.

#### Anchors used by this overlay

- 16 CFR Part 314 — FTC Safeguards Rule (post-2021 amendment; 2023 breach-notification amendment effective May 2024).
- 16 CFR Part 313 — FTC Privacy of Consumer Financial Information Rule.
- 12 CFR Part 1016 — Regulation P (federal financial agencies' privacy rule).
- 17 CFR §248.30 — Reg S-P (post-2024 amendment).
- 17 CFR §248.201 / §248.202 — Reg S-ID.
- 45 CFR Parts 160 and 164 — HIPAA Privacy, Security, and Breach Notification Rules.
- 15 USC §1681 et seq. — FCRA / FACTA; 16 CFR Part 682 (Disposal Rule); 16 CFR §681.1 (Red Flags Rule).
- Cal. Civ. Code §1798.100 et seq. — CCPA / CPRA; 11 CCR §7000 et seq. — implementing regulations.
- Va. Code §59.1-575 et seq. — VCDPA; analogous citations for other state comprehensive privacy laws as enacted.
- NAIC Insurance Information and Privacy Protection Act (Model #672) — insurance-side privacy.
- Regulation (EU) 2016/679 — GDPR; UK Data Protection Act 2018.
- State breach-notification statutes — verify per binding state.
