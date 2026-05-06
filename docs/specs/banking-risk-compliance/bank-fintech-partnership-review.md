# bank-fintech-partnership-review — spec sheet

Plugin: `banking-risk-compliance`
Phase 2 owner: TBD
Status: spec locked, content build pending

## Activation-tuned description

Reviews a bank-fintech partnership from the bank's side as principal supervised entity. Produces a partnership risk pack covering service description and risk classification, risk-based diligence, contract gaps, customer-facing controls, applicability of Reg O / Reg W / Reg E / Reg DD, and termination and wind-down readiness. Output is the artifact a second-line review pod hands to the partnership owner, the chief risk officer, and the relationship manager before a sponsor-bank go-live, a contract refresh, or an examiner request.

Best for:
- A bank is onboarding a fintech relationship (BaaS sponsor program, embedded lending partner, deposit-program partner, fraud or KYC service partner) and second-line needs the partnership pack before commitment or production launch.
- A bank is refreshing an existing fintech partnership ahead of an OCC, FDIC, or FRB examination cycle, and needs to surface contract, control, and customer-protection gaps.
- A bank is responding to an MRA or supervisory letter targeting fintech-partnership oversight (BSA/AML, Reg E, Reg DD, third-party risk, BaaS-specific controls) and needs the artifact that demonstrates remediation.

Not the right tool when:
- The reviewer is the fintech, not the bank. Use `payments-fintech-compliance/skills/fintech-partner-controls` (a fintech-side artifact: bank-program controls, Reg E disclosures the fintech ships, complaint routing).
- The work is generic vendor diligence on any third party. Use `third-party-operational-resilience/skills/vendor-diligence` with the banking sector overlay.
- The work is exit-plan testing for a critical fintech relationship. Use `third-party-operational-resilience/skills/exit-plan` with the banking sector overlay.
- The work is the AML risk assessment for a sponsor-bank program. Use `financial-crime-governance/skills/aml-risk-assessment` (when present) or `edd-escalation-pack` for individual high-risk relationships.

Anchored to: Interagency Guidance on Third-Party Relationships: Risk Management (June 6, 2023, OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023) Section III risk-based lifecycle and Section IV.D fintech-arrangement considerations [verify section]; FDIC, OCC, FRB Joint Statement on Banks' Arrangements with Third Parties to Deliver Bank Deposit Products and Services (July 25, 2024) [verify date]; OCC Bulletin 2024-XX on Bank-Fintech Arrangements [verify bulletin number and effective date]; OCC Bank-Fintech Request for Information (July 2024) and the agencies' subsequent guidance [verify final form]; Bank Service Company Act, 12 U.S.C. §1867(c) examination authority over bank service providers; Regulation O (12 CFR Part 215) for insider transactions where fintech principals are insiders of the partner bank; Regulation W (12 CFR Part 223) for transactions with affiliates if the fintech is an affiliate; Regulation E (12 CFR Part 1005) for consumer EFT protections in sponsor-bank deposit and prepaid programs; Regulation DD (12 CFR Part 1030) for truth-in-savings on deposit products marketed via fintech channels.

## Source anchors

