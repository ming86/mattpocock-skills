## What it does

`to-tickets` decomposes an established plan or spec into coherent, dependency-aware work units that can be executed and verified in focused contexts.

The goal is not to maximize ticket count. A good ticket has a meaningful outcome, a manageable reasoning scope, and only genuine prerequisites.

## When to reach for it

Type `/to-tickets` when the work benefits from several execution contexts, explicit dependencies, separate ownership, parallel work, or durable progress tracking.

Do not split a small coherent change just because a ticket workflow exists.

## Choosing boundaries

For feature work, a narrow end-to-end tracer bullet is often useful because it produces observable progress. It is not a universal shape.

Refactors, migrations, infrastructure work, and tightly coupled changes may have different natural boundaries. Decompose around behavior, ownership, dependencies, and reasoning rather than arbitrary size or architectural layers.

Enabling refactors belong in the graph only when there is concrete evidence they are needed or materially reduce the requested work's risk or complexity.

## Common questions

**How small should a ticket be?**

Small enough that a fresh context can reason about it reliably, but large enough to remain a coherent unit with an independently meaningful completion condition.

**Should every ticket be a vertical slice?**

No. Use vertical slices when they create valid independent progress. Do not force them onto work whose natural boundary is different.

**Should I refactor first to make implementation easier?**

Only when the current code demonstrates a real need. Speculative prefactoring is not a default stage.

## It's working if

- Ready work can be identified from real dependency edges.
- Fresh executors need only the ticket plus focused source context, not the whole planning conversation.
- Completing a ticket produces observable or independently verifiable progress.

## Where it fits

It commonly follows [`to-spec`](../../skills/engineering/to-spec/SKILL.md), but it can decompose any sufficiently established source of truth. Each ready unit can later be handled by [`implement`](../../skills/engineering/implement/SKILL.md) or the project's own execution workflow.