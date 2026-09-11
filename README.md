[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](https://github.com/louis3979/pm-skills/blob/main/LICENSE)

# PM Skills: an AI Operating System for Head-of-Product work

> 31 skills and 10 chained workflows across 2 plugins for Claude Code and Claude Cowork. Tech-product requirements/delivery rigor (including PMBOK-grounded scope/schedule/risk/change management) and Head-of-Product leadership — focused on technology/IT products, not business-vertical domain knowledge.

Built from a Head-of-Product skill analysis: each skill encodes a concrete workflow (input → framework → output), not a generic prompt. Each command chains one or more skills into an end-to-end process.

## Plugins

<details>
<summary><strong>1. pm-tech-product</strong> — Requirements and delivery rigor for technology/IT products: process modeling, business rules, security, QA, release gating, access control, audit logging, data consistency, PMBOK scope/schedule/risk/change management (19 skills, 6 commands)</summary>

Fills the gap between "a PRD exists" and "engineering can safely build it" for any tech product with real state, permission, and data-consistency complexity — not tied to a specific business vertical.

**Skills (19):**

- `business-process-modeler` — Formalize a raw business workflow into actors, process flow, documents, state machine, exception flows, and a permission matrix
- `business-rule-designer` — Convert fuzzy business logic in prose into explicit, classified IF/THEN rules
- `technical-product-analyst` — Translate a requirement/PRD into concrete technical impact areas
- `security-product-reviewer` — Run a product-level security review before a feature ships
- `product-qa-reviewer` — Generate adversarial test scenarios from a PRD
- `release-manager` — Run a go/no-go release checklist and render a GO / GO WITH RISK / NO-GO verdict
- `problem-validator` — Validate whether a suspected user problem is real, how big, and how urgent
- `persona-builder` — Build an evidence-based persona from research/interview data, with every attribute traced to a source
- `rbac-permission-designer` — Design role-based permission matrices for any feature or module
- `approval-workflow-designer` — Design multi-level approval chains with thresholds, delegation, and escalation
- `audit-trail-designer` — Specify what must be logged for every state-changing action
- `data-consistency-reviewer` — Review consistency across any systems/domains sharing the same underlying data
- `document-numbering-designer` — Design human-readable, collision-free numbering schemes for any record type
- `reconciliation-designer` — Design a process to detect and resolve drift between two systems
- `wbs-scope-decomposer` — Break a large deliverable/epic into a Work Breakdown Structure with in/out-of-scope, deliverables, and acceptance criteria
- `schedule-critical-path-analyzer` — Sequence activities, estimate durations, identify the critical path, and assess the real schedule impact of a delay
- `risk-register-manager` — Build and maintain a risk register: identify, analyze probability × impact, plan a response, define monitoring triggers
- `change-control-manager` — Run a scope/requirement change through Integrated Change Control: impact analysis, decision, baseline update, communication
- `project-metrics-tracker` — Track delivery performance with PV/EV/AC/SPI/CPI and modern flow metrics, and force the output-vs-outcome distinction

**Commands (6):**

- `/model-business-process` — Formalize a raw business workflow into actors, states, and explicit rules before it becomes a PRD
- `/prep-technical-handoff` — Translate a requirement into technical impact areas and run a security pass
- `/gate-release` — Generate adversarial QA test scenarios and run the go/no-go release checklist
- `/setup-access-controls` — Design the full control layer (permissions, approvals, audit logging, numbering) for a feature
- `/audit-data-consistency` — Audit a feature or flow for cross-system data consistency risk
- `/plan-delivery-risk` — Plan a large deliverable from scope breakdown through schedule/critical path to a tracked risk register

</details>

<details>
<summary><strong>2. pm-leadership</strong> — Head-of-Product leadership workflows: copilot orchestrator, weekly digests, 1:1 prep, board updates, hiring, stakeholder mapping, project closure (12 skills, 4 commands)</summary>

For the Head of Product's own operating rhythm and judgment calls: an orchestrator that routes broad questions to the right specialist skill, plus the recurring artifacts of running a product organization.

**Skills (12):**

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
- `stakeholder-power-interest-mapper` — Map stakeholders onto a Power × Interest grid and define an engagement approach per quadrant
- `project-retrospective-closer` — Formally close out a project: acceptance, handover, retrospective, and outcome-vs-intent review

**Commands (4):**

- `/copilot` — Route a broad Head-of-Product question to the right specialist skills and synthesize one recommendation
- `/weekly-review` — Produce a combined personal weekly digest and product health rollup
- `/evaluate-bet` — Evaluate a product bet, resolve how to acquire it if relevant, and formalize the outcome as a decision memo
- `/close-project` — Formally close out a completed initiative: retrospective, handover, and an honest outcome-vs-intent review

</details>

## Installation

### Claude Cowork (recommended for non-developers)

1. Open **Customize** (bottom-left)
2. Go to **Plugins** → **Personal** → **+**
3. Select **Add marketplace from GitHub**
4. Enter: `louis3979/pm-skills`
5. Click **Sync**

Both plugins install automatically. You get both commands (`/copilot`, `/gate-release`, etc.) and skills.

### Claude Code (CLI)

```bash
# Step 1: Add the marketplace
claude plugin marketplace add louis3979/pm-skills

# Step 2: Install individual plugins
claude plugin install pm-tech-product@pm-skills
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
