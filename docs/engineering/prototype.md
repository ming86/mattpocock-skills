## What it does

`prototype` builds the smallest throwaway artifact that can answer one material design, behavior, integration, or UI question more reliably than further discussion.

The prototype exists to produce evidence. It is not an early production implementation and it is not a mandatory phase before coding.

## When to reach for it

Type `/prototype`, or let the agent reach for it when an important uncertainty is easier to test than to reason about on paper.

Useful questions include whether a state model behaves coherently, which interaction communicates the intended behavior, or whether a proposed integration works against the real dependency.

## Cheap credible fidelity

Choose the lowest fidelity that can still answer the question: a scratch script, small harness, temporary route, single HTML file, focused executable example, or another narrow artifact.

Make the relevant outcome observable and stop when the question is answered. Production hardening, generalized abstractions, persistence, exhaustive tests, and unrelated cleanup normally reduce the value of a prototype by turning it into accidental implementation.

Preserve the validated decision when later work depends on it. Whether the throwaway artifact itself is retained, committed, branched, or discarded is a project decision.

## Common questions

**Should the prototype become the production code if it works?**

Not automatically. Production implementation should follow the validated decision and current project constraints, not the accidental structure of throwaway code.

**Do I need a prototype for every UI feature?**

No. Prototype only when a material question remains and executable evidence is worth the cost.

## It's working if

- You can name the question before building the artifact.
- The artifact gets no more polished than required to answer that question.
- The resulting decision is clearer than it was before the experiment.

## Where it fits

A prototype can appear during clarification, wayfinding, planning, or implementation whenever evidence is needed. Its result can feed [`to-spec`](../../skills/engineering/to-spec/SKILL.md) without forcing the prototype code into the final design.