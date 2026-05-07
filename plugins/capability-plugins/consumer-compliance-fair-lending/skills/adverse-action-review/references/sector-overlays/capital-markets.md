# Capital markets sector overlay for adverse-action-review

When the engagement-scope record names sector `capital-markets`, this overlay adds capital-markets-specific scope to the adverse-action notice review. The overlay is narrow because most capital-markets credit extension is institutional and outside ECOA scope.

Loaded by: `adverse-action-review/SKILL.md` when `engagement_scope.sector_overlay_set` includes `capital-markets`, or when the institution type is a broker-dealer, prime broker, or wealth-management entity extending credit to retail customers.

Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for capital-markets adverse-action review

The skill's core machinery is built for consumer credit. The capital-markets overlay flags the narrow population that comes inside ECOA / Reg B scope and the wider population that does not.

### 1. ECOA scope boundary

ECOA and Reg B apply to credit primarily for personal, family, or household purposes; commercial and institutional credit extension by a broker-dealer falls outside that scope. The adverse-action review applies where the institution extends credit to retail customers for consumer purposes. The bulk of broker-dealer margin lending is to retail customers buying or carrying securities, which is consumer-purpose only when the securities are being held as a personal investment in the retail customer's individual capacity; institutional and commercial accounts are out of scope.

The review records the population's consumer-vs-institutional split at the population level and excludes institutional decisions from the §1002.9 perimeter explicitly.

### 2. Securities-based lending and margin calls

Securities-based lending (SBL) extends non-purpose credit to retail customers collateralized by their securities portfolio; margin loans extend purpose credit for securities purchases. Both can be consumer-purpose where the retail customer is the borrower in an individual capacity.

Adverse action on SBL declines and margin-application declines falls under §1002.9. Margin calls and forced liquidations on existing accounts are a different question: the action is taken under the customer margin agreement and Reg T (12 CFR Part 220), not under ECOA. The §1002.2(c) "existing account adverse change" category does not extend to actions taken under the customer agreement's pre-disclosed margin mechanics. The review records margin-call actions out of §1002.9 scope but inside the firm's customer-disclosure and conduct review.

### 3. Wealth-channel credit boundary

Where a broker-dealer affiliate of a bank holding company offers wealth-channel credit (lombard loans, securities-backed lines of credit, jumbo mortgage referrals to the bank affiliate), the credit decision and the §1002.9 obligation sit with the lender of record. Wealth-channel referrals to the bank affiliate are reviewed under the banking overlay; loans extended by the broker-dealer affiliate directly are reviewed here.

### 4. Disparate-impact panel applies narrowly

The disparate-impact red-flag panel runs on the consumer-purpose population only. Wealth-channel populations are typically small, demographically clustered, and statistically thin; the BISG signal is often unreliable on this scale. The review may produce qualitative red flags but should not produce statistical disparity findings on small wealth populations; flag and route to `fair-lending-test-plan` for any quantitative work.

## Capital-markets-specific review additions

- `population.consumer_purpose_subset` boolean per decision; ECOA scope applies only to the subset.
- `population.margin_call_subset` excluded from §1002.9 timing-compliance and content-compliance fields; reviewed instead under conduct and customer-disclosure framing.
- `decisions[].sbl_or_margin` enum (`sbl`, `margin`, `wealth_loan`, `n_a`).

## Common pitfalls in capital-markets adverse-action review

- Pulling the full margin-decision population into ECOA scope; institutional accounts and commercial-purpose extensions are out of scope.
- Treating margin calls and forced liquidations as adverse action under §1002.9; these are taken under the customer agreement, not under Reg B.
- Running disparate-impact statistics on a small wealth-channel population; the BISG signal on small clustered populations is unreliable, and the artifact should flag the limitation rather than produce a finding.
- Reviewing wealth-channel referral declines without identifying whether the broker-dealer or the bank affiliate was the creditor of record; the §1002.9 obligation follows the lender of record.
