# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay for prompt-injection-risk

When the scope record names `banking` as the sector, this overlay adds banking-specific carriers, mitigations, monitoring signals, and incident-notification triggers to the review. Loaded by `prompt-injection-risk/SKILL.md` when `scope.sector_overlay_set` includes `banking`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- FFIEC IT Examination Handbook, Information Security and AIO booklets, applied to the GenAI system's serving environment, change controls, and access controls.
- Joint Interagency Guidance on Third-Party Relationships (June 2023; OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023) where the GenAI system is vendor-hosted or relies on a foundation-model provider.
- The joint interagency Revised Guidance on Model Risk Management (OCC 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, supersedes SR 11-7 and SR 21-8) expressly excludes generative AI from its scope (footnote 3); the GenAI use case is not within the bulletin. Where the bank's model risk programme treats it as a model by analogy, the principles inform but the binding hook is firm policy.
- 12 CFR Part 30 Appendix D (OCC Heightened Standards) for OCC-supervised large banks where the GenAI use case sits inside a risk-appetite-statement-relevant function.
- NYDFS 23 NYCRR Part 500 and the October 2024 AI Industry Letter for NY-footprint covered entities.
- The 36-hour banking computer-security incident notification rule: 12 CFR Part 53 (OCC), 12 CFR Part 225 Subpart N (FRB), 12 CFR Part 304 (FDIC), effective 2022.
- FFIEC BSA/AML Examination Manual where the GenAI use case touches AML alert handling, customer risk rating, or SAR drafting.

#### Carriers and trust posture nuances specific to banking

The recurring banking GenAI use-case patterns and the carriers that usually drive the threat surface:

- **Relationship-manager assistant**: retrieves over internal CRM, recent earnings transcripts, internal research notes, third-party vendor research. Highest-likelihood vector is indirect injection in third-party content (transcripts, news, vendor research). The CRM is firm-controlled but contains client-supplied content (emails, chat, meeting notes) that can carry adversarial instructions placed by a counterparty.

- **Customer-service assistant**: retrieves over customer history (calls, chats, emails), policy and procedure corpus. Highest-likelihood vector is indirect injection via customer-history content and cross-customer information bleed via crafted query. The agent-review gate is preventive but is the only line of defence between a misleading summary and the customer; off-switch criterion under the agent-review gate is therefore load-bearing.

- **AML alert-triage assistant**: retrieves over alert narratives, customer profiles, transaction histories, sanctions screening hits, third-party intelligence. Highest-likelihood vector is indirect injection via alert narrative content (which can be free-text and originate from analyst notes, system-generated descriptions, or third-party intelligence feeds). Misrouted alert handling is a BSA/AML programme integrity issue; the BSA officer is a co-reviewer where the use case touches alert disposition.

- **KYC/EDD assistant**: retrieves over identity-verification documents, beneficial-ownership records, third-party adverse-media feeds, jurisdiction risk content. Highest-likelihood vector is indirect injection via adverse-media or third-party intelligence content; PII exfiltration risk is structural.

- **Treasury-management assistant**: retrieves over client cash-management profiles, payment patterns, fraud-rule documentation. Where tools are enabled (rate quotes, payment initiation, statement generation), tool-boundary controls become the load-bearing mitigation; fraud and authorisation framings apply.

#### Mitigations the review should expect to see

Beyond the standard set:

- Role-based access on retrieval scoping, aligned to the banking entitlement model. Per-customer query scoping is the default for any customer-facing or customer-handling assistant; the review should confirm the scope at the retrieval layer rather than only at the prompt layer.
- Marketing Rule and consumer-disclosure-equivalent output filtering for any customer-facing communication generated or assisted by the system; UDAAP exposure on customer-facing AI output is the conduct-overlay seam, not a banking-specific one, but the banking sector inherits the framing.
- Sanctions and OFAC name-screening on any output that could include third-party identifying information.
- BSA/AML output filtering where the system outputs contribute to alert disposition or SAR narratives; the BSA officer signs off on the filtering specification.
- Foundation-model and vendor change-of-version notice and audit rights, captured in the third-party risk register and consistent with the June 2023 interagency guidance.

#### Monitoring signals the overlay adds

