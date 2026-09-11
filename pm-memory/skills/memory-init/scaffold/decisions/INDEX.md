# Decisions — Index

Audit-trailed decision log. See `_SCHEMA.md` for the entry format.

| Date | Decision | Status | Reversal condition met? |
|---|---|---|---|

**Status values**: `pending` (drafted by the agent, awaiting operator confirmation) → `decided` (operator confirmed). Never set `decided` without explicit operator confirmation.

This index is maintained by `/decide` (new entries) and `/review` (flags: pending decisions older than 14 days, decisions whose stated reversal condition has since been met).
