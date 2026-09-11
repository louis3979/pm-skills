---
description: Draft a six-block plan for an objective — knowledge, assumptions vs. evidence, stakeholders, hypotheses, experiments, and decision points
argument-hint: "<objective>"
---

# /plan -- Memory-Grounded Plan

Turn an objective into a structured six-block plan that separates what's known from what's assumed and names the real decision points ahead.

## Invocation

```
/plan Reduce mid-market churn by end of quarter
/plan Validate demand for a self-serve tier
/plan [describe the objective]
```

## Workflow

### Step 1: Confirm the Objective

Ask if not already clear: what's the objective, and where did it come from (a strategy check, an ideation direction, a direct ask)?

### Step 2: Draft the Plan

Apply the **memory-plan** skill to produce all six blocks: what we know, assumption vs. evidence, who to talk to, hypotheses to open, experiments needed, and decision points.

### Step 3: Report

Output the full six-block plan per the skill's template.

### Step 4: Offer Next Steps

- "Want me to **open the hypotheses** named in block 4 (`hypothesize`)?"
- "Should I **check this against strategy** before committing to it (`strategy-check`)?"
- "When you reach a decision point, run `decide` to formalize it."

## Notes

- All six blocks are mandatory — a plan with no decision points named is incomplete.
- This command drafts the plan; it doesn't execute experiments or make the decisions inside it.
