# Stakeholder file schema

Copy this structure for a new file at `stakeholders/<slug>.md`.

```markdown
# [Name]

- **Role**: [title/relationship to this initiative]
- **Influence**: [High/Medium/Low] — **Interest**: [High/Medium/Low]
- **Cadence**: expected touch every [N weeks]

## Open asks
- [ask] — raised [date], status: [open/resolved]

## Last unresolved concern
[what they last pushed back on or worried about, and whether it's been addressed]

## Touchpoints
- [date]: [what happened — meeting/interview/ad-hoc]. [link to ingestion record if one exists].
```

**Fields `/review` checks**: last touchpoint date (flags if stale relative to stated cadence), any open ask older than the cadence window with no update.
