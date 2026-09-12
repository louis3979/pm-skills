# Changelog

All notable changes to this marketplace are documented here. The newest `## vX.Y.Z` heading is the current released version — `marketplace.json` and every plugin's `plugin.json` are kept in lockstep with it (checked by `scripts/validate.py`).

## v3.0.0 — 2026-09-12

### Added
- **BMAD-inspired skills**, adapted from `bmad-code-org/BMAD-METHOD` as self-contained skills with no dependency on that project's own scaffold/tooling:
  - `pm-tech-product`: `structured-brainstormer` (named-technique divergent brainstorming), `sprint-retrospective` (lightweight recurring retro), plus `/brainstorm` and `/sprint-retro`.
  - `pm-leadership`: `pr-faq-writer` (Amazon Working Backwards), `advanced-elicitation` (menu-driven critique techniques), `course-correction-planner` (mid-delivery disruption triage), `party-mode-debate` (simulated multi-persona roundtable), plus `/write-prfaq`, `/sharpen`, `/correct-course`, `/party-mode`.
- **Governance/CI**: `scripts/validate.py` (manifest/frontmatter/README-sync validator, zero third-party dependencies), a real `.github/workflows/validate.yml` replacing the placeholder `blank.yml`, `CONTRIBUTING.md`, `SECURITY.md`.

### Changed
- Version numbers across `marketplace.json` and all `plugin.json` files reset to a single consistent `3.0.0` (previously drifted independently — a gap this release's CI now prevents from recurring).

## v2.0.0 — 2026-09-11/12

### Added
- **pm-memory** plugin (10 skills, 10 commands): a markdown-native project memory system — source → ingestion → durable knowledge/hypotheses/decisions/stakeholders layers, plus a weekly maintenance sweep. Inspired by the second-brain model in `phuryn/pm-brain`, rebuilt independently.
- **PMBOK-grounded delivery skills** in `pm-tech-product`: `wbs-scope-decomposer`, `schedule-critical-path-analyzer`, `risk-register-manager`, `change-control-manager`, `project-metrics-tracker`, plus `/plan-delivery-risk`.
- **Requirements-core and strategy skills**, closing gaps identified against a Head-of-Product skill reference: `pm-tech-product` gained `prd-writer`, `requirement-analyzer`, `state-machine-designer`, `acceptance-criteria-generator`, `user-story-writer`, `sprint-planner`, `/write-prd`; `pm-leadership` gained `product-strategist`, `roadmap-planner`, `product-prioritizer`, `/set-strategy`.
- Stakeholder power/interest mapping and project closure/retrospective skills in `pm-leadership`.

### Changed
- `pm-erp-domain` (16 ERP/retail/inventory-vertical skills) removed to keep the marketplace focused on generic technology/IT product work rather than business-vertical domain knowledge; 6 domain-agnostic skills from it (RBAC, approvals, audit trail, data consistency, document numbering, reconciliation) were kept and merged into `pm-tech-product`.

## v1.0.0 — 2026-09-11

### Added
- Initial release: `pm-tech-product` and `pm-leadership` plugins, independently built (not a fork) — see each plugin's README for its skill/command list.
