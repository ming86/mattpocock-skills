---
name: implement
description: "Implement a well-scoped work item whose intended outcome is already defined by a ticket, specification, or current plan. Use for execution rather than requirements discovery; preserve the agreed scope, follow repository practices, keep supporting validation proportional to the actual change, and report when implementation shows that an important assumption or part of the plan is wrong in a way that changes the work."
disable-model-invocation: true
---

# Implement

Implement the well-scoped work described by the current spec, ticket, or plan.

## Process

1. Read the source work item and the relevant repository instructions before changing code. Preserve the current requirements, decisions, constraints, and completion or acceptance criteria without treating tentative assumptions as fixed facts.
2. Inspect enough surrounding code to follow existing architecture, vocabulary, interfaces, and relevant project practices. Prefer existing project patterns when they fit the requested behavior.
3. Implement the most direct solution that fits the current scope and codebase. Do not add unrelated cleanup, speculative abstractions, compatibility layers, defensive machinery, or future-facing configurability without a concrete need.
4. Derive validation and other supporting checks from the behavior, outcome, or uncertainty this work needs to establish. Use the smallest useful check or representative workflow that could expose a relevant failure, together with checks the project specifically requires. Keep preflights, benchmarks, gates, rollout or rollback checks, compatibility checks, integrity checks, and similar process at the level justified by the current task and its consequences. A spec section, ticket boundary, or available check does not by itself expand that scope. When a broader interpretation would add substantial supporting work, make the chosen scope explicit and name only the boundary that is actually relevant.
5. If something discovered during implementation shows that a requirement, assumption, interface, architecture decision, or part of the plan is wrong in a way that changes the work or planned direction, treat that as a change to the work rather than silently absorbing it into implementation. Report what changed and what it means before switching direction. When the work already has saved project state and the finding will matter later, update it rather than leaving the old assumption in place.
6. Complete the well-scoped implementation and report what changed, what was validated, and any unresolved issue that matters to dependent work. Do not create an implementation diary; save only information that later work would otherwise have to reconstruct.
