# Insurance sector overlay — section1071-readiness

**Out of scope flag**. Section 1071 is a small-business-lending data-collection rule under ECOA / Regulation B. Insurance underwriting and claims activity are not credit-extension activities and sit outside the §1071 covered-credit-transaction definition. This overlay exists so that a reviewer at an insurer does not over-extend the readiness work; the sector boundary is named explicitly here.

## Why insurers are typically not in §1071 scope

The rule's covered-financial-institution definition under 12 CFR 1002.105 reads against entities that originate covered credit transactions to small businesses. Insurance products (commercial property and casualty, commercial liability, workers' compensation, surety, marine, professional liability, cyber insurance, and commercial life) are not credit transactions in the rule's sense. The §1071 readiness machinery does not apply to insurance underwriting, premium-financing referrals, or claims handling.

ECOA itself applies in narrower ways to insurance (notably to credit-life and credit-disability products bundled with credit transactions), but those obligations sit elsewhere; §1071's data-collection-and-reporting scope is the lender's, not the insurer's.

## Where an insurer might still touch §1071

There are narrow cases where an entity operating primarily in insurance has a §1071 nexus:

- **An affiliated lender within an insurance group** (a captive finance company, a premium-financing subsidiary that extends credit on its own account to small-business borrowers, an affiliated bank). The CFI determination runs at the lending affiliate, not at the insurer; the readiness work follows the lender, not the insurance entity.
- **Premium financing extended directly by the insurer or its agent on terms that constitute a covered credit transaction**. The classification depends on the structure: premium financing offered through an unaffiliated lender (the insurer is not the lender) is the more common pattern, and the readiness work runs at the lender, not the insurer. Where the insurer or an insurance-group affiliate is itself the lender, surface for legal.
- **Surety and credit-insurance products** that resemble credit-extension in their economics. These are typically classified as insurance, not credit, and sit outside §1071; surface as an open question for legal where the structure is non-trivial.

In all of these, route the engagement to the appropriate sector overlay (`banking.md` or `payments-fintech.md`) at the lending affiliate, and keep the insurance entity itself out of the §1071 readiness perimeter.

## What this overlay tells the reviewer

- **Do not run a §1071 readiness assessment at an insurance entity that does not originate covered credit transactions.** It produces a memo full of "not applicable" rows and a misleading source trace.
- **Surface the boundary in the scoping conversation.** Where the scope flags insurance but the underlying question is about an affiliated lender, restate the scope at the lender and load the appropriate overlay.
- **Where premium financing or credit insurance sits structurally close to credit extension,** the threshold question (is this a covered credit transaction under 1002.106?) is itself the question, and a legal review is appropriate before assuming §1071 scope.

## Common errors at insurance entities

- Running §1071 readiness as a defensive exercise at an entity that has no covered originations. The correct conclusion is "not a covered financial institution; no §1071 readiness obligation."
- Conflating the insurer with its lending affiliate when the two operate under separate legal entities. Run the readiness at the lending affiliate.
- Assuming premium financing is in scope by default. The classification depends on which entity is the lender and on the structure of the financing arrangement.

## When this overlay is not enough

If an insurance-led group has a meaningful direct-lending or affiliated-bank presence, route to the right capability plugin and the right sector overlay rather than stretching this overlay. `consumer-compliance-fair-lending` (this plugin) at the lending affiliate with the `banking.md` or `payments-fintech.md` overlay loaded.
