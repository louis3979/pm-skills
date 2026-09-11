---
description: Draft a new hypothesis or update an existing one with new evidence, confidence, and a decision trigger
argument-hint: "<the pattern/belief to track, or the update to an existing hypothesis>"
---

# /hypothesize -- Memory Hypothesize

Turn a hunch or observed pattern into a tracked, evidence-scored hypothesis with an explicit condition for when it becomes a decision.

## Invocation

```
/hypothesize ops leads seem to prefer weekly batch over real-time alerts
/hypothesize update H2 with the new interview evidence
/hypothesize [describe the pattern and what evidence exists so far]
```

## Workflow

### Step 1: Draft or Update

Apply the **memory-hypothesize** skill:

- Check for an existing hypothesis on this topic before creating a new one
- New: statement, initial confidence, evidence, explicit decision trigger
- Update: new evidence row, confidence delta shown explicitly (old → new), trigger status re-checked

### Step 2: Offer Next Steps

- If the decision trigger just got met: "This just crossed its trigger — want me to run `/decide`?"
- "Want me to check `/review` for other stalled hypotheses while we're here?"

## Notes

- A hypothesis with no stated decision trigger isn't finished — it needs a path to resolution, not just a confidence number.
- Confidence changes always show their reasoning — never a silent overwrite.
