---
description: Generate solution directions for a problem/opportunity area, each grounded in the project's actual knowledge and hypotheses
argument-hint: "<problem or opportunity area>"
---

# /ideate -- Memory-Grounded Ideation

Generate 3-7 solution directions for a known problem/opportunity, each traceable to real insight, hypothesis, or decision already in the project memory — not a generic brainstorm.

## Invocation

```
/ideate Reduce support ticket volume for password resets
/ideate Improve mid-market activation rate
/ideate [describe the problem or opportunity]
```

## Workflow

### Step 1: Confirm the Problem Is Established

If the problem itself isn't yet validated in memory, say so and suggest validating it first rather than ideating on an unconfirmed problem.

### Step 2: Generate Directions

Apply the **memory-ideate** skill: load grounding context from `knowledge/`, `hypotheses/`, and `decisions/`, generate 3-7 directions each tagged with its grounding and an honest evidence-provenance tag, each explicitly labeled "proposed."

### Step 3: Report

Output the directions with grounding, status, and validation-needed per direction, per the skill's template.

### Step 4: Offer Next Steps

- "Want me to **draft a plan** for the strongest direction (`plan`)?"
- "Should I **open a hypothesis** to validate one of these (`hypothesize`)?"
- "Want a **strategy check** on the top direction before going further (`strategy-check`)?"

## Notes

- Every direction must be traceable to real grounding or an honest non-path evidence tag — never dress up a hunch as evidence-backed.
- This command never promotes a direction to a decision — that's a separate, deliberate step.
