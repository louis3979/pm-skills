---
name: advanced-elicitation
description: "Pressure-test and refine the most recent draft/decision/plan using a menu of named critique techniques (Socratic questioning, first principles, pre-mortem, red team, five whys, and more), applying only the ones the user picks. Use when a draft needs deeper scrutiny before being finalized, or the user names a specific critique method."
---

# Advanced Elicitation

## Purpose

You are the shared refinement checkpoint for $ARGUMENTS — the most recent piece of work in the conversation (a PRD section, a strategy, a decision memo, a plan) — offering a short menu of critique techniques and applying only the ones chosen, so refinement is deliberate and visible rather than a vague "make it better."

## Context

Use this at a natural pause after any skill produces a draft, or whenever the user asks for a deeper critique or names a specific method ("run a pre-mortem on this," "red-team this decision"). It targets the most recent output unless the user points at something else.

## Technique menu

Offer 4-5 techniques picked to fit the target (don't dump the whole list) — e.g. risk-heavy techniques before a launch decision, collaborative ones when stakeholders disagree, structural ones for a technical plan:

- **Socratic Questioning** — a chain of "why do we believe that" questions on the target's core claims, exposing which are actually load-bearing.
- **First Principles** — strip the plan/decision to its bedrock facts, check whether the current approach is actually the one that follows, or just the familiar one.
- **Pre-mortem** — imagine this has failed in 6 months; work backward to what caused it. (Complements `product-qa-reviewer`/`risk-register-manager` for concrete follow-through.)
- **Red Team** — argue against the target as convincingly as possible, as if trying to kill it, then see what survives.
- **Five Whys** — chain "why" five times on the stated problem/goal to check it's not solving a symptom.
- **Assumption Reversal** — list every assumption the target rests on, flip each, and check if the conclusion still holds.
- **Six Thinking Hats** — pass over the target six times: facts, feelings/gut reaction, benefits, risks, alternatives, and process/next-steps.
- **Alternative POV** — argue the case from a stakeholder who'd naturally oppose this (finance, a skeptical customer, the on-call engineer who has to support it).
- **Steelman the Alternative** — construct the strongest possible case for the option that was NOT chosen, then see if the original choice still wins.

## Instructions

1. **Fix the target**: the most recent output, or whatever the user points at.
2. **Offer the menu**: 4-5 techniques by name, matched to the target, plus the options **Reshuffle** (different 4-5), **List all**, or **Proceed** (no further elicitation).
3. **Run chosen technique(s)** against the CURRENT version of the target (if multiple methods are run, each builds on the last one's result, not the original) — show what the method revealed and the specific changes it proposes.
4. **Halt for a decision on every proposal**: Apply / Reject / give different direction. Never change the work unless the user accepts — this is not an automatic rewrite.
5. **After applying or rejecting, offer the menu again** until the user chooses Proceed.
6. **On Proceed**: hand back the current (possibly refined) version as the final replacement for what the invoking work had, clearly noting what changed and why.

## Output

No separate document — this skill edits the target in place (the draft/decision/plan already being worked on) and reports:

```markdown
## Elicitation pass: [technique(s) run]

**What it revealed**: ...

**Proposed change**: ...
**Applied?**: [yes/no/modified per user direction]
```

## Notes

- Never silently rewrite the target without the user accepting the specific proposal — the halt-and-choose loop is the point, not a formality to skip.
- Scale depth to the target: a paragraph gets a light pass, a launch decision or architecture-level plan gets the full treatment.
- If a technique's application would just restate what's already known/settled, say so and suggest a different technique rather than manufacturing a proposal for the sake of it.
- Pairs naturally with `party-mode-debate` when the critique benefits from several distinct voices arguing at once rather than one technique applied linearly.

## Example

Input: a draft decision to defer a feature to next quarter. Technique chosen: Pre-mortem. Reveals: the stated reason (low confidence) doesn't address the sales team's already-promised commitment to two enterprise deals contingent on this feature. Proposed change: add an explicit risk section naming the sales commitment and a mitigation (renegotiate the commitment date) before the decision is finalized. User applies it.
