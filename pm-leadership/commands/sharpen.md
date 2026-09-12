---
description: Pressure-test the most recent draft/decision/plan with a menu of critique techniques, applying only what's chosen
argument-hint: "[optional: what to target, if not the most recent output]"
---

# /sharpen -- Advanced Elicitation Pass

Offer a menu of named critique techniques against the most recent draft or decision, and apply only the ones picked — refinement made deliberate and visible.

## Invocation

```
/sharpen
/sharpen run a pre-mortem on this
/sharpen the decision memo above
```

## Workflow

### Step 1: Fix the Target

Default to the most recent substantive output in the conversation, unless the user names something else.

### Step 2: Offer the Menu

Apply the **advanced-elicitation** skill: present 4-5 techniques matched to the target, plus Reshuffle / List all / Proceed.

### Step 3: Run and Halt

For each technique chosen, run it against the current version, show what it revealed and the proposed change, then halt for Apply / Reject / different direction. Repeat until the user chooses Proceed.

### Step 4: Hand Back

Return the current (possibly refined) version as the replacement for the original, noting what changed.

### Step 5: Offer Next Steps

- "Want a **second pass with a different technique**?"
- "Should I **run a full simulated debate** on this instead (`party-mode-debate`)?"

## Notes

- Never apply a proposed change without the user accepting it — the halt-and-choose loop is the entire point.
- Scale depth to the target: a paragraph gets a light pass, a launch decision gets the full treatment.
