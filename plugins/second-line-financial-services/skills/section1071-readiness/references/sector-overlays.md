# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — section1071-readiness

When the scope flags banking, load this overlay alongside `references/source-anchors.md`. This is the heaviest sector overlay for §1071 readiness because depository institutions are the predominant covered-financial-institution population.

#### Covered-financial-institution determination for depository institutions

- **Origination-volume counting at depositories**. The 12 CFR 1002.105 threshold under the May 2026 revised rule is **1,000 covered originations to small businesses in each of the two preceding calendar years**. Depositories typically have the operational data to count cleanly, but the count's correctness depends on the per-product covered-transaction mapping (1002.106). Common mistakes: counting all SBA originations regardless of small-business definition; counting renewals as new originations where the rule treats them differently; counting business-credit-card originations on a per-account basis where the rule's treatment of business credit cards needs careful reading [verify the credit-card treatment under the current rule text].
- **Threshold-proximity sensitivity**. A depository sitting near the 1,000-transaction line in either of the two preceding calendar years can flip CFI / not-CFI year-over-year. Run the count under both years and surface the proximity in the memo; near-threshold firms still build to the same compliance date as far-above-threshold firms because the binary determination triggers it.
- **Affiliate aggregation question**. Where the firm operates through multiple affiliated depository entities, each entity's CFI determination is its own. The rule does not aggregate at the holding-company level for the threshold count [verify under current rule]; surface this as an open question for legal where the firm's structure makes the answer non-trivial.

#### Per-product covered-transaction mapping at depositories

Depositories have the broadest small-business product range. Each product needs `in / out / edge` classification with rule-cited rationale:

- **Term loans for business purposes** — typically `in` under 1002.106.
- **Lines of credit for business purposes** — typically `in`; capture the line-establishment vs. draw treatment.
- **Business credit cards** — `in` per the rule's express coverage; the data-point capture for business credit cards differs operationally from term-loan capture (no formal "application date" in the same shape; verify the application-method and application-recipient capture for the credit-card flow).
- **SBA 7(a) and SBA 504 loans** — `in` where the borrower meets the small-business definition; the data already collected for SBA reporting overlaps with §1071 but does not satisfy §1071 (different schema, different demographic-collection requirements, different firewall posture). Map; do not assume SBA capture is §1071 capture.
- **Commercial real-estate loans for small-business borrowers** — `in` where the borrower is a small business under the rule's definition; HMDA-reportable transactions are excluded under 1002.106(b)(1) and the boundary between HMDA-reportable and §1071-reportable for owner-occupied commercial real estate needs careful per-loan classification.
- **Equipment finance and equipment leases** — `in` where the lease meets the credit-extension definition; capital-lease vs. operating-lease treatment is the operative distinction [verify].
- **Letters of credit and trade finance** — `edge`; surface as an open question for legal. The boundary between letter-of-credit issuance and a covered credit transaction is non-trivial.
- **Demand-deposit-account-secured lines** — `in` where the secured line is a covered credit transaction.
- **Floor-plan financing** — `in` for dealer floor plans where the dealer meets the small-business definition.
- **Agricultural credit** — `in` where the borrower meets the small-business definition; the agricultural-credit population overlaps with the rule but agricultural-specific exemptions in other regimes do not extend to §1071.
- **Intra-group lending and shareholder loans** — `edge`; surface for legal.

#### Firewall design at depositories

The firewall under 1002.108 reads against the depository's role-based access controls in the LOS, the customer-360 / relationship-management view, and any data warehouse that aggregates lending and deposit data. The most material 1002.108 gap at depositories is rarely in the LOS itself; the LOS vendor builds the firewall capability into the product. The gap is usually in the customer-360 view where:

