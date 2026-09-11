---
name: user-story-writer
description: "Turn a PRD or epic into an Epic + User Stories + acceptance criteria + dependencies + Definition of Done. Use when a scoped requirement needs to become an implementable, assignable backlog."
---

# User Story Writer

## Purpose

You are converting a scoped requirement in $ARGUMENTS into an Epic broken into user stories that engineering can pick up directly — each one independently valuable, estimable, and testable.

## Context

Use this after scope is settled (from `prd-writer` or an existing epic description) — not to define requirements from scratch. For decomposing a larger deliverable into a full hierarchical breakdown with schedule implications, use `wbs-scope-decomposer` first; this skill is specifically about story-level backlog writing.

## Instructions

1. **State the Epic**: one clear statement of the overall capability being delivered and why it matters.
2. **Break into User Stories**: each in "As a [persona], I want [action], so that [benefit]" form — small enough to be completed and demoed independently (INVEST: Independent, Negotiable, Valuable, Estimable, Small, Testable).
3. **Order stories by dependency and value**: which must come first for later stories to make sense, and which delivers the most user-visible value soonest.
4. **Attach Acceptance Criteria per story** — use `acceptance-criteria-generator` for stories complex enough to need a dedicated pass, otherwise write 2-4 concrete Given/When/Then lines directly.
5. **Flag Dependencies between stories and on other teams/systems** explicitly — a story with an unstated dependency will get picked up out of order.
6. **Define the Definition of Done** for the epic as a whole — not just "all stories closed," but what must be true (tests passing, docs updated, feature flag configured, analytics verified) before the epic itself is considered complete.
7. **Check story sizing**: any story that can't be confidently estimated is too big or too vague — split it or flag it for more discovery before sprint planning.

## Output

```markdown
# Epic: [epic name]

## Epic Statement
[what and why]

## User Stories
| # | Story | Priority | Dependencies |
|---|---|---|---|

### Story 1: [title]
As a ..., I want ..., so that ...
**Acceptance Criteria**:
- Given ... When ... Then ...

## Definition of Done (Epic level)
- ...
```

Save as a markdown document.

## Notes

- A story with no clear persona benefit ("so that...") is probably a technical task disguised as a story — that's fine, just label it as a technical/enabler story rather than forcing a fake user benefit.
- Stories should be orderable into a sprint immediately — if a story still needs discovery before it can be estimated, say so rather than sizing it anyway.
- Hand the ordered story list to `sprint-planner` once capacity is known.

## Example

Input: Epic "Store stock request with warehouse approval." Output story: "As a store staff member, I want to submit a stock request with visible status, so that I don't lose track of it in a group chat." Dependencies: none (first story in the epic, unblocks the approval story).
