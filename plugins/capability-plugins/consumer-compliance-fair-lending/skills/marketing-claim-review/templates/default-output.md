# Marketing-claim review memo

> Status: draft until the named decision forum acts. The memo surfaces marketing-asset findings for human decision; it does not approve marketing for launch, take down live assets, finalize UDAAP / fair-lending / privacy-claim determinations, or issue customer-facing actions.

## 1. Scope and review posture

| Field | Value |
|---|---|
| Review ID | `[review_id]` |
| As of date | `[YYYY-MM-DD]` |
| Trigger | `pre-launch-review` / `in-market-sweep` / `post-complaint-trigger` / `post-mra-trigger` / `regulator-inquiry` / `ai-personalisation-deployment` / `other` |
| Unit of analysis | `single-creative` / `single-campaign` |
| Campaign or creative ID | `[id]` |
| Period in market | `[start] to [end]` |
| Channels in scope | `[web, in-app, email, push, paid-social, digital-display, broadcast, print, script, landing-page, app-store, other]` |
| Sector overlay set | `[banking / payments-fintech / capital-markets / insurance]` |
| Cross-cutting overlay set | `[conduct (where chained), privacy (default for digital channels)]` |
| Source posture | `public-only` / `public-plus-firm-policy` / `public-plus-firm-policy-plus-evidence` / `connector-aware` |
| Sampling basis | `full-coverage` / `random-sample` / `risk-based-sample` / `channel-stratified-sample` / `n-a` |
| Sampling-frame description | `[describe; for non-full-coverage]` |
| Exclusions | `[explicit out-of-scope items]` |

### Reviewer and review posture

- Reviewer role: `[marketing-compliance-reviewer / independent-consumer-compliance-second-line / advisory-engagement / joint-with-sponsor-bank / other]`
- Review independence: `independent-second-line` / `embedded-1-5-line` / `advisory` / `joint-with-sponsor-bank` / `other`
- Counsel directing: `[yes / no]`
- Legal privilege posture: `attorney-client-privileged` / `attorney-work-product` / `dual-purpose-business-and-privileged` / `not-privileged` / `posture-pending-counsel`

## 2. Asset register

| Asset ID | Channel | Audience | Version | Dates in market | Device classes captured | Screenshot or recording reference |
|---|---|---|---|---|---|---|
| | web / in-app / email / push / paid-social / digital-display / broadcast / print / script / landing-page / app-store / other | [target segment, geography, language] | [version] | YYYY-MM-DD to YYYY-MM-DD | desktop / mobile / tablet / TV / radio / OOH | [file path or asset id] |

## 3. Per-asset findings

For each asset in the register, populate the following blocks. Repeat sections 3.a through 3.i per asset.

### 3.a Asset claim register (asset `[asset_id]`)

| Claim ID | Claim text (as it appears) | Category | Substantiation status | Substantiation source | Date | Notes |
|---|---|---|---|---|---|---|
| | | rate / fee / apr-mapr / eligibility / endorsement / comparative-superlative / privacy / security / rewards / availability / time-to-funding / green-or-esg / ai-capability / other | substantiated / partially-substantiated / not-substantiated / not-substantiable / evidence-needed | internal-data / third-party-study / regulator-data / controlled-study / MAP / other | YYYY-MM-DD | |

### 3.b Disclosure adequacy (asset `[asset_id]`)

| Operative rule | In-scope per asset | Required disclosure | Disclosure location | Device-class delta | Clear-and-conspicuous read | Finding |
|---|---|---|---|---|---|---|
| Reg Z 1026.16 (open-end credit advertising; trigger terms) | yes / no / n-a | | above-the-fold / below-the-fold / on-click / etc. | desktop / mobile / tablet | adequate / inadequate / indeterminate | |
| Reg Z 1026.24 (closed-end credit advertising; trigger terms; mortgage prohibitions) | yes / no / n-a | | | | | |
| Reg Z 1026.40 (HELOC advertising) | yes / no / n-a | | | | | |
| Reg Z 1026.60 (card application and solicitation; Schumer box) | yes / no / n-a | | | | | |
| Reg DD 1030.8 (deposit-account advertising) | yes / no / n-a | | | | | |
| FDIC 12 CFR Part 328 (FDIC insurance representation) | yes / no / n-a | | | | | |
| MLA 32 CFR 232 (MAPR; covered-borrower disclosures) | yes / no / n-a | | | | | |
| TRID 12 CFR 1026.37 / 1026.38 (mortgage-disclosure adjacency) | yes / no / n-a | | | | | |
| Other (firm-overlay; sector-specific) | | | | | | |

