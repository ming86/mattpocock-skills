---
name: to-tickets
description: Break a plan, spec, or conversation into coherent, dependency-aware work units that can be executed and verified in focused contexts.
disable-model-invocation: true
---

# To Tickets

Turn an established plan or spec into durable work units. Tickets should preserve enough context for a fresh agent or engineer to understand what outcome is required without carrying the entire planning conversation.

## Process

### 1. Gather the source of truth

Work from the current conversation, approved plan, spec, relevant issue, and repository evidence. If a referenced artifact exists, read the material needed to preserve its requirements, decisions, constraints, and unresolved points accurately.

### 2. Understand the implementation surface when needed

Inspect the codebase enough to choose meaningful boundaries and dependencies. Use established domain vocabulary and respect relevant ADRs and repository conventions.

Do not create prefactoring work merely because it might make later implementation cleaner. Add enabling refactors only when there is concrete evidence that they are required or materially reduce the risk or complexity of the requested work.

### 3. Decompose at natural boundaries

Prefer work units that are coherent in terms of behavior, ownership, dependency, and reasoning. A ticket should normally:

- deliver an observable or independently verifiable increment of the requested outcome;
- contain a reasoning scope that a fresh context can understand reliably;
- state genuine prerequisites rather than incidental ordering preferences;
- avoid bundling semantically independent work merely because it is adjacent;
- avoid splitting tightly coupled reasoning merely to make tickets smaller.

Tracer-bullet vertical slices are a strong default for feature work when a narrow end-to-end increment can work independently. Do not force every task through every architectural layer, and do not force vertical slicing onto refactors, migrations, infrastructure changes, or other work whose natural boundary is different.

For wide mechanical changes that cannot remain valid as independent vertical slices, use an appropriate staged migration such as expand–migrate–contract when the system actually requires it. Keep the staging no more elaborate than necessary.

### 4. Declare dependencies

For each ticket, identify only the other tickets that genuinely block it. Tickets with all blockers resolved form the ready frontier. The governing orchestration policy decides whether ready units are executed independently, sequentially, or in parallel.

### 5. Check material decomposition decisions

If materially different decompositions would change interfaces, scope, sequencing risk, ownership, or the user's intended delivery shape, surface the tradeoff according to the governing consultation rules. Do not require a ceremonial approval round for routine decomposition when the direction is already established.

### 6. Publish durable work units

Use the project's configured issue tracker or local task convention. Preserve blocking relationships using native tracker relationships when practical; otherwise state them explicitly in the ticket.

Each ticket should contain:

## What to deliver

The coherent behavior, result, migration state, or other outcome this ticket makes true.

## Acceptance criteria

A small set of observable criteria sufficient to establish completion. Do not restate implementation details as acceptance criteria unless the implementation detail is itself a requirement.

## Blocked by

References to genuine prerequisite tickets, or `None`.

## Context

Only decision-relevant context that a fresh executor would otherwise be likely to miss: important constraints, established decisions, relevant evidence, or links to the source spec/prototype. Do not copy the entire planning history.

Avoid volatile file-by-file instructions unless a file or interface location is itself a meaningful constraint. Preserve prototype-derived snippets only when they encode a validated decision more precisely than prose.

Follow the governing project instructions for labels, assignment, user checkpoints, parallelism, commits, and when dependent work may begin.