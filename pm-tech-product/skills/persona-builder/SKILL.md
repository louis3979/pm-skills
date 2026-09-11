---
name: persona-builder
description: "Build an evidence-based user persona from research/interview data — role, goals, pain points, workflow, decision authority. Use when the team relies on assumed or outdated personas and needs one grounded in actual evidence."
---

# Persona Builder

## Purpose

You are a researcher building a persona for $ARGUMENTS strictly from evidence, refusing to fill gaps with convenient assumptions. The output should reflect what has actually been observed about this user segment, so downstream PRD, UX, and JTBD work stands on a grounded model instead of a stereotype.

## Context

Personas built from internal assumptions quietly poison every decision downstream. The discipline here is refusing to publish an attribute that can't be traced to a real source — and marking clearly what's still unknown.

## Instructions

1. **Confirm evidence sufficiency before starting.** If the only input is internal opinion with no real user data behind it, say so and recommend the minimum research needed first (e.g. 5 interviews) rather than building an assumption-dressed-as-evidence persona.
2. **Extract Role & Responsibilities** from evidence directly — not inferred from a job title alone.
3. **Extract Goals** in the user's own terms where possible; use direct quotes if available.
4. **Extract Pain Points**, each tied to its source — don't generalize beyond what the evidence actually supports.
5. **Extract Workflow**: how this person gets the job done today, including tools/workarounds already in use.
6. **Extract Decision Authority**: decide / influence / use only. This matters for any go-to-market or stakeholder work built on this persona later.
7. **Define Success Criteria** in language that maps to something measurable where possible.
8. **Tag every attribute with its evidence source.** An attribute with no traceable source is a guess, not a finding — label it "Assumption — needs validation" explicitly rather than presenting it as confirmed.
9. If evidence sources conflict (e.g. two interviewees describe very different workflows), do not blend them into one persona — split into two, or state the variance explicitly.

## Output

```
## Persona: [role name]

**Role & Responsibilities**: [sourced description]

**Goals**:
- ...

**Pain Points**:
- [pain point] (source: [source])

**Workflow**: [how they get the job done today]

**Decision Authority**: [decide / influence / use only]

**Success Criteria**:
- ...

**Evidence Sources**:
| Attribute | Source |
|-----------|--------|

**Assumptions Needing Validation**:
- [anything filled in without a traceable source]
```

Save as a markdown document.

## Notes

- Never present an unsourced attribute as confirmed — a persona doc where claims can't be traced back is indistinguishable from a guess.
- A partial persona with explicit "Unknown — needs research" gaps is more useful than a complete one padded with invented detail.
- Feed the finished persona into JTBD framing or UX/design brief work so that work stays grounded in the same evidence.
