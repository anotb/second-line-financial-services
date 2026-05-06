# Climate cross-cutting overlay — rule-to-obligation-extraction

Load only when the rule under extraction is anchored to climate-related disclosure, climate-risk management, or sustainability reporting. The space is unsettled in the United States and more developed in the EU and UK; the extraction must capture the rule under extraction at the version in effect at the extraction date and flag the litigation or revision history where it is material.

## US — SEC climate-related disclosure rule history

The SEC adopted the climate-related disclosure final rule on March 6 2024 (89 FR 21668, March 28 2024) and stayed it on April 4 2024 pending litigation. The rule's effective and compliance dates have been overtaken by subsequent procedural events; the extraction must read the rule's current operational status before producing rows. When the rule is operative, decomposition includes:

- **Material-climate-related-risks disclosure** (Reg S-K Item 1500 series). Annual disclosure of material climate-related risks affecting the registrant's strategy, business model, and outlook.
- **Governance disclosure**. Board oversight; management's role in assessing and managing material climate-related risks.
- **Risk-management disclosure**. Processes for identifying, assessing, and managing material climate-related risks.
- **Material-climate-targets-and-goals disclosure** (where the registrant has them).
- **Greenhouse-gas-emissions disclosure** (Scope 1 and Scope 2 for large accelerated filers and accelerated filers, where material). Scope 3 was not part of the final rule (changed from the proposal). Assurance requirements phased in.
- **Financial-statement footnote disclosures** of climate-related effects on financial statements.

When extracting from the rule (in any operational status), the source pin is the codified Reg S-K item number plus the FR cite. Litigation status goes in the open-extraction-questions section with a note on the blocker for downstream skills.

## EU — Corporate Sustainability Reporting Directive (CSRD) and ESRS

- **Directive (EU) 2022/2464 (CSRD)** amends prior accounting and audit directives to require sustainability reporting by in-scope entities. Implementation is through member-state legislation; the directive is binding as to result. Reporting follows the European Sustainability Reporting Standards (ESRS) adopted as Commission Delegated Regulations.
- **ESRS adopted standards** (Commission Delegated Regulation (EU) 2023/2772): cross-cutting standards (ESRS 1 General requirements; ESRS 2 General disclosures); environmental standards (E1 climate change, E2 pollution, E3 water and marine resources, E4 biodiversity and ecosystems, E5 resource use and circular economy); social standards (S1 own workforce, S2 workers in the value chain, S3 affected communities, S4 consumers and end-users); governance standards (G1 business conduct).
- **Phased application**. CSRD applies in stages: large public-interest entities (financial year 2024); other large undertakings (FY 2025); listed SMEs and small and non-complex credit institutions (FY 2026 with a two-year deferral option); third-country undertakings (FY 2028).

Extraction from CSRD plus an ESRS standard pins to the ESRS standard reference (e.g., `ESRS E1 §AR.46`); each ESRS disclosure requirement is potentially a row depending on the granularity required.

## EU — Sustainable Finance Disclosure Regulation (SFDR)

- **Regulation (EU) 2019/2088 (SFDR)** plus Commission Delegated Regulation (EU) 2022/1288 (RTS). Applies to financial-market participants and financial advisers. Decomposition: entity-level disclosures (Article 3 sustainability-risk policy; Article 4 due-diligence statements on principal adverse impacts; Article 5 remuneration policies); product-level disclosures (Article 6 sustainability-risk integration; Article 8 light-green products promoting environmental or social characteristics; Article 9 dark-green products with sustainable investment objective); periodic-reporting under the RTS templates.

## EU — Taxonomy Regulation

- **Regulation (EU) 2020/852 (Taxonomy Regulation)** plus Commission Delegated Regulations. Defines environmentally sustainable economic activities and imposes turnover, capex, and opex disclosure obligations on financial-market participants and large undertakings. Decomposition: in-scope-activity classification; technical-screening-criteria conformity; do-no-significant-harm assessment; minimum-safeguards conformity; reported KPIs.

## UK — TCFD-aligned and SDR

- **FCA TCFD-aligned disclosure** in PS 21/23 (asset managers) and PS 21/24 (listed-company premium-listed and standard-listed segment) [verify FCA policy-statement numbers]. Pin to the FCA Handbook chapter (ESG sourcebook; LR sourcebook).
- **FCA Sustainability Disclosure Requirements (SDR) and labels** (PS 23/16, November 28 2023; rules in ESG sourcebook). Anti-greenwashing rule effective May 31 2024; labels and naming-and-marketing rules staged through 2025.

## ISSB-aligned standards

- **IFRS S1 General Requirements for Disclosure of Sustainability-related Financial Information** and **IFRS S2 Climate-related Disclosures** (issued June 2023). The ISSB standards are adopted by jurisdictions as their domestic-disclosure framework permits; jurisdiction-by-jurisdiction adoption status applies. Where a jurisdiction has adopted ISSB, the extraction pins to the jurisdiction's adoption instrument (e.g., the relevant securities regulator's rule) plus the IFRS S1/S2 reference.

## Defined-term sensitivity

Climate rules are particularly sensitive to defined-term scope. Definitions to capture verbatim with their source pins:

- "Material climate-related risks" — varies; SEC framing under Reg S-K is the materiality standard from US securities law; CSRD-ESRS double-materiality differs.
- "Greenhouse-gas emissions" and the Scope 1/2/3 framing — usually GHG-Protocol-aligned but the rule's own definition controls.
- "Physical risk" and "transition risk" — sometimes defined; sometimes used without definition.
- "Sustainable investment" (SFDR Article 2(17)).
- "Environmentally sustainable economic activity" (Taxonomy Regulation Article 3).

## When to layer with sector overlays

Climate obligations frequently sit on top of sector-specific rules. When the rule under extraction is a banking-supervisor climate-risk-management framework (e.g., FRB SR 23-5; OCC framework; PRA Supervisory Statement 3/19), load `cross-cutting/climate.md` and `sector-overlays/banking.md`. When the rule is a SEC disclosure rule, load `cross-cutting/climate.md` and `sector-overlays/capital-markets.md`. When the rule is a NAIC climate-risk disclosure framework, load `cross-cutting/climate.md` and `sector-overlays/insurance.md`.
