# Policy diff change log

Diff ID: <DIFF-YYYY-XXX-NN>
As of: <YYYY-MM-DD>
Author / persona: <role>
Status: <draft / in-review / attested>
Engagement scope reference: <ENG-YYYY-XXX-NN or "scope not formalised">

## 1. Diff anchor

| Field | Value |
|---|---|
| Policy name | <named policy> |
| Policy domain | <TPRM / BSA-AML / model risk / cybersecurity / conduct / fair lending / AI governance / op resilience> |
| Policy owner | <named role> |
| Named approver for version B | <committee / role / board> |
| Trigger | <annual-review / mra-remediation / regulatory-amendment / consent-order / internal-incident / control-failure / board-direction / system-migration / scope-expansion> |
| Trigger detail | <free text: cite the SR letter, MRA reference, board minute, etc.> |
| Target effective date | <YYYY-MM-DD> |
| Source posture | <public-only / public-plus-firm-policy / public-plus-firm-policy-plus-evidence / connector-aware> |

## 2. Versions in scope

| | Version A (prior) | Version B (proposed or new) |
|---|---|---|
| Version label | | |
| Approval date | | |
| Approver role | | |
| Document hash / pointer | | |
| Effective date | | |
| Status | live / superseded / draft / withdrawn | live / superseded / draft / withdrawn |

## 3. Change log

One row per change. Sections that did not change get a single row with `diff_type: no-change` so the reader can see they were inspected.

| ID | Section path (version B) | Diff type | Version A excerpt | Version B excerpt | Substantive delta | Materiality | Downstream impact (training / control / system / comms / attestation) | Approver | Effective date | Confidence | Open questions |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CHG-001 | <heading hierarchy + clause number> | <added / removed / reworded-substantive / reworded-cosmetic / restructured / defined-term-changed / cross-reference-changed / no-change> | <text excerpt> | <text excerpt> | <one sentence: operative verb shift, threshold movement, named-role change, timing change, scope shift> | <material / incremental / clarifying / cosmetic / open-question> | <yes/no per category, with one-sentence rationale per yes> | <named approver role> | <YYYY-MM-DD or section-specific phase-in> | <high / medium / low> | <items requiring legal or compliance review> |

> Cosmetic and clarifying rows usually carry no downstream impact. Material rows almost always do. Where the materiality call is contested, the row's materiality is `open-question` and routes to the named reviewer.

## 4. Cross-policy ripple

Other firm policies that point to renamed defined terms, moved sections, or deleted paragraphs in this policy.

| Referenced policy | Ripple type | Affected change IDs | Remediation owner | Notes |
|---|---|---|---|---|
| <policy name> | <stale-cross-reference / renamed-defined-term / deleted-section-pointer / moved-section-pointer / supersession-chain> | <CHG-IDs> | <named role> | <one paragraph> |

## 5. Defined-term inventory

Defined terms whose name or scope changed between versions. Downstream consumers (training, control matrix, attestation) read this block.

| Term | Change type | Version A definition | Version B definition | Downstream consumers |
|---|---|---|---|---|
| <defined term> | <renamed / scope-broadened / scope-narrowed / added / removed> | <text> | <text> | <named policies, controls, training modules> |

## 6. Approver routing summary

Material rows grouped by approver so the policy committee or board paper can be drafted directly.

### <approver role 1>
- <CHG-IDs>: <one-paragraph summary of the rows>

### <approver role 2>
- <CHG-IDs>: <summary>

## 7. Communication plan summary

Rows grouped by audience so line-manager packs and all-staff comms can be sequenced.

### All-staff
- <CHG-IDs>: <delivery window>, <one-line summary>

### Line-managers
- <CHG-IDs>: <delivery window>, <one-line summary>

### Specific function: <function name>
- <CHG-IDs>: <delivery window>, <one-line summary>

### Customer-facing
- <CHG-IDs>: <delivery window>, <one-line summary>

### Vendor-facing
- <CHG-IDs>: <delivery window>, <one-line summary>

## 8. Open-question summary

Grouped by reviewer.

### Legal review
- <CHG-IDs>: <question with rule cite or factual ambiguity>

### Compliance review
- <CHG-IDs>: <question>

### Function head review
- <CHG-IDs>: <question>

### Policy owner
- <CHG-IDs>: <question>

## 9. Source trace and confidence

| Section | Confidence | Rationale |
|---|---|---|
| <policy section or version pair> | <high / medium / low> | <unambiguous redline / interpretation involved / change-control record incomplete> |

## 10. Sign-off

- Policy owner: <role>, <attestation status>, <date>
- Named approver: <role>, <approval status>, <date>
- Independent reviewer (advisory: legal / compliance / internal audit): <role>, <date>

> The change log is a draft until the policy owner and the named approver attest. Material claims cite version A or version B (or, for downstream impact, the control matrix or obligation register where supplied). `[evidence needed]` flags items needing follow-up.

## 11. Revision log

Append-only.

| Date | Reason | Delta | Approved by |
|------|--------|-------|-------------|
| <YYYY-MM-DD> | initial diff | created | <persona> |
