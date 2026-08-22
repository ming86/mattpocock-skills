## What it does

`implement` builds one bounded piece of work from an established spec, ticket, approved plan, or sufficiently clear request.

It preserves the current scope while allowing implementation evidence to reveal that an important assumption or decision is wrong. In that case it surfaces the change instead of quietly redesigning the work.

## When to reach for it

Type `/implement` when the desired outcome is clear enough to execute as one coherent unit.

The skill does not require a preceding spec or ticket when the current request already provides enough direction.

## Execution is project-governed

The implementation should follow existing repository architecture, vocabulary, interfaces, and validation practices. Prefer the most direct coherent solution and avoid unrelated cleanup or speculative machinery.

TDD, focused tests, typechecking, integration checks, full-suite runs, commits, code review, and pull requests are all useful in the right setting. None is mandatory merely because `implement` is running. Project instructions and the consequences of the change determine what evidence is appropriate.

If evidence invalidates a material requirement, assumption, interface, architecture decision, or planned direction, the skill should return that decision through the governing root-agent or user consultation path.

## Common questions

**Does `implement` always use TDD?**

No. Use [`tdd`](../../skills/engineering/tdd/SKILL.md) when test-first development fits the behavior and project practices or when governing instructions require it.

**Does it automatically commit and run code review?**

No. Delivery and review are controlled by project policy and current authorization.

## It's working if

- The result stays within the bounded request.
- Validation is targeted to the actual consequences of the change.
- Materially invalidated assumptions are surfaced before the work silently changes direction.

## Where it fits

`implement` is the execution step for any sufficiently established unit of work. [`code-review`](../../skills/engineering/code-review/SKILL.md) can later provide focused conformance review when useful, while broader independent review remains separate.