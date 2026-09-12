---
name: party-mode-debate
description: "Simulate a roundtable of 3-5 distinct, disagreeing personas debating a decision or topic in character, surfacing real tension instead of one voice narrating every side. Use when a decision would benefit from being pressure-tested from several genuinely opposed angles at once, not resolved into false consensus."
---

# Party Mode Debate

## Purpose

You are running a simulated roundtable on $ARGUMENTS — voicing 3-5 distinct personas who actually disagree with each other, so the collision of perspectives surfaces an angle no single viewpoint (including your own default one) would reach alone.

## Context

Use this when a decision/topic has real, legitimate tension between perspectives (e.g. growth vs. trust, speed vs. quality, a customer ask vs. engineering cost) and hearing them argue is more useful than one synthesized recommendation. Complements `head-of-product-copilot` (which routes to specialist skills and synthesizes one answer) and `advanced-elicitation` (one technique applied linearly) — this is deliberately about live, unresolved disagreement between distinct voices, in one self-contained pass (not a persistent multi-agent session).

## Instructions

1. **Cast 3-5 personas** genuinely suited to the topic's real tensions — not generic yes-men. Give each a one-line identity with a real point of view and something specific they'd push for (e.g. not "a skeptic" but "the CFO who won't approve anything without payback under 18 months and says so immediately"). Typical useful casts: a customer advocate, an engineer who has to build/support it, a finance/business-viability voice, a skeptic who assumes the plan is wrong until proven otherwise, a growth-focused voice who wants to move fast.
2. **Voice the roundtable as a real conversation**: short turns, direct exchanges, each persona reacting to what the last one said — not a sequence of independent position statements. Format each turn as `**[Persona name]:** ...`.
3. **Let them actually disagree.** Do not soften positions into agreement or wrap the conversation up in a tidy consensus — the value is in the unresolved tension being visible. If two personas would genuinely clash, let them clash.
4. **Keep every voice distinct and consistent** — the same persona shouldn't drift into arguing someone else's point partway through.
5. **Pull out the substance, not just the performance**: after the roundtable runs its course, extract the real disagreements and any genuinely new angle that emerged from the collision (something none of the individual positions would have surfaced alone).
6. **Do not force a resolution** the roundtable itself didn't reach — if the personas end in real disagreement, say so and name what would need to be true to resolve it, rather than picking a winner yourself. If the operator wants a recommendation despite the disagreement, that's a separate step (hand off to `decision-memo` or `head-of-product-copilot`), not something this skill does automatically.

## Output

```markdown
# Party Mode: [topic]

## Cast
- **[Persona]** — [one-line identity and stance]

## Roundtable

**[Persona A]:** ...
**[Persona B]:** ...
...

## What the collision surfaced
[the real tension(s) that emerged, and any angle none of the individual voices would have reached alone]

## Unresolved (if any)
[what's still genuinely contested, and what would need to be true to settle it]
```

Save as a markdown document if the operator wants a record; otherwise this can run inline in conversation.

## Notes

- A roundtable where everyone politely agrees by the third turn has failed at its one job — push for real friction where the topic warrants it.
- Distinct voices, not distinct topics — every persona should be reacting to the same live conversation, not delivering a separate memo in sequence.
- If the operator wants a decided recommendation, not just the debate, say so plainly and hand off to `decision-memo` afterward rather than quietly picking a side mid-roundtable.

## Example

Input: "Should we ship the AI-generated summary feature with no human review step?" Cast: Growth PM (wants to ship fast, cites competitor pressure), Trust & Safety voice (won't accept unreviewed AI output reaching customers), Engineer (flags review-queue infra doesn't exist yet, would take 3 weeks), Customer Advocate (customers explicitly asked for speed over perfection in recent interviews). Roundtable surfaces a middle path neither the Growth PM nor the Trust & Safety voice proposed alone: ship with a confidence-score gate — low-confidence summaries queue for review, high-confidence ship immediately. Unresolved: what confidence threshold is safe enough — flagged as needing actual data, not a debate-table guess.
