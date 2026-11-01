# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — cdd-risk-review

When the scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the bank-specific CDD frame the generic capability skill does not own.

#### Operative CIP / CDD rule set

- **31 CFR §1020.220** [verify section] — bank CIP. Identifying-information collection, verification (documentary or non-documentary or both), recordkeeping and retention (five-year posture), comparison against government lists.
- **FinCEN CDD Final Rule (May 2016, compliance May 11, 2018)** [verify section] — applied to banks across the four pillars.
- **31 CFR §1010.230** — beneficial ownership for legal-entity bank customers.
- **31 CFR §1010.610** [verify section] — enhanced due diligence for correspondent accounts for foreign financial institutions. Risk-assessment framework; EDD elements; the foreign-bank-account due-diligence program.
- **31 CFR §1010.620** [verify section] — enhanced due diligence for private-banking accounts. Source-of-funds inquiry; scrutiny for senior foreign political figures.
- **FFIEC BSA/AML Examination Manual — CDD section and Beneficial Ownership section** [verify section anchors] — examiner-facing detail.

#### Bank-specific risk drivers the QA reads in the file

- **Cash-intensive businesses.** Convenience stores, restaurants, car washes, laundromats, parking, certain entertainment venues, certain retail. A "small business with cash deposits" label is not a rated decision; the QA reads whether the file evidences the cash intensity (industry profile, expected cash volumes quantified, customer-stated rationale, any CTR pattern history) and whether the rating drivers tie to that evidence.
- **MSB customers of a bank.** Banking an MSB carries customer-CDD obligations that are heavier than the customer-segment label implies. The QA reads whether the MSB customer's own AML program is on file (where the bank's program asks for it), whether the MSB's business model is documented, and whether the expected-activity profile reflects the MSB's customer base.
- **Marijuana-related businesses (MRBs).** Where the bank serves MRBs, the FinCEN MRB guidance (FIN-2014-G001) [verify date and current effectiveness] sets the program-level expectations; the CDD QA reads whether the MRB-specific CDD elements (state licensing, ongoing-monitoring scope, ongoing review of public sources) are on file.
- **Politically exposed persons (PEPs) and PEP-adjacent.** Domestic-PEP and foreign-PEP profiles carry program-level EDD obligations; the QA marks `edd_status` accordingly and cross-references `edd-escalation-pack`.
- **Correspondent and private-banking accounts.** Read against `§1010.610` and `§1010.620` directly. The QA scopes the rule first; banks frequently mis-apply the foreign-correspondent rule (it is for accounts maintained for foreign FIs, not for any wire counterparty).
- **Complex-structure entities.** Multi-tier ownership, foreign holding companies, trust intermediaries, family-office structures. The beneficial-ownership read on these customers is harder than the certification form alone supports; the QA reads for inconsistency between the certification and any other file evidence.
- **Trade-based money-laundering exposure.** Commercial customers with international counterparties; the expected-activity profile should reflect trade flows specifically enough to evaluate alerts against.

#### Refresh cadence at a bank

The CDD Final Rule does not set a uniform refresh cadence; refresh is on a risk basis and the institution's program defines the cycle. The QA reads against the program's cycle, not against an external default. Common bank patterns: high-risk annually; medium-risk every two to three years; low-risk on event only or on a longer cycle. The QA flags refresh-cycle adherence when the cycle is missed.

#### Bank-specific CIP nuances

- **Joint accounts.** CIP applies to each customer; the file should evidence both.
- **Trust accounts.** Trust-customer scope under CIP is the trust itself; the trustee is not the customer for CIP purposes but is the operative actor for verification. Beneficial ownership under `§1010.230` does not apply to trusts as legal-entity customers; trust-specific due diligence sits in the institution's program.
- **Sole proprietors and DBAs.** Sole proprietors are individuals for CIP purposes and not legal-entity customers under `§1010.230`. The QA scopes the rule before applying the beneficial-ownership pillar.
- **Online-only / non-face-to-face onboarding.** Verification method weighs more heavily; non-documentary verification methods should be evidenced specifically (database matching, public-record corroboration, reference checks where the program calls for them).

#### Cross-link inside the plugin