Primary:
- Interagency Guidance on Third-Party Relationships: Risk Management — joint OCC, FRB, FDIC final guidance, June 6, 2023. Sections to cite: III.A (risk-based approach and tailoring), III.B (planning), III.C (due diligence and selection), III.D (contract negotiation), III.E (ongoing monitoring), III.F (termination), IV.D (fintech and BaaS-specific considerations) [verify section labels; the published guidance uses lifecycle-phase headings rather than numbered sections]. Use for: lifecycle-stage scoping, tailoring expectations to criticality, contract elements list.
- FDIC FIL-29-2023, OCC Bulletin 2023-17, FRB SR 23-4 — agency-specific releases of the interagency guidance. Cite alongside the interagency text when the artifact is for a single agency's exam.
- Joint Agency Statement on Bank-Fintech Arrangements (FDIC / OCC / FRB, 2024) [verify exact title and date]. Use for: deposit-program arrangement expectations, end-user reconciliation, ledgering, FBO-account governance, beneficial-ownership clarity.
- OCC Bulletin on BaaS / bank-fintech arrangements [verify bulletin number, OCC has issued multiple BaaS-relevant bulletins post-2023]. Use for: OCC-specific expectations on heightened-risk fintech models.
- Bank Service Company Act, 12 U.S.C. §1867(c). Use for: regulator examination authority over the fintech as a bank service provider, flow-down of examination rights into the contract.
- Regulation O, 12 CFR Part 215 — extensions of credit to insiders and their related interests. Use for: when a fintech principal or its affiliates are insiders of the partner bank or its affiliates, screen all credit and credit-equivalent transactions through Reg O.
- Regulation W, 12 CFR Part 223 — sections 223.11–223.16 on covered transactions, collateral, and quantitative limits. Use for: when the fintech is an affiliate, flag affiliate-transaction limits, collateral, and exemptions.
- Regulation E, 12 CFR Part 1005, especially §1005.6 (consumer liability), §1005.7 (initial disclosures), §1005.11 (error resolution). Use for: sponsor-bank deposit and prepaid programs where the fintech is the customer-facing operator and the bank is the financial institution under Reg E.
- Regulation DD, 12 CFR Part 1030, especially §1030.4 (account disclosures) and §1030.8 (advertising). Use for: deposit products marketed through fintech channels.
- Comptroller's Handbook, Third-Party Relationships: Risk Management [verify current edition post-2023 guidance]. Use for: OCC examiner-facing detail on diligence, contract, and monitoring expectations.
- Comptroller's Handbook, Deposit-Related Credit (and related deposit-product handbooks) [verify current edition]. Use for: deposit-program-specific control expectations.

Secondary (overlay only):
- FFIEC IT Examination Handbook, Outsourcing Technology Services booklet (2004, with subsequent updates) [verify current effective date]. Use for: technology-control expectations layered onto fintech relationships that are also ICT service providers.
- 12 CFR Part 30 Appendix D (OCC Heightened Standards) Sections II–IV [verify section labels] for large covered banks. Use for: third-party risk governance expectations under Heightened Standards when the partner bank is a covered bank.

Public enforcement reference set (for example scenarios — public OCC, FDIC, FRB consent orders involving fintech-partner banks):
- OCC and FDIC consent orders against sponsor banks involving BaaS-program weaknesses, BSA/AML failures, and middleware-ledger reconciliation issues [reference by published case docket; do not invent facts].
- FRB consent orders involving fintech-partner banks and synthetic-deposit / FBO-account weaknesses [reference by published case docket].

## Sector overlays needed

This skill is banking-sector-only by definition. No `references/sector-overlays/` subfolder. The skill ships banking content directly in `SKILL.md` and `references/source-anchors.md`.

## Cross-cutting overlays needed

- `cyber.md` — Required. Bank-fintech arrangements concentrate cyber and ICT risk. Anchors: NYDFS Part 500 (especially §500.11 third-party service providers), FFIEC IT booklet, GLBA Safeguards Rule (16 CFR 314.4), SEC Reg S-K Item 106 disclosure spillover for the public bank holding company.
- `privacy.md` — Required where the fintech handles consumer financial information (most BaaS programs and embedded-lending partners). Anchors: GLBA Privacy Rule (Regulation P, 12 CFR 1016), GLBA Safeguards Rule, state privacy laws (CCPA/CPRA, Texas, Virginia, Colorado) where the fintech operates.
- `conduct.md` — Required where the fintech is customer-facing on a deposit, payments, or credit product. Anchors: CFPB UDAAP exam manual [verify section], FDIC consumer-protection examination handbook for deposit programs, OCC consumer-compliance examination expectations.
- `climate.md` — Not required at v1.

## Output template named sections

Top of artifact:
- Scope and source posture (institution type, asset size and Heightened Standards applicability, jurisdiction, product or program in scope, fintech name [if user supplies], engagement stage [pre-LOI / pre-contract / pre-launch / refresh / exam-driven], source posture)
- Confidence label (high / medium / low / unknown)
- Reviewer questions

