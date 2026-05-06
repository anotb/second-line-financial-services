# Insurance sector overlay — concentration-risk-review

When the engagement scope flags insurance, load this overlay alongside `references/source-anchors.md`. It carries the insurance-specific concentration framings the generic skill does not own.

## Policy-administration system concentration

- A small set of policy-administration vendors covers most of the US carrier market. A carrier whose pricing, billing, claims, and renewal flows all sit on one PAS vendor is concentration even where the contract is sound. The dimension reads as `single-vendor` with a function-spread sub-finding; the substitutability read names that PAS migration is multi-year, expensive, and rarely fully rehearsed.

## Claims-TPA concentration

- A property-and-casualty carrier may use one TPA across multiple lines of business; a workers'-compensation carrier may use one TPA for a substantial book. The TPA's own infrastructure (cloud, workflow vendor, sub-contracted adjusters) carries the concentration's downstream dependencies. The fourth-party dimension surfaces these; recommend a sub-contractor-chain re-ask in `vendor-diligence` where rank-2 visibility is thin.

## Reinsurance and retrocession-vendor concentration

- Reinsurance counterparty concentration is a separate (and well-developed) discipline; this skill does not replicate the reinsurance-credit concentration view. It does cover the concentration in operational vendors that support reinsurance accounting, claims-recovery processing, and treaty administration. The line is: counterparty credit concentration sits with the actuarial and reinsurance teams; operational-vendor concentration that supports reinsurance flows sits here.

## Holding-company filing dimension

- **NAIC Insurance Holding Company System Regulatory Act (Model #440)** [verify model number] and **Holding Company Model Regulation (Model #450)** [verify model number]. Form B and Form F filings carry the holding-company-level material-vendor concentration view across affiliates; the structured record from this skill is the supporting artifact for the operational-risk concentration items in Form F [verify Form F section reference]. State-by-state adoption.
- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act (Model #505)** [verify model number]. Critical outsourced functions and their concentration posture belong in the ORSA Summary Report; this skill's output is the input to the ORSA section that addresses operational-third-party concentration.

## Analytics-vendor and ECDIS concentration in life and health

- **Colorado SB 21-169** and **NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting** (January 2024) [verify exact circular number] [verify section]. Where multiple lines of business depend on a single ECDIS or analytics-vendor, the concentration is read as `technology-stack-other` and as `ai-provider` where applicable. State-by-state adoption.

## NAIC Bulletin on AI-vendor concentration

- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers** (December 4, 2023). Carrier accountability for vendor and third-party AI extends to the concentration question: a carrier dependent on one AI vendor across pricing, claims, and underwriting use cases carries concentration the bulletin reads as part of the AIS Programme third-party-AI-accountability element. State-by-state adoption.

## Output-template additions for insurance

- Form F and ORSA cross-reference for the holding-company filing dimension.
- Policy-administration-system row in the function-level dimension.
- Claims-TPA row with sub-contractor-chain visibility for the rank-2 disclosed adjuster network.
- AI-provider row read against the NAIC Bulletin AIS Programme expectations where AI is in scope.

## Common pitfalls in insurance concentration reviews

- Confusing reinsurance counterparty credit concentration with operational-vendor concentration that supports reinsurance flows. Two different reviews, two different owners.
- Reading PAS concentration as a single-vendor finding without the function-spread sub-finding.
- Missing the ECDIS and analytics-vendor concentration in life and health where state-specific obligations apply.
- For AI vendors used across multiple lines, undercounting the AIS-Programme accountability dimension.
- Treating the structured record as the Form F filing or the ORSA section. The record is an input; the regulated filing has its own legal artifact.
