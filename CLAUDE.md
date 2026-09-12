# CLAUDE.md

Guidance for AI agents working in this repository.

## Project Overview

**pm-skills** — a marketplace of 3 independent plugins (56 skills, 28 commands) for Head-of-Product work on technology/IT products: tech-product requirements/delivery rigor, Head-of-Product leadership workflows, and a markdown-native project memory system.

## Repo Structure

```
pm-skills/
├── .claude-plugin/marketplace.json   <- root marketplace manifest (lists all 3 plugins)
├── .github/workflows/validate.yml    <- CI: runs scripts/validate.py on every push/PR to main
├── scripts/validate.py               <- manifest/frontmatter/README-sync validator, no dependencies
├── CHANGELOG.md                      <- release source of truth
├── CONTRIBUTING.md                   <- how to add a skill/command, release process
├── SECURITY.md                       <- security policy
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

## Versioning & Releases

`CHANGELOG.md` is the source of truth — the newest `## vX.Y.Z — YYYY-MM-DD` heading is the current version. `marketplace.json` and every `plugin.json` must carry that same version (`scripts/validate.py` fails otherwise). Semver: breaking (renaming/removing a skill or command) = major; new skills/commands or changed behavior = minor; fixes/docs = patch. Full procedure: `CONTRIBUTING.md § Releasing`.

## After any skill/command change

1. Run `python3 scripts/validate.py` (also runs in CI on push/PR to `main`).
2. If skills/commands were added or removed, update: the plugin's own `README.md` (`## Skills (N)` / `## Commands (N)`), the root `README.md` (headline counts + that plugin's summary line), and `marketplace.json`'s `description` if totals changed.
3. Add a `CHANGELOG.md` entry and bump versions per `CONTRIBUTING.md § Releasing`.
