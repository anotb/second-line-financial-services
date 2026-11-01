# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Banking sector overlay — edd-escalation-pack

When the scope flags banking, load this overlay alongside `references/source-anchors.md`. It carries the bank-specific EDD frame the generic capability skill does not own. The two regulator-driven EDD frames in banking are private banking (`§1010.620`) and foreign correspondent banking (`§1010.610`); both interact with PEP and Section 311 / 312 considerations.

#### Operative EDD rule set in banking

- **31 CFR §1010.620** [verify section] — Due diligence programs for private-banking accounts. Applies to a US bank or federally insured branch maintaining a private-banking account for a non-US person where the account meets the rule's threshold and characteristics. Source-of-funds inquiry; scrutiny of activity; senior-foreign-political-figure handling; reporting and recordkeeping.
- **31 CFR §1010.610** [verify section] — Due diligence programs for correspondent accounts for foreign financial institutions. EDD elements for foreign-FI correspondents: ownership; products and services offered to non-US persons; AML/CFT regime in the foreign FI's home country; public information on the foreign FI; nested-correspondent posture; payable-through-account considerations.
- **31 USC §5318(i)** [verify section] — Section 312 statutory underpinning for both `§1010.620` and `§1010.610`.
- **31 USC §5318A** [verify section] — Section 311 special measures. Where Treasury has designated a jurisdiction, an FI, or a class of transactions as of primary money-laundering concern, the special measures interact with the bank's EDD obligations and the products and services it can offer the customer. The pack reads the designation status against the customer's exposure where applicable.
- **FFIEC BSA/AML Examination Manual** sections on PEPs, Private Banking Due Diligence, and Correspondent Accounts (Foreign) [verify section anchors].

#### Bank-specific EDD trigger profiles

- **Private-banking customers (non-US person at threshold).** `§1010.620` is the rule frame. The pack reads source-of-funds inquiry on each meaningful funding event, ongoing scrutiny on activity, the heightened scrutiny path on senior-foreign-political-figure relationships, and the program elements the bank applies. A US-person private-banking customer is outside the rule's scope, but the bank's program may apply parallel EDD on a risk basis; the pack reads against the program in that case and notes that `§1010.620` does not apply on the US-person leg.
- **Foreign correspondent accounts.** `§1010.610` is the rule frame. The pack walks the EDD elements: respondent ownership, products and services the respondent offers to non-US persons, AML/CFT regime in the respondent's home country (FATF mutual-evaluation public reports are the cleanest public source), publicly available information on the respondent (regulatory standing, enforcement history, ownership changes, sanctions exposure), and the nested-correspondent posture (whether the respondent provides correspondent services to other banks, and the resulting indirect exposure). Wolfsberg CBDDQ is the industry-standard questionnaire structure most respondents complete; the pack reads the respondent's CBDDQ as one input, not as standalone evidence.
- **PEP and PEP-adjacent profiles.** The 2020 joint statement clarifies that PEP status alone does not require EDD; the bank applies EDD on a risk basis. The pack records the PEP determination, the source of the finding (commercial PEP-screening tool, public source, customer disclosure, regulator notice), the date of the assessment, and the risk-based judgment that triggered EDD on this customer. Senior foreign political figures in private-banking accounts carry the heightened scrutiny path under `§1010.620` directly.
- **Cash-intensive businesses with elevated drivers.** Cash intensity alone is a CDD-rating driver; EDD escalation is warranted when cash intensity combines with other drivers (geography of concern, complex ownership, undisclosed beneficial control, structuring patterns in transaction history). The pack reads the combination, not the cash intensity alone.
- **Marijuana-related businesses (MRBs).** Where the bank serves MRBs, FinCEN MRB guidance (FIN-2014-G001) [verify date and current effectiveness] sets the program-level expectations. EDD on an MRB customer reads against the MRB-specific elements (state licensing, ongoing-monitoring scope, public-source posture) on top of the standard EDD frame.
- **MSB customers of a bank.** Banking an MSB carries customer-CDD obligations heavier than the segment label implies. EDD escalation on an MSB customer reads the MSB's own AML program (where the bank's program asks for it), the MSB's business model, the MSB's customer base by jurisdiction, and the consistency of the MSB's expected-activity profile with its actual transactional pattern.
- **Complex-structure entities.** Multi-tier ownership, foreign holding companies, trust intermediaries, family-office structures. The beneficial-ownership read on these customers is harder than the certification form alone supports; the pack walks the chain layer by layer with explicit residual uncertainty per layer.
- **Section 311 special-measures-adjacent customers.** Where a customer's transactional flow, counterparties, or jurisdictional exposure intersects with a Section 311 designation, the pack reads the designation's measures (special information requirements, prohibition on certain account types, reporting requirements) against the customer's product mix.

