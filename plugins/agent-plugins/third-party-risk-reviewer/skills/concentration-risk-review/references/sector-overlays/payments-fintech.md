# Payments and fintech sector overlay — concentration-risk-review

When the engagement scope flags payments-fintech, load this overlay alongside `references/source-anchors.md`. It carries the payments and fintech-specific concentration framings the generic skill does not own.

## Sponsor-bank concentration (the partner-fintech end of the BaaS dimension)

- A fintech that uses a single sponsor bank for deposit-product issuance carries concentration that is not optional in many products. The dimension reads as `sponsor-bank-baas`. The substitutability read names that sponsor-bank substitution is contractually possible but in practice constrained by the sponsor-bank market's small number of active programme banks, the supervisory posture toward new programmes (currently cautious in the post-2024 supervisory environment), and the operational difficulty of migrating end-user balances. A fintech with one sponsor bank for deposits and a second small sponsor bank for a lending product still carries elevated concentration on the deposit side.

## BIN-sponsor concentration

- For card-issuing fintechs, the BIN sponsor is the regulatory and operational anchor; using one BIN sponsor for a single card programme is the norm and not by itself concentration, but using one BIN sponsor across multiple card programmes (consumer debit, business debit, credit, virtual) is concentration. The dimension reads as `bin-sponsor`. Substitutability read names that BIN re-issuance is operationally costly and customer-disruptive.

## Payment-rails access concentration

- For a payments firm, access to the rails (FedNow, RTP, ACH, card networks, cross-border correspondent) sits behind a small set of vendor-of-record access points. Concentration on one ACH originator or one card-network gateway is the standard pattern; the dimension reads as `payment-rails`. Substitutability read names that rails-access substitution is contractually possible but operationally heavy and may require re-certification with the rails operator.
- **NACHA Operating Rules (current edition)** Third-Party Sender registration and risk-management rules carry concentration framing for ACH originators with multiple Third-Party Senders [verify rule citations]. Where the firm sits as a Third-Party Sender for multiple ACH originators, the concentration reads from the originator side as well.

## Programme-partner concentration at a sponsor bank

- The mirror of the partner-fintech-end view: from the sponsor bank's side, concentration sits on a small set of programme-partner fintechs each carrying many end-users and meaningful deposit balances. Cross-loaded with the banking overlay where the firm is the sponsor bank.

## MSB and PSP concentration

- **FinCEN MSB rules at 31 CFR Part 1022** and registration requirements at 31 CFR §1010.380 [verify §]. MSB concentration on a single agent network or a single sub-MSB carries the BSA/AML supervisory focus; the dimension reads as `single-vendor` with a regulatory-posture sub-finding.
- **CFPB final rule defining larger participants of a market for general-use digital consumer payment applications** (December 2024) [verify Federal Register citation and current state]. Where the rule applies, the supervisory frame for digital-payment-application providers reads concentration in the technology-stack and shared-utility dimensions.

## Cross-border correspondent concentration

- For a cross-border payments firm, correspondent-bank access concentration is a structural feature. The dimension reads as `single-vendor` with a jurisdictional sub-finding (where the correspondent bank's jurisdiction concentrates the firm's sanctions and AML exposure). Substitutability read names that correspondent-bank substitution depends on the correspondent's risk-appetite for the firm's customer base and is not always available on demand.

## Output-template additions for payments-fintech

- Sponsor-bank programme-partner row (from either side, depending on the firm's role).
- BIN-sponsor row in `bin-sponsor`.
- Payment-rails row with per-rail breakdown.
- ACH Third-Party Sender row where applicable.
- Cross-border correspondent row with jurisdictional sub-finding.

## Common pitfalls in payments-fintech concentration reviews

- Treating sponsor-bank concentration as substitutable on procurement timelines. It is not.
- Reading BIN-sponsor concentration as one programme rather than across the firm's card-product set.
- Missing the ACH Third-Party Sender concentration when the firm sits as the originator's sender for multiple originators.
- Conflating MSB agent-network concentration with general single-vendor concentration. The BSA/AML supervisory frame applies and the recommended actions cluster for the BSA officer rather than the head of TPRM.
- Reading correspondent-bank substitutability against benign-conditions only. Stressed substitutability in correspondent banking is a known thin market.
