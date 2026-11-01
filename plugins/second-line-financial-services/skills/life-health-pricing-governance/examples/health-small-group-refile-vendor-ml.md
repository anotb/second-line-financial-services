# Example: small-group health refile with a new geographic-area factor and a vendor-supplied ML risk-adjustment input

**Public-source-derived. No named institutions.**

## Scenario

A US health insurer is refiling small-group rates in three states. The refile introduces a new geographic-area factor (a redrawn rating-area structure) and a vendor-supplied ML risk-adjustment input. ACA pricing rules apply.

## Source posture

Public-plus-firm-policy-plus-evidence.

## What the artifact carries

### Rate filing summary

Three SERFF filings (small-group ACA-regulated). Refile, not new filing. Effective date next plan year.

### Rating factor map (Excel workbook)

Five rating factors (four are ACA-permitted: family size, geography, age within 3:1, tobacco within 1.5:1; the ML risk-adjustment input is a sub-component of the geographic factor's actuarial methodology, not an additional rating factor). The artifact names this distinction clearly: the ML input feeds the actuarial methodology under the permitted geographic factor; it is not an additional factor.

### Unfair discrimination analysis

Per-factor under #880 plus a rating-plan-as-a-whole assessment. All factors carry `clear` actuarial-justification status because they are ACA-permitted on the bright-line list. Plan-as-a-whole assessment carries the methodology question (whether the vendor ML input is being applied consistently within the permitted geographic factor).

### Disparate-impact red flags

State guidance limited in the three states in scope; no CO, NY, or CA presence in this filing. Standard #880 monitoring expectation only.

### AI / ML governance: AIS Program cross-walk

Vendor ML input pulls third-party-AI-accountability obligations under the NAIC Bulletin December 2023. Six AIS Program elements `in-place`, three `partial`. The carrier-level monitoring against the vendor's input is the key open item.

### Documentation completeness vs federal model-risk-equivalent

Vendor-supplied validation evidence; carrier-level validation `partial` (similar to the AU example). Cite the **Joint Interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026; supersedes SR 11-7)** as analogous.

### State DOI bulletin alignment

Three states in scope; standard rate-filing checklist. NAIC Model Bulletin adoption status verified per state on the analysis date.

### ACA-pricing checks

| Check | Status |
|---|---|
| Permitted rating factors only used | `pass` |
| No prohibited rating factors used | `pass` |
| Geographic rating-area structure under 45 CFR §147.102 | `pass` for two states, `[evidence-needed]` for the third (rating-area-vs-zip-code mapping documentation incomplete) |
| Guaranteed renewability under §147.106 | `pass` |

### Privacy and consumer-disclosure posture

HIPAA applies (small-group health). Vendor BAA chain on file. Minimum-necessary analysis `pass` (the vendor receives only the inputs needed for the risk-adjustment computation).

### Recommended disposition

`Approve-with-conditions`. Two conditions: (1) complete the rating-area-vs-zip-code mapping documentation for the third state before SERFF submission; (2) close the carrier-level monitoring gap on the vendor ML input within 90 days of effective date.

## Public sources used

- ACA pricing rules (45 CFR Part 147).
- NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers (December 2023).
- NAIC Unfair Trade Practices Act, Model #880.
- HIPAA Privacy Rule, 45 CFR Part 164 Subpart E.
- Joint Interagency Revised Guidance on Model Risk Management (OCC Bulletin 2026-13 / FRB SR 26-2 / FDIC FIL-15-2026, April 17, 2026; supersedes SR 11-7) — cited as analogous model-risk expectation language.