- **Self-reported demographics from the deposit side** (race, ethnicity, sex captured at account opening for HMDA cross-product or other firm-internal purposes) are aggregated into the customer-360 record and exposed to underwriters who pull the customer-360 record during credit decisioning. The §1071 firewall is breached if the underwriter sees the demographic from the deposit-side feed even though the LOS-side firewall is intact.
- **Cross-product reporting** that pulls demographic data into a firm-internal dashboard accessible to underwriters.
- **Manager / executive overrides** that grant temporary access for case review without a documented exception process.

Depositories also need to pin the firewall-trained-personnel design: who is trained, what training, what cadence, what attestation. The rule's notice provision for permitted-exception cases needs a documented procedure (script, log, attestation per case).

#### Recordkeeping and the broader records-retention schedule

Depositories typically have an enterprise records-retention schedule managed by records management or general counsel. The §1071 three-year retention from the date of submission needs to be reflected explicitly in the schedule, with the records identified and the disposition policy named. A depository running on a generic "lending records — seven years" rubric needs the §1071-specific retention added to the schedule.

#### FIG conformance, validation engine, and submission channel

Depositories typically have an existing regulatory-reporting pipeline (HMDA LAR submission, Call Report, FFIEC reporting). The §1071 submission flows through the CFPB's filing channel [verify current channel and authentication mechanics]; the validation-engine choice (CFPB-provided, vendor-built, or in-house) and the test-submission plan should land before the compliance-date go-live. A depository assuming the HMDA pipeline serves §1071 misses the schema differences and the firewall implications for the analytics environment.

#### Output-template additions for banking

- CFI determination section carries the per-affiliate count where the firm operates through multiple affiliated depositories.
- Product mapping table includes the SBA / HMDA boundary rows explicitly.
- Firewall section calls out the customer-360 / relationship-management view as a standing review row.
- Recordkeeping section calls out the integration with the enterprise records-retention schedule.
- FIG-readiness section names the existing regulatory-reporting pipeline and the analytics-environment firewall posture.

#### Common pitfalls in banking §1071 readiness

- Treating SBA reporting as §1071 readiness. Different schema, different demographic-collection design, different firewall posture.
- Assuming the LOS vendor's firewall capability is the firm's firewall control. The vendor builds the capability; the firm operates the control across the customer-360 and analytics environments.
- Counting business-credit-card originations using a per-transaction definition where the rule expects per-account [verify under current rule text].
- Missing the HMDA / §1071 boundary for owner-occupied commercial real estate.
- Pinning the compliance date from a stale source (the original 2023 final-rule dates, or an outdated CFPB compliance-date-table snapshot). The dates have moved; pin from the current CFPB compliance-resources page at the time of drafting.
- Relying on the existing enterprise records-retention schedule without an explicit §1071 row; "covered by the lending-records retention rule" is not the same as named retention.

## capital-markets

### Capital-markets sector overlay — section1071-readiness

**Out of scope flag**. Section 1071 is a small-business-lending data-collection rule under ECOA / Regulation B, and capital-markets activity is not the rule's target population. This overlay exists so that a reviewer at a capital-markets entity does not over-extend the readiness work; the sector boundary is named explicitly here.

#### Why capital-markets entities are typically not in §1071 scope

The rule's covered-financial-institution definition under 12 CFR 1002.105 reads against entities that originate covered credit transactions to small businesses. Capital-markets entities — broker-dealers, investment advisers, registered funds, trading venues, central counterparties, central securities depositories, swap dealers, security-based swap dealers — typically do not originate small-business credit transactions in the rule's sense. Securities transactions are excluded under 12 CFR 1002.106(b) [verify subsection]. The rule's data-collection and reporting machinery is built for lenders, not for securities intermediaries.

#### Where a capital-markets entity might still touch §1071

There are narrow cases where an entity operating primarily in capital markets has a §1071 nexus:

- **A broker-dealer or investment adviser whose affiliated entity originates small-business credit** (a private-credit fund's lending vehicle, a wealth-management business's cash-management lending product, a prime-brokerage entity's margin-lending product where extended to a small-business borrower). The CFI determination runs at the originating entity, not at the broker-dealer or adviser; the readiness work follows the lender, not the capital-markets affiliate.
- **A captive or affiliated bank** within a capital-markets-led group. The bank affiliate may itself be a CFI; the readiness work runs at the bank, not at the broader group.
- **A direct-lending business model** where the entity itself originates business loans alongside its capital-markets activity. Run the readiness work as a banking or fintech engagement at that entity.

In all of these, route the engagement to the appropriate sector overlay (`banking.md` or `payments-fintech.md`) at the originating entity, and keep the capital-markets entity itself out of the §1071 readiness perimeter.

#### What this overlay tells the reviewer

- **Do not run a §1071 readiness assessment at a capital-markets entity that does not originate covered credit transactions.** It produces a memo full of "not applicable" rows and a misleading source trace.
- **Surface the boundary in the scoping conversation.** Where the scope flags capital-markets but the underlying question is about a lending affiliate, restate the scope at the lending affiliate and load the appropriate overlay.
- **Where the capital-markets entity has a treasury / liquidity function that extends short-term credit to a small-business counterparty,** the credit-extension question is itself the threshold question and a legal review is appropriate before assuming the §1071 scope.

#### Common errors at capital-markets entities

- Running §1071 readiness as a defensive exercise at an entity that has no covered originations. Time and committee attention are wasted; the readiness memo's correct conclusion is "not a covered financial institution; no §1071 readiness obligation."
- Conflating the capital-markets entity with its lending affiliate when the two operate under separate legal entities with separate registrations. Run the readiness at the lending affiliate.
- Assuming securities-financing transactions (margin lending, securities-based lending) are §1071-reportable. The rule's covered-credit-transaction definition under 1002.106 excludes securities transactions [verify subsection]; surface as an open question for legal where the structure is non-trivial.

#### When this overlay is not enough

If a capital-markets-led group has a meaningful direct-lending or affiliated-bank presence, route to the right capability plugin and the right sector overlay rather than stretching this overlay. `risk-compliance-core` for the group-wide compliance posture; `consumer-compliance-fair-lending` (this plugin) at the lending affiliate with the `banking.md` or `payments-fintech.md` overlay loaded.

## insurance

### Insurance sector overlay — section1071-readiness

**Out of scope flag**. Section 1071 is a small-business-lending data-collection rule under ECOA / Regulation B. Insurance underwriting and claims activity are not credit-extension activities and sit outside the §1071 covered-credit-transaction definition. This overlay exists so that a reviewer at an insurer does not over-extend the readiness work; the sector boundary is named explicitly here.

#### Why insurers are typically not in §1071 scope

The rule's covered-financial-institution definition under 12 CFR 1002.105 reads against entities that originate covered credit transactions to small businesses. Insurance products (commercial property and casualty, commercial liability, workers' compensation, surety, marine, professional liability, cyber insurance, and commercial life) are not credit transactions in the rule's sense. The §1071 readiness machinery does not apply to insurance underwriting, premium-financing referrals, or claims handling.

ECOA itself applies in narrower ways to insurance (notably to credit-life and credit-disability products bundled with credit transactions), but those obligations sit elsewhere; §1071's data-collection-and-reporting scope is the lender's, not the insurer's.

#### Where an insurer might still touch §1071

There are narrow cases where an entity operating primarily in insurance has a §1071 nexus:

- **An affiliated lender within an insurance group** (a captive finance company, a premium-financing subsidiary that extends credit on its own account to small-business borrowers, an affiliated bank). The CFI determination runs at the lending affiliate, not at the insurer; the readiness work follows the lender, not the insurance entity.
- **Premium financing extended directly by the insurer or its agent on terms that constitute a covered credit transaction**. The classification depends on the structure: premium financing offered through an unaffiliated lender (the insurer is not the lender) is the more common pattern, and the readiness work runs at the lender, not the insurer. Where the insurer or an insurance-group affiliate is itself the lender, surface for legal.
- **Surety and credit-insurance products** that resemble credit-extension in their economics. These are typically classified as insurance, not credit, and sit outside §1071; surface as an open question for legal where the structure is non-trivial.

