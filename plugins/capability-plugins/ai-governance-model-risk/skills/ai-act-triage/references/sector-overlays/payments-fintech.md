# Payments and fintech sector overlay for ai-act-triage

When the scope record names sector `payments-fintech`, this overlay adds payments-and-fintech-specific scoping, BNPL and consumer-lending reach, and parallel-regime reconciliation to the EU AI Act triage. EU-authorised payment institutions and electronic-money institutions, BNPL and consumer-lending fintechs operating in or into the EU, sponsor-bank-program partners with EU end-customer exposure, and crypto-asset service providers under MiCA all use this overlay alongside the capability triage. Where there is conflict between the capability defaults and this overlay, the overlay governs the payments-and-fintech-specific elements.

Loaded by: `ai-act-triage/SKILL.md` when `scope.sector_overlay_set` includes `payments-fintech`, or when the institution type implicates a payment institution, electronic-money institution, BNPL provider, consumer-lending fintech, sponsor-bank-program partner, or MiCA-authorised crypto-asset service provider with EU operations or EU end-customers. Cited and section-referenced anchors live in `references/source-anchors.md`.

## What changes for a payments-and-fintech triage

### 1. Annex III(5)(b) is the spine for BNPL and consumer-lending fintechs

Annex III(5)(b) reaches AI systems used to evaluate creditworthiness or establish credit scores of natural persons, with the fraud-detection carve-out. For BNPL providers, consumer-lending fintechs, and any fintech extending consumer credit in or into the EU, the row is the most direct route to high-risk classification.

Boundary cases the triage flags:

- BNPL with deferred-payment-only structure (no credit charge, single-statement settlement): Consumer Credit Directive II (2023/2225) brings most BNPL into consumer-credit scope from 20 November 2026 transposition; the triage walks Annex III(5)(b) against the BNPL credit-decisioning model and typically lands in scope.
- Sponsor-bank-program decisioning where the fintech operates the model and the bank books the loan: the fintech is the provider (in-house build), the bank is the deployer (uses under its authority on its loan book). The triage records both roles.
- Salary-advance and earned-wage-access products: the EU regulatory perimeter is patchy at member-state level; where the product is consumer credit under member-state law, Annex III(5)(b) reaches.
- Merchant-credit and SME-credit decisioning: in scope of (5)(b) only where natural-person exposure is present (sole traders, micro-enterprises whose obligations attach to a natural person).

Article 6(3) derogation analysis is rarely available for credit-decisioning models that materially influence the lending decision; the triage records the derogation analysis explicitly and typically does not invoke it.

### 2. Fraud-detection AI: the carve-out and what it does not cover

The (5)(b) carve-out for fraud detection covers fraud detection. Payments fraud, account-takeover detection, transaction-fraud scoring, and chargeback-fraud prediction are not creditworthiness systems and do not fall under (5)(b) at all; the triage records the row as not applicable rather than relying on the carve-out.

Boundary cases the triage flags:

- Risk-rating models that combine fraud signals with credit signals into a single score that influences lending or pricing: the carve-out does not protect the credit-influencing portion of the score; the model is in scope of (5)(b) for the credit use.
- Behavioural authentication AI: not (5)(b); not typically Annex III; Article 50 transparency screened on the user-interface facts.

### 3. PSD2 / PSD3 / PSR strong customer authentication and AI fraud

For payment institutions and credit institutions providing payment services in the EU, the strong customer authentication regime under PSD2 (and the PSD3 and PSR proposals at the time of writing) reaches the authentication surface. AI used in transaction risk analysis exemptions under Commission Delegated Regulation 2018/389 (the SCA RTS) attaches:

- The SCA TRA exemption regime is the operative governance frame for AI in payment-fraud transaction risk analysis; the AI Act high-risk regime does not attach because (5)(b) is for creditworthiness and the carve-out covers fraud detection.
- The SCA TRA model nonetheless attracts EBA Guidelines on the limited application of the SCA exemption and member-state competent-authority oversight.

