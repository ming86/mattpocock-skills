# Design It Twice

Use this technique when an important interface decision still has several credible shapes and comparing them is likely to improve the choice. Do not generate alternatives merely because this file exists.

The value comes from comparing genuinely different designs, not from any particular subagent setup. The idea is based on Ousterhout's "Design It Twice": the first plausible interface is not always the best one.

Use the design concepts from [SKILL.md](SKILL.md) when they help, while keeping the repository's normal terminology.

Follow governing project instructions for delegation, fresh contexts, parallel work, and user checkpoints. One agent can produce the alternatives sequentially, or the governing orchestration policy can assign them to independent workers.

## Process

### 1. State the constraints

Write down what every candidate must satisfy:

- behavior and use cases the interface must support;
- relevant dependencies and their category from [DEEPENING.md](DEEPENING.md);
- important invariants, ordering rules, error behavior, and performance expectations;
- a small code sketch when it makes the constraints clearer without prematurely choosing a design.

If different interpretations of the problem would lead to meaningfully different designs, resolve that through the project's consultation rules before treating one interpretation as settled.

### 2. Generate distinct alternatives

Produce two or, when useful, three substantially different interfaces only when the decision is important enough to justify comparison. Make them differ in structure or tradeoffs, not just naming.

Useful design pressures include:

- minimize what callers must learn;
- support known variation without making the common path awkward;
- make the most common caller simple;
- isolate a real external or replaceable dependency when that helps the design.

If the governing orchestration policy uses separate workers, give each one the relevant files, constraints, dependency information, domain language, and expected output. Do not spawn workers merely because this technique mentions alternatives.

For each alternative, capture:

1. The interface: types, methods, parameters, invariants, ordering, and error behavior.
2. A short example showing how representative callers use it.
3. The complexity hidden behind the interface.
4. Dependency or adapter choices when relevant.
5. The important tradeoffs: caller simplicity, how concentrated changes stay, flexibility, testability, and migration cost.

### 3. Compare and recommend

Compare the alternatives on the constraints that actually matter. Explain the tradeoffs in plain terms rather than scoring every possible dimension.

Recommend one when the evidence supports it. A hybrid is valid when it combines compatible strengths without making the interface larger or less clear. Leave an important tradeoff unresolved when the available evidence cannot settle it; do not force a conclusion merely to finish the exercise.
