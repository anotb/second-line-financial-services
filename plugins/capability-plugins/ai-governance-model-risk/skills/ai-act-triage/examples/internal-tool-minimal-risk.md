# Example: vendor-hosted GenAI assistant for pension-document summarisation, EU institutional clients

Public-source-derived. No named institution. Triage pattern drawn from EU AI Act (Regulation (EU) 2024/1689) Article 6, Annex III, and Article 50; AI Office guidance on the boundary between deployer and provider obligations for vendor-hosted GenAI; and the EU Code of Practice on General-Purpose AI as a soft-law reference.

## Input description

A US asset-management group with an Irish UCITS management-company subsidiary deploys a vendor-hosted GenAI assistant inside the institutional-client servicing function. The assistant ingests scheme documents (trust deeds, statements of investment principles, annual reports), summarises them on request, and drafts written responses to scheme-trustee queries that the client servicing team reviews before sending. No automated trade execution, no investment recommendation generation, no client-facing chatbot. Human-in-the-loop on every output. Second-line AI governance has been asked for the EU AI Act triage so the deployment can clear the AI risk committee gate before go-live in the Irish entity.

Engagement scope provided by `scoping`:

- Institution type: UCITS management company (Irish ManCo); US group asset manager; in-scope engagement covers the EU deployment only.
- Primary regulators: Central Bank of Ireland (UCITS-supervisor capacity); Marketing Rule reach considered for the US parent if any output is reused into US-client materials (out of scope of this engagement).
- Persona: AI Governance Lead (second line), reporting to the EMEA CRO; legal review at sponsor level.
- Sector overlay set: capital markets. Cross-cutting overlays: privacy (GDPR; document content includes some scheme-member personal data in tables and trustee correspondence), conduct (institutional-client communication; Marketing Rule reach in US considered separately).
- Source posture: public-plus-firm-policy-plus-vendor-evidence.

## Output sketch

Triage decision (abbreviated):

- **Use case scope and EU exposure** — assistant is operated by the Irish ManCo on EU institutional clients; eu_users true, eu_operations true, eu_data_subjects true (limited; scheme-member data appears in source documents), market_placement true. EU exposure clear.
- **Operator role** — the Irish ManCo is deployer (uses under its own authority, on its own clients). The vendor is provider of the underlying GenAI system and provider of the GPAI model upstream of the system. The triage notes both relationships and the related obligations the deployer must evidence from the vendor.
- **Article 5 prohibited screen** — clear. Each sub-practice screened: subliminal techniques (no, professional summarisation context), exploitation of vulnerabilities (no, institutional client base), social scoring (no), the law-enforcement and biometric sub-practices (n/a), emotion recognition (no), biometric categorisation (no). Recorded explicitly.
- **Article 6 high-risk classification** — not high-risk. Walk of Annex III row by row recorded:
  - Annex III(1) biometrics — no.
  - Annex III(2) critical infrastructure — no.
  - Annex III(3) education and vocational training — no.
  - Annex III(4) employment, workers' management, access to self-employment — no.
  - Annex III(5)(a) public assistance benefits — no.
  - Annex III(5)(b) creditworthiness or credit scoring of natural persons — no; this is institutional servicing, not consumer credit.
  - Annex III(5)(c) life and health insurance pricing — no.
  - Annex III(5)(d) emergency dispatch — no.
  - Annex III(6) law enforcement — no.
  - Annex III(7) migration, asylum, border control — no.
  - Annex III(8) administration of justice and democratic processes — no.
- **Article 50 transparency** — applies. The assistant generates synthetic content (summaries and draft responses); Article 50 sub-obligations screen as follows:
  - 50(1) interaction with AI system disclosure: applies inside the firm (employees know they are interacting with the assistant; documented in firm policy).
  - 50(2) synthetic content marking: applies; output that leaves the firm to clients carries a disclosure that the draft was AI-generated and reviewed by the named team. Disclosure owner: client servicing.
  - 50(3) deepfake disclosure: not applicable (no synthetic image, audio, or video).
  - 50(4) AI-generated text on matters of public interest: not applicable (institutional-servicing context, not public-interest publication).
  - 50(5) emotion recognition / biometric categorisation disclosure: not applicable.