- **`edd-escalation-pack`** carries the EDD pack itself. The CDD QA marks `edd_status` and cross-references; it does not produce the EDD pack.
- **`sar-decision-qa`** reads the customer's CDD posture as context when an alert closes against the same customer. A CDD-segment-mismatch finding at the SAR-decision level is a CDD QA cross-reference.
- **`negative-news-triage`** carries adverse-media triage. An event-driven CDD refresh triggered by negative news consumes the triage record as input.
- **`aml-model-monitoring`** carries monitoring scenario tuning. A CDD finding tagged to expected-activity-versus-monitoring-scope mismatch routes to `aml-model-monitoring`; the CDD QA does not re-tune scenarios.
- **`sanctions-screening-qa`** carries sanctions-screening match disposition. A sanctions-hit-triggered CDD refresh consumes the screening QA record as input.

#### Common pitfalls in banking CDD reviews

- Treating CIP completeness as CDD completeness. CIP is Pillar 1; the QA reads all four pillars separately.
- Reading the foreign-correspondent rule (`§1010.610`) on customers that are not foreign FIs.
- Missing the inconsistency check between the beneficial-ownership certification and the rest of the file (entity filings, signatories, transactional patterns).
- Letting risk-rating drivers stand as labels without evidence linkage ("cash-intensive", "international", "PEP-adjacent" with nothing underneath).
- Generic expected-activity boilerplate ("general business banking") that cannot drive monitoring scenario tuning.
- Asserting BOI filing status under `§1010.380` without an as-of date and a rule-state read on that date; the CTA implementing rule has live litigation history.
- Treating sole proprietors, trusts, or unincorporated associations as legal-entity customers under `§1010.230`.

## capital-markets

### Capital-markets sector overlay — cdd-risk-review

When the scope flags capital markets (broker-dealer, mutual fund, FCM/IB, covered investment adviser), load this overlay alongside `references/source-anchors.md`. It carries the capital-markets-specific CDD frame the generic capability skill does not own.

#### Operative CIP / CDD rule set

- **31 CFR §1023.220** [verify section] — broker-dealer CIP.
- **31 CFR §1024.220** [verify section] — mutual-fund CIP.
- **31 CFR §1026.220** [verify section] — FCM and IB CIP.
- **FinCEN CDD Final Rule (May 2016)** [verify section] — applies to broker-dealers, mutual funds, and FCMs/IBs across the four pillars.
- **31 CFR §1010.230** — beneficial ownership for legal-entity customers across the same institution set.
- **FinCEN AML / CFT Programs and SAR Rule for Registered Investment Advisers and Exempt Reporting Advisers (Final Rule, August 2024)**. **IA AML Rule effective date delayed to January 1, 2028 (FinCEN final rule January 2, 2026; 91 FR 14) — superseding the original January 1, 2026 effective date.** Until the effective date, the rule's obligations are not enforceable against RIAs / ERAs. Brings covered investment advisers within the BSA regime when operative; CDD and beneficial-ownership obligations extend to covered advisers under the rule's scope and timing.

#### Capital-markets-specific risk drivers the QA reads

- **High-net-worth individuals with international exposure.** Source-of-wealth statements should be corroborated by independent file evidence (public-record search, prior-firm reference where appropriate, asset documentation), not stand alone as customer self-attestation. Stale source-of-wealth statements at periodic refresh are a common gap.
- **Foreign omnibus accounts and intermediated holdings.** Where the customer is a foreign financial intermediary holding for underlying clients, the CDD work extends to the intermediary's CDD-equivalent posture; the QA reads whether the file evidences the intermediary's own program and the look-through posture for high-risk underlying clients.
- **Pooled investment vehicles and private funds.** Some pooled-investment-vehicle customers are exempt from the beneficial-ownership rule under `§1010.230`'s exemption list; the QA scopes the exemption before applying or skipping the pillar. Where the fund is not exempt, the beneficial-ownership read applies.
- **PEPs and senior foreign political figures.** Private-wealth and prime-brokerage customer populations carry elevated PEP exposure. The QA marks `edd_status` and cross-references `edd-escalation-pack`.
- **Correspondent broker-dealer accounts.** Broker-dealers maintaining accounts for foreign broker-dealers operate under the foreign-correspondent EDD frame; read against `§1010.610` where the rule applies.
- **Day-trading and high-velocity retail customers.** Expected-activity profiles should reflect the velocity and the strategy; a generic "active trading" profile is not specific enough to drive monitoring on layering, manipulation-adjacent, or wash-trade typologies.
- **Insider-account proximity.** Customers with reporting-officer or large-shareholder status at issuers carry insider-trading-monitoring obligations adjacent to CDD; the QA notes the cross-reference but does not handle insider-trading surveillance here.

