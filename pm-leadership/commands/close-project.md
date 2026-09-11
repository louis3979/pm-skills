---
description: Formally close out a completed initiative — retrospective, handover, and an honest outcome-vs-intent review
argument-hint: "<the initiative to close out>"
---

# /close-project -- Project Closure

Run a completed initiative through a proper close-out instead of letting "it shipped" quietly stand in for "we're done."

## Invocation

```
/close-project Q2 checkout redesign
/close-project The legacy auth migration
/close-project [describe the initiative and link its original goal/PRD]
```

## Workflow

### Step 1: Gather Context

Ask if not already clear:
- What was the original goal/success criteria (link the PRD, charter, or decision memo if one exists)?
- How long has it been live, and is there enough data yet to assess outcome?
- Who's involved in the retrospective (just you, or the full delivery team)?

### Step 2: Check Delivery Performance

Apply the **project-metrics-tracker** skill (if a delivery-performance history exists) to pull the output-vs-outcome data feeding into this closure.

### Step 3: Run the Closure

Apply the **project-retrospective-closer** skill:

- Confirm acceptance against original success criteria
- Confirm production status and handover ownership
- Run the retrospective (what went well / didn't / change next time)
- Review actual outcome vs. original intent and render a verdict

### Step 4: Consolidate the Closure Doc

Output the full closure document per the **project-retrospective-closer** skill's template.

Save as markdown.

### Step 5: Offer Next Steps

- "If the outcome fell short, want me to **scope a follow-up initiative**?"
- "Should I **update the stakeholder map** (`stakeholder-power-interest-mapper`) for whoever owns this going forward?"
- "Want a **board-level summary** of this closure (`pm-leadership:copilot`'s sibling `board-update` skill)?"

## Notes

- Don't run this the day something ships — wait until there's enough signal to actually assess outcome, or explicitly note that outcome is "not yet measurable" rather than guessing.
- A closure with no named follow-up owner for a shortfall is an unfinished closure — always name what happens next, even if it's "explicitly accepted, no follow-up planned."
