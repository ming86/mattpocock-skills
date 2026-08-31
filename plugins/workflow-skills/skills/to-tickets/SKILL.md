---
name: to-tickets
description: "Split a plan or specification into clear work units with real dependencies that can be executed in focused contexts. Use when the work is large enough to benefit from multiple independently understandable units or sessions; keep tightly coupled reasoning together instead of splitting work just to make smaller tickets."
disable-model-invocation: true
---

# To Tickets

Turn an established plan or spec into durable work units. Each ticket should give a fresh agent or engineer enough context to understand the required outcome without carrying the whole planning conversation.

## Process

### 1. Gather the source of truth

Work from the current conversation, current plan, spec, relevant issue, and repository evidence. If a referenced artifact exists, read the material needed to preserve its requirements, decisions, constraints, and unresolved points accurately.

### 2. Understand the implementation surface when needed

Inspect the codebase enough to choose meaningful boundaries and dependencies. Use established domain vocabulary and respect relevant ADRs and repository conventions.

Do not create preparatory refactors merely because they might make later implementation cleaner. Add enabling refactors only when evidence shows they are required or meaningfully reduce the risk or complexity of the requested work.

### 3. Decompose at natural boundaries

Prefer work units that are coherent in terms of behavior, ownership, dependency, and reasoning. A ticket should normally:

- deliver a coherent increment of the requested outcome or a necessary part of it;
- contain enough focused context for a fresh session to understand reliably;
- state genuine prerequisites rather than incidental ordering preferences;
- avoid bundling semantically independent work merely because it is adjacent;
- avoid splitting tightly coupled reasoning merely to make tickets smaller.

Tracer-bullet vertical slices are useful for feature work when a narrow end-to-end increment can work independently and gives meaningful progress. Do not force every task through every architectural layer, and do not force vertical slicing onto refactors, migrations, infrastructure changes, or other work whose natural boundary is different.

Keep supporting work at the level where it serves the requested outcome. A ticket boundary organizes execution; it does not create an independent validation, benchmark, preflight, review, rollout, or rollback boundary. Shared or end-to-end checks can remain shared rather than being copied into every ticket.

For wide mechanical changes that cannot remain valid as independent vertical slices, use an appropriate staged migration such as expand–migrate–contract when the system actually requires it. Keep the staging no more elaborate than necessary.

### 4. Declare dependencies

For each ticket, identify only the other tickets that genuinely block it. Tickets whose blockers are resolved form the ready set.

### 5. Check material decomposition choices

If different ways of splitting the work would materially change interfaces, scope, sequencing risk, ownership, or the intended delivery shape, do not hide that decision inside ticket decomposition. Keep the materially different decomposition choices explicit until the direction is settled. Routine decomposition can proceed when the direction is already clear.

### 6. Publish durable work units

Use the work's existing task location or follow the project's issue-tracker or task convention. Reuse an existing tracker, planning document, or work location instead of creating a parallel ticket store. When the tracker already preserves the work units and dependencies, do not copy the same tickets into local state just for persistence. Local working state should contain only detail or provisional context the shared record does not preserve well. If no convention exists, keep the tickets in the simplest work-centered task location that fits the work. Use native blocking relationships when practical; otherwise state dependencies explicitly in the ticket.

Each ticket should contain:

## What to deliver

The coherent behavior, result, migration state, or other outcome this ticket makes true.

## Completion criteria

A small set of conditions that make this work unit complete according to the source plan or specification. Focus on the outcome this ticket owns. Include specific validation only when the source work or nature of the change requires it; do not manufacture a separate validation program for each ticket.

## Blocked by

References to genuine prerequisite tickets, or `None`.

## Context

Only decision-relevant context that a fresh executor would otherwise be likely to miss: important constraints, established decisions, relevant evidence, or links to the source spec/prototype. Do not copy the entire planning history.

Avoid volatile file-by-file instructions unless a file or interface location is itself a meaningful constraint. Preserve prototype-derived snippets only when they encode a validated decision more precisely than prose.
