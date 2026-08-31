---
name: prototype
description: "Build the smallest throwaway experiment that can answer a design, behavior, UI, integration, or feasibility question whose answer could change the work. Use when trying something will answer the uncertainty more cheaply or reliably than more discussion or research; treat prototype structure as throwaway rather than production design."
disable-model-invocation: true
---

# Prototype

A prototype is **throwaway work that answers a specific question**. Use it when concrete evidence will resolve an important uncertainty more effectively than more planning or discussion. When the relevant behavior or design is already clear enough, proceed without a prototype.

## Choose the question first

Identify the uncertainty the prototype is meant to resolve. Common forms include:

- **Logic or state:** "Does this model behave correctly across cases that are hard to reason about on paper?"
- **UI or interaction:** "Which structure or interaction best communicates the intended behavior?"
- **Integration or feasibility:** "Does this proposed mechanism actually work against the real dependency or environment?"

Be clear about what different plausible results would change before building. If plausible interpretations would lead to meaningfully different prototypes, settle on one concrete question first. Otherwise infer the most likely question from the task and surrounding code, and state any important assumption. A prototype is most useful when a plausible result could change what happens next.

For common experiment shapes, [LOGIC.md](LOGIC.md) and [UI.md](UI.md) provide optional patterns. Use them only when that shape fits the question; they do not add mandatory stages or retention rules.

## Rules

1. **Keep it disposable.** Build only enough to answer the question. Avoid production hardening, generalized abstractions, persistence, broad error handling, exhaustive tests, cleanup, or unrelated refactoring unless the experiment itself requires them.
2. **Use the simplest credible experiment.** Prefer a focused executable example, temporary route, small harness, scratch script, single HTML file, or similarly narrow experiment over production-shaped implementation.
3. **Make the relevant state or outcome observable.** The user or agent should be able to see the result that answers the question, not merely inspect internal implementation.
4. **Use realistic dependencies only when they matter to the uncertainty.** Otherwise isolate the experiment from production state and persistent data.
5. **Stop when the question is answered.** Once the experiment has answered the question well enough to choose what happens next, further prototype polish is unnecessary.
6. **Preserve the conclusion, not accidental prototype structure.** When later contexts depend on the result, record the question, relevant result, conclusion, and remaining uncertainty in the work's existing location or follow how the project normally saves work that must survive context changes. Use local working state when the result is provisional or too detailed for shared project documentation. If no convention exists, keep the result in the simplest work-centered location that preserves the result for later work. Keep the record compact rather than saving a transcript or prototype diary. Keep or discard the prototype itself according to project conventions and whether it remains useful for later work; no particular retention method is required.
7. **Treat the prototype as evidence, not as the production design.** Production implementation should follow the conclusion supported by the experiment and the current project constraints. It does not need to preserve throwaway code or turn provisional working state into project truth.
