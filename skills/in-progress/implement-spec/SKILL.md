---
name: implement-spec
description: Drive an established specification and dependency-aware work graph to completion while leaving orchestration, review, and delivery policy to the governing project instructions.
disable-model-invocation: true
---

# Implement Spec

Use this skill when a specification already exists, its work has been decomposed into dependency-aware units, and the user wants the whole bounded effort driven toward completion.

This is a root-level orchestration workflow. If you are a spawned worker or subagent, do not use it to create another orchestration layer. Execute the work you were assigned and report back to the root agent.

The specification and work units are the durable source of truth. The current agent context coordinates execution; it should not become the only place where material decisions, dependencies, or completion state live.

Follow the governing project or user instructions for worker selection, delegation, parallelism, user checkpoints, branches, worktrees, commits, pull requests, validation, and independent review.

## Process

1. **Load the governing state.** Read the specification, work units, dependency relationships, relevant repository instructions, and enough current codebase state to understand the integration surface. Preserve the distinction between requirements, decisions, facts, assumptions, and unresolved points.

2. **Establish the ready frontier.** A work unit is ready only when its genuine blockers are resolved. Do not treat the ticket list as a sequential checklist when dependencies permit another order, and do not invent parallelism where units share tightly coupled reasoning or integration state.

3. **Choose the integration surface.** Use the repository's existing branch, pull-request, worktree, or direct-commit convention. Create new delivery machinery only when the project or requested workflow calls for it.

4. **Execute ready work in coherent contexts.** The root agent may delegate ready units according to the governing orchestration policy. Give each executor the bounded objective, relevant requirements and constraints, acceptance criteria, and pointers to durable sources. Include enough direct context to make the assignment reliable; context pointers are a tool for avoiding duplication, not a substitute for a clear assignment.

5. **Integrate and verify before unlocking dependents.** Review each completed unit appropriately, integrate it into the shared line of development, and establish that its acceptance criteria and consequential assumptions hold before treating its blockers as resolved. Keep verification proportional to the change and project practices.

6. **Advance the frontier.** Recompute which units are ready after integration. Run independent units in parallel only when the governing orchestration policy permits it and when concurrency improves throughput without creating disproportionate coordination or merge risk. Optimize for reliable progress, not maximum concurrency.

7. **Surface invalidated assumptions.** If implementation evidence materially changes the basis of the spec, interfaces, scope, dependencies, or approved direction, stop the affected path and follow the governing consultation rules. Do not silently redesign the specification merely to keep the graph moving.

8. **Respect milestones and checkpoints.** When the project instructions require a checkpoint before materially dependent work, complete the appropriate review and validation, report the resulting state, and wait for the required decision before advancing.

9. **Close the bounded effort.** Once all required units are complete, run the final validation and review required by the project. `code-review` can provide focused Intent / Spec and Repository / Implementation review when useful; broader independent criticism remains separate and governed by project instructions.

10. **Finalize delivery.** Commit, update or open a pull request, mark it ready, or perform cleanup only according to the repository's delivery conventions and the user's requested scope. Remove temporary worktrees or branches only if this workflow created them and they are no longer needed.