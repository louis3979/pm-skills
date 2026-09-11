---
description: Run the weekly maintenance sweep across project memory (stale knowledge, evidence, hypotheses, stakeholder cadence, compression, archival)
argument-hint: "[optional: focus area, e.g. hypotheses or stakeholders]"
---

# /review -- Memory Review

Run the full six-check maintenance sweep over project memory, producing one dated report — the operation that keeps the whole memory system from rotting.

## Invocation

```
/review
/review stakeholders
/review hypotheses — focus on anything close to a decision trigger
```

## Workflow

### Step 1: Run the Sweep

Apply the **memory-review** skill:

- All six checks: stale knowledge, stale evidence, hypothesis hygiene, stakeholder cadence + strategy tension, knowledge compression, archival
- Narrow depth to the focus area if one was given, but don't skip the other checks entirely unless explicitly asked to

### Step 2: Save and Surface

Save the report to `maintenance/<date>-review.md`. Lead the response with the priority actions, not a wall of six equally-weighted sections.

### Step 3: Offer Next Steps

- If any strategy tension was flagged: "Want me to run `/strategy-check` on that decision?"
- If a hypothesis trigger looks close: "Want me to check whether `/decide` is warranted here?"
- If stakeholders came up stale: "Want to `/prep` for a check-in with any of them?"

## Notes

- Run this on a regular cadence (weekly is typical) — skipping it for a month is how memory stops being trustworthy.
- A clean check ("nothing stale") is reported as such — never padded with manufactured findings.
