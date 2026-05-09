# Banking sector overlay for complaint-theme-analysis

When the scope record names sector `banking`, this overlay adds banking-specific theme patterns, evidence sources, and cross-skill chain detail. Where there is conflict between the capability defaults and this overlay, the overlay governs the banking-sector elements.

Loaded by: `complaint-theme-analysis/SKILL.md` when `scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, bank holding company, foreign banking organization with US operations).

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for banking complaint-theme analysis

Banking is the heaviest overlay on this skill. The CFPB Complaint Database has the deepest history on depository products; the firm's internal complaint-management surface for banking is typically more mature than for payments-fintech; the regulatory exposure surface is the most articulated. The memo inherits that machinery directly.

### 1. Recurring banking complaint themes

A non-exhaustive theme catalogue for the deposits, mortgage, credit-card, and auto-credit lines:

- *Deposit account themes.* Overdraft and NSF themes (the APSN pattern; surprise representment fees; daily-fee-cap surprise; high-to-low transaction reordering); account-closure themes (closed-account-reopened-for-deposit fee themes per Circular 2023-02; closure without notice; closure for AML reasons with unclear consumer recourse); account-fee themes (minimum-balance fee surprise; paper-statement fee; dormant-account fee); funds-availability themes (Reg CC hold disputes; provisional-credit reversal); error-resolution themes (Reg E §1005.11 dispute handling on debit-card unauthorised use); account-opening themes (denial reason coding; ChexSystems-driven denial).
- *Mortgage themes.* Loss-mitigation themes (the repeatedly-lost-application pattern; clock-reset under Reg X §1024.41; continuity-of-contact gap); force-placed insurance themes (pricing dispute; existing-coverage-on-file disputes); payment-application themes (payments held in suspense during loss-mit; payments applied in non-borrower-favorable order); transfer-of-servicing themes (payment misapplication after transfer; fee assessment disputes); escrow-analysis themes (payment-shock surprise on escrow shortage); payoff-statement themes; PMI-cancellation themes (HPA timing); foreclosure-process themes.
- *Credit-card themes.* Fee-disclosure themes (FX fee not disclosed at point of sale; annual fee surprise; balance-transfer fee mechanic); deferred-interest themes (the no-interest-if-paid-in-full mechanic and the back-end interest assessment); rewards-program themes (devaluation; expiration; mid-cycle term changes); payment-application themes (Reg Z §1026.53 allocation order disputes; promotional-balance-vs-purchase-balance handling); late-fee themes (cutoff-time disputes; weekend-and-holiday cutoff disputes; intersects pending §1026.52 rule [verify operative status]); credit-line-decrease and adverse-action themes (reason-code specificity per Circulars 2022-03 and 2023-03 where complex models are in path); identity-theft and dispute themes (FCRA §1681i timing; Regulation V furnisher conduct).
- *Indirect auto themes.* Add-on product themes (GAP, VSC, debt-cancellation cancellation-and-refund disputes); dealer-discretionary-markup themes (where complaints surface at the lender level); titling and registration themes; default and repossession themes.
- *HELOC themes.* Account-suspension themes (suspension during draw period); rate-change themes (tied to index movement); payment-shock themes (interest-only-to-amortising transition).

The memo names the in-scope themes; the analysis blocks address each theme separately where multiple are at the top of the period count.

### 2. CFPB Complaint Database scope and limits

The CFPB Complaint Database is the public anchor for banking complaint-theme analysis. The database covers complaints submitted directly to the CFPB consumer portal; the firm reports these into its complaint-management system through the bureau's company portal. The database is not the firm's full complaint surface; the firm-direct complaint channels (call center, web form, branch escalation, executive-resolution) typically dwarf the CFPB-portal subset.

The memo records:

- The CFPB-portal subset count and share of the firm's total period complaints.
- The deduplication treatment (CFPB-portal complaints typically exist in both the CFPB extract and the firm's internal records; the memo deduplicates against the firm's internal where the consent-flag permits matching).
- The narrative-consent treatment (the public extract redacts narrative on consumers who did not consent; the firm's internal records have the full narrative).
- The product, sub-product, issue, sub-issue field handling (the bureau's taxonomy is the public coding; the firm typically maintains a parallel firm taxonomy that maps to but does not equal the bureau's).

The bureau's taxonomy is not a root-cause taxonomy; it is the bureau's complaint-coding taxonomy. The memo themes against the firm's taxonomy and maps back to the bureau's coding for the public-comparison work.

### 3. Bank size and CFPB authority

CFPB consumer-compliance authority reaches large banks (over $10B in assets) directly for the named consumer-protection statutes including UDAAP. Smaller banks fall under the prudential regulator (OCC, FRB, FDIC) for supervisory purposes; the substantive standards apply across the threshold. The memo records:

- Whether the institution is over the $10B threshold.
- The primary federal consumer-compliance regulator.
- Whether a CFPB enforcement angle is plausible on the in-scope themes (driven by Supervisory Highlights focal items, peer enforcement actions, and the consumer-harm magnitude of the themes).

### 4. Sponsor-bank arrangement attribution

Where the bank operates a sponsor-bank arrangement (deposit, card, lending program for a fintech partner, BaaS arrangement), complaints often arrive at the bank but originate from the program operator's product or marketing. The memo records:

- Which legal entity holds the consumer-facing relationship for each theme.
- Which entity owns the product, marketing, and fee design at issue.
- Joint-program complaint-routing patterns; whether the program operator's complaint surface is also reviewed.
- Cross-skill chain into `udaap-risk-review` or `marketing-claim-review` is named with the bank as the accountable party.

### 5. Mortgage-servicing rules intersection

Mortgage-servicing themes interact with the CFPB Servicing Rules (Reg X 12 CFR Part 1024 Subpart C; Reg Z 12 CFR §1026.41). The intersection is operationally important:

- Reg X §1024.41 (loss-mitigation procedures) is the operational baseline; loss-mit themes are tested against the §1024.41 timing and content requirements as a parallel inquiry to the UDAAP analysis.
- Reg X §1024.39 (early intervention) and §1024.40 (continuity of contact) anchor the borrower-communication themes.
- Reg X §1024.37 (force-placed insurance) anchors the FPI themes.
- Reg X §1024.33 (transfer of servicing) anchors the transfer themes.
- Reg X §1024.36 (request for information) anchors the QWR themes.

Compliance with the literal Reg X requirements is a baseline, not a UDAAP defence; the memo treats the Reg X check and the UDAAP unfairness analysis as parallel inquiries.

### 6. CRA and HMDA cross-walk for mortgage and small-business themes

For HMDA-reportable mortgage and (where operative) §1071-reportable small-business themes, the geographic and demographic concentration analysis can use the firm's HMDA LAR or §1071 register as the denominator rather than BISG. HMDA self-reported demographics are stronger evidence than BISG for mortgage; the memo uses HMDA where available and falls back to BISG where not. CRA assessment-area overlap matters where redlining-adjacent themes appear; the cross-skill chain into `fair-lending-test-plan` carries the CRA framing.

### 7. Banking-specific evidence sources

Banking complaint-theme analysis typically pulls evidence from:

- The firm's complaint-management system (firm-direct complaints from call center, branch, web form, executive resolution; CFPB-portal complaints routed through the bureau's company portal).
- The CFPB Consumer Complaint Database (public extract for the firm and product).
- Core-banking transaction data (denominator for rate analysis).
- Deposit-account, card, and mortgage-servicing system logs.
- Branch and call-center call recordings (for the consumer-journey context on top themes).
- Marketing-asset library (where themes trace to a campaign).
- Account-disclosure documents and Reg DD §1030.4 truth-in-savings disclosures.
- HMDA LAR for the mortgage denominator.

### 8. Banking AI / algorithmic surfaces

Banks deploy AI / ML in credit-line decisioning, fraud-deny decisioning, customer-service voice agents, conversational AI, retention-offer engines, marketing personalisation, and AI-generated communication. Themes that touch these surfaces carry `ai_flag: true` and feed the cross-skill chain to `adverse-action-review` (for AAN-content themes), `udaap-risk-review` (for algorithmic-outcome themes), or `fair-lending-test-plan` (for protected-class-disparity themes). The April 2023 Joint Statement and CFPB Circulars 2022-03 and 2023-03 anchor the algorithmic-discrimination framing.

## Banking-specific theme matrix additions

Per theme:

- `cfpb_portal_count` — count of complaints in the CFPB Complaint Database for this theme in the period.
- `cfpb_portal_share` — share of the theme's period count that arrives via the CFPB portal.
- `bank_size_threshold` — `over-10b` / `under-10b` / `unknown` (sets the CFPB-authority framing).
- `primary_federal_regulator` — `OCC` / `FRB` / `FDIC` / `NCUA`.
- `sponsor_bank_program` — boolean; if true, the program-operator attribution is named in the memo.
- `servicing_rules_intersection` — boolean; if true for mortgage-servicing themes, Reg X / Reg Z servicing rules are named alongside the UDAAP analysis.
- `cra_intersection` — boolean; if true for redlining-adjacent mortgage themes, CRA assessment area is named.

## Common pitfalls in banking complaint-theme analysis

- Treating the CFPB Complaint Database as the full complaint surface. The CFPB portal is one channel; the firm-direct channels typically carry the larger volume.
- Theming at the bureau's product / sub-product / issue / sub-issue grain. The bureau's taxonomy is a complaint-coding taxonomy, not a root-cause taxonomy; two themes can share a sub-issue.
- Counting CFPB-portal and firm-direct complaints separately and double-counting the routed-portal subset. The memo deduplicates explicitly.
- Treating Reg X §1024.41 compliance as a UDAAP defence on mortgage-servicing themes. Reg X compliance is a baseline; the UDAAP analysis is parallel.
- Treating sponsor-bank-program themes as the program-operator's issue. The bank carries accountability under the third-party guidance and the program agreement; the memo names the bank as the accountable party.
- Reading credit-card fee themes from the marketing copy alone and missing the cardholder-agreement disclosure path. Both surfaces are in the consumer journey.
- Watching only the volume movement on a theme without rate framing. A volume increase that aligns with a campaign may not represent a rate increase; the memo computes rate per relevant denominator.
- Treating the BISG signal on banking themes as protected-class evidence. For mortgage, HMDA self-reported demographics are the operative source; for non-mortgage, BISG is signal-grade and feeds the watch-list, not the finding.
