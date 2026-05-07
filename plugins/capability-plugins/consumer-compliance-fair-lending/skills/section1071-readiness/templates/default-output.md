# Section 1071 readiness — gap memo and matrix template

This template carries two artifacts: the **narrative gap memo** (rendered as a Word document via the `docx` skill) and the **readiness matrix** (rendered as an Excel workbook via the `xlsx` skill). The memo references the matrix by file name; the matrix is the system-of-record for the per-data-point readiness state, the memo is what the named accountable executive reads.

---

## Part A — Narrative gap memo (Word)

**Assessment ID**: [firm-defined, e.g., `<entity-id>-1071-readiness-<YYYY-NN>`]
**As-of date**: [YYYY-MM-DD]
**Entity assessed**: [legal-entity name; LEI where applicable]
**Author / persona**: [head of consumer compliance | chief compliance officer | fair-lending lead | engagement lead]
**Sponsor / accountable executive**: [role]
**Source posture**: [public-only | public-plus-firm-policy | public-plus-firm-policy-plus-evidence | connector-aware]
**Confidence label**: [high | medium | low | unknown]
**Companion matrix**: [filename of the readiness matrix workbook]
**Status**: [draft | under-review | signed-off]

### 1. Executive summary

Five bullets maximum. Lead with the current-state caveat on §1071 compliance dates (the dates have been moved by court order and bureau response; the date carried in this memo is sourced as of the as-of date and may move).

- [Tier classification and currently effective compliance date, marked `[verify current effectiveness and tier dates]` and sourced]
- [Headline readiness state across the 12 CFR 1002.107 data points: how many `ready`, how many `partial`, how many `gap`, how many `unverifiable`]
- [The most material gap (firewall, demographic-collection mechanics, vendor LOS, FIG conformance, or other)]
- [Open legal / interpretive question that, if it resolves the wrong way, changes the readiness state]
- [The sign-off ask of the accountable executive]

### 2. Scope and source posture

| Field | Value |
|---|---|
| Jurisdiction | United States |
| Entity type | [national bank | state-member bank | state-non-member bank | savings association | credit union | fintech | sponsor-bank-program | other] |
| Sector overlay loaded | [banking | payments-fintech | (with capital-markets / insurance flagged out-of-scope where applicable)] |
| Cross-cutting overlays loaded | [privacy | conduct | both | neither] |
| Engagement type | [pre-compliance-date readiness | annual operating-state refresh | vendor / LOS readiness | re-scope after volume change] |
| Timeframe | [as-of date and target sign-off date] |
| Source posture | [as above] |
| Engagement-scope record reference | [if supplied] |

### 3. Covered-financial-institution determination

| Field | Value | Source |
|---|---|---|
| Covered originations to small businesses, year T-1 | [count] | [system / report] |
| Covered originations to small businesses, year T-2 | [count] | [system / report] |
| 12 CFR 1002.105 threshold | [value, marked `[verify under current rule]`] | `references/source-anchors.md` |
| CFI determination | [is-CFI | not-CFI | sensitivity-at-boundary] | |
| Tier classification | [Tier 1 | Tier 2 | Tier 3] | |
| Currently effective compliance date for tier | [YYYY-MM-DD] `[verify current effectiveness and tier dates]` | [CFPB compliance-resources page URL with retrieval date] |
| Methodology used to count covered originations | [narrative; per-product covered-transaction mapping reference] | |
| Affiliate aggregation question | [resolved / open question for legal] | |

### 4. Covered-application and covered-credit-transaction scoping

Per-product mapping. The full table sits in the matrix's *Product mapping* sheet; the memo carries the executive read.

- **In-scope products**: [list with brief rule-cited rationale]
- **Out-of-scope products**: [list with rule-cited rationale]
- **Edge-case products**: [list with the open legal question for each]

### 5. Data-point readiness against 12 CFR 1002.107

The full per-data-point matrix sits in the matrix's *Data-point matrix* sheet (one row per 1002.107 data point, with system of record, capture method, readiness, gap description, owner, due date). The memo carries the headline read:

- **Ready**: [n] data points
- **Partial**: [n] data points
- **Gap**: [n] data points
- **Unverifiable** (evidence not available at current source posture): [n] data points