Body — six named sections, in this order:

1. **Service description and risk classification**
   - What the fintech does for the bank and the bank's customers (BaaS deposit issuance, embedded lending origination, fraud/KYC service, payments processor, credit card co-brand, etc.)
   - Where the fintech sits in the customer experience (front-of-app, behind-the-scenes, jointly branded)
   - Customer of record (bank vs fintech)
   - Money flow (FBO account, ledgering, settlement)
   - Criticality classification under interagency guidance (critical activity vs lower-risk)
   - BSA/AML risk classification
   - Heightened Standards applicability (12 CFR Part 30 Appendix D) where the bank is a covered bank

2. **Risk-based diligence summary**
   - Diligence elements completed and gaps, organized by interagency-guidance categories: strategy and goals; legal and regulatory compliance; financial condition; business experience; qualifications and backgrounds of principals; risk management; information security; management of information systems; resilience; incident reporting and management; physical security; reliance on subcontractors; insurance; conflicts of interest
   - Reg O screen (any fintech principal an insider of the partner bank or its affiliates?)
   - Reg W screen (is the fintech an affiliate?)
   - Bank Service Company Act notification status

3. **Contract gaps**
   - Examination flow-down (12 U.S.C. §1867(c)): regulator access, audit rights, examiner cooperation
   - SLAs and operational metrics
   - Information security clauses (incident notification timelines, breach response, data return on termination)
   - Subcontractor governance (notice, consent, flow-down of bank requirements)
   - Customer-data ownership and use restrictions
   - Insurance and indemnification
   - Limits on fintech use of bank brand and disclosures
   - Exit and wind-down clauses (data return, customer-account portability, transition assistance, communication rights)

4. **Customer-facing controls**
   - Reg E applicability and division of responsibility (who handles error resolution, who issues provisional credit, who sends initial disclosures)
   - Reg DD applicability for deposit products (account disclosures, advertising, APY accuracy)
   - UDAAP screen on customer-facing copy, fees, and disclosures the fintech ships in the bank's name
   - Complaint routing and CFPB/OCC complaint-portal handling
   - Marketing review and approval gate

5. **Reg O / Reg W / Reg E / Reg DD applicability**
   - Reg O: insider screen result, any covered transactions, prior-approval status, aggregate-limit headroom
   - Reg W: affiliate determination, covered transaction inventory, collateral and quantitative-limit position, attribution rules screen
   - Reg E: which entity is the financial institution under §1005.2(i), error resolution responsibility, disclosure responsibility
   - Reg DD: which entity provides §1030.4 disclosures, advertising review process, APY-calculation responsibility

6. **Termination and wind-down readiness**
   - Triggers (financial deterioration, BSA/AML deterioration, regulator concern, contract breach, strategic exit)
   - Customer notification responsibility and timeline
   - Customer-account portability (deposit-program deconversion to alternative bank, data return, ledger reconciliation)
   - FBO-account wind-down sequence
   - Resolution of pending Reg E disputes, Reg DD obligations, and outstanding disclosures
   - Test record (most recent simulated wind-down or tabletop)

Tail of artifact:
- Recommended owner actions (named role, action, target date or trigger)
- Coverage gaps (interagency-guidance categories with insufficient evidence)
- Source trace (every material claim cites a source — public guidance, contract section, evidence pointer, or `[evidence needed]`)
- Sign-off block (reviewer name, date, reviewer questions, confidence label)

## Structured output fields

Schema: `schemas/vendor.schema.json` (existing, plugin-level) extended with bank-fintech-specific fields. Phase 2 adds a wrapper schema `schemas/bank-fintech-partnership.schema.json`.