- **GPAI considerations** — gpai_in_scope true. The vendor's underlying GPAI model is in scope of Article 51-55 obligations on the vendor; the firm's deployer-side asks include training-data summary per Article 53(1)(d), copyright posture, and transparency documentation for the deployer's own evidence file. The vendor's signature status on the EU AI Office Code of Practice is recorded (signed). Systemic-risk designation of the vendor's model: recorded as the vendor's published status; the deployer's own obligations do not change, but the evidence-asks tier up if the vendor is a designated systemic-risk GPAI provider.
- **Classification** — primary: limited_risk_article_50. Secondary: gpai (vendor-side; recorded so the deployer's evidence file picks up the GPAI provider's published documentation under Article 53). Out of high-risk; Annex III walk recorded so the analysis is auditable.
- **Obligations summary** (selected):
  - Article 50(1) and 50(2) transparency to users (deployer-shared with provider where the disclosure is technically generated; firm-side owner: client servicing for the marking on outbound drafts; AI governance for the policy).
  - Article 26 deployer obligations are limited where the system is not high-risk; the assistant is in scope of Article 50 only, so the substantive deployer obligations of Article 26 (logging, monitoring, instruction-of-use compliance, human oversight at deployer level) do not attach in the same way they would for a high-risk system. Recorded explicitly.
  - GPAI vendor-evidence asks per Article 53 documentation (deployer-side; asks logged in the vendor diligence record cross-linked to `vendor-diligence` and to `llm-vendor-evidence-review`).
- **Annex IV documentation deltas** — not required at this classification (not high-risk). The model card produced under `model-card-builder` covers the firm-side governance artifact; Annex IV is not the applicable obligation.
- **FRIA** — not required (not high-risk and not Article 27 trigger).
- **Registration** — not required (Article 71 register is for high-risk systems).
- **Applicable date** — Article 50 transparency obligations applicable from 2 August 2026 per Article 113. GPAI obligations on the vendor applicable from 2 August 2025. The deployer's go-live can proceed against current vendor documentation; the 2 August 2026 date is the binding constraint for the Article 50 disclosure language being live on every outbound draft.
- **Monitoring for re-classification** — re-triage triggers: change in scope of the assistant (e.g., adding investment-recommendation generation; adding consumer-facing surface; adding emotion-recognition feature); change in vendor model that materially shifts capabilities; change in the EU AI Office's interpretation of Article 6 or Annex III boundaries (track AI Office guidance and Code of Practice updates); change in the firm's product line that brings the assistant into a high-risk Annex III row by extension. Owner: AI Governance Lead, frequency quarterly plus at trigger events.
- **Open questions and dissent** — one item flagged for legal: whether the inclusion of scheme-member personal data in the source documents (tables of beneficiaries) tips the GDPR profile materially enough to require a fresh DPIA scoped to the assistant deployment. Counsel position pending. Article 50 disclosure language pre-cleared by legal as a separate workstream.
- **Source trace** — every material claim cited to article and annex; AI Office Code of Practice referenced as soft-law for vendor-evidence framing; vendor's published Article 53 documentation cited at confidence high (vendor-issued, dated, and signed under Code of Practice); deployer-side evidence asks recorded in the vendor diligence record.
- **Capital-markets overlay notes** — Marketing Rule reach considered for any reuse of the assistant's output in US-client materials (out of scope of this engagement, flagged for the US parent's compliance team); MiFID II considerations for any reuse in EU professional-client communications (within scope; firm policy already requires the human-review gate for any such reuse).

## Why this scenario matters

- It exercises the Article 6 / Annex III walk for a use case that ends in not-high-risk. A senior reviewer should not skip the row-by-row analysis just because the obvious answer is "no". The analysis is auditable evidence that the screen ran.
- It exercises Article 50 in the limited-risk landing zone, including the explicit screen of each sub-obligation. The triage shows that 50(2) synthetic content marking is the load-bearing obligation for outbound drafts; the firm's disclosure language is a deliverable consequence.
- It exercises the GPAI-as-secondary-classification pattern: the vendor's GPAI obligations on the upstream model do not transfer to the deployer, but the deployer's evidence file picks up the vendor's published documentation and tracks Code of Practice signature status. The triage routes the deployer-side asks to the vendor-diligence record and to `llm-vendor-evidence-review`.
- It exercises the deployer-vs-provider distinction without conflating the two: the vendor is provider; the firm is deployer; the obligations attach differently. The triage records the vendor's role and the firm's role, and attaches obligations to each.
- It exercises the phasing: Article 50 obligations applicable from 2 August 2026, GPAI obligations on the vendor from 2 August 2025. The triage carries both dates and the disclosure-language deliverable as the binding go-live constraint on the firm side.
