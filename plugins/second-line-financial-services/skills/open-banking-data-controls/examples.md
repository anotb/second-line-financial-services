# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## account-aggregator-screen-scraping-migration-to-api-tokenised-access

### Example: account aggregator (data recipient) migrating screen-scraping integrations to API-tokenised access

#### Input description

A US account aggregator running PFM and lending-underwriting feeds for a portfolio of fintech recipients is migrating its data-provider integrations from credential-based screen scraping to API-tokenised access. The firm runs as a data recipient under the personal-financial-data-rights frame. It has 14 active screen-scraping integrations against banks and fintechs that have not yet exposed a developer interface, hashed-but-recoverable credentials in a vendor-managed vault for those integrations, no end-to-end deletion path for consumer-revoked authorisations on the legacy integrations, and a consumer-facing scope description in its app that is broader than the actual data flow for several integrations. The firm is preparing for its second-line review ahead of a downstream lender's vendor-diligence cycle.

The engagement was scoped at connector-aware posture (the firm has system-of-record access for token-issuance logs, consent-store audit trail, and deletion-job records). The audience is the firm's second-line lead and the downstream lender's TPRM team for the vendor-diligence-cycle review.

#### Output sketch

The pack opens with a **programme summary** naming the firm role (data recipient; aggregator), the products consuming the feed (PFM, lending-underwriting), the consumer base, the data-provider integrations (mix of API-tokenised and legacy screen-scraping), and the downstream-recipient portfolio.

The **current-state regulatory frame** carries the structured `s1033_status_note` block: the effective date with `[verify]` flag re-checked on the engagement date; the firm's posture as a data recipient (the implementation-tier dates phase data-provider obligations; data-recipient duties apply earlier on consumer-permissioned flows); the docket-status note as of the engagement date; the firm-specific notes (screen-scraping migration in progress; legacy-integration credential-vault retirement on a 12-month roadmap).

The **data-recipient duties** block fires:

- Collection limits: the firm collects only authorised data on API-tokenised integrations; on legacy screen-scraping integrations, the data envelope is broader than the consumer-facing scope description. Finding recorded.
- Use limits: PFM and lending-underwriting are the authorised purposes; secondary use for analytics-derivative production runs on de-identified aggregated data. The de-identification posture is reviewed and current.
- Secondary-use posture: model-training pipeline runs on de-identified data; benchmarking products run on aggregated data; marketing posture is opt-in only. The DPA-vs-actual reconciliation is current.
- Retention schedule: 24-month retention by category; legacy-integration retention reviewed against the rule's "reasonably necessary" standard; finding recorded for one category that exceeds the necessary-period.
- Deletion-on-revocation operational path: API-tokenised integrations have an end-to-end deletion path; legacy screen-scraping integrations have a partial path (consent-store revocation propagates to the data store but not to the credential vault). Finding recorded as a critical gap.
- Reauthorisation cadence: the firm runs a 12-month consumer-facing reauthorisation surface; reauthorisation flow re-establishes authentication at the same AAL.
- Downstream sharing: the firm shares with downstream lender-recipients under DPAs that mirror the upstream consent scope; DPA-vs-actual reconciliation is current.
- Consumer-facing scope language vs actual data flow: the scope description in the firm's app is broader than the actual flow for three legacy integrations and matches the actual flow for the API-tokenised integrations. Finding recorded.

The **screen-scraping migration plan** is the artifact's centre of gravity:

- **Credential-storage inventory**: 14 active integrations, hashed-but-recoverable credentials in a vendor-managed vault; the vault's recoverability is the issue. Vault rotation cadence quarterly.
- **Deprecation roadmap**: 9 integrations with target migration dates within 12 months; 5 integrations awaiting data-provider-side developer-interface readiness; sponsor-bank coordination not applicable (the firm is not a sponsor-bank programme on the recipient side).
- **Fallback posture**: dual-write during the API ramp for 6 integrations; API-only for 3; active screen-scraping during ramp for 5 awaiting provider readiness.
- **Customer-impact assessment**: re-onboarding required for the 9 in-progress integrations; broken-connection risk recorded with the customer-communications plan.

The **cyber controls on the data flow** block carries:

- Token lifecycle for the API-tokenised integrations: OAuth 2.0 with PKCE for consumer-facing flows; FAPI 2.0 message-signing for high-value scopes; refresh-token expiry tied to the 12-month reauthorisation cadence.
- Token revocation propagation: end-to-end on API-tokenised integrations; partial on legacy integrations (the credential-vault deletion lags). Finding recorded.
- Authentication assurance level (consumer-side): AAL2 with phishing-resistant authenticator types; evidence reviewed.
- Monitoring on the developer interface side and the legacy-integration side: anomaly detection on both; alert-investigation cadence current.

The **privacy controls** block fires the largest finding set, because the firm is a data recipient and the privacy frame layers on top of the data-rights frame:

- Federal privacy notice content: current; data-recipient flows reflected.
- State-privacy-law inventory: CA / VA / CO / CT / UT / TX / OR / MT in scope (verify currency on the engagement date).
- Dual-purpose consent stack: three surfaces (data-rights authorisation, GLBA notice, state-privacy-law consent) with three separate content sets; reviewed and current.
- Retention and deletion duties: the deletion-on-revocation operational path gap on legacy integrations is the largest finding; recorded as critical.
- Secondary-use posture: model-training, benchmarking, and marketing rows reviewed; DPA-vs-actual reconciliation current.
- GPC signal handling: honoured for CA/CCPA opt-outs.
- Vendor DPA-vs-actual reconciliation: 12 vendor relationships reviewed; one DPA-vs-actual gap recorded.

The **vendor and fourth-party register** carries the credential-vault vendor (legacy), the authorisation-server vendor (current), the consent-management vendor, the identity vendor, the fraud-decision vendor, and the data-provider integrations as upstream relationships with criticality flags.

The **gaps** block elevates three to issue level: deletion-on-revocation operational path on legacy integrations (critical), consumer-facing scope description vs actual flow on three legacy integrations (high), and the credential-vault retirement timeline (high; the 12-month roadmap is reasonable, but the interim posture is the issue).

The **recommended disposition** is `remediate_then_re_review`. The conditions block names the three issues that must close before re-review.

#### Why this scenario matters

The scenario tests the most-frequent findings on the data-recipient side: the deletion-on-revocation operational path (the contractual baseline and the operational job often diverge), the consumer-facing scope description vs the actual flow (legacy integrations carry envelopes broader than the consent language), and the credential-vault retirement (hashed-but-recoverable credentials are still credentials, and reporting "vaulted" as compliant is a frequent failure). It also exercises the screen-scraping migration plan as the artifact's centre of gravity and the dual-purpose consent stack discipline (data-rights, GLBA, and state-privacy-law are three separate frames).

The scenario uses only public-source-derived material. CFPB and FTC enforcement actions in the aggregator and credential-storage space establish the conceptual fact pattern; no named institution is used in the artifact narrative.

## data-provider-readiness-ahead-of-implementation-tier-date

### Example: mid-tier data-provider fintech preparing developer-interface and authorisation stack ahead of its implementation-tier date

#### Input description

A mid-tier programme operator running a consumer neobank on a BaaS sponsor-bank stack is preparing for its data-provider implementation-tier date under the personal-financial-data-rights frame. The firm is a data provider for checking-equivalent and credit-card-equivalent products; it currently exposes a partner-portal API to a small set of aggregator-recipients but does not enforce per-consumer authorisation scope at the API runtime, charges aggregators a per-call fee, and has no documented one-year reauthorisation mechanism. The sponsor bank's TPRM team has scheduled a controls-inventory review.

The engagement was scoped at public-plus-firm-policy-plus-evidence posture. The audience is the sponsor-bank operating committee for the readiness review, with a parallel artifact for the firm's internal-audit retrospective.

#### Output sketch

The pack opens with a **programme summary** naming the firm role (data provider), the products in scope (consumer asset accounts under the consumer-EFT regime; credit-card-equivalent product under the credit-card regime), the consumer base, the integrated aggregators, and the sponsor-bank programme name.

The **current-state regulatory frame** carries the structured `s1033_status_note` block: the effective date with `[verify]` flag re-checked on the engagement date; the firm's tier date under the asset-size phase-in; the docket-status note as of the engagement date (with notes on the litigation history and any compliance-date relief); the firm-specific notes (BaaS-stack-coordinated; sponsor-bank readiness on the depository side; partner-portal API legacy posture). The block propagates into the artifact's source-citations footer.

The **data-provider scope** block carries the covered-data inventory (transaction data, account balance, configuration data, payment-initiation information; verified against the published rule), the in-scope account types (consumer asset accounts; the credit-card-equivalent product), and the out-of-scope items with rationale.

The **developer-interface posture** block fires the gaps:

