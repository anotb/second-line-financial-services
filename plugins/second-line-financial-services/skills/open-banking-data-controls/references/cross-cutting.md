# cross-cutting

One section per topic. Read only the sections the scope calls for.

## cyber

### Cross-cutting overlay — cyber

Required-on for every engagement run through this skill. The data-rights programme runs on tokens, keys, authentication assurance levels, and an exposed developer interface; the cyber controls on the data flow are not a separate workstream but the operative substance of the controls inventory. This overlay carries the encryption, key lifecycle, token-issuance posture, authentication-assurance reasoning, monitoring, and breach-response detail that the **cyber controls on the data flow** named section reflects.

The overlay does not substitute for the firm's own information-security programme, for an architectural review of the developer interface, or for a penetration-test programme. The pack records the supervisory-level controls posture and the evidence-of-oversight; deeper engineering work flows to the firm's information-security function or to a counsel-led security review.

#### Anchor frame

- **GLBA Safeguards Rule, 16 CFR Part 314** as amended (FTC, December 2021 amendments effective 2023). **§314.4** the written information security programme; **§314.4(c)** access controls, encryption, MFA, secure disposal; **§314.4(d)** monitoring; **§314.4(e)** training; **§314.4(f)** service-provider obligations; **§314.4(h)** incident response; **§314.4(i)** annual report to the board. The Safeguards Rule is the federal floor for the data-flow security posture.
- **NYDFS 23 NYCRR Part 500** including **§500.11** third-party service-provider security, **§500.12** multi-factor authentication, **§500.15** encryption, **§500.16** incident-response plan, **§500.17(a)** cybersecurity-event notification (72 hours from determination). Applies where the firm is a NYDFS Covered Entity; many fintechs are by virtue of NY footprint.
- **FFIEC IT Examination Handbook — Information Security booklet** [verify current edition]. Sets the supervisory expectation for the information-security programme.
- **FFIEC Authentication and Access to Financial Institution Services and Systems Guidance** (August 11, 2021). Sets the supervisory expectation for authentication posture, including for high-risk transactions and customer-permissioned data sharing.
- **NIST SP 800-63B Digital Identity Guidelines** [verify current revision]. Authentication assurance levels (AAL1, AAL2, AAL3) and the lifecycle controls each level requires.
- **OAuth 2.0 (RFC 6749)** and **OpenID FAPI security profile** [verify whether the firm cites FAPI 1.0 Final, FAPI 2.0, or a later profile]. The authorisation-server pattern for tokenised access.

#### Encryption and key management

The artifact's **cyber controls on the data flow** block records:

- Encryption in transit (TLS version, cipher suite posture, certificate-rotation cadence, mutual-TLS posture for B2B integrations).
- Encryption at rest (key strength, vault posture, customer-data-store coverage, token-store coverage, audit-trail-store coverage).
- Key management (HSM-backed vs software-vault-backed, key-rotation cadence, key-escrow posture, separation of duties for key custody, vendor-managed-key posture for any layer the vendor controls).
- The named GLBA Safeguards §314.4(c) encryption requirement and the named FFIEC IT Information Security supervisory expectation as the anchor.

Common failure mode: vendor-managed-key posture without firm-side key-custody evidence. The artifact records the vendor's SOC 2 Type II key-custody attestation and reconciles against the firm's own audit-rights evidence.

#### Token lifecycle for the developer interface

The token lifecycle is the operative control set for the data-rights programme. The artifact records:

- **Token issuance.** Where issuance sits (sponsor-bank side, programme-operator side, vendor-managed authorisation server). The OAuth / FAPI flow type (authorisation-code with PKCE, client-credentials for B2B, FAPI message-signing posture). The audience scope for issued tokens (which data-recipient app, which consumer, which scope subset).
- **Token scope.** Per-consumer scope enforcement at the API runtime, not just at the consent-store record. The artifact records whether the API enforces consent-narrowing (the developer interface returns only what the consumer authorised) or whether it relies on the recipient to filter (a finding).
- **Token revocation.** The propagation path from consumer revocation through the consent store, the authorisation server, the active-token registry, and the API runtime. Revocation that stops the next token issuance but does not invalidate the active token is a finding.
- **Token expiry.** The named expiry cadence for access tokens and refresh tokens; the reauthorisation cadence under the data-rights frame for refresh-token reissuance.
- **Audit trail.** Token-issuance log, token-scope log, token-revocation log, token-use log. Aggregating these into a single audit feed for sponsor-bank review and examiner access is the operative discipline.

