# Fork adaptation principles

This fork keeps useful workflow mechanisms from Matt Pocock's skills while making them complementary to repository or user-level agent policy rather than a second orchestration framework.

The upstream project remains the source of the original skill set and is preserved under the MIT license in [LICENSE](./LICENSE).

## Authority boundaries

- `AGENTS.md`, `CLAUDE.md`, or equivalent governing instructions own engineering policy: scope, orchestration, delegation, user consultation, checkpoints, validation, commits, and independent review.
- Skills provide task-specific procedures. They should not override repository instructions or turn optional practices into mandatory gates.
- Independent critic agents such as `rubber-duck` remain separate from workflow skills. A workflow skill may prepare work for review, but review policy belongs to the governing agent instructions.

## Design principles

1. **Use process in proportion to the work.** Do not require specs, tickets, prototypes, TDD, full-suite runs, commits, or review merely because a workflow contains them. Use them when the task, project conventions, or governing instructions justify them.
2. **Externalize durable state.** Important decisions, constraints, dependencies, and completion state should survive fresh agent contexts in the repository, issue tracker, or other project artifacts when the work is long-running.
3. **Use fresh contexts at meaningful boundaries.** Decompose work at semantic, ownership, dependency, and reasoning boundaries, not arbitrary size. A work unit should contain enough context to be coherent and independently verifiable.
4. **Resolve uncertainty cheaply.** Prototype when a concrete experiment is cheaper or more reliable than more discussion. A prototype answers a specific question; it is not a mandatory implementation stage.
5. **Preserve decision status.** Do not silently convert guesses, examples, working assumptions, or tentative preferences into requirements. Surface material unresolved decisions instead of inventing them.
6. **Prefer observable progress.** Tickets should usually deliver a coherent, verifiable outcome. Vertical slices are useful when they fit the work, but should not be forced onto refactors or concerns whose natural boundary is different.
7. **Keep execution subordinate to the goal.** Implementation should follow the current approved direction while remaining able to surface evidence that invalidates a material assumption. It should not independently redesign the work.
8. **Separate review questions.** "Did we build what was requested?" and "Is it appropriate for this codebase?" are distinct review axes. Broader goal, proportionality, and assumption review can remain the responsibility of an independent critic.

## Adapted workflow surface

The initial fork work adapts the workflow spine used for substantial agent-driven engineering:

- `grill-with-docs`
- `prototype`
- `to-spec`
- `to-tickets`
- `wayfinder`
- `implement`
- `code-review`

Supporting workflow behavior is also adapted where leaving the upstream version intact would contradict those skills:

- `grilling` and `grill-me` now stop when material ambiguity is resolved instead of requiring exhaustive interrogation.
- `ask-matt` is retained as a compatibility router but selects the smallest useful flow instead of enforcing a fixed main pipeline.
- `setup-matt-pocock-skills` is optional shared configuration rather than a prerequisite or policy installer.
- the experimental `implement-spec` drives a durable task graph while leaving delegation, parallelism, checkpoints, integration, and review to governing project policy.

Other upstream skills remain intact unless their behavior later conflicts with these principles or there is a concrete reason to adapt them.

## Compatibility names

The `ask-matt` and `setup-matt-pocock-skills` invocation names are retained for compatibility even though their behavior and displayed titles are now fork-specific. Renaming them can be considered separately if breaking existing installations and references becomes worthwhile.

## Upstream changes

Treat upstream as a source of useful mechanisms and improvements, not as a policy authority for the fork.

When upstream changes a skill that has been adapted here:

1. inspect the upstream change and identify the underlying mechanism or bug fix;
2. check whether it still fits the authority boundaries and design principles above;
3. port the useful behavior intentionally rather than blindly restoring upstream text;
4. update fork docs and metadata when the behavior visible to users changes.

This keeps upstream learning cheap without making the fork dependent on conflict-heavy wholesale merges.