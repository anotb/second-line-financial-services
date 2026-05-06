# Banking sector overlay — rule-to-obligation-extraction

Load this overlay when the rule under extraction is issued by OCC, FRB, FDIC, NCUA, or by the federal banking agencies jointly (FFIEC inter-agency statements). The overlay carries banking-rule citation conventions and recurrent extraction patterns for OCC bulletins, FRB SR letters, FDIC FILs, NCUA letters to credit unions, and FFIEC inter-agency statements. The base SKILL.md row spine does not change; this overlay tells the practitioner which sources are permitted citations and which extraction patterns recur for banking rules.

## Banking-rule citation conventions

- **12 CFR** is split across the three federal banking agencies. OCC rules generally land in Parts 1 to 199 (OCC under Title 12 Chapter I); FRB rules in Parts 200 to 299 (FRB under Title 12 Chapter II); FDIC rules in Parts 300 to 399 (FDIC under Title 12 Chapter III). NCUA rules land in Parts 700 to 799 (NCUA under Title 12 Chapter VII). CFPB rules transfer-of-authority rules land in 12 CFR Chapter X (Parts 1001 onward).
- The 36-hour bank notification rule was adopted in parallel by all three agencies: 12 CFR Part 53 (OCC); 12 CFR Part 225 Subpart N (FRB Regulation Y); 12 CFR Part 304 Subpart C (FDIC). When extracting from the parallel rule, the obligation rows are agency-specific by codified Part; the substantive obligation is the same shape across the three agencies.
- OCC Bulletins, FRB SR letters, FDIC FILs, and NCUA Letters to Credit Unions are interpretive supervisory instruments rather than rules in the CFR sense. The pin is the section inside the instrument (e.g., `OCC Bulletin 2013-29 §III.A`; `SR 11-7 §IV.A`). Operative-text-vs-preamble distinction does not apply the same way as it does for Federal Register rules; the entire bulletin text is interpretive, and the section structure inside the bulletin is the spine for extraction.

## Recurrent extraction patterns — federal banking supervisory letters

The supervisory-letter genre carries recurrent obligation patterns that the extraction should expect:

- **Program-and-process pattern**. The letter identifies a programme (third-party-risk management; model risk management; operational resilience; cybersecurity; BSA/AML; capital planning) and decomposes into governance (board oversight; senior management oversight; written programme approval; periodic review), risk-assessment, life-cycle controls (onboarding/development; ongoing monitoring; offboarding/decommissioning), independent testing or validation, and reporting to the board or board committee. Each named life-cycle stage is a row.
- **Tier-by-tier scope pattern**. The letter scales expectations by institution size, complexity, or risk. The obligation is the same shape across tiers but the implementation depth differs. Capture each tier as its own scope-trigger row when the letter is explicit; capture the tier-language verbatim where it is not.
- **Examples-as-expectation pattern**. Bulletins and SR letters frequently embed examples as `For example, the institution should consider ...`. The example is interpretive, not binding; the binding obligation sits in the surrounding text. Resist extracting examples as obligations.

## OCC Bulletin 2013-29 (rescinded) and the June 2023 Interagency Guidance — worked pattern

OCC Bulletin 2013-29 was the OCC's third-party-risk-management guidance from October 2013 to June 2023. It was rescinded on issuance of the **Interagency Guidance on Third-Party Relationships: Risk Management** (88 FR 37920, June 9 2023), issued jointly by FRB, FDIC, and OCC. The interagency guidance is the operative supervisory expectation for third-party-risk obligations across federally regulated banking organizations.

The interagency guidance decomposes into the third-party-risk life-cycle (planning; due diligence and third-party selection; contract negotiation; ongoing monitoring; termination) plus governance and oversight. Each life-cycle stage carries discrete obligations on the banking organisation: documentation expectations (risk assessment of the third-party relationship; due-diligence record), contract-clause expectations (right-to-audit, subcontracting controls, business-continuity, incident-notification, termination triggers), monitoring expectations (performance-monitoring, control-testing, financial-condition tracking), and termination expectations (data-return-or-destruction, exit transition). Each is a row in the extraction.

## SR 11-7 / OCC Bulletin 2011-12 — model risk management worked pattern

The joint guidance text appended to SR 11-7 (April 4 2011) and OCC Bulletin 2011-12 is the operative supervisory expectation for model risk management. The guidance decomposes into governance (§V), model development (§III), model validation (§IV including effective-challenge expectations), reliance on vendors and third parties (§VI), and the model inventory (§V). Each section carries discrete obligations on the institution. Recent updates: extraction should track agency-issued updates to model-risk guidance (OCC Bulletin 2026-13 if applicable [verify bulletin number and current title]); when extracting an update, also extract the change relative to the prior bulletin.

## The 36-hour bank notification rule — worked pattern

12 CFR Part 53 (OCC); 12 CFR Part 225 Subpart N (FRB); 12 CFR Part 304 Subpart C (FDIC), 86 FR 66424 (November 23 2021), compliance date May 1 2022. Extraction pattern:

- **Defined terms** (each captured in the defined-terms section, with the rule's text of definition and the section pin): "computer-security incident"; "notification incident"; "banking organisation"; "bank service provider".
- **Trigger** (condition_or_trigger column): the banking organisation's determination that a notification incident has occurred.
- **Deadline** (deadline column): "as soon as possible and no later than 36 hours after the banking organisation determines that a notification incident has occurred."
- **Action** (action_type: notice_or_disclosure): notification to the primary federal regulator.
- **Evidence shape** (evidence_expected): incident-determination record; notification log; regulator-acknowledgement record.
- **Bank-service-provider obligation**: separate row. The bank service provider must notify each affected banking-organisation customer "as soon as possible" when the BSP determines a covered incident has occurred or is reasonably likely to occur. This is a third-party-side obligation that flows into the bank's third-party-risk register downstream.

## BSA/AML rule structure

BSA/AML rules sit in 31 CFR Chapter X (Parts 1010 to 1029, FinCEN regulations) and in the relevant agency's BSA/AML rule (12 CFR 21 OCC; 12 CFR 208 and 12 CFR 211 FRB; 12 CFR 326 FDIC; 12 CFR 748 NCUA). The FFIEC BSA/AML Examination Manual is interpretive and is the inter-agency framework for examiner expectations; pin to the manual chapter when extracting from the manual, and to the underlying 31 CFR or 12 CFR section when extracting from the rule itself.

The Anti-Money Laundering Act of 2020 amendments to the BSA introduced: beneficial-ownership reporting under 31 CFR 1010.380 (FinCEN BOI rule); national priorities for AML/CFT under 31 USC 5318(h)(4)(A); modernisation of SAR/CTR processes. Each amendment carries its own implementation-rule schedule; capture extraction-time effective dates as the rule provides them.

## When to escalate to a sector-skill chain

The base SKILL.md is the right tool when the extraction is from a banking rule and the next step is `obligation-mapping`. When the extraction is the upstream artifact for a full-scope OCC, FRB, or FDIC examination readiness sprint at a bank carrying the Heightened Standards (12 CFR Part 30 Appendix D), the downstream sector-readiness skill is `sector-plugins/banking-risk-compliance/banking-supervision-readiness`; the extraction register feeds that readiness sprint. The base skill does not produce the readiness pack; it produces the obligation list the readiness pack reads.
