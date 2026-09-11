---
name: build-buy-partner-analyzer
description: "Compare building in-house vs. buying software vs. integrating a partner vs. outsourcing for a needed capability. Use when deciding how to acquire a capability whose value is already validated — not whether to pursue it at all."
---

# Build / Buy / Partner Analyzer

## Purpose

Give a structured comparison of acquisition options so the decision isn't made by default or by whoever argues loudest. If it's still unclear whether the capability is worth pursuing at all, evaluate that first (see `product-bet-evaluator` in this plugin).

## Context

Check the product vision/strategy, if available, for whether this capability is meant to be a core differentiator.

## Instructions

1. Classify the capability: a core differentiator for this product, or a commodity every competitor also needs? This drives the whole recommendation.
2. Score each option — Build internally, Buy software, Integrate partner, Outsource — on: cost (upfront + ongoing), time-to-value, control/customizability, differentiation value, maintenance burden, vendor lock-in risk.
3. Apply the core rule: commodity capability → lean Buy/Partner; core differentiator with real product-specific nuance → lean Build.
4. Check switching cost: if buying/partnering, how hard would it be to migrate away later if the vendor underperforms?
5. Recommend one option with explicit rationale and a stated trigger condition that would make the team revisit the decision.

```markdown
# Build / Buy / Partner — <capability>

## Capability Classification
<core differentiator / commodity, and why — e.g. "Commodity: payment reconciliation isn't a differentiator for a retail SaaS product">

## Option Comparison
| Option | Cost | Time-to-value | Lock-in risk |
|---|---|---|---|
| Build | [high upfront] | [6-9 months] | [none] |
| Buy | [subscription] | [weeks] | [medium-high] |
| Partner | [rev-share or fee] | [weeks-months] | [low-medium] |
| Outsource | [contract cost] | [weeks] | [medium] |

### Control, differentiation & maintenance detail
- **Build** — Control: [full]; Differentiation value: [low, if commodity]; Maintenance burden: [ongoing eng cost]
- **Buy** — Control: ...; Differentiation value: ...; Maintenance burden: ...
- **Partner** — Control: ...; Differentiation value: ...; Maintenance burden: ...
- **Outsource** — Control: ...; Differentiation value: ...; Maintenance burden: ...

## Recommendation
<option, with rationale>

## Revisit Trigger
<condition that would reopen this decision — e.g. "if usage exceeds vendor's pricing tier ceiling">
```

Once decided, hand the chosen option to a PRD-writing skill (build) or a vendor-evaluation skill (buy/partner, to compare specific vendors).

## Notes

- Commodity capability + a mature vendor option existing means Build is rejected by default unless a specific stated reason overrides it (e.g. no vendor fits a required compliance regime).
- High vendor lock-in risk on a capability that might later become a differentiator favors Partner over Buy — partner relationships are typically easier to unwind than deep platform lock-in.
- No vendor/partner research yet? Do a lightweight scan first, or mark Buy/Partner scores provisional — don't guess vendor capability.
