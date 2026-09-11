---
description: Check a proposal, decision, or initiative against stated strategy, citing specific clauses served or contradicted
argument-hint: "<proposal, decision, or initiative to check>"
---

# /strategy-check -- Strategy Alignment Check

Check something against the project's stated strategy with citations, not a vague yes/no — built to catch drift, not rubber-stamp.

## Invocation

```
/strategy-check Building a white-label version for a reseller partner
/strategy-check The Q3 roadmap draft
/strategy-check [describe the proposal, decision, or initiative]
```

## Workflow

### Step 1: Confirm the Target and Load Strategy

Ask if not already clear what's being checked. Load the stated strategy/priorities/non-goals from `knowledge/`; if it doesn't exist yet, say so and stop rather than inventing one.

### Step 2: Run the Check

Apply the **memory-strategy-check** skill: check the input against specific strategy clauses, render a verdict (Aligned / Tension found / Gray zone), and check recent `decisions/` for a drift pattern, not just this one input.

### Step 3: Report

Output the clause-by-clause table, verdict, and recommendation per the skill's template.

### Step 4: Offer Next Steps

- "If a tension was found, want me to **draft a decision memo** to resolve it (`decide`)?"
- "Should I **flag this as a strategy gap** to raise with leadership if it's a gray zone?"

## Notes

- Every verdict must cite specific clauses — a check with no citations isn't a strategy check.
- Actively check for a drift pattern across recent decisions, not just the single input in front of you.
