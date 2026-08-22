# Design It Twice

When the user wants to explore alternative interfaces for a chosen deepening candidate, generate several materially different designs before converging. The useful mechanism is independent alternatives, not a particular subagent topology. Based on "Design It Twice" (Ousterhout): the first plausible interface is rarely the only one worth considering.

Use the vocabulary in [SKILL.md](SKILL.md): **module**, **interface**, **seam**, **adapter**, **leverage**.

Follow the governing project instructions for delegation, fresh contexts, parallelism, and user checkpoints. This procedure works whether alternatives are produced by one agent sequentially or by independent workers chosen by the root agent.

## Process

### 1. Frame the problem space

Write down the constraints every candidate interface must satisfy:

- the behavior and use cases the interface must support;
- the dependencies it relies on and their category from [DEEPENING.md](DEEPENING.md);
- important invariants, ordering constraints, error modes, and performance expectations;
- a small illustrative code sketch when it helps make the constraints concrete without prematurely selecting a design.

If materially different problem framings remain plausible, follow the governing consultation rules before treating one as established.

### 2. Generate independent alternatives

Produce at least two, and usually three, substantially different interfaces when the design question is consequential enough to justify comparison. Use different design pressures so the alternatives are genuinely distinct rather than cosmetic variants. Useful pressures include:

- minimize the interface and maximize leverage per entry point;
- maximize flexibility across known use cases;
- optimize the most common caller and make the default path trivial;
- place a seam around a real external or replaceable dependency when that is material.

If the governing orchestration policy chooses separate workers, give each a self-contained brief with the relevant files, constraints, dependency category, domain vocabulary, and expected output. Do not spawn workers merely because this document exists.

For each alternative, capture:

1. Interface: types, methods, parameters, invariants, ordering, and error modes.
2. Usage example showing how representative callers use it.
3. What complexity the implementation hides behind the seam.
4. Dependency and adapter strategy where relevant.
5. Tradeoffs in leverage, locality, flexibility, and migration cost.

### 3. Compare and recommend

Compare the alternatives on the constraints that actually matter to this module, especially **depth**, **locality**, and **seam placement**. Explain the material tradeoffs rather than scoring every dimension mechanically.

Give a recommendation when the evidence supports one. A hybrid is valid when it combines compatible strengths without creating a larger or less coherent interface. Preserve unresolved material tradeoffs instead of forcing convergence for its own sake.
