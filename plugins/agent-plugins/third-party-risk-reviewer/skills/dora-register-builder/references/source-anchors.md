# Source anchors — dora-register-builder

The named, dated regulatory sources this skill anchors to. SKILL.md cites this file by path and does not restate excerpts. Sector-specific and cross-cutting anchors live in the corresponding overlay files.

## Primary frame — DORA Register of Information

- **Regulation (EU) 2022/2554 (DORA), Articles 28 to 30**. Article 28 sets the general principles for ICT third-party risk and is the source of the register obligation; **Article 28(3)** requires every financial entity to maintain a register of information for all contractual arrangements on the use of ICT services provided by ICT third-party service providers, distinguishing arrangements supporting critical or important functions from the rest [verify subarticle]. **Article 28(7)** governs annual reporting to the competent authority on the number of new arrangements, the categories of ICT third-party providers, the type of contractual arrangements, and the ICT services and functions provided [verify subarticle]. **Article 28(8)** addresses the prior-information obligation when entering into a new arrangement supporting a critical or important function [verify subarticle]. **Article 29** covers the preliminary assessment of ICT concentration risk and the related register-driven analysis. **Article 30** sets the key contractual provisions that the register must reflect (rights of access, audit, sub-outsourcing chain, exit, service-level descriptions) [verify subarticle structure of 30(2) and 30(3)]. Source: https://eur-lex.europa.eu/eli/reg/2022/2554/oj .

- **Article 6, DORA — ICT risk management framework**. The register sits inside the ICT risk management framework; the register output feeds the framework's third-party-risk view and the firm's policy on the use of ICT services supporting critical or important functions (Article 28(2)) [verify subarticle].

## ITS Register of Information schema

- **Commission Implementing Regulation (EU) 2024/2956 of 29 November 2024 laying down implementing technical standards for the application of Article 28(9) of Regulation (EU) 2022/2554 of the European Parliament and of the Council with regard to the standard templates for the register of information** [verify exact Commission Implementing Regulation number, OJ reference, and adoption date against the published Official Journal text]. The ITS sets the standard templates (the B-tables and accompanying R-, RT-, and relational tables) the register must follow, and the technical instructions for completion. The schema includes contractual-arrangement tables, ICT-third-party-service-provider tables, ICT-service tables, function tables, sub-contractor-chain tables, and identification-code tables; the joint ESA preparation materials and the EBA preparation page are the public anchors for the schema as adopted. EBA preparation page: https://www.eba.europa.eu/activities/direct-supervision-and-oversight/digital-operational-resilience-act/preparation-dora-application . OJ entry point: https://eur-lex.europa.eu/ [verify exact OJ URL].

- **Joint Final Report on the draft ITS on the register of information** (ESAs, 17 January 2024) [verify exact title and date]. The draft ITS submitted by the EBA, EIOPA, and ESMA to the European Commission; useful as the explanatory record for the schema decisions and for the ICT-service-type taxonomy in Annex III of the ITS [verify Annex reference].

- **Joint Guidelines on the contents and procedures for the management of the register of information** (ESAs, where issued) [verify exact title, joint-guideline number, and date]. Where the ESAs have issued joint guidelines accompanying the ITS, they sit alongside the ITS as the operational reading.

- **Joint Decision on data collection for the designation of CTPPs** [verify exact title and date], where applicable, sets the supervisory data-collection cycle that consumes register data for the CTPP designation process under Article 31.

## Sub-outsourcing RTS

- **Commission Delegated Regulation laying down regulatory technical standards specifying the elements which a financial entity has to determine and assess when sub-contracting ICT services supporting critical or important functions** (RTS on sub-contracting under DORA Article 30(5)) [verify exact Commission Delegated Regulation number, OJ reference, and adoption date]. The RTS sets the elements the financial entity must assess before allowing sub-contracting in the chain supporting a critical or important function. The register's sub-contractor-chain table (`b_06_sub_contractors_chain` in the schema mapping) is the structured artifact the RTS reads back into. EBA draft RTS reference: https://www.eba.europa.eu/regulation-and-policy/operational-resilience/regulatory-technical-standards-subcontracting-ict-services [verify URL].

## EBA outsourcing register (predecessor and parallel artifact)

- **EBA Guidelines on outsourcing arrangements (EBA/GL/2019/02), §11 outsourcing register** [verify section number]. Pre-DORA outsourcing-register obligation for EU credit institutions, investment firms, payment institutions, and e-money institutions. The schema is flatter and narrower than the DORA Register of Information; the natural input to the DORA register is the existing outsourcing register plus the broader ICT-third-party arrangements that fall outside the EBA outsourcing definition. Mapping is required, not copy-paste. https://www.eba.europa.eu/regulation-and-policy/internal-governance/guidelines-on-outsourcing-arrangements .

## Competent-authority technical instructions (vary by jurisdiction)

- **ECB SSM technical reporting instructions for register submission** [verify exact instruction reference, channel, and validation-rule package]. Operative for ECB direct-supervised significant institutions. The SSM channel is the submission route; NCAs still play a role for less-significant institutions and for non-banking subsidiaries within the SSM perimeter.
- **EBA-coordinated approach for less-significant institutions and for payment / e-money institutions**. Submission flows through the host-state NCA; the technical channel and validation rules vary by NCA and must be pinned per filing.
- **EIOPA-coordinated approach for insurers and reinsurers**. Submission flows through the host-state NCA following the EIOPA-coordinated approach.
- **ESMA-coordinated approach for investment firms, fund managers, trading venues, CSDs, and CCPs**. Submission flows through the host-state NCA following the ESMA-coordinated approach. CCPs and CSDs sit under direct ESMA supervisory perimeters in some respects; pin the channel per entity type.

## Cross-skill anchors inside this plugin

- `criticality-assessment` — the source of the critical-or-important-function flag the register's `b_04_functions.criticality` field consumes.
- `vendor-diligence` — the source of the structured per-arrangement input the register's contractual-arrangement and sub-contractor-chain tables consume.
- `concentration-risk-review` — downstream consumer of the register output; the register is a precondition for the portfolio analysis.
- `exit-plan` — the register's critical-or-important-function entries should each have a current exit plan; the absence is itself a finding.

## Plugin-level shared references

Also consult, when present in the plugin:

- `references/source-map.md` — plugin-wide named-source map.
- `references/policy-control-library.md` — plugin-wide policy-and-control library.
- `references/review-gates.md` — named human-review gates and confidence-label definitions.

## Firm overlays

A firm using this skill in production adds firm-specific detail in `references/firm-overlay.md`. The skill consumes that file when present. Firm overlays do not modify the public anchors above.

## ITS table and field labels — verification posture

Indicative table labels used in this skill (`b_01_contractual_arrangement_general`, `b_02_contractual_arrangement_specific`, `b_03_ict_third_party_service_providers`, `b_04_functions`, `b_05_ict_services`, `b_06_sub_contractors_chain`, `b_07_identification_codes`) follow the published ITS table convention but column codes and exact label strings must be verified against the published Commission Implementing Regulation and its Annexes for each filing cycle. Mark uncertain field labels `[verify ITS column]` in any draft register output. The ICT-service-type taxonomy referenced as `b_05_ict_services.ict_service_type_code` is set by the ITS Annex [verify Annex number] and changes between cycles trigger a register-mapping refresh.
