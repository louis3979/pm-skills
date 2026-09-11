---
description: Evaluate a specific product bet, resolve how to acquire it if relevant, and formalize the outcome as a decision memo
argument-hint: "<a specific product bet or capability decision>"
---

# /evaluate-bet -- Bet Evaluation + Decision Memo

Take one specific, named bet from raw idea to a documented, sign-off-ready decision.

## Invocation

```
/evaluate-bet Should we build automated inventory allocation?
/evaluate-bet We need payment reconciliation — build or buy?
/evaluate-bet Add SSO support for enterprise customers
```

## Workflow

### Step 1: Clarify the Bet

Restate it in one sentence: what it is, what problem it addresses, for whom. Ask if this is missing.

### Step 2: Evaluate the Bet

Apply the **product-bet-evaluator** skill:

- Score customer value, business impact, strategic fit, feasibility, time-to-value, risk, cost, reversibility
- Produce a BUILD / BUILD MVP / PARTNER / DON'T BUILD recommendation with MVP scope and deferred scope

### Step 3: Resolve Acquisition Method (if relevant)

If the recommendation is PARTNER, or the bet is really an acquisition question ("build or buy"), apply the **build-buy-partner-analyzer** skill:

- Classify the capability as core differentiator or commodity
- Compare Build / Buy / Partner / Outsource on cost, time-to-value, control, differentiation, maintenance, lock-in
- Recommend one option with a revisit trigger

### Step 4: Formalize as a Decision

Apply the **decision-memo** skill to turn the recommendation into a sign-off-ready memo:

- Options (including "do nothing"), trade-off comparison, clear recommendation, named approver and deadline

### Step 5: Present the Consolidated Output

```
# Bet Evaluation & Decision — [bet name]

## Bet Evaluation
[product-bet-evaluator output]

## Acquisition Method (if applicable)
[build-buy-partner-analyzer output]

## Decision Memo
[decision-memo output]
```

### Step 6: Offer Next Steps

- "Ready to hand this off to a PRD-writing skill if BUILD/BUILD MVP?"
- "Want a **board-update** line drafted on this decision for the next report?"
- "Should this decision be raised in your next **1:1** with anyone it affects?"

## Notes

- Don't run Step 3 if the bet clearly isn't an acquisition question — skip straight to formalizing the BUILD/DON'T BUILD call.
- If the bet description is too vague to score (no target user or problem stated), stop and ask before scoring.
- The decision memo always needs a named approver and deadline — don't finalize without one.
