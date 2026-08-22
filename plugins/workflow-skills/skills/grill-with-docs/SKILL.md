---
name: grill-with-docs
description: "Clarify material product, design, or domain decisions when existing repository context or documentation should be examined alongside user input. Use before dependent work when unresolved decisions could materially change scope, behavior, interfaces, or direction, and preserve durable decisions when useful."
disable-model-invocation: true
---

# Grill With Docs

Use this skill when unresolved decisions or domain ambiguity would materially affect the work. The goal is not to maximize the number of questions; it is to reach enough shared understanding for the next meaningful phase to proceed reliably.

## Process

1. Inspect the available conversation, codebase, documentation, ADRs, and other project evidence first. Resolve factual questions from evidence when practical instead of asking the user to supply facts the agent can establish itself.
2. Use `grilling` for material product, behavior, scope, interface, or tradeoff decisions that require the user's judgment.
3. Use `domain-modeling` when ambiguity in domain concepts, terminology, entities, invariants, or relationships is itself material to the work. Do not invoke it merely because the task has domain vocabulary.
4. Ask one focused question at a time when an answer materially changes subsequent work. Do not manufacture decisions or continue interviewing after the remaining uncertainty is immaterial.
5. Preserve important resolved decisions when they have meaningful cross-context value. Reuse the work's existing durable artifact or follow the project's configured durable-state convention rather than creating a parallel location. Use a local working-state area when detailed or provisional state should survive contexts but does not belong in shared project documentation. If choosing a new location or source of truth is material, follow the governing consultation rules. Keep status accurate: distinguish explicit decisions from discovered facts, working assumptions, and unresolved points. Preserve the compressed decision state, not a question-and-answer transcript.
6. When enough is known for the next phase, stop. Do not turn clarification into an open-ended requirements exercise or create durable files for information that is immediately consumed and cheap to reconstruct.

Follow the governing project or user instructions for consultation, checkpoints, documentation, and issue-tracker behavior.