#### Authentication assurance level

The artifact's authentication-assurance row carries the named AAL for each consumer-facing flow:

- Consumer authentication into the consent flow at the data provider. AAL2 is the typical supervisory expectation for high-value financial-data access; AAL3 may apply for high-risk programmes.
- Consumer reauthorisation flow. The reauthorisation should re-establish authentication at the same AAL; a reauthorisation flow that drops to a lower AAL (e.g., a magic link without a second factor) is a finding.
- Recipient-side authentication into the developer interface. The OAuth client authentication (mutual-TLS, FAPI message signing, signed JWTs) and the named recipient-side authentication assurance.

The artifact distinguishes the AAL the firm asserts from the AAL the firm evidences. Asserting AAL2 with username-and-password plus an email-OTP flow is a frequent gap; the AAL2 floor requires authenticator types that resist phishing in the same way. The cross-cutting cyber overlay carries the evidence ask.

#### Monitoring and incident detection on the developer interface

The artifact records:

- Anomaly detection on the developer interface (unusual access patterns, unusual scope requests, unusual recipient behaviour). The named monitoring vendor where applicable; the alert-volume and alert-investigation cadence.
- Bot and credential-stuffing detection on consumer-facing authentication flows. The named bot-management vendor where applicable.
- Account-takeover detection at the data provider and the data recipient. The named ATO-detection vendor where applicable.
- The breach-response chain: detection, internal escalation, sponsor-bank notification, customer notification, regulator notification. The named GLBA Safeguards §314.4(h) incident-response posture is the anchor.

#### Breach-response chain to the consumer and the sponsor bank

Where a breach in the data flow touches consumer information, the artifact records the parallel notification clocks:

- The sponsor-bank programme-agreement contractual clock for cyber-incident notification (typically tighter than any regulator clock; often 24 hours or less for cyber events).
- The federal banking agencies' Computer-Security Incident Notification Rule 36-hour clock (binds the sponsor bank, not the programme operator; the programme operator's clock to the sponsor bank under the programme agreement is the input).
- The NYDFS 23 NYCRR Part 500 §500.17(a) 72-hour clock (where the firm is a Covered Entity).
- The state breach-notification clocks (one row per state with affected residents; timing windows vary; cross-link to the privacy overlay for the resident-by-resident detail).
- The GLBA Safeguards Rule notification (where the firm is FTC-supervised and the affected-customer threshold is met; verify current threshold).
- The §1033-specific incident posture: where consumer authorisation flows or developer-interface tokens were affected, the data-rights frame implicates the reauthorisation cadence, the revocation propagation path, and the data-recipient duties chain. The artifact records the §1033-implications row separately and propagates the `s1033_status_note` block.

Cross-link to `payment-operations-incident-review` for the payments-operational chain when an incident has both an open-banking leg and a payments-rail leg, and to `cyber-disclosure-readiness` for the public-disclosure leg where the firm or its sponsor bank is a public registrant.

#### Vendor-stack cyber posture for the developer interface

Where the developer interface, the authorisation server, or the consent-management runtime sits with a vendor, the artifact's **vendor and fourth-party register** records:

- The vendor's most-recent SOC 2 Type II report status (current, expired, qualified opinion, exception with management response) and the audit-rights posture under the firm-vendor contract.
- The vendor's penetration-test cadence and the firm's right-to-receive-results posture.
- The vendor's incident-notification clock under the firm-vendor contract (often 24 hours or less for cyber events) and the firm's right-to-cooperate posture.
- The vendor's fourth-party exposure (the vendor's own subcontractors with relevant access) — the Interagency Guidance on Third-Party Relationships (June 2023) sets the risk-based fourth-party expectation; the artifact records the firm's visibility.

Treating SOC 2 Type II as a substitute for the firm's own evidence is a common failure mode. The artifact records SOC 2 status as one input among several.

#### Common pitfalls

