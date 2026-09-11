---
description: Formalize a raw business workflow into actors, states, and explicit rules before it becomes a PRD
argument-hint: "<raw business workflow description>"
---

# /model-business-process -- Formalize a Business Workflow

Turn a rough, verbal description of a multi-actor, multi-state business process into an unambiguous model — actors, flow, documents, state machine, permission matrix, and explicit business rules — ready to feed a PRD.

## Invocation

```
/model-business-process Store requests stock from central warehouse; warehouse approves or rejects; on approval a transfer note is created and shipped.
/model-business-process Customer submits a return request; support approves partial or full refund; refund posts to original payment method or store credit.
/model-business-process [upload a process doc, flowchart description, or old SOP]
```

## Workflow

### Step 1: Confirm the Problem Is Worth Modeling (optional)

If the underlying problem hasn't already been confirmed as real and painful, offer to apply the **problem-validator** skill first — a rough workflow idea based purely on a hunch is worth validating before investing in a full process model. Skip this step if the problem is already confirmed (e.g. a known, recurring operational process).

### Step 2: Model the Process

Apply the **business-process-modeler** skill:

- Identify every actor
- Draw the process flow
- Identify every document/record
- Design the state machine per document, including illegal transitions
- Enumerate exception flows (partial approval, cancellation, timeout, concurrent edits)
- Build the full permission matrix

### Step 3: Formalize the Business Rules

Apply the **business-rule-designer** skill to every conditional rule surfaced in Step 2:

- Convert each into an explicit IF/THEN statement
- Classify by type (validation, calculation, authorization, state transition, allocation, accounting)
- Flag conflicts, undefined fields, and vague quantifiers needing an explicit threshold

### Step 4: Consolidate

```
## Business Process Model: [process name]

[full process model from Step 2]

## Business Rules

[rule table from Step 3]

## Open Questions
[anything the source description left ambiguous]
```

Save as a markdown document.

### Step 5: Offer Next Steps

- "This process touches sensitive permissions — want me to **prep a technical handoff** with a security pass?"
- "Ready to **gate this for release** once it's built?"
- "Should I build a **persona** for the actor whose workflow this most affects?"

## Notes

- Don't invent behavior for gaps the source description left open — list them as open questions instead.
- A permission matrix with any blank cell isn't done — every actor × action combination must be marked explicitly.
- If two rules can fire on the same condition with contradictory outcomes, treat that as a blocker, not a footnote.