In all of these, route the engagement to the appropriate sector overlay (`banking.md` or `payments-fintech.md`) at the lending affiliate, and keep the insurance entity itself out of the §1071 readiness perimeter.

#### What this overlay tells the reviewer

- **Do not run a §1071 readiness assessment at an insurance entity that does not originate covered credit transactions.** It produces a memo full of "not applicable" rows and a misleading source trace.
- **Surface the boundary in the scoping conversation.** Where the scope flags insurance but the underlying question is about an affiliated lender, restate the scope at the lender and load the appropriate overlay.
- **Where premium financing or credit insurance sits structurally close to credit extension,** the threshold question (is this a covered credit transaction under 1002.106?) is itself the question, and a legal review is appropriate before assuming §1071 scope.

#### Common errors at insurance entities

- Running §1071 readiness as a defensive exercise at an entity that has no covered originations. The correct conclusion is "not a covered financial institution; no §1071 readiness obligation."
- Conflating the insurer with its lending affiliate when the two operate under separate legal entities. Run the readiness at the lending affiliate.
- Assuming premium financing is in scope by default. The classification depends on which entity is the lender and on the structure of the financing arrangement.

#### When this overlay is not enough

If an insurance-led group has a meaningful direct-lending or affiliated-bank presence, route to the right capability plugin and the right sector overlay rather than stretching this overlay. `consumer-compliance-fair-lending` (this plugin) at the lending affiliate with the `banking.md` or `payments-fintech.md` overlay loaded.

## payments-fintech

### Payments-fintech sector overlay — section1071-readiness

When the scope flags payments-fintech, load this overlay alongside `references/source-anchors.md`. Fintech small-business lending sits in §1071 scope where the fintech is the covered financial institution, and sponsor-bank arrangements raise their own attribution question.

#### Sponsor-bank attribution and CFI determination

The first question for a fintech operating under a sponsor bank is which entity is the covered financial institution. The rule looks to the entity extending the credit; in most sponsor-bank arrangements:

- **The sponsor bank is the covered financial institution** for the credit transactions originated under its name on its balance sheet; the sponsor bank's CFI determination (against the revised 1,000-transaction threshold) and the January 1, 2028 compliance date apply.
- **The fintech is the data-collection agent** under the contractual arrangement, with operational responsibility for the application flow, the demographic-collection mechanics, the LOS data capture, and the data-flow back to the sponsor bank for inclusion in the bank's submission.
- **The firewall posture** (12 CFR 1002.108) sits on both sides: the sponsor bank's firewall expectations need to mirror in the fintech's environment, and the fintech's underwriting team (where the fintech does any underwriting work, even if the credit decision is the bank's) cannot have access to demographic data outside the rule's permitted exceptions.

Where the fintech extends credit on its own balance sheet (not under a sponsor-bank arrangement), the fintech is the covered financial institution and the full readiness assessment runs at the fintech.

Surface the sponsor-bank vs. fintech-of-record question in the readiness memo's executive summary; getting it wrong scopes the work to the wrong entity.

#### Merchant cash advance and sales-based financing

§1071 expressly covers merchant cash advance (MCA) and sales-based financing under 12 CFR 1002.106 [verify subsection]. The data-collection mechanics for MCA differ from term-loan capture in ways the readiness work has to surface:

- **Pricing data for sales-based financing** under 1002.107 [verify subsection] includes the *additional cost for merchant cash advance and other sales-based financing* alongside the standard pricing fields. The additional-cost field is computed from the financing structure (purchase price, expected duration, expected delivery rate); systems frequently compute it post-funding from settlement data rather than at origination, sitting as `firm_inferred` capture method rather than `applicant_provided`. This raises downstream amendment-reporting risk: where the actual delivery rate diverges from the expected rate, the additional-cost figure may need to be amended after submission. Surface in the readiness matrix.
- **The application-method and application-recipient fields** for an online MCA flow read against the digital-application convention; capture which channel each row reflects and how returns / referrals from broker channels are coded.
- **Action-taken-date** for MCA flows where approval and funding can be near-instantaneous needs careful design to distinguish *approval* from *origination*.

