# Examples and troubleshooting

One section per worked example, then troubleshooting. Read only what you need.

## binding-authority-mga-renewal

### Example: binding-authority MGA renewal across 12 states

#### Input

A mid-size US property-and-casualty carrier is renewing a binding-authority managing general agent (MGA) writing commercial-auto on the carrier's paper across 12 states. Premium volume material to the line of business. The MGA is non-affiliate. The MGA recently rolled out a third-party AI rating tool that was not covered in the original delegation contract. The renewal sits with second-line; the carrier's state DOI in three of the states has tightened expectations on commissioner-access language since the contract was first written.

#### Output sketch

The pack opens with the arrangement summary: counterparty type MGA, functions delegated underwriting and binding, states-of-operation list, line of business commercial-auto. Holding-company status is non-affiliate; Form D is not triggered, and the pack records the negative answer with a citation to the model regulation rather than leaving the field empty.

Producer-licensing review surfaces the per-state confirmation set; in two of the 12 states the per-individual-producer status for one named-producer role has lapsed without re-appointment. That goes in `gaps` with severity high and an owner.

Contractual control review reads the audit-rights, books-and-records, sub-delegation, and termination clauses against insurance outsourcing expectations. The books-and-records clause does not flow commissioner access through to the MGA in three of the 12 states; that is the contract gap that drives the renewal condition.

The Insurance Data Security Model Law §4.F third-party-service-provider review confirms a written contract is in place and references the §4.F clause set. Sub-processor visibility is partial; the MGA's data-aggregator sub-processor for vehicle-history data is named, but downstream sub-processors are not. Incident-response cooperation language is present; the breach-notification clock from the MGA to the carrier sits at a length that does not preserve the carrier's downstream regulator-notification windows in two states. Both findings go in `data_security_findings`.

Claims-handling oversight is not in scope (this MGA does not handle claims); the section reads "not applicable" with a note rather than being omitted.

Vendor-AI exposure is the standout finding. The MGA's AI rating tool was rolled out without amendment to the delegation contract and without notice to the cedent. The pack ties that back to the NAIC AI Bulletin December 2023 expectation that the carrier remains accountable for vendor and third-party AI used on its policies, names the AIS Program elements not evidenced (governance, third-party-AI accountability, monitoring, transparency), and routes the deeper evidence-pack review to the AI governance function via cross-link.

ORSA fit is yes; this MGA is enterprise-material to the commercial-auto line and belongs in the ORSA Summary Report under Model #505. The pack records `orsa_inclusion = true` and notes the carrier should confirm the function is reflected in the next ORSA cycle.

Recommended disposition: approve-with-conditions. Conditions: (1) contract amendment to flow commissioner access to the MGA in the three named states by the next renewal cycle; (2) per-individual-producer re-appointment in the two named states within 30 days; (3) AI delegation amendment with the AIS Program governance evidence ask listed; (4) sub-processor list completed below the data-aggregator. The pack stops at the recommendation. The TPRM committee or the AI risk committee, depending on which is the named approver in the firm-overlay, signs off.

#### Why this scenario matters

It exercises the full spine: holding-company status as a negative answer carried explicitly, per-state per-individual producer licensing rather than entity-only, contract-control gaps tied to commissioner access (the insurance-specific clause that federal banking guidance does not name), §4.F sub-processor and breach-notification findings, and the vendor-AI exposure that bank-flavoured vendor-diligence does not surface. Public-source-derived; no named institutions.

## life-tpa-claims-administration

### Example: life carrier renewing a TPA for closed-block claims administration

#### Input

A US life carrier is renewing a third-party administrator (TPA) handling claims administration on a closed block of life policies. The TPA processes protected health information in the course of claims adjudication. The TPA is non-affiliate. The TPA recently changed its sub-processor for OCR of claims documents without notice to the carrier. The renewal sits with second-line; the carrier operates in states that have adopted the NAIC Insurance Data Security Model Law and the renewal also needs to read against the carrier's HIPAA business-associate posture.

#### Output sketch

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

#### Why this scenario matters

