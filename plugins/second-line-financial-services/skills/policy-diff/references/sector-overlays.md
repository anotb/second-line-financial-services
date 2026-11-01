# sector-overlays

One section per sector. Read only the sections the scope calls for.

## banking

### Sector overlay: banking

Loaded when the scope flags `banking` as the sector. The change-log spine is unchanged; what changes is the source citation set, the named approver expectations, and the typical downstream-impact patterns for bank policy diffs.

#### Approver routing expectations

For large national banks operating under OCC heightened standards (12 CFR Part 30 Appendix D), material changes to the policies that constitute the written framework default to a routing posture that includes board or board-committee attestation. Specifically:

- Risk-appetite, top-risks, and risk-governance-framework policy changes route to the board risk committee.
- Credit, market, liquidity, and operational risk policy changes route to the board risk committee with named-CRO sign-off.
- Insider-lending (Reg O), affiliate-transactions (Reg W), and savings-and-loan-holding-company policy changes carry both committee and board director attestation depending on the firm's bylaws.
- BSA/AML policy changes route to the BSA Officer and to the board-designated BSA committee where one exists; the FFIEC BSA/AML Examination Manual's program-element expectations frame the materiality call.

For community banks not subject to heightened standards, the routing posture is lighter — typically the relevant committee or function head with board-committee notification — but the lifecycle expectation under OCC Bulletin 2021-36 still applies.

#### Source-citation patterns specific to banking diffs

When a banking policy diff cites supervisory letters, the citation carries the SR letter or OCC Bulletin number with section reference where the letter is structured (most are). FRB SR letters and OCC bulletins are the working source set for bank policy diffs along with the underlying CFR.

- 12 CFR Part 30 Appendix D — heightened standards written framework.
- 12 CFR Part 215 (Reg O) — insider lending.
- 12 CFR Part 223 (Reg W) — affiliate transactions.
- 12 CFR Part 252 (Reg YY) — enhanced prudential standards for large bank holding companies.
- Joint interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026) — model risk policy. Supersedes SR 11-7 / OCC Bulletin 2011-12 (April 4, 2011) and SR 21-8 (April 9, 2021); GenAI and agentic AI explicitly out of scope.
- Interagency Guidance on Third-Party Relationships (OCC / FRB / FDIC, June 2023) — TPRM policy.
- FFIEC BSA/AML Examination Manual — BSA/AML policy.

#### Downstream-impact patterns specific to banking diffs

A few patterns recur in bank policy diffs and the change log carries them as expected fields rather than ad-hoc rationale.

- Material BSA/AML policy changes almost always touch the BSA training program, the suspicious activity reporting workflow, the customer due diligence procedures, and the bank's response to OFAC alerts. The downstream-impact rows enumerate each.
- Material TPRM policy changes touch the master vendor contract templates and the procurement workflow; large banks typically maintain template-by-template change logs that the diff cross-references.
- Material model-risk policy changes touch the model inventory's policy-version field and the validation-cadence schedule; the diff feeds the model risk committee's quarterly review.
- Material capital and liquidity policy changes touch the firm's resolution and recovery plan and may require coordination with the firm's resolution group at the FRB or the FDIC.

#### Cross-cutting overlay interaction

Banking policy diffs commonly interact with the cyber cross-cutting overlay (NYDFS Part 500 §500.3 for NY-licensed banks, FFIEC IT booklet for federally regulated banks). Where the policy in scope is information security or third-party security, both the banking sector overlay and `references/cross-cutting.md#cyber` load and the materiality lens picks up both sets of expectations.

## capital-markets

### Sector overlay: capital-markets

Loaded when the scope flags `capital-markets` (broker-dealer, investment adviser, registered fund) as the sector. The change-log spine is unchanged; what changes is the source-citation set, the approver expectations, and the typical patterns for capital-markets policy diffs.

#### Approver routing expectations

SEC and FINRA examination postures shape approver routing for capital-markets policy diffs.

