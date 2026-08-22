## What it does

`grill-with-docs` clarifies product, scope, interface, design, or domain decisions that materially affect later work. It also preserves resolved decisions in durable project artifacts when doing so will help future contexts.

Its stopping condition matters: the goal is enough shared understanding for the next meaningful phase, not an exhaustive interview about every conceivable edge case.

## When to reach for it

Type `/grill-with-docs` when unresolved user-owned decisions would materially change what should be built or how the work should proceed.

Do not use it merely because a change exists. If the request and repository already make the important direction clear, proceed without manufacturing a clarification phase.

## Facts and decisions

The agent should establish facts from the codebase, documentation, tools, and other available evidence. Questions are for decisions that genuinely require user judgment.

When domain terminology or relationships are themselves ambiguous, [`domain-modeling`](../../skills/engineering/domain-modeling/SKILL.md) can help sharpen them. That is optional rather than automatic.

Durable records should preserve status accurately. An explicit decision is different from a discovered fact, a working assumption, or an unresolved point.

## Common questions

**Should I run this before every implementation?**

No. Use it when material ambiguity exists. Repeatedly grilling already-clear work adds latency and can create requirements that nobody actually asked for.

**Does it always create `CONTEXT.md` or ADRs?**

No. Reuse the project's existing durable documentation when useful. Create or update an artifact only when later work benefits from preserving the information.

## It's working if

- The questions get narrower as material uncertainty is resolved.
- The agent investigates facts instead of asking you to look them up.
- The session stops once the next phase can proceed reliably.
- Durable notes distinguish decisions from assumptions.

## Where it fits

Use [`prototype`](../../skills/engineering/prototype/SKILL.md) when executable evidence is cheaper than more discussion. Use [`to-spec`](../../skills/engineering/to-spec/SKILL.md) when the resolved understanding should become a durable implementation description.