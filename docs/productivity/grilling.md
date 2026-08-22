## What it does

`grilling` is the reusable interview primitive behind the grill skills. It clarifies user-owned decisions that materially affect a plan, design, or next step.

It no longer tries to visit every theoretical branch of a design tree. The stopping condition is enough shared understanding for the intended next step to proceed reliably.

## When to reach for it

The agent can invoke `grilling` when a wrapper skill needs focused clarification, and you can invoke it directly when you want the interview without repository-specific behavior.

Use [`grill-me`](../../skills/productivity/grill-me/SKILL.md) for an explicitly user-invoked general interview, or [`grill-with-docs`](../../skills/engineering/grill-with-docs/SKILL.md) when repository context and durable decisions matter.

## The frontier

The frontier is the set of material decisions whose prerequisites are already settled and that can usefully be answered now.

Facts that can be established from tools, files, documentation, or other evidence are the agent's responsibility. The user owns product, scope, interface, operational, and tradeoff decisions that genuinely require judgment.

Questions that become irrelevant are retired. New questions are added only when earlier answers expose material downstream decisions.

## Common questions

**Why not resolve every possible edge case?**

Because exhaustive questioning can create scope and requirements that do not matter to the next step. Material uncertainty is the useful boundary.

**Can several questions be asked together?**

Yes, when they are independent and grouping them reduces unnecessary back-and-forth. Ask sequentially when one answer changes the next question.

## It's working if

- The agent investigates facts instead of outsourcing lookup work to the user.
- Questions follow real decision dependencies.
- The interview stops when remaining uncertainty is no longer material.

## Where it fits

This is a model-invoked primitive used by higher-level clarification workflows. The calling skill supplies the narrower purpose and any documentation behavior.