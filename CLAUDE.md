# CLAUDE.md

Guidance for AI agents working in this repository.

## Project Overview

**pm-skills** — a marketplace of 3 independent plugins (34 skills, 9 commands) for Head-of-Product work: ERP/retail/inventory domain intelligence, enterprise requirements rigor, and Head-of-Product leadership workflows.

## Repo Structure

```
pm-skills/
├── .claude-plugin/marketplace.json   <- root marketplace manifest (lists all 3 plugins)
├── LICENSE                           <- MIT
├── README.md                         <- public documentation
└── pm-{name}/                        <- plugin directories
    ├── .claude-plugin/plugin.json    <- per-plugin manifest
    ├── skills/{skill}/SKILL.md       <- one folder per skill
    ├── commands/{command}.md         <- one file per command
    └── README.md                     <- per-plugin documentation
```

## Key Design Rules

- **Skills = nouns/concepts.** Domain knowledge and frameworks Claude auto-loads when the topic matches.
- **Commands = verbs.** User-triggered workflows that chain one or more skills within the same plugin.
- **No cross-plugin references.** Commands suggest follow-ups in natural language only. Never hard-reference a command from another plugin — plugins install independently.
- **Frontmatter required:** Skills need `name` + `description`; commands need `description` + `argument-hint`.
- A skill's `name` **must match its directory name**.
- Skills can be force-loaded with `/plugin-name:skill-name` or `/skill-name`.
- Keep frontmatter lean (always loaded); put detail in the SKILL.md body (loaded when triggered).

## After any skill/command change

1. If skills/commands were added or removed, update the counts in `README.md` (headline + per-plugin summary line) and `marketplace.json`'s `description`.
2. Keep `marketplace.json` version and each `plugin.json` version in sync.
