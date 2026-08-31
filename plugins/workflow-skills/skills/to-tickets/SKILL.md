---
name: to-tickets
description: "Split a plan or specification into clear work units with real dependencies that can be executed in focused contexts. Use when the work is large enough to benefit from multiple independently understandable units or sessions; keep tightly coupled reasoning together instead of splitting work just to make smaller tickets."
disable-model-invocation: true
---

# To Tickets

Turn the current plan or spec into work units the project can find and continue. Each ticket should give a fresh agent or engineer enough context to understand the required outcome without carrying the whole planning conversation.

## Process

### 1. Gather the current source material

Work from the current conversation, current plan, spec, relevant issue, and relevant repository context. If a referenced document or work item exists, read the parts needed to carry forward its requirements, decisions, constraints, assumptions, unresolved points, and proposals accurately. Preserve those statuses during decomposition rather than treating every useful idea in the source material as part of the current work.

### 2. Understand the implementation surface when needed

Inspect the codebase enough to choose meaningful boundaries and dependencies. Use the project's existing domain vocabulary and respect relevant ADRs and repository conventions.

Do not create preparatory refactors merely because they might make later implementation cleaner or safer. An internal refactor that is genuinely necessary to deliver the current outcome can be part of the decomposition. If codebase inspection reveals an additional prerequisite or refactor that would expand the work beyond the current outcome or requirements, surface it as a proposed change rather than silently turning it into a required ticket.

### 3. Decompose at natural boundaries

Prefer work units that are coherent in terms of behavior, ownership, dependency, and reasoning. A ticket should normally:

- deliver a coherent increment of the requested outcome or a necessary part of it;
- contain enough focused context for a fresh session to understand reliably;
- state genuine prerequisites rather than incidental ordering preferences;
- avoid bundling semantically independent work merely because it is adjacent;
- avoid splitting tightly coupled reasoning merely to make tickets smaller.

Tracer-bullet vertical slices are useful for feature work when a narrow end-to-end increment can work independently and gives meaningful progress. Do not force every task through every architectural layer, and do not force vertical slicing onto refactors, migrations, infrastructure changes, or other work whose natural boundary is different.

Keep supporting work at the level where it serves the requested outcome. A ticket boundary organizes execution; it does not create a separate validation or supporting-process boundary. Shared or end-to-end checks can remain shared rather than being copied into every ticket.

For wide mechanical changes that cannot remain valid as independent vertical slices, use an appropriate staged migration such as expand–migrate–contract when the system actually requires it. Keep the staging no more elaborate than necessary.

### 4. Declare dependencies

For each ticket, identify only the other tickets that genuinely block it. Tickets whose blockers are resolved form the ready set.

### 5. Check decomposition choices that change the work

If different ways of splitting the work would change interfaces, scope, sequencing risk, ownership, or the intended delivery shape, keep that decision visible rather than hiding it inside ticket decomposition. Keep meaningfully different choices open until the direction is clear. Routine decomposition can proceed when the direction is already clear.

### 6. Keep newly discovered additions separate

If decomposition reveals a prerequisite, refactor, validation requirement, supporting step, or other work that is not already part of the source work or existing project requirements, report it separately as a proposed addition. Do not publish it as a required ticket, dependency, or completion criterion until it becomes part of the current work.

### 7. Publish the work units

Use the work's existing task location or follow the project's issue-tracker or task convention. Reuse an existing tracker, planning document, or work location instead of creating a parallel ticket store. When the tracker already preserves the work units and dependencies, do not copy the same tickets into local state just for persistence. Local working state should contain only detail or provisional context the shared record does not preserve well. If no convention exists, keep the tickets in the simplest work-centered task location that fits the work. Use native blocking relationships when practical; otherwise state dependencies explicitly in the ticket.

Each ticket should contain:

## What to deliver

The coherent behavior, result, migration state, or other outcome this ticket makes true.

## Completion criteria

A small set of conditions that make this work unit complete according to the source plan or specification. Focus on the outcome this ticket owns. Carry forward specific validation when the source work or existing project practice already requires it; otherwise keep completion criteria about the outcome rather than inventing new validation commitments for the ticket.

## Blocked by

References to genuine prerequisite tickets, or `None`.

## Context

Only context that a fresh executor would otherwise be likely to miss: important constraints, current decisions, relevant findings or source links, or links to the source spec/prototype. Do not copy the entire planning history.

Avoid volatile file-by-file instructions unless a file or interface location is itself a meaningful constraint. Preserve prototype-derived snippets only when they capture an important result or the basis for a current decision more precisely than prose.
