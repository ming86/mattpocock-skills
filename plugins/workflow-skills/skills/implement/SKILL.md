---
name: implement
description: "Implement a well-scoped work item whose intended outcome is already defined by a ticket, specification, or current plan. Use for execution rather than requirements discovery; preserve the current scope, follow repository practices, use required and focused checks without inventing supporting work, and report when implementation shows that an important assumption or part of the plan is wrong in a way that changes the work."
disable-model-invocation: true
---

# Implement

Implement the well-scoped work described by the current spec, ticket, or plan.

## Process

1. Read the source work item and the relevant repository instructions before changing code. Preserve the current requirements, decisions, constraints, and completion or acceptance criteria without treating tentative assumptions as fixed facts.
2. Inspect enough surrounding code to follow existing architecture, vocabulary, interfaces, and relevant project practices. Prefer existing project patterns when they fit the requested behavior.
3. Implement the most direct solution that fits the current scope and codebase. Do not add unrelated cleanup, speculative abstractions, compatibility layers, defensive machinery, or future-facing configurability without a concrete need.
4. Run checks already required by the source work or project practice, together with the smallest focused existing or direct check that can reveal whether the changed behavior works as intended. A focused check of the changed behavior is normal implementation work; it does not need to become a new durable requirement. Do not introduce new validation infrastructure or other supporting process merely because it could increase confidence or reduce risk. If implementation reveals a specific reason to add such work, report it as a proposed expansion instead of silently adding it to the implementation.
5. If something discovered during implementation shows that a requirement, assumption, interface, architecture decision, or part of the plan is wrong in a way that changes the work or planned direction, treat that as a change to the work rather than silently absorbing it into implementation. Report what changed and what it means before switching direction. When the work already has saved project state and the finding will matter later, update it rather than leaving the old assumption in place.
6. Complete the well-scoped implementation and report what changed, what was checked and what those checks showed, and any unresolved issue that matters to dependent work. Do not create an implementation diary; save only information that later work would otherwise have to reconstruct.