- Asserting AAL2 without evidencing the authenticator type. SMS-OTP for first-factor reauthentication does not meet AAL2; the artifact records the gap.
- Reporting per-consumer scope enforcement as compliant when the API runtime returns the full data envelope and relies on the recipient to filter. The compliance is at the runtime, not at the recipient.
- Storing credentials in a hashed-but-recoverable form for legacy screen-scraping integrations and reporting the storage as compliant. The recoverability is the issue.
- Running consumer-revoked authorisations through the consent store without propagating to the active-token registry, the API runtime, or the credential-vault deletion. The deletion path must close end-to-end.
- Treating the federal banking agencies' 36-hour rule as the programme operator's clock rather than the sponsor bank's. The programme operator's clock is contractual.
- Omitting the §1033-implications row from the incident-response posture. Where authorisation flows or developer-interface tokens were affected, the data-rights frame implicates duties downstream of the cyber-event response.
- Treating SOC 2 Type II as a substitute for the firm's own evidence on vendor-managed key posture, vulnerability-management cadence, or incident-response cooperation terms.

## privacy

### Cross-cutting overlay — privacy

Required-on for every engagement run through this skill. Open banking is fundamentally a privacy domain: the data being shared is consumer financial data, the consumer's authorisation and revocation is the operative control, and the federal and state privacy frames sit alongside the data-rights frame as parallel duty sets that overlap but are not the same. This overlay is the artifact's largest cross-cutting block; it carries the federal privacy-notice posture, the state-privacy-law inventory, the dual-purpose consent stack, the retention and deletion duties, the secondary-use posture, and the signal-handling detail that the **privacy controls** named section reflects.

The overlay does not substitute for a privacy-counsel-led review of customer-facing notices, for a state-by-state privacy-law inventory across the firm's resident footprint, or for a data-mapping exercise. The pack records the supervisory-level controls posture and the evidence-of-oversight; deeper privacy work flows to the privacy office or to a counsel-led review.

#### Anchor frame

- **CFPB Personal Financial Data Rights Final Rule under §1033 of the Dodd-Frank Act** (October 22, 2024 — verify Federal Register citation, exact citation, implementation tier dates, and current docket status). The rule is the central anchor; the `s1033_status_note` block carries the firm-specific application.
- **GLBA Privacy Rule / Reg P, 12 CFR Part 1016**. Initial and annual privacy notices, sharing limits, opt-out mechanics. Applies where the firm is CFPB-supervised under the prudential framework.
- **FTC GLBA Privacy Rule, 16 CFR Part 313**. Applies where the firm is FTC-supervised.
- **GLBA Safeguards Rule, 16 CFR Part 314** as amended (FTC, December 2021 amendments effective 2023). The Safeguards Rule and the Privacy Rule sit as parallel federal duties; both apply to the same data.
- **California Consumer Privacy Act / California Privacy Rights Act** — Cal. Civ. Code §1798.100 et seq. Consumer rights to know, delete, correct, opt-out of sale and sharing; sensitive-personal-information limits; data-breach private right of action under specific conditions.
- **Rolling state-privacy-law landscape** — Virginia (VCDPA), Colorado (CPA), Connecticut (CTDPA), Utah (UCPA), Texas (TDPSA), Oregon (OCPA), Montana (MTCDPA), and others (verify currency on the analysis date). Each carries its own consumer-rights set, sensitive-data category, opt-out mechanics, and enforcement posture.
- **State breach-notification statutes** — state-by-state; verify per state in the firm's resident footprint.

#### §1033 status note

The `s1033_status_note` block is required and cannot be blank. It is the cross-skill contract; the same field structure propagates into any downstream artifact that touches the data-rights frame. The block carries:

- **`effective_date`** — the rule's effective date as cited in the Federal Register, with `[verify]` flag where the analysis date has not been re-checked.
- **`firm_implementation_tier`** — the firm's tier under the data-provider asset-size phase-in, with the tier's compliance date.
- **`litigation_status_as_of`** — date of the most recent docket check, with notes on any active litigation, stays, or compliance-date relief.
- **`notes`** — any firm-specific posture (early-adopter, lagging, BaaS-stack-coordinated, awaiting sponsor-bank readiness, screen-scraping migration in progress).

Defaulting the status note to "we will be ready" without naming the firm's tier and implementation-date posture is a finding. The block is structured, not narrative.

