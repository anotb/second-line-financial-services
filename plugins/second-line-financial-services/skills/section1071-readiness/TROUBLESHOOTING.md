# Troubleshooting: section1071-readiness

Recurring pitfalls in §1071 readiness work, with the corrective posture for each. Sources are in `references/source-anchors.md`. Sector-specific pitfalls live in the corresponding overlay files.

## Compliance date treated as a static fact

The 12 CFR 1002.114 compliance-date schedule has been moved by court order and the CFPB's response (the CTA-style litigation history). Pinning the date from the original 2023 final-rule notice or from a stale CFPB compliance-date-table snapshot produces a memo with a wrong date in the executive summary.

**Corrective posture**: pin from the CFPB compliance-resources page at the time of drafting; carry the date as a sourced citation in `cfi_determination.compliance_date` (value, source, retrieval date, `[verify current effectiveness and tier dates]` marker), not as a bare value. Re-pin if the dates move again. The structured output's compliance-date object enforces this.

## Per-product mapping built from the firm's procurement taxonomy

The firm's product taxonomy (the one used by the lending business and procurement) does not align one-for-one with the 12 CFR 1002.106 covered-credit-transaction definition. Mapping the procurement product list directly to in-scope without rule-cited rationale produces a scope that the compliance officer cannot defend in supervisory dialogue.

**Corrective posture**: per-product mapping with explicit `1002.106(a)` or `1002.106(b)` citation per product; `in / out / edge` classification with rationale; edge cases routed to legal as open questions. The scope's `rule_reference` field is mandatory.

## Demographic data collection treated as a UI question

Collecting the demographic data is half the rule (the 1002.107(a)(19) through (a)(22) data points and the form mechanics). Isolating it from underwriting access under 12 CFR 1002.108 is the other half. A readiness assessment that treats demographic data as a form-design question and does not produce a 1002.108 firewall section misses the point.

**Corrective posture**: the firewall section is mandatory in every readiness assessment. The `firewall` object in the structured output produces an attestation map per role and an exception process; the customer-360 / relationship-management-view review is a standing review row at depositories; the data-warehouse access-control review is a standing review row at fintechs.

## Vendor LOS readiness treated as the firm's readiness

The firm is the covered financial institution. The vendor is a data-collection agent. A readiness assessment that says "the LOS vendor will deliver §1071 capability in [quarter]" and treats that as the firm's readiness state misses the firm's accountability.

**Corrective posture**: `vendor_readiness[]` is mandatory with attestation status, change-control identifier, contractual responsibility allocation, and SLA on the data-flow. Vendor-driven gaps roll up to the firm's gap list with severity. The firm signs off on the readiness, not the vendor.

## Refusal coded as `null`

The §1071 rule requires that an applicant's refusal of demographic data is coded with a specific refusal value, not `null`. Coding refusal as `null` breaks the FIG validation downstream and miscodes the refusal in the firm's own dataset, distorting the demographic-data completeness picture.

**Corrective posture**: surface in the demographic-collection-mechanics section; gap list with severity `blocking` if not yet corrected at the design stage. The refusal-handling code path is one of the most common operational defects.

## Census tract populated from the borrower's mailing address

12 CFR 1002.107 requires the census tract of the **principal address** of the small business. Populating from the borrower's mailing address (or from the application-contact's home address) is wrong and predictably common where the LOS captures an address but does not distinguish principal address from mailing address.

**Corrective posture**: confirm the field's source in the system-of-record column of the data-point matrix; gap list as `partial` or `gap` if the LOS captures only mailing address.

## NAICS captured at SBA-line origination only

A common pattern at depositories: NAICS is captured at SBA-line origination (because SBA reporting requires it) but not at general commercial lending. The §1071 obligation is uniform across covered credit transactions; partial NAICS coverage leaves a gap across the rest of the in-scope portfolio.

**Corrective posture**: per-data-point matrix with system-of-record column; gap rolls up where NAICS is not captured for all in-scope products.

## Pricing-additional-cost field for sales-based financing computed post-funding

For merchant cash advance and other sales-based financing, the §1071 *additional cost* field is computed from the financing structure. Systems frequently compute it post-funding from settlement data rather than at origination, sitting as `firm_inferred` rather than `applicant_provided` capture method. This raises downstream amendment-reporting risk: where the actual delivery rate diverges from the expected rate, the additional-cost figure may need to be amended after submission.

**Corrective posture**: surface explicitly in the data-point matrix's `notes` column; consider re-engineering the capture to compute and capture at origination; document the bona-fide-error and amendment procedure under 1002.112.

## Bona-fide-error policy not in place at go-live

12 CFR 1002.112 sets the bona-fide-error and safe-harbor approach. A firm going live on §1071 reporting without a documented bona-fide-error policy and an amendment procedure is exposed to the predictable error pattern of a first-cycle submission.