The triage records the regime overlap and routes the SCA-TRA model to the firm's payments-compliance function.

### 4. EMD / EMD2 e-money issuance and AI

For electronic-money institutions issuing e-money in the EU, AI used in onboarding, monitoring, or limit-management decisions reaches the EMI regulatory regime. AI Act high-risk classification attaches only where the use case lands in an Annex III row; for most EMI use cases, the answer is not Annex III. The triage walks the rows and records the conclusion.

### 5. Sponsor-bank-program partnerships: EU-side exposure for US fintechs

For US fintechs in sponsor-bank-program structures with EU end-customer exposure (e.g., a US BNPL fintech offering checkout into EU merchants whose customers reside in the EU), the AI Act extraterritorial reach under Article 2(1)(c) attaches where the system's output is used in the EU. The triage records:

- The US fintech's role under the AI Act (typically provider of the credit-decisioning model used in the EU).
- The sponsor-bank's role (the US sponsor bank may not have an EU operator role; the EU-side deployer may be a separate EU entity or the analysis may turn on whether the system's output is used in the EU).
- The authorised representative obligation under Article 22 if the US fintech is a provider with EU exposure but no EU establishment; the representative is required.
- The interaction with PSD2 / E-Money Directive licensing for the EU-facing service (typically a separate workstream).

The Article 2(1)(c) extraterritorial reach is the load-bearing analysis for US fintechs without an EU establishment. The triage records the analysis on the operator-role line and routes to legal where the reach is contested.

### 6. MiCA reach for crypto-asset service providers

For crypto-asset service providers authorised under MiCA (Regulation (EU) 2023/1114), AI used in client-onboarding, transaction monitoring, market-abuse detection (under MiCA Article 92), and ARTs / EMTs operations attaches under MiCA. The AI Act overlay attaches where any Annex III row applies (rare for typical CASP use cases) or where Article 50 transparency obligations attach to client-facing surfaces. The triage records:

- The CASP authorisation status and the MiCA obligations operative for the use case.
- Whether the CASP issues ARTs or EMTs (additional issuer obligations under MiCA Title III and IV).
- The AI Act exposure on the EU side (typically Article 50 transparency for client-facing surfaces; market-abuse detection under MiCA Article 92 runs alongside but does not displace MAR-like AI Act considerations).

### 7. DORA reach for ICT third-party risk

For payment institutions, EMIs, credit institutions, and CASPs in scope of the Digital Operational Resilience Act (Regulation (EU) 2022/2554), AI vendor relationships are ICT third-party arrangements under DORA. The triage records:

- Whether the AI vendor is an ICT third-party service provider supporting a critical or important function under DORA.
- The DORA register-of-information entry for the AI vendor (cross-link to `dora-register-builder`).
- The DORA exit-strategy and contractual-clauses obligations for AI vendor contracts.
- The interaction with AI Act Article 26 deployer obligations on logging and monitoring (the DORA logging requirements and the AI Act logging requirements both apply; the firm operates one logging stack that satisfies both).

### 8. Article 27 FRIA reach for credit institutions and certain private operators

Article 27(1) reaches deployers that are public bodies (Article 27(1)(a)), private entities providing public services (also under (1)(a)), credit institutions (Article 27(1)(b)), insurance undertakings ((1)(b)), and deployers using systems intended to evaluate creditworthiness or establish credit score under Annex III(5)(b) ((1)(b)). For payments and fintech entities:

- A consumer-lending fintech that is not a credit institution under EU classification: (1)(b) reaches via the Annex III(5)(b) trigger; the FRIA is required.
- A BNPL fintech under CCD II: same analysis; (1)(b) reaches via the (5)(b) trigger.
- A sponsor-bank-program structure with the credit-institution sponsor as deployer: the credit-institution arm of (1)(b) reaches the bank; the fintech is the provider but not the deployer of the (5)(b) system in the bank's loan book.

The triage records the FRIA-vs-DPIA reconciliation; the GDPR DPIA does not satisfy Article 27 on the fundamental-rights, mitigation, governance, and complaints-handling elements.

