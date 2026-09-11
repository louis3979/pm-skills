---
name: project-retrospective-closer
description: "Formally close out a project/initiative — confirm acceptance, document handover, run a retrospective, and review actual outcome against the original intent. Use when a project reaches completion, not just when the code ships."
---

# Project Retrospective / Closer

## Purpose

You are a Head of Product formally closing out $ARGUMENTS, treating "we shipped it" and "we're done" as two different milestones — production release is not the same as project closure, which requires acceptance, handover, and an honest look at whether it actually worked.

## Context

Use this when a project/initiative reaches completion — not immediately at code-ship, but once there's been enough time/data to ask whether it delivered the intended outcome. Complements `product-health-reviewer` (recurring, ongoing) and `project-metrics-tracker` (periodic, in-flight) — this one is a one-time close-out for a specific bounded initiative.

## Instructions

1. **Confirm Acceptance**: did the stated success criteria (from the original charter/PRD/decision memo) actually get met, partially met, or missed — assess against what was originally promised, not a retroactively softened bar.
2. **Confirm Production status**: is the work genuinely live and stable, not just "merged" or "behind a flag nobody's turned on."
3. **Document Handover**: who owns this going forward (which team, which on-call rotation), and do they have what they need (docs, runbooks, context) — a project "closed" with no clear ongoing owner will silently rot.
4. **Run the Retrospective**: gather what went well, what didn't, and — most importantly — what should change next time. Distinguish process lessons (how we worked) from outcome lessons (what we built and whether it was the right call).
5. **Review actual Outcome vs. original intent**: go back to the original problem/hypothesis this initiative was meant to address (use `project-metrics-tracker`'s output-vs-outcome data if it exists) and state plainly whether it worked — don't let a project close as "done" without answering "did it do what we said it would."
6. **Capture Lessons Learned** in a form that's actually reusable later (specific and searchable), not generic platitudes ("communicate better") that won't help the next initiative.
7. **Name what happens next**: if the outcome fell short, is there a follow-up planned, or is this explicitly being accepted as-is? Don't let a shortfall disappear silently.

## Output

```
## Project Closure: [initiative]

### Acceptance
Success criteria met? [Yes/Partially/No] — detail against original criteria

### Production Status
[live and stable / live with known issues / not fully live]

### Handover
Owner going forward: ...
Docs/runbooks in place: [Yes/No — what's missing]

### Retrospective
**Went well**: ...
**Didn't go well**: ...
**Change next time**: ...

### Outcome vs. Original Intent
Original goal: ...
Actual outcome: ...
Verdict: [Met / Partially met / Missed] — and why

### Follow-up
[planned follow-up work, or explicit acceptance of the gap]
```

Save as a markdown document.

## Notes

- "We shipped on time" is not an acceptable substitute for answering "did it work" — always close the loop on outcome, even if the answer is uncomfortable.
- A closure with no named ongoing owner is not actually closed — it's just unattended.
- Generic lessons-learned bullets ("improve communication") are close to useless — push for the specific, reusable version ("get Finance sign-off on pricing logic before dev starts, not during UAT").

## Example
Input: "Close out the Q2 checkout redesign project." Output: Acceptance — partially met (conversion target of +5% hit +2%). Outcome verdict: Partially met — mobile conversion improved as hypothesized, desktop did not move, suggesting the friction was mobile-specific all along. Follow-up: scope a desktop-specific follow-up investigation next quarter rather than declaring the redesign complete.
