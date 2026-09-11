[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](https://github.com/louis3979/pm-skills/blob/main/LICENSE)

# PM Skills: an AI Operating System for Head-of-Product work

> 34 skills and 9 chained workflows across 3 plugins for Claude Code and Claude Cowork. ERP/retail/inventory domain intelligence, enterprise requirements rigor, and Head-of-Product leadership.

Built from a Head-of-Product skill analysis: each skill encodes a concrete workflow (input → framework → output), not a generic prompt. Each command chains one or more skills into an end-to-end process.

## Plugins

<details>
<summary><strong>1. pm-erp-domain</strong> — ERP, retail, and inventory domain intelligence: stock logic, transfers, procurement, RBAC, reconciliation (16 skills, 3 commands)</summary>

For PMs building on ERP, retail, warehouse, or accounting-adjacent systems. Fills the domain gap generic PM frameworks don't cover: the operational and financial correctness rules specific to inventory, transfers, procurement, and access control.

**Skills (16):**

- `inventory-domain-expert` — Validate on-hand/available/reserved stock quantity formulas and state transitions for internal consistency
- `inventory-transaction-reviewer` — Verify every stock-changing action produces a complete, traceable transaction record
- `warehouse-workflow-designer` — Design a complete warehouse operational process with actors and exception paths
- `stock-transfer-designer` — Standardize the Request → Approval → Allocation → Pick → Ship → Receive → Reconcile transfer lifecycle
- `allocation-rule-designer` — Design the rule that decides who gets how much when demand exceeds supply
- `procurement-domain-expert` — Validate a purchase-to-pay flow against standard 3-way-match discipline
- `accounting-logic-reviewer` — Check a requirement's financial logic for gaps before it reaches finance engineering
- `financial-transaction-consistency-reviewer` — Check that a document, transaction, and accounting entry stay consistent end-to-end
- `rbac-permission-designer` — Design role-based permission matrices for a business workflow
- `approval-workflow-designer` — Design multi-level approval chains with thresholds, delegation, and escalation
- `audit-trail-designer` — Specify what must be logged for every state-changing action
- `data-consistency-reviewer` — Review cross-domain consistency (inventory/orders/payments/accounting/reports) before shipping
- `document-numbering-designer` — Design human-readable, collision-free document numbering schemes
- `reconciliation-designer` — Design a process to detect and resolve drift between two systems
- `retail-domain-expert` — Apply correct retail domain concepts (store, POS, promotion, cash shift) to a requirement
- `product-master-data-designer` — Design the product/variant/SKU master data model

**Commands (3):**

- `/design-inventory-flow` — Design a complete inventory/stock-transfer flow from a raw scenario
- `/audit-erp-consistency` — Audit a feature or flow for cross-system data consistency risk
- `/setup-erp-controls` — Design the full control layer (permissions, approvals, audit logging, numbering) for a workflow

</details>

<details>
<summary><strong>2. pm-requirements-plus</strong> — Requirements and delivery rigor for complex/enterprise systems: process modeling, business rules, security, QA, release gating (8 skills, 3 commands)</summary>

Fills the gap between "a PRD exists" and "engineering can safely build it" for workflows with real state, permission, and data-consistency complexity — the kind common in ERP, B2B SaaS, and other operationally heavy products.

**Skills (8):**

- `business-process-modeler` — Formalize a raw business workflow into actors, process flow, documents, state machine, exception flows, and a permission matrix
- `business-rule-designer` — Convert fuzzy business logic in prose into explicit, classified IF/THEN rules
- `technical-product-analyst` — Translate a requirement/PRD into concrete technical impact areas
- `security-product-reviewer` — Run a product-level security review before a feature ships
- `product-qa-reviewer` — Generate adversarial test scenarios from a PRD
- `release-manager` — Run a go/no-go release checklist and render a GO / GO WITH RISK / NO-GO verdict
- `problem-validator` — Validate whether a suspected user problem is real, how big, and how urgent
- `persona-builder` — Build an evidence-based persona from research/interview data, with every attribute traced to a source

**Commands (3):**

- `/model-business-process` — Formalize a raw business workflow into actors, states, and explicit rules before it becomes a PRD
- `/prep-technical-handoff` — Translate a requirement into technical impact areas and run a security pass
- `/gate-release` — Generate adversarial QA test scenarios and run the go/no-go release checklist

</details>

<details>
<summary><strong>3. pm-leadership</strong> — Head-of-Product leadership workflows: copilot orchestrator, weekly digests, 1:1 prep, board updates, hiring (10 skills, 3 commands)</summary>

For the Head of Product's own operating rhythm and judgment calls: an orchestrator that routes broad questions to the right specialist skill, plus the recurring artifacts of running a product organization.

**Skills (10):**

- `head-of-product-copilot` — Orchestrate multiple PM skills to answer a broad Head-of-Product question that no single skill fully covers
- `product-bet-evaluator` — Evaluate a single specific product bet across customer value, business impact, strategic fit, feasibility, risk, cost, and reversibility
- `build-buy-partner-analyzer` — Compare building in-house vs. buying vs. partnering vs. outsourcing for a needed capability
- `weekly-digest` — Roll up a personal weekly digest from scattered updates across every domain
- `one-on-one-prep` — Prepare notes for a 1:1 with a direct report
- `board-update` — Write a high-level board update from a period's business and product results
- `hiring-brief` — Write a job description and interview-loop design for a PM or related role
- `decision-memo` — Write a structured decision memo — context, options, trade-offs, recommendation
- `product-meeting-assistant` — Extract decisions, actions, owners, deadlines, and risks from a raw meeting transcript
- `product-health-reviewer` — Produce a periodic product health rollup across KPIs, delivery, incidents, feedback, and risk

**Commands (3):**

- `/copilot` — Route a broad Head-of-Product question to the right specialist skills and synthesize one recommendation
- `/weekly-review` — Produce a combined personal weekly digest and product health rollup
- `/evaluate-bet` — Evaluate a product bet, resolve how to acquire it if relevant, and formalize the outcome as a decision memo

</details>

## Installation

### Claude Code (CLI)

```bash
# Step 1: Add the marketplace
claude plugin marketplace add louis3979/pm-skills

# Step 2: Install individual plugins
claude plugin install pm-erp-domain@pm-skills
claude plugin install pm-requirements-plus@pm-skills
claude plugin install pm-leadership@pm-skills
```

### Other AI assistants (skills only)

The `skills/*/SKILL.md` files follow the standard skill format and work with any tool that reads it. Commands (`/slash-commands`) are Claude-specific.

```bash
# Example: copy all skills for OpenCode (project-level)
for plugin in pm-*/; do
  mkdir -p .opencode/skills/
  cp -r "$plugin/skills/"* .opencode/skills/ 2>/dev/null
done
```

## How It Works

**Skills** give Claude domain knowledge and a guided workflow for a specific task. They load automatically when relevant to the conversation, or can be force-loaded with `/plugin-name:skill-name`.

**Commands** are user-triggered workflows invoked with `/command-name`. Each chains one or more skills in the same plugin into an end-to-end process, and ends by suggesting relevant next commands.

**Plugins** group related skills and commands into an installable package.

## License

MIT — see [LICENSE](LICENSE).
