# Capital-markets sector overlay — contract-gap-review

When the engagement scope flags capital markets (advisers, broker-dealers, registered funds, asset managers, SCI entities), load this overlay alongside `references/source-anchors.md`. The bank-flavoured interagency-guidance frame is not the operative supervisory frame for non-bank registrants; the contract clause set is built differently.

## Operative supervisory frame

There is no single interagency third-party-contract bulletin for SEC and FINRA registrants. Contract expectations come through:

- **Investment Advisers Act Rule 206(4)-7** — adviser compliance-program rule. The adviser must have written policies and procedures reasonably designed to prevent violations; service-provider oversight requires contractual reach into evidence, monitoring, and incident-response cooperation. The matrix must surface the rows that enable the adviser's compliance-program oversight.

- **Investment Company Act Rule 38a-1(a)(4)** — fund compliance-program rule, including service-provider compliance-program-adequacy assessment for transfer agent, custodian, fund accountant, principal underwriter, valuation designee, pricing services. The fund CCO oversees; the contract must give the fund CCO information-access, certification, and incident-cooperation rights.

- **FINRA Rule 3110 (supervision)** — for broker-dealers, supervisory obligations extend to outsourced functions. The contract must support the BD's supervisory reach (records access, personnel-reach, exam-cooperation).

- **SEC Division of Examinations Risk Alerts on outsourced CCO arrangements** (the SEC's 2022 Risk Alert is the most-cited; [verify exact title and date]). Where the vendor is an outsourced-CCO provider, the matrix has additional rows on conflicts, capacity, evidence-access, and termination on regulatory-action triggers.

## Custody Rule

- **Investment Advisers Act Rule 206(4)-2** — where the vendor touches client assets, the contract must reflect qualified-custodian status, account-statement-delivery responsibilities, surprise-audit cooperation, and SLOA inventory access. Distinct contract-row set from generic safekeeping-services language.

## Books-and-records and retention

- **17 CFR §§240.17a-3 and 240.17a-4 (BD books-and-records)** and **17 CFR §270.31a-2 (fund books-and-records)**: retention windows, form requirements (electronic-storage media, write-once-read-many or audit-trail equivalents under amended 17a-4), prompt-production-on-request. The contract must give the registrant the records, in the required form, within the timeframes the rules contemplate. The matrix surfaces a row for retention scope and form, a separate row for production-timing, and a separate row for media-format compliance.

## Reg S-P (May 2024 amendments)

- **17 CFR Part 248 (Reg S-P) as amended May 2024** [verify exact compliance dates by entity type and size]: covered-institution safeguarding obligations, service-provider written-contract requirements, and breach-notification timing. The matrix must surface the Reg S-P contract-clause set, including the service-provider written-contract requirement and the upstream breach-notification clock that supports the covered institution's customer-notice obligation.

## Reg SCI

- **Reg SCI (17 CFR §§242.1000-1007)** for SCI entities. The contract for an SCI-system-supporting vendor must include incident-notification (timing aligned with the SCI entity's Reg SCI obligations), BCP cooperation, change-management cooperation, and documentation access. The clause set is enhanced over the generic third-party-contract baseline.

## Sub-adviser and best-execution arrangements

- **Sub-adviser oversight**: where a sub-adviser is the vendor, the contract must reflect the fund adviser's 38a-1 program reach, the code-of-ethics flow-down, soft-dollar and affiliated-broker conflicts disclosure, and termination triggers tied to compliance findings.
- **Best execution under Investment Advisers Act §206 fiduciary duty and FINRA Rule 5310** — where the vendor is an execution venue, ATS, or broker-dealer counterparty, the matrix overlaps with `best-execution-surveillance` (capital-markets sector skill). The contract must give the registrant the data and reporting that support the best-execution analysis.

## Cross-link inside the plugin

- **`exit-plan` capital-markets overlay** carries the records-portability sequence under 17a-4 and 31a-2, the fund-board notification posture for a critical-fund-service-provider exit, and the SEC and state notification posture where applicable. The contract gap matrix should evidence the contract clauses that enable each of those exit steps.

## Common capital-markets pitfalls

- Applying the bank-flavoured interagency-guidance contract checklist verbatim. The non-bank registrant's contract clause set comes through 206(4)-7, 38a-1, FINRA 3110, and the rule-specific contract reach (Custody Rule, books-and-records, Reg S-P, Reg SCI). The matrix must build off the right frame.
- Missing the books-and-records media-format row. Amended 17a-4 changed the acceptable-storage-media requirements; a contract written against the prior frame can be silent on the current requirement.
- Conflating fund-adviser oversight with sub-adviser oversight. The fund's 38a-1 reach into a sub-adviser is distinct from the adviser's 206(4)-7 reach into a service provider; the matrix must reflect the right rule for the right vendor.
- Treating the Reg S-P May 2024 service-provider contract requirement as already satisfied by the generic confidentiality clause. The amended rule has specific contract-content expectations; the matrix surfaces them as a distinct row.
