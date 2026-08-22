# Deepening Modules

Use this guide when several shallow modules may be simpler as one deeper module. The terms **module**, **interface**, **seam**, and **adapter** come from [SKILL.md](SKILL.md), but the repository's own terminology remains valid.

These are design heuristics, not automatic refactoring rules. Combining modules should make the caller-facing design simpler or keep related change in fewer places without collapsing responsibilities that are genuinely useful to keep separate.

## Dependency categories

When considering a merge of shallow modules, inspect their dependencies. The dependency shape affects how easily the combined behavior can be exercised and tested.

### 1. In-process

Pure computation, in-memory state, no I/O. These are often easier to combine because no external adapter is required. Combine them when the resulting interface hides meaningful complexity and the old separation has no independent value; then test through the resulting observable behavior.

### 2. Local-substitutable

Dependencies with faithful local test substitutes, such as PGLite for Postgres or an in-memory filesystem. A local substitute can make a deeper module practical, but it is not by itself a reason to merge anything. Use it when it gives credible coverage without forcing test-only concepts into the public interface.

### 3. Remote but owned

Your own services across a network boundary, such as internal APIs or microservices. A port or adapter can help when the network boundary is meaningful or several implementations genuinely need the same contract. Keep business or orchestration logic behind the module's normal interface and keep transport details near the network boundary.

For tests, use the cheapest substitute that preserves the behavior the test needs to prove. An in-memory adapter is one option, not a requirement.

Example recommendation: *"Keep transport details behind the existing service interface so callers depend on behavior rather than HTTP/gRPC details. Use a local adapter in tests only if it gives a credible and meaningfully cheaper feedback loop."*

### 4. External third party

Services such as Stripe or Twilio that you do not control. A narrow adapter is often useful when it prevents vendor details from spreading through the codebase or makes important behavior practical to test. Do not add an abstraction merely because an SDK is external; a direct integration can be appropriate when it is already simple and well contained.

## When a seam is useful

- Multiple real uses or implementations are strong evidence that a seam is useful. Production and test adapters can count when the interface represents a real contract, but do not invent a port solely so a test can mock it.
- A single implementation can still justify a seam when it hides important complexity, isolates volatility, or marks a real ownership boundary.
- A module can have private internal seams as well as a caller-facing interface. Do not expose internal collaborators merely because a particular test would find that convenient.

## Reassess tests after combining modules

- Remove tests that have become redundant checks of the old wiring, but keep narrower tests when they still provide useful speed, failure localization, difficult edge-case coverage, or protection for an important invariant.
- Prefer tests through the combined module's observable interface when that interface credibly proves the behavior callers rely on.
- Prefer observable outcomes over incidental internal state, while using lower-level evidence when it is the clearest way to protect an important invariant.
- Tests that survive harmless refactors are usually valuable, but implementation-aware tests can still be appropriate for algorithms, performance properties, or internal invariants. Judge a test by what it protects, not by a blanket rule about abstraction level.