#### BNPL-for-business edge cases

Buy-now-pay-later for business borrowers (B2B BNPL) is an `edge` product. The boundary against the §1071 covered-credit-transaction definition is non-trivial:

- A B2B BNPL product extending credit to a small business for business purposes is `in` where the credit-extension definition is met.
- Where the product is structured as a payment-deferral or a vendor-financing arrangement that may not constitute credit extension under Reg B, the classification depends on the structure [verify under the current rule text and any CFPB guidance specific to BNPL].
- Sponsor-bank vs. fintech-of-record adds another layer for B2B BNPL operating under a bank partnership.

Surface as an open question for legal in the readiness memo.

#### Vendor LOS readiness for fintechs

Fintech LOS environments are typically vendor-supplied or built in-house with vendor components (KYB / KYC providers, identity-verification vendors, decisioning-engine vendors, demographic-collection-form providers, data-warehouse providers). Each material vendor needs a row in `vendor_readiness[]` with role, attestations, change-control identifier for the §1071-driven change, and the contractual responsibility allocation. The fintech remains responsible for the readiness state regardless of whether the LOS vendor has delivered the capability; the gap list rolls up vendor-driven gaps as `severity = high` or `blocking` where the vendor's roadmap does not align with the firm's compliance-date go-live.

#### Firewall design at fintechs

Fintechs typically run a smaller, flatter access-control environment than a bank. The firewall under 1002.108 reads against:

- **The LOS access controls** for the underwriting team.
- **The data-warehouse access controls** for the analytics, risk, and growth teams (the most material fintech-specific firewall risk: a data-engineering or analytics environment that pulls demographic data into a general-purpose dataset accessible to the broader product team).
- **The customer-support access controls** where customer-support personnel can pull a customer record that includes the demographic data.
- **Any customer-360 dashboard** that aggregates the demographic data alongside other customer attributes.

Firewall-trained-personnel design at fintechs needs explicit attestation; the smaller team sizes can mask the need with informal access conventions, but the rule reads against documented controls.

#### Output-template additions for payments-fintech

- CFI determination section opens with the sponsor-bank attribution question explicitly.
- Product mapping table includes MCA, sales-based financing, B2B BNPL, factoring, and any vendor-financing or payment-deferral product the fintech offers, with the per-product covered-transaction classification and rule-cited rationale.
- Demographic-collection-mechanics section captures the digital-application flow specifics (collection point, refusal-handling, data-flow to the sponsor bank where applicable).
- Firewall section calls out the data-warehouse access controls and the customer-360 dashboard as standing review rows.
- Vendor-readiness section runs longer for fintechs than for banks because more of the LOS stack is vendor-supplied.

#### Common pitfalls in payments-fintech §1071 readiness

- Treating the fintech as the CFI when the sponsor bank is the CFI (or vice versa). Resolve the attribution question first.
- Treating MCA additional-cost capture as `applicant_provided` when the system computes it post-funding from settlement data. Capture method is `firm_inferred` and the amendment-reporting risk surfaces in the readiness memo.
- Coding applicant refusal of demographic data as `null` rather than the rule's required refusal value. Breaks FIG validation and miscodes the refusal.
- Assuming the LOS vendor's product roadmap will deliver §1071 capability in time. Attestation, change-control identifier, and SLA on the data-flow live in `vendor_readiness[]`.
- Missing the data-warehouse firewall risk because the LOS-side firewall is intact. The data-engineering pipeline is the predictable §1071 firewall failure mode at fintechs.
- Treating B2B BNPL as definitionally out of scope. The classification depends on the credit-extension structure and is a legal question, not a default.
