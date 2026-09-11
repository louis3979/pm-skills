# pm-tech-product

Requirements and delivery rigor for technology/IT product PMs: business process modeling, business rules, technical impact analysis, security review, QA test-scenario generation, release go/no-go gating, access control, audit logging, and cross-system data consistency.

## Overview

Fills the gap between "a PRD exists" and "engineering can safely build it" for any tech product with real state, permission, and data-consistency complexity — not tied to a specific business vertical.

## Install

Add the marketplace and install this plugin (or the whole collection) the same way as any other `pm-skills` plugin — see the root [README.md](../README.md) for the marketplace add/install commands.

## Skills (14)

- **business-process-modeler** — Formalize a raw business workflow into actors, process flow, documents, state machine, exception flows, and a permission matrix.
- **business-rule-designer** — Convert fuzzy business logic in prose into explicit, classified IF/THEN rules.
- **technical-product-analyst** — Translate a requirement/PRD into concrete technical impact areas across 10 surfaces (frontend, backend, API, data, integration, security, and more).
- **security-product-reviewer** — Run a product-level (not code-level) security review before a feature ships.
- **product-qa-reviewer** — Generate adversarial test scenarios (happy/negative/boundary/permission/state/concurrency/data-consistency) from a PRD.
- **release-manager** — Run a 12-point go/no-go release checklist and render a GO / GO WITH RISK / NO-GO verdict.
- **problem-validator** — Validate whether a suspected user problem is real, how big, and how urgent, before committing to a PRD.
- **persona-builder** — Build an evidence-based persona from research/interview data, with every attribute traced to a source.
- **rbac-permission-designer** — Design role-based permission matrices (role, org/tenant, resource scope, ownership, status, action) for any feature or module.
- **approval-workflow-designer** — Design approval workflows — single/multi-level, thresholds, delegation, escalation.
- **audit-trail-designer** — Specify what must be logged for every state-changing action, for compliance, debugging, or dispute resolution.
- **data-consistency-reviewer** — Review consistency across any systems/domains sharing the same underlying data, with attention to double writes and race conditions.
- **document-numbering-designer** — Design human-readable, collision-free numbering schemes for any user-facing record/document type.
- **reconciliation-designer** — Design a process to detect and resolve drift between two systems or two views of the same data.

## Commands (5)

- `/pm-tech-product:model-business-process` — Formalize a raw business workflow into actors, states, and explicit rules before it becomes a PRD.
- `/pm-tech-product:prep-technical-handoff` — Translate a requirement into technical impact areas and run a security pass before engineering starts.
- `/pm-tech-product:gate-release` — Generate adversarial QA test scenarios and run the go/no-go release checklist in one pass.
- `/pm-tech-product:setup-access-controls` — Design the full control layer for a feature/module: permissions, approval chain, audit logging, record numbering.
- `/pm-tech-product:audit-data-consistency` — Audit a feature or flow for cross-system data consistency risk and design the reconciliation safety net.

## Author

LDJ

## License

MIT