#### Investment-adviser scope discipline

Until the FinCEN adviser AML rule's compliance date is operative for the customer's adviser, advisers do not have a stand-alone CDD obligation under the rule. Where the adviser's customers are also clients of an affiliated broker-dealer or fund, the affiliated entity's CDD program may carry the obligation. The QA dates the read and scopes the rule's effective state on that date.

#### Beneficial ownership in capital-markets contexts

Beneficial-ownership work on broker-dealer, mutual-fund, and FCM/IB legal-entity customers follows `§1010.230` directly. The exemption list matters: publicly traded companies, certain regulated entities, certain pooled investment vehicles, and others are out of scope under the rule. The QA reads the exemption claim against the rule, not as a default. Custody, omnibus, and intermediated accounts have their own exemption posture; read carefully.

#### CIP nuances in capital markets

- **Account openings via introducing broker.** Where the introducing broker collects CIP information and the carrying broker maintains the record, the program contract allocation matters. The QA reads whether both ends of the arrangement have done the allocated work.
- **Mutual-fund accounts opened through an intermediary.** The intermediary may be the customer for CIP purposes (an omnibus account), or each underlying customer may be the customer (a direct account). The QA scopes which.
- **Cross-border customer onboarding.** Verification corroboration for non-US-resident customers is harder; the QA reads whether the file evidences the corroboration work.

#### Refresh cadence in capital markets

The CDD Final Rule does not set a uniform refresh cadence. Capital-markets programs commonly refresh on event and on a longer time-based cycle for risk-tiered customers; the QA reads against the firm's program. Source-of-wealth refresh is the most common gap on high-net-worth periodic reviews.

#### Cross-link inside the plugin

- **`edd-escalation-pack`** for PEPs, private-banking-equivalent customers, foreign-correspondent BD relationships, complex-structure entities.
- **`sar-decision-qa`** for downstream alert-decision QA on capital-markets typologies (layering, structuring, wash-trade-adjacent, insider-trading-adjacent where AML overlaps).
- **`negative-news-triage`** for adverse-media-triggered refresh on high-net-worth customers.
- **`sanctions-screening-qa`** for sanctions-hit-triggered refresh.
- **`aml-model-monitoring`** for monitoring scenario tuning where expected-activity-versus-scope mismatch surfaces.

#### Common pitfalls in capital-markets CDD reviews

- Treating customer self-attestation on source of wealth as evidence; corroboration belongs in the file.
- Stale source-of-wealth statements at periodic refresh on long-tenured high-net-worth customers.
- Reading the foreign-correspondent rule on customers that are not foreign broker-dealers or foreign FIs.
- Missing the look-through posture on foreign omnibus accounts where the program calls for it.
- Asserting beneficial-ownership exemption under `§1010.230` without scoping the exemption against the rule's list.
- Generic expected-activity profiles for high-velocity or strategy-specific customers that cannot drive monitoring on the relevant typologies.
- Asserting investment-adviser CDD obligations before the FinCEN adviser rule's compliance date is operative for that adviser.

## insurance

### Insurance sector overlay — cdd-risk-review

When the scope flags insurance, load this overlay alongside `references/source-anchors.md`. It carries the insurance-specific CDD frame the generic capability skill does not own. The CDD review applies only to covered products under the operative rule; many insurance products are outside scope.

#### Operative CIP / CDD rule set

- **31 CFR §1025.210** [verify section] — AML program rule for insurance companies. Defines the covered products and scopes the program obligation.
- **31 CFR §1025.220** [verify section] — CIP for insurance companies; applies to covered-product customers.
- **FinCEN CDD Final Rule (May 2016)** [verify section] — applies to insurance companies for covered products.
- **31 CFR §1010.230** — beneficial ownership for legal-entity covered-product customers.

#### Covered-product scope — the QA's first read

Covered products are, generally: permanent life insurance with cash value (other than group), annuity contracts (other than group), and other insurance products with features of cash value or investment. P&C, term life without cash value, group life, group annuity, health, disability, title, and most reinsurance are outside the rule's scope. The QA scopes the product before applying any pillar. A CDD review on a P&C-only customer is out of scope; a CDD review on a customer with both covered and non-covered products is in scope only for the covered products.

#### Insurance-specific risk drivers the QA reads

