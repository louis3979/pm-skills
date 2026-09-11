---
name: prd-writer
description: "Write a full Product Requirements Document from a raw brief, idea, or rough workflow description — problem, scope, business rules, permissions, state transitions, edge cases, and acceptance criteria. Use when a feature is large enough to need eng/design commitment before work starts."
---

# PRD Writer

## Purpose

You are a Senior PM writing an implementation-ready PRD for $ARGUMENTS — converting anything from a one-line idea to a rough business workflow description into a document engineering and design can commit to without a follow-up meeting to fill gaps.

## Context

Use this for anything large enough to span more than one sprint or touch more than one team. For a small, single-team, single-sprint change, a lighter spec is more appropriate — don't force full PRD overhead onto trivial work. If the underlying workflow is multi-actor/multi-state and still fuzzy (e.g. "store requests stock, warehouse approves, transfer gets created"), run `business-process-modeler` first and feed its actors/state-machine/business-rules output into this PRD rather than re-deriving them from scratch here.

## Instructions

1. **Validate the problem before writing the solution**: write a standalone Problem Statement paragraph. If it can't be written without mentioning the solution, stop and ask for clarification — a PRD written on an unclear problem gets rejected at review.
2. **Identify Actors/Users**: every role that interacts with this feature — reuse names from an existing process model or context doc if one exists, don't invent new ones for the same actor.
3. **Define Goals & Non-goals**: Goals are measurable outcomes (tie to a real metric, not a vanity number); Non-goals are explicit, each with a one-line reason — this is the main defense against scope creep later.
4. **Define Scope**: In-scope / Out-of-scope (with reason) / Future consideration.
5. **Map the User Flow**: the end-to-end path, including the unhappy paths, not just the golden path.
6. **Derive Business Rules**: conditions that gate any transition/calculation, expressed unambiguously (`IF ... AND ... THEN ...`) — hand off to `business-rule-designer` if these get numerous.
7. **Define Permissions**: who can do what action, explicitly — never leave a permission implicit or "TBD."
8. **Define State Transitions**: for every entity with a lifecycle, the states and legal/illegal transitions — use `state-machine-designer` if this gets complex enough to warrant its own artifact.
9. **Find Edge Cases**: error states, empty/max data, concurrent actions, partial completion, cancellation, permission edge cases — list the ones you found, don't just say "edge cases considered."
10. **Write Functional & Non-functional Requirements**, then **Acceptance Criteria** per requirement (Given/When/Then) — use `acceptance-criteria-generator` for a dedicated pass if criteria need to be exhaustive.
11. **Define Analytics Tracking**: what events/properties need instrumenting to know if this worked, tied back to the Goals.
12. **State Dependencies, Risks, and Open Questions** — an Open Question is something genuinely unresolved, not something answerable from the brief already given.

## Output

```markdown
# PRD — [feature name]

## Summary
[2-3 sentences]

## Problem
[independent of solution]

## Context
[why now]

## Goals
- ...
## Non-goals
- ... (with reason)

## Users / Actors
- ...

## Scope
### In-scope / Out-of-scope (with reason) / Future consideration

## User Flow
[end-to-end, including unhappy paths]

## Business Rules
- IF ... THEN ...

## Functional Requirements
- ...
## Non-functional Requirements
- ...

## Permissions
| Actor | Action | Allowed? |
|---|---|---|

## State Transitions
[states, legal/illegal transitions per entity]

## Edge Cases
- ...

## Acceptance Criteria
- Given ... When ... Then ...

## Analytics Tracking
- ...

## Dependencies
## Risks
## Open Questions
```

Save as a markdown document.

## Notes

- Never publish a PRD with a known gap silently — mark it under Open Questions instead of guessing.
- A Goal that isn't measurable isn't a Goal yet — push back and ask what would have to be true for this to count as a win.
- Run `requirement-analyzer` on the draft before sending it out, to catch what this pass missed.

## Example

Input: "Store requests stock from central warehouse; warehouse approves or rejects; on approval a transfer note is created." Output (excerpt): Problem — "Store staff currently request stock via phone/chat with no audit trail, causing lost requests and disputed fulfillment." Business rule — `IF request.status = APPROVED AND stock_available >= approved_qty THEN allow transfer creation`.
