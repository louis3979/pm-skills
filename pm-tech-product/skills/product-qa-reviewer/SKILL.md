---
name: product-qa-reviewer
description: "Generate adversarial test scenarios (happy path, negative path, boundary, permission, state, concurrency, data consistency) from a PRD. Use before or alongside QA test planning, not for slicing scope."
---

# Product QA Reviewer

## Purpose

You are acting as an adversarial test-case generator against the PRD for $ARGUMENTS, surfacing untested scenarios before they reach production by systematically generating test cases across categories that are easy to forget under deadline pressure.

## Context

Run this once a PRD exists, before or alongside QA test planning, to make sure coverage isn't limited to the happy path. It doesn't slice a PRD into implementable stories or critique its structure — it assumes scope is already settled and focuses purely on test coverage.

## Instructions

Generate cases across all 7 categories, marking any not applicable with a reason rather than skipping silently:

1. **Happy path** — the primary intended flow, end to end.
2. **Negative path** — invalid input, unauthorized attempts, malformed requests.
3. **Boundary cases** — empty states, maximum/minimum values, pagination edges, zero-quantity/zero-record scenarios.
4. **Permission cases** — every role explicitly allowed and explicitly denied for each action.
5. **State transition cases** — every valid and invalid transition implied by the feature, including an attempted illegal transition.
6. **Concurrency cases** — two actors acting on the same record simultaneously (two approvers, a cancel racing an approval).
7. **Data consistency cases** — what happens if related data changes mid-flow (stock quantity changing after submission but before approval, for example).

If the PRD doesn't define explicit states/permissions, don't silently skip categories 4-5 — flag that the PRD is missing what's needed and recommend defining the state machine or business rules first. Weight concurrency and data-consistency cases higher for any feature touching inventory, payments, or approvals — these cause the most real incidents in complex/ERP-style systems.

## Output

```
## QA Test Cases: [feature name]

**Happy Path**: [end-to-end primary flow]

**Negative Path**:
- [e.g. "Submit request with negative quantity — must be rejected with a clear error"]

**Boundary Cases**:
- [e.g. "Approve a request with quantity = 0"]

**Permission Cases**:
- [e.g. "Store staff attempts to approve their own request — must be denied"]

**State Transition Cases**:
- [e.g. "Attempt to approve an already-cancelled request — must be rejected"]

**Concurrency Cases**:
- [e.g. "Two approvers approve the same request simultaneously — must not create two transfer documents"]

**Data Consistency Cases**:
- [e.g. "Stock quantity changes after request submitted but before approval"]
```

Save as a markdown document.

## Notes

- Every permission case names the specific role; every state case references an actual defined state — no vague "a user" or "some state."
- Every concurrency case must describe two concrete simultaneous actors, not a generic "race condition."
- If a category can't be meaningfully generated due to missing PRD detail, say so rather than inventing a model that wasn't specified.
