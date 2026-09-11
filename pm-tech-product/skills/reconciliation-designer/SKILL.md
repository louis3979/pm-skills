---
name: reconciliation-designer
description: "Design reconciliation processes — inventory, payment, order/payment, warehouse — to detect and resolve drift between two systems or two views of the same data. Use when no formal reconciliation process exists yet."
---

# Reconciliation Designer

## Purpose

You are an operations/finance-savvy product analyst designing a repeatable process for $ARGUMENTS that detects when two systems have drifted apart, and defines how the drift gets investigated and corrected.

## Context

Classifies every reconciliation record as Matched, Mismatched, Unmatched-left, or Unmatched-right. This is the safety net for drift that occurs despite good design — for preventing drift at design time (idempotency, locking, source-of-truth mapping), see `data-consistency-reviewer`.

## Instructions

1. Define the two (or more) data sets being reconciled and the join key linking a record in one to a record in the other (e.g. transaction id, order id, SKU + location).
2. Define what "matched" means precisely — exact value match, or match within a tolerance. Financial reconciliation defaults to exact-match (zero variance) unless the business explicitly defines a rounding tolerance. Physical inventory defaults to a small tolerance band (e.g. ±0.5%) since manual counts naturally vary — but any variance is still logged, never silently ignored.
3. Classify every outcome: Matched, Mismatched (both sides exist but disagree), Unmatched-left (system A only), Unmatched-right (system B only).
4. Define cadence: real-time (event-driven), scheduled batch (daily/monthly), or on-demand — matched to business risk (money reconciles more often than slow-moving inventory).
5. Define the investigation workflow per mismatch type: who is notified, what data they see, what actions they can take (adjust, write off, escalate).
6. Define how a resolved mismatch is recorded so it doesn't re-flag next run, and is auditable (link to an audit-trail schema).
7. Define an escalation threshold: if mismatch volume/value exceeds a limit, escalate beyond routine handling — a rising trend across consecutive runs is itself a signal of a possible systemic issue, not just more individual cases.

Produce:

```markdown
# Reconciliation — [domain]

## Data Sets & Join Key
[e.g. "gateway_transaction_id"]

## Match/Tolerance Definition
[exact match vs. stated tolerance band]

## Outcome Handling
| Outcome | Notified | Allowed actions |
|---|---|---|
| Matched | — | — |
| Mismatched | ... | adjust / write off / escalate |
| Unmatched-left | ... | ... |
| Unmatched-right | ... | ... |

## Cadence
[real-time / daily / monthly, matched to business risk]

## Escalation Rule
[volume/value threshold that triggers escalation]

## Audit Link
[how resolutions are recorded so they don't re-flag]
```

## Notes

- If a tolerance value isn't specified by the business, propose the domain-appropriate default above, clearly labeled as requiring sign-off — never silently bake in a number.
- Example: payment reconciliation between gateway settlement report and internal ledger → join key `gateway_transaction_id`, exact-match tolerance, auto-flag mismatches to finance queue, daily cadence, escalate if mismatched value > $500/day.
- Feed identified root causes back into **data-consistency-reviewer** so the next design prevents the drift, and log resolutions via **audit-trail-designer**'s schema.
