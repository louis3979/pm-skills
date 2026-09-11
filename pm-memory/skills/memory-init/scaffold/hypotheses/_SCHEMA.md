# Hypothesis entry schema

Group related hypotheses into one topic file (e.g. `hypotheses/onboarding.md`); each entry inside follows this shape.

```markdown
## H[N]. [Short statement of the belief]

**Status**: proposed / active / promoted / resolved
**Confidence**: [0.0-1.0]

**Evidence for:**
- [claim] — [provenance tag or ingestion/source link]

**Evidence against:**
- [claim] — [provenance tag or ingestion/source link]

**Decision trigger**: [the explicit condition that would convert this into a decision — e.g. "if confidence > 0.8 across 5+ independent observations"]

**History**: [date] confidence [old] → [new], reason: [what changed it]
```

**Provenance tag vocabulary**: a path link into `ingestion/`/`source/`/`knowledge/` when a real artifact exists, otherwise one of `(stakeholder-verbal, <name>, <date>)`, `(intuition, PM, <date>)`, `(industry-knowledge)`, `(chat, no artifact)`.