#### Section 312 EDD elements for foreign correspondent accounts — the walk

The pack follows the rule's elements explicitly:

1. **Respondent ownership.** Names of the foreign FI's owners (where required to be obtained); ownership changes since the last refresh.
2. **Respondent's products and services to non-US persons.** What the respondent offers, particularly products that obscure identity (numbered accounts, certain pooled vehicles).
3. **AML/CFT regime in the respondent's home country.** The pack consults the FATF mutual-evaluation public report for the jurisdiction (when available) for an outside-in read on regime effectiveness; FATF grey/black-list status where applicable; the home-country regulator's public posture on the respondent (regulatory standing, supervisory action history).
4. **Public information on the respondent.** Enforcement history, news coverage on AML / sanctions / fraud / market-conduct exposure, ownership changes, recent supervisory action.
5. **Nested-correspondent posture.** Whether the respondent provides correspondent services to other banks and, if so, what disclosure the respondent has provided on its downstream correspondent customer base.
6. **Payable-through-account considerations.** Where the respondent's account permits its customers to engage in banking activities directly through the respondent's account, the heightened-scrutiny path applies.

#### Cross-link inside the plugin

- **`cdd-risk-review`** is the upstream baseline; the EDD pack consumes the CDD QA's `edd_status = required_pending` or `borderline` cases.
- **`negative-news-triage`** triages adverse media on the customer; the EDD pack consumes triaged hits and does not re-triage.
- **`sanctions-screening-qa`** disposes screening matches on the customer and connected parties; the EDD pack consumes screening QA outputs.
- **`aml-model-monitoring`** owns scenario tuning; the EDD pack flags scenario-tuning implications for the post-EDD profile and cross-references.
- **`sar-decision-qa`** sits downstream where an alert closes against this customer.

#### Common pitfalls in banking EDD packs

