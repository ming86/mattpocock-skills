## What it does

`to-spec` turns the current conversation and established project context into a durable implementation specification.

The defining constraint is that it does not reopen already-resolved discussion. It synthesizes what is known and preserves material unresolved points instead of inventing answers to make the document look complete.

## When to reach for it

Type `/to-spec` when later implementation, delegation, review, or context replacement would benefit from a durable statement of the intended outcome and important decisions.

A small change that can be implemented coherently from the current request may not need a spec at all.

## Preserve information status

A useful spec distinguishes:

- established requirements and explicit decisions;
- facts or constraints discovered from the repository;
- working assumptions that may still change;
- unresolved points that later work must not silently decide.

The document should contain enough implementation detail to preserve material decisions without turning into a volatile file-by-file script.

Verification should focus on valuable observable seams already available in the project. The skill does not create new test layers merely to fill a template.

## Common questions

**What if an important decision is still unresolved?**

Keep it unresolved and surface it according to the project's consultation policy. Do not convert the most likely guess into a requirement.

**Do I need an exhaustive list of user stories and test cases?**

No. Include them when they clarify behavior, actors, value, or verification. Detail should be proportional to the work.

## It's working if

- A fresh executor can recover the intended outcome and important constraints.
- Tentative assumptions are visibly different from requirements.
- The spec is shorter when the work is simple and richer only where the work needs it.

## Where it fits

A spec can feed [`to-tickets`](../../skills/engineering/to-tickets/SKILL.md) when decomposition is useful, or [`implement`](../../skills/engineering/implement/SKILL.md) directly when the work is already a coherent unit.