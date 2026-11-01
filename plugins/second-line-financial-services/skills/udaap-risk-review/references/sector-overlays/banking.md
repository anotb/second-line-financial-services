# Banking sector overlay for udaap-risk-review

When the scope record names sector `banking`, this overlay adds banking-specific fact patterns, evidence sources, and review-gate detail to the UDAAP memo. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-sector elements.

Loaded by: `udaap-risk-review/SKILL.md` when `scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, bank holding company, foreign banking organization with US operations).

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for banking UDAAP review memos

Banking is one of the heaviest overlays on this skill. Most of the bureau's UDAAP enforcement and supervisory work has centered on depositories; the memo inherits that machinery directly.

### 1. Recurring banking UDAAP themes

A non-exhaustive list of fact patterns that recur in banking UDAAP review:

- *Overdraft and NSF mechanics.* Authorize-positive-settle-negative (APSN) fees (Circular 2022-06); surprise representment NSF fees (Circular 2022-04); high-to-low transaction reordering for fee-maximisation; overdraft-protection program enrolment with deceptive opt-in; overdraft-program-related deposit-account closures.
- *Deposit-account fee mechanics.* Account-maintenance fee disclosure; minimum-balance-fee mechanics; surprise fees on dormant accounts; account-reopening fees on accounts the consumer believed closed (Circular 2023-02); paper-statement fees and electronic-delivery default state.
- *Mortgage servicing.* Loss-mitigation conduct (timing, completeness, accuracy of evaluation); force-placed insurance pricing and disclosure; fee assessment during loss-mit; payment-application order; escrow-account analysis; payoff-statement accuracy; transfer-of-servicing notices.
- *Credit-card UDAAP themes.* Deferred-interest promotion mechanics (the "no interest if paid in full" advertising vs. the back-end interest calculation); rewards-program changes (devaluation, expiration, mid-cycle term changes); balance-transfer fee mechanics; retention-offer mechanics; credit-card late-fee assessment in light of the §1026.52 amendment [verify operative status given litigation].
- *Auto-loan add-on products.* GAP, VSC, debt-cancellation, credit-life mechanics. Disclosure timing relative to closing; cancellation-and-refund mechanics; bundled-pricing transparency.
- *Indirect-auto dealer-finance practices.* Dealer-discretionary markup mechanics (the historical CFPB / DOJ focal area); add-on bundling at the dealer; the consumer's path to recourse.
- *Debt collection.* Convenience-fee mechanics (Pay-by-Phone Advisory Opinion 2022); debt-substantiation conduct; misrepresentations of legal status, credit-reporting consequences, or settlement terms.
- *Sales-practices conduct.* Account-opening-quota incentive design and the unauthorised-account-opening fact pattern; cross-sell mechanics; branch-incentive tie-backs to consumer-detrimental outcomes.

The memo names the in-scope theme(s); the element-analysis blocks address each theme separately where multiple are in scope.

### 2. CFPB authority over banks

CFPB consumer-protection authority reaches large banks (over $10B in assets) for the named consumer-protection statutes including UDAAP. Smaller banks fall under the prudential regulator (OCC, FRB, FDIC) for supervisory purposes, but the substantive UDAAP standards apply across the size threshold. The memo records:

- Whether the institution is over the $10B threshold.
- The primary federal regulator for consumer-compliance supervision.
- Whether a CFPB enforcement angle is plausible on the in-scope fact pattern (driven by Supervisory Highlights focal items, peer enforcement actions, and the consumer-harm magnitude).

### 3. Sponsor-bank arrangement attribution

Where the bank operates a sponsor-bank arrangement (deposit, card, lending program for a fintech partner, BaaS arrangement), UDAAP duty allocates per the program agreement and the bank's own consumer-compliance program. The interagency third-party guidance (June 2023) anchors the bank-side accountability; the bank is not insulated from UDAAP findings against the program operator. The memo records:

- Which legal entity holds the consumer-facing relationship (typically the sponsor bank for the deposit, card, or credit account).
- Which entity owns the product, marketing, and fee design at issue (often the program operator).
- Which second-line function is reviewing the in-scope fact pattern (typically the sponsor-bank consumer-compliance officer; sometimes joint with the fintech's compliance team).
- Joint approval and joint remediation framing where the fact pattern crosses both entities.

### 4. Servicing-side UDAAP and CFPB Servicing Rules

Mortgage servicing UDAAP analysis interacts with the CFPB Servicing Rules (Reg X 12 CFR Part 1024 Subpart C; Reg Z 12 CFR §1026.41 periodic statements). Reg X §1024.41 (loss-mitigation procedures), §1024.39 (early intervention requirements), §1024.40 (continuity of contact), and the related provisions set the operational baseline; UDAAP analysis reaches conduct that complies with the literal Reg X requirements but materially misleads or harms the borrower in context.

### 5. Deposit-account-specific evidence sources

Banking UDAAP review typically pulls evidence from:

- Core-banking-system transaction data (overdraft and NSF assessment patterns).
- Account-level fee-assessment logs.
- Branch and call-center call recordings (for the consumer-journey context).
- Marketing-asset library (for the deception-prong analysis).
- Complaint-management-system records (CFPB-portal complaints; firm-direct complaints).
- Account-disclosure documents and Reg DD §1030.4 truth-in-savings disclosures.

The memo names the evidence sources used and flags the sources that would be needed but are not yet available.

### 6. Overdraft-as-fair-lending overlap

Where the overdraft-program impact is concentrated in particular customer segments, the UDAAP fact pattern can also raise a fair-lending angle (disparate-impact theory under ECOA / Reg B effects-test framing). The memo cross-references `fair-lending-test-plan` where the fact pattern raises the parallel ECOA theory; the UDAAP memo handles the §1031 elements, the fair-lending test plan handles the disparate-impact testing.

### 7. AI / algorithmic surfaces in banking

Banks deploy AI / ML in marketing personalisation, retention-offer engines, fraud-deny decisioning, voice-agent customer service, conversational AI in the mobile app, and AI-generated communication. The AI-block in the memo names each in-scope AI surface and the UDAAP angle (typically unfairness on algorithmic outcome; deception on AI-generated communication; abusiveness on algorithmic dark-pattern design).

## Banking-specific memo template additions

The following fields are added to the memo (mapped to schema where present):

- `scope.bank_size_threshold` — enum (`over-10b`, `under-10b`, `unknown`); drives CFPB authority framing.
- `scope.primary_federal_regulator` — enum (`OCC`, `FRB`, `FDIC`, `NCUA`, `n-a`).
- `scope.sponsor_bank_program` — boolean; if true, program agreement and joint review framing apply.
- `scope.servicing_rules_intersection` — boolean; if true, Reg X / Reg Z servicing rules baseline is named alongside the UDAAP analysis.
- `recurring_banking_themes[]` — list of themes from the recurring-themes catalogue above that the in-scope fact pattern matches.
- `evidence_base[].core_banking_system` — true where transaction-level evidence is pulled from core-banking systems.
- `cross_reference_skills[]` — extends to include `fair-lending-test-plan` where the fact pattern raises a parallel ECOA theory.

## Common pitfalls in banking UDAAP review memos

- Treating CFPB authority as out of scope because the bank is OCC- or FRB-supervised; CFPB authority reaches large banks for the named consumer-protection statutes including UDAAP.
- Reading overdraft mechanics through the Reg E §1005.17 opt-in lens only and missing the unfairness analysis on the post-opt-in fee mechanic; opt-in compliance is a baseline, not a UDAAP defence.
- Treating the Reg X §1024.41 loss-mit checklist as a UDAAP defence; conduct that complies with the literal Reg X timing and content requirements can still raise UDAAP concerns where the loss-mit-evaluation accuracy or the borrower communication misleads.
- Sponsor-bank programs treated as the program-operator's UDAAP issue; the bank retains accountability under the third-party guidance and the program agreement.
- Auto-add-on review reading the disclosure document in isolation from the closing-flow context; UDAAP analysis reaches the moment of consumer commitment.
- Card-rewards-program changes reviewed for Reg Z §1026.9 change-in-terms compliance only and missing the deception analysis on the marketing of the rewards program over time.
- Sales-practices fact patterns reviewed only for the unauthorised-account-opening conduct and missing the underlying incentive-design root cause; the conduct-risk implications block names the incentive design.
- Treating AI-driven retention offers or AI-driven communication as out of UDAAP scope because the AI is "just personalisation"; the bureau has been explicit that existing UDAAP authority reaches algorithmic outcomes.
