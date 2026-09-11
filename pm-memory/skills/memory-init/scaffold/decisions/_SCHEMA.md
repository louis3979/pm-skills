# Decision entry schema

One file per decision at `decisions/<date>-<slug>.md`.

```markdown
# [Decision title]

**Status**: pending / decided
**Date**: [date]
**Driver**: [what triggered this — a hypothesis crossing its decision trigger, an operator ask, a stakeholder request]

**What we're deciding**: [concrete, unambiguous]

**What would reverse this**: [explicit condition]

**Evidence trail**:
- [hypothesis/knowledge/ingestion link, or provenance tag]
```

**Discipline**: this skill/system drafts decisions as `pending` only. A decision becomes `decided` when the operator explicitly says so — never inferred from silence or from the agent's own confidence.
