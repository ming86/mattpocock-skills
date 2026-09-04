---
name: codebase-design
description: "Design or improve module boundaries, interfaces, dependency structure, and responsibility placement. Use when deciding where responsibilities belong, simplifying what callers must understand, or making code easier for humans and coding agents to navigate; focus on software structure rather than domain-model discovery."
---

# Codebase Design

Prefer modules that hide useful complexity behind a small, clear interface. Use the ideas in this skill when they help explain or improve the design; do not force the repository to adopt this vocabulary.

The aim is simple: callers should need to know less, related behavior should stay together when that improves coherence, and important changes should remain understandable and localized.

## Useful design terms

These terms are analytical tools, not a required dialect. Keep the repository's existing names when they are already clear. A project may reasonably call something a service, component, API, boundary, package, or subsystem.

**Module**: any piece of software with something callers use and an implementation behind it. It can be a function, class, package, service, or larger slice.

**Interface**: what a caller must know to use a module correctly. This can include the type signature, invariants, ordering rules, error behavior, required configuration, and important performance characteristics. `API` or `signature` may be the right project term when that narrower meaning is intended.

**Implementation**: the code behind the interface.

**Depth**: how much useful behavior a module hides relative to how much callers must understand. A deep module provides substantial behavior through a relatively small interface. A shallow module exposes nearly as much complexity as it hides.

**Seam** _(Michael Feathers)_: a place where behavior can be changed or substituted without editing the code at that point. Use this term when replaceability or test control is the point. `Boundary`, `extension point`, or the repository's own term may be clearer in other contexts.

**Adapter**: a concrete implementation that fits an interface at a seam. Use the term when the role of plugging into that interface matters.

## Deep vs shallow

**Deep module** = small interface + substantial hidden behavior:

```
┌─────────────────────┐
│   Small Interface   │  ← Few methods, simple params
├─────────────────────┤
│                     │
│  Deep Implementation│  ← Complexity hidden here
│                     │
└─────────────────────┘
```

**Shallow module** = large interface + little hidden behavior:

```
┌─────────────────────────────────┐
│       Large Interface           │  ← Many methods, complex params
├─────────────────────────────────┤
│  Thin Implementation            │  ← Mostly passes through
└─────────────────────────────────┘
```

When designing an interface, ask:

- Can callers learn fewer methods or concepts?
- Can the parameters become simpler?
- Can more related complexity stay behind the interface?
- Does the current separation serve an independent responsibility, or merely spread one responsibility across files?

## Principles

- **Judge depth from the caller's side.** Internal decomposition can still use small helpers, collaborators, or private seams. They do not have to become part of the public interface.
- **Use the deletion test.** Imagine deleting the module. If its complexity mostly disappears, it may be a pass-through. If that complexity spreads back across many callers, the module is probably doing useful work.
- **Prefer boundaries around stable behavior.** Callers benefit when the interface reflects behavior that is less volatile than the implementation behind it.
- **Place responsibility where the behavior is owned.** The caller, UI, or file where an effect appears is not automatically the right place to define it. When several components can independently determine the same state or rule, make that multiplicity intentional or converge on the component that should own the behavior.
- **Make an extra seam earn its keep.** Real variation, multiple consumers or implementations, ownership boundaries, volatility, or a concrete need to substitute a dependency can justify a seam. Testing convenience alone is not a reason to introduce one.

## When dependency control matters

Good interfaces sometimes make dependencies easier to substitute or important behavior easier to exercise. Treat that as a consequence of a useful boundary, not a reason to invent one.

1. **Make dependencies controllable when substitution has real value.** Pass in an external or variable dependency when that creates a useful runtime, ownership, or implementation boundary, or when the work has a concrete need to control the dependency during a check or experiment. Keep direct construction when it is simpler and the dependency does not need independent control.

   ```typescript
   // Useful when payment is an external dependency we need to control
   function processOrder(order, paymentGateway) {}

   // Direct construction can be fine when no independent control is needed
   function processOrder(order) {
     const gateway = new StripeGateway();
   }
   ```

2. **Separate computation from side effects when doing so improves the design.** Returning a value can be easier to compose and reason about, but side effects are legitimate when performing them is the module's job.

   ```typescript
   // Computation with a directly observable result
   function calculateDiscount(cart): Discount {}

   // A command-style interface can still be right when mutation is the behavior
   function applyDiscount(cart): void {
     cart.total -= discount;
   }
   ```

3. **Prefer a small interface.** Fewer methods and parameters usually reduce what callers must understand, as long as the interface still exposes the genuinely different operations the module owns.

## Relationships between the terms

- A module presents an interface to its callers.
- Depth describes how much useful behavior sits behind that interface.
- A seam is a place where an implementation can vary or be substituted.
- An adapter is one implementation that fits such an interface.

These relationships are reasoning aids, not naming requirements for the codebase.

## Common misreadings

- **Do not measure depth by implementation lines divided by interface lines.** More code is not automatically better. The useful question is whether callers get substantial behavior without learning unnecessary complexity.
- **Do not reduce "interface" to a language keyword or method list.** The important caller-visible contract can include behavior and constraints that types do not express.
- **Do not replace ordinary project terms merely to match this skill.** Use `seam` when replaceability is the important distinction; use `boundary`, `API`, `service`, or another existing project term when it communicates the design more clearly.

## Going deeper

- For **combining shallow modules when dependencies make that useful**, see [DEEPENING.md](DEEPENING.md).
- For **comparing genuinely different interface designs when the decision warrants it**, see [DESIGN-IT-TWICE.md](DESIGN-IT-TWICE.md).
- When the broader question is whether an abstraction, layer, mechanism, or other design complexity materially contributes to the current solution, use `simplify-by-ablation`.