Wrapper object:
- `partnership_id`: string. Stable ID.
- `bank`: object. `legal_name` (string), `asset_size_band` (enum: `<10B`, `10B-50B`, `50B-100B`, `100B-250B`, `>250B`), `heightened_standards_applicable` (boolean), `primary_federal_regulator` (enum: `OCC`, `FRB`, `FDIC`).
- `fintech`: object. `legal_name` (string), `program_type` (enum: `BaaS-deposit`, `BaaS-card`, `embedded-lending`, `fraud-kyc-service`, `payments-processor`, `co-brand-card`, `other`), `customer_of_record` (enum: `bank`, `fintech`, `joint`).
- `engagement_stage`: enum. `pre-LOI`, `pre-contract`, `pre-launch`, `production`, `refresh`, `exam-driven`, `wind-down`.
- `criticality`: enum. `critical-activity`, `significant`, `lower-risk`, `not-classified`.
- `diligence_findings`: array of objects, one per interagency-guidance diligence category, with `category` (string), `status` (enum: `complete`, `partial`, `missing`, `not-applicable`), `evidence_pointer` (string), `gap_description` (string).
- `contract_gaps`: array of objects with `clause_topic` (string), `gap_description` (string), `severity` (enum: `high`, `medium`, `low`), `recommended_action` (string).
- `customer_facing_controls`: array of objects with `regulation` (enum: `Reg E`, `Reg DD`, `Reg P`, `Reg Z`, `UDAAP`), `responsibility_split` (string), `gap_description` (string).
- `reg_applicability`: object with `reg_o` (object), `reg_w` (object), `reg_e` (object), `reg_dd` (object), each with `applicable` (boolean), `position` (string), `gap_description` (string).
- `termination_readiness`: object with `triggers_documented` (boolean), `customer_notification_owner` (string), `wind_down_test_date` (string, ISO date or `none`), `outstanding_gaps` (array of strings).
- `recommended_owner_actions`: array of objects with `owner` (string, role), `action` (string), `target_date_or_trigger` (string).
- `confidence_label`: enum. `high` / `medium` / `low` / `unknown`.
- `human_review_required`: boolean. Always true for v1.

## Example scenarios

### Scenario 1: BaaS sponsor-bank deposit program — pre-launch second-line review

Input: a community bank ($4B assets, OCC-regulated) is preparing to launch a BaaS deposit program in partnership with a fintech that will market checking and savings accounts under the fintech's brand. The bank is the deposit-issuing institution. Funds flow into an FBO account held at the bank, with end-user ledgering at the fintech. Engagement stage is pre-launch. The second-line risk team needs the partnership pack for the bank's risk committee and for the OCC supervisory team.

Output emphasizes:
- Service description: bank is customer of record for deposit insurance purposes; fintech is customer-facing operator. Money flow is FBO account at the bank with end-user ledgering at the fintech and a daily reconciliation feed. Criticality: critical activity (consumer-protection-sensitive deposit product, brand-flow-down to bank).
- Risk-based diligence summary: 11 of 14 interagency categories complete; gaps in (a) reliance on subcontractors (the fintech uses an unnamed middleware platform with no flow-down terms), (b) resilience (no documented incident-notification timeline below 4 hours), (c) financial condition (most recent fintech audited financials are 14 months stale).
- Contract gaps: Bank Service Company Act §1867(c) examination clause is present but does not cover subcontractor cooperation; data-return clause does not specify format or timeline; subcontractor consent clause is informational rather than approval-based.
- Customer-facing controls: Reg E error-resolution flow assigns initial intake to the fintech with escalation to the bank only on disputes over $50; reviewer questions whether this division satisfies §1005.11 timing obligations on the bank as the financial institution. Reg DD account disclosures are drafted by the fintech with bank legal review only on annual refresh.
- Reg applicability: Reg O — no insider screen on fintech principals (gap); Reg W — fintech is not an affiliate; Reg E — bank is the financial institution under §1005.2(i); Reg DD — bank is the depository institution and bears advertising-rule risk on fintech-shipped marketing copy.
- Termination readiness: triggers are documented but the wind-down sequence has never been tabletop-tested; FBO-account deconversion path to an alternative bank is not in the contract.
- Recommended owner actions include: head of vendor management to obtain refreshed fintech audited financials within 60 days; chief compliance officer to document Reg E error-resolution division and bank fallback for §1005.11 timing; head of deposit operations to schedule a Q3 wind-down tabletop.
- Confidence: medium overall, low on subcontractor governance and termination readiness.
- Public-source basis: anchored to Interagency Guidance June 2023 §III, Joint Agency Statement on Bank-Fintech Arrangements 2024, Reg E §1005.11, Reg DD §1030.4 and §1030.8. Anonymous; no named institutions.

