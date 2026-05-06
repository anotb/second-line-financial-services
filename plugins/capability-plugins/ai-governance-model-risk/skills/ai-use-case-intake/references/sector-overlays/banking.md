# Banking sector overlay for ai-use-case-intake

When the engagement-scope record names sector `banking`, this overlay tells the intake what additional fields to capture, which named regulators belong on the regulatory-flags table, and which review gates are firm-policy defaults at federally regulated banks. The overlay does not invent firm taxonomy (those are firm-overlay content); it tells the intake which banking-specific facts are load-bearing for the downstream tier and pre-prod work.

Loaded by: `ai-use-case-intake/SKILL.md` when `engagement_scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, BHC, FBO with US operations).

## Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

## What changes for banking intake

### 1. Model definition and inventory anchor is SR 11-7 / OCC Bulletin 2026-13

For federally regulated banks, the intake record is the entry the use case takes in the model inventory under SR 11-7 §III (or the revised OCC Bulletin 2026-13 inventory expectations once on the new guidance). Intake captures:

- `regulatory_flags`: `SR_11_7` and `OCC_2026_13` (the latter where the firm has migrated to the revised guidance) with the routing destination `ai-risk-tiering`.
- The accountable first-line owner is the model owner role under firm policy, with linkage to the firm's model risk management office.
- The lifecycle stage drives whether the inventory entry is "in development" or "in use" under the firm's MRMO state machine.

For non-bank entities under the same parent, SR 11-7 reach is by extension only when the bank inherits model risk through transactions, services, or balance-sheet exposure. Intake should not over-claim SR 11-7 reach to non-bank entities.

### 2. ECOA / Reg B and CFPB Circulars on adverse action

Where the AI use case influences a credit decision (origination, pricing, line management, collections triggers, fraud-driven adverse action), the intake captures:

- `regulatory_flags`: `CFPB_Circular_2022_03` (specific reasons under ECOA for complex algorithms) and `CFPB_Circular_2023_03` (actual principal reasons) where the use case drives adverse-action notice generation. Routing destinations: `ai-risk-tiering` and `validation-plan`.
- `decision_impact.customer_impact`: scored high; basis names the credit-decision touch.
- `decision_impact.regulatory_impact`: scored at least medium with CFPB and prudential reach noted.
- An open question for `validation-plan`: how is the adverse-action reason generation method validated and sampled.

### 3. CCAR / DFAST and CECL stress-testing exposure

For banks subject to stress testing (DFAST, CCAR for the largest BHCs) and for CECL methodology under ASC 326, models in scope for stress projections, allowance methodology, or capital planning carry stress-side documentation expectations on top of the model risk inventory entry. Intake captures:

- A regulatory flag for stress-eligibility with routing to `ai-risk-tiering` (most firm policies tier stress-eligible models at tier-1 by default regardless of customer-facing posture).
- A vendor dependency entry where the stress engine itself is a vendor model.
- A change-plan field capturing the annual stress-testing cycle as a re-intake trigger.

### 4. AML, BSA, sanctions, and fraud framing

For models supporting BSA/AML transaction monitoring, sanctions screening, customer risk rating, and fraud detection, the intake captures:

- `regulatory_flags`: `FFIEC_BSA_AML` with routing to `ai-risk-tiering` and `validation-plan`. The FFIEC BSA/AML Examination Manual is the supervisory frame.
- `decision_impact.regulatory_impact`: scored at least medium with FFIEC manual exposure noted.
- `intended_users`: BSA officer or designee should appear in the user roles for any AML use case (the BSA officer is the named approver on triggered gates downstream).
- The intake distinguishes fraud-model purpose from AML-effectiveness purpose; the two are doctrinally distinct and must not be conflated in the purpose statement.

### 5. Bank-fintech arrangements and sponsor-bank reach

For sponsor-bank programs, OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023 (June 2023) and the OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements (July 25, 2024) [verify date] are operative. Where the bank inherits AI-model risk from a fintech-supplied model:

- `vendor_dependencies`: name the sponsor-bank counterparty (fintech operator) with role `sponsor_bank` or `data_provider` as appropriate; criticality scores at least `important`.
- `regulatory_flags`: `OCC_2023_17_third_party` and `July_2024_bank_fintech` with routing to `ai-risk-tiering` and `vendor-diligence`.
- An open question for `vendor-diligence`: what is the sponsor-bank's evidence pack for the fintech-supplied AI, and how does the bank's MRMO inherit the model risk.

### 6. CRA-relevant models

For models that influence community-development assessment, low-and-moderate-income outreach, or branch-network analytics where they touch CRA performance, intake captures the regulatory flag and a routing destination of `ai-risk-tiering`. Firm policy may add the head of community reinvestment as a named reviewer downstream.

### 7. Heightened Standards reach

For OCC-supervised large banks subject to 12 CFR Part 30 Appendix D (Heightened Standards), intake captures:

- A regulatory flag noting Heightened Standards reach with routing to `ai-risk-tiering` and `board-ai-risk-pack`.
- A note in the change plan that any AI use case named in the firm's risk-appetite statement carries board-level reach; tier-1 models in scope of the appetite statement appear by name or by category at the board.

## Banking-specific intake fields

In addition to the capability intake spine, the following bank-specific facts belong on the record when relevant:

- Federal regulator (OCC / FRB / FDIC) and supervisory cycle posture (any open MRA, MRIA, consent order touching the model or the business line).
- BSA officer or designee linkage where the use case touches BSA/AML.
- Sponsor-bank arrangement counterparty where applicable.
- Stress-testing pedigree where the model is stress-eligible.
- Risk-appetite-statement linkage where the use case appears by name or category.

## Common pitfalls in banking intake

- Treating CFPB authority as out of scope because the entity is OCC- or FRB-supervised. CFPB consumer-protection authority reaches large banks for ECOA, RESPA, EFTA, and UDAAP purposes.
- Recording an AML model as "internal use only" with a low decision-impact score; the FFIEC manual exposure and SAR-workflow integration push the regulatory dimension up regardless of customer-facing posture.
- Missing the sponsor-bank reach when the AI runs at the fintech program operator. The bank inherits model risk wholesale under the June 2023 interagency guidance and the July 2024 joint statement.
- Recording a stress-eligible model without flagging the stress-testing pedigree. Auditors and examiners catch this in the cross-walk.
- Underweighting the Heightened Standards bank's risk-appetite-statement linkage; tier-1 models in scope of the appetite statement carry board-level reach.
