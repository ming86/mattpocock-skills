# Domain Modeling

## What it does

`domain-modeling` sharpens the vocabulary, relationships, invariants, and durable decisions that make up a project's domain model. It is for cases where the model itself is changing or materially ambiguous, not merely for reading an existing glossary.

The fork uses the repository's established domain-document convention instead of assuming every project should create a root `CONTEXT.md` or ADR tree.

## When to reach for it

Use it when overloaded terms hide different concepts, entity relationships are unclear, domain scenarios expose conflicting assumptions, or current code and stated domain behavior disagree in a way that matters to the work.

Do not invoke it simply because a task contains domain vocabulary.

## Common questions

**Does resolving a term automatically create or update `CONTEXT.md`?**

No. Preserve a material domain change when later work needs it, using the project's existing artifact. If no durable domain artifact exists, create or propose one only when its value justifies adding it.

**When is an ADR appropriate?**

When the project uses ADRs and the decision is costly to reverse, surprising without context, and the result of a real tradeoff. Do not turn every terminology discussion into architecture documentation.

**What if the code and the conversation disagree?**

Treat the discrepancy as evidence to resolve. Neither side becomes authoritative merely because it already exists.

## It's working if

The domain language becomes more precise where precision matters, concrete scenarios expose real invariants or distinctions, and durable documentation captures only decisions that future work actually needs.