### 9. CFPB Circulars analogue and adverse-action posture

For US-side consumer-credit reach, CFPB Circulars on adverse-action notification (2022-03 and 2023-03) reach the US-side adverse-action workflow; the AI Act does not directly impose a CFPB-style obligation on the EU side, but Articles 13 (transparency to deployers) and 14 (human oversight) plus GDPR Article 22 reach the EU side of the same surface. The triage records the parallel obligations on a side-by-side block where the firm's footprint includes both jurisdictions.

### 10. Payments-and-fintech-AI use-case categories the triage explicitly recognises

The triage labels the use-case category up front:

- Consumer-credit decisioning (BNPL, consumer-lending fintech, sponsor-bank-program credit): Annex III(5)(b) applies; FRIA via (1)(b); CCD II reach where transposed.
- Payments fraud (transaction-fraud scoring, account-takeover, chargeback-fraud): not Annex III; SCA TRA regime operative.
- KYC / onboarding AI: not Annex III; AML regime (AMLR / AMLD6 transposition) operative.
- Customer-facing chatbot or assistant: not Annex III; Article 50 transparency applies.
- Merchant-credit and SME-credit decisioning: Annex III(5)(b) applies for natural-person exposure; legal-entity-only scope routes outside (5)(b).
- Crypto-asset services AI (CASP): not Annex III typically; MiCA regime operative; Article 50 for client-facing surfaces.
- Internal productivity GenAI: not Annex III; Article 50 sub-obligations screened on the facts.
- Marketing personalisation: typically not Annex III; Article 5(1)(a) manipulation screen runs (conduct overlay) where behavioural-economics levers are in play.

## Payments-and-fintech-specific output template additions

The triage artifact adds the following blocks when this overlay loads:

- A use-case category line at the top (per the categories above).
- An EU-extraterritorial-reach line where the firm has no EU establishment (Article 2(1)(c) analysis).
- An authorised-representative obligation line (Article 22) where extraterritorial reach attaches and no EU establishment exists.
- A sponsor-bank-program operator-role table (which entity is provider, which is deployer) where the structure applies.
- A SCA TRA regime line for payment-fraud AI use cases.
- A DORA register-and-exit-strategy line for AI vendor relationships in scope.
- A MiCA regime line for CASP use cases.
- A FRIA-vs-DPIA reconciliation note for any (5)(b) use case.
- A US-side / EU-side parallel-regime reconciliation block where the firm's footprint spans both.

## Common pitfalls in payments-and-fintech AI Act triages

- Treating BNPL as outside consumer-credit and therefore outside (5)(b); CCD II brings most BNPL into consumer-credit scope and the triage must walk (5)(b) on the BNPL credit-decisioning surface.
- Relying on the (5)(b) fraud-detection carve-out for risk-rating models that combine fraud and credit signals; the carve-out does not protect the credit-influencing portion of the score.
- Missing Article 2(1)(c) extraterritorial reach for US fintechs serving EU end-customers without an EU establishment; the reach attaches and the authorised-representative obligation under Article 22 follows.
- Conflating the SCA TRA regime with the AI Act high-risk regime for payment-fraud AI; the SCA TRA regime is the operative governance frame; the AI Act high-risk regime does not attach.
- Skipping the FRIA on the assumption that a payment institution or BNPL fintech is not a credit institution; (1)(b) reaches via the (5)(b) trigger regardless of credit-institution classification.
- Treating sponsor-bank-program AI as the bank's problem; the fintech as provider has Article 11, 13, 14, 15 obligations on its own surface.
- Missing DORA register-of-information entries for AI vendors supporting critical or important functions; the register is operational on 17 January 2025 and the AI vendor relationship is in scope.
- Treating MiCA AI use cases as outside the AI Act because MiCA is the operative regime; Article 50 transparency reaches client-facing CASP surfaces and the screen must run.
- Asserting Article 6(3) derogation for credit-decisioning to escape high-risk classification; the derogation is rarely available for systems that materially influence credit decisions.
