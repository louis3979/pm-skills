---
description: Write a full PRD from a raw idea or workflow description, with an adversarial review pass before it's considered done
argument-hint: "<feature idea, problem statement, or raw workflow description>"
---

# /write-prd -- PRD Writing Pass

Turn a raw idea or workflow description into an implementation-ready PRD, then stress-test it before calling it done.

## Invocation

```
/write-prd SSO support for enterprise customers
/write-prd Stores request stock from central warehouse; warehouse approves or rejects; on approval a transfer note is created
/write-prd [paste a brief, research doc, or feature request]
```

## Workflow

### Step 1: Understand the Ask

Accept the input in any form — a feature name, a problem statement, a rough workflow, or an uploaded brief. Ask conversationally for anything critical that's missing: the target user, why now, and any known constraints.

### Step 2: Formalize the Workflow (if needed)

If the input describes a multi-actor, multi-state business workflow that isn't yet unambiguous, apply the **business-process-modeler** skill first to produce actors, process flow, state machine, and a permission matrix — then feed that into Step 3 instead of re-deriving it.

### Step 3: Write the PRD

Apply the **prd-writer** skill to produce the full PRD: problem, goals/non-goals, scope, user flow, business rules, permissions, state transitions, edge cases, requirements, acceptance criteria, analytics tracking, dependencies, risks, and open questions.

### Step 4: Adversarial Review

Apply the **requirement-analyzer** skill against the draft: find missing requirements, conflicts, ambiguity, invalid assumptions, undefined ownership, and missing permission/state/rollback cases. Fix any Blocker-severity findings before proceeding.

### Step 5: Finalize Acceptance Criteria

If the PRD's acceptance criteria need to be more exhaustive than the first draft, apply the **acceptance-criteria-generator** skill for a dedicated pass (happy path, negative path, permission cases, state cases).

Save the final PRD as markdown.

### Step 6: Offer Next Steps

- "Want me to **break this into user stories** for engineering (`user-story-writer`)?"
- "Should I **translate this into technical impact areas** (`/prep-technical-handoff`)?"
- "Want me to **plan the delivery** (scope/schedule/risk) for this (`/plan-delivery-risk`)?"

## Notes

- Don't skip Step 4 — a PRD that hasn't been adversarially reviewed routinely ships with a gap that becomes an expensive mid-sprint surprise.
- If the idea is too big for one PRD, say so and propose phasing rather than writing one sprawling document.
- Non-goals are as important as goals — always include them explicitly, with a reason.
