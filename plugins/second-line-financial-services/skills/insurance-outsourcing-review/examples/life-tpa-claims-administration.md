# Example: life carrier renewing a TPA for closed-block claims administration

## Input

A US life carrier is renewing a third-party administrator (TPA) handling claims administration on a closed block of life policies. The TPA processes protected health information in the course of claims adjudication. The TPA is non-affiliate. The TPA recently changed its sub-processor for OCR of claims documents without notice to the carrier. The renewal sits with second-line; the carrier operates in states that have adopted the NAIC Insurance Data Security Model Law and the renewal also needs to read against the carrier's HIPAA business-associate posture.

## Output sketch

The arrangement summary names counterparty type TPA, functions delegated claims and data processing, states-of-operation list, lines of business closed-block life, claims volume material. Holding-company status non-affiliate; Form D not triggered.

Producer-licensing review notes that the TPA does not exercise binding or producer authority; the section reads "not applicable" with a note rather than being omitted.

Contractual control review reads the audit-rights, books-and-records, sub-delegation, and termination clauses. Sub-delegation is the load-bearing finding: the contract permits sub-processor changes with notice to the carrier, the TPA changed its OCR sub-processor without giving notice, and the carrier discovered the change months after the fact. That is a contract-control finding (sub-delegation) and a §4.F finding (sub-processor visibility).

The Insurance Data Security Model Law §4.F third-party-service-provider review carries the bulk of the pack. Due diligence on the new OCR sub-processor was not performed before the change; the §4.F written-contract terms are not flowed through to the sub-processor; the breach-notification chain from the OCR sub-processor up to the cedent is broken in places. Each finding cites the §4.F clause set with `[verify section]` where the exact subsection is not confirmed.

HIPAA cross-overlay loads because PHI flows. The business-associate agreement (BAA) is in place between the carrier and the TPA but a corresponding subcontractor BAA was not executed before the OCR sub-processor change. Breach-notification clock posture is read against the HIPAA 60-day clock and the §4.F clock; both findings go in `data_security_findings` with a privacy-overlay tag.

Claims-handling oversight runs against the NAIC Unfair Claims Settlement Practices Act (Model #900) and the relevant state unfair-claims-settlement-practices acts. A sample of the TPA's denial letters shows reasoned-denial language is generally consistent with state requirements; one state's required appeal-rights notice is missing in two of the sampled letters. That goes in `claims_handling_findings` with severity medium and an owner.

Premium-handling and fiduciary-account posture is not applicable (closed-block claims-only); the section reads "not applicable" with a note.

Vendor-AI exposure: the TPA confirms it has not deployed AI in the claims-handling path. The pack records the negative answer with a citation rather than leaving the section silent and notes that the next-review trigger includes any change in the AI-use posture.

ORSA fit is yes; the closed block is enterprise-material to the carrier and the TPA function belongs in the ORSA Summary Report. The pack records `orsa_inclusion = true`.

Recommended disposition: remediate-then-re-review. The §4.F sub-processor and HIPAA-BAA gaps are too material for approve-with-conditions on this cycle. Open items name the TPA-side actions (subcontractor BAA, sub-processor due-diligence file, breach-notification chain document) and the carrier-side actions (notify the privacy office, assess whether a regulator notification is required for the OCR sub-processor change). The pack stops at the recommendation; the named sign-off owner closes the disposition.

## Why this scenario matters

It exercises the §4.F sub-processor and breach-notification chain on a real PHI flow, the HIPAA BAA cross-overlay, the Model #900 fair-claims-settlement read on the delegated function, and the negative-answer disciplines (Form D not triggered, producer-licensing not applicable, vendor-AI not present, premium-handling not applicable) that keep the artifact honest about what was reviewed and what was not. Public-source-derived; no named institutions.
