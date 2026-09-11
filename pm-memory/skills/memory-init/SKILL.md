---
name: memory-init
description: "Initialize a project memory system in the current directory — durable knowledge, decisions, hypotheses, and stakeholder tracking that survives context loss between sessions. Detects greenfield vs. migration vs. active-code-repo, runs a short interview, copies the deterministic scaffold, populates it from the interview, and commits locally. Use when invoked via /init-memory or when asked to set up project memory."
---

# Project Memory — Init

## Purpose

You are scaffolding a durable, markdown-native memory system into the current working directory for $ARGUMENTS (a product/initiative one operator is accountable for), so future sessions don't start from zero — decisions, evidence, and stakeholder context persist across context windows instead of being re-explained every time.

## Context

The scaffold is deterministic (static files under `scaffold/`, copied as-is) — the reasoning around it (mode detection, interview, populating placeholders) is adaptive. Do not invoke this for routine operation afterward (ingesting, prepping, reviewing) — those are the other skills in this plugin, guided by the seeded `CLAUDE.md` this skill installs.

## Instructions

1. **Detect mode** by inspecting the current working directory:
   - **Greenfield**: empty or near-empty directory → proceed directly to the interview.
   - **Migration**: directory already has PM artifacts (docs, notes, a prior ad-hoc knowledge base) but no code → copy (never move) existing artifacts into `source/adhoc/` for audit-anchor purposes, bulk-ingest them with epistemic caution (tag as observations/assumptions, not promoted knowledge, until verified), and note any cross-document conflicts found for later.
   - **Active code repo**: this is clearly a working software project already → stop and confirm with the operator before proceeding; don't scaffold on top of an active repo without explicit go-ahead.
   Announce the detected mode in one line before continuing.

2. **Run a short interview** (skip any question already answered by migrated source artifacts):
   - **Batch A — Strategy & Product**: North Star metric, current top 1-3 priorities, non-goals (if any), 1-3 active features worth tracking now.
   - **Batch B — Stakeholders & Team**: who are the 2-5 people that matter most to this initiative right now (name, role, rough influence level), who's on the working team, what recurring rituals exist (standups, reviews).
   - **Batch C — Working rules & preferences**: how much should this system draft autonomously vs. ask first (autonomy mode), any topics/files explicitly off-limits for autonomous writes, preferred maintenance cadence (default weekly if not stated), the evidence-promotion threshold if they want something other than the default (3+ independent observations).
   Confirm back what you heard before scaffolding — don't silently assume an unclear answer.

3. **Copy the scaffold**: copy every file and folder from this skill's `scaffold/` directory into the current working directory, preserving structure exactly, including `.gitkeep` placeholders in empty subfolders and the `.gitignore`. Copy in place — the current working directory **is** the project root; never create a nested subfolder for it.
   - Bash: `cp -R scaffold/. <dest>/` (the trailing `/.` picks up dotfiles).
   After copying, verify every top-level folder is present (`knowledge/`, `stakeholders/`, `hypotheses/`, `decisions/`, `source/`, `ingestion/`, `rules/`, `maintenance/`) plus `INDEX.md` and `CLAUDE.md`. Re-copy if anything is missing.

4. **Populate placeholders from interview answers**: walk the copied files and fill in what the interview (or migrated source) provided —
   - `knowledge/strategy.md` — North Star, priorities, non-goals (Batch A).
   - `knowledge/product.md` — one Active Features block per feature named in Batch A.
   - `stakeholders/<slug>.md` — one file per person named in Batch B, using `_SCHEMA.md`; update `stakeholders/INDEX.md`'s table.
   - `knowledge/org.md` — team + rituals from Batch B.
   - `CLAUDE.md § Operating preferences` and `§ Off-limits` — from Batch C.
   - `rules/INDEX.md` — promotion threshold and cadence from Batch C if they differed from defaults.
   Leave anything not covered by the interview as the placeholder, and list it as a scaffold gap in the handoff (step 6) rather than inventing a value.
   **Provenance**: every populated field should be traceable to either an interview answer or a migrated source artifact — link to the artifact inline when one exists.

5. **Self-test**: verify every internal markdown link in the populated files resolves (fix or flag broken ones); confirm you can correctly route each of the four `/ingest` artifact shapes (interview/meeting/market/adhoc) to its matching `source/`+`ingestion/` subfolder; if migration mode surfaced cross-document conflicts, list them now (or say explicitly "none found" — never fabricate conflicts to seem thorough).

6. **Commit locally**: check `git rev-parse --is-inside-work-tree` in the current directory. If already a repo, stage the scaffolded files and commit (`feat: initialize project memory`). If not, `git init` first, then stage and commit. **Never push remotely** — publication is the operator's call. If any git step fails, surface the error and stop rather than attempting a destructive recovery.

7. **Hand off**, leading with what's useful in the next 24 hours, not a folder tour:
   - The habit loop: suggest a first concrete action (e.g. "ingest today's notes," "prep for your next 1:1," "run `/review` this Friday").
   - Any contradictions found during migration (or "none found").
   - 2-3 scaffold gaps worth filling when there's time.
   - One short paragraph on what was built.
   Then stop and wait for the operator's first real task.

## Output

The full scaffold copied into the current directory (see `scaffold/INDEX.md` for the folder map), populated per step 4, plus the handoff message per step 7 — not a separate document.

## Notes

- Never regenerate scaffold content from scratch during init — copy from `scaffold/`. If a template needs to change permanently, that's a change to this skill's `scaffold/`, not an ad-hoc rewrite during someone's init.
- Never fabricate migration conflicts or scaffold gaps to look thorough — an honest "none found" is correct when it's true.
- Broken internal links are memory corruption, not a cosmetic issue — never skip the self-test.
- If the interview reveals this is really a multi-product or multi-team scope, flag that this system is designed for one operator/one initiative and ask whether to scope it down before proceeding.

## Example

Input: "Set up project memory for our B2B compliance product." Mode detected: greenfield. After the interview, `knowledge/strategy.md` gets a North Star of "time-to-SOC2-evidence," `stakeholders/acme-ops.md` and `stakeholders/eng-lead.md` get created, `CLAUDE.md § Operating preferences` records "draft freely in ingestion/, ask before writing decisions/." Handoff: "Ingest today's onboarding call notes, then prep for your Thursday sync with the eng lead. No conflicts (greenfield). Scaffold gaps: market landscape is empty, no rituals recorded yet."