- For registered investment advisers, material changes to compliance policies route to the chief compliance officer designated under IAA Rule 206(4)-7. The annual review under §275.206(4)-7(b) is itself the trigger event for many policy diffs at advisers.
- For registered investment companies (mutual funds, ETFs, closed-end funds), material policy changes route to the fund board's compliance committee or, when material, the full board, consistent with ICA Rule 38a-1.
- For broker-dealers, material WSP changes route to the named supervisory principal under FINRA Rule 3110, with CEO annual certification per Supplementary Material .04.
- For dual registrants, the diff often produces parallel approver routing for both the adviser-side CCO and the broker-dealer-side principal.

#### Source-citation patterns specific to capital-markets diffs

- IAA Rule 206(4)-7 (17 CFR §275.206(4)-7) — adviser compliance program.
- ICA Rule 38a-1 (17 CFR §270.38a-1) — fund compliance program.
- FINRA Rule 3110 — supervision and WSPs.
- FINRA Rule 4511 — books and records.
- 17 CFR §240.17a-3 and §240.17a-4 — broker-dealer recordkeeping.
- SEC Marketing Rule (17 CFR §275.206(4)-1) — adviser marketing.
- Investment Company Act, where the policy concerns fund operations.
- SEC Division of Examinations annual exam priorities — used as an interpretive lens, not as a binding citation.

#### Downstream-impact patterns specific to capital-markets diffs

- Material adviser compliance policy changes touch the firm's CCO annual review documentation, the firm's training program (RIA-specific), the firm's books-and-records configuration under §275.204-2, and the firm's Form ADV Part 2 disclosure where the change is material to clients.
- Material WSP changes touch the FINRA-required CEO annual certification and the supervisory principal review schedule.
- Material fund-compliance policy changes touch the fund board's compliance committee charter and the next quarterly compliance report to the board.
- Marketing Rule policy changes touch the firm's marketing review queue and the recordkeeping configuration for marketing communications.

#### Cross-cutting overlay interaction