Notable per-data-point findings:

- [Data point]: [readiness state] — [narrative finding and the action]
- [Data point]: [readiness state] — [narrative finding and the action]

### 6. Applicant-demographic data-collection mechanics

- **Collection point in the application flow**: [where in the application; channel-by-channel where relevant]
- **Script and form text**: [reference to the document; check that the rule's required disclosures are present]
- **Refusal handling**: [code value used; the rule requires a specific refusal code, not `null`]
- **Principal-owner identification logic**: [narrative; how principal owners are identified]
- **Firm-observed-capture procedure** (where applicable, per the rule's narrow allowance for in-person applications): [narrative or "not applicable"]
- **Data-flow diagram**: [reference to the diagram in the matrix or appendix]
- **Findings**: [list]

### 7. Firewall and data-isolation review per 12 CFR 1002.108

- **Systems hosting demographic data**: [LOS, customer-360, data warehouse, other]
- **Role-based access controls**: [narrative; reference to the access-control policy]
- **Named exceptions** (the rule's permitted exceptions where the underwriter cannot reasonably avoid access): [list with documentation reference]
- **Firewall-trained-personnel design**: [training, cadence, attestation]
- **Audit-log posture for access events**: [narrative]
- **Customer-360 / relationship-management-view review**: [the predictable depository firewall failure mode; explicit treatment]
- **Findings**: [list]

### 8. Recordkeeping under 12 CFR 1002.110

- **Records identified**: [the §1071 dataset and supporting documentation]
- **Retention period**: three years from date of submission
- **Disposition policy**: [reference to the firm's records-retention schedule and the §1071 row within it]
- **Recovery posture**: [can the firm produce records on regulator request within an examination timeline?]
- **Findings**: [list]

### 9. Reporting and filing readiness (FIG conformance)

- **FIG edition built against**: [edition / version, marked `[verify current edition]`]
- **File-format readiness**: [ready | partial | gap]
- **Validation engine in use**: [CFPB-provided | vendor-built | in-house]
- **Test-submission plan**: [narrative; named test cycles]
- **Submission channel**: [CFPB-specified channel, marked `[verify current channel and authentication mechanics]`]
- **Named owner of submission**: [role]
- **Findings**: [list]

### 10. Vendor and LOS readiness

The full per-vendor table sits in the matrix's *Vendor readiness* sheet. The memo carries the executive read:

- **Material vendors in scope**: [list with role]
- **Attestation status**: [n signed, n requested, n not-yet-requested]
- **Change-control identifier per vendor for the §1071 build**: [reference]
- **Vendor-driven gaps with a `severity` of `high` or `blocking`**: [list]

### 11. Fair-lending testing readiness on the §1071 dataset

- **Completeness of demographic fields needed for testing**: [narrative]
- **Firewall compatibility with fair-lending team access** (the testing team is a permitted exception under 1002.108; access has to be designed in): [narrative]
- **Data-pipeline from production §1071 capture to the fair-lending analytics environment**: [narrative]
- **Cross-reference**: route to `fair-lending-test-plan` for the testing design once the dataset exists.

### 12. Bona-fide-error and safe-harbor approach (12 CFR 1002.112)

- **Documented bona-fide-error policy**: [in place | drafted | not-yet-drafted]
- **Procedure for amending submitted data**: [narrative]
- **Named owner**: [role]
- **Link to broader regulatory-reporting-error policy**: [reference]
- **Findings**: [list]

### 13. Privacy posture (where the privacy overlay is loaded)

- **GLBA Safeguards posture on the §1071 dataset**: [narrative; reference to the firm's information-security program]
- **State-privacy applicability**: `[verify state-specific scope]` for [list of states]
- **CFPB modified-data publication and re-identification considerations**: [narrative; flag for low-volume / identifiable-geography portfolios]
- **Findings**: [list]

### 14. Conduct posture (where the conduct overlay is loaded)

- **Demographic-collection-script integrity in practice**: [narrative; front-line behaviour]
- **Firewall integrity in practice**: [narrative; daily behaviour vs. designed control]
- **Vendor-staff conduct in the applicant interaction**: [narrative]
- **Conduct-themes routing**: [conduct committee | risk committee | both]
- **Findings**: [list]

### 15. Gap list

Severity definitions: `blocking` (cannot go live), `high` (must remediate before go-live), `medium` (target remediation in next cycle), `low` (track and monitor).

| ID | Gap | Severity | Source (table / data point / firewall / vendor / FIG / other) | Owner | Due date | Status |
|---|---|---|---|---|---|---|
| 1 | | blocking / high / medium / low | | | YYYY-MM-DD | open / in-progress / closed |

(The full gap list lives in the matrix's *Gap list* sheet; the memo carries the executive selection of `blocking` and `high` items.)

### 16. Open questions for legal and compliance

| ID | Question | Function | Status |
|---|---|---|---|
| 1 | | legal | open |

### 17. Source trace

| Claim | Source | Section | Date | URL or file ref |
|---|---|---|---|---|
| | | | | |

Cite `references/source-anchors.md` for the canonical citations. Use `[verify current effectiveness and tier dates]` for compliance-date references, `[verify current edition]` for FIG and other edition-specific references, `[verify state-specific scope]` for state-privacy references, and `[verify subsection]` where the exact 1002.107 subsection label is uncertain. Do not invent.

### 18. Review-gate posture and sign-off ask

- **Review gates this assessment must clear**: [scope | evidence | authority | impact | decision] per `references/review-gates.md`.
- **The skill does not file**. The matrix and memo carry the readiness state; the named accountable executive signs off; the firm's regulatory-reporting pipeline files the actual submission through the CFPB-specified channel.
- **Sign-off ask of the accountable executive**: [the specific decision the memo asks the executive to make]
- **Next review trigger**: [next compliance milestone | scope-change trigger | tier-shift trigger | post-go-live operating-state refresh date]

---

## Part B — Readiness matrix (Excel)

The matrix workbook produced by the `xlsx` skill carries the structured per-record detail. Sheet structure:

### Sheet 1 — Cover

| Field | Value |
|---|---|
| Assessment ID | |
| As-of date | |
| Entity assessed | |
| Author / persona | |
| Sponsor | |
| Source posture | |
| Confidence label | |
| Companion memo | [filename] |

### Sheet 2 — Scope and CFI determination

Mirrors §3 of the memo: covered-origination counts, threshold, CFI determination, tier classification, compliance date with sourced citation, methodology, affiliate aggregation note.

### Sheet 3 — Product mapping (per 12 CFR 1002.106)

| Product | In / Out / Edge | Rule reference | Rationale | Open question for legal |
|---|---|---|---|---|
| | | 1002.106(a) / (b) / etc. | | |

### Sheet 4 — Data-point matrix (per 12 CFR 1002.107)

The core sheet. **One row per 1002.107 data point.** The list is the contract; partial matrices are not assessments.

| # | Data point | Rule reference | System of record | Capture method | Readiness | Gap description | Owner | Due date | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Unique identifier | 1002.107(a)(1) `[verify subsection]` | | applicant_provided / firm_inferred / vendor_supplied / manual_entry / not_yet_captured | ready / partial / gap / unverifiable | | | YYYY-MM-DD | |
| 2 | Application date | 1002.107(a)(2) `[verify subsection]` | | | | | | | |
| 3 | Application method | 1002.107(a)(3) `[verify subsection]` | | | | | | | |
| 4 | Application recipient | 1002.107(a)(4) `[verify subsection]` | | | | | | | |
| 5 | Credit type — product type | 1002.107(a)(5) `[verify subsection]` | | | | | | | |
| 6 | Credit type — guarantee | 1002.107(a)(5) `[verify subsection]` | | | | | | | |
| 7 | Credit type — loan term | 1002.107(a)(5) `[verify subsection]` | | | | | | | |
| 8 | Credit purpose | 1002.107(a)(6) `[verify subsection]` | | | | | | | |
| 9 | Amount applied for | 1002.107(a)(7) `[verify subsection]` | | | | | | | |
| 10 | Amount approved or originated | 1002.107(a)(8) `[verify subsection]` | | | | | | | |
| 11 | Action taken | 1002.107(a)(9) `[verify subsection]` | | | | | | | |
| 12 | Action taken date | 1002.107(a)(10) `[verify subsection]` | | | | | | | |
| 13 | Denial reasons | 1002.107(a)(11) `[verify subsection]` | | | | | | | |
| 14 | Pricing — interest rate | 1002.107(a)(12) `[verify subsection]` | | | | | | | |
| 15 | Pricing — total origination charges | 1002.107(a)(12) `[verify subsection]` | | | | | | | |
| 16 | Pricing — broker fees | 1002.107(a)(12) `[verify subsection]` | | | | | | | |
| 17 | Pricing — initial annual charges | 1002.107(a)(12) `[verify subsection]` | | | | | | | |
| 18 | Pricing — additional cost for MCA / sales-based financing | 1002.107(a)(12) `[verify subsection]` | | | | | | | |
| 19 | Pricing — prepayment penalty | 1002.107(a)(12) `[verify subsection]` | | | | | | | |
| 20 | Census tract (principal address) | 1002.107(a)(13) `[verify subsection]` | | | | | | | |
| 21 | Gross annual revenue | 1002.107(a)(14) `[verify subsection]` | | | | | | | |
| 22 | NAICS code | 1002.107(a)(15) `[verify subsection]` | | | | | | | |
| 23 | Number of workers | 1002.107(a)(16) `[verify subsection]` | | | | | | | |
| 24 | Time in business | 1002.107(a)(17) `[verify subsection]` | | | | | | | |
| 25 | Number of principal owners | 1002.107(a)(18) `[verify subsection]` | | | | | | | |
| 26 | Minority-owned business status | 1002.107(a)(19) `[verify subsection]` | | | | | | | |
| 27 | Women-owned business status | 1002.107(a)(20) `[verify subsection]` | | | | | | | |
| 28 | LGBTQI+-owned business status | 1002.107(a)(21) `[verify subsection]` | | | | | | | |
| 29 | Ethnicity of principal owners | 1002.107(a)(22) `[verify subsection]` | | | | | | | |
| 30 | Race of principal owners | 1002.107(a)(22) `[verify subsection]` | | | | | | | |
| 31 | Sex of principal owners | 1002.107(a)(22) `[verify subsection]` | | | | | | | |

Verify the complete list and the exact subsection labels against the current rule text at each engagement; the CFPB has issued technical amendments and the matrix's `Rule reference` column must match.

### Sheet 5 — Demographic-collection mechanics

| Field | Value |
|---|---|
| Collection point | |
| Script reference | |
| Required-disclosures present | yes / no / partial |
| Refusal-handling code | |
| Principal-owner identification logic | |
| Firm-observed-capture procedure | |
| Data-flow reference | |
| Findings | |

### Sheet 6 — Firewall (12 CFR 1002.108)

| System | Role | Access control | Permitted-exception process | Trained personnel | Audit-log | Finding |
|---|---|---|---|---|---|---|
| | | | | | | |

### Sheet 7 — Vendor readiness

| Vendor | Role | Attestation status | Change-control ID | Contractual responsibility | SLA | Finding |
|---|---|---|---|---|---|---|
| | LOS / form / pricing / submission utility / other | signed / requested / not-yet-requested | | | | |

### Sheet 8 — Gap list

| ID | Gap | Severity | Source | Owner | Due date | Status | Conduct theme (where applicable) |
|---|---|---|---|---|---|---|---|
| | | blocking / high / medium / low | | | | open / in-progress / closed | |

### Sheet 9 — Source trace

| Claim | Source | Section | Date | URL or file ref |
|---|---|---|---|---|
| | | | | |

---

*Memo depth scales to source posture and review type.* A pre-compliance-date readiness check at public-plus-firm-policy posture reads narrative-heavy with `unverifiable` rows where evidence has not landed yet; an annual refresh at connector-aware posture reads matrix-heavy with the year-on-year delta as the headline.

*Audience drives shape.* A pack for the compliance programme lead reads operational. A pack for the named accountable executive leads with the residual gap posture and the sign-off question. A pack for a regulator dialogue reads as a justification of the firm's own readiness posture before the supervisor asks.
