# Design It Twice

Use this technique when the user wants to compare alternative interfaces, or when a material interface decision cannot be resolved reliably without comparing several credible designs. Do not generate alternatives merely because this file exists.

The value comes from comparing genuinely different designs. The idea is based on Ousterhout's "Design It Twice": the first plausible interface is not always the best one.

Use the design concepts from [SKILL.md](SKILL.md) when they help, while keeping the repository's normal terminology.

## Process

### 1. State the constraints

Write down what every candidate must satisfy:

- behavior and use cases the interface must support;
- relevant dependencies and their category from [DEEPENING.md](DEEPENING.md);
- important invariants, ordering rules, error behavior, and performance expectations;
- a small code sketch when it makes the constraints clearer without prematurely choosing a design.

If plausible interpretations of the problem would lead to materially different designs, surface the ambiguity and establish the intended interpretation before comparing designs; do not silently choose one.

### 2. Generate distinct alternatives

When the gate above is met, produce two or, when useful, three substantially different interfaces. Make them differ in structure or tradeoffs, not just naming.

Useful design pressures include:

- minimize what callers must learn;
- support known variation without making the common path awkward;
- make the most common caller simple;
- isolate a real external or replaceable dependency when that helps the design.

For each alternative, capture:

1. The interface: types, methods, parameters, invariants, ordering, and error behavior.
2. A short example showing how representative callers use it.
3. The complexity hidden behind the interface.
4. Dependency or adapter choices when relevant.
5. The important tradeoffs: caller simplicity, how concentrated changes stay, flexibility, testability, and migration cost.

### 3. Compare and recommend

Compare the alternatives on the constraints that actually matter. Explain the tradeoffs in plain terms rather than scoring every possible dimension.

Recommend one when the evidence supports it. A hybrid is valid when it combines compatible strengths without making the interface larger or less clear. Leave a material tradeoff unresolved when the available evidence cannot settle it; do not force a conclusion merely to finish the exercise.