### 3.c Fair-lending distribution and targeting findings (asset `[asset_id]`)

| Finding | Category | Channel | Geographic scope | Audience-targeting parameters | Protected-class implication | AI-personalisation in path | Cross-reference to fair-lending-test-plan |
|---|---|---|---|---|---|---|---|
| | distribution-skew / targeting-parameter / ai-personalisation-audit / discouragement-content / dwelling-related-discriminatory-advertising / other | | MSA / census-tract / ZIP / state / national | [audience definition; lookalike-source; interest-categories; exclusions] | [ECOA / FHA theory if any] | yes / no | yes / no |

### 3.d UDAAP findings (asset `[asset_id]`)

| Finding | Prong | Claim or asset element implicated | Reasoning | Severity | Cross-reference to udaap-risk-review |
|---|---|---|---|---|---|
| | deception / unfairness / abusiveness | | | low / medium / high / critical | yes / no |

### 3.e Privacy claim findings (asset `[asset_id]`)

| Finding | Category | Claim or element | Reasoning | Cross-reference |
|---|---|---|---|---|
| | glba-reg-p-consistency / adchoices-representation / dark-pattern-privacy / state-privacy-law-interaction / sensitive-attribute-targeting / ai-personalisation-on-restricted-data / other | | | |

### 3.f Dark-pattern findings (asset `[asset_id]`)

| Finding | FTC taxonomy entry | Location in asset | Consumer-harm hypothesis | Severity |
|---|---|---|---|---|
| | nagging / obstruction / sneaking / interface-interference / forced-action / social-proof-manipulation / asymmetric-choice / hidden-subscription / confirmshaming / other | | | low / medium / high |

### 3.g AI-generated and AI-personalised content review (asset `[asset_id]`)

(Populate when AI is in the production path or the personalisation path on this asset.)

| Variant ID | Model ID | Prompt template | Variable inputs | Output review status | Substantiation per variant | Fabrication risk | Privacy implication |
|---|---|---|---|---|---|---|---|
| | | | | reviewed / pending / not-reviewed | substantiated / partially / not-substantiated / not-substantiable / evidence-needed | low / medium / high | |

- AI in path: `[yes / no]`
- April 2023 Joint Statement cited: `[yes / no]`
- Cross-reference to fair-lending-test-plan (algorithmic-targeting LDA): `[yes / no]`

### 3.h Recommended edits and kill-switch list (asset `[asset_id]`)

| Edit ID | Edit | Owner role | Due date | Severity | Kill-switch candidate |
|---|---|---|---|---|---|
| | | head-of-marketing-compliance / head-of-marketing / head-of-product / head-of-personalisation / sponsor-bank-marketing-compliance / other | YYYY-MM-DD | low / medium / high / critical | yes / no |

### 3.i Requested controls (asset `[asset_id]`)

| Control | Control type | Owner | Rationale |
|---|---|---|---|
| | MAP-control / marketing-review-gate / ai-personalisation-review / device-class-disclosure-test / substantiation-recency-control / dark-pattern-design-review / other | | |

## 4. Open legal questions

- `[items deferred to counsel; e.g., state-AG exposure under state baby-FTC acts; FTC Endorsement Guides applicability for non-bank fintech; treatment of "we will not sell your data" claims under CCPA / CPRA broader sale-and-share definitions; whether substantiation file is sufficient where the underlying study is the firm's own]`

## 5. Cross-references

- `udaap-risk-review` `[where the asset-level finding chains to a product-level UDAAP read]`
- `fair-lending-test-plan` `[where distribution or targeting raises a parallel ECOA / FHA theory needing a disparity test]`
- `complaint-theme-analysis` `[where the asset-level pattern aligns with or feeds a complaint cluster]`
- `adverse-action-review` `[where the asset relates to credit-decisioning representations covered by AAN]`
- `marketing-rule-evidence` (in `capital-markets-asset-management-compliance`) `[where the asset is in the SEC investment adviser Marketing Rule lane]`
- `model-card-builder` / `llm-vendor-evidence-review` `[where AI personalisation or AI-generated content is in path]`

## 6. Source trace and confidence

| Claim or finding | Source | Section | Date | URL or file path |
|---|---|---|---|---|
| | | | | |

- Confidence label: `high` / `medium` / `low` / `unknown`
- Assumptions and dependencies: `[list]`

## 7. Decision forum

- Named forum: `[marketing-compliance committee / CCO / counsel / conduct committee]`
- Decision status: `draft` / `submitted` / `in-review` / `decided` / `deferred` / `rejected`
- Decision date: `[YYYY-MM-DD]`
- Conditions: `[where applicable]`
