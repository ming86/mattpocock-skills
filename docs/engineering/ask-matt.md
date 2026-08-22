## What it does

`ask-matt` is the compatibility router for this skill set. It chooses the smallest useful procedure for the current situation instead of sending every task through one fixed workflow.

The folder and invocation name are retained for compatibility with upstream installs and habits. The behavior in this fork is deliberately adaptive.

## When to reach for it

Type `/ask-matt` when you know the kind of work you have but are unsure which skill, if any, adds value.

| Situation | Likely route |
| --- | --- |
| Clear bounded implementation | [`implement`](../../skills/engineering/implement/SKILL.md), or direct work |
| Material ambiguity | [`grill-with-docs`](../../skills/engineering/grill-with-docs/SKILL.md) |
| Executable evidence would settle a question | [`prototype`](../../skills/engineering/prototype/SKILL.md) |
| Large uncertain work must survive several contexts | [`wayfinder`](../../skills/engineering/wayfinder/SKILL.md) |
| Settled decisions need a durable description | [`to-spec`](../../skills/engineering/to-spec/SKILL.md) |
| Multiple coherent work units would help | [`to-tickets`](../../skills/engineering/to-tickets/SKILL.md) |

## The important boundary

The router does not own engineering policy. Project and user instructions still decide delegation, checkpoints, validation, commits, parallelism, and independent review.

A later skill is not required merely because an earlier skill was used. Existing specs, tickets, decisions, and repository state should be reused rather than recreated to satisfy a nominal chain.

## Common questions

**Does every feature still go through grill, spec, tickets, and implement?**

No. A small clear feature can go directly to implementation. A large uncertain project may need several of those tools. The amount of workflow should follow the actual uncertainty and coordination needs.

**Why keep the `ask-matt` name?**

Compatibility. Renaming the folder would break existing invocations and installation references without improving the routing mechanism.

## It's working if

- Straightforward work takes a short route.
- Additional artifacts appear only when they solve a real context, ambiguity, or coordination problem.
- Existing durable state is reused instead of rewritten.

## Where it fits

This is the map over the promoted skills. It should stay consistent with [FORK.md](../../FORK.md) and the current skill behavior.