- Per-consumer scope enforcement at the API runtime: gap. The partner-portal API returns a fixed data envelope and relies on the recipient to filter. Migration-path commitment recorded.
- Free-access posture: gap. The firm charges aggregators a per-call fee. The rule prohibits charging consumers or authorised third parties for access; the fee structure must change before the tier date. Recorded as a finding with target-close date.
- Documentation, sandbox, conformance testing: partial. Sandbox available; conformance testing against the FDX message-structure profile not yet completed.
- Third-party developer-portal vendor: in scope. The vendor is recorded in the **vendor and fourth-party register** with criticality flag.

The **authorisation, scope, duration, revocation** block fires:

- Consumer-facing scope language vs actual data flow: the scope description in the consent flow is broader than the actual data envelope returned by the partner-portal API. Recorded as a finding (worse failure mode: actual flow broader than scope language; this is the inverse, but still a finding).
- One-year reauthorisation cadence: not implemented. The firm relies on aggregator-side periodic re-prompting rather than a data-provider-enforced reauthorisation surface. Migration-path commitment recorded.
- Revocation propagation: provider stops on revocation; recipient-stop and deletion-runs evidence not aggregated into a single audit feed. Migration-path commitment recorded.

The **data-recipient screening** block carries the third-party authorisation conditions the firm applies to recipients (basic certification collected; ongoing monitoring posture light) with the tie-back to the firm's TPRM lifecycle.

The **cyber controls on the data flow** block carries:

- Encryption in transit: TLS 1.2+ with mutual-TLS for the partner-portal API; gap on FAPI message-signing posture for high-value scopes.
- Token issuance: programme-operator-side; OAuth 2.0 authorisation-code flow; FAPI 1.0 not yet adopted. Recorded as a migration commitment.
- Token scope enforcement: gap (per the developer-interface row above).
- Authentication assurance level (consumer-side): AAL2 asserted; evidence reviewed (TOTP authenticator app plus password); meets the floor.
- Monitoring on the developer interface: anomaly detection at the API gateway; alert-investigation cadence acceptable.

