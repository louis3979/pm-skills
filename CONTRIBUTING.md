# Contributing

## Repo structure

```
pm-skills/
├── .claude-plugin/marketplace.json   <- root marketplace manifest (lists all plugins)
├── CHANGELOG.md                      <- release source of truth
├── scripts/validate.py               <- manifest/frontmatter/README-sync validator
└── pm-{name}/                        <- one directory per plugin
    ├── .claude-plugin/plugin.json    <- per-plugin manifest
    ├── skills/{skill}/SKILL.md       <- one folder per skill
    ├── commands/{command}.md         <- one file per command
    └── README.md                     <- per-plugin documentation
```

See `CLAUDE.md` for the design rules (skills vs. commands, frontmatter requirements, no cross-plugin references).

## Adding a skill

1. Create `pm-{plugin}/skills/{skill-name}/SKILL.md` with frontmatter `name` (must equal the directory name) and `description` (a full sentence, front-loaded with "Use when..." trigger language so it auto-loads at the right time).
2. Body: `## Purpose`, `## Context`, `## Instructions` (numbered), `## Output` (a concrete template), `## Notes` (3-5 terse bullets), optionally `## Example`.
3. If it belongs in a chained workflow, add or update a command that references it as `Apply the **skill-name** skill:`.

## Adding a command

Create `pm-{plugin}/commands/{command-name}.md` with frontmatter `description` and `argument-hint`. Body: `# /command-name -- Title`, `## Invocation` (2-3 examples), `## Workflow` (numbered steps chaining skills in the **same plugin only** — never a hard reference to another plugin's command, since plugins install independently), an output template, an "offer next steps" step, and `## Notes`.

## Before committing

Run the validator from the repo root:

```bash
python3 scripts/validate.py
```

It checks JSON validity, required manifest fields, name-matches-directory for every skill, required frontmatter on every skill/command, version sync across all manifests + `CHANGELOG.md`, and that `README.md`'s skill/command counts match what's actually on disk. This also runs in CI on every push/PR to `main` (`.github/workflows/validate.yml`).

If you added or removed a skill/command, update:
- The plugin's own `README.md` (`## Skills (N)` / `## Commands (N)` headers and lists).
- The root `README.md` (headline counts + that plugin's `<summary>` line and lists).
- The plugin's `.claude-plugin/plugin.json` `description` if the plugin's scope description changed.

## Releasing

1. Add a `CHANGELOG.md` entry under a new `## vX.Y.Z — YYYY-MM-DD` heading (newest first). Semver: breaking = major (renaming/removing a skill or command), new skills/commands or changed behavior = minor, fixes/docs = patch.
2. Bump the version in `marketplace.json` and every `plugin.json` to match — the validator fails if they drift.
3. Run `python3 scripts/validate.py` one more time, then commit and push.
