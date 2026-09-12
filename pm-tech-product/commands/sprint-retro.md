---
description: Run a lightweight recurring sprint retrospective with owned action items
argument-hint: "<sprint identifier and raw input from the team>"
---

# /sprint-retro -- Sprint Retrospective

Turn a sprint's raw impressions into a short, honest retro with action items that actually get followed up on.

## Invocation

```
/sprint-retro Sprint 14 — API integration slipped, new PR review process worked well
/sprint-retro [paste team notes/impressions from the sprint]
```

## Workflow

### Step 1: Gather Input

Ask if not already clear: what happened this sprint (scope completed/incomplete, blockers, process friction, wins worth naming).

### Step 2: Run the Retro

Apply the **sprint-retrospective** skill: check previous action items first, sort input into Went Well / Didn't Go Well / Puzzling, generate action items from patterns (not every complaint), each with an owner and a deadline small enough to actually happen next sprint.

Save the output as markdown.

### Step 3: Offer Next Steps

- "Want me to **plan next sprint** against these action items (`sprint-planner`)?"
- "Should I **track this as a risk** if the same issue has repeated 2+ sprints running (`risk-register-manager`)?"

## Notes

- Keep it to 20-30 minutes of substance — this isn't a status report on what shipped.
- A repeated, never-resolved action item is the single most important finding in the retro — call it out directly.
