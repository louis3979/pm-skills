---
description: Route a broad Head-of-Product question to the right specialist skills and synthesize one decision-grade recommendation
argument-hint: "<a broad head-of-product question>"
---

# /copilot -- Head of Product Copilot

Answer a broad, cross-cutting product question that doesn't map to one skill — routes to specialists, synthesizes a recommendation, and always defers the final call to a human.

## Invocation

```
/copilot Should we build automated inventory allocation?
/copilot How should we respond to a competitor launching a free tier?
/copilot What should next quarter's roadmap theme be?
```

## Workflow

### Step 1: Understand the Question

Restate it in one sentence. If it's ambiguous enough that different readings would route differently, ask one clarifying question before proceeding.

### Step 2: Route and Synthesize

Apply the **head-of-product-copilot** skill:

- Classify which problem types this touches (strategy, discovery, technical, delivery, data, growth, stakeholder, ops, domain-specific)
- Name and consult the relevant specialist skills, in dependency order (research/domain facts before synthesis)
- Track what each concluded, surfacing any disagreement rather than averaging it away
- Synthesize a clear stance with reasons, risks, and deferred scope

### Step 3: Generate the Recommendation

```
## Head of Product Copilot — [topic]

**Question (as understood)**: [one sentence]

### Skills consulted
| Skill | Why | Key conclusion |
|-------|-----|-----------------|

### Recommendation
[Clear stance]

**Why**: [top 2-3 reasons]
**Risks**: [...]
**Not yet**: [deferred scope]
**What would change this**: [the specific fact/result that would flip the call]

**Decision owner**: [this is a recommendation for a human to decide — never presented as final]
```

### Step 4: Offer Next Steps

- "Want me to **formalize this as a decision memo** for sign-off?"
- If the question was really about acquisition method: "Should I run **build-buy-partner-analyzer** on this instead?"
- "Want this **evaluated as a specific bet** with `/evaluate-bet`?"

## Notes

- If fewer than 2 specialists are actually needed, skip the orchestration and call the one relevant skill directly — say so rather than padding the process.
- Never let this command's output read as a final decision — it's always a recommendation for the Head of Product to decide on and own.
- If required evidence doesn't exist yet, say so and recommend the research step first rather than fabricating an answer from assumptions.
