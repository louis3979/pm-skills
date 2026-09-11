# pm-requirements-plus

Requirements and delivery rigor for PMs building on complex/enterprise systems: business process modeling, business rules, technical impact analysis, security review, QA test-scenario generation, and release go/no-go gating.

## Overview

Fills the gap between "a PRD exists" and "engineering can safely build it" for workflows with real state, permission, and data-consistency complexity — the kind common in ERP, B2B SaaS, and other operationally heavy products.

## Install

Add the marketplace and install this plugin (or the whole collection) the same way as any other `pm-skills` plugin — see the root [README.md](../README.md) for the marketplace add/install commands.

## Skills (8)

- **business-process-modeler** — Formalize a raw business workflow into actors, process flow, documents, state machine, exception flows, and a permission matrix.
- **business-rule-designer** — Convert fuzzy business logic in prose into explicit, classified IF/THEN rules.
- **technical-product-analyst** — Translate a requirement/PRD into concrete technical impact areas across 10 surfaces (frontend, backend, API, data, integration, security, and more).
- **security-product-reviewer** — Run a product-level (not code-level) security review before a feature ships.
- **product-qa-reviewer** — Generate adversarial test scenarios (happy/negative/boundary/permission/state/concurrency/data-consistency) from a PRD.
- **release-manager** — Run a 12-point go/no-go release checklist and render a GO / GO WITH RISK / NO-GO verdict.
- **problem-validator** — Validate whether a suspected user problem is real, how big, and how urgent, before committing to a PRD.
- **persona-builder** — Build an evidence-based persona from research/interview data, with every attribute traced to a source.

## Commands (3)

- `/pm-requirements-plus:model-business-process` — Formalize a raw business workflow into actors, states, and explicit rules before it becomes a PRD.
- `/pm-requirements-plus:prep-technical-handoff` — Translate a requirement into technical impact areas and run a security pass before engineering starts.
- `/pm-requirements-plus:gate-release` — Generate adversarial QA test scenarios and run the go/no-go release checklist in one pass.

## Author

LDJ

## License

MIT
