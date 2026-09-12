[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](https://github.com/louis3979/pm-skills/blob/main/LICENSE)

# PM Skills: an AI Operating System for Head-of-Product work

> 56 skills and 28 chained workflows across 3 plugins for Claude Code and Claude Cowork. Tech-product requirements/delivery rigor, Head-of-Product leadership, and a markdown-native project memory system — focused on technology/IT products, not business-vertical domain knowledge.

Built from a Head-of-Product skill analysis: each skill encodes a concrete workflow (input → framework → output), not a generic prompt. Each command chains one or more skills into an end-to-end process.

## Start Here

Broad question, don't know where to start? → `/copilot`
Need strategic clarity? → `/set-strategy`
Writing a PRD? → `/write-prd`
Planning delivery (scope/schedule/risk)? → `/plan-delivery-risk`
Ready to release? → `/gate-release`
Worried you'll forget something important? → `/init-memory`, then `/ingest`
Need to pressure-test a decision from every angle? → `/party-mode` or `/sharpen`

If this project helps you, ⭐ the repo.

## Plugins

<details>
<summary><strong>1. pm-tech-product</strong> — Requirements and delivery rigor for technology/IT products: PRD writing, requirement analysis, state machines, acceptance criteria, user stories, sprint planning/retrospectives, structured brainstorming, process modeling, business rules, security, QA, release gating, access control, audit logging, data consistency, PMBOK scope/schedule/risk/change management (27 skills, 9 commands)</summary>

Fills the gap between "a PRD exists" and "engineering can safely build it" for any tech product with real state, permission, and data-consistency complexity — not tied to a specific business vertical.

**Skills (27):**

- `prd-writer` — Write a full PRD from a raw brief, idea, or rough workflow description
- `requirement-analyzer` — Adversarially review a requirement/PRD for missing requirements, conflicts, ambiguity, undefined permission/state/rollback cases
- `state-machine-designer` — Design a complete state machine for any stateful entity — states, transitions, actors, conditions, illegal transitions
- `acceptance-criteria-generator` — Generate exhaustive Given/When/Then acceptance criteria: happy/negative path, permission cases, state cases
- `user-story-writer` — Turn a PRD/epic into an Epic + user stories + acceptance criteria + dependencies + Definition of Done
- `sprint-planner` — Plan a sprint from a prioritized backlog and real team capacity
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
- `structured-brainstormer` — Run a divergent-then-convergent brainstorm using named techniques (SCAMPER, Five Whys, Reverse Brainstorming, and more)
- `sprint-retrospective` — Lightweight recurring sprint retro: went well / didn't / puzzling, with owned action items

**Commands (9):**

- `/write-prd` — Write a full PRD from a raw idea or workflow description, with an adversarial review pass before it's done
- `/model-business-process` — Formalize a raw business workflow into actors, states, and explicit rules before it becomes a PRD
- `/prep-technical-handoff` — Translate a requirement into technical impact areas and run a security pass
- `/gate-release` — Generate adversarial QA test scenarios and run the go/no-go release checklist
- `/setup-access-controls` — Design the full control layer (permissions, approvals, audit logging, numbering) for a feature
- `/audit-data-consistency` — Audit a feature or flow for cross-system data consistency risk
- `/plan-delivery-risk` — Plan a large deliverable from scope breakdown through schedule/critical path to a tracked risk register
- `/brainstorm` — Run a structured divergent-then-convergent brainstorm on a problem
- `/sprint-retro` — Run a lightweight recurring sprint retrospective with owned action items

</details>

<details>
<summary><strong>2. pm-leadership</strong> — Head-of-Product leadership workflows: strategy, roadmap, prioritization, PR/FAQ, advanced elicitation, course correction, simulated debate, copilot orchestrator, weekly digests, 1:1 prep, board updates, hiring, stakeholder mapping, project closure (19 skills, 9 commands)</summary>

For the Head of Product's own operating rhythm and judgment calls: an orchestrator that routes broad questions to the right specialist skill, plus the recurring artifacts of running a product organization.

**Skills (19):**

- `product-strategist` — Turn company context into product vision, strategic themes, North Star metric, recommended bets, and an investment thesis
- `roadmap-planner` — Sequence strategic bets into an outcome-oriented roadmap by period, checking capacity and dependencies
- `product-prioritizer` — Score and rank a backlog (RICE/ICE/WSJF/Impact-Effort/MoSCoW/Kano) into Do Now/Next/Later/Don't Do
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
- `pr-faq-writer` — Stress-test a concept with Amazon's Working Backwards PR/FAQ method before it proceeds to a PRD
- `advanced-elicitation` — Pressure-test the most recent draft/decision with a menu of named critique techniques
- `course-correction-planner` — Assess a significant unexpected disruption mid-delivery and produce a continue/adjust/pivot/stop proposal
- `party-mode-debate` — Simulate a roundtable of distinct, disagreeing personas debating a decision

**Commands (9):**

- `/set-strategy` — Set product strategy from company context, then sequence it into a roadmap and a prioritized near-term backlog
- `/copilot` — Route a broad Head-of-Product question to the right specialist skills and synthesize one recommendation
- `/weekly-review` — Produce a combined personal weekly digest and product health rollup
- `/evaluate-bet` — Evaluate a product bet, resolve how to acquire it if relevant, and formalize the outcome as a decision memo
- `/close-project` — Formally close out a completed initiative: retrospective, handover, and an honest outcome-vs-intent review
- `/write-prfaq` — Stress-test a concept with the PR/FAQ working-backwards method before it proceeds to a PRD
- `/sharpen` — Pressure-test the most recent draft/decision with a menu of critique techniques
- `/correct-course` — Assess a mid-delivery disruption and produce a structured change proposal
- `/party-mode` — Simulate a roundtable debate of distinct, disagreeing personas on a decision or topic

</details>

<details>
<summary><strong>3. pm-memory</strong> — A markdown-native project memory system: durable knowledge, decisions, hypotheses, and stakeholder tracking that survives context loss between sessions (10 skills, 10 commands)</summary>

One operator, one product/initiative. `/init-memory` scaffolds a folder structure: raw artifacts land in `source/` (immutable), get synthesized into `ingestion/` (tagged observation/interpretation/hypothesis/assumption), and propagate into the durable layer — `knowledge/`, `hypotheses/` (evidence + confidence score), `decisions/` (audit trail + reversal condition), `stakeholders/` (touchpoints and cadence). A weekly `/review` sweep is what keeps it from rotting. Inspired by the second-brain model in [phuryn/pm-brain](https://github.com/phuryn/pm-brain), rebuilt in this marketplace's own conventions.

**Skills (10):**

- `memory-init` — Scaffold the memory folder structure into the current directory; detects greenfield/migration/active-repo, runs a short interview, commits locally (never pushes)
- `memory-ingest` — The workhorse: classify a raw artifact, copy it to `source/`, tag observations in `ingestion/`, propagate to the durable layer as warranted
- `memory-prep` — Read-only pre-meeting brief for a stakeholder or topic: last touchpoint, open asks, suggested questions
- `memory-review` — Weekly maintenance sweep: stale knowledge, stale evidence, hypothesis hygiene, stakeholder cadence, knowledge compression, archival
- `memory-decide` — Formalize a decision with a full evidence trail and reversal condition, drafted `pending` until the operator confirms it
- `memory-hypothesize` — Draft or update a tracked belief with evidence, confidence score, and a decision trigger
- `memory-risk-scan` — Five-area risk scan for a feature/initiative, drafting hypothesis stubs for uncovered areas
- `memory-ideate` — Grounded solution directions for a problem area, tagged with the evidence behind each
- `memory-plan` — Six-block plan for an objective: known, assumed, who to talk to, hypotheses to open, experiments, decision points
- `memory-strategy-check` — Check a proposal against stated strategy, citing the specific clause

**Commands (10):**

- `/init-memory` — Initialize the project memory system in the current directory
- `/ingest` — Ingest a raw artifact into project memory
- `/prep` — Pre-meeting/pre-task brief for a stakeholder or topic
- `/review` — Run the weekly maintenance sweep
- `/decide` — Formalize a decision with an evidence trail
- `/hypothesize` — Draft or update a tracked hypothesis
- `/risk-scan` — Five-area risk scan for a feature/initiative
- `/ideate` — Grounded solution directions for a problem area
- `/plan` — Six-block plan for an objective
- `/strategy-check` — Check a proposal against stated strategy

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
claude plugin install pm-memory@pm-skills
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
