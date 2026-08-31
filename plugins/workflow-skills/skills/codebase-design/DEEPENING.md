# Deepening Modules

Use this guide when several shallow modules may be simpler as one deeper module. The terms **module**, **interface**, **seam**, and **adapter** come from [SKILL.md](SKILL.md), but the repository's own terminology remains valid.

These are design heuristics, not automatic refactoring rules. Combining modules should make the caller-facing design simpler or keep related change in fewer places without collapsing responsibilities that are genuinely useful to keep separate.

## Dependency shape

When considering a merge of shallow modules, inspect the characteristics of their dependencies. Relevant characteristics can include whether a dependency crosses a process, device, or network boundary; who controls its implementation; how easily its behavior can be exercised in normal development; and operational properties such as determinism, cost, latency, availability, or side effects.

These characteristics can overlap. What matters is how the dependency affects the caller-facing design, the value of a seam, and whether the combined behavior remains practical to exercise when needed.

Common dependency shapes include:

### In-process dependencies

Pure computation, in-memory state, or other behavior that does not cross an I/O boundary. These are often easier to combine because no external adapter is required. Combine them when the resulting interface hides meaningful complexity and the old separation has no independent value.

### Dependencies with faithful local substitutes

Some dependencies have credible local substitutes, such as PGLite for Postgres or an in-memory filesystem. A local substitute can make a deeper module easier to exercise, but it is not by itself a reason to merge anything or introduce a public abstraction.

### Owned external processes or services

Dependencies you control across a process, device, or network boundary, such as a local daemon, internal service, or device-side component. A port or adapter can help when the boundary is meaningful or several implementations genuinely need the same contract. Keep higher-level domain or coordination logic behind the module's normal interface and keep boundary-specific transport or protocol details near the boundary.

When validation needs to control this dependency, use the simplest substitute that preserves the behavior being checked. An in-memory adapter is one option, not a requirement.

Example recommendation: *"Keep boundary-specific transport details behind the existing interface so callers depend on behavior rather than HTTP, IPC, or protocol details. Use a local adapter only when the work actually needs that control and it gives a credible, meaningfully cheaper feedback loop."*

### Third-party dependencies

Dependencies you do not control, such as hosted services, native libraries, device SDKs, or vendor APIs. A narrow adapter is often useful when it prevents vendor details from spreading through the codebase or isolates a genuinely variable external contract. Do not add an abstraction merely because a dependency is external; a direct integration can be appropriate when it is already simple and well contained.

## When a seam is useful

- Multiple real uses or implementations are strong evidence that a seam is useful. A validation substitute can also fit an interface that already represents a real contract, but testing convenience alone does not create that contract.
- A single implementation can still justify a seam when it hides important complexity, isolates volatility, or marks a real ownership boundary.
- A module can have private internal seams as well as a caller-facing interface. Do not expose internal collaborators merely because a particular test would find that convenient.

## Reassess affected tests after combining modules

When the refactor changes existing test surfaces, keep the tests that still protect meaningful behavior or a concrete regression and retire checks that only preserve the old wiring. Prefer an observable interface when it credibly exposes the behavior, while retaining a narrower test when it is the clearest useful check for an algorithm, performance property, failure mode, or important invariant. The refactor itself does not create a requirement for additional tests.
