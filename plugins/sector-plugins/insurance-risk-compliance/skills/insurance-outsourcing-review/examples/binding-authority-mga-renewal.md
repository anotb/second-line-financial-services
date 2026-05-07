# Example — binding-authority MGA renewal across 12 states

## Input

A mid-size US property-and-casualty carrier is renewing a binding-authority managing general agent (MGA) writing commercial-auto on the carrier's paper across 12 states. Premium volume material to the line of business. The MGA is non-affiliate. The MGA recently rolled out a third-party AI rating tool that was not covered in the original delegation contract. The renewal sits with second-line; the carrier's state DOI in three of the states has tightened expectations on commissioner-access language since the contract was first written.

## Output sketch

The pack opens with the arrangement summary: counterparty type MGA, functions delegated underwriting and binding, states-of-operation list, line of business commercial-auto. Holding-company status is non-affiliate; Form D is not triggered, and the pack records the negative answer with a citation to the model regulation rather than leaving the field empty.

Producer-licensing review surfaces the per-state confirmation set; in two of the 12 states the per-individual-producer status for one named-producer role has lapsed without re-appointment. That goes in `gaps` with severity high and an owner.

Contractual control review reads the audit-rights, books-and-records, sub-delegation, and termination clauses against insurance outsourcing expectations. The books-and-records clause does not flow commissioner access through to the MGA in three of the 12 states; that is the contract gap that drives the renewal condition.

The Insurance Data Security Model Law §4.F third-party-service-provider review confirms a written contract is in place and references the §4.F clause set. Sub-processor visibility is partial; the MGA's data-aggregator sub-processor for vehicle-history data is named, but downstream sub-processors are not. Incident-response cooperation language is present; the breach-notification clock from the MGA to the carrier sits at a length that does not preserve the carrier's downstream regulator-notification windows in two states. Both findings go in `data_security_findings`.

Claims-handling oversight is not in scope (this MGA does not handle claims); the section reads "not applicable" with a note rather than being omitted.

Vendor-AI exposure is the standout finding. The MGA's AI rating tool was rolled out without amendment to the delegation contract and without notice to the cedent. The pack ties that back to the NAIC AI Bulletin December 2023 expectation that the carrier remains accountable for vendor and third-party AI used on its policies, names the AIS Program elements not evidenced (governance, third-party-AI accountability, monitoring, transparency), and routes the deeper evidence-pack review to the AI governance function via cross-link.

ORSA fit is yes; this MGA is enterprise-material to the commercial-auto line and belongs in the ORSA Summary Report under Model #505. The pack records `orsa_inclusion = true` and notes the carrier should confirm the function is reflected in the next ORSA cycle.

Recommended disposition: approve-with-conditions. Conditions: (1) contract amendment to flow commissioner access to the MGA in the three named states by the next renewal cycle; (2) per-individual-producer re-appointment in the two named states within 30 days; (3) AI delegation amendment with the AIS Program governance evidence ask listed; (4) sub-processor list completed below the data-aggregator. The pack stops at the recommendation. The TPRM committee or the AI risk committee, depending on which is the named approver in the firm-overlay, signs off.

## Why this scenario matters

It exercises the full spine: holding-company status as a negative answer carried explicitly, per-state per-individual producer licensing rather than entity-only, contract-control gaps tied to commissioner access (the insurance-specific clause that federal banking guidance does not name), §4.F sub-processor and breach-notification findings, and the vendor-AI exposure that bank-flavoured vendor-diligence does not surface. Public-source-derived; no named institutions.
