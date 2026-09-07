---
name: domain-modeling
description: "Clarify or evolve domain concepts, terminology, entities, relationships, invariants, and domain decisions. Use when ambiguity in the business or problem model could change interpretation, responsibilities, processes, requirements, interfaces, data, or implementation; not merely for reorganizing software modules."
---

# Domain Modeling

Use this skill when the domain model itself is changing or unclear enough to affect the work: terminology, entities, relationships, invariants, or decisions that later work and discussion need to name consistently.

Merely reading an existing glossary for vocabulary is not domain modeling. Follow the project's existing documentation convention rather than assuming every project should have a root `CONTEXT.md` or `docs/adr/` tree.

## Understand the current model

Inspect relevant glossaries, context documents, forms, records, procedures, representative cases, and the language used by the people doing the work. Where software represents or enforces the domain, inspect relevant code, schemas, tests, and ADRs as well. Follow the project's existing domain-document convention when there is one.

If no shared domain document exists, do not create one automatically for incidental terminology. When a working model is worth keeping across contexts, first reuse the work's existing location or follow how the project normally saves domain work. A local working-state area is appropriate when the model is provisional or too detailed for shared project documentation. If no convention exists, use a simple work-centered document only when preserving the model is useful.

## During the session

### Challenge conflicting language

When current discussion conflicts with existing terminology or behavior, point out the contradiction. Distinguish a vocabulary disagreement from a real change in domain meaning.

### Sharpen fuzzy concepts

When an overloaded term hides meaningfully different concepts, propose clearer names or definitions and test them against concrete scenarios. Use distinctions that materially change interpretation, responsibilities, decisions, requirements, or behavior.

### Probe relationships and invariants

Use representative scenarios and edge cases when they help expose whether entities, states, roles, ownership, or transitions are actually understood. Keep the exploration tied to decisions the current work needs.

### Cross-check the model against current practice

Compare stated domain behavior with relevant documents, records, procedures, and representative cases. Where software represents or enforces the domain, compare it with the relevant code, schemas, tests, and documentation. Distinguish current practice, intended behavior, and proposed changes. Treat discrepancies as something to resolve rather than assuming either existing materials or the conversation is automatically right.

### Preserve changes when later work needs them

When a term, relationship, or invariant is clear enough that later work depends on it, preserve the compact current model in the work's existing saved state. Update the project's existing domain document when that is already the appropriate shared source of truth; otherwise keep provisional detail in the work's configured local state when useful. If the project uses `CONTEXT.md`, [CONTEXT-FORMAT.md](./CONTEXT-FORMAT.md) is available as a format. Do not record every conversational refinement or preserve a transcript.

### Record architectural decisions separately

Offer or create an ADR only when the repository uses ADRs and the decision is genuinely costly to reverse, surprising without context, and the result of a meaningful tradeoff. Use [ADR-FORMAT.md](./ADR-FORMAT.md) when that convention fits the project.

Keep direct findings, explicit decisions, working assumptions, and unresolved points distinct so later work can revise the model as understanding changes.
