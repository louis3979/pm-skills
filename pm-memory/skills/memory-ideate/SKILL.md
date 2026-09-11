---
name: memory-ideate
description: "Generate 3-7 solution directions for a problem/opportunity area, each grounded in the project's actual knowledge/insights/hypotheses rather than generic brainstorming. Use when exploring how to address a known problem, not for validating whether the problem is real."
---

# Memory Ideate

## Purpose

You are generating solution directions for $ARGUMENTS grounded in what the operator's project memory actually knows — not a generic brainstorm, a set of candidates each traceable to a real insight, hypothesis, or decision already on file.

## Context

Use this once a problem/opportunity is already established (from `knowledge/`, prior `hypotheses/`, or an explicit ask) and the question is "what could we do about this." If the problem itself isn't validated yet, that's a discovery/research question, not an ideation one — ideation on an unvalidated problem just produces well-organized guesses.

## Instructions

1. **Load grounding context**: the relevant strategy/priorities, any `knowledge/users` insights touching this area, related `hypotheses/` (especially ones with real evidence), and recent `decisions/` that already touched this space (don't propose something already explicitly rejected without noting the prior decision).
2. **Generate 3-7 directions** — enough for real option coverage, not padded to hit a number. Each direction gets a name and a one-paragraph description.
3. **Tag every direction with its grounding** — a specific insight, hypothesis, or decision it's based on, using the evidence provenance format: a path-link to a real memory-system file when one exists, or an honest non-path tag (`(intuition, PM, <date>)`, `(industry-knowledge)`) when it's not literally backed by an artifact. Never present a direction as evidence-backed when it's actually a hunch.
4. **Explicitly label every direction "proposed"** — this skill never promotes a direction to a decision or a committed plan; that's `memory-decide`'s and `memory-plan`'s job.
5. **Name the validation step** each direction would need before being taken further (an interview, a prototype test, a data pull) — an idea with no stated next validation step isn't actionable yet.
6. **Flag directions that revisit a previously rejected decision** — don't silently re-propose something already decided against; if you do propose it, say explicitly why now might be different.

## Output

```markdown
## Ideation: [problem/opportunity area]

### Direction 1: [name]
[one paragraph]
**Grounded in**: [insight/hypothesis/decision link, or honest non-path tag]
**Status**: Proposed — not promoted
**Validation needed**: [specific next step]

### Direction 2: ...
...

### Directions revisiting a prior decision (if any)
- [direction] — previously decided against in [decision link] — why reconsider now: [...]
```

Save as a markdown document, or hand back directly if this is a quick exploratory pass.

## Notes

- Never present an ungrounded direction as if it were evidence-backed — an honest `(intuition, PM, <date>)` tag is fine; a fabricated citation is not.
- "Proposed" means proposed — this skill does not decide anything; hand the chosen direction to `memory-plan` or `memory-hypothesize` for the next step.
- If memory genuinely has thin grounding for this area, say so and lead with that gap rather than papering over it with generic directions.

## Example

Input: "Reduce support ticket volume for password resets." Direction: "Self-service reset via SMS OTP" — grounded in `knowledge/users.md` note that 60% of reset tickets come from users without email access on mobile; validation needed: confirm SMS delivery reliability in target markets before committing.
