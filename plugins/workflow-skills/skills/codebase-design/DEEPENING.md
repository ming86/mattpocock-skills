# Deepening Modules

Use this guide when several shallow modules may be simpler as one deeper module. The terms **module**, **interface**, **seam**, and **adapter** come from [SKILL.md](SKILL.md), but the repository's own terminology remains valid.

These are design heuristics, not automatic refactoring rules. Combining modules should make the caller-facing design simpler or keep related change in fewer places without collapsing responsibilities that are genuinely useful to keep separate.

## Dependency shape

When considering a merge of shallow modules, inspect the characteristics of their dependencies. Relevant characteristics can include whether a dependency crosses a process, device, or network boundary; who controls its implementation; whether its behavior can be exercised faithfully in a focused test; and operational properties such as determinism, cost, latency, availability, or side effects.

These characteristics can overlap. What matters is how the dependency affects the caller-facing design, the value of a seam, and the evidence available to validate the combined behavior.

Common dependency shapes include:

### In-process dependencies

Pure computation, in-memory state, or other behavior that does not cross an I/O boundary. These are often easier to combine because no external adapter is required. Combine them when the resulting interface hides meaningful complexity and the old separation has no independent value; then test through the resulting observable behavior.

### Dependencies with faithful local substitutes

Dependencies with credible local test substitutes, such as PGLite for Postgres or an in-memory filesystem. A local substitute can make a deeper module practical, but it is not by itself a reason to merge anything. Use it when it gives credible coverage without forcing test-only concepts into the public interface.

### Owned external processes or services

Dependencies you control across a process, device, or network boundary, such as a local daemon, internal service, or device-side component. A port or adapter can help when the boundary is meaningful or several implementations genuinely need the same contract. Keep higher-level domain or coordination logic behind the module's normal interface and keep boundary-specific transport or protocol details near the boundary.

For tests, use the cheapest substitute that preserves the behavior the test needs to prove. An in-memory adapter is one option, not a requirement.

Example recommendation: *"Keep boundary-specific transport details behind the existing interface so callers depend on behavior rather than HTTP, IPC, or protocol details. Use a local adapter in tests only if it gives a credible and meaningfully cheaper feedback loop."*

### Third-party dependencies

Dependencies you do not control, such as hosted services, native libraries, device SDKs, or vendor APIs. A narrow adapter is often useful when it prevents vendor details from spreading through the codebase or makes important behavior practical to test. Do not add an abstraction merely because a dependency is external; a direct integration can be appropriate when it is already simple and well contained.

## When a seam is useful

- Multiple real uses or implementations are strong evidence that a seam is useful. Production and test adapters can count when the interface represents a real contract, but do not invent a port solely so a test can mock it.
- A single implementation can still justify a seam when it hides important complexity, isolates volatility, or marks a real ownership boundary.
- A module can have private internal seams as well as a caller-facing interface. Do not expose internal collaborators merely because a particular test would find that convenient.

## Reassess tests after combining modules

- Remove tests that have become redundant checks of the old wiring, but keep narrower tests when they still provide useful speed, failure localization, difficult edge-case coverage, or protection for an important invariant.
- Prefer tests through the combined module's observable interface when that interface credibly proves the behavior callers rely on.
- Prefer observable outcomes over incidental internal state, while using lower-level evidence when it is the clearest way to protect an important invariant.
- Tests that survive harmless refactors are usually valuable, but implementation-aware tests can still be appropriate for algorithms, performance properties, or internal invariants. Judge a test by what it protects, not by a blanket rule about abstraction level.