**Corrective posture**: `bona_fide_error_approach.policy_status` is mandatory; gap list with severity `high` if not in place at the readiness as-of date; the policy needs to be in place before go-live, not after the first amendment is needed.

## Modified-data publication re-identification risk not considered

12 CFR 1002.109 provides for the CFPB to publish a modified version of submitted data. The CFPB modifies fields to manage privacy risk, but for low-volume small-business lending in identifiable geographies, the re-identification risk persists. Firms with low-volume lending in sparsely-populated census tracts publish records where the combination of geography, NAICS, revenue band, and loan amount may identify the borrower.

**Corrective posture**: load the privacy overlay; the privacy section of the readiness memo includes a re-identification-risk row for low-volume / identifiable-geography portfolios; gap list rolls up an action to brief legal and communications before the first modified-data publication.

## Customer-360 firewall breach at depositories

The most material 1002.108 gap at depositories is rarely the LOS firewall (the LOS vendor builds the firewall capability into the product). It is the customer-360 / relationship-management view that aggregates self-reported demographics from the deposit side (collected at account opening for HMDA cross-product or other firm-internal purposes) and exposes them to the underwriter who pulls the customer-360 record during credit decisioning. The §1071 firewall is breached if the underwriter sees the demographic from the deposit-side feed even though the LOS-side firewall is intact.

**Corrective posture**: the firewall section's `customer_360_view_review` field is a standing review row at depositories; remediation typically requires either suppressing the demographic fields from the underwriter's view or re-architecting the customer-360 access controls. Treat as severity `high` until remediated.

## Data-warehouse firewall breach at fintechs

The fintech-specific equivalent: the data-engineering or analytics environment pulls the demographic data into a general-purpose dataset accessible to the broader product, growth, or risk-analytics team. The 1002.108 firewall is breached at the data-warehouse layer even though the LOS-side firewall is intact.

**Corrective posture**: the firewall section's `customer_360_view_review` field at fintechs covers the data-warehouse layer; remediation is access-control segregation of the §1071 demographic dataset.

## Sponsor-bank attribution wrong at fintechs

A fintech operating under a sponsor-bank arrangement may run the readiness assessment at the fintech rather than at the sponsor bank, missing that the sponsor bank is the CFI. Or it may treat the sponsor bank as the CFI without recognising that the fintech operates §1071 controls in operational practice and is the data-collection agent under the contractual arrangement.

**Corrective posture**: the sponsor-bank attribution question is the first item in the readiness memo's executive summary for sponsor-bank-program engagements. Resolve before drafting.

## Affiliate aggregation question silently resolved

Where the firm operates through multiple affiliated depository entities (or a sponsor bank with multiple sponsor-bank programs), the threshold count under 1002.105 raises an aggregation question. Silently aggregating (or silently not aggregating) without documenting the rationale is a defect.

**Corrective posture**: `cfi_determination.affiliate_aggregation_question_status` is `resolved` (with documented methodology), `open-question-for-legal`, or `not-applicable`. Surface the question explicitly in the executive summary where it is open.

## Treating the readiness assessment as the filing

This skill drafts the readiness assessment and the gap memo. The submission is a regulated filing requiring sign-off by the named accountable executive at the CFI, and is filed through the CFPB-specified channel by the firm's regulatory-reporting pipeline. The skill does not file, does not sign off, and does not finalize the CFI determination.

**Corrective posture**: the SKILL.md guardrail is restated in the readiness memo's review-gate section; review-gate boolean flags in the structured output do not mark `decision_gate = true` without the executive sign-off.

## FIG edition pinned from a stale source

The CFPB Filing Instructions Guide is updated between cycles. Pinning the FIG edition from a prior-year copy or from a stale screenshot produces a readiness state against the wrong specification.

**Corrective posture**: `reporting_readiness.fig_edition` carries the `[verify current edition]` marker until pinned from the current CFPB filing-instructions page; the test-submission plan reads against the pinned edition.

## Three-year retention conflated with the firm's enterprise schedule

The 12 CFR 1002.110 three-year retention from date of submission is specific. Conflating with the firm's enterprise records-retention schedule ("we keep lending records for seven years, so we're fine") misses the §1071-specific retention requirement and the regulator's expectation that the records are produceable on examination request within an examination timeline.

**Corrective posture**: `recordkeeping.records_identified` names the §1071 dataset and supporting documentation specifically; `recordkeeping.disposition_policy_reference` ties to a §1071-specific row in the firm's records-retention schedule, not to the generic lending-records rule.

## Treating §1071 readiness as decoupled from fair-lending testing

The §1071 dataset becomes the canonical small-business-lending fair-lending dataset once it exists. A readiness assessment that does not consider whether the dataset is fit for the downstream fair-lending testing pipeline (`fair-lending-test-plan`) misses the point of the rule's data-collection design.

**Corrective posture**: `fair_lending_handoff` is mandatory in the structured output; the readiness memo includes the §11 fair-lending-handoff section; the firewall section anticipates the fair-lending team's permitted access under 1002.108.
