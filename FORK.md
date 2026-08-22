# Fork adaptation principles

This fork keeps the useful workflow mechanisms from Matt Pocock's skills while making them complementary to a repository or user-level `AGENTS.md` rather than a second orchestration policy.

## Authority boundaries

- `AGENTS.md` owns engineering policy: scope, orchestration, delegation, user consultation, checkpoints, validation, and independent review.
- Skills provide task-specific procedures. They should not override repository instructions or turn optional practices into mandatory gates.
- Independent critic agents such as `rubber-duck` remain separate from workflow skills. A workflow skill may prepare work for review, but review policy belongs to `AGENTS.md`.

## Design principles

1. **Use process in proportion to the work.** Do not require specs, tickets, prototypes, TDD, full-suite runs, commits, or review merely because a workflow contains them. Use them when the task, project conventions, or governing instructions justify them.
2. **Externalize durable state.** Important decisions, constraints, dependencies, and completion state should survive fresh agent contexts in the repository, issue tracker, or other project artifacts when the work is long-running.
3. **Use fresh contexts at meaningful boundaries.** Decompose work at semantic, ownership, dependency, and reasoning boundaries, not arbitrary size. A work unit should contain enough context to be coherent and independently verifiable.
4. **Resolve uncertainty cheaply.** Prototype when a concrete experiment is cheaper or more reliable than more discussion. A prototype answers a specific question; it is not a mandatory implementation stage.
5. **Preserve decision status.** Do not silently convert guesses, examples, working assumptions, or tentative preferences into requirements. Surface material unresolved decisions instead of inventing them.
6. **Prefer observable progress.** Tickets should usually deliver a coherent, verifiable outcome. Vertical slices are useful when they fit the work, but should not be forced onto refactors or concerns whose natural boundary is different.
7. **Keep execution subordinate to the goal.** Implementation should follow the current approved direction while remaining able to surface evidence that invalidates a material assumption. It should not independently redesign the work.
8. **Separate review questions.** "Did we build what was requested?" and "Is it appropriate for this codebase?" are distinct review axes. Broader goal, proportionality, and assumption review can remain the responsibility of an independent critic.

## Initial adaptation scope

The first pass focuses on the workflow spine used for substantial agent-driven engineering:

- `grill-with-docs`
- `prototype`
- `to-spec`
- `to-tickets`
- `wayfinder`
- `implement`
- `code-review`

Other upstream skills remain intact unless their behavior later conflicts with this fork's workflow.