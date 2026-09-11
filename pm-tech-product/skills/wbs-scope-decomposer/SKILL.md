---
name: wbs-scope-decomposer
description: "Break a large deliverable/epic into a Work Breakdown Structure — hierarchical, estimable, assignable, controllable pieces — with explicit in-scope, out-of-scope, deliverables, and acceptance criteria. Use before estimating, staffing, or scheduling a large piece of work."
---

# WBS / Scope Decomposer

## Purpose

You are a delivery-accountable PM decomposing $ARGUMENTS into a Work Breakdown Structure, so a large deliverable becomes a set of pieces small enough to estimate, assign, and track — instead of one opaque blob of "the project."

## Context

Use this before estimating, staffing, or scheduling anything large enough that "how long will this take" can't be answered with confidence in one shot. It's the structural step that `schedule-critical-path-analyzer` and `risk-register-manager` build on top of.

## Instructions

1. **State Scope boundaries first**: In-scope, Out-of-scope, and — critically — the reason each Out-of-scope item is excluded (deferred to later phase, someone else's responsibility, deliberately descoped for this release).
2. **Decompose hierarchically**, top-down: deliverable → major components → sub-components → work packages. Stop decomposing once a leaf node is small enough that one person/small group can estimate and own it with confidence (the "8/80 rule" heuristic: roughly 1-10 days of work per leaf, adjust to the team's actual cadence).
3. **Every leaf node is a noun** (a deliverable/component), not a verb (a task/activity) — "Stock Transfer API" is a WBS leaf; "build the API" is an activity that belongs to schedule/activity planning, a separate (later) step.
4. **Attach Deliverables and Acceptance Criteria** to each meaningful node — what does "done" look like, concretely, for this piece.
5. **Check for completeness**: does the full tree, summed up, actually cover 100% of the stated in-scope work? A WBS with implicit gaps (functionality nobody's node covers) is worse than a WBS that's simply detailed — check explicitly rather than assuming coverage.
6. **Flag ambiguous ownership**: any leaf node that could plausibly belong to more than one team/component, or none, needs to be resolved before estimation — don't let it stay ambiguous and get silently dropped or duplicated.

## Output

```
## WBS: [deliverable/epic name]

### In-scope
- ...
### Out-of-scope (with reason)
- ...

### Work Breakdown Structure
[deliverable name]
├── [major component]
│   ├── [sub-component / work package] — Deliverable: ... | Acceptance: ...
│   └── ...
└── [major component]
    └── ...

### Coverage Check
[confirm the tree sums to 100% of in-scope work, or list the gap]

### Ambiguous Ownership Flags
- ...
```

Save as a markdown document.

## Notes

- Leaf nodes name deliverables/components, not activities — "Reporting Dashboard," not "Build the dashboard."
- If a leaf node still feels too large to estimate confidently, decompose it further rather than accepting a rough guess.
- Out-of-scope items without a stated reason will silently reappear as "wait, isn't this included?" later — always attach the reason.

## Example

Input: "Break down a new internal admin console for managing user accounts." Output (excerpt): In-scope — user CRUD, role assignment, activity log view. Out-of-scope — bulk import (reason: "phase 2, no immediate customer ask"). WBS leaf: "Role Assignment UI" — Deliverable: screen + API; Acceptance: "an admin can assign/revoke any defined role and see the change reflected within 5 seconds."