- Reading the foreign-correspondent rule (`§1010.610`) on a customer that is not a foreign FI; the rule has a defined scope.
- Reading `§1010.620` private-banking elements on a US-person private-banking customer where the rule does not apply (the bank's program may still impose parallel EDD; the pack notes the program basis, not the rule basis).
- Treating PEP status as automatically EDD-required; the 2020 joint statement frames PEP status as a risk indicator, not an automatic trigger.
- Stopping at the beneficial-ownership certification form on a complex-structure entity rather than walking the chain to the trusts, nominees, and foreign holding intermediaries.
- Treating the respondent's CBDDQ as standalone evidence in a foreign-correspondent EDD pack rather than as one input on top of the rule's elements.
- Missing the nested-correspondent disclosure on a foreign-correspondent relationship (the indirect exposure through the respondent's customer base by jurisdiction is a load-bearing finding).
- Asserting a Section 311 special-measures position on a customer without a current read of the designation's status and the measures it imposes.

## capital-markets

### Capital-markets sector overlay — edd-escalation-pack

When the scope flags capital markets (broker-dealer, mutual fund, FCM/IB, covered investment adviser), load this overlay alongside `references/source-anchors.md`. It carries the capital-markets-specific EDD frame the generic capability skill does not own. Private-banking and prime-brokerage customer populations carry the heaviest EDD load in this sector; investment-adviser EDD obligations are evolving with the FinCEN adviser AML rule.

#### Operative EDD rule set in capital markets

- **31 CFR §1010.610** [verify section] — Foreign-correspondent EDD applies where a broker-dealer maintains accounts for foreign broker-dealers or other foreign FIs that meet the rule's definition.
- **31 CFR §1010.620** [verify section] — Private-banking EDD applies where the broker-dealer maintains a private-banking-equivalent account for a non-US person at the rule's threshold; many wealth-management arms read against `§1010.620` directly.
- **FinCEN CDD Final Rule (May 2016)** [verify section] — applies to broker-dealers, mutual funds, and FCMs/IBs across the four pillars; EDD on higher-risk customers is on a risk basis.
- **31 CFR §1010.230** — beneficial ownership for legal-entity customers; the EDD pack walks the chain layer by layer.
- **FinCEN Anti-Money Laundering / Countering the Financing of Terrorism Programs and Suspicious Activity Reports for Registered Investment Advisers and Exempt Reporting Advisers** (Final Rule, August 2024). **IA AML Rule effective date delayed to January 1, 2028 (FinCEN final rule January 2, 2026; 91 FR 14) — superseding the original January 1, 2026 effective date.** Until the effective date, the rule's obligations are not enforceable against RIAs / ERAs. Brings covered investment advisers within the BSA regime when operative; EDD obligations extend to covered advisers under the rule's scope and timing.
- **FFIEC BSA/AML Examination Manual** sections on PEPs, Private Banking Due Diligence, and Customer Due Diligence [verify section anchors] — examiner-facing detail; relevant to broker-dealer practice through industry application even where the manual's primary audience is banks.

#### Capital-markets-specific EDD trigger profiles

- **High-net-worth individuals with international exposure (private wealth, prime brokerage).** Source-of-wealth and source-of-funds work is the core EDD load. Customer self-attestation on SoW is the customer's claim; corroboration is what other file evidence provides (public-record search, prior-firm reference where appropriate, asset documentation, business-sale documentation, family-trust deeds, employment / role history). Stale SoW statements at periodic refresh are the dominant defect; the EDD pack refreshes the SoW with corroboration on a high-net-worth EDD escalation.
- **Foreign omnibus accounts and intermediated holdings.** Where the customer is a foreign financial intermediary holding for underlying clients, the EDD work extends to the intermediary's CDD-equivalent posture and the look-through posture for high-risk underlying clients (where the intermediary's program supports look-through).
- **Pooled investment vehicles and private funds (non-exempt).** Where the fund is not exempt under `§1010.230` and is also a higher-risk customer (offshore feeder, complex-structure parent, jurisdictional concentration), the EDD pack walks the beneficial-ownership chain through the fund structure to the control parties.
- **PEPs and senior foreign political figures in private wealth.** Same risk-based PEP framing as banking; the 2020 joint statement applies. Senior foreign political figures in private-banking-equivalent accounts carry the heightened scrutiny path under `§1010.620` directly.
- **Foreign correspondent broker-dealer accounts.** Broker-dealers maintaining accounts for foreign broker-dealers operate under the foreign-correspondent EDD frame; read against `§1010.610`. The EDD pack walks the rule's elements (respondent ownership, products and services, AML/CFT regime in the home country, public information, nested-correspondent posture).
- **Microcap and low-priced-securities concentration customers.** Customers with concentrated activity in low-priced or microcap securities, or with deposit-and-sale patterns characteristic of unregistered-distribution typologies, are EDD candidates. The pack reads the typology against the customer's profile and SoW.
- **Insider-account proximity.** Customers with reporting-officer or large-shareholder status at issuers carry insider-trading-monitoring obligations adjacent to EDD; the pack notes the cross-reference but does not handle insider-trading surveillance here.
- **Day-trading and high-velocity retail customers in EDD escalation.** Where EDD is triggered (PEP exposure, jurisdictional exposure, structuring patterns, complex-structure entity), the pack reads the trading strategy and the velocity against the customer's profile and SoW.

#### Investment-adviser EDD discipline

Until the FinCEN adviser AML rule's compliance date is operative for the customer's adviser, advisers do not have a stand-alone CDD or EDD obligation under the rule. Where the adviser's customers are also clients of an affiliated broker-dealer or fund, the affiliated entity's program may carry the EDD obligation. The pack dates the read and scopes the rule's effective state on that date for the adviser in question; an EDD pack drafted in early 2026 reads differently from one drafted later as the rule's compliance dates flow through.

#### Beneficial ownership in capital-markets EDD

Beneficial-ownership work on broker-dealer, mutual-fund, and FCM/IB legal-entity customers follows `§1010.230` directly. The exemption list matters: publicly traded companies, certain regulated entities, certain pooled investment vehicles, and others are out of scope. The EDD pack reads the exemption claim against the rule. For non-exempt complex-structure entities, the pack walks the chain layer by layer and surfaces residual uncertainty per layer.

#### Source-of-wealth corroboration — the EDD walk

For a high-net-worth EDD pack, the SoW work is the load-bearing element:

1. **Customer statement.** Paraphrase from the customer-supplied statement; do not quote unless verbatim is in the file.
2. **Categorise the wealth source.** Inherited; business sale or stake; long-term professional earnings; investment returns; trust distributions; political role compensation (for a PEP or family member); other.
3. **Match corroboration to the category.** Inherited wealth: probate documentation, family-trust deeds, prior-firm reference. Business sale: transaction documentation, public-source confirmation of the transaction, attestation from advising counsel where in scope. Long-term professional earnings: employment history, public-source role confirmation. Investment returns: prior-firm statements, fund documentation. Trust distributions: trust deed and distribution history.
4. **Independent corroboration confidence.** High where multiple independent sources align; medium where one source is independent and the rest are customer-supplied; low where corroboration is thin.
5. **Residual gaps.** Mark explicitly; do not infer.

#### Cross-link inside the plugin

- **`cdd-risk-review`** is the upstream baseline.
- **`negative-news-triage`** for adverse-media triage on high-net-worth customers (the dominant trigger for EDD refresh in private wealth).
- **`sanctions-screening-qa`** for sanctions-screening QA on customers and counterparties.
- **`aml-model-monitoring`** for monitoring scenario tuning where post-EDD profile changes implicate scenario calibration (layering, structuring, microcap-deposit-and-sale typologies).
- **`sar-decision-qa`** sits downstream where an alert closes against the customer.

#### Common pitfalls in capital-markets EDD packs

- Treating customer self-attestation on source of wealth as evidence; corroboration belongs in the file.
- Stale SoW statements left in place at EDD refresh on long-tenured high-net-worth customers; refresh is the EDD pack's job at escalation.
- Reading the foreign-correspondent rule on customers that are not foreign broker-dealers or foreign FIs.
- Missing the look-through posture on foreign omnibus accounts where the program supports it.
- Asserting beneficial-ownership exemption under `§1010.230` without scoping the exemption against the rule's list.
- Treating an investment-adviser customer as in scope before the FinCEN adviser rule's compliance date is operative for that adviser.
- Treating PEP status as automatically EDD-required (the 2020 joint statement frames it as risk-based).
- Importing prior-firm-reference attestations as standalone corroboration on SoW (a prior-firm reference is one input on top of independent public-source or transactional documentation).

## insurance

### Insurance sector overlay — edd-escalation-pack

When the scope flags insurance, load this overlay alongside `references/source-anchors.md`. It carries the insurance-specific EDD frame the generic capability skill does not own. EDD escalations apply only to covered products under the operative rule; many insurance products are outside scope.

#### Operative rule set in covered insurance

- **31 CFR §1025.210** [verify section] — AML program rule for insurance companies. Defines covered products and scopes the program obligation; EDD escalations sit on the program for covered-product customers.
- **31 CFR §1025.220** [verify section] — CIP for insurance companies; applies to covered-product customers.
- **FinCEN CDD Final Rule (May 2016)** [verify section] — applies to insurance companies for covered products; EDD on higher-risk covered-product customers is on a risk basis.
- **31 CFR §1010.230** — beneficial ownership for legal-entity covered-product customers.
- **FFIEC BSA/AML Examination Manual** [verify section] — examiner manual is bank-focused; insurers consult it for principles where they translate. The insurer's regulator (state insurance department, NAIC standards where applicable) supplements through public guidance.

#### Covered-product scope — the EDD pack's first read

Covered products under `§1025.210` are, generally: permanent life insurance with cash value (other than group), annuity contracts (other than group), and other insurance products with features of cash value or investment. P&C, term life without cash value, group life, group annuity, health, disability, title, and most reinsurance are outside scope. The pack scopes the product before any EDD work; an EDD pack on a P&C-only customer is out of scope under the rule and should not be drafted under this skill.

#### Insurance-specific EDD trigger profiles

- **Single-premium and large-premium covered-product customers.** Lump-sum funding of permanent life or annuity contracts at scale is the dominant EDD trigger in insurance. The pack reads the SoF on the premium funding (originating account, counterparty, jurisdiction of origin), the SoW underpinning the customer's capacity to fund at that level, and the customer rationale for the product structure (estate planning, wealth-transfer mechanism, other).
- **Free-look-period surrenders and early-surrender patterns.** Patterns of early surrender on covered products are a typology indicator; an EDD pack triggered by an early-surrender pattern reads the customer's intent at funding, the SoF on the original premium, and the destination of the surrender proceeds.
- **Third-party premium funding.** Premiums funded by a third party (not the policyholder) carry elevated ML risk. The EDD pack reads the third-party relationship: who funds, why, how the funding flows, and whether the third party's CIP / CDD on the carrier's books supports the funding pattern.
- **Assignment-of-benefit and assignment-of-contract patterns.** Where a covered-product contract or its benefits are assigned to a third party shortly after issuance, the pattern is a typology indicator; the EDD pack reads the assignment documentation, the assignee's relationship to the policyholder, and the underlying intent.
- **PEPs and senior foreign political figures.** Wealth-transfer covered products attract PEP exposure; same risk-based PEP framing as banking. The 2020 joint statement applies. Senior foreign political figures purchasing high-premium covered products carry the heightened scrutiny path.
- **Cross-border policyholders and beneficiaries.** Geography of policyholder and beneficiary should be documented; high-risk-jurisdiction exposure on either end is an EDD-trigger candidate. The pack reads the FATF posture (where in scope) of each named jurisdiction.
- **Complex-structure policyholder entities.** Where the policyholder is a legal entity with multi-tier ownership, foreign holding intermediaries, or trust intermediaries, the beneficial-ownership read on the policyholder is harder than the certification form alone supports. The pack walks the chain layer by layer.

#### Distribution-channel nuances in EDD

- **Independent-agent / broker distribution.** The agent collects KYC at point of sale; the insurance company is the institution of record. EDD escalation on a customer brought in by an independent agent reads whether the agent's documentation has been reviewed and accepted by the insurer and whether the insurer's program evidences the oversight posture. EDD work itself sits on the insurer's program, not on the agent.
- **Direct-to-consumer and online distribution.** Verification corroboration weighs more heavily; the EDD pack reads non-documentary verification specifically.
- **Institutional channels and bank-distributed products.** Covered products distributed through a bank channel may be governed by either the bank's program or the insurer's program depending on the arrangement; the pack scopes the institution of record before drafting.

#### Beneficial ownership in insurance EDD

Beneficial-ownership work applies to legal-entity covered-product policyholders under `§1010.230`. The customer is the policyholder, not the beneficiary; the beneficial-ownership read is on the legal-entity policyholder. Where the policyholder is an individual, the rule does not apply (but the EDD pack still reads PEP, jurisdictional exposure, SoF / SoW, and product-rationale on the individual). Where the policyholder is a trust, trust-customer scope is what it is in banking — trusts are not legal-entity customers under `§1010.230`, and trust-specific due diligence sits in the institution's program, which the EDD pack reads against.

#### SoF and SoW corroboration in covered insurance

For a high-premium EDD pack, the SoF / SoW work is the load-bearing element:

- **Source of funds.** The premium-funding instrument (wire, check, securities transfer); the originating account; the originating account holder's relationship to the policyholder (self-funded, family-funded, third-party-funded). Third-party funding carries the elevated risk and a separate documentation requirement.
- **Source of wealth.** The customer's capacity to fund at the premium level; corroboration as in capital-markets work (business sale, inherited wealth, long-term earnings, investment returns, trust distributions). Customer self-attestation is the customer's claim; corroboration is what other file evidence provides.

#### Cross-link inside the plugin

- **`cdd-risk-review`** is the upstream baseline; the insurer's CDD on covered-product customers feeds the EDD pack.
- **`negative-news-triage`** for adverse-media triage on high-value covered-product customers.
- **`sanctions-screening-qa`** for sanctions-screening QA on policyholders and beneficiaries.
- **`aml-model-monitoring`** for monitoring scenario tuning where post-EDD profile changes implicate scenario calibration (early-surrender, third-party-funding, premium-anomaly typologies).
- **`sar-decision-qa`** sits downstream where an alert closes against the policyholder or a related party.

#### Common pitfalls in insurance EDD packs

- Drafting an EDD pack on a non-covered product (P&C, term life without cash value, group products, health). The pack scopes the product first.
- Treating the agent's KYC documentation as the insurer's record without evidence the insurer reviewed and accepted it.
- Missing third-party-funding or assignment-of-contract documentation where the customer is funded or controlled by a third party.
- Accepting customer self-attestation on SoW as corroboration; corroboration belongs in the file.
- Reading beneficial-ownership on individual or trust policyholders where the rule does not apply.
- Asserting jurisdictional EDD without reading the FATF posture of the jurisdiction (where in scope).
- Treating PEP status as automatically EDD-required (the 2020 joint statement frames it as risk-based; covered insurance applies the same risk-based framing).

## payments-fintech

### Payments-fintech sector overlay — edd-escalation-pack

When the scope flags payments or fintech (sponsor-bank model, licensed MSB, payment processor, BaaS arrangement, neobank, virtual-asset on-ramp / off-ramp), load this overlay alongside `references/source-anchors.md`. It carries the fintech-and-payments EDD frame the generic capability skill does not own.

#### Regulatory perimeter — the EDD pack's first read

The applicable EDD frame depends on which entity is the institution of record:

- **Sponsor-bank (BaaS) model.** The sponsor bank carries the BSA/AML program for the customer relationship. EDD escalations flow through the sponsor bank's program; the fintech operates under the program contract. The pack reads against the sponsor bank's EDD trigger set and decision machinery, not against a fintech-only standard. Where the program contract allocates EDD investigation work to the fintech, the pack reads whether the bank-side oversight posture (bank monitoring of the fintech's EDD work) is documented; allocation alone is not evidence of execution.
- **Licensed MSB.** MSBs operate under `31 CFR §1022.210` (AML program rule) and `§1022.320` (SAR rule). EDD on high-risk MSB customers is on the MSB's program; the pack reads against the program. Where the MSB also serves as agent for a payment-processor or sponsor-bank arrangement, the EDD obligation may sit on the principal's program; the pack scopes the obligation before drafting.
- **OCC-chartered fintech, state-chartered fintech bank, industrial loan company.** Same EDD frame as a bank. Read alongside the banking overlay.
- **Payment processor.** Where the processor is not itself an FI under the BSA, the EDD work sits with the sponsor bank. The processor's KYB / KYC may inform the bank's pack but does not substitute for it.

#### Fintech-specific EDD trigger profiles

- **MSB-affiliated fintech customers.** A fintech customer that is itself an MSB (or operates a money-transmission business under a fintech wrapper) carries the heavier customer-CDD frame banking an MSB implies; the EDD pack reads the MSB's own program, business model, customer base by jurisdiction, and consistency of expected vs actual activity.
- **Virtual-asset service providers (VASPs) and crypto on-ramp / off-ramp customers.** EDD on a customer transacting with VASPs (or being a VASP customer) reads the FinCEN guidance on virtual currency [verify guidance dates]; the pack walks the VASP's compliance posture (registration as MSB where applicable, public source on regulatory standing, jurisdiction of operation), the customer's transactional pattern with the VASP, and the typology exposure (mixers, chain-hopping, decentralised-finance bridges, peel chains). Sanctions-evasion typologies in the virtual-asset space are documented in OFAC and FinCEN advisories.
- **Third-party payment processors (TPPP) as customers of a bank.** Banking a TPPP carries customer-CDD obligations on the TPPP's own merchant base (where the bank's program asks for it). EDD on a TPPP customer reads the TPPP's merchant-onboarding program, merchant-category-code distribution, expected vs actual chargeback patterns, and the existence of any high-risk merchant verticals (high-risk-jurisdiction merchants, adult content, certain online-gambling categories where in scope, certain telemarketing categories).
- **High-velocity P2P customers.** Fintech customers running high-velocity P2P with structured patterns (round-number transactions just below reporting thresholds; rapid pass-through; mule-pattern indicators) are EDD candidates. The pack reads the structured pattern, not the velocity alone.
- **PEP and PEP-adjacent fintech customers.** Same risk-based PEP framing as banking. The 2020 joint statement applies; the pack records the PEP determination, the source, the date, and the risk-based judgment.
- **Cross-border remittance customers with corridor concentration.** EDD on a money-transmission customer with concentrated activity into a high-risk jurisdiction reads the corridor specifically; the FATF mutual-evaluation public report for the jurisdiction is the cleanest public-source frame.
- **Sanctions-adjacent customers in cross-border payments.** Customers transacting near sanctions thresholds (50 percent rule application, sectoral-sanctions exposure, jurisdiction-of-concern transactional flow) are EDD candidates; the pack reads the sanctions-screening QA outputs and walks the connected-party exposure.

#### Beneficial ownership in fintech contexts

Beneficial-ownership work on fintech customers (legal-entity customers under `§1010.230`) is the same rule, but the evidence stack is often thinner because onboarding is non-face-to-face and the verification corroboration is data-stack rather than document-stack. The EDD pack walks the chain layer by layer; for high-risk fintech customers (PEP-adjacent, complex-structure, high-risk-jurisdiction nexus, MSB-affiliated), the certification form alone is not enough. The pack reads identity-verification corroboration, transactional consistency with the certification, and any inconsistency with public sources.

#### BOI reporting status — the dating discipline

`31 CFR §1010.380` BOI reporting status applies to many small fintech LLC customers. The CTA implementing rule has live litigation history; the pack marks `boi_filing_status` with an as-of date and the rule-state read on that date. A fintech EDD pack from early 2024 reads differently from one from late 2024 or from later periods; assertion without grounding is itself a finding.

#### Sponsor-bank program contract — the EDD walk in BaaS

In BaaS arrangements the EDD work involves both entities:

1. **Trigger surfacing.** The fintech's onboarding or monitoring stack surfaces the EDD trigger; the program contract specifies how the trigger flows to the sponsor bank.
2. **Investigation work.** The contract typically allocates investigation work; the pack reads whether the work was executed (not just whether it was allocated).
3. **Bank-side EDD decision.** The sponsor bank's EDD committee or designated approver decides; the fintech does not.
4. **Conditions and ongoing monitoring.** Where retention with conditions is the decision, the program contract specifies how conditions are operationalised in the fintech's stack and how the sponsor bank monitors compliance with the conditions.

The pack reads each step; a gap at any step is a finding.

#### Cross-link inside the plugin

- **`cdd-risk-review`** is the upstream baseline.
- **`negative-news-triage`** for adverse-media triage on fintech customers.
- **`sanctions-screening-qa`** for sanctions-screening QA on customers and counterparties; the cyber overlay on that skill carries the virtual-currency and ransomware-evasion typology frame.
- **`aml-model-monitoring`** for monitoring scenario tuning where post-EDD profile changes implicate scenario calibration.
- **`sar-decision-qa`** sits downstream where an alert closes against the customer.

#### Common pitfalls in fintech EDD packs

- Reading the fintech's investigation as the sponsor bank's EDD work without evidence the bank reviewed and accepted it.
- Treating the program contract's allocation of EDD work as evidence the work was done.
- Stopping at the beneficial-ownership certification form on a complex-structure fintech customer or on a customer with crypto-business or MSB exposure.
- Asserting `boi_filing_status` under `§1010.380` without an as-of date and a rule-state read.
- Treating a TPPP customer's program assertions as evidence without reading the TPPP's merchant base and chargeback patterns.
- Missing the corridor-specific read on a cross-border-remittance customer (volume into a jurisdiction without reading the FATF posture of the jurisdiction is a thin EDD pack).
- Treating PEP status as automatically EDD-required (the 2020 joint statement frames it as risk-based).
- Importing crypto-transactional-pattern findings without anchoring to the FinCEN / OFAC virtual-currency guidance.