- **Single-premium and large-premium covered products.** Lump-sum funding of permanent life or annuity contracts at scale carries elevated ML risk; expected-activity profile (premium pattern, source of funds) should be specific.
- **Free-look-period surrenders and early surrenders.** Pattern of early surrender on covered products is a typology indicator the program monitors; the QA reads whether the customer's profile and the expected-activity-profile reflect surrender posture if relevant.
- **Third-party premium funding and assignment of benefit / contract.** Third-party-funded covered products and contract assignments to third parties carry ML risk; the QA reads whether the file documents the third-party relationship.
- **PEPs and senior foreign political figures.** Wealth-transfer covered products attract PEP exposure; the QA marks `edd_status` and cross-references `edd-escalation-pack`.
- **Cross-border policyholders and beneficiaries.** Geography of policyholder and beneficiary should be documented; high-risk jurisdiction exposure on either end is an EDD-trigger candidate.

#### Distribution-channel nuances

- **Independent-agent / broker distribution.** The agent collects CIP and CDD information at point of sale; the insurance company is the institution of record. The QA reads whether the agent's collection has been reviewed by the insurer and whether the insurer's program evidences the oversight posture.
- **Direct-to-consumer and online distribution.** Verification corroboration weighs more heavily; the QA reads non-documentary verification specifically.
- **Group-structured contracts with covered features.** Some group products may have covered-product features for individual certificate holders; the QA scopes whether each certificate holder is in scope under the rule.

#### Beneficial ownership in insurance contexts

Beneficial-ownership work applies to legal-entity covered-product customers under `§1010.230`. The customer is the policyholder, not the beneficiary; the beneficial-ownership read is on the legal-entity policyholder. Where the policyholder is an individual, the rule does not apply. Where the policyholder is a trust, the trust-customer scope is what it is in banking — trusts are not "legal entity customers" under `§1010.230`, and trust-specific due diligence sits in the institution's program.

#### Cross-link inside the plugin

- **`edd-escalation-pack`** for PEPs, large-premium covered products, complex-structure policyholder entities, third-party-funded contracts.
- **`sar-decision-qa`** for downstream alert-decision QA on insurance typologies (early-surrender patterns, third-party assignments, premium-funding anomalies).
- **`negative-news-triage`** for adverse-media-triggered refresh on high-value covered-product customers.
- **`sanctions-screening-qa`** for sanctions-hit-triggered refresh on policyholders or beneficiaries.

#### Common pitfalls in insurance CDD reviews

- Applying the rule to non-covered products (P&C, term life without cash value, group products, health). The QA scopes the product first.
- Treating the agent's CIP collection as the insurer's record without evidence the insurer reviewed and accepted it.
- Missing the third-party-funding or assignment-of-contract documentation where the customer is funded or controlled by a third party.
- Generic expected-activity / expected-premium profiles that cannot drive monitoring on the early-surrender or third-party-funding typologies.
- Reading beneficial-ownership on individual or trust policyholders where the rule does not apply.

## payments-fintech

### Payments-fintech sector overlay — cdd-risk-review

When the scope flags payments or fintech (sponsor-bank model, licensed MSB, payment processor, BaaS arrangement, neobank), load this overlay alongside `references/source-anchors.md`. It carries the fintech-and-payments CDD frame the generic capability skill does not own.

#### Operative CIP / CDD frame for fintech

The applicable rule set depends on the regulatory perimeter the fintech sits inside:

- **Sponsor-bank (BaaS) model.** The sponsor bank is the institution of record for CIP, CDD, and the BSA/AML program. The fintech operates under the sponsor's program contract. The QA reads against the sponsor's program (which itself reads against `31 CFR §1020.220` and the CDD Final Rule), not against a fintech-only standard. The program contract typically allocates CIP collection, identity verification, beneficial-ownership data capture, ongoing monitoring, and SAR detection across the sponsor and the fintech; the QA reads whether the file evidences the allocated work.
- **Licensed MSB.** MSBs operate under `31 CFR §1022.210` (AML program rule) and `§1022.320` (SAR rule). MSBs are not subject to a stand-alone CIP rule of the `§1020.220` form; the institution's CIP-equivalent program applies. The QA reads the program against the customer file. Money-transmitter customer onboarding, agent-of-payee considerations, and cross-border remittance posture set the expected-activity-profile depth.
- **OCC-chartered fintech / state-chartered fintech bank / industrial loan company.** Same rule set as a bank under `§1020.220` and the CDD Final Rule. Read against the bank overlay where the institution holds a bank charter.
- **Payment processor.** Where the processor is not itself an FI under the BSA, the customer-due-diligence work sits with the sponsor bank; the processor's KYB / KYC operations may inform the bank's CDD file but do not substitute for it.

