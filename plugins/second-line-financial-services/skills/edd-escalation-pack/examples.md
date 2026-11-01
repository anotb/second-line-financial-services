# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## foreign-correspondent-respondent-bank-higher-risk-jurisdiction

### Example: foreign correspondent account with a small respondent bank in a higher-risk jurisdiction

Public-source-derived. No named institution. The shape mirrors a standing pattern in regional-bank correspondent-banking businesses: a Section 312 EDD pack on a foreign correspondent account for a small respondent bank in a higher-risk jurisdiction (per FATF mutual-evaluation public reports for that jurisdiction), where nested-correspondent disclosure has historically been incomplete and the sanctions-exposure-through-respondent-customer-base read has not been quantified.

#### Input

- **Institution**: a regional US bank with a correspondent-banking business; primary regulators include the OCC and FinCEN.
- **Customer**: a foreign respondent bank in a higher-risk jurisdiction. Account opened seven years ago.
- **Pack inputs (as presented for QA)**:
  - Respondent ownership: foreign holding company structure with two layers of ownership; ownership has changed once during the relationship (publicly reported).
  - Respondent's products and services to non-US persons: documented at original onboarding; a recent expansion into a payable-through-account-adjacent product line is on file but not refreshed in the EDD pack.
  - AML/CFT regime in respondent's home country: per FATF mutual-evaluation public report for that jurisdiction (recent report).
  - Respondent's regulatory standing: per home-country regulator's public registry; current; one historical supervisory action publicly reported, closed.
  - Respondent's CBDDQ on file (Wolfsberg format): completed at last refresh 24 months ago; one open question on nested-correspondent disclosure left blank in the prior CBDDQ.
  - Public information on the respondent: enforcement history, news coverage, ownership changes, sanctions exposure indicators — outside-in read available.
  - Nested-correspondent posture: respondent has acknowledged providing correspondent services to other banks; the disclosure on its downstream customer-base by jurisdiction is incomplete on the file.
  - Sanctions exposure through respondent's customer base by jurisdiction: not quantified on the file.
  - Volume and pattern of transactions through the respondent: documented; pattern shows concentration on cross-border wire activity into and out of the respondent's home jurisdiction and into two adjacent higher-risk jurisdictions.
  - Adverse media on the respondent: triaged hit from `negative-news-triage` on a media report concerning the respondent's customer base in a sanctions-adjacent jurisdiction; materiality "moderate", linkage confidence "medium".
  - Sanctions screening: clear at current scan on the respondent itself; multiple historical hits on connected counterparties resolved over the lookback.
- **Engagement scope supplied**: institution = regional US bank correspondent-banking business; primary regulators = OCC, FinCEN; persona = second-line EDD reviewer reporting to the BSA officer; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlay = banking; cross-cutting overlays = none (conduct not loaded — relationship is institution-to-institution; no retail-customer-conduct nexus).
- **Pack type**: periodic_refresh.
- **EDD trigger**: correspondent + high_risk_jurisdiction.

#### Output sketch

The skill produces an EDD pack against the file. Headlines:

- **Background and EDD trigger** — periodic refresh on the Section 312 foreign-correspondent EDD frame; trigger combines correspondent and high-risk-jurisdiction. Cross-references upstream `cdd-risk-review` record and the `negative-news-triage` triaged hit on the respondent's customer base.
- **Beneficial ownership and control chain** (respondent ownership) — two-layer foreign holding structure walked; ownership change during the relationship is documented; current ownership corroborated against the home-country registry where the registry is publicly accessible.
- **Derogatory information and adverse media** — one moderate hit consumed from `negative-news-triage` on the respondent's customer base in a sanctions-adjacent jurisdiction; pattern observation: the hit is consistent with the public-source posture on that jurisdiction's correspondent-banking risk profile but does not implicate the respondent's program directly.
- **PEP, sanctions-adjacency, and high-risk-jurisdiction posture** — PEP status: not applicable on the institutional customer; PEP framing applies to the respondent's named control parties (one named control party is reported in the home country's public political register; PEP-adjacent). Sanctions-adjacency: through respondent's customer base by jurisdiction (the load-bearing concern). High-risk-jurisdiction nexus: respondent is headquartered in a higher-risk jurisdiction per the FATF mutual-evaluation public report; transactional pattern concentrates flow into the home jurisdiction and two adjacent higher-risk jurisdictions.
- **Source of wealth and source of funds** — `§1010.620`-style SoW / SoF framing does not apply directly to a foreign-correspondent customer; the pack reads the funding pattern of the correspondent relationship instead (transactional flow, settlement pattern, fee arrangements).
- **Customer rationale and expected vs. actual activity** — relationship rationale documented at original onboarding (USD clearing for the respondent's customer base). Expected activity profile predates the recent payable-through-account-adjacent product expansion. Actual activity is consistent with the original profile on the legacy product set; the new product line introduces a deviation the file does not address. Cross-reference to `aml-model-monitoring` for the new-product monitoring scope.
- **Sanctions screening posture** — current clear on the respondent; multiple historical connected-party hits resolved with disposition rationale on file (cross-reference to `sanctions-screening-qa`). List coverage: OFAC SDN, OFAC sectoral, UN, internal lists; `sanctions-screening-qa` cyber overlay relevant for the virtual-asset-service-provider posture of any of the respondent's downstream customers.
- **Conduct-risk indicators** — conduct overlay not loaded; institution-to-institution correspondent relationship without a retail-customer-conduct nexus.
- **Ongoing monitoring plan** — recommended scenarios: cross-border wire pattern, jurisdictional concentration, payable-through-activity (newly relevant given the product expansion), nested-correspondent transactional indicators. Refresh-cycle interval recommended: 12 months given the elevated combined trigger, with event-driven trigger on any further adverse-media activity on the respondent or its customer base.
- **Open issues, evidence-needed items, and committee questions**:
  - Ownership: nothing open at this refresh; ownership chain corroborated.
  - Section 312 elements: nested-correspondent disclosure — `[evidence needed]`; specifically the respondent's downstream correspondent customer base by jurisdiction at named granularity.
  - Section 312 elements: sanctions exposure through respondent's customer base by jurisdiction — `[evidence needed]`; quantified read at named-jurisdiction granularity.
  - Activity: the new payable-through-account-adjacent product line — owner: relationship owner; the EDD evidence on the product expansion has not been gathered.
  - Conduct: not in scope here.
  - Sanctions: connected-party screening on the respondent's downstream customer base flagged via the new-product expansion — owner: sanctions officer.
- **Recommended human-review gates and decision options** — gate: EDD committee review, composition includes BSA officer, CCO, sanctions officer, head of correspondent banking, legal, relationship owner. Decision options: retain_with_conditions; retain_with_enhanced_monitoring; retain_pending_further_evidence (improved nested-correspondent disclosure within X cycles; transaction-volume cap pending the disclosure); restrict_products_or_volumes (cap on the new product line until the EDD evidence on the expansion is gathered); escalate_to_relationship_exit_deliberation. Stop conditions: nested-correspondent disclosure remains incomplete after the second cycle; sanctions exposure through downstream customer base surfaces at material levels; respondent's regulatory standing changes adversely. Cross-references to `cdd-risk-review`, `negative-news-triage`, `sanctions-screening-qa`, `aml-model-monitoring`. The pack does not retain, restrict, or exit; the committee decides.
- **Sign-off and source trace** — drafter: second-line EDD reviewer; reviewer: BSA officer; approver: EDD committee chair. Source trace anchors to `references/source-anchors.md` (FFIEC correspondent section, `§1010.610`, 31 USC §5318(i), Wolfsberg CBDDQ as public industry standard), `references/sector-overlays.md#banking` (Section 312 EDD-element walk).
- **Confidence label** — `medium`. The `§1010.610` element-by-element walk is at high confidence on the file evidence for ownership, regulatory standing, and home-country regime; at medium confidence on the products-and-services-to-non-US-persons element pending the new-product EDD evidence; at low confidence on the nested-correspondent disclosure and the sanctions-exposure-through-customer-base elements (these are the load-bearing gaps).

#### Why this scenario matters

- **The Section 312 EDD elements are walked one by one.** A foreign-correspondent EDD pack that summarises the rule's elements without walking each one against the file has under-read the work. The pack's section on Section 312 elements forces the walk.
- **Nested-correspondent disclosure is the dominant defect on foreign-correspondent EDD packs.** The respondent's downstream customer base by jurisdiction is what carries the indirect exposure; an incomplete disclosure is a load-bearing finding.
- **Sanctions exposure through the respondent's customer base is not the same as sanctions screening of the respondent itself.** The pack reads both; clear screening of the respondent does not close the customer-base-exposure question.
- **CBDDQ is one input, not standalone evidence.** A completed CBDDQ with an open question on nested-correspondent disclosure left blank in the prior cycle is itself a finding.
- **Product expansion during the relationship reshapes the EDD profile.** The new payable-through-account-adjacent product line introduces a new EDD element and new monitoring scope; the pack reads the post-expansion profile, not the original profile.
- **The pack stops at the recommendation.** Retention with conditions, restriction on the new product line, escalation to exit deliberation are decision options the committee evaluates; the pack does not retain, restrict, or exit.

#### Anchors

- FFIEC BSA/AML Examination Manual — Correspondent Accounts (Foreign), Customer Due Diligence sections [verify section anchors].
- 31 CFR §1010.610 — Section 312 EDD on foreign correspondent accounts [verify section].
- 31 USC §5318(i) — Section 312 statutory underpinning.
- Wolfsberg Correspondent Banking Due Diligence Questionnaire (CBDDQ) (most recent public version; public industry standard reference).
- FATF mutual-evaluation public report for the respondent's jurisdiction (consulted as outside-in read on regime effectiveness).

See `references/source-anchors.md` for full citations and `references/sector-overlays.md#banking` for the bank-specific Section 312 walk.

## private-banking-pep-family-foreign-procurement

### Example: private-banking PEP-family customer with foreign-procurement adverse media

Public-source-derived. No named institution or named natural person. The shape mirrors a standing pattern at mid-sized US bank private-banking businesses: a long-tenured non-US-person private-banking customer who is an immediate family member of a senior foreign government official, with an EDD pack last refreshed 30 months ago, periodic cycle now due, and a recent media report on the family member's involvement in a foreign-procurement matter.

#### Input

- **Institution**: a mid-sized US bank private-banking business; primary regulator the OCC for this example; FFIEC manual frames examiner expectations.
- **Customer**: non-US person; immediate family member of a senior foreign government official; PEP-adjacent under FFIEC manual and Wolfsberg PEP guidance. Account opened five years ago in the bank's private-banking program. Funded by inbound wires routed through a foreign correspondent.
- **Pack inputs (as presented for QA)**:
  - Beneficial ownership: customer is the natural-person account holder; ownership chain runs through two foreign holding entities the customer controls; one foreign trust intermediary appears as ultimate beneficial recipient on a recent distribution.
  - SoW statement on file: customer-attested family-trust distribution; corroboration on file is one prior-firm reference and a copy of the trust deed (translated extract).
  - SoF on inbound wires: routed through one foreign correspondent in a higher-risk jurisdiction.
  - Adverse media: a triaged hit from `negative-news-triage` (recent media report on the family member's involvement in a foreign-procurement matter), materiality marked "material", linkage confidence "high".
  - Sanctions screening: clear at current scan; one historical hit on a connected party resolved with disposition rationale on file.
  - Expected vs. actual activity: expected profile from original onboarding documents wire activity within a defined band; actual activity over the lookback exceeds the band on volume and on counterparty concentration.
  - Conduct overlay: foreign-procurement exposure on the family member triggers the conduct lens.
- **Engagement scope supplied**: institution = mid-sized US bank private-banking business; primary regulators = OCC, FinCEN; persona = second-line EDD reviewer reporting to the BSA officer; source posture = public-plus-firm-policy-plus-system-of-record-evidence; sector overlay = banking; cross-cutting overlays = conduct.
- **Pack type**: periodic_refresh (with material change since last refresh).
- **EDD trigger**: pep + private_banking.

#### Output sketch

The skill produces an EDD pack against the file. Headlines:

- **Background and EDD trigger** — periodic refresh on the PEP-family / private-banking trigger; material change since last refresh is the new adverse-media report on the family member's foreign-procurement exposure. Cross-references upstream `cdd-risk-review` record and the `negative-news-triage` triaged hit.
- **Beneficial ownership and control chain** — three layers walked: customer (control); two foreign holding entities (ownership at named jurisdictions); foreign trust intermediary at the recent-distribution layer. Residual uncertainty on the trust intermediary's control parties (trust deed extract is partial; corroboration on the protector / trustee role is thin).
- **Derogatory information and adverse media** — one material hit consumed from `negative-news-triage` (foreign-procurement reporting on the family member; high linkage confidence; recent date). Pattern observation: the hit is the first publicly reported derogatory information on the customer's connected parties; no clustering yet.
- **PEP, sanctions-adjacency, and high-risk-jurisdiction posture** — PEP status: family_close_associate; source of finding: customer disclosure at onboarding plus commercial PEP-screening-tool corroboration; date of latest assessment: this refresh. The PEP role is named; the principal jurisdiction is named. Sanctions-adjacency: connected-party historical hit was resolved; current scan clear. High-risk-jurisdiction nexus: principal residence and source-of-funds origin in a higher-risk jurisdiction per FATF mutual-evaluation public report; transactional corridor concentrated to that jurisdiction.
- **Source of wealth and source of funds** — SoW: family-trust distribution; corroboration confidence is "low" on this refresh. Trust deed extract on file is partial; one prior-firm reference is on file but is dated; no independent public-source corroboration of the trust's underlying assets or distribution history. Residual gap: independent corroboration of the SoW statement. SoF: inbound wires through a foreign correspondent; corroboration on the originating account is thin.
- **Customer rationale and expected vs. actual activity** — customer rationale documented at onboarding (wealth management for international family). Expected wire-activity band documented at original onboarding; actual activity over the lookback exceeds the band on volume and on counterparty concentration. Deviation finding: actual exceeds expected; scenario links to the firm's wire-monitoring scenarios. Cross-reference to `aml-model-monitoring` for tuning consideration once the post-EDD profile is set.
- **Sanctions screening posture** — current clear; one resolved historical hit on a connected party with disposition rationale on file. List coverage: OFAC SDN, OFAC sectoral, UN, internal lists; no UK OFSI / EU consolidated coverage in scope at this institution.
- **Conduct-risk indicators** — material indicator: foreign-procurement exposure on the family member, with the source from the consumed `negative-news-triage` hit. Severity: material. Anchor: FFIEC manual relationship-behaviour treatment (US side); the conduct lens via the conduct overlay. Reputational exposure on connected parties surfaces as a secondary indicator.
- **Ongoing monitoring plan** — recommended scenarios in scope: wire-activity-anomaly (recalibrated to the post-EDD expected profile once set), counterparty-concentration, jurisdictional-concentration, PEP-adjacent-activity. Refresh-cycle interval recommended: 12 months given the elevated profile, with event-driven trigger on any further adverse-media activity. Cross-reference to `aml-model-monitoring` for tuning.
- **Open issues, evidence-needed items, and committee questions**:
  - Ownership: independent corroboration of the foreign trust intermediary's control parties — `[evidence needed]`.
  - SoW: independent public-source corroboration of the family-trust distribution narrative — `[evidence needed]`.
  - Activity: customer-rationale update for the post-onboarding deviation in expected-vs-actual activity — `[evidence needed]`.
  - Conduct: any further public reporting on the family member's foreign-procurement exposure since the consumed triage record — owner: relationship owner.
  - Sanctions: any additional connected-party screening implication of the named jurisdictions — owner: sanctions officer.
- **Recommended human-review gates and decision options** — gate: EDD committee review, composition includes BSA officer, CCO, sanctions officer, head of private banking, legal, relationship owner. Decision options the committee evaluates: retain_with_conditions; retain_with_enhanced_monitoring; retain_pending_further_evidence; restrict_products_or_volumes; escalate_to_relationship_exit_deliberation. Stop conditions: SoW corroboration not produced within the firm's defined window; sanctions exposure surfaces on a further connected-party screen; further material adverse-media reporting in the same theme. Cross-references to `cdd-risk-review`, `negative-news-triage`, `sanctions-screening-qa`, `aml-model-monitoring`. The pack does not retain, restrict, or exit; the committee decides.
- **Sign-off and source trace** — drafter: second-line EDD reviewer; reviewer: BSA officer; approver: EDD committee chair. Source trace anchors to `references/source-anchors.md` (FFIEC PEP / private-banking sections, `§1010.620`, CDD Final Rule, 2020 PEP joint statement), `references/sector-overlays.md#banking` (private-banking EDD frame), `references/cross-cutting.md#conduct` (conduct-overlay frame for the family-member foreign-procurement exposure), and the upstream `cdd-risk-review` record.
- **Confidence label** — `medium`. The financial-crime findings are at high confidence on the file evidence; the SoW corroboration gap is at medium confidence (a clear gap, but the gap itself is the finding, not the SoW conclusion); the conduct-overlay finding is at high confidence on linkage and at medium confidence on the customer-relationship implication pending the committee's read.

#### Why this scenario matters

- **PEP status alone is not the EDD trigger; PEP combined with private-banking, foreign jurisdiction, and material adverse media is.** The 2020 joint statement framing carries here: the pack records the PEP determination but builds the EDD case on the risk-based combination, not on the PEP label.
- **SoW corroboration is the dominant defect on private-banking PEP packs.** Family-trust distributions corroborated only by customer self-attestation and a prior-firm reference are a thin SoW; the EDD pack flags the gap and asks for independent public-source or transactional corroboration.
- **The beneficial-ownership chain walks past the certification.** Two foreign holding entities and a trust intermediary at the recent-distribution layer mean the certification form alone is not the read; the pack walks the chain and surfaces residual uncertainty per layer.
- **Adverse media is consumed from `negative-news-triage`, not re-litigated.** The pack reads the triaged hit as input; it does not replay the source-tier or identity-confidence work.
- **The conduct overlay surfaces on top of the financial-crime frame.** The family member's foreign-procurement exposure is conduct-relevant and bears on the EDD committee's decision; the pack flags it without turning into a conduct review.
- **The pack stops at the recommendation.** Retention with conditions, restriction, escalation to exit deliberation are decision options the committee evaluates; the pack does not retain, restrict, or exit.

#### Anchors

- FFIEC BSA/AML Examination Manual — Politically Exposed Persons, Private Banking Due Diligence, Customer Due Diligence sections [verify section anchors].
- 31 CFR §1010.620 — private-banking EDD [verify section].
- FinCEN CDD Final Rule (May 2016, compliance May 11, 2018).
- Joint Statement by Treasury, Federal Banking Agencies, and FinCEN on Banking Politically Exposed Persons (August 21, 2020).
- Wolfsberg Group Guidance on PEPs and on Source of Wealth / Source of Funds (most recent public versions; public industry standard reference).

See `references/source-anchors.md` for full citations, `references/sector-overlays.md#banking` for the bank-specific frame, and `references/cross-cutting.md#conduct` for the conduct overlay.

## troubleshooting

### Troubleshooting: edd-escalation-pack

Recurring pitfalls. Read before producing the EDD pack and again before sign-off.

#### Scope discipline

##### Drifting into the retention or exit decision

The EDD pack assembles evidence and surfaces decision options. It does not retain, restrict, or exit. The named decisionmaker is the EDD committee or the designated EDD approver. A pack that reads "retain the relationship" or "exit the relationship" as a conclusion has misread its scope. Frame the pack's output as decision options the gate evaluates, with stop conditions and conditions on retention.

##### Building the EDD pack without an upstream CDD baseline

The EDD pack consumes a CDD baseline. Where `cdd-risk-review` has not run on the customer or has run with material gaps, the EDD pack notes the missing baseline and flags it as a finding; it does not paper over the gap. A pack drafted on no upstream CDD baseline is structurally thin.

##### Re-litigating adverse-media triage

Adverse media on the customer is triaged by `negative-news-triage`. The EDD pack consumes the triaged outputs; it does not replay the source-tier or identity-confidence work. A pack that re-triages adverse media has stepped into the adjacent skill's scope.

##### Re-disposing sanctions hits

Sanctions hits on the customer are disposed by `sanctions-screening-qa`. The EDD pack reads the screening QA outputs and the dispositions; it does not re-dispose. A pack that re-disposes a hit has stepped into the adjacent skill's scope.

##### Re-tuning monitoring scenarios

Scenario tuning belongs to `aml-model-monitoring`. The EDD pack flags scenario implications for the post-EDD profile and cross-references; it does not re-tune. A pack that includes scenario thresholds or tuning recommendations has stepped into the adjacent skill's scope.

#### PEP discipline

##### Treating PEP status as automatically EDD-required

The 2020 joint statement clarifies that PEP status alone does not trigger EDD; firms apply EDD on a risk basis. The pack records the PEP determination, the source of the finding, and the date, then builds the EDD case on the risk-based combination (PEP plus product, jurisdiction, structure, transactional pattern, adverse media). A pack that triggers EDD on PEP status alone is over-reading the rule.

##### PEP status assessed once and treated as immutable

Family / close-associate status, political role changes, and adverse-media accumulation move; PEP determinations need a refresh date and a refresh trigger. The pack records the date of latest assessment and the source; a stale PEP determination on a long-tenured relationship is itself a finding.

##### Treating commercial PEP-screening-tool flags as evidence

A commercial PEP-screening tool's flag is one input. The pack reads the underlying source (public political register, government appointment record, news source) and dates the read.

#### Source-of-wealth discipline

##### Customer self-attestation treated as corroboration

A SoW statement from the customer is the customer's claim. Corroboration is what other file evidence provides (public records, third-party documentation, prior-firm references, asset documentation). The pack keeps the statement and the corroboration on different lines.

##### Stale SoW left in place at EDD refresh

Long-tenured high-net-worth customers frequently carry SoW statements that predate material life events (business sale, inheritance, role change). The EDD refresh is the moment to refresh the SoW with corroboration; leaving an 11-year-old SoW in place at refresh is a finding.

##### SoW corroboration mis-matched to the wealth category

Corroboration that fits inherited wealth (probate, family-trust deeds) does not fit a business-sale narrative (transaction documentation, public-source confirmation). The pack matches corroboration to the category; otherwise the corroboration field is thin.

##### Treating prior-firm references as standalone corroboration

A prior-firm reference is one input on top of independent public-source or transactional documentation. The pack does not treat a prior-firm reference as standalone corroboration on a high-risk SoW.

#### Source-of-funds discipline

##### SoF on inbound wires summarised without the originating account

The originating account, the originating account holder, and the relationship of that holder to the customer are the load-bearing details. A "wire from a foreign correspondent" summary without the originating-account read is thin SoF.

##### Third-party funding not surfaced as such

Where the customer is not the funder of an inbound flow (third-party-funded premium on a covered insurance product; third-party-funded inbound wire on a private-banking account), the pack reads the third-party relationship explicitly. Glossing the funder as "customer-related" is a finding.

#### Beneficial-ownership discipline

##### Stopping at the certification form on a complex-structure entity

The `§1010.230` certification form is one layer. The EDD pack walks the chain layer by layer for high-risk profiles: certification → entity filings → trust intermediaries → foreign holding companies → control parties. Residual uncertainty per layer goes in the pack explicitly.

##### Inconsistency check skipped

The certification on file may be inconsistent with the latest entity filings, signatory list, public filings, or transactional patterns implying undisclosed control. The pack runs the inconsistency check and flags the finding.

##### Asserting BOI filing status without an as-of date

`31 CFR §1010.380` (CTA implementing rule) has had live litigation; the entity-class scope and the rule-state have moved. The pack marks `boi_filing_status` with an as-of date and the rule-state read on that date, and uses the `[verify]` flag where the rule-state is unsettled.

##### Trust-customer scope mis-applied

`§1010.230` does not apply to trusts as legal-entity customers. Trust-specific due diligence sits in the institution's program, which the EDD pack reads against. Applying the BO certification form to a trust customer is a rule-scope error.

#### Section 312 (foreign correspondent) discipline

##### Reading `§1010.610` on a customer that is not a foreign FI

The rule has a defined scope. The pack confirms the customer is a foreign FI under the rule before applying the EDD elements. A bank's wire counterparty in a foreign jurisdiction is not automatically a `§1010.610` customer.

##### Treating the respondent's CBDDQ as standalone evidence

CBDDQ is industry-standard documentation; it is one input on top of the rule's elements. The pack reads the CBDDQ alongside the home-country regime read, the public-information read, and the nested-correspondent disclosure.

##### Missing the nested-correspondent disclosure

The respondent's downstream correspondent customer base by jurisdiction is the load-bearing element on indirect exposure. Incomplete or stale disclosure is a finding.

##### Sanctions exposure through customer base not quantified

Clear screening of the respondent itself does not close the sanctions-exposure-through-customer-base question. The pack reads both; the customer-base read is at named-jurisdiction granularity where the firm's program supports it.

##### Payable-through-account considerations missed

Where the respondent's account permits its customers to engage in banking activities directly, the heightened-scrutiny path applies. The pack reads the product mix at the respondent and flags any payable-through-account-adjacent product line.

#### Section 311 discipline

##### Asserting a Section 311 position without a current designation read

Section 311 designations and the special measures they impose move. The pack reads the current designation status against the customer's exposure where applicable; an outdated read is a finding.

#### Conduct overlay discipline

##### Folding conduct in as a label

A conduct finding needs an indicator type, evidence, severity, and an anchor. "PEP-adjacent reputational exposure" without source, date, or materiality is a label, not a finding.

##### Loading the conduct overlay where it does not bear on the relationship

An institution-to-institution correspondent relationship without a retail-customer-conduct nexus does not load the conduct overlay. The pack loads the overlay only where the customer profile makes conduct exposure material.

##### Conduct overlay anchors mis-matched to the firm's regulator constellation

FCA conduct anchors on a US-only firm without UK nexus are out of scope. The pack loads the conduct anchors that apply to the firm's regulator constellation.

#### Sanctions-screening posture discipline

##### Importing screening dispositions without the rationale pointer

A historical hit marked "resolved" with no disposition rationale pointer is a thin posture statement. The pack carries the disposition rationale pointer (cross-reference to `sanctions-screening-qa`).

##### Connected-party screening posture summarised without the named parties

Beneficial owners, signatories, and key counterparties are connected parties. The pack names the parties screened and the disposition; "all connected parties screened" without naming is thin.

#### Output discipline

##### Citing without sections

Every regulator citation in the pack carries a section reference or a `[verify section]` placeholder in the source-anchors file. The pack body does not carry `[verify section]`; the source-anchors file does.

##### Marking unsupported claims silently

Use `[evidence needed]` explicitly. An inferred claim presented as evidenced is the failure mode the source-trace structure exists to prevent.

##### Closing with too much certainty

The confidence label is `high` only when source posture, file evidence, and EDD criteria all line up. `medium` and `low` are normal where the gaps are part of the finding; `unknown` is honest where the firm has not yet resourced the evidence ask. A `high` confidence label on a pack with material SoW or sanctions-exposure gaps is incoherent.

##### Pack over-extending into the next skill or the prior skill

`cdd-risk-review` is upstream. `negative-news-triage`, `sanctions-screening-qa`, `aml-model-monitoring`, `sar-decision-qa` are adjacent. The EDD pack consumes upstream and adjacent records and cross-references; it does not re-do their work.

##### No sign-off block

The pack carries a sign-off block (drafter, reviewer, approver) so the audit trail is on the artifact. A pack without a sign-off block has shipped half the artifact.