- Per-customer retrieval audit (random sampling plus rule-based detection on cross-customer ID surfaces); any confirmed event is an investigation trigger and may be a §500.17(a) trigger for NY-footprint entities.
- Marketing Rule output-filter trip rate where applicable (joint trust company / RIA / BD entities); escalation to compliance.
- AML alert-disposition anomaly where the system supports alert handling; escalation to the BSA officer.
- 36-hour banking computer-security incident notification trigger evaluation: any cybersecurity event that materially disrupts or degrades, or is reasonably likely to materially disrupt or degrade, the bank's ability to deliver services, or that has resulted in actual harm to the bank's operations, must be evaluated against the 36-hour trigger; cyber and AI governance jointly assess.

#### Incident-response triggers the overlay adds

In addition to the cyber-overlay-named triggers (NYDFS §500.17(a), SEC 8-K Item 1.05, GLBA Safeguards Rule):

- 12 CFR Part 53 / Part 225 / Part 304 (36-hour banking computer-security incident notification): the bank must notify its primary federal regulator within 36 hours of determining that a notification incident has occurred. Prompt-injection events causing material disruption, degradation, or actual harm to bank operations are within scope. The notification decision sits with the cyber and operational-resilience leads with general counsel.
- BSA/AML programme integrity event triggers if the GenAI use case touches alert disposition or SAR narratives and the integrity of those outputs is in question; the BSA officer evaluates against the SAR continuing-activity reporting framework and against programme-integrity examination expectations.
- Consumer-protection event triggers if customer-facing AI output causes a UDAAP-relevant communication issue; consumer compliance evaluates.

#### Recommended-action items the overlay surfaces

- Where the GenAI use case is in OCC large-bank scope (12 CFR Part 30 Appendix D), the review records the connection to the bank's risk-appetite-statement framework and surfaces residual-risk acceptance to the chief risk executive function.
- Where the use case is vendor-hosted or relies on a foundation-model provider, the third-party risk register entry is updated to reference the prompt-injection review and the foundation-model swap re-validation flag is recorded.
- Where the use case touches AML alert handling, the BSA officer co-signs the residual-risk acceptance.
- Where the use case is customer-facing in NY footprint, the NYDFS §500.17(a) notification-decision process is rehearsed against AI-specific incident scenarios.

#### Common pitfalls specific to banking

- Treating a bank-hosted assistant on a vendor-hosted foundation model as if the firm controls the full stack. The vendor's foundation-model behaviour shift is a third-party event and a cyber event; both framings need to be in the review.
- Omitting the 36-hour banking computer-security incident notification rule. It is distinct from the NYDFS 72-hour notice and from the SEC 8-K four-business-day disclosure; all three can apply concurrently for a single material event in a NY-footprint public-registrant bank.
- Failing to involve the BSA officer when the GenAI use case touches alert handling; an integrity issue with AI-assisted alert disposition is a BSA programme issue.
- Treating the agent-review gate as a permanent control without an off-switch criterion. Under volume pressure, the gate becomes rubber-stamping; the review should record a defined off-switch (e.g., agent-edit rate falling below a threshold for two consecutive periods triggers a pause and re-validation).

## capital-markets

### Capital markets sector overlay for prompt-injection-risk

When the scope record names `capital-markets` as the sector, this overlay adds capital-markets-specific carriers, mitigations, monitoring signals, and incident-notification triggers to the review. Loaded by `prompt-injection-risk/SKILL.md` when `scope.sector_overlay_set` includes `capital-markets`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- SEC Investment Advisers Act Rule 206(4)-1 (Marketing Rule) for AI-generated client-facing content from registered investment advisers.
- SEC Adviser Books and Records Rule 17 CFR §275.204-2 and BD Rules 17 CFR §240.17a-3 / §240.17a-4 for preservation of AI-generated records supporting recommendations or trading decisions.
- SEC Investment Advisers Act Rule 206(4)-7 (Compliance Program Rule) where the AI system is in scope of the adviser's compliance programme.
- SEC Rule 15c3-5 (Market Access Rule) where the GenAI system is in the path of an order-routing or market-access decision.
- SEC Regulation BI and the SR/IA fiduciary lens where the AI output supports retail recommendations.
- SEC cyber disclosure rules (8-K Item 1.05 and Reg S-K Item 106) for public registrants.
- FINRA Rules 2010 (standards of commercial honor), 2210 (communications with the public), 3110 (supervision), and 4511 (general books and records) for FINRA member broker-dealers.
- Market Abuse Regulation (EU) 596/2014 and SEC Rule 10b-5 / Regulation FD where the AI system handles or generates content adjacent to material non-public information.