Capital-markets policy diffs commonly interact with the cyber cross-cutting overlay (SEC cybersecurity disclosure rules, Reg S-P safeguards) and the conduct cross-cutting overlay (Marketing Rule's anti-fraud framing, broker-dealer suitability and Reg BI).

## insurance

### Sector overlay: insurance

Loaded when the scope flags `insurance` as the sector. The change-log spine is unchanged; what changes is the source-citation set, the approver expectations, and the typical patterns for insurer policy diffs.

#### Approver routing expectations

State insurance regulators expect insurer policy lifecycles to surface board-level visibility for material changes. The named approver expectations in insurance policy diffs default to:

- Corporate governance, risk-appetite, and ORSA-related policy changes route to the board or its risk committee, consistent with NAIC Corporate Governance Annual Disclosure (CGAD) expectations and ORSA filing scope.
- Market-conduct, claims, and underwriting policy changes route to the named market-conduct officer or claims executive with audit-committee notification when the change responds to a market-conduct exam finding.
- Reinsurance, investment, and capital-management policy changes route to the named CFO or chief investment officer with board-committee attestation.
- Cybersecurity policy changes for NYDFS-covered insurers follow the §500.3 annual-approval routing (senior officer or board).

#### Source-citation patterns specific to insurance diffs

Insurance regulation is state-by-state with NAIC model laws as the convergence layer. Diffs cite both the state's adopted code and the NAIC model where relevant.

- NAIC Model Law 305 (Insurance Holding Company System Regulatory Act) — group supervision policy.
- NAIC Model Law 440 (Risk Management and Own Risk and Solvency Assessment Model Act) — ORSA policy.
- NAIC Model Bulletin on Use of Artificial Intelligence Systems by Insurers (December 2023) — AI governance policy.
- State-by-state insurance code (cite the state by its enacted law section).
- NYDFS Part 500 for NY-licensed entities — cybersecurity policy.
- NAIC Market Conduct Examiners Handbook — market-conduct-policy reference.

#### Downstream-impact patterns specific to insurance diffs

- Material ORSA-related policy changes touch the next ORSA filing's narrative and may require coordination with the firm's appointed actuary.
- Material claims-handling policy changes touch the claims operations system, agent-and-broker training, and the firm's market-conduct exam-readiness file.
- Material AI-governance policy changes (post-NAIC Model Bulletin) touch the firm's model risk inventory if the firm uses AI in underwriting, claims, or marketing; the diff feeds both the model risk committee and the AI governance forum if both exist.
- Material privacy and data-handling policy changes for insurers carry state insurance privacy law overlays (some states have their own insurance-specific privacy regulations that go beyond GLBA).

#### Cross-cutting overlay interaction

Insurance policy diffs commonly interact with the conduct cross-cutting overlay (claims-handling, market-conduct, suitability) and the cyber cross-cutting overlay (NYDFS Part 500, NAIC Insurance Data Security Model Law adoptions).

## payments-fintech

### Sector overlay: payments-fintech

Loaded when the scope flags `payments-fintech` as the sector. The change-log spine is unchanged; what changes is the source-citation set, the approver expectations, and the typical patterns for payments-and-fintech policy diffs.

#### Approver routing expectations

Payments and fintech firms typically operate either as money transmitters under state law, as bank-sponsored programs, or as supervised banks themselves with a fintech-style operating model. Approver expectations differ accordingly.

- Bank-sponsored fintech programs run policy diffs on both sides. The fintech's policy diff is usually approved at the fintech's CCO or risk-committee level; the sponsor bank's policy diff routes per the banking sector overlay. Where the fintech's policy reflects an obligation imposed by the sponsor under the program agreement, the sponsor bank typically attests as a downstream consumer.
- Money-transmitter compliance program policy changes route to the named BSA Officer and the firm's compliance committee, consistent with state money-transmitter law and FinCEN expectations for MSBs.
- CFPB-supervised firms running consumer-financial-products policy diffs route through the CMS's policies-and-procedures pillar; material changes notify the board or its committee.
- Where the policy implements a CFPB consent order or settlement obligation, the named monitor (where one is appointed) is a routing destination alongside the firm's internal approver.

#### Source-citation patterns specific to payments-fintech diffs

- Reg E (12 CFR Part 1005) — electronic fund transfers.
- Reg Z (12 CFR Part 1026) — truth in lending.
- Reg DD (12 CFR Part 1030) — truth in savings.
- CFPB Section 1033 — open banking, where applicable (**compliance dates stayed as of October 29, 2025; CFPB-initiated reconsideration with ANPR** — verify current docket status before benchmarking against tier-based compliance dates).
- State money-transmitter laws (cite the state's enacted law).
- FinCEN regulations under 31 CFR Chapter X — BSA/AML for MSBs.
- CFPB CMS guidance — Supervision and Examination Manual.
- OCC fintech-bank-partnership expectations and the Interagency Guidance on Third-Party Relationships (June 2023) for sponsor-bank programs.

#### Downstream-impact patterns specific to payments-fintech diffs

- Material Reg E policy changes touch the firm's error-resolution workflow (the 10-day provisional-credit clock and the 45-day investigation clock are operative deadlines that frequently appear in the substantive-delta column), the customer-disclosure templates, and the call-center training.
- Material BSA/AML policy changes for money transmitters touch the transaction monitoring system configuration, the SAR workflow, and the customer due diligence (CIP and CDD) onboarding flow.
- Material UDAAP-related policy changes touch the marketing review queue, the customer complaint handling workflow, and the consumer-disclosure templates.
- Material sponsor-bank-program policy changes propagate from the bank's policy to the fintech's procedures via the program agreement; the diff often surfaces an open question where the sponsor's expectation has tightened mid-cycle and the fintech's procedure has not yet caught up.

#### Cross-cutting overlay interaction

Payments-fintech policy diffs commonly interact with the cyber cross-cutting overlay (Reg S-P safeguards, GLBA Safeguards Rule, NYDFS Part 500 for NY-licensed entities) and the conduct cross-cutting overlay (CFPB UDAAP framing, fair lending where credit is in scope).
