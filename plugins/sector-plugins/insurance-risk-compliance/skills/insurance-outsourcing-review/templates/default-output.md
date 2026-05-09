# Insurance outsourcing review

**Counterparty**: [legal entity; brand name if different]
**Counterparty type**: [MGA | MGU | TPA | claims-administrator | underwriting-bureau | IT-outsourcer | actuarial-outsourcer | other]
**Arrangement ID**: [stable ID; reused across renewals and exam responses]
**Engagement ID**: [pointer to engagement-scope record, or "none — scope not formalised"]
**As of**: [date]
**Review type**: [pre-onboarding | renewal | mid-term | remediation | exam-response]
**Owner (role)**: [e.g., outsourcing risk lead, second-line]
**Approver (role)**: [per firm policy for this counterparty type and ORSA materiality]
**Confidence label**: [high | medium | low | unknown]

## 1. Arrangement summary

- Functions delegated: [underwriting | binding | rating | claims | premium-handling | data-processing | actuarial | IT | other].
- States of operation: [list].
- Lines of business: [list].
- Premium volume: [annual; basis].
- Claims volume: [annual; basis].
- Inherent-risk read: [one paragraph; carrier exposure if the function fails or misperforms].

## 2. Holding-company status and Form D posture

- Affiliate status: [affiliate | non-affiliate].
- Ultimate controlling person (where affiliate): [entity].
- Form B reference (where affiliate): [filing identifier and date].
- Form D applicability: [triggered | not-triggered | under-review]. Cite Insurance Holding Company System Model Regulation by section in `references/source-anchors.md`; mark `[verify section]` where the exact subsection is not confirmed.

> Carry the negative answer explicitly. A non-affiliate posture with the citation in place is itself the evidence the exam looks for.

## 3. Producer-licensing and binding-authority posture

- Authority delegated: [binding | quoting | issuance | premium-collection | claims-pay | none].
- Per-state per-individual producer-licensing status: [confirmed | partial | gaps | not-applicable].
- Appointment status by state: [confirmed | partial | gaps | not-applicable].
- Open licensing items: [bulleted; each names state, individual or entity, target close date].

> Where authority is not delegated, mark "not applicable" with a note. Do not omit the section.

## 4. Contract-control review against NAIC outsourcing expectations

| Clause family | Expectation | Present? | Note |
|---|---|---|---|
| Audit rights and books-and-records access by the carrier | | | |
| Commissioner / state-DOI examination access flow-through | | | |
| Sub-delegation restrictions and consent | | | |
| Indemnification | | | |
| Termination and transition assistance | | | |
| Performance-standards and SLA reporting | | | |

Cite the operative model law(s) in `references/source-anchors.md`; mark `[verify section]` where the exact subsection is not confirmed.

## 5. Insurance Data Security Model Law §4.F third-party-service-provider review

- Due-diligence file before contract: [present | partial | missing].
- Written-contract clauses required by §4.F: [present | partial | missing] — itemise gaps.
- Ongoing monitoring posture: [evidenced | partial | missing].
- Incident-response cooperation language: [present | partial | missing].
- Breach-notification chain (counterparty → carrier → carrier's regulators): [intact | partial | broken] — note the time-to-notify against the carrier's downstream regulator clocks.
- Sub-processor visibility: [full | partial | none] — list known sub-processors and the change-notice mechanism.
- State-by-state §4.F adoption status in operating footprint: [list with citation to NAIC adoption tracker].

## 6. Claims-handling oversight (where claims function is delegated)

- Fair-claims-settlement standards (NAIC Model #900 and state UCSPA; Model #880 where the state UTPA reaches claims-handling conduct) coverage: [evidenced | partial | missing].
- Acknowledgement, investigation, and decision timing: [meets standard | drift evidenced | not-evidenced].
- Reasoned-denial drafting and named human-review checkpoint: [evidenced | partial | missing].
- Complaint flow from policyholder through TPA to carrier: [evidenced | partial | missing].
- Denial-letter sample review: [scope, sample size, findings].

> Where the claims function is not delegated, mark "not applicable" with a note. Do not omit.

## 7. Premium-handling and fiduciary-account posture (where premium is collected or held)

- Fiduciary-account structure: [evidenced | partial | missing].
- Segregation from operating funds: [evidenced | partial | missing].
- Reconciliation cadence and exception register: [evidenced | partial | missing].
- State TPA-act fiduciary requirements applied: [confirmed | partial | gaps | not-applicable].

## 8. Vendor-AI exposure

- AI tools deployed by the counterparty on the carrier's policies: [list, including underwriting AI, rating ML, claims-AI, FNOL chatbot, severity prediction, fraud-indicator routing, agent-AI co-pilot, OCR / document-AI, marketing-AI to policyholders].
- Carrier notice and contractual coverage of each tool: [in-contract | side-letter | not-covered | unknown].
- AIS Program elements evidenced (governance, risk management, testing, validation, third-party-AI accountability, monitoring, documentation, transparency, fairness): [list with status].
- Cross-link to AI evidence-pack review: [linked record ID, or "not chained"].
- Where the counterparty confirms no AI deployment, record the negative answer with a citation; the next-review trigger includes any change in AI-use posture.

## 9. ORSA fit

- Function materiality assessed against the carrier's ORSA materiality threshold: [yes | no | unknown].
- ORSA Summary Report inclusion: [included | recommended | not-recommended | not-applicable].
- Cross-link to the ORSA cycle and the ERM lead.

## 10. Gaps, issues, and recommended disposition

- Gaps: [each gap names the citation, severity, owner, and target close date].
- Issues elevated to the risk register or to internal audit: [list].
- Recommended disposition: [approve | approve-with-conditions | remediate-then-re-review | decline].
- Conditions (where approve-with-conditions): [bulleted, specific, verifiable].
- Decline rationale or remediation runway (where remediate or decline): [bulleted].

> The skill stops at the recommendation. The named sign-off owner — TPRM committee, ERM lead, AI risk committee for vendor-AI exposure, depending on firm-overlay — closes the disposition.

## 11. Open items and next-review triggers

- Open items: [each names description, owner, target date].
- Next-review trigger: [renewal cycle date; sub-processor change; AI-use change; ORSA-cycle anchor; incident-driven re-review condition; state-DOI bulletin update in operating footprint].

## 12. Source trace

| Claim | Source | Section | Date | URL or file ref |
|---|---|---|---|---|
| | | | | |

Cite `references/source-anchors.md` for canonical citations. Use `[verify section]` if the section reference is unknown; do not invent.

---

*Pack depth scales to counterparty type and ORSA materiality.* A non-material IT outsourcer with no PHI and no producer authority collapses the producer-licensing and claims-handling sections to "not applicable" with a note. A binding-authority MGA in a multi-state footprint with vendor-AI exposure runs full depth.

*Audience shapes the pack.* A TPRM-forum read is short and operational. A risk-committee read for an enterprise-material outsourced function is longer with reviewer questions clustered for the forum. An exam-response file is formal, with citations cleaned and `[verify section]` flags resolved.
