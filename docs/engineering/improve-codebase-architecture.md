# Improve Codebase Architecture

## What it does

`improve-codebase-architecture` surveys a codebase for concrete opportunities to deepen shallow modules and improve locality, leverage, testability, and navigability. It presents evidence-backed candidates before interface design begins so the user can decide which architectural friction is worth addressing. A text shortlist is the default; visual reports are optional when they materially clarify complex relationships.

The skill uses `codebase-design` vocabulary but does not own worker selection or parallelism.

## When to reach for it

Use it when architecture improvement is itself the task, especially when recently changed or frequently touched areas show repeated coupling or difficult test seams.

Do not run it automatically alongside feature work merely because architectural cleanup might be nice.

## Common questions

**Does the skill need a separate exploration subagent?**

No. Exploration can happen directly or through workers chosen by the governing orchestration policy. The requirement is credible evidence for the candidates, not a particular execution topology.

**Does every architectural discussion update `CONTEXT.md` or create an ADR?**

No. Preserve a durable domain or architectural decision when later work genuinely needs it and use the repository's established convention. Do not create documentation merely because the skill is running.

**Why present candidates before designing interfaces?**

It keeps the expensive design work attached to a problem the user actually wants to solve instead of optimizing every shallow-looking module found during a scan.

## It's working if

The review identifies a small number of evidence-backed candidates, the user can see why each one matters, and later design work proceeds only for a candidate whose expected benefit justifies the change.
