---
name: product-prioritizer
description: "Score and rank a backlog using RICE, ICE, WSJF, Impact/Effort, MoSCoW, or Kano — accounting for dependency, strategic fit, risk, sequencing, tech debt, and opportunity cost, not just the raw score. Use when multiple initiatives compete for the same limited capacity."
---

# Product Prioritizer

## Purpose

You are ranking competing initiatives in $ARGUMENTS into Do Now / Do Next / Do Later / Don't Do, using a scoring framework as a forcing function for explicit trade-offs — not as a substitute for judgment about dependency, risk, and strategic fit.

## Context

Use this when 5+ initiatives compete for the same capacity and a defensible, explainable ranking is needed instead of prioritizing by whoever argued loudest. Complements `roadmap-planner` (which sequences the result into time periods).

## Instructions

1. **Choose the right framework** for the situation: RICE (Reach × Impact × Confidence / Effort) for feature-level backlogs with estimable reach; ICE for early-stage/lower-data-availability contexts; WSJF when cost-of-delay reasoning matters (time-sensitive work); Impact/Effort for a quick visual pass; MoSCoW when stakeholder alignment on must-have vs. nice-to-have is the main problem; Kano when the question is delighter vs. basic-expectation vs. indifferent feature.
2. **Define the scoring scale explicitly before scoring** — don't let each item get scored against a different implicit bar.
3. **Score each initiative**, requiring a one-line rationale per score — a score with no rationale isn't trustworthy input to a ranking.
4. **Adjust for factors the raw score doesn't capture**: dependency (can this even be built before its prerequisite?), strategic fit (does it serve a stated strategic theme?), risk, sequencing, tech debt reduction, and opportunity cost of NOT doing something else.
5. **Sanity-check the ranking** against intuition — if the result is wildly counter to what an experienced PM would expect, look for a mis-scored input (usually Effort underestimated or Confidence overestimated) before trusting the output.
6. **Separate out Strategic Overrides**: anything that must be done regardless of score (compliance, contractual commitment) — flag and exclude from the main ranking so it doesn't distort other scores.
6a. **Handle items with no natural Reach/Impact** (pure tech debt, infra migrations, security hardening): don't force a fake user-facing score on them. List them in their own short section instead — what they unblock or protect against, and any initiative above whose score/risk they materially affect (e.g. an infra migration a top-ranked feature secretly depends on) — so they're visibly tracked without corrupting the scored ranking.
7. **Bucket into Do Now / Do Next / Do Later / Don't Do**, sized to actual near-term capacity, not just a sorted list with no cut lines.

## Output

```markdown
# Prioritization: [backlog/cycle], framework: [RICE/ICE/WSJF/etc.]

## Scoring Scale
[the scale definitions used for this pass]

## Ranked Initiatives
| # | Initiative | Score | Rationale | Dependency/Risk notes |
|---|---|---|---|---|

## Strategic Overrides (excluded from ranking)
| Initiative | Reason mandatory |
|---|---|

## Unscored: Tech Debt / Infra (no natural Reach/Impact)
| Initiative | What it unblocks/protects against | Affects which scored item(s) |
|---|---|---|

## Do Now
- ...
## Do Next
- ...
## Do Later
- ...
## Don't Do
- ...
```

Save as a markdown document.

## Notes

- Never present a ranking score without its rationale — an unexplained number invites re-litigation later with no way to resolve it.
- If the ranking surprises you, check Effort and Confidence first — those are the two inputs most often distorted by optimism.
- Do Now should fit real near-term capacity — an oversized Do Now bucket is not actually a prioritization, it's a wish list with a label.

## Example

Input: "Rank 8 backlog items using RICE, quarterly capacity ~3 major initiatives." Output: top-ranked item scores high on Reach and Impact with Effort of 1.5 person-months — Do Now. An item with a dependency on unscheduled platform work is flagged and moved to Do Later despite a decent raw score, with the dependency noted explicitly rather than silently dropped.
