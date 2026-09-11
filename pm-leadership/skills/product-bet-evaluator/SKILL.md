---
name: product-bet-evaluator
description: "Evaluate a single, specific product bet across customer value, business impact, strategic fit, feasibility, risk, cost, and reversibility, producing a BUILD / BUILD MVP / PARTNER / DON'T BUILD call. Use when deciding whether to commit to one named initiative, not when ranking a backlog."
---

# Product Bet Evaluator

## Purpose

Give a structured, evidence-based recommendation on one specific bet — including MVP scope and what's explicitly deferred — instead of a gut call. For ranking many competing initiatives at once, use a prioritization-framework skill instead; this is for depth on one bet.

## Context

Pull in the product vision/strategy if available (for a strategic-fit check) and any existing customer-research output (for evidence behind the claimed customer value).

## Instructions

1. Restate the bet in one sentence to confirm scope before scoring it.
2. Score it on each of: Customer value, Business impact, Strategic fit, Technical feasibility, Time-to-value, Risk, Cost, Reversibility — one line of rationale per score, never a bare number.
3. Check the evidence behind Customer value specifically: is it based on real observed pain (cite the source), or assumed? Downgrade confidence if it's assumed.
4. Decide the recommendation type:
   - **BUILD** — high confidence, high value, low risk.
   - **BUILD MVP** — real pain confirmed but open questions remain; de-risk with a minimal version first.
   - **PARTNER/BUY** — value is real but building in-house isn't the differentiator.
   - **DON'T BUILD** — weak evidence or poor strategic fit.
5. Define MVP scope explicitly (the smallest version that tests the core assumption) and separate it clearly from "not yet" scope.
6. List the top risks that could invalidate the bet even after the MVP ships.

```markdown
# Product Bet — <bet name>

## Recommendation
<BUILD / BUILD MVP / PARTNER / DON'T BUILD>
Confidence: <High/Medium/Low>

## Why
- [Top 1-3 reasons, e.g. "High operational cost today", "Repeated customer pain", "Strong strategic alignment"]

## Scoring
| Criterion | Score | Rationale |
|---|---|---|
| Customer value | [High/Med/Low] | [evidence-backed reason] |

## MVP Scope
- [Smallest version that tests the core assumption]

## Not Yet
- [What's explicitly deferred, e.g. "ML-based demand forecasting"]

## Risks
- [What could invalidate this bet even after the MVP ships]
```

If the recommendation is BUILD/BUILD MVP, hand off to a PRD-writing skill next. If the real open question is "how to acquire this," not "whether to," switch to `build-buy-partner-analyzer` in this plugin instead.

## Notes

- Customer value scored high with zero cited evidence caps the recommendation at BUILD MVP, never a full BUILD — validate before full investment.
- Low reversibility + not-high confidence defaults to recommending a smaller, reversible first step regardless of how attractive the upside looks.
- If the bet description is too vague to score (no target user or problem stated), ask before scoring — a scored evaluation on a vague bet is false precision.
