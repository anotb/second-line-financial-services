#!/usr/bin/env python3
"""Static content tests for public-regulatory examples and expected outputs.

These tests intentionally avoid named institutions and private policies. They check
that the bundled examples retain source anchors, human-review gates, and the
minimum public-source-derived concepts the skills and agents should preserve.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

def fail(msg: str) -> None:
    errors.append(msg)

def read(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        fail(f"missing required test artifact: {rel}")
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")

checks = {
    "examples/public-regulatory/ai-governance/eu-ai-act-creditworthiness-triage.md": [
        "Annex III",
        "creditworthiness",
        "natural persons",
        "high-risk",
        "fraud detection",
        "Human-review gate",
    ],
    "examples/public-regulatory/ai-governance/occ-model-risk-ai-gap-assessment.md": [
        "OCC Bulletin 2026-13",
        "generative AI and agentic AI",
        "not within the scope",
        "validation",
        "governance and controls",
        "Human-review gate",
    ],
    "examples/public-regulatory/third-party-operational-resilience/dora-ict-register-entry.yaml": [
        "source_anchor",
        "critical_or_important_function",
        "ict_third_party_service_provider",
        "subcontractor",
        "exit_plan",
    ],
    "examples/public-regulatory/third-party-operational-resilience/interagency-tprm-contract-gap.md": [
        "planning",
        "due diligence",
        "contract negotiation",
        "ongoing monitoring",
        "termination",
        "Human-review gate",
    ],
    "examples/public-regulatory/risk-reporting/bcbs239-risk-report-gap.md": [
        "aggregate risk exposures",
        "fully, quickly, and accurately",
        "Governance",
        "Accuracy and integrity",
        "Completeness",
        "Human-review gate",
    ],
    "examples/public-regulatory/risk-reporting/sec-cyber-disclosure-readiness.md": [
        "four business days",
        "materiality determination",
        "not discovery",
        "without unreasonable delay",
        "disclosure committee",
        "Human-review gate",
    ],
    "examples/public-regulatory/compliance-testing/cfpb-1071-data-firewall-test-plan.md": [
        "Section 1071",
        "Regulation B section 1002.107",
        "protected demographic information",
        "shielded",
        "covered applications",
        "Human-review gate",
    ],
    "examples/public-regulatory/financial-crime-governance/ffiec-cdd-high-risk-customer-review.md": [
        "FFIEC",
        "Customer risk profile",
        "Beneficial ownership",
        "ongoing monitoring",
        "Human-review gate",
    ],
}

for rel, needles in checks.items():
    text = read(rel)
    lower = text.lower()
    for needle in needles:
        if needle.lower() not in lower:
            fail(f"{rel}: missing expected public-source concept: {needle}")

policy = read("common/references/policy-control-library.md")
for risk_id in ["R-AI-01", "R-AI-03", "R-TPRM-01", "R-DORA-01", "R-RPT-01", "R-CYB-01", "R-FC-01", "R-FL-01"]:
    if risk_id not in policy:
        fail(f"policy-control library missing baseline risk {risk_id}")

for rel in [
    "tests/expected/ai-creditworthiness-expected.md",
    "tests/expected/dora-register-expected.md",
    "tests/expected/sec-cyber-expected.md",
]:
    text = read(rel)
    if "Does not" not in text and "Leaves final" not in text:
        fail(f"{rel}: expected output should include negative/guardrail checks")

if errors:
    print("Content tests failed:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)
print("Content tests passed")
