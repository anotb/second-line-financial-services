# Banking sector overlay for ai-risk-tiering

When the engagement-scope record names sector `banking`, this overlay tells the tier rubric what is banking-specific and which named regulators and bulletins set the bar. The overlay does not invent tier names or cutoffs (those are firm policy); it tells the rubric which factors elevate, which gates trigger by default, and which re-tiering events to name.

Loaded by: `ai-risk-tiering/SKILL.md` when `engagement_scope.sector_overlay_set` includes `banking`, or when the institution type implicates a federal banking regulator (national bank, state member bank, savings association, BHC, FBO with US operations).

## Source basis

Cited and section-referenced in `references/source-anchors.md`. This overlay names the regulators and sources without restating excerpts.

## What changes for banking tiering decisions

### 1. SR 11-7 §III risk-based principle is binding

For federally regulated banks, the tier produced by this skill is the firm-side artefact that operationalises the SR 11-7 §III risk-based principle and the §IV materiality framing. OCC Bulletin 2026-13 refreshes the guidance for AI/ML inclusion. Tier names and cutoffs remain firm policy; the materiality factors (purpose, decision influence, financial exposure, complexity, uncertainty, vendor dependence) are the spine of the rubric.

For non-bank registrants under the same parent, SR 11-7 reaches by extension only when the bank inherits model risk through transactions, services, or balance-sheet exposure. Tiering record should not over-claim SR 11-7 reach to non-bank entities.

### 2. OCC Heightened Standards (12 CFR Part 30 Appendix D)

For OCC-supervised large banks, the Heightened Standards add a board-level risk-governance frame; risk-appetite statements name model risk and tier-1 models typically appear by name or by category. Tier-side implications:

- The tier decision references the firm's risk-appetite-statement classification where the bank is in scope.
- Tier-1 cards in scope of an in-scope bank trigger AI risk committee approval at minimum; firm policy may stack additional approvals.

### 3. ECOA / Reg B and CFPB Circulars on adverse action

Where the AI use case influences a credit decision (origination, pricing, line management, collections triggers, fraud-driven adverse action), the tier rubric reads the conduct factor as high and the regulatory factor as high. Specifically:

- CFPB Circular 2022-03: complex algorithms do not excuse the specific-reasons requirement under ECOA / Reg B; the tier decision flags adverse-action notice generation as a triggered control gate.
- CFPB Circular 2023-03: reasons given in the adverse-action notice must be the actual principal reasons; the tier decision flags adverse-action notice quality sampling as a monitoring gate.

Default sign-off questions added at tier-1 for credit-decisioning use cases:

- What is the method of adverse-action reason generation, and how is its accuracy sampled?
- How does the firm handle a proxy variable identified post-deployment as fairness-sensitive?
- What is the integration with the firm's fair-lending test plan, and at what cadence?

### 4. CCAR / DFAST and CECL overlap

For banks subject to stress testing (DFAST, CCAR for the largest BHCs) and for CECL methodology under ASC 326, models in scope for stress projections, allowance methodology, or capital planning are read as tier-1 by default under most firm policies regardless of customer-facing posture. The tier decision:

- Flags the stress-testing pedigree as a triggered control gate.
- Names the annual stress-testing cycle as a re-tiering trigger.
- Cross-references CCAR/DFAST owner; this skill does not own the stress-testing-side documentation expectations.

Tiering-record flag: a stress-eligible model carries SR 15-18 or successor-letter expectations [verify SR letter] in addition to SR 11-7 / OCC Bulletin 2026-13.

### 5. AML, BSA, sanctions, and fraud framing

For models supporting BSA/AML transaction monitoring, sanctions screening, customer risk rating, and fraud detection, the FFIEC BSA/AML Examination Manual sets the supervisory frame. Tier-side implications:

- Threshold tuning and SAR-workflow integration push the regulatory and conduct factors upward.
- BSA officer or designee is a named approver on triggered gates when the use case touches AML.
- The tier decision distinguishes fraud-model performance from AML-effectiveness evidence; the two are doctrinally distinct and must not be conflated at tier-decision time.

### 6. Bank-fintech arrangements and sponsor-bank reach

For sponsor-bank programs, OCC Bulletin 2023-17 / FRB SR 23-4 / FDIC FIL-29-2023 (June 2023) and the OCC / FRB / FDIC Joint Statement on Bank-Fintech Arrangements (July 25, 2024) [verify date] are operative. Where the bank inherits model risk from a fintech-supplied model:

- Vendor-dependence factor scores at minimum medium; concentration-risk factor scores upward when a single fintech is the dominant program.
- The tier decision names the sponsor-bank validator and the bank-side committee path even when day-to-day operation sits at the fintech.
- A re-tiering trigger fires on any change in the sponsor-bank-fintech arrangement, including program expansion or contraction.

### 7. CRA-relevant models

For models that influence community-development assessment, low-and-moderate-income outreach, or branch-network analytics where they touch CRA performance, the regulatory factor scores at least medium. Firm policy may add the head of community reinvestment as an approver on triggered gates.

## Banking-specific tier-elevation factors

In addition to the capability rubric, the following bank-specific factors elevate the tier:

- In-scope CCAR/DFAST or CECL use case → tier-1 by default under most firm policies.
- Customer-binding credit decisioning under ECOA / Reg B → conduct factor high, regulatory factor high.
- AML, sanctions, or BSA transaction-monitoring use case at scale → regulatory factor high, FFIEC manual exposure named.
- OCC Heightened Standards bank with model in risk-appetite statement → tier-1 by default for the named model.
- Sponsor-bank arrangement with fintech-supplied AI → vendor-dependence and concentration factors elevated; bank-side committee path named.

## Banking-specific re-tiering triggers

Add to the re-tiering trigger block for banking sector use cases:

- Annual stress-testing cycle (where in scope). Owner: stress-testing function. Detection: stress-testing calendar.
- Adverse-action notice generation method change. Owner: consumer compliance with model owner. Detection: change-management notice.
- Material change in NACHA, OFAC, or FFIEC manual expectations relevant to the use case. Owner: regulatory change function. Detection: regulatory horizon scan.
- Sponsor-bank-fintech arrangement change (program expansion, dual-sponsor add, sponsor exit). Owner: bank's third-party risk function. Detection: third-party-risk reporting plus contract change-control.
- MRA / MRIA issued against the use case or against a closely related model. Owner: regulatory affairs. Detection: examiner correspondence.

## Common pitfalls in banking tiering

- Treating CFPB authority as out of scope because the entity is OCC- or FRB-supervised; CFPB consumer-protection authority reaches large banks for ECOA, RESPA, EFTA, and UDAAP purposes.
- Treating an AML model's tier as low because operations are internal; FFIEC manual exposure and SAR-workflow integration push the regulatory factor upward regardless of customer-facing posture.
- Omitting CCAR/DFAST pedigree on a stress-eligible model; auditors and examiners catch this in the cross-walk.
- Tiering a sponsor-bank-fintech AI use case as if the bank's exposure were limited to vendor risk; the bank inherits model risk wholesale under the June 2023 interagency guidance and the July 2024 joint statement.
- Underweighting the OCC Heightened Standards bank's risk-appetite-statement linkage; tier-1 models in scope of the appetite statement carry board-level reach.
