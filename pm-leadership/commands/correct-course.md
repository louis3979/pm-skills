---
description: Assess a significant unexpected disruption mid-delivery and produce a structured change proposal
argument-hint: "<the triggering issue and the initiative it affects>"
---

# /correct-course -- Course Correction

Turn a mid-delivery disruption into a structured continue/adjust/pivot/stop proposal with a clear recommendation, instead of an ad hoc scramble.

## Invocation

```
/correct-course Our third-party data provider is shutting down in 60 days, mid-Q2 roadmap
/correct-course [describe what happened and what plan it affects]
```

## Workflow

### Step 1: Name the Trigger

Confirm what happened, when it was discovered, and how it differs from the current plan's assumptions.

### Step 2: Run the Assessment

Apply the **course-correction-planner** skill: impact across scope/schedule/team, flag any prior decisions resting on the now-invalid assumption, generate all four option types (Continue/Adjust/Pivot/Stop), recommend one with reasoning, name the decision owner and deadline.

Save the output as markdown.

### Step 3: Offer Next Steps

- "Want me to **formally revisit the affected decision** (`decide` / `memory-decide` if project memory is in use)?"
- "Should I **map who needs to hear about this first** (`stakeholder-power-interest-mapper`)?"
- "Want me to **update the schedule/critical path** for the new plan (`schedule-critical-path-analyzer`)?"

## Notes

- Always address all four option types, even when one clearly wins — skipping "Continue" or "Stop" makes the proposal look like it didn't consider the full range.
- This is triage for a real disruption, not the path for a routine planned scope-change request — use `change-control-manager` for that instead.
