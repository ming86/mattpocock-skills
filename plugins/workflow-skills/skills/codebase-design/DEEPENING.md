# Deepening

How to deepen a cluster of shallow modules safely, given its dependencies. Assumes the vocabulary in [SKILL.md](SKILL.md): **module**, **interface**, **seam**, **adapter**.

The categories below are design heuristics, not automatic refactoring rules. A dependency shape can make deepening easier or harder, but the change should still improve leverage or locality without collapsing responsibilities that are genuinely useful to keep separate.

## Dependency categories

When assessing a candidate for deepening, classify its dependencies. The category helps determine how a deepened module could be tested across its seam.

### 1. In-process

Pure computation, in-memory state, no I/O. These are often strong deepening candidates because merging them does not require an external adapter. Deepen when the combined interface hides meaningful complexity and the former separation is not independently useful; then test through the resulting observable interface.

### 2. Local-substitutable

Dependencies that have faithful local test stand-ins (PGLite for Postgres, an in-memory filesystem). A stand-in can make deepening practical, but its existence is not by itself a reason to merge modules. When the design benefits from deepening, test the resulting behavior with the stand-in where that gives credible coverage without exposing a test-only external interface.

### 3. Remote but owned (Ports & Adapters)

Your own services across a network boundary (microservices, internal APIs). A port can be useful when the network seam is a meaningful design boundary or when multiple adapters genuinely need to satisfy the same contract. Keep the domain or orchestration logic behind the module interface and let transport concerns remain at the seam. For tests, use the cheapest substitute that preserves the behavior the test needs to establish; an in-memory adapter is one option, not a requirement.

Recommendation shape: *"Keep the transport behind a narrow port at the existing service seam so callers depend on the behavior rather than HTTP/gRPC details. Use a local adapter in tests if that gives a credible and materially cheaper feedback loop."*

### 4. True external

Third-party services (Stripe, Twilio, etc.) you don't control. Isolating the external contract behind a narrow adapter is often useful when it keeps vendor details from spreading through the codebase or makes important behavior testable. Do not introduce an abstraction solely because an external SDK exists; a thin direct integration may be appropriate when it is already the project's established, low-complexity seam.

## Seam discipline

- **Multiple real uses are stronger evidence for a seam.** Production and test adapters can be legitimate evidence when the seam represents a meaningful contract, but do not introduce a port solely so a test can mock it. A single implementation can still justify a seam when the boundary itself hides material complexity, volatility, or ownership differences.
- **Internal seams vs external seams.** A deep module can have internal seams private to its implementation as well as the external seam at its interface. Do not expose internal seams through the public interface merely because a particular test would find them convenient.

## Testing strategy: consolidate intentionally

- Reassess tests on the former shallow modules after deepening. Remove tests that have become redundant implementation-detail checks, but retain narrower tests when they still provide material value such as fast feedback, useful failure localization, difficult edge-case coverage, or protection of an independently meaningful invariant.
- Prefer tests at the deepened module's observable interface when those tests credibly establish the behavior callers rely on.
- Prefer observable outcomes over incidental internal state, while following repository conventions and using lower-level evidence when it is the clearest way to establish a meaningful invariant.
- Tests that survive harmless internal refactors are usually more valuable, but some tests intentionally protect internal algorithms, performance properties, or invariants. Judge coupling by what the test is meant to protect rather than treating all implementation awareness as a defect.
