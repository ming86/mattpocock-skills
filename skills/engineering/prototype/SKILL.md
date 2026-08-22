---
name: prototype
description: Build the smallest throwaway artifact that can answer a material design, behavior, or UI question more cheaply or reliably than further discussion.
---

# Prototype

A prototype is **throwaway work that answers a specific question**. Use it when concrete evidence will resolve an important uncertainty more effectively than more planning or discussion. Do not insert a prototype stage when the relevant behavior or design is already clear enough to proceed.

## Choose the question first

Identify the uncertainty the prototype is meant to resolve. Common forms include:

- **Logic or state:** "Does this model behave coherently across the cases that are hard to reason about on paper?"
- **UI or interaction:** "Which structure or interaction best communicates the intended behavior?"
- **Integration or feasibility:** "Does this proposed mechanism actually work against the real dependency or environment?"

If materially different interpretations remain plausible and would produce different prototypes, follow the governing consultation rules. Otherwise infer the most likely question from the task and surrounding code and state any material assumption.

## Rules

1. **Keep it disposable.** Build only enough to answer the question. Avoid production hardening, generalized abstractions, persistence, broad error handling, exhaustive tests, cleanup, or unrelated refactoring unless the experiment itself requires them.
2. **Use the cheapest credible fidelity.** Prefer a focused executable example, temporary route, small harness, scratch script, single HTML file, or similarly narrow artifact over production-shaped implementation.
3. **Make the relevant state or outcome observable.** The user or agent should be able to see the evidence that answers the question, not merely inspect internal implementation.
4. **Use realistic dependencies only when they matter to the uncertainty.** Otherwise isolate the experiment from production state and persistent data.
5. **Stop when the question is answered.** Do not continue polishing a prototype after it has produced enough evidence for the decision.
6. **Preserve the validated decision, not accidental prototype structure.** Record the question, evidence, and resulting decision in the project's durable state when later work depends on it. Retain, commit, branch, or discard the prototype itself according to project conventions and the value of keeping it as evidence; no particular retention mechanism is mandatory.
7. **Do not silently promote the prototype into production.** Production implementation should be guided by the validated decision and current project constraints, not by a requirement to preserve throwaway code.

Follow repository and user instructions for where temporary artifacts belong and for any checkpoint before dependent implementation begins.