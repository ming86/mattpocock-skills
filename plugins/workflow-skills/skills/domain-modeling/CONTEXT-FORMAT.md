# CONTEXT.md Format

## Structure

```md
# {Context Name}

{One or two sentence description of what this context is and why it exists.}

## Language

**Order**:
{A one or two sentence description of the term}
_Avoid_: Purchase, transaction

**Invoice**:
A request for payment sent to a customer after delivery.
_Avoid_: Bill, payment request

**Customer**:
A person or organization that places orders.
_Avoid_: Client, buyer, account
```

## Rules

- **Choose a preferred term.** When several words mean the same domain concept, choose the clearest project term and list confusing synonyms under `_Avoid_` when that helps keep usage consistent.
- **Keep definitions short.** Usually one or two sentences. Define the concept clearly; include behavior only when it is part of the meaning.
- **Only include terms specific to this project's context.** General programming concepts (timeouts, error types, utility patterns) don't belong even if the project uses them extensively. Before adding a term, ask: is this a concept unique to this context, or a general programming concept? Only the former belongs.
- **Group terms under subheadings** when natural clusters emerge. If all terms belong to a single cohesive area, a flat list is fine.

## Single vs multi-context repos

**Single context (most repos):** One `CONTEXT.md` at the repo root.

**Multiple contexts:** A `CONTEXT-MAP.md` at the repo root lists the contexts, where they live, and how they relate to each other:

```md
# Context Map

## Contexts

- [Ordering](./src/ordering/CONTEXT.md): receives and tracks customer orders
- [Billing](./src/billing/CONTEXT.md): generates invoices and processes payments
- [Fulfillment](./src/fulfillment/CONTEXT.md): manages warehouse picking and shipping

## Relationships

- **Ordering → Fulfillment**: Ordering emits `OrderPlaced` events; Fulfillment consumes them to start picking
- **Fulfillment → Billing**: Fulfillment emits `ShipmentDispatched` events; Billing consumes them to generate invoices
- **Ordering ↔ Billing**: Shared types for `CustomerId` and `Money`
```

Use this structure only when the repository already uses the `CONTEXT.md` convention or the project has explicitly adopted it as a durable domain artifact. Then:

- If `CONTEXT-MAP.md` exists, read it to find contexts.
- If only a root `CONTEXT.md` exists, treat it as a single context.
- If neither exists and the project has explicitly chosen this convention, start with one root `CONTEXT.md`; split into multiple contexts only when real domain boundaries justify it.

When multiple contexts exist, infer where the current topic belongs when the evidence is clear. If several materially different placements remain plausible, surface the ambiguity rather than inventing one.