#### Sponsor-bank delineation — the QA's first read

Before reading the file pillar by pillar, the QA confirms which entity is the institution of record and what the program contract allocates. A common defect: the file presents the fintech's onboarding flow as the institution's CIP record without evidence that the sponsor bank reviewed and accepted it. Where the program contract assigns ongoing monitoring to the fintech, the QA reads whether the bank has a documented oversight posture (monitoring of the fintech's monitoring), not just a contractual allocation. The CFPB's interagency 2023 third-party guidance and the FRB / OCC / FDIC sponsor-bank-program supervision posture frame the bank-side oversight expectation.

#### Fintech-specific risk drivers the QA reads

- **Onboarding velocity vs CDD depth.** Fintech onboarding is fast; CDD depth has to keep up. A 90-second onboarding flow is not a defect by itself, but it is a defect when the file evidences no human review, no verification corroboration on flagged cases, and no escalation route. The QA reads whether risk-tier branching is evidenced in the flow.
- **Synthetic-identity and first-party-fraud exposure.** Non-face-to-face onboarding at scale carries elevated synthetic-identity risk. The QA reads whether non-documentary verification (database matching, public-record corroboration, device intelligence, behavioural signals) is evidenced for the customer, and whether the file reflects any flag-and-resolve activity from the verification stack.
- **Crypto-adjacent customer activity.** Fintech customers transacting with virtual-asset service providers, mixers, or chain-hopping intermediaries carry typology-specific monitoring expectations. The QA reads whether the expected-activity profile reflects this exposure and whether the monitoring scope picks it up.
- **Agent-of-payee and merchant-acquiring exposure.** Where the fintech's customer is itself a merchant or sub-merchant, the CDD scope extends to the merchant's business model and the underlying transaction flow. The QA reads whether merchant-category-code, expected-volume, and chargeback-history exposure are evidenced.
- **Cross-border remittance exposure.** Money-transmitter and cross-border-payment customers carry geography-and-corridor-specific risk. The QA reads whether the expected-activity profile reflects the corridors actually transacted.

#### Beneficial ownership in fintech contexts

Beneficial-ownership work on fintech customers (legal-entity customers under `§1010.230`) is the same rule, but the evidence stack is often thinner because the onboarding is non-face-to-face and the verification corroboration is data-stack rather than document-stack. The QA reads whether the certification is on file, whether the verification of the named individuals is corroborated (document upload, identity-verification stack, ID-document liveness), and whether the file's transactional pattern is consistent with the certification. Where the customer is a small LLC with one named beneficial owner, the file should still evidence the verification work; the certification form alone is the form, not the verification.

#### BOI reporting status — the dating discipline

`31 CFR §1010.380` BOI reporting status applies to many small fintech LLC customers. The Corporate Transparency Act's implementing rule has live litigation history; the QA marks `boi_filing_status` with an as-of date and the rule-state read on that date. A fintech CDD file from early 2024 reads differently from one from late 2024 or from later periods, and the QA does not assert without grounding.

#### Cross-link inside the plugin

- **`edd-escalation-pack`** for high-risk fintech customers (PEP-adjacent, large MSB customers, complex-structure entities, jurisdictions of concern).
- **`sar-decision-qa`** for downstream alert-decision QA on the same customer.
- **`aml-model-monitoring`** for monitoring scenario tuning where expected-activity-versus-scope mismatch surfaces.
- **`sanctions-screening-qa`** for sanctions-hit-triggered refresh.
- **`negative-news-triage`** for adverse-media-triggered refresh.

#### Common pitfalls in fintech CDD reviews

- Reading the fintech's onboarding artifact as the sponsor bank's CIP record without evidence the sponsor reviewed and accepted it.
- Treating the program contract's allocation of work as evidence the work was done.
- Letting onboarding velocity carry through to a "CDD complete in 90 seconds" file without evidence of human review, escalation, or verification corroboration on flagged cases.
- Generic expected-activity profiles that cannot drive monitoring scenario tuning on fintech customer behavior (high-volume P2P, crypto-adjacent flows, cross-border corridors).
- Asserting BOI filing status without an as-of date and a current rule-state read.
- Missing the bank-side oversight posture on a sponsor-bank arrangement (the bank monitors the fintech's CDD work; that monitoring is itself in scope of the bank's CDD review).
