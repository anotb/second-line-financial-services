# Insurance sector overlay — insurance-outsourcing-review

This skill is insurance-only by design; the overlay carries the insurance frame the body of SKILL.md walks generically. Load this overlay alongside `references/source-anchors.md` whenever the skill runs.

## Counterparty-type-by-applicable-Model crosswalk

| Counterparty type | Holding Company Act / Reg (#440 / #450) | Insurance Data Security Model (#668 §4.F) | Unfair Trade Practices (#880) | Producer Licensing Model Act | ORSA (#505) |
|---|---|---|---|---|---|
| Managing General Agent (MGA) | applies if affiliate (Form D) | applies | applies if claims-touching | applies (binding / quoting) | apply materiality |
| Managing General Underwriter (MGU) | applies if affiliate (Form D) | applies | applies if claims-touching | applies | apply materiality |
| Third-Party Administrator (TPA) | applies if affiliate (Form D) | applies | applies (claims-handling) | applies if premium-collecting or producer-acting | apply materiality |
| Claims administrator | applies if affiliate (Form D) | applies | applies (Model #900 plus state UCSPAs) | usually n/a | apply materiality |
| Underwriting bureau | applies if affiliate (Form D) | applies | n/a | n/a | apply materiality |
| IT outsourcer | applies if affiliate (Form D) | applies (cyber chain) | n/a | n/a | apply materiality |
| Actuarial outsourcer | applies if affiliate (Form D) | applies (data) | n/a | n/a | apply materiality |

## Holding-company status — Form B / Form D

The Form D filing is the procedural mechanism. Where the counterparty is an affiliate of the carrier under the holding-company definition, an outsourcing arrangement crossing the materiality threshold under the Holding Company Model Regulation triggers a Form D filing. The exam picks up the procedural absence even when the substance of the contract is sound. Carry the Form D answer in the pack as a named line. Cite Model #450 by section in `references/source-anchors.md`; mark `[verify section]` where the exact subsection is not confirmed.

## §4.F third-party-service-provider obligations

The §4.F clause set on the Insurance Data Security Model Law is insurance-specific and reads on its own terms, not on federal banking interagency-guidance terms. The diligence-before-contract obligation, the written-contract requirement, the ongoing monitoring obligation, the incident-response cooperation obligation, and the breach-notification chain to the cedent insurer each require a finding in the pack. Where the carrier's operating footprint includes states that have not adopted Model #668, NYDFS 23 NYCRR Part 500.11 may be the operative third-party-cyber frame instead; consult the cross-cutting cyber overlay for the §500.11 read.

## Producer licensing per state per individual

The exam reviews per-state per-individual-producer status where binding, quoting, issuance, premium-collection, or producer authority is exercised. Confirming the counterparty entity holds a corporate licence is not enough. The pack lists the per-state per-individual licensing posture or flags it as an open gap with an owner. Appointment status by state runs alongside licensing — a licensed producer who is not appointed by the carrier in a state where they are exercising authority is a finding.

## Claims-handling under Model #900 plus state UCSPAs follows the function

UDAP and unfair-claims-settlement-practices exposure under the NAIC Unfair Claims Settlement Practices Act (Model #900) and the relevant state unfair-claims-settlement-practices acts attach to the carrier of record regardless of who executes the claim decision. The TPA's letters are the carrier's letters for that purpose. The pack reads denial-letter samples against the standard, surfaces drift in acknowledgement and decision timing, and confirms the complaint flow from policyholder through TPA back to the carrier. State UCSPAs add state-specific timing, notice, and reasoned-denial expectations on top of the model; cite by state when used. Where a state's unfair-trade-practices act (often the analogue to NAIC Model #880) reaches claims-handling conduct, name it alongside the UCSPA cite.

## Premium-handling and fiduciary-account posture

Where the TPA collects or holds premium, the state TPA Act fiduciary-account requirements apply (segregation from operating funds, reconciliation cadence, fidelity bond, signatory controls). This is distinct from claims-handling oversight; do not fold the two sections together.

## Vendor-AI exposure under the NAIC AI Bulletin

The NAIC Bulletin December 2023 holds the carrier accountable for vendor and third-party AI used on its policies. The pack must surface vendor-AI as an explicit named line, even where the answer is "the counterparty has not deployed AI", in which case the negative answer is recorded with a citation and the next-review trigger includes any change in AI-use posture. AIS Program elements (governance, risk management, testing, validation, third-party-AI accountability, monitoring, documentation, transparency, fairness) are the framework the carrier owes against the counterparty's AI. Adoption is state-by-state; cite the NAIC AI Working Group adoption tracker for the operating-footprint read.

Where the question becomes "is the counterparty's published evidence pack on its AI sufficient for our deployment context", chain to `ai-governance-model-risk/llm-vendor-evidence-review` and record the linked record ID. Do not duplicate model-risk evidence-review analysis in this pack.

## ORSA fit

Whether the outsourced function belongs in the ORSA Summary Report depends on the carrier's own materiality threshold under Model #505. The pack consumes the carrier's threshold and applies it. Where the threshold is not in evidence, the pack flags ORSA-fit as `[evidence needed]` and routes the question to the ERM lead. ORSA-material outsourced functions also typically warrant elevation in the next risk-committee pack; cross-link to `risk-reporting/risk-committee-pack` insurance overlay where relevant.

## Cross-link inside the plugin and to capability skills

- `third-party-operational-resilience/vendor-diligence` — when the counterparty is a generic IT or data vendor with no delegated underwriting, claims, premium-handling, or policyholder-data role, route there with the insurance overlay loaded; do not run this skill.
- `risk-reporting/cyber-disclosure-readiness` — when the work is a cyber-incident response at the counterparty, route there with the insurance overlay loaded; this skill produces an outsourcing-oversight artifact, not an incident-response artifact.
- `ai-governance-model-risk/llm-vendor-evidence-review` — for the deeper AI-evidence-pack read once the vendor-AI line in this pack identifies a deployed AI system.

## Common pitfalls captured in `TROUBLESHOOTING.md`

Vendor-diligence framing creep, missed Form D on affiliate transactions, entity-only producer licensing, §4.F translated into federal banking vocabulary, vendor-AI dropped, fairness vocabulary substituted for fair-claims-settlement, ORSA-fit answered from feel, premium-handling folded into claims, sub-processor change treated as notification rather than control, disposition over-stretched.
