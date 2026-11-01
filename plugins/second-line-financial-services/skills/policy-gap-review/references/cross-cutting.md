# cross-cutting

One section per topic. Read only the sections the scope calls for.

## conduct

### Conduct cross-cutting overlay — policy-gap-review

Loads when the scope `cross_cutting_overlay_set` includes `conduct`. Binds the matrix to conduct-and-customer-facing-policy expectations when the policy in scope is a customer-facing policy: product approval, marketing review, complaints handling, fair lending, sales practice, fee design, or any policy whose operationalisation directly affects customers.

#### Why conduct loads

Customer-facing policies are the policies whose gaps get litigated, enforced, and surfaced in news cycles. The CFPB UDAAP standard applies at the policy-design level — a policy that produces unfair, deceptive, or abusive outcomes is itself UDAAP-deficient even when individual transactions are facially compliant. Fair-lending statutes (ECOA, FHA, HMDA-anchored disparate-impact theories) impose policy-level expectations beyond the transaction-level rules. Conduct findings drive larger remediation (customer restitution, monetary penalty, public consent order) than back-office findings; the gap matrix takes conduct seriously.

#### Source basis

##### CFPB UDAAP framework

- **CFPB UDAAP Examination Manual** (current edition). The chapter-level expectations on policies governing consumer-facing decisions, marketing review, fee disclosure, complaint response, and product approval. The unfair-deceptive-abusive standard applies at the policy-design level.
- **CFPB Bulletins and Circulars** that announce UDAAP positions on specific practices. Bulletin 2017-01 (auto loans), Bulletin 2018-01 (Hsbc consent on credit reporting), Circular 2022-02 (deceptive representations in mortgage marketing), Circular 2022-03 (adverse action notices for AI/algorithmic decisioning), Circular 2024-04 and successors. The matrix references the circulars in force at the engagement's effective date.
- **Dodd-Frank §1031 / §1036** — the statutory UDAAP authority that supplements FTC Act §5 unfair-deceptive standard for CFPB-jurisdictional providers.

##### Fair-lending statutes

- **ECOA / Reg B** — 12 CFR Part 1002. §1002.4 prohibition against discrimination on prohibited bases; §1002.6 evaluation of applications; §1002.9 adverse-action notice; Subpart B for §1071 small-business data collection (phase-in).
- **Fair Housing Act** — 42 USC §3601 et seq.; HUD's Discriminatory Effects rule (24 CFR Part 100, post-2023 reinstatement).
- **HMDA / Reg C** — 12 CFR Part 1003 — for fair-lending data accuracy and reporting policy expectations.
- **Disparate-impact theories** — recognised by the Supreme Court in Texas Department of Housing and Community Affairs v. Inclusive Communities Project (2015) under FHA; ECOA disparate-impact recognised by the federal banking agencies in interagency guidance.

##### Complaint-handling expectations

- **CFPB Compliance Management System guidance** — the consumer-complaint-response pillar.
- **OCC Bulletin 2020-94 / 2021-31** — bank complaint-handling expectations under the OCC's Consumer Compliance examination procedures.
- **State complaint-handling requirements** — state-by-state, e.g., NYDFS Insurance Regulation 64 Part 216.

##### Sales-practice and product-approval expectations

- **OCC Bulletin 2014-37** — Consumer Compliance: Bank Subjects.
- **FRB Consumer Compliance handbook** — current edition.
- **Sector-specific sales-practice rules** — Reg DD (deposits), Reg Z (credit-card account-opening disclosures), Reg E (prepaid disclosures), insurance suitability rules, broker-dealer best-interest rules (Reg BI under SEC Rule 15l-1).

##### Marketing-review expectations

- **CFPB UDAAP** — for any consumer-facing marketing.
- **Reg N** — 12 CFR Part 1014, the Mortgage Acts and Practices Rule.
- **Reg Z marketing rules** — for credit-card and HELOC marketing.
- **State consumer-protection acts** — including UDAP statutes that often parallel FTC Act §5 with state-specific extensions.
- **SEC Marketing Rule** (Rule 206(4)-1) — for adviser marketing where the policy in scope governs adviser-side marketing.
- **FINRA Rule 2210** — for broker-dealer communications with the public.