#### Carriers and trust posture nuances specific to capital markets

The recurring capital-markets GenAI use-case patterns and the carriers that usually drive the threat surface:

- **Equity research assistant**: retrieves over internal research notes, past models, vendor research, earnings transcripts, news, social media. Highest-likelihood vector is indirect injection in third-party content (news, social media, transcripts, vendor research). For agentic configurations with tool use (web fetch, market-data API, draft-write), the threat surface fans out per the agentic example in `examples.md#agentic-research-assistant`.

- **Investment-banking deal assistant**: retrieves over deal documents, comparables, legal precedents, regulatory filings. The MNPI handling lens is structural; cross-deal information bleed is the structural risk and the conduct-side seam is information-barrier integrity.

- **Compliance and surveillance assistant**: retrieves over transaction records, communication archives (email, chat, voice transcripts), market data, alert narratives. Highest-likelihood vector is indirect injection via communication-archive content (which can be free-text and user-controlled at origin); surveillance-system integrity is the downstream consequence.

- **Wealth-management/RIA client-facing assistant**: retrieves over client profiles, account history, model portfolios, planning content. The Marketing Rule and Reg BI / fiduciary lens bite hard; any AI-generated client-facing content is in scope of the Marketing Rule for advisers, and the books-and-records preservation applies.

- **Trading-desk and execution-algo support**: where the GenAI system is in or adjacent to the order path, Rule 15c3-5 controls overlap with the prompt-injection mitigation set; the trading-controls function is a co-reviewer.

#### Mitigations the review should expect to see

Beyond the standard set:

- Marketing Rule output filtering for any AI-generated client-facing content; compliance signs off on the filtering specification. The general prohibitions, performance-presentation rules, and testimonial/endorsement requirements all apply where the output meets the definition of an advertisement.
- Books-and-records capture of AI-generated content supporting a recommendation or trading decision; the record-retention configuration is part of the mitigation set.
- Information-barrier-aligned retrieval scoping for any system that operates across deal teams or across public and private sides; cross-side retrieval is a finding, not a discretionary mitigation.
- MNPI-handling controls on retrieval scoping for systems handling deal documents, research-in-progress, or material non-public information; the firm's information-barrier programme defines the scope.
- Surveillance-system integrity controls for systems that support alert disposition; the surveillance and supervision functions co-sign the mitigation specification.
- Rule 15c3-5 control overlap for any system in the order path; the trading-controls function reviews the GenAI-side mitigations against the existing market-access controls.
- For agentic systems with tool use, planner-side topic validation and tool-boundary controls; tool-boundary on any tool that could publish, send, trade, or take a consequential external action is the load-bearing mitigation.

#### Monitoring signals the overlay adds

