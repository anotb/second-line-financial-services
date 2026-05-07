# Source anchors — insurance-outsourcing-review

The named, dated regulatory sources this skill anchors to. SKILL.md cites this file by path and does not restate excerpts. Cross-cutting and sector-overlay flavour live in the corresponding overlay files.

## Primary frame — NAIC outsourcing and holding-company family

- **NAIC Insurance Holding Company System Regulatory Act, Model #440** [verify model number]. Affiliate-transaction supervision, ultimate-controlling-person disclosure, and the supervisory frame for intra-group outsourcing [verify section]. The regulators applying this Act are state insurance departments, not federal banking agencies. https://content.naic.org/cipr-topics/insurance-holding-company-system [verify URL].

- **NAIC Insurance Holding Company System Model Regulation, Model #450** [verify model number]. Form B (holding-company registration) and Form D (transactions between affiliates) detail. Form D is the procedural filing the exam picks up when an affiliate outsourcing arrangement crosses the materiality threshold. Subsection references for Form B / Form D mechanics: [verify section]. https://content.naic.org/cipr-topics/insurance-holding-company-system [verify URL].

- **NAIC Insurance Data Security Model Law, Model #668**. Third-party service-provider oversight at §4.F: written-contract requirements, due diligence before contract, ongoing monitoring, incident-response cooperation, breach-notification chain to the cedent insurer. Adoption is state-by-state; the NAIC adoption tracker is the public reference. https://content.naic.org/sites/default/files/MO668.pdf [verify URL].

- **NAIC Unfair Trade Practices Act, Model #880**. Claims-handling standards that follow the function even when delegated to a TPA or claims administrator; §4 unfair claims-settlement practices [verify section]. UDAP exposure on the carrier flows from the delegated function back to the carrier of record. https://content.naic.org/cipr-topics/unfair-trade-practices [verify URL].

- **NAIC Risk Management and Own Risk and Solvency Assessment Model Act, Model #505** [verify model number]. Critical outsourced functions belong in the ORSA Summary Report; the carrier's own ORSA materiality threshold drives inclusion [verify section]. https://content.naic.org/cipr-topics/own-risk-and-solvency-assessment-orsa [verify URL].

- **NAIC Producer Licensing Model Act** [verify model number]. Per-state per-individual licensing required for any party exercising binding, quoting, issuance, or producer authority on the carrier's behalf [verify section]. The exam reviews per-individual status, not entity-only. https://content.naic.org/cipr-topics/producer-licensing [verify URL].

## State Department of Insurance bulletins

- **State DOI bulletins on TPA registration and oversight**. Pin by state and date when used; treat each as a state-specific overlay. Many states have a TPA Act based on the NAIC TPA Model Act with their own registration and fiduciary requirements [verify state-by-state model adoption against the current NAIC adoption tracker].

- **State DOI bulletins on AI use in insurance**. Operating footprint drives which bulletins apply; cite by state and date when used. Examples that recur in the operating footprint: Colorado SB 21-169 implementing regulation (life-insurance underwriting governance and risk management); NY DFS Insurance Circular Letter on AI and ECDIS in life-insurance underwriting (January 2024) [verify exact circular number]; California DOI bulletin on AI use in insurance [verify exact bulletin]. The NAIC AI Working Group adoption tracker covers state-by-state adoption of the NAIC Bulletin December 2023 model.

## Vendor-AI accountability anchor

- **NAIC Bulletin on the Use of Artificial Intelligence Systems by Insurers, December 4, 2023**. Carrier accountability for vendor and third-party AI used on its policies. AIS Program elements (governance, risk management, testing, validation, third-party-AI accountability, monitoring, documentation, transparency, fairness). The Bulletin itself is not law; track state-by-state adoption status via the NAIC AI Working Group adoption tracker. https://content.naic.org/sites/default/files/inline-files/2023-12-04%20Model%20Bulletin_Adopted_0.pdf [verify URL].

## Privacy anchors that load into the cross-cutting privacy overlay

- **HIPAA Privacy Rule (45 CFR Parts 160, 164 Subpart E) and Security Rule (45 CFR Parts 160, 164 Subpart C)**. Business-associate-agreement and breach-notification posture for any TPA, claims administrator, or data-processing outsourcer that touches protected health information; relevant to life and health TPA arrangements. https://www.hhs.gov/hipaa/for-professionals/index.html .

- **NAIC Insurance Information and Privacy Protection Model Act, Model #670** [verify model number]. State insurance information-and-privacy framework where adopted; relevant to consumer-information handling in delegated functions [verify section]. https://content.naic.org/cipr-topics/privacy-protections [verify URL].

## Cross-cutting cyber anchors

- **NAIC Insurance Data Security Model Law, Model #668 (cyber components)**. The cyber expectation chain to the third-party service provider and its sub-processors flows from §4.F. Adoption state-by-state.

- **NYDFS 23 NYCRR Part 500.11**. Where the carrier is a NYDFS Covered Entity, 500.11 reach extends to vendor diligence directly and runs alongside or in place of Model #668 depending on state of license and entity type.

## Plugin-level shared references

Also consult, when present in the plugin:

- `references/source-map.md` — plugin-wide named-source map (NAIC Model index entries dated to the live NAIC Model Laws & Regulations index).
- `references/policy-control-library.md` — plugin-wide policy-and-control library (AIS Program elements, §4.F third-party-service-provider control families).
- `references/public-regulatory-scenarios.md` — canonical public-source-derived scenario library for example reuse across the plugin.

## Firm overlays

A firm using this skill in production adds firm-specific detail in `references/firm-overlay.md` (carrier-specific ORSA materiality threshold, named TPA-agreement template clauses, named sign-off owners, internal AI register, named state-DOI relationship-managers). The skill consumes that file when present. Firm overlays do not modify the public anchors above.

## Verification posture

`[verify model number]`, `[verify section]`, and `[verify URL]` flags are deliberate. Several NAIC model numbers (Holding Company Act / Reg #440 and #450; ORSA Model #505; Producer Licensing Model Act; NAIC Insurance Information and Privacy Protection Model Act #670) need confirmation against the live NAIC Model Laws & Regulations index before the citation is used in a final pack. Phase-3 verification grinds these down. Fabrication is not the alternative.