#### Federal privacy notices

The artifact's **privacy controls** block records:

- **Initial privacy notice content** (Reg P §1016.4 / FTC §313.4). Reviewed against the data-sharing flow: the categories of information collected, the categories of affiliates and non-affiliates with which information is shared, the categories of consumers, and the firm's policies and practices for protecting confidentiality and security. A notice drafted before the data-rights programme launched and not updated to reflect data-recipient flows is a frequent gap.
- **Annual privacy notice posture** (Reg P §1016.5 / FTC §313.5). The firm provides an annual notice unless an exception applies. The artifact records the exception posture and the annual-notice cadence where the exception does not apply.
- **Opt-out mechanics** (Reg P §1016.7 / FTC §313.7). Where the firm shares non-public personal information with non-affiliates outside the §502(e) exceptions, the opt-out mechanism applies. The data-rights frame's consumer-authorisation flow is not a substitute for the GLBA opt-out; the two run as parallel consumer-facing surfaces.

#### State privacy frame

The artifact records one row per state where the firm meets the comprehensive privacy law's threshold or the breach-notification statute applies. The block is not a single "state privacy" line; states behave differently and the artifact must keep them separate.

- **California CCPA / CPRA.** Consumer rights to know, delete, correct, opt-out of sale and sharing, opt-out of sensitive-data processing. Sensitive personal information includes financial-account data; the data-rights flow implicates the SPI category. Opt-out signals (Global Privacy Control) must be honoured. The data-breach private right of action under §1798.150 applies for unauthorised access and exfiltration of certain categories of personal information, subject to specific conditions.
- **Virginia, Colorado, Connecticut, Utah, Texas, Oregon, Montana.** Each carries its own consumer-rights set, sensitive-data category, opt-out mechanics, and enforcement posture (verify currency on the analysis date). The artifact records the state-by-state row with the firm's resident footprint, the rights set in scope, and the opt-out posture.
- **State breach-notification statutes** — one row per state where customer information was implicated and the state's notification trigger is met. Timing windows vary; the artifact records each state's clock separately. Defaulting to a single "USA" row is a finding.

#### Dual-purpose consent stack

The data-rights frame's consumer authorisation runs alongside the GLBA notice/opt-out frame and the state-privacy-law consent frame. The three are not interchangeable. The artifact records:

- The consumer-facing **authorisation flow** under the data-rights frame (scope, duration, revocation, reauthorisation). This is the data-rights-specific consent.
- The consumer-facing **GLBA notice** (initial and annual) and the **opt-out posture** (where applicable). This is the federal privacy frame's consent surface.
- The consumer-facing **state-privacy-law consent** (CCPA / CPRA opt-outs, sensitive-data limits, GPC signal handling; rolling state-law equivalents). This is the state frame's consent surface.

A common failure mode: rolling all three into a single "Privacy Policy" page with a checkbox at the bottom. The three serve different statutory frames with different content requirements; the artifact records each as a separate row with the named anchor and the evidence of operational delivery.

#### Retention and deletion duties

The artifact records the operational deletion path end-to-end:

- **Retention schedule** by data category (covered data under the data-rights frame; non-covered data subject to GLBA and state privacy frames). The schedule names the retention period and the legal basis.
- **Deletion-on-revocation path.** Consumer revokes authorisation; the data recipient stops collecting; the recipient runs the deletion job against its data store, against any analytics derivatives, against any vendor-managed copies, and against any backup-restore exclusions. The audit trail records each step. A revocation captured in the consent store but not enforced operationally is a finding.
- **Deletion-on-state-rights-request path.** Consumer exercises a state-law deletion right (CCPA / CPRA / VCDPA / etc.); the firm runs the same deletion job under the state-law rather than the data-rights basis. The two paths can converge on the same operational job; the artifact records both as covered.
- **Backup-restore posture.** Most firms exclude deleted records from backup-restore; the artifact records the exclusion mechanism and the named retention period for backup-only records.

Treating DPA contractual coverage as evidence of operational deletion is a frequent failure mode. DPA coverage is the contractual baseline; the artifact reconciles the contractual baseline against the operational deletion-job evidence.

#### Secondary-use posture

The data-rights frame places secondary-use restrictions on data recipients: the recipient may use covered data only for purposes the consumer authorised. Common secondary uses that require separate analysis:

