# Insurance sector overlay — criticality-assessment

When the engagement scope flags insurance, load this overlay alongside `references/source-anchors.md`. It carries the insurance-only criteria the generic capability skill does not own.

## Operative supervisory frame

- **NAIC Insurance Data Security Model Law (Model #668), §4.F** third-party service-provider obligations including a risk-based criticality assessment.
- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number]. Critical outsourced functions belong in the ORSA Summary Report; a `critical` call here flows into the ORSA narrative.
- **NAIC Insurance Holding Company System Regulatory Act (Model #440)** [verify model number] and **Holding Company Model Regulation (Model #450)** [verify model number]. Where the arrangement is intragroup, Form B / Form D filings depend on the affiliated-vendor read; criticality call drives the disclosure shape.
- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers** (December 4, 2023). Carrier accountability for vendor and third-party AI; AIS Program elements (governance, risk management, testing, validation, third-party-AI accountability) inform the criticality read for AI vendors on a regulated decisioning path.

## Candidate IBS for insurers

Important business services at an insurance carrier typically include claims handling and adjustment, policy administration (issuance, endorsements, renewals), underwriting, premium collection and reconciliation, policyholder communications and disclosures, and reserve and capital reporting. State guaranty-fund and policyholder-protection considerations weight the criticality call upward where the arrangement sits on the policyholder-facing path. The IBS list is the firm's; the candidate list above tracks BCBS Principles for Operational Resilience (March 2021) translated into the insurance setting.

## State-by-state lens

- **State adoption tracker for the NAIC AI Bulletin** is the public reference; the operative state framework for an AI-driven life-insurance underwriting use case may include **Colorado SB 21-169 implementing regulation** (3 CCR 702-10 §1 [verify section]), the **NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting** (January 2024) [verify exact circular number], and similar state circulars.
- The criticality call considers the state-by-state adoption pattern where the arrangement supports a regulated decisioning path; an AI vendor on the underwriting-decisioning chain in a state with a published AI circular sits at `important` at minimum.

## Cross-link inside the plugin

- **`vendor-diligence` insurance overlay** consumes the `tier` and the named IBS to set diligence depth, including AIS Program third-party-AI accountability where applicable.
- **`exit-plan` insurance overlay** consumes the `tier`, the supported IBS, and the customer-impact read to set transition mechanics, including policyholder-notice posture and policy-administration data portability.
- **`concentration-risk-review`** consumes the `concentration_considerations` flag for hyperscaler region, claims-TPA reach, and shared-policy-administration-platform concentration.

## AI vendor mode at an insurer

When `ai_vendor=true` and the firm is an insurer:

- **NAIC AI Bulletin (December 2023)** AIS Program third-party-AI accountability frames the criticality call. An AI vendor on a regulated insurance-decisioning path (underwriting, pricing, claims-decisioning) is rarely below `important`.
- The carrier remains accountable for the AI vendor's decisions reaching policyholders. The criticality call must reflect that the carrier (not the vendor) is the regulated entity for fairness, transparency, and consumer-impact obligations.
- A `critical` AI-vendor call triggers parallel review by the AI governance function downstream; record the cross-link.

## Output additions for insurance

- IBS named explicitly and matched against the candidate list above.
- ORSA-Summary-Report inclusion check for `critical` calls.
- Holding-company-act applicability check for intragroup arrangements.
- State-by-state lens for AI vendors on regulated decisioning paths.

## Common pitfalls in insurance criticality calls

- Skipping the policyholder-facing-path test. A vendor that touches policyholder communications, claims, or premium collection sits closer to `critical` than the procurement category suggests.
- Treating an AI vendor as a "tooling" arrangement. Where the AI system reaches a regulated decision, the carrier accountability framework applies and the tier follows.
- Missing the holding-company-act lens for intragroup arrangements. An affiliate vendor still triggers the criticality call and the Form B / Form D filing read.
- Defaulting to the vendor's claimed RTO/RPO as the test. The firm's tolerance from the IBS impact analysis is the test; a state guaranty-fund event is a low-probability high-severity tail that must inform the tolerance.
