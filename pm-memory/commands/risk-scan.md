---
description: Run a 5-area risk scan for a feature/initiative against project memory, drafting hypothesis stubs for uncovered areas
argument-hint: "<feature or initiative name>"
---

# /risk-scan -- Memory-Grounded Risk Scan

Scan a feature or initiative across value, usability, feasibility, viability, and ethical/compliance risk — grounded in what the project memory already knows, not a generic checklist.

## Invocation

```
/risk-scan Automated inventory reordering
/risk-scan Self-serve password reset via SMS
/risk-scan [describe the feature or initiative]
```

## Workflow

### Step 1: Confirm the Target

Ask if not already clear: which feature/initiative, and roughly what stage it's at (early idea vs. about to be built).

### Step 2: Run the Scan

Apply the **memory-risk-scan** skill: check `knowledge/`, `hypotheses/`, and `decisions/` for existing evidence across all 5 risk areas, classify each as Evidenced / Partial / Uncovered, and draft a hypothesis stub in `hypotheses/` for every Uncovered area.

### Step 3: Report

Output the risk table, the hypothesis stubs drafted, and the single biggest current threat, per the skill's template.

### Step 4: Offer Next Steps

- "Want me to **hypothesize further** on the uncovered areas (`hypothesize`)?"
- "Should I **draft a validation plan** for the biggest threat (`plan`)?"

## Notes

- If `knowledge/`/`hypotheses/`/`decisions/` don't exist yet in this project, run `/init-memory` first.
- An "Uncovered" area always gets a hypothesis stub — that's the point of the scan, not an optional extra.