##### Fee-design and product-pricing

- **CFPB junk-fees focus** — circulars and bulletins addressing overdraft fees, NSF fees, surprise fees, return-deposited-item fees. The matrix references the circulars in force at the engagement's effective date.
- **Reg Z late-fee rules** — including the 2024 final rule on credit-card late fees (status subject to ongoing litigation; the matrix references the rule in force at the engagement's effective date).
- **Reg DD overdraft disclosure** — including the post-2010 Reg E §1005.17 opt-in for ATM and one-time debit overdraft.

#### Gap patterns the conduct overlay flags

##### UDAAP-design gaps

- Product-approval policies that lack a UDAAP review step before launch. Frequent gap site for fintech product policies and bank-fintech-program policies.
- Marketing-review policies that do not require UDAAP review of marketing materials, scripts, or social-media content.
- Fee-design policies that allow fee structures the CFPB has flagged as junk-fee-adjacent without an articulated business-justification framework.
- Complaint-handling policies that do not surface UDAAP-implicating complaint patterns to the policy-owner level for remediation.

##### Fair-lending policy gaps

- Adverse-action-notice content policy under Reg B §1002.9, where the policy does not require principal-reasons specificity at the rigor Reg B and Comment 9(b)(2)-3 of the Official Staff Commentary expect (frequent gap site for ML-decisioning policies).
- Prohibited-basis monitoring policy (testing, comparator-file analysis, exception-and-override review) where the policy is silent or generic.
- Disparate-impact assessment policy, where the policy is silent on the disparate-impact dimension.
- Section 1071 small-business data collection policy, where the firm meets the originations-volume threshold and the policy is silent or pre-rule.

##### Complaint-handling policy gaps

- Complaint-channel coverage policy (intake methods, response timing, escalation) where the policy is silent on a channel the firm operates (social media, app store reviews, executive-office complaints, regulator-forwarded complaints).
- Root-cause analysis and remediation-loop policy, where the policy treats complaints as a customer-service operation rather than as a feedback loop into product design.
- Complaint-data analytics and reporting policy, where the policy is silent on the analytics expected to surface UDAAP-implicating patterns.
- CFPB Complaint Database engagement policy, where the policy is silent on the firm's response timing and content.

##### Sales-practice and best-interest gaps

- Suitability policy (annuity, life, structured product) under the operative rule, where the policy lags the post-2020 best-interest amendments most states have adopted.
- Reg BI policy under Rule 15l-1 (broker-dealer best-interest), where the policy is silent on the four obligations (disclosure, care, conflicts of interest, compliance).
- Sales-incentive design policy, where compensation structures create UDAAP risk and the policy is silent on the incentive-design review.

##### Marketing-review gaps

- Algorithmic and AI-generated marketing content review policy, where the policy is silent on the review of GenAI-produced marketing copy.
- Influencer and third-party endorser policy, where the policy is silent on the FTC Endorsements Guides expectations.
- Cross-channel consistency policy, where the policy is silent on the obligation that disclosures present in one channel are not undone in another (the CFPB and FTC have repeatedly flagged this).

#### Implications for matrix construction

- **UDAAP gaps are usually `partial` or `weak`, rarely `missing`.** Most firms have product-approval, marketing-review, and complaint-handling policies; the question is whether they require the design-level UDAAP review the CFPB expects.
- **Fair-lending policy gaps surface as `partial` more often than `missing`.** The matrix is honest about the rigor gap rather than rating an existing-but-thin policy as covered.
- **Customer impact is a severity driver.** Severity rationale on conduct rows references the population the gap could harm and the harm pattern (financial loss, denial of credit, data exposure, deceptive impression).
- **Cross-policy interactions are common.** A product-approval policy gap interacts with the marketing-review policy and the sales-incentive-design policy; the matrix surfaces all three rather than fixing one in isolation.

#### Anchors used by this overlay

- CFPB UDAAP Examination Manual — current edition.
- CFPB Circulars and Bulletins on UDAAP positions — current at engagement effective date.
- Dodd-Frank §1031 / §1036 — 12 USC §5531 / §5536.
- 12 CFR Part 1002 — Regulation B (ECOA), including §1002.4, §1002.6, §1002.9, Subpart B (§1071).
- 12 CFR Part 1003 — Regulation C (HMDA).
- 42 USC §3601 et seq. — Fair Housing Act.
- 24 CFR Part 100 — HUD Discriminatory Effects rule.
- 12 CFR Part 1014 — Regulation N (MAP Rule).
- 12 CFR Part 1026 — Regulation Z, including credit-card marketing and 2024 late-fee rule [verify litigation status].
- 12 CFR Part 1030 — Regulation DD (Truth in Savings).
- 12 CFR Part 1005 — Regulation E, including §1005.17 overdraft opt-in.
- 17 CFR §240.15l-1 — SEC Reg BI.
- 17 CFR §275.206(4)-1 — Adviser Marketing Rule.
- FINRA Rule 2210 — Communications with the Public.
- OCC Bulletin 2014-37 / 2020-94 / 2021-31 — bank consumer compliance and complaint handling [verify operative bulletins].
- FTC Act §5 — 15 USC §45.

## cyber

### Cyber cross-cutting overlay — policy-gap-review

Loads when the scope `cross_cutting_overlay_set` includes `cyber`. The overlay binds the matrix to cybersecurity-policy expectations when the policy in scope is a cybersecurity policy, an information-security policy, or a substantive policy that includes a cybersecurity section (most material policies do).

#### Why cyber loads on most policy gap reviews

Most material firm policies touch information systems or customer data somewhere. A vendor-management policy carries cyber-tagged sections on third-party security; an MRM policy carries cyber-tagged sections on model-serving environment access; a consumer-deposit policy carries cyber-tagged sections on customer data protection; a board-pack policy carries cyber-tagged sections on distribution and DLP. The cyber overlay surfaces the cybersecurity-benchmark expectations the substantive policy needs to address.

The overlay is consultative. It does not duplicate the firm's CISO-owned information-security policy; it ensures the substantive policy carries the cybersecurity sections the supervisor will read.

#### Source basis for cyber-policy benchmarks

- **NYDFS 23 NYCRR Part 500** — Cybersecurity Requirements for Financial Services Companies. November 2023 amendment introduced new tiering (Class A companies, covered entities, small businesses) and tighter incident-notice requirements. The most prescriptive cybersecurity-policy-content rule in US financial-services regulation; §500.3 lists fifteen content elements the policy must address.
- **FFIEC IT Examination Handbook** — Information Security booklet (governance, logical security, change management) and the Management booklet on policy-framework expectations. Operative for FFIEC-supervised institutions.
- **SEC cybersecurity rules** — 8-K Item 1.05 (material cybersecurity incident disclosure, effective December 2023) and Reg S-K Item 106 (cybersecurity risk management, strategy, and governance) for public registrants. Both impose policy-disclosure expectations.
- **Reg S-P** — 17 CFR §248.30, customer-information safeguards for SEC-registered entities. The 2024 amendment introduced incident-response and customer-notification policy requirements.
- **GLBA Safeguards Rule** — 16 CFR Part 314 (FTC) and the bank-supervisor equivalent. §314.4 lists program elements.
- **NIST Cybersecurity Framework 2.0** (February 2024) — used as a policy taxonomy where the firm anchors on it. The Govern function is new in 2.0 and is a frequent benchmark for governance-policy gaps in pre-2024 cyber policies.
- **NIST SP 800-53 Rev. 5** — Security and Privacy Controls. Used as a granular policy benchmark for federal-tied entities and for firms that anchor on FedRAMP-style profiles.
- **CISA Cross-Sector Cybersecurity Performance Goals** — voluntary baseline; sometimes referenced in supervisor expectations for critical-infrastructure entities.

#### Gap patterns the cyber overlay flags

##### Governance gaps

- Cybersecurity policy approval cadence and board attestation, where NYDFS §500.3 expects board (or equivalent governing-body) approval at least annually and a CISO report to the board annually under §500.4.
- CISO appointment and reporting line, where NYDFS §500.4 and Reg S-K Item 106(c) expect the policy to articulate the CISO's role and reporting.
- Risk assessment cadence, where NYDFS §500.9 expects the policy to set the cadence and methodology.

##### Identity and access gaps

- Multi-factor authentication policy, where NYDFS §500.12 (post-amendment) is more prescriptive than pre-amendment; covered entities must address MFA on all individuals accessing internal networks from external networks, all privileged accounts, and all third-party applications accessing nonpublic information.
- Privileged access management policy, where NYDFS §500.7 (post-amendment) introduces explicit expectations on privileged-account management.
- Access review cadence, where the policy is silent on quarterly cadence for privileged accounts.

##### Vulnerability and threat-management gaps

- Vulnerability management program policy, where NYDFS §500.5 expects continuous monitoring or vulnerability assessments; pre-amendment policies often stop at periodic scanning.
- Penetration testing cadence, where NYDFS §500.5(a)(2) expects annual penetration testing for covered entities.
- Patch-management policy, where the policy lacks named SLAs for critical-vulnerability remediation.

##### Incident-response gaps

- Incident-response plan, where NYDFS §500.16 expects the policy to address detection, response, recovery, communication, and reporting; gap rows often surface on the post-amendment expansion to ransomware and extortion.
- Incident-notice readiness, where the policy does not name the materiality-determination workflow, the named approver, the notification template, or the dispatch path. NYDFS §500.17 imposes a 72-hour notice for material cybersecurity events; SEC 8-K Item 1.05 imposes a 4-business-day disclosure for public-registrant material incidents; Reg S-P amended customer-notification timing.
- Ransomware-payment notice (post-amendment NYDFS §500.17) and CISA reporting expectations where applicable.

##### Third-party-cyber gaps

- Third-party service-provider security policy, where NYDFS §500.11 imposes specific content elements that pre-amendment policies often miss.
- Vendor cyber-incident notification policy, where the policy says vendors will notify but does not name the expected timing in the contract template.
- Subservice-provider transparency policy, where the policy is silent on the SOC report's complementary subservice organisation controls (CSOCs).

##### Data-protection gaps

- Encryption policy, where NYDFS §500.15 expects encryption of nonpublic information in transit and at rest, with documented compensating controls if not feasible.
- Data-loss prevention (DLP) policy, where the policy is silent or generic.
- Data-classification policy, where the policy does not feed protective controls to data tiers.

##### Public-registrant disclosure-process gaps

For SEC public registrants, the matrix carries gap rows on the cyber-disclosure process itself: materiality-determination policy (who decides, against what threshold, with what documentation), 8-K filing-timing policy (4 business days from materiality determination), and Reg S-K Item 106 annual disclosure policy (governance, risk management strategy, board oversight). Frequent gap site for pre-2023 disclosure policies.

##### AI-system cybersecurity gaps (when in scope)

- Model-artefact integrity policy (signing, attestation).
- Model-serving-endpoint authentication and rate-limiting policy.
- Prompt-injection and adversarial-input handling policy.
- Tool-and-agent-privilege boundary policy (when scope includes agentic AI).

#### Implications for matrix construction

- **Cyber-policy gaps are usually `partial` or `outdated`, rarely `missing`.** Most firms have a cybersecurity policy; the question is whether it addresses the named benchmark's content elements at the rigor the rule expects.
- **The matrix surfaces the materiality-determination workflow as a control, not a fact.** A policy that says "we will determine materiality" is partial until the materiality-determination workflow is named.
- **Joint ownership is common and explicit.** Cyber-policy gaps for AI models name the CISO function and the model owner together; cyber-policy gaps for vendor controls name the CISO function and the head of TPRM together.
- **Pre-November-2023 NYDFS policies almost always carry `outdated` rows.** The 2023 amendment expanded enough content that policies untouched since 2017-2022 will not pass the post-amendment expectations.

#### Anchors used by this overlay

- 23 NYCRR Part 500 — NYDFS Cybersecurity Requirements (post-November 2023 amendment) [verify section labels for amended provisions].
- FFIEC IT Examination Handbook, Information Security booklet (September 2016) [verify currently posted edition].
- 17 CFR §229.106 — SEC Reg S-K Item 106 (cybersecurity risk management, strategy, and governance disclosure).
- Form 8-K Item 1.05 — material cybersecurity incident disclosure (effective December 2023).
- 17 CFR §248.30 — Reg S-P (Safeguards Rule and 2024-amendment incident-response and notification).
- 16 CFR Part 314 — FTC Safeguards Rule [verify post-amendment edition].
- NIST Cybersecurity Framework 2.0 (February 2024).
- NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations.
- CISA Cross-Sector Cybersecurity Performance Goals.

## privacy

### Privacy cross-cutting overlay — policy-gap-review

Loads when the scope `cross_cutting_overlay_set` includes `privacy`. Binds the matrix to privacy-and-data-handling-policy expectations when the policy in scope is a privacy policy, a customer-data-handling policy, a data-governance policy, or a substantive policy that includes a section on personally identifiable information or nonpublic personal information.

#### Source basis

##### GLBA Safeguards Rule and Privacy Rule

- **16 CFR Part 314** (FTC Safeguards Rule, post-amendment 2021/2023) and the bank-supervisor equivalent for prudentially-supervised institutions. §314.4 lists program elements: designate a qualified individual, conduct a written risk assessment, implement safeguards (access controls, identification and inventory of data, encryption, secure development, MFA, secure disposal, change management, monitoring), test, train, oversee service providers, written incident-response plan, periodic reporting to board.
- **16 CFR Part 313** (FTC Privacy Rule), with bank-supervisor-equivalent rules for prudential-supervised institutions and Reg P (12 CFR Part 1016) for CFPB-supervised institutions.

##### Reg P — 12 CFR Part 1016

Anchor: §1016.4 initial privacy notice; §1016.5 annual privacy notice (with the post-2015 exception for institutions meeting the FAST Act conditions); §1016.10 sharing limitations and opt-out; §1016.13 affiliate sharing under FCRA. [verify section labels.]

##### Reg S-P — 17 CFR §248.30

Anchor: SEC customer-information safeguards rule. The 2024 amendment introduced incident-response and customer-notification policy requirements that pre-2024 policies almost always miss. [verify post-2024 amendment numbering.]

##### State privacy laws

- **California Consumer Privacy Act / California Privacy Rights Act** (CCPA/CPRA) — Cal. Civ. Code §1798.100 et seq. Operative for businesses meeting the threshold; financial-services entities are partially exempt for GLBA-covered information but the exemption is narrower than commonly assumed.
- **Virginia Consumer Data Protection Act** (VCDPA), **Colorado Privacy Act** (CPA), **Connecticut Data Privacy Act** (CTDPA), and a growing list of state laws since 2023. Each carries its own thresholds and policy expectations; the matrix references the operative state laws where the firm has covered consumers.

##### FCRA-related anchors

- **FCRA** — 15 USC §1681 et seq., for any policy touching consumer-report information.
- **Reg V** — 12 CFR Part 1022, including affiliate-marketing rules and the Identity Theft Red Flags rules under Subpart J (the Reg S-ID parallel).
- **Reg V furnisher accuracy and integrity rules** under §1022.42 et seq.

##### Sectoral rules touching privacy

- **HIPAA** — 45 CFR Part 160, 164 (when the firm holds protected health information; less common in financial services but applies to insurance entities holding member health data).
- **Gramm-Leach-Bliley** umbrella applies across financial services; the matrix's privacy section anchors here for most engagements.

#### Gap patterns the privacy overlay flags

##### Information-security-program policy gaps

- Designation of a qualified individual responsible for the security program (§314.4(a)).
- Written risk assessment (§314.4(b)) at the cadence the rule expects, with documented methodology.
- Written incident-response plan (§314.4(h) post-2021 amendment), with named roles and customer-notification triggers.
- Periodic written report to the board (§314.4(i) post-2021 amendment) at least annually.

##### Privacy-notice policy gaps

- Initial privacy notice content (Reg P §1016.4 / Reg S-P §248.4), where the policy does not name the content elements the rule requires.
- Annual privacy notice (Reg P §1016.5 / Reg S-P §248.5), where the policy is silent on the FAST Act exception conditions for opt-out-eligible institutions.
- Opt-out mechanics (Reg P §1016.7 / Reg S-P §248.7), where the policy does not name the opt-out method or the response timing.
- Affiliate-marketing opt-out under FCRA §624 (Reg V §1022.20-§1022.27), where the policy is silent on the affiliate-marketing-specific opt-out separate from Reg P opt-out.

##### Customer-incident-notification policy gaps (Reg S-P 2024 amendment)

- Customer-notification triggers and timing under the 2024 Reg S-P amendment (notify customers as soon as practicable but not later than 30 days after determining unauthorised access or use occurred or is reasonably likely to have occurred). Pre-2024 customer-notification policies almost always miss this.
- Service-provider oversight including contractual obligation to notify the firm of incidents within a named timeframe.
- Documentation of the materiality determination and the customer-list scoping.

##### State-privacy-law gaps

- CCPA/CPRA disclosure requirements under §1798.100, where the policy does not address the categories of information the firm collects, the sources, the business purposes, the disclosures to third parties, and the consumer rights.
- Consumer-rights handling (access, deletion, correction, portability, opt-out of sale/share) where the policy is silent on the workflow and timing.
- Service-provider and third-party contractor flow-down provisions, where the firm-side contract templates do not pass through the state-law required terms.

##### FCRA and Reg V gaps

- Furnisher accuracy and integrity policy (Reg V §1022.42), where the firm furnishes information to a consumer reporting agency and the policy is silent on the accuracy-and-integrity expectations.
- Identity Theft Red Flags policy (Reg V Subpart J / Reg S-ID), where the policy is silent on the red-flags identification, response, and program-administration content elements.
- FCRA dispute handling under §1681s-2(b), where the policy is silent on the firm's investigation obligations on receiving a CRA dispute.

##### Sectoral overlays

- HIPAA policy expectations where the firm is a covered entity or business associate.
- Children's Online Privacy Protection Act (COPPA) where the firm collects information from users under 13; rare in financial services but applies in some fintech edu-products.

#### Implications for matrix construction

- **GLBA Safeguards is the most-cited privacy benchmark** because it imposes prescriptive program-element expectations. Most privacy-policy gaps trace to a Safeguards element the policy does not address at the rigor the rule expects.
- **The 2024 Reg S-P customer-notification amendment is a high-frequency `outdated` row.** Policies that were refreshed in 2022-2023 typically do not address the 2024 amendment.
- **State-privacy-law gaps appear as a layered set.** Where the firm operates across multiple state perimeters, the matrix surfaces gaps state-by-state rather than rolling up to a single "state privacy" row.
- **GLBA-exemption claims under CCPA/CPRA need explicit support.** A policy that broadly cites the GLBA exemption without addressing the narrowing courts have applied is a gap; the matrix flags the exemption-scope question for legal review.

#### Anchors used by this overlay

- 16 CFR Part 314 — FTC Safeguards Rule [verify post-2021/2023 amendment edition].
- 16 CFR Part 313 — FTC Privacy Rule.
- 12 CFR Part 1016 — Regulation P (CFPB privacy rule).
- 17 CFR §248.30 — Reg S-P [verify post-2024 amendment numbering].
- 12 CFR Part 1022 — Regulation V (FCRA implementation), including Subpart J (Identity Theft Red Flags) and §1022.20-§1022.27 (affiliate marketing).
- 15 USC §1681 — FCRA.
- Cal. Civ. Code §1798.100 et seq. — CCPA/CPRA.
- Va. Code §59.1-575 et seq. — VCDPA.
- Colo. Rev. Stat. §6-1-1301 et seq. — CPA.
- Conn. Gen. Stat. §42-515 et seq. — CTDPA.
- 45 CFR Parts 160, 164 — HIPAA Privacy and Security Rules (when in scope).
- 16 CFR Part 312 — COPPA (when in scope).