- Marketing Rule output-filter trip rate for any client-facing AI output; escalation to compliance.
- Books-and-records preservation health check (is the AI-generated content actually being retained per the firm's books-and-records configuration?); periodic.
- Cross-deal or cross-side retrieval audit for systems operating across information-barrier boundaries; any confirmed event is an investigation trigger.
- Cross-ticker tool-invocation anomaly for systems with market-data tool access (queries on tickers outside the user's coverage); escalation to surveillance and supervision.
- Tool-invocation rate and pattern monitoring for agentic systems; escalation to information security with cyber overlay framing.
- For systems supporting surveillance, alert-disposition anomaly and SAR-narrative integrity sampling.

#### Incident-response triggers the overlay adds

In addition to the cyber-overlay-named triggers:

- SEC Marketing Rule violation: a confirmed publication of misleading AI-generated client communications creates Marketing Rule exposure; compliance evaluates against the Marketing Rule violation framework and against the firm's compliance-programme self-reporting posture.
- SEC books-and-records violation: a confirmed failure to preserve AI-generated records supporting a recommendation or trading decision creates books-and-records exposure.
- FINRA Rule 4530 reporting: FINRA member broker-dealers must report certain events under Rule 4530; AI-driven incidents that fall within the rule's scope are reportable.
- Information-barrier breach via cross-side retrieval: legal and compliance evaluate; potential reportable event depending on materiality and the firm's information-barrier programme commitments.
- Market Abuse Regulation considerations for EU-footprint registrants: AI-driven inadvertent disclosure of MNPI or AI-driven market-manipulation-relevant output is in scope.

#### Recommended-action items the overlay surfaces

- Where the use case is client-facing and from a registered investment adviser, the Marketing Rule compliance review is a required pre-prod step, not a discretionary one; compliance co-signs the residual-risk acceptance.
- Where the use case operates across information-barrier boundaries, the information-barrier owner co-signs and the retrieval-scope configuration is documented in the firm's information-barrier programme.
- Where the use case is in or adjacent to the order path, the trading-controls function reviews the GenAI-side mitigations against the Rule 15c3-5 control framework.
- Where the use case supports surveillance, the chief compliance officer or the head of surveillance co-signs the residual-risk acceptance.
- For agentic systems with tool use, the planner-side topic validation and the tool-boundary controls are tested under firm-internal red team before pre-prod gate; vendor red-team coverage of multi-agent and tool-use topologies is typically thin.

#### Common pitfalls specific to capital markets

- Treating an internal-only research assistant as out of Marketing Rule scope. The moment the analyst publishes the AI-drafted note, the Marketing Rule reach kicks in. The analyst-publication seam is where the conduct lens lands; the review records the seam as a residual risk and the analyst-attestation step as a recommended mitigation.
- Omitting the books-and-records preservation health check. AI-generated content that is not preserved per the firm's books-and-records configuration is a recurring exam finding; the review records the preservation control and the periodic health check.
- Treating information-barrier retrieval scoping as a one-time configuration decision. The retrieval scope must be re-validated when the information-barrier programme changes, when the data sources change, and when the user population changes.
- Failing to involve the trading-controls function for systems in or adjacent to the order path. Rule 15c3-5 controls are not optional; the GenAI-side mitigations must be reviewed alongside the existing market-access controls, not in parallel.
- Treating vendor red-team coverage as sufficient for agentic systems with tool use. Vendor sets do not exercise multi-agent topologies and rarely exercise firm-specific tool inventories; firm-internal red team is the load-bearing test source.
- Recording rolling-with-notice foundation-model versioning for any tier-1 or tier-2 capital-markets agentic system. Pinned versioning is the recommended posture; the review surfaces the rolling-with-notice posture as a finding and pinning as a recommended action.

## insurance

### Insurance sector overlay for prompt-injection-risk

When the scope record names `insurance` as the sector, this overlay adds insurance-specific carriers, mitigations, monitoring signals, and incident-notification triggers to the review. Loaded by `prompt-injection-risk/SKILL.md` when `scope.sector_overlay_set` includes `insurance`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- NAIC Model Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023), AIS Program elements covering risk management, testing and validation, third-party AI accountability, monitoring, and documentation; binding only to the extent state DOIs adopt it (state-adoption tracker maintained by the NAIC AI Working Group).
- NYDFS Insurance Circular Letter on the Use of AI Systems and ECDIS in Insurance Underwriting and Pricing (January 2024) for NY-licensed life carriers.
- NYDFS October 2024 cyber-AI Industry Letter for NY-licensed insurers (NYDFS-covered entity status applies under 23 NYCRR Part 500).
- Colorado Division of Insurance regulation implementing SB 21-169 (life insurance underwriting governance for ECDIS and predictive models).
- HIPAA Privacy Rule (45 CFR Part 164) where the GenAI use case handles PHI under a covered-entity or business-associate relationship; HIPAA Security Rule (45 CFR Part 164 Subpart C) for the security side.
- State insurance commissioner cybersecurity regulations modelled on the NAIC Insurance Data Security Model Law (e.g., 23 NYCRR Part 500 for NY, similar regulations in other adopting states); state breach-notification laws for non-adopting states.
- ACORD standards and carrier proprietary forms for document-handling injection considerations.

#### Carriers and trust posture nuances specific to insurance

The recurring insurance GenAI use-case patterns and the carriers that usually drive the threat surface:

- **Claims-summary assistant**: retrieves over scanned correspondence (claimant letters, third-party adjuster notes, repair estimates), medical records, police reports, attorney correspondence, recorded statement transcripts. Highest-likelihood vector is indirect injection via scanned correspondence and via medical-record content; OCR'd content is partially trusted and contains content originating from claimants, providers, attorneys, and third-party adjusters who may have an adversarial interest in claim outcome.

- **Underwriting assistant** (life and health): retrieves over application data, medical records, prescription history, motor vehicle records, public-records databases, ECDIS sources (consumer reports, social and behavioural data sources). Highest-likelihood vector is indirect injection via ECDIS content (third-party-controlled at source) and the unfair-discrimination overlay is structural; the NYDFS Circular Letter and Colorado SB 21-169 framings both apply where in jurisdiction.

- **Customer-service assistant** (P&C and life): retrieves over policy data, call and chat history, claims status. Similar pattern to banking customer-service assistant; cross-policy and cross-policyholder bleed is the structural risk.

- **Producer/agent assistant**: retrieves over product documentation, illustration software output, regulatory filings. Marketing Rule analogues (state insurance advertising rules and SEC Rule 156 for variable products) are the conduct-side seam.

- **Fraud-detection assistant**: retrieves over claim files, social-media content, third-party fraud-network data. Indirect injection in third-party intelligence is the structural risk; SIU referral integrity is the downstream consequence.

#### Mitigations the review should expect to see

Beyond the standard set:

- HIPAA-aligned access controls on PHI carriers; per-claim or per-policy query scoping is the default for any claim or policy-handling assistant.
- ECDIS-specific input controls: source-vetting at the data-vendor layer, change-detection on ECDIS sources, drift monitoring on ECDIS-sourced features (NYDFS Circular Letter and Colorado SB 21-169 expectations on ECDIS governance flow into the prompt-injection mitigation set).
- OCR-stage input sanitisation for scanned correspondence: normalisation of suspicious patterns, separation of OCR'd text from system instructions in the prompt structure, content-type tagging.
- State unfair-discrimination output filtering for any underwriting or pricing recommendation; the underwriting actuary signs off on the filtering specification.
- Marketing Rule equivalents for any customer-facing or agent-facing communication generated or assisted by the system; state insurance advertising rules apply.
- Foundation-model and vendor change-of-version notice and audit rights, captured in the third-party AI register required by the NAIC Bulletin AIS Program element on third-party accountability.

#### Monitoring signals the overlay adds

- Per-claim and per-policy retrieval audit; any confirmed cross-claim or cross-policy bleed is a HIPAA evaluation trigger and may be a NYDFS §500.17(a) trigger for NY-licensed entities.
- ECDIS source-integrity monitoring (vendor change-of-content, last-modified, content hash on dynamic sources) for underwriting and pricing assistants.
- Unfair-discrimination output-filter trip rate where applicable; escalation to the underwriting actuary and to the chief actuarial officer or equivalent.
- State insurance advertising rule output-filter trip rate where applicable; escalation to compliance.
- Cyber-side signals from the cyber overlay (authentication anomalies, tool-invocation patterns, vendor change-of-version) apply per NYDFS Part 500 and adopting-state Insurance Data Security Model Law equivalents.

#### Incident-response triggers the overlay adds

In addition to the cyber-overlay-named triggers:

- HIPAA breach notification: the Breach Notification Rule (45 CFR §§164.400-414) requires notification to affected individuals, HHS, and in some cases the media following discovery of a breach of unsecured PHI. Prompt-injection events causing PHI exfiltration are within scope.
- State Insurance Data Security Model Law-adopting jurisdictions: cybersecurity event notification to the state insurance commissioner per the adopting state's regulation (timing varies; commonly 72 hours).
- State unfair-discrimination event triggers if an injection-driven event causes a discriminatory output that affects an underwriting or pricing decision; the state DOI may be the appropriate notification authority depending on jurisdiction.
- Producer-side conduct triggers if the system is used in a way that violates state insurance advertising rules or state suitability requirements.

#### Recommended-action items the overlay surfaces

- Where the use case is in scope of the NAIC Bulletin (in adopting states), the AIS Program documentation is updated to reference the prompt-injection review and the residual risk acceptance is recorded against the AIS Program element on documentation.
- Where the use case is in NY-licensed life-carrier underwriting scope, the NYDFS Circular Letter governance, fairness-testing, disclosure, and consumer-recourse expectations are mapped to the review's mitigations and recommended actions.
- Where the use case is in Colorado life-carrier underwriting scope, the SB 21-169 implementing regulation is referenced and the unfair-discrimination testing is mapped to the review's tested-attack and monitoring sections.
- Where the use case handles PHI, the privacy officer co-signs the residual-risk acceptance and the HIPAA breach-notification process is rehearsed.

#### Common pitfalls specific to insurance

- Treating ECDIS-sourced content as trusted because the data vendor is on the firm's approved-vendor list. The vendor's source-of-source is third-party-controlled; ECDIS-specific source-vetting and change-detection are the load-bearing controls, not vendor approval at procurement time.
- Omitting OCR-stage sanitisation for scanned correspondence in claims assistants. The OCR output is the point at which injected content lands in the prompt path; sanitisation at the OCR stage is more reliable than at the prompt-construction stage.
- Failing to involve the privacy officer when the use case handles PHI; a HIPAA-relevant exfiltration is a privacy event with binding notification timelines, not a discretionary AI-governance decision.
- Treating the unfair-discrimination overlay as separable from the prompt-injection overlay for underwriting assistants. An injection-driven feature shift in an ECDIS-sourced input can produce discriminatory output that violates state unfair-discrimination law; the two overlays are entangled.
- Omitting state-by-state breach-notification analysis when the firm operates across multiple states; the state patchwork is the firm's responsibility to maintain and the review references the firm's matrix rather than restating it.

## payments-fintech

### Payments and fintech sector overlay for prompt-injection-risk

When the scope record names `payments-fintech` as the sector, this overlay adds payments-fintech-specific carriers, mitigations, monitoring signals, and incident-notification triggers to the review. Loaded by `prompt-injection-risk/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`. Cited and section-referenced anchors live in `references/source-anchors.md`.

#### Source basis

- Joint Interagency Guidance on Third-Party Relationships (June 2023; OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023) where the GenAI use case sits in a sponsor-bank / fintech (BaaS) arrangement; the sponsor bank retains accountability for the third-party AI risk.
- The 36-hour banking computer-security incident notification rule (12 CFR Part 53 / Part 225 / Part 304) where the fintech is bank-affiliated or operates under a sponsor-bank.
- CFPB UDAAP authority and CFPB consumer-financial-product expectations for fintechs in CFPB scope.
- Reg E (12 CFR Part 1005, Electronic Fund Transfers) and Reg Z (12 CFR Part 1026) for consumer-facing payments and credit products.
- FinCEN BSA expectations applied to money services businesses, virtual-currency businesses, and payments processors in BSA scope.
- State money-transmitter licensing regimes (state-by-state patchwork; the firm maintains the matrix).
- NYDFS 23 NYCRR Part 500 and the Part 200 virtual-currency regulation for NY-licensed entities.
- PCI DSS for cardholder-data-handling systems.

#### Carriers and trust posture nuances specific to payments and fintech

The recurring payments-fintech GenAI use-case patterns and the carriers that usually drive the threat surface:

- **Customer-onboarding assistant** (KYC, identity verification, account opening): retrieves over identity-document content, third-party identity-verification responses, sanctions-screening hits, adverse-media. Highest-likelihood vector is indirect injection via document content (synthetic ID documents with embedded instructions) and via third-party identity-verification API responses; PII exfiltration risk is structural.

- **Dispute-handling assistant** (Reg E, chargeback): retrieves over customer-supplied evidence (photos, screenshots, written narratives), merchant correspondence, transaction records, fraud-detection signals. Highest-likelihood vector is indirect injection via customer-supplied evidence and merchant correspondence; the Reg E provisional-credit decision-support context is the consumer-protection seam (10-day provisional credit, 45-day investigation timeline).

- **Customer-service assistant**: similar pattern to banking customer-service assistant; account-takeover-fraud adjacency is the structural risk because customer-service interactions are an account-takeover entry point.

- **Transaction-monitoring and AML alert-triage assistant**: similar to banking AML overlay; in the fintech context, the BSA officer and the sponsor-bank BSA function (where applicable) are co-reviewers.

- **Merchant-onboarding and underwriting assistant**: retrieves over merchant application data, processor risk data, card-network watch lists. Risk-based pricing and adverse-action-notice considerations apply where the AI output supports adverse decisions.

- **Crypto/virtual-asset-specific assistants**: retrieves over wallet-screening data, blockchain-analytics output, sanctions-screening hits. NYDFS Part 200 and FinCEN MSB framings apply for in-scope entities.

#### Mitigations the review should expect to see

Beyond the standard set:

- Consumer-facing output filtering aligned to UDAAP and Reg E / Reg Z disclosure requirements; consumer compliance signs off.
- Sanctions / OFAC screening on any output that could include third-party identifying information.
- Per-customer query scoping at the retrieval layer for any customer-handling assistant; account-takeover-relevant retrieval audit on top.
- Document-stage input sanitisation for synthetic-ID-resilient document handling in onboarding flows.
- BSA/AML output filtering where the system supports alert disposition or SAR drafting; the BSA officer signs off.
- For sponsor-bank BaaS arrangements, the sponsor-bank's third-party risk register is updated to reference the prompt-injection review and the sponsor-bank's review obligations are documented.
- PCI DSS-aligned controls on systems handling cardholder data.
- Foundation-model and vendor change-of-version notice and audit rights, captured in the third-party risk register; the sponsor-bank's interagency-guidance obligations apply.

#### Monitoring signals the overlay adds

- Per-customer retrieval audit; account-takeover-relevant patterns (off-hours queries, rapid sequential queries, queries from unusual originating IPs) added to the cross-customer audit.
- UDAAP-relevant output-filter trip rate; escalation to consumer compliance.
- Reg E / Reg Z disclosure-content output-filter trip rate where applicable; escalation to consumer compliance.
- BSA/AML alert-disposition anomaly where the system supports alert handling; escalation to the BSA officer and to the sponsor-bank BSA function (where applicable).
- 36-hour banking computer-security incident notification trigger evaluation for sponsor-bank-affiliated incidents.
- Sponsor-bank vendor-management reporting cadence: prompt-injection review status reported to the sponsor-bank per the contractual reporting cadence.

#### Incident-response triggers the overlay adds

In addition to the cyber-overlay-named triggers:

- 36-hour banking computer-security incident notification (where sponsor-bank-affiliated): the sponsor bank notifies its primary federal regulator within 36 hours of determining that a notification incident has occurred. The fintech and the sponsor bank's incident-response chains coordinate.
- Reg E error-resolution timeline: an injection-driven event that affects dispute resolution (delays provisional credit, mishandles error claims) creates Reg E exposure with statutory timelines (10-day provisional credit, 45-day investigation) that the response must meet.
- UDAAP event triggers if customer-facing AI output causes a UDAAP-relevant communication or decisional issue.
- State money-transmitter regulator notification for in-scope entities; the firm's matrix of state-by-state notification obligations governs.
- NYDFS Part 500 §500.17(a) for NY-licensed entities (as in the cyber overlay) and Part 200 incident-handling for NY-licensed virtual-currency entities.
- FinCEN BSA programme-integrity considerations where the system supports alert handling.
- PCI DSS incident-response and card-brand notification for cardholder-data exposure.

#### Recommended-action items the overlay surfaces

- For sponsor-bank BaaS arrangements, the sponsor-bank's review and approval is recorded; the residual-risk acceptance includes the sponsor-bank function as a co-acceptor or as a notification party per the contractual arrangement.
- For consumer-facing assistants, consumer compliance co-signs the residual-risk acceptance and the UDAAP / Reg E / Reg Z output-filter specifications are documented.
- For onboarding assistants, the synthetic-ID-resilience testing is included in the firm-internal red team scope.
- For dispute-handling assistants, the Reg E timeline integrity is documented in the incident-response section (an injection-driven delay in dispute handling is itself a Reg E violation).
- For crypto/virtual-asset assistants, the NYDFS Part 200 framing and the FinCEN MSB framing are mapped to the review's mitigations and incident-response sections.

#### Common pitfalls specific to payments and fintech

- Treating the sponsor-bank as a downstream consumer of the prompt-injection review. Under the June 2023 interagency guidance, the sponsor bank retains accountability for the third-party AI risk; the bank is a co-reviewer or a co-acceptor depending on the contractual arrangement, not a downstream notification party.
- Omitting the 36-hour banking computer-security incident notification rule when the fintech is bank-affiliated. The rule applies to the bank, but the fintech's incident-response chain must support the bank's 36-hour determination timeline.
- Failing to surface Reg E timeline considerations in the dispute-handling-assistant review. An injection-driven event that delays provisional credit or mishandles error claims is a Reg E violation independent of the cyber and AI-governance lenses.
- Treating consumer-facing AI output as an AI-governance-only concern. UDAAP authority and Reg E / Reg Z disclosure requirements apply; consumer compliance is a co-reviewer.
- Omitting state money-transmitter and state-by-state regulator notification considerations. The state patchwork is the firm's responsibility to maintain; the review references the firm's matrix.
- Treating PCI DSS as out of scope because the AI system does not directly handle cardholder data. If the AI system is on the same network segment, can be reached from the cardholder-data environment, or processes content that includes cardholder data even incidentally, PCI DSS scope extends.
