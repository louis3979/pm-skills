---
description: Simulate a roundtable of distinct, disagreeing personas debating a decision or topic
argument-hint: "<decision or topic to debate>"
---

# /party-mode -- Simulated Roundtable

Voice 3-5 distinct personas who genuinely disagree, debating a decision live, so the collision surfaces angles a single synthesized answer would miss.

## Invocation

```
/party-mode Should we ship the AI summary feature with no human review step?
/party-mode Growth vs. trust trade-off on the new referral program
```

## Workflow

### Step 1: Understand the Tension

Confirm the decision/topic and, if not obvious, what real perspectives are actually in tension here.

### Step 2: Run the Roundtable

Apply the **party-mode-debate** skill: cast 3-5 personas with genuine, specific stances; voice a real back-and-forth with actual disagreement; extract what the collision surfaced; name what's still unresolved.

### Step 3: Offer Next Steps

- "Want me to **turn this into a decision** now that the tensions are visible (`decision-memo`)?"
- "Should I **run a critique pass on the winning direction** (`/sharpen`)?"

## Notes

- A roundtable that politely agrees by the third turn has failed — push for real friction where the topic warrants it.
- This doesn't pick a winner on its own — if a decided recommendation is wanted, say so and hand off to `decision-memo` afterward.
