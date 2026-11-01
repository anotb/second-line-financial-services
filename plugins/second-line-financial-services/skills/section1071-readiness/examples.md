# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## community-bank-pre-go-live

### Example: pre-compliance-date readiness check at a community bank

#### Input

A US community bank, state-chartered, originates a moderate volume of small-business credit (term loans, lines of credit, business credit cards, SBA 7(a), commercial real estate at the small-business boundary). The compliance officer commissions a readiness check ahead of the January 1, 2028 compliance date under the May 2026 revised final rule. Inputs supplied: small-business origination counts for the two preceding calendar years from the LOS reporting module (1,420 originations year T-1; 1,310 year T-2 — above the 1,000 threshold in both years); the firm's small-business product taxonomy; the LOS vendor's §1071 build documentation (vendor is mid-build, attestation requested but not yet signed); the customer-360 data dictionary; the firm's records-retention schedule; and the existing fair-lending program documentation. Sector overlay: `banking.md`. Cross-cutting overlays: `privacy.md`, `conduct.md`. Source posture: public-plus-firm-policy-plus-evidence.

#### Output sketch

The skill produces a readiness matrix workbook conforming to `schemas/section1071-readiness.schema.json` and a narrative gap memo per `templates/default-output.md`. Highlights:

- **CFI determination**: covered (1,420 / 1,310 against the 1,000 threshold in each of the two preceding calendar years). Compliance date January 1, 2028 under the May 2026 revised rule, carried as a sourced citation. Distance-from-threshold: ~30% headroom; year-over-year monitoring recommended.
- **Per-product covered-transaction mapping**: 11 in-scope product rows; 4 out-of-scope (consumer-purpose products, HMDA-reportable owner-occupied 1-4 family); 3 edge cases (letters of credit, demand-deposit-account-secured small lines, agricultural credit at the small-business boundary) routed to legal.
- **Data-point matrix (1002.107)**: 31 rows. **18 ready** (the credit-detail data points already captured in the LOS), **6 partial** (NAICS captured at SBA-line origination but not at general commercial lending; census tract populated from the borrower's mailing address rather than the principal address; pricing fields for business credit cards captured at account origination but with the application-method field needing the LOS vendor's build to deliver), **5 gap** (demographic data fields — race, ethnicity, sex, minority-owned, women-owned, LGBTQI+-owned — pending the LOS vendor's demographic-collection-form build), and **2 unverifiable** (pricing-prepayment-penalty field; total origination charges field — vendor build description ambiguous on the exact computation).
- **Demographic-collection mechanics**: the script and form text are not yet in the LOS; the planned design follows the CFPB Sample Data Collection Form. Refusal-handling code path is in design and the readiness state is `gap` until the LOS build delivers.
- **Firewall (1002.108)**: a **material gap**. The LOS-side firewall design follows vendor RBAC and is intact in concept, but the bank's customer-360 view aggregates self-reported demographics from the deposit-side onboarding (collected for HMDA cross-product purposes) and exposes them to the underwriting role. A 1002.108 breach in the customer-360 layer; remediation requires either suppressing the demographic fields from the underwriter's customer-360 view or re-architecting access. Severity: `high`.
- **Recordkeeping**: the firm's enterprise records-retention schedule covers lending records under a generic seven-year rule; the §1071 three-year retention from date of submission needs explicit addition to the schedule. Severity: `medium`.
- **Reporting and filing readiness**: FIG edition pinned with `[verify current edition]`; validation engine choice not yet made; test-submission plan not yet drafted. Severity: `high`.
- **Vendor and LOS readiness**: vendor mid-build; attestation requested but not signed; change-control identifier provided. Sponsor-bank flag not applicable (bank is the CFI on its own balance sheet).
- **Bona-fide-error approach (1002.112)**: not yet drafted. Severity: `high`.
- **Privacy posture**: GLBA Safeguards posture intact at the firm level; the §1071 dataset needs explicit naming in the firm's information-security program. Modified-data publication re-identification risk: low-volume in three rural-county census tracts; flag for legal and communications review before first publication.
- **Conduct posture**: the front-line training has not been delivered; once delivered, an operating-state check on script integrity is recommended within 90 days of go-live. The customer-360 firewall gap is also a conduct theme (the firewall control was designed in isolation from how underwriters work).
- **Gap list**: 14 items rolled up. Two `blocking` (FIG validation engine and test plan; LOS demographic-collection-form build not delivered), four `high` (customer-360 firewall remediation; bona-fide-error policy; vendor attestation; reporting-and-filing readiness), six `medium`, two `low`.
- **Reviewer questions** for the head of consumer compliance and the named accountable executive (CRO). **Open questions** for legal on the three edge-case products and the affiliate-aggregation question for the bank's holding-company structure.

#### Why this scenario matters

It exercises the full readiness spine for a depository: CFI determination against the revised 1,000-transaction threshold, per-product mapping with edge cases, the customer-360 firewall failure mode that depository firewall reviews predictably miss, a vendor-mid-build LOS posture that produces real `unverifiable` rows in the matrix, and the privacy-overlay re-identification flag for low-volume census tracts. It also shows the conduct-overlay theme on the customer-360 design as a governance issue, not just a control gap.

## fintech-mca-sponsor-bank

### Example: sales-based-financing fintech operating under a sponsor bank

#### Input

A US-based fintech offering merchant cash advance and other sales-based financing to small businesses, originating credit on the sponsor bank's balance sheet under a sponsor-bank arrangement. The fintech is the data-collection agent in operational practice (online application flow, KYB / KYC, decisioning recommendation, demographic-collection form, post-funding settlement-data integration); the sponsor bank is the covered financial institution and the §1071 filer. The sponsor bank's compliance officer commissions a readiness review at the sponsor-bank / fintech interface, ahead of the January 1, 2028 compliance date under the May 2026 revised final rule. Inputs supplied: the contractual responsibility allocation between sponsor bank and fintech; the fintech's online-application flow documentation; the fintech's LOS data dictionary; the fintech's data-warehouse access-control documentation; sample script and form text; the sponsor bank's existing §1071 readiness program for its direct-lending portfolio. Sector overlay: both `banking.md` (sponsor-bank view) and `payments-fintech.md` (fintech view). Cross-cutting overlays: `privacy.md`, `conduct.md`. Source posture: public-plus-firm-policy.

#### Output sketch

The skill produces a readiness matrix workbook conforming to `schemas/section1071-readiness.schema.json` and a narrative gap memo per `templates/default-output.md`. Highlights:

- **Sponsor-bank attribution resolved** in the executive summary: the sponsor bank is the CFI; the fintech is the data-collection agent. The CFI determination and the January 1, 2028 compliance date apply at the sponsor bank. The readiness work runs at the fintech's operational layer, but the sign-off and the filing are the sponsor bank's.
- **CFI determination**: covered above the 1,000-transaction threshold at the sponsor bank when its sponsor-bank-program originations are aggregated with its direct-lending originations [verify aggregation methodology with legal]. Single compliance date: January 1, 2028 under the May 2026 revised rule.
- **Per-product covered-transaction mapping**: 4 in-scope product rows (merchant cash advance, daily-remit sales-based financing, weekly-remit sales-based financing, factoring-without-recourse on the boundary). 1 edge case (a B2B BNPL product the fintech is piloting) routed to legal as an open question.
- **Data-point matrix (1002.107)**: 31 rows. **9 ready** (the credit-detail data points captured at application); **8 partial** (the pricing-additional-cost field for sales-based financing is computed post-funding from settlement data — capture method `firm_inferred` rather than `applicant_provided`, with downstream amendment-reporting risk; the action-taken-date field needs careful handling because approval-and-funding can be near-instantaneous; pricing fields including the additional-cost-for-MCA field need verification of the exact computation method against the rule); **11 gap** (demographic-data fields are present in the form but the refusal-handling code path records refusal as `null` rather than the rule's required refusal value — the most material data-point gap; principal-owner identification logic captures only the lead application contact, not all 25%+ owners as the rule requires `[verify threshold]`); **3 unverifiable** (broker-fees field for arrangements where the fintech also pays a marketplace platform; initial-annual-charges field where the product structure does not have a periodic-charge equivalent).
- **Demographic-collection mechanics**: the form is in the digital application flow but the script's required disclosures need re-review against the rule's text. Refusal-handling miscoded as `null`. Principal-owner identification gap is material because the fintech's decisioning model trains on a single contact's credit profile rather than the full principal-owner set.
- **Firewall (1002.108)**: the LOS-side firewall is intact in the underwriting-decisioning pipeline. The **material gap** is in the data-warehouse: the fintech's analytics environment pulls the demographic-data fields into the same tables the growth and product teams use, with role-based access that does not segregate the §1071 demographic data. Severity: `high`. Remediation: re-architect the data-warehouse access controls to segregate the §1071 demographic dataset.
- **Sponsor-bank firewall alignment**: the sponsor bank's §1071 firewall expectations need to be mirrored in the fintech's environment. Currently the contractual allocation requires the fintech to comply with the sponsor bank's policies, but the fintech has not yet operationalised the sponsor-bank firewall standards in its data-warehouse. Severity: `high`.
- **Recordkeeping**: the contractual allocation places primary recordkeeping with the fintech for the application-stage data and with the sponsor bank for the post-origination data. Three-year retention from date of submission applies; the fintech's records-retention policy needs to add the §1071 row with the disposition-policy reference back to the sponsor bank.
- **Reporting and filing readiness**: the sponsor bank files; the fintech feeds the data to the sponsor bank for inclusion. The data-flow from fintech to sponsor bank for the §1071 dataset needs explicit design with reconciliation against the sponsor bank's other §1071 sources (its direct-lending portfolio).
- **Vendor and LOS readiness**: 6 vendor rows. The KYB / KYC vendor (provider of beneficial-ownership data used for principal-owner identification), the demographic-collection-form provider (an internal build, not a vendor), the pricing-data computation engine (internal build computing the additional-cost field), the FIG-validation utility (sponsor bank's selection, not yet pinned), the data-warehouse provider, and the broker-channel marketplace partner.
- **Bona-fide-error approach (1002.112)**: not yet drafted at either entity. Joint sponsor-bank / fintech draft required. Severity: `high`.
- **Privacy posture**: GLBA Safeguards posture: the sponsor bank's information-security program covers the dataset by attribution; the fintech's program needs to name the §1071 dataset explicitly. Modified-data publication re-identification: not material at this fintech's volume profile across most census tracts; flag two specialised industry segments where the combination of NAICS, gross-revenue band, and loan-amount band may identify the borrower.
- **Conduct posture**: the front-line interaction is digital; the conduct-theme work focuses on the application-flow design (does the demographic-collection request appear in a way that suggests it matters for the credit decision?) and on the broker-channel partner's representation of the request to applicants. Routing: conduct committee at the sponsor bank.
- **Gap list**: 19 items rolled up. Three `blocking` (refusal-handling code; principal-owner identification logic; FIG-validation utility selection), seven `high`, eight `medium`, one `low`.
- **Reviewer questions** for the sponsor bank's head of consumer compliance and the fintech's head of compliance jointly. **Open questions** for legal on the B2B BNPL product, the principal-owner-threshold reading, and the affiliate-aggregation methodology for the sponsor-bank-program origination count.

#### Why this scenario matters

It exercises the sponsor-bank attribution question (the most common sponsor-bank-program scoping error), the sales-based-financing pricing capture pattern (`firm_inferred` rather than `applicant_provided` with amendment-reporting risk), the data-warehouse firewall failure mode (the predictable fintech-specific 1002.108 gap), the sponsor-bank firewall-alignment expectation, and the joint sponsor-bank / fintech bona-fide-error policy. It also shows the principal-owner identification gap, which is operationally subtle but materially affects the dataset's utility for the downstream fair-lending testing handoff.

## troubleshooting

### Troubleshooting: section1071-readiness

Recurring pitfalls in §1071 readiness work, with the corrective posture for each. Sources are in `references/source-anchors.md`. Sector-specific pitfalls live in the corresponding overlay files.

#### Compliance date treated as a static fact

The 12 CFR 1002.114 compliance-date schedule has been moved by court order and the CFPB's response (the CTA-style litigation history). Pinning the date from the original 2023 final-rule notice or from a stale CFPB compliance-date-table snapshot produces a memo with a wrong date in the executive summary.

**Corrective posture**: pin from the CFPB compliance-resources page at the time of drafting; carry the date as a sourced citation in `cfi_determination.compliance_date` (value, source, retrieval date, `[verify current effectiveness and tier dates]` marker), not as a bare value. Re-pin if the dates move again. The structured output's compliance-date object enforces this.

#### Per-product mapping built from the firm's procurement taxonomy

The firm's product taxonomy (the one used by the lending business and procurement) does not align one-for-one with the 12 CFR 1002.106 covered-credit-transaction definition. Mapping the procurement product list directly to in-scope without rule-cited rationale produces a scope that the compliance officer cannot defend in supervisory dialogue.

**Corrective posture**: per-product mapping with explicit `1002.106(a)` or `1002.106(b)` citation per product; `in / out / edge` classification with rationale; edge cases routed to legal as open questions. The scope's `rule_reference` field is mandatory.

#### Demographic data collection treated as a UI question

Collecting the demographic data is half the rule (the 1002.107(a)(19) through (a)(22) data points and the form mechanics). Isolating it from underwriting access under 12 CFR 1002.108 is the other half. A readiness assessment that treats demographic data as a form-design question and does not produce a 1002.108 firewall section misses the point.

**Corrective posture**: the firewall section is mandatory in every readiness assessment. The `firewall` object in the structured output produces an attestation map per role and an exception process; the customer-360 / relationship-management-view review is a standing review row at depositories; the data-warehouse access-control review is a standing review row at fintechs.

#### Vendor LOS readiness treated as the firm's readiness

The firm is the covered financial institution. The vendor is a data-collection agent. A readiness assessment that says "the LOS vendor will deliver §1071 capability in [quarter]" and treats that as the firm's readiness state misses the firm's accountability.

**Corrective posture**: `vendor_readiness[]` is mandatory with attestation status, change-control identifier, contractual responsibility allocation, and SLA on the data-flow. Vendor-driven gaps roll up to the firm's gap list with severity. The firm signs off on the readiness, not the vendor.

#### Refusal coded as `null`

The §1071 rule requires that an applicant's refusal of demographic data is coded with a specific refusal value, not `null`. Coding refusal as `null` breaks the FIG validation downstream and miscodes the refusal in the firm's own dataset, distorting the demographic-data completeness picture.

**Corrective posture**: surface in the demographic-collection-mechanics section; gap list with severity `blocking` if not yet corrected at the design stage. The refusal-handling code path is one of the most common operational defects.

#### Census tract populated from the borrower's mailing address

12 CFR 1002.107 requires the census tract of the **principal address** of the small business. Populating from the borrower's mailing address (or from the application-contact's home address) is wrong and predictably common where the LOS captures an address but does not distinguish principal address from mailing address.

**Corrective posture**: confirm the field's source in the system-of-record column of the data-point matrix; gap list as `partial` or `gap` if the LOS captures only mailing address.

#### NAICS captured at SBA-line origination only

A common pattern at depositories: NAICS is captured at SBA-line origination (because SBA reporting requires it) but not at general commercial lending. The §1071 obligation is uniform across covered credit transactions; partial NAICS coverage leaves a gap across the rest of the in-scope portfolio.

**Corrective posture**: per-data-point matrix with system-of-record column; gap rolls up where NAICS is not captured for all in-scope products.

#### Pricing-additional-cost field for sales-based financing computed post-funding

For merchant cash advance and other sales-based financing, the §1071 *additional cost* field is computed from the financing structure. Systems frequently compute it post-funding from settlement data rather than at origination, sitting as `firm_inferred` rather than `applicant_provided` capture method. This raises downstream amendment-reporting risk: where the actual delivery rate diverges from the expected rate, the additional-cost figure may need to be amended after submission.

**Corrective posture**: surface explicitly in the data-point matrix's `notes` column; consider re-engineering the capture to compute and capture at origination; document the bona-fide-error and amendment procedure under 1002.112.

#### Bona-fide-error policy not in place at go-live

12 CFR 1002.112 sets the bona-fide-error and safe-harbor approach. A firm going live on §1071 reporting without a documented bona-fide-error policy and an amendment procedure is exposed to the predictable error pattern of a first-cycle submission.

**Corrective posture**: `bona_fide_error_approach.policy_status` is mandatory; gap list with severity `high` if not in place at the readiness as-of date; the policy needs to be in place before go-live, not after the first amendment is needed.

#### Modified-data publication re-identification risk not considered

12 CFR 1002.109 provides for the CFPB to publish a modified version of submitted data. The CFPB modifies fields to manage privacy risk, but for low-volume small-business lending in identifiable geographies, the re-identification risk persists. Firms with low-volume lending in sparsely-populated census tracts publish records where the combination of geography, NAICS, revenue band, and loan amount may identify the borrower.

**Corrective posture**: load the privacy overlay; the privacy section of the readiness memo includes a re-identification-risk row for low-volume / identifiable-geography portfolios; gap list rolls up an action to brief legal and communications before the first modified-data publication.

#### Customer-360 firewall breach at depositories

The most material 1002.108 gap at depositories is rarely the LOS firewall (the LOS vendor builds the firewall capability into the product). It is the customer-360 / relationship-management view that aggregates self-reported demographics from the deposit side (collected at account opening for HMDA cross-product or other firm-internal purposes) and exposes them to the underwriter who pulls the customer-360 record during credit decisioning. The §1071 firewall is breached if the underwriter sees the demographic from the deposit-side feed even though the LOS-side firewall is intact.

**Corrective posture**: the firewall section's `customer_360_view_review` field is a standing review row at depositories; remediation typically requires either suppressing the demographic fields from the underwriter's view or re-architecting the customer-360 access controls. Treat as severity `high` until remediated.

#### Data-warehouse firewall breach at fintechs

The fintech-specific equivalent: the data-engineering or analytics environment pulls the demographic data into a general-purpose dataset accessible to the broader product, growth, or risk-analytics team. The 1002.108 firewall is breached at the data-warehouse layer even though the LOS-side firewall is intact.

**Corrective posture**: the firewall section's `customer_360_view_review` field at fintechs covers the data-warehouse layer; remediation is access-control segregation of the §1071 demographic dataset.

#### Sponsor-bank attribution wrong at fintechs

A fintech operating under a sponsor-bank arrangement may run the readiness assessment at the fintech rather than at the sponsor bank, missing that the sponsor bank is the CFI. Or it may treat the sponsor bank as the CFI without recognising that the fintech operates §1071 controls in operational practice and is the data-collection agent under the contractual arrangement.

**Corrective posture**: the sponsor-bank attribution question is the first item in the readiness memo's executive summary for sponsor-bank-program engagements. Resolve before drafting.

#### Affiliate aggregation question silently resolved

Where the firm operates through multiple affiliated depository entities (or a sponsor bank with multiple sponsor-bank programs), the threshold count under 1002.105 raises an aggregation question. Silently aggregating (or silently not aggregating) without documenting the rationale is a defect.

**Corrective posture**: `cfi_determination.affiliate_aggregation_question_status` is `resolved` (with documented methodology), `open-question-for-legal`, or `not-applicable`. Surface the question explicitly in the executive summary where it is open.

#### Treating the readiness assessment as the filing

This skill drafts the readiness assessment and the gap memo. The submission is a regulated filing requiring sign-off by the named accountable executive at the CFI, and is filed through the CFPB-specified channel by the firm's regulatory-reporting pipeline. The skill does not file, does not sign off, and does not finalize the CFI determination.

**Corrective posture**: the SKILL.md guardrail is restated in the readiness memo's review-gate section; review-gate boolean flags in the structured output do not mark `decision_gate = true` without the executive sign-off.

#### FIG edition pinned from a stale source

The CFPB Filing Instructions Guide is updated between cycles. Pinning the FIG edition from a prior-year copy or from a stale screenshot produces a readiness state against the wrong specification.

**Corrective posture**: `reporting_readiness.fig_edition` carries the `[verify current edition]` marker until pinned from the current CFPB filing-instructions page; the test-submission plan reads against the pinned edition.

#### Three-year retention conflated with the firm's enterprise schedule

The 12 CFR 1002.110 three-year retention from date of submission is specific. Conflating with the firm's enterprise records-retention schedule ("we keep lending records for seven years, so we're fine") misses the §1071-specific retention requirement and the regulator's expectation that the records are produceable on examination request within an examination timeline.

**Corrective posture**: `recordkeeping.records_identified` names the §1071 dataset and supporting documentation specifically; `recordkeeping.disposition_policy_reference` ties to a §1071-specific row in the firm's records-retention schedule, not to the generic lending-records rule.

#### Treating §1071 readiness as decoupled from fair-lending testing

The §1071 dataset becomes the canonical small-business-lending fair-lending dataset once it exists. A readiness assessment that does not consider whether the dataset is fit for the downstream fair-lending testing pipeline (`fair-lending-test-plan`) misses the point of the rule's data-collection design.

**Corrective posture**: `fair_lending_handoff` is mandatory in the structured output; the readiness memo includes the §11 fair-lending-handoff section; the firewall section anticipates the fair-lending team's permitted access under 1002.108.
