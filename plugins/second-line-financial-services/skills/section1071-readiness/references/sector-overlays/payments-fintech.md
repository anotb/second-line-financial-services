# Payments-fintech sector overlay — section1071-readiness

When the scope flags payments-fintech, load this overlay alongside `references/source-anchors.md`. Fintech small-business lending sits in §1071 scope where the fintech is the covered financial institution, and sponsor-bank arrangements raise their own attribution question.

## Sponsor-bank attribution and CFI determination

The first question for a fintech operating under a sponsor bank is which entity is the covered financial institution. The rule looks to the entity extending the credit; in most sponsor-bank arrangements:

- **The sponsor bank is the covered financial institution** for the credit transactions originated under its name on its balance sheet; the sponsor bank's CFI determination (against the revised 1,000-transaction threshold) and the January 1, 2028 compliance date apply.
- **The fintech is the data-collection agent** under the contractual arrangement, with operational responsibility for the application flow, the demographic-collection mechanics, the LOS data capture, and the data-flow back to the sponsor bank for inclusion in the bank's submission.
- **The firewall posture** (12 CFR 1002.108) sits on both sides: the sponsor bank's firewall expectations need to mirror in the fintech's environment, and the fintech's underwriting team (where the fintech does any underwriting work, even if the credit decision is the bank's) cannot have access to demographic data outside the rule's permitted exceptions.

Where the fintech extends credit on its own balance sheet (not under a sponsor-bank arrangement), the fintech is the covered financial institution and the full readiness assessment runs at the fintech.

Surface the sponsor-bank vs. fintech-of-record question in the readiness memo's executive summary; getting it wrong scopes the work to the wrong entity.

## Merchant cash advance and sales-based financing

§1071 expressly covers merchant cash advance (MCA) and sales-based financing under 12 CFR 1002.106 [verify subsection]. The data-collection mechanics for MCA differ from term-loan capture in ways the readiness work has to surface:

- **Pricing data for sales-based financing** under 1002.107 [verify subsection] includes the *additional cost for merchant cash advance and other sales-based financing* alongside the standard pricing fields. The additional-cost field is computed from the financing structure (purchase price, expected duration, expected delivery rate); systems frequently compute it post-funding from settlement data rather than at origination, sitting as `firm_inferred` capture method rather than `applicant_provided`. This raises downstream amendment-reporting risk: where the actual delivery rate diverges from the expected rate, the additional-cost figure may need to be amended after submission. Surface in the readiness matrix.
- **The application-method and application-recipient fields** for an online MCA flow read against the digital-application convention; capture which channel each row reflects and how returns / referrals from broker channels are coded.
- **Action-taken-date** for MCA flows where approval and funding can be near-instantaneous needs careful design to distinguish *approval* from *origination*.

## BNPL-for-business edge cases

Buy-now-pay-later for business borrowers (B2B BNPL) is an `edge` product. The boundary against the §1071 covered-credit-transaction definition is non-trivial:

- A B2B BNPL product extending credit to a small business for business purposes is `in` where the credit-extension definition is met.
- Where the product is structured as a payment-deferral or a vendor-financing arrangement that may not constitute credit extension under Reg B, the classification depends on the structure [verify under the current rule text and any CFPB guidance specific to BNPL].
- Sponsor-bank vs. fintech-of-record adds another layer for B2B BNPL operating under a bank partnership.

Surface as an open question for legal in the readiness memo.

## Vendor LOS readiness for fintechs

Fintech LOS environments are typically vendor-supplied or built in-house with vendor components (KYB / KYC providers, identity-verification vendors, decisioning-engine vendors, demographic-collection-form providers, data-warehouse providers). Each material vendor needs a row in `vendor_readiness[]` with role, attestations, change-control identifier for the §1071-driven change, and the contractual responsibility allocation. The fintech remains responsible for the readiness state regardless of whether the LOS vendor has delivered the capability; the gap list rolls up vendor-driven gaps as `severity = high` or `blocking` where the vendor's roadmap does not align with the firm's compliance-date go-live.

## Firewall design at fintechs

Fintechs typically run a smaller, flatter access-control environment than a bank. The firewall under 1002.108 reads against:

- **The LOS access controls** for the underwriting team.
- **The data-warehouse access controls** for the analytics, risk, and growth teams (the most material fintech-specific firewall risk: a data-engineering or analytics environment that pulls demographic data into a general-purpose dataset accessible to the broader product team).
- **The customer-support access controls** where customer-support personnel can pull a customer record that includes the demographic data.
- **Any customer-360 dashboard** that aggregates the demographic data alongside other customer attributes.

Firewall-trained-personnel design at fintechs needs explicit attestation; the smaller team sizes can mask the need with informal access conventions, but the rule reads against documented controls.

## Output-template additions for payments-fintech

- CFI determination section opens with the sponsor-bank attribution question explicitly.
- Product mapping table includes MCA, sales-based financing, B2B BNPL, factoring, and any vendor-financing or payment-deferral product the fintech offers, with the per-product covered-transaction classification and rule-cited rationale.
- Demographic-collection-mechanics section captures the digital-application flow specifics (collection point, refusal-handling, data-flow to the sponsor bank where applicable).
- Firewall section calls out the data-warehouse access controls and the customer-360 dashboard as standing review rows.
- Vendor-readiness section runs longer for fintechs than for banks because more of the LOS stack is vendor-supplied.

## Common pitfalls in payments-fintech §1071 readiness

- Treating the fintech as the CFI when the sponsor bank is the CFI (or vice versa). Resolve the attribution question first.
- Treating MCA additional-cost capture as `applicant_provided` when the system computes it post-funding from settlement data. Capture method is `firm_inferred` and the amendment-reporting risk surfaces in the readiness memo.
- Coding applicant refusal of demographic data as `null` rather than the rule's required refusal value. Breaks FIG validation and miscodes the refusal.
- Assuming the LOS vendor's product roadmap will deliver §1071 capability in time. Attestation, change-control identifier, and SLA on the data-flow live in `vendor_readiness[]`.
- Missing the data-warehouse firewall risk because the LOS-side firewall is intact. The data-engineering pipeline is the predictable §1071 firewall failure mode at fintechs.
- Treating B2B BNPL as definitionally out of scope. The classification depends on the credit-extension structure and is a legal question, not a default.
