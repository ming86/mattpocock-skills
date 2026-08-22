---
name: domain-modeling
description: "Clarify or evolve domain concepts, terminology, entities, relationships, invariants, and domain decisions. Use when ambiguity in the business or problem model materially affects requirements, interfaces, data, or implementation; not merely for reorganizing software modules."
---

# Domain Modeling

Use this skill when the domain model itself is changing or materially ambiguous: terminology, entities, relationships, invariants, or decisions that later code and discussion need to name consistently.

Merely reading an existing glossary for vocabulary is not domain modeling. Follow the repository's established documentation convention rather than assuming every project should have a root `CONTEXT.md` or `docs/adr/` tree.

## Establish the current model

Inspect the project's existing glossary, context documents, ADRs, schema, code, tests, and user language that bear on the concept being discussed. If the repository has a configured domain-document convention, use it.

If no durable domain document exists, do not create one automatically for incidental terminology. When a working model is worth keeping across contexts, first reuse the work's existing durable location or follow the project's domain or durable-state convention. A local working-state area is appropriate when the model is provisional or too detailed for shared project documentation. If no convention exists, use a simple work-centered document only when preserving the model is useful, and follow the applicable project and user instructions for consultation before creating a new shared domain source of truth.

## During the session

### Challenge conflicting language

When current discussion conflicts with established terminology or behavior, point out the contradiction. Distinguish a vocabulary disagreement from a real change in domain meaning.

### Sharpen fuzzy concepts

When an overloaded term hides meaningfully different concepts, propose clearer names or definitions and test them against concrete scenarios. Do not manufacture distinctions that have no behavioral consequence.

### Probe relationships and invariants

Use representative scenarios and edge cases when they help expose whether entities, states, ownership, or transitions are actually understood. Keep the exploration tied to decisions the current work needs.

### Cross-check the implementation

When the user states how the domain behaves, compare it with relevant code, schema, tests, or existing docs. Treat discrepancies as evidence to resolve, not as automatic proof that either the code or conversation is authoritative.

### Preserve durable changes when useful

When a term, relationship, or invariant is materially resolved and later work depends on it, preserve the compact current model in the work's existing durable state. Update the repository's established domain artifact when that is already the appropriate shared source of truth; otherwise keep provisional detail in the work's configured local state when useful. If the project uses `CONTEXT.md`, [CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md) is available as a format. Do not record every conversational refinement or preserve a transcript.

### Record architectural decisions separately

Offer or create an ADR only when the repository uses ADRs and the decision is genuinely costly to reverse, surprising without context, and the result of a meaningful tradeoff. Use [ADR-FORMAT.md](./ADR-FORMAT.md) when that convention fits the project.

For material domain decisions, follow the applicable project and user instructions for consultation. Preserve the actual status of facts, explicit decisions, working assumptions, and unresolved points rather than forcing premature closure.
