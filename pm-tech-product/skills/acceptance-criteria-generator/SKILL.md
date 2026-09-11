---
name: acceptance-criteria-generator
description: "Generate Given/When/Then acceptance criteria covering happy path, negative path, permission cases, and state cases for a feature or user story. Use when criteria need to be exhaustive and testable, standalone or as a focused pass on an existing PRD/story."
---

# Acceptance Criteria Generator

## Purpose

You are generating testable, exhaustive acceptance criteria for $ARGUMENTS, so QA and engineering have an unambiguous definition of done instead of a vague "should work correctly."

## Context

Use this standalone for a specific feature/story, or as a dedicated pass on an existing `prd-writer` or `user-story-writer` output when its acceptance criteria need to be more exhaustive than a first draft provided.

## Instructions

1. **Confirm the feature/story scope** before generating criteria — criteria generated against an unclear scope will be wrong in ways that look plausible.
2. **Write Happy Path criteria**: the primary successful flow, in Given/When/Then form, specific enough to be a pass/fail test (never "the system works correctly").
3. **Write Negative Path criteria**: invalid input, failed preconditions, and error states — what should visibly happen, not just "an error is shown."
4. **Write Permission Cases**: for every role that can and cannot perform this action, an explicit criterion.
5. **Write State Cases**: for a stateful entity, criteria covering entry into this feature from each relevant prior state, and what happens if the state changes underneath the action (use `state-machine-designer` output if it exists).
6. **Write Boundary/Concurrency Cases** where relevant: empty data, maximum data, two actors acting at once.
7. **Check every criterion is independently testable** — a criterion that depends on another criterion having already run should be split or made explicit about its precondition.

## Output

```markdown
# Acceptance Criteria — [feature/story name]

## Happy Path
- Given ... When ... Then ...

## Negative Path
- Given ... When ... Then ...

## Permission Cases
- Given [role] ... When ... Then [allowed/denied] ...

## State Cases
- Given [entity in state X] ... When ... Then ...

## Boundary / Concurrency Cases
- Given ... When ... Then ...
```

Save as a markdown document, or fold directly into the PRD/story it belongs to.

## Notes

- Every criterion must be a concrete, checkable pass/fail statement — "fast," "intuitive," "correctly" are not acceptable predicates without a number or explicit behavior attached.
- If permission rules or the state machine aren't defined yet, generating permission/state criteria will just be guessing — flag the dependency and request that input first rather than inventing plausible-sounding rules.
- Negative-path and permission criteria are usually under-specified relative to happy-path — deliberately check you have at least as many of those as happy-path criteria for anything with real complexity.

## Example

Input: "Approve a stock request." Output (excerpt): Given a request in Submitted state, When a Central Warehouse user approves it with sufficient stock available, Then the request moves to Approved and a transfer note is created within the same transaction. Given the same request, When a Store user (not Central Warehouse) attempts to approve it, Then the action is denied and no state change occurs.
