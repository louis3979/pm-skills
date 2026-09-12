---
name: structured-brainstormer
description: "Run a structured divergent-then-convergent brainstorm on a problem using named techniques (SCAMPER, Five Whys, Reverse Brainstorming, First Principles, Six Thinking Hats, and more) instead of an unstructured list of ideas. Use when exploring a problem/opportunity wide-open, before narrowing to a direction with problem-validator or memory-ideate."
---

# Structured Brainstormer

## Purpose

You are facilitating a real divergent brainstorm on $ARGUMENTS, using named techniques deliberately rather than free-associating a list — different techniques surface genuinely different classes of ideas, and naming which one you're running keeps the session from collapsing into the same three obvious ideas restated five ways.

## Context

Use this for wide-open exploration before a direction is chosen — it deliberately does NOT require existing evidence (unlike `memory-ideate`, which grounds directions in accumulated project memory). Use `structured-brainstormer` to widen the field, then `problem-validator` or `memory-ideate`/`memory-hypothesize` to narrow and validate what came out of it.

## Technique menu

Offer the user a short menu (don't dump the whole list) picked to fit the problem — 4-5 techniques spanning at least two categories:

**Structured** (good for: feature ideas, scoping)
- **SCAMPER** — run the idea through 7 lenses: Substitute, Combine, Adapt, Modify, Put-to-other-use, Eliminate, Reverse.
- **Six Thinking Hats** — examine one at a time: facts, feelings, benefits, risks, new ideas, process.
- **Morphological Analysis** — list independent parameters, generate options per parameter, combine across them for untried configurations.

**Deep/Diagnostic** (good for: root-cause, strategy, unsticking)
- **Five Whys** — chain "why?" five times until you hit the root cause beneath the symptom.
- **First Principles Thinking** — strip every assumption to bedrock fact, rebuild from scratch.
- **Assumption Reversal** — list every assumption baked into the problem, flip each, rebuild on the inverted foundation.
- **Reverse Brainstorming** — generate ways to make it *fail*, then mine each failure mode for its inverse.
- **Question Storming** — generate only questions, zero answers, until the real problem worth solving comes into focus.

**Creative** (good for: novel angles, when stuck)
- **Analogical Thinking** — "this is like what?" — steal the solution pattern from a domain that already solved something structurally similar.
- **What-If Scenarios** — detonate one constraint at a time (unlimited budget, opposite is true, problem vanished) and chase what rushes in.
- **Forced Relationships** — grab two unrelated things at random, force a bridge between them until an idea falls out.

**Collaborative** (good for: group sessions, stakeholder buy-in)
- **Role Playing** — voice different stakeholders (user, engineer, finance, support) — what each wants, fears, and would demand of the idea.
- **Yes-And Building** — never negate; each new idea must accept and build on the last one.

## Instructions

1. **Confirm the topic and goal** — what problem/opportunity, and what "useful output" looks like (a feature list, a root cause, a strategic direction).
2. **Pick 4-5 techniques** spanning at least two categories above, matched to the goal (diagnostic goal → lean Deep; feature ideation → lean Structured/Creative). Name them before starting.
3. **Run each technique for real** — apply its actual mechanic, don't just label a generic idea list with a technique name. Aim to genuinely push past the first, obvious ideas; if a technique goes quiet fast, switch rather than forcing it.
4. **Log every idea as it's generated** — don't silently discard anything, even ones that look weak; weak ideas sometimes seed the next technique's breakthrough.
5. **Converge deliberately** — once diverged, pick ONE convergence method that fits (don't apply all of them):
   - **Affinity Clustering** — group into themes when there are many scattered ideas; name each cluster.
   - **Impact/Effort** — place each surviving idea on impact vs. effort; harvest high-impact/low-effort first.
   - **PMI (Plus/Minus/Interesting)** — pressure-test one strong candidate before committing.
   - **Forced Ranking / Dot Vote** — when you just need a ranked top-N, no ties.
   - **MoSCoW** — when scoping toward a build: Must/Should/Could/Won't-this-time.
6. **Synthesize**: 3-7 surviving directions, each tagged with which technique produced it and why it survived convergence.

## Output

```markdown
# Brainstorm: [topic]

## Goal
[what a useful outcome looks like]

## Techniques run
1. [technique] — [what it surfaced]
2. ...

## Raw ideas (all of them, not just survivors)
- [idea] ([technique])

## Convergence: [method used]
[the convergence pass and its result]

## Surviving directions
1. [direction] — from [technique], because [why it survived]
```

Save as a markdown document.

## Notes

- Naming the technique out loud is not decoration — it's what keeps the session from defaulting to the same instinct every time.
- Don't skip convergence — a pile of 40 raw ideas with no narrowing pass isn't a brainstorm output, it's a transcript.
- If the user wants a group/stakeholder session rather than a solo pass, lean on the Collaborative techniques (Role Playing pairs well with `pm-leadership`'s `party-mode-debate` if a fuller simulated debate is wanted instead).

## Example

Input: "Reduce onboarding drop-off." Techniques run: Five Whys (surfaces root cause: users abandon at the permissions-request step, not the tutorial itself as assumed), Reverse Brainstorming (generates "how to guarantee drop-off" → invert into "ask for the single riskiest permission last, not first"), SCAMPER (Eliminate: remove the permissions step from onboarding entirely, request it contextually on first use instead). Convergence: Impact/Effort — "contextual permission request" scores high impact/low effort, becomes the surviving direction.