The **privacy controls** block carries the federal initial privacy notice content (reviewed and current; data-recipient sharing categories listed), the annual privacy notice posture (delivered on cadence), the state-privacy-law inventory (one row per state in the firm's resident footprint; CA / VA / CO / CT / UT in scope; verify currency on the engagement date), the dual-purpose consent stack (data-rights authorisation, GLBA notice, state-privacy-law consent: three separate surfaces with three separate content sets), and the GPC signal handling posture (honoured for CA/CCPA opt-outs).

The **vendor and fourth-party register** carries the sponsor bank, the developer-portal vendor, the authorisation-server (in-house), the consent-management vendor, the identity vendor, the fraud-decision vendor, and three named aggregator-recipients with criticality flags and evidence-of-oversight references.

The **self-evidence index** carries the artifact list mapped to each control section; the freshness flags surface three stale items that need refresh ahead of the tier date.

The **gaps** block elevates four to issue level: free-access posture, per-consumer scope enforcement at the API runtime, one-year reauthorisation cadence, and FAPI message-signing posture for high-value scopes. Each carries severity, owner role, target close date, and escalation path.

The **recommended disposition** is `remediate_then_re_review`. The conditions block names the four issues that must close before re-review.

#### Why this scenario matters

The scenario tests three of the most-frequent findings on the data-provider side: the free-access posture (charging aggregators is a frequent legacy practice that does not survive the tier date), per-consumer scope enforcement at the API runtime (legacy partner-portal APIs return fixed envelopes), and the one-year reauthorisation cadence (most data providers had no such surface before the rule). It also exercises the `s1033_status_note` block discipline (the litigation history, the firm's tier date, the engagement-date verification) and the FAPI / authentication-assurance-level discipline (asserting AAL2 with evidence, not just policy).

The scenario uses only public-source-derived material. CFPB final rule text and supervisory signal establish the conceptual fact pattern; no named institution is used in the artifact narrative.

## troubleshooting

### Troubleshooting: open-banking-data-controls

Recurring pitfalls. Read before drafting if the engagement looks unfamiliar; consult after drafting if the artifact does not feel right to a senior payments-compliance reviewer or to a sponsor-bank programme-management reader.

#### Categorical "covered data" answers

Symptom: the data-provider scope block carries a single sentence asserting that "all consumer transaction data is covered" or "balance and transaction data are in scope" without the row-by-row inventory.

Why it fails: the rule's covered-data list is granular against the firm's specific account scope. Different account types carry different covered-data sets; a credit-card-equivalent product and a consumer asset account do not have the same scope. A categorical assertion is an examiner-friendly target; it also pre-commits the firm on edge cases (e.g., configuration data, stored payment instruments, payment-initiation information) that the rule treats specifically.

Fix: the data-provider scope block carries a row-by-row covered-data inventory against the firm's account scope, with each row's in-scope flag verified against the published rule and the firm's product configuration. Out-of-scope items carry a rationale row.

#### Treating screen scraping as fine because it has been in production for years

Symptom: the screen-scraping migration plan block is empty, abbreviated, or framed as a footnote. The credential-storage inventory is missing or carries a single-line "vaulted" entry without recoverability detail.

Why it fails: the migration off credential-based screen scraping is the artifact's centre of gravity for any firm with legacy integrations. The rule explicitly contemplates the migration; the supervisory signal in CFPB and FTC actions establishes the credential-storage failure mode. Hashed-but-recoverable credentials are still credentials; reporting the storage as "vaulted" without addressing recoverability is a finding.

Fix: the screen-scraping migration plan block carries the credential-storage inventory (where credentials sit, encryption posture, vault rotation cadence), the deprecation roadmap (one row per legacy integration, with target migration date and status), the fallback posture during the migration window, the customer-impact assessment, and the sponsor-bank coordination posture where applicable. Where the inventory is empty, the block records "no legacy screen-scraping integrations" with the basis.

#### Per-consumer scope enforcement at the recipient rather than at the API runtime

Symptom: the developer-interface posture block reports per-consumer scope enforcement as compliant, but the API runtime returns a fixed data envelope and the recipient is expected to filter to the consumer-authorised subset.

Why it fails: the rule places per-consumer scope enforcement at the data provider's API runtime, not at the recipient. A fixed-envelope API that relies on the recipient to filter is a finding regardless of whether the recipient does the filtering correctly. The compliance test is at the runtime.

Fix: the developer-interface posture block records the per-consumer scope enforcement row honestly. Where the API runtime does not enforce, the row records the gap and the migration-path commitment; the gap rolls into the gaps block with severity, owner, and target-close date.

#### Conflating Safeguards with the data-rights frame

Symptom: the artifact treats GLBA Safeguards controls and the data-rights frame as a single undifferentiated control set. The cyber-controls block and the privacy-controls block carry the same row set.

Why it fails: the federal Safeguards Rule and the data-rights frame overlap on encryption, MFA, monitoring, and incident response, but the data-rights frame adds authorisation, scope, duration, revocation, secondary-use limits, and reauthorisation cadence as duties the Safeguards Rule does not carry. A Safeguards-compliant programme is not automatically data-rights-compliant; a gap in one is not automatically a gap in the other.

Fix: the cyber-controls block records the security posture (encryption, MFA, monitoring, incident response). The data-provider scope block, the developer-interface posture block, the authorisation-controls block, and the data-recipient duties block record the data-rights-specific duties separately. The privacy-controls block records the privacy-specific duties. Cross-references between blocks are explicit; the duty sets do not collapse into one row set.

#### §1033 status note left as marketing copy

Symptom: the `s1033_status_note` block carries narrative language ("the firm is preparing for §1033", "we will be ready", "compliance roadmap in flight") without the structured field set.

Why it fails: the field is structured by design. Downstream consumers (vendor-diligence packs, incident reviews, privacy reviews) read the block directly; narrative language does not propagate. The rule's docket has been active since finalisation, and the date-stamp on the verification is load-bearing for any artifact claiming the firm's posture.

Fix: the block carries the four structured fields. `effective_date` with the Federal Register effective date and the `[verify]` flag where the analysis date has not been re-checked. `firm_implementation_tier` with the tier under the asset-size phase-in and the tier's compliance date. `litigation_status_as_of` with the date of the most recent docket check. `notes` with firm-specific posture. The block repeats verbatim in the source-citations footer.

#### Dropping the developer-portal vendor from the fourth-party register

Symptom: the vendor and fourth-party register lists the sponsor bank, the aggregators, and the identity vendor, but does not list the developer-portal vendor that hosts the API documentation, the sandbox, and (often) the key issuance.

Why it fails: the developer-portal vendor sits in the data path. The vendor manages keys, hosts documentation that consumers may rely on, and runs the sandbox that recipients certify against. The Interagency Guidance on Third-Party Relationships (June 2023) sets the risk-based fourth-party expectation; missing the portal vendor is a TPRM gap regardless of whether the data flows through it directly.

Fix: the vendor and fourth-party register carries one row for the developer-portal vendor (function, criticality, evidence-of-oversight reference). Where the function is split across multiple vendors (documentation vendor, key-issuance vendor, authorisation-server vendor), each is a separate row.

#### Mixing data-provider duties and data-recipient duties for both-sides firms

Symptom: a both-sides firm produces a single undifferentiated controls inventory mixing data-provider duties (developer interface, authorisation, third-party screening) and data-recipient duties (collection limits, retention, deletion-on-revocation, secondary use).

Why it fails: the duty sets are separate. The recommended disposition can differ across the two sides. Mixing them hides which side has gaps and which side is ready.

Fix: a both-sides firm produces two parallel control families with a shared current-state regulatory frame, shared cyber and privacy overlays, a shared vendor register, and a shared `s1033_status_note` block. Each side has its own self-evidence index, gaps row, and recommended disposition. The recommended dispositions are recorded separately in the artifact.

#### Treating FDX alignment as compliance

Symptom: the artifact frames FDX-aligned message structure as evidence of compliance with the data-rights frame.

Why it fails: FDX is the de facto US industry standard. Alignment is supervisory expectation, not a legal obligation by itself. A firm that aligns to the FDX message structure but does not enforce per-consumer scope, does not propagate revocation, or charges for access is not compliant regardless of the FDX-alignment row.

Fix: the artifact distinguishes FDX alignment (an industry-standard implementation pattern) from compliance with the data-rights frame (the operative legal duty set). The developer-interface posture block records FDX alignment as one row; the rule-specific duties (per-consumer scope, free access, authorisation, revocation) carry their own rows.

#### Default-to-USA on the state-privacy-law inventory

Symptom: the privacy-controls block carries a single "USA" or "state privacy" line for the state-privacy-law inventory.

Why it fails: state privacy laws diverge on consumer rights, sensitive-data category, opt-out mechanics, signal-handling, and enforcement. CCPA / CPRA differs from VCDPA differs from CPA differs from CTDPA. A default-to-USA row hides the state-by-state work an examiner or state AG will look for.

Fix: one row per state where the firm meets the comprehensive privacy law's threshold or the breach-notification statute applies. The block names the firm's resident footprint, the rights set in scope by state, the opt-out posture, and the signal-handling posture. Verify currency on the analysis date.

#### Reauthorisation flow that drops authentication assurance

Symptom: the authorisation-controls block reports the one-year reauthorisation cadence as compliant; the cyber-controls block reports AAL2 for the consumer-facing flow. The reauthorisation flow itself runs on a magic link without a second factor.

Why it fails: the reauthorisation should re-establish authentication at the same AAL as the initial authorisation. A magic-link reauthorisation does not meet AAL2 because the authenticator type does not resist phishing in the same way. The artifact rows are consistent on paper but inconsistent in operation.

Fix: the authorisation-controls block records the reauthorisation cadence and the authentication-assurance posture in the reauthorisation flow. The cyber-controls AAL row reconciles against the reauthorisation flow specifically; a reauthorisation that drops AAL is recorded as a finding.

#### DPA contractual coverage as evidence of operational compliance

Symptom: the data-recipient duties block reports operational compliance on collection limits, secondary use, retention, and deletion-on-revocation by citing the DPA.

Why it fails: DPA coverage is the contractual baseline. Operational evidence is the test. A DPA that contractually restricts secondary use to model improvement is not evidence that the model-training pipeline runs on de-identified data; a DPA that contractually requires deletion-on-revocation is not evidence that the deletion job runs and closes against the data store, the analytics derivatives, and the vendor-managed copies.

Fix: each row in the data-recipient duties block carries the DPA-vs-actual reconciliation. The DPA reference and the operational evidence reference both appear; where the operational evidence is missing, the row is `[evidence needed]` and the gap rolls into the gaps block.

#### Engagement scope absent and not flagged

Symptom: the artifact reads as if a formal scope record were on file when it was not.

Why it fails: downstream skills key off the scope record (institution type, primary regulators, sector overlay set, persona, source posture). When scope was not formalised, the pack must say so; otherwise downstream consumers (`fintech-partner-controls` updating after this review, `payment-operations-incident-review` cross-linking on a subsequent incident, `vendor-diligence` running on an aggregator-recipient) cannot calibrate.

Fix: when the practitioner did not supply a formal scope record, ask the questions in the SKILL's "Ask first" section and default to public posture if the practitioner declines. Note in the artifact that scope was not formalised; do not silently apply a default.