It exercises the §4.F sub-processor and breach-notification chain on a real PHI flow, the HIPAA BAA cross-overlay, the Model #900 fair-claims-settlement read on the delegated function, and the negative-answer disciplines (Form D not triggered, producer-licensing not applicable, vendor-AI not present, premium-handling not applicable) that keep the artifact honest about what was reviewed and what was not. Public-source-derived; no named institutions.

## troubleshooting

### Troubleshooting: insurance-outsourcing-review

Recurring defects in outsourcing-review packs and how to read past them.

#### The pack reads like a vendor-diligence pack

A market-conduct examiner will not accept a vendor-diligence pack as evidence of outsourcing oversight. The audience and the statutory frame are different. If the draft talks about SOC 2, hyperscaler concentration, and BCDR test reports without naming Form D, §4.F, Model #900 (and the relevant state UCSPA), or per-state producer licensing, the wrong skill ran. Restart from the spec; the bank-flavoured `vendor-diligence` does not produce a state-DOI-grade artifact.

#### Form D filing trigger missed on an affiliate transaction

The substance of the contract may be fine and still fail an exam because the procedural Form D filing under the holding-company model regulation did not happen. Whenever the counterparty is in the carrier's holding company group, the affiliate-status field forces a Form D applicability check and the pack carries the answer with a citation, not a silent omission.

#### Producer licensing confirmed at the entity, not the individual

The exam reviews per-state per-individual-producer status where binding or producer authority is exercised. Confirming that the MGA holds a corporate licence is not enough. The pack must list the per-state per-individual producer-licensing posture or flag it as an open gap with an owner and a date.

#### §4.F treated as the federal third-party guidance with insurance stickers

The Insurance Data Security Model Law third-party clauses are insurance-specific. Commissioner access, cedent breach-notification chain, and sub-processor visibility are written for an insurance examiner, not a federal banking examiner. Reading §4.F through interagency-guidance vocabulary loses the insurance content. Cite the model law text directly and mark unconfirmed subsections `[verify section]` rather than paraphrasing into bank language.

#### Vendor AI exposure quietly dropped

The MGA or TPA has often rolled out an AI rating tool, an FNOL chatbot, or a claims-severity model without telling the cedent. The NAIC AI Bulletin holds the carrier accountable. The pack must surface vendor-AI exposure as an explicit named line, not as a footnote. Where the answer is unknown, that is a finding.

#### Claims-handling controls assessed against fairness rather than fair-claims-settlement

Fairness vocabulary belongs in AI governance. Insurance claims oversight runs on the NAIC Unfair Claims Settlement Practices Act (Model #900) and the state's unfair-claims-settlement-practices act: timing, notice, documentation, reasoned denial. The pack tests the delegated function against the insurance standard, not against generic AI fairness. Where both vocabularies apply (claims AI), the artifact carries both reads and translates between them.

#### ORSA-fit answered with a guess

Whether the outsourced function belongs in the ORSA Summary Report depends on the carrier's materiality threshold. If that threshold is not in evidence, the pack flags ORSA-fit as `[evidence needed]` and routes the question to the ERM lead rather than answering it from feel.

#### TPA premium-handling not separated from claims-handling

A TPA that collects or holds premium sits on a fiduciary-account posture (state TPA acts and producer-licensing rules) that is distinct from claims-handling oversight under Model #900 and the state UCSPAs. Folding both into one section loses the fiduciary-account question. Keep them as two named sections in the pack.

#### Sub-processor changes treated as a notification rather than a control

Many TPA contracts permit sub-processor changes with notice. Under §4.F the carrier is on the hook for the sub-processor's practices. Notice without a consent gate or a rapid-objection window is a contract gap; the pack carries that finding even when the TPA argues the clause is market-standard.

#### Disposition over-stretched

`Approve` on an arrangement with a known §4.F sub-processor gap or a missing per-state producer-licensing confirmation reads as an unconditional sign-off on an exam-visible defect. `Approve-with-conditions`, with the conditions specific and verifiable, is the correct posture. The skill stops at the recommended disposition; the named sign-off owner decides.
