---
description: Formalize a decision into project memory with a full evidence trail, drafted as pending until you confirm it
argument-hint: "<the decision to record, or the hypothesis/event driving it>"
---

# /decide -- Memory Decide

Draft a formal decision record — what's being decided, why now, the full evidence trail, and what would reverse it — always as a pending draft awaiting your confirmation.

## Invocation

```
/decide defer real-time alerts, H2 just crossed its trigger threshold
/decide we're sunsetting the legacy export feature
/decide [describe the choice and why now]
```

## Workflow

### Step 1: Draft the Decision

Apply the **memory-decide** skill:

- State what's being decided, the driver, the full evidence trail (with provenance tags), and the explicit reversal condition
- Status is always `pending` — never self-confirmed

### Step 2: Present for Confirmation

Show the draft and explicitly ask the operator to confirm before treating it as `decided`.

### Step 3: Offer Next Steps

- "Once confirmed, want me to check this against strategy (`/strategy-check`)?"
- "Should I check if any other tracked hypotheses are affected by this decision?"

## Notes

- Never mark a decision `decided` without the operator's explicit confirmation — silence is not consent.
- A decision with no evidence trail or no reversal condition is not finished — both are always required.
