---
description: Produce a combined personal weekly digest and product health rollup from this week's scattered updates
argument-hint: "<this week's updates, or leave blank to use conversation context>"
---

# /weekly-review -- Weekly Digest + Product Health

Roll up the week into a personal digest and, alongside it, a system-level product health view — the two together give both "what did I do" and "is the product okay."

## Invocation

```
/weekly-review
/weekly-review Shipped the transfer-approval flow, churn ticked up 0.5pp, blocked on payments API access
/weekly-review [paste status updates, Slack summaries, or metrics exports]
```

## Workflow

### Step 1: Gather the Week's Signal

Accept whatever's given — raw notes, status reports, experiment results — or pull from the current conversation's context if no argument is provided.

### Step 2: Produce the Personal Digest

Apply the **weekly-digest** skill:

- Bucket by domain, keep only what changed state
- Lead with 3-5 cross-domain highlights, tag status per item
- Call out blockers/risks separately, propose next week's focus

### Step 3: Produce the Product Health Rollup

Apply the **product-health-reviewer** skill:

- Score each health dimension (KPIs, delivery, incidents, feedback, churn, risks, strategic progress) by trend, not snapshot
- Cross-check dimensions for correlated degradation
- Recommend actions tied to specific weak dimensions

### Step 4: Combine and Present

```
# Weekly Review — Week [N], [year]

## Personal Digest
[weekly-digest output]

## Product Health
[product-health-reviewer output]
```

### Step 5: Offer Next Steps

- "A recurring 🔴 health dimension here — want a **decision memo** on it?"
- "Should I **prep board-update** numbers from this period's health data?"
- "Anything here worth flagging in an upcoming **1:1**?"

## Notes

- Skip a section entirely if there's genuinely nothing to report for it — don't pad either digest to look complete.
- If most product-health dimensions have no data this period, say so and recommend which data source to wire up next.
