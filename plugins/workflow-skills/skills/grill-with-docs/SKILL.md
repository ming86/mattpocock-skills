---
name: grill-with-docs
description: Clarify material product, design, or domain decisions before dependent work, while recording durable decisions when useful.
---

# Grill With Docs

Use this skill when unresolved decisions or domain ambiguity would materially affect the work. The goal is not to maximize the number of questions; it is to reach enough shared understanding for the next meaningful phase to proceed reliably.

## Process

1. Inspect the available conversation, codebase, documentation, ADRs, and other project evidence first. Resolve factual questions from evidence when practical instead of asking the user to supply facts the agent can establish itself.
2. Use `grilling` for material product, behavior, scope, interface, or tradeoff decisions that require the user's judgment.
3. Use `domain-modeling` when ambiguity in domain concepts, terminology, entities, invariants, or relationships is itself material to the work. Do not invoke it merely because the task has domain vocabulary.
4. Ask one focused question at a time when an answer materially changes subsequent work. Do not manufacture decisions or continue interviewing after the remaining uncertainty is immaterial.
5. Preserve important resolved decisions in the project's existing durable artifacts when useful. Keep their status accurate: distinguish explicit decisions from discovered facts, working assumptions, and unresolved points.
6. When enough is known for the next phase, stop. Do not turn clarification into an open-ended requirements exercise.

Follow the governing project or user instructions for consultation, checkpoints, documentation, and issue-tracker behavior.