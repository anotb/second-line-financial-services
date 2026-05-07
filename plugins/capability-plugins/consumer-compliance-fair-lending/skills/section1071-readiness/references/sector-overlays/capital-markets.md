# Capital-markets sector overlay — section1071-readiness

**Out of scope flag**. Section 1071 is a small-business-lending data-collection rule under ECOA / Regulation B, and capital-markets activity is not the rule's target population. This overlay exists so that a reviewer at a capital-markets entity does not over-extend the readiness work; the sector boundary is named explicitly here.

## Why capital-markets entities are typically not in §1071 scope

The rule's covered-financial-institution definition under 12 CFR 1002.105 reads against entities that originate covered credit transactions to small businesses. Capital-markets entities — broker-dealers, investment advisers, registered funds, trading venues, central counterparties, central securities depositories, swap dealers, security-based swap dealers — typically do not originate small-business credit transactions in the rule's sense. Securities transactions are excluded under 12 CFR 1002.106(b) [verify subsection]. The rule's data-collection and reporting machinery is built for lenders, not for securities intermediaries.

## Where a capital-markets entity might still touch §1071

There are narrow cases where an entity operating primarily in capital markets has a §1071 nexus:

- **A broker-dealer or investment adviser whose affiliated entity originates small-business credit** (a private-credit fund's lending vehicle, a wealth-management business's cash-management lending product, a prime-brokerage entity's margin-lending product where extended to a small-business borrower). The CFI determination runs at the originating entity, not at the broker-dealer or adviser; the readiness work follows the lender, not the capital-markets affiliate.
- **A captive or affiliated bank** within a capital-markets-led group. The bank affiliate may itself be a CFI; the readiness work runs at the bank, not at the broader group.
- **A direct-lending business model** where the entity itself originates business loans alongside its capital-markets activity. Run the readiness work as a banking or fintech engagement at that entity.

In all of these, route the engagement to the appropriate sector overlay (`banking.md` or `payments-fintech.md`) at the originating entity, and keep the capital-markets entity itself out of the §1071 readiness perimeter.

## What this overlay tells the reviewer

- **Do not run a §1071 readiness assessment at a capital-markets entity that does not originate covered credit transactions.** It produces a memo full of "not applicable" rows and a misleading source trace.
- **Surface the boundary in the engagement-scoping conversation.** Where the engagement scope flags capital-markets but the underlying question is about a lending affiliate, restate the scope at the lending affiliate and load the appropriate overlay.
- **Where the capital-markets entity has a treasury / liquidity function that extends short-term credit to a small-business counterparty,** the credit-extension question is itself the threshold question and a legal review is appropriate before assuming the §1071 scope.

## Common errors at capital-markets entities

- Running §1071 readiness as a defensive exercise at an entity that has no covered originations. Time and committee attention are wasted; the readiness memo's correct conclusion is "not a covered financial institution; no §1071 readiness obligation."
- Conflating the capital-markets entity with its lending affiliate when the two operate under separate legal entities with separate registrations. Run the readiness at the lending affiliate.
- Assuming securities-financing transactions (margin lending, securities-based lending) are §1071-reportable. The rule's covered-credit-transaction definition under 1002.106 excludes securities transactions [verify subsection]; surface as an open question for legal where the structure is non-trivial.

## When this overlay is not enough

If a capital-markets-led group has a meaningful direct-lending or affiliated-bank presence, route to the right capability plugin and the right sector overlay rather than stretching this overlay. `risk-compliance-core` for the group-wide compliance posture; `consumer-compliance-fair-lending` (this plugin) at the lending affiliate with the `banking.md` or `payments-fintech.md` overlay loaded.