- **Model training.** Using covered data to train fraud-detection models, underwriting models, recommendation engines. The artifact records whether the secondary use sits within the consumer-authorised scope, whether the firm has a separate consent for it, and whether the model-training pipeline runs on de-identified or aggregated data.
- **Benchmarking and analytics.** Using covered data to produce aggregate insights, benchmarks, or analytics products. The artifact records the de-identification posture (re-identification-resistance evidence) and the consumer-disclosure posture.
- **Marketing and cross-sell.** Using covered data to drive marketing or cross-sell. The data-rights frame is restrictive on this; the artifact records the consumer-consent basis and the §1033-specific limits.

A recipient that documents the secondary-use posture in the DPA but cannot evidence operational enforcement is a finding.

#### Signal handling

The artifact records the firm's handling of consumer privacy signals:

- **Global Privacy Control (GPC)** for state-law opt-outs (CCPA / CPRA mandates honouring the signal as an opt-out of sale and sharing; other state laws are converging).
- **Do-not-track and other browser signals** (informational; few statutes mandate honouring them).
- **Consumer-direct revocation requests** through the data-rights consent flow, the firm's privacy-rights portal, and any vendor-managed consent surface. The artifact records the routing and the operational deletion path for each surface.

A signal received at one surface that does not propagate to the operational deletion path at all data stores is a finding.

#### Vendor data-processing posture

Where the data flow runs through a vendor (aggregator, developer-portal vendor, consent-management vendor, identity vendor, fraud-decision vendor), the artifact's **vendor and fourth-party register** records:

- The vendor's **data-processing agreement (DPA)** coverage of the affected data category and the secondary-use scope (model-improvement, benchmarking, anonymous-aggregate use).
- The vendor's notification clock under the DPA and the vendor's actual notification posture.
- DPA-vs-actual reconciliation (the contractual baseline against the operational fact).
- The vendor's fourth-party exposure (the vendor's own subcontractors with relevant access) — the Interagency Guidance on Third-Party Relationships sets the risk-based fourth-party expectation.

#### Customer-notification posture for privacy-leg breaches

Where a breach in the data flow touches personal data, the artifact's customer-notification block records:

- **Notification content.** Tracks each state's content requirements (date of incident, nature of personal information involved, steps taken, advice on what the resident can do, contact information). Some states require specific language (e.g., on credit-monitoring offers).
- **Channel.** Tracks each state's channel requirements (substitute notice when direct notice is impracticable; specific direct-notice methods). Email is permitted in many states but not all.
- **The data-rights-specific posture.** Where the breach implicates the data-rights consent flow (e.g., unauthorised access to the consent store, unauthorised token issuance), the artifact records the §1033-implications row and the cross-link to `payment-operations-incident-review`.

Vague language ("we are addressing a security matter") is a finding; state AG offices have pursued under-disclosed customer notifications.

#### Common pitfalls

- Treating GLBA as the only privacy frame and missing the state regimes in CA, VA, CO, CT, UT, TX, OR, MT, and other states where the firm meets the threshold.
- Rolling the data-rights authorisation flow, the GLBA notice/opt-out, and the state-privacy-law consent into a single "Privacy Policy" surface. The three serve different statutory frames.
- Defaulting the §1033 status note to "we will be ready" without naming the firm's tier and implementation-date posture.
- Treating DPA contractual coverage as evidence of operational deletion. DPA coverage is the baseline; operational deletion-job evidence is the test.
- Documenting secondary-use restrictions in the DPA without evidencing operational enforcement (model-training-pipeline scope, benchmarking-derivative posture, marketing-use posture).
- Storing the consumer-revocation event in the consent store without propagating to the data store, the analytics derivatives, the vendor-managed copies, and the backup-restore exclusions.
- Failing to honour the Global Privacy Control signal for CCPA / CPRA opt-outs.
- Drafting customer-notification text against a single state's content requirements when the affected population spans multiple states.
- Treating the data-rights frame and the GLBA Safeguards Rule as the same control set. They overlap on encryption, MFA, monitoring, and incident response, but the data-rights frame adds authorisation, scope, duration, revocation, secondary-use limits, and reauthorisation cadence as duties the Safeguards Rule does not carry.
