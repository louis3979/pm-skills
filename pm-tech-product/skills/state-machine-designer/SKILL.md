---
name: state-machine-designer
description: "Design a complete state machine for any stateful entity (order, transfer, payment, request, ticket, approval) — states, allowed transitions, actor per transition, conditions, side effects, and illegal transitions. Use when an entity's lifecycle needs to be unambiguous before implementation."
---

# State Machine Designer

## Purpose

You are formalizing the lifecycle of an entity in $ARGUMENTS into an explicit state machine, so "what happens next" and "what's not allowed" are both answered precisely instead of left to be discovered during implementation or QA.

## Context

Use this standalone for any single entity whose lifecycle needs precision (a payment, a ticket, an approval), or as a focused sub-step within `prd-writer`/`business-process-modeler` when a full process model isn't otherwise needed.

## Instructions

1. **List every State** the entity can be in, using names that are unambiguous and specific (not generic "in progress").
2. **Define Allowed Transitions**: for every state, which states it can move to — and just as important, which it explicitly cannot.
3. **Assign the Actor** who triggers each transition — a system/automated transition (e.g. timeout) is still an "actor" and must be named as such.
4. **Define Conditions** that gate each transition (reuse `business-rule-designer` output if it exists).
5. **Define Side Effects** of each transition — what else changes in the system when this transition happens (a notification sent, a downstream record created, a balance updated).
6. **Enumerate Illegal Transitions explicitly** — don't just omit them; state them, since "this transition is not possible" is information engineering needs as much as what is possible.
7. **Check for dead ends and unreachable states**: does every non-terminal state have at least one way forward? Is every state reachable from the initial state? Flag any that aren't.
8. **Check for concurrency**: can two transitions race on the same entity (e.g. two approvals at once)? If so, state the resolution (locking, last-write-wins, first-write-wins) explicitly rather than leaving it undefined.

## Output

```markdown
# State Machine — [entity name]

## States
- ...

## Transition Table
| From | To | Actor | Condition | Side Effects |
|---|---|---|---|---|

## Illegal Transitions (explicit)
- [From] → [To]: not allowed because ...

## Reachability Check
[every state reachable? every non-terminal state has a way forward?]

## Concurrency Handling
[what happens if two transitions race on the same entity]
```

Save as a markdown document.

## Notes

- A state machine with no illegal-transitions section is incomplete — always state what's explicitly disallowed, not just what's allowed.
- Terminal states (e.g. Completed, Cancelled) should never have outgoing transitions back into an active state — if a "reopen" flow is needed, model it as a new entity or an explicit new state, not a transition backward into the original lifecycle.
- If concurrency handling isn't decided yet, say so as an open question rather than silently picking a resolution strategy.

## Example

Input: "Design the state machine for a stock transfer." Output (excerpt): States — Draft → Submitted → Approved/Rejected → (if Approved) In Transit → Received → Completed, plus Cancelled (from Draft/Submitted only). Illegal: Rejected → Approved (must resubmit as a new request). Concurrency: two approvals racing on the same Submitted request resolved via optimistic locking with a `version` field.