### Scenario 2: Fintech-partner BSA/AML remediation under an OCC consent order — refresh review

Input: a midsize bank ($25B assets, OCC-regulated) is operating under a published OCC consent order requiring remediation of fintech-partner BSA/AML controls. The bank has six fintech relationships in its sponsor program. The second-line team is refreshing the partnership pack for one named relationship as part of the consent-order remediation evidence package, ahead of an examiner-letter response.

Output emphasizes:
- Service description: fintech operates an embedded-lending product targeting small business borrowers; the bank originates loans, the fintech handles application intake, KYC, and servicing.
- Risk-based diligence summary: criticality reclassified from significant to critical activity in light of consent-order findings; CIP/CDD reliance arrangement under 31 CFR 1020.220 reviewed and gap flagged on annual certification cadence.
- Contract gaps: examination flow-down clause does not extend to the fintech's KYC subcontractor; SAR-related confidentiality clause is silent on referral-back timelines; insurance limits are below the new policy floor set post-consent-order.
- Customer-facing controls: complaint routing reviewed; the fintech is the front-line complaint receiver and forwards to the bank weekly. Reviewer questions whether weekly cadence satisfies the bank's complaint-management policy under the consent-order remediation plan.
- Reg applicability: Reg O — fintech founder holds <5% of partner bank common stock and is not an insider; Reg W — fintech is not an affiliate; Reg E — limited applicability on this lending product; Reg DD — not applicable on a credit product.
- Termination readiness: the consent order requires documented exit triggers; current contract has commercial termination triggers but not BSA/AML-deterioration triggers. Recommended action: contract amendment to add named-trigger language tied to the bank's consent-order metrics.
- Recommended owner actions tied to consent-order remediation milestones with named-month targets.
- Confidence: high on BSA/AML scope (driven by consent order specificity), medium on customer-facing controls.
- Public-source basis: anchored to Interagency Guidance June 2023 §III.D and §III.F, FFIEC BSA/AML manual reliance-arrangement section, the public OCC consent order text. Anonymous; consent order referenced by docket only, no fact invention.

## Common pitfalls

1. **Confusing the bank's lens with the fintech's lens.** This skill produces the bank's pack. The fintech's controls are inputs to the bank's diligence; they are not the artifact's subject. If the output reads like a fintech compliance program, the lens is wrong — switch to `payments-fintech-compliance/skills/fintech-partner-controls`.
2. **Treating the contract as evidence of operation.** A clause that says "the fintech will provide X" is a control statement, not evidence that X happens. The diligence-findings section needs an evidence pointer (most recent SOC report, BSA/AML audit, ledger-reconciliation log) — not just a clause reference.
3. **Skipping the Reg O / Reg W screen because "the fintech is not a bank."** Reg O catches insider-of-the-partner-bank facts (a fintech founder who is also a director of the partner bank, an LLC partly owned by an insider). Reg W catches affiliate facts (common control through a holding company). Both screens must run on every BaaS or sponsor-program partnership at intake and on refresh.
4. **Treating Reg E division of responsibility as a contract drafting exercise.** Under §1005.2(i) the bank is typically the financial institution and bears the §1005.11 error-resolution timing risk. Even when the fintech does the operational intake, the bank cannot contract out of the timing obligation. Reviewer questions need to test the bank's fallback if the fintech misses an intake event.
5. **Rating the partnership "lower-risk" because the bank is small.** The interagency guidance is risk-based; small banks with concentrated fintech exposure (sponsor-bank programs that are a large share of deposits or fee income) carry critical-activity risk regardless of asset size. The criticality field is product-and-flow-driven, not asset-driven.
6. **Treating the wind-down section as theoretical.** If the most recent simulated wind-down date is `none`, the section needs a recommended owner action with a target date, not a narrative reassurance. Examiners read the test-record field first.
