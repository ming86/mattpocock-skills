---
name: grill-with-docs
description: "Clarify material product, design, or domain decisions using both repository evidence and user judgment. Use before dependent work when unresolved choices could materially change scope, behavior, interfaces, or direction; preserve decisions when later contexts will need them."
disable-model-invocation: true
---

# Grill With Docs

Use this skill when unresolved decisions or domain ambiguity could materially affect the work. Ask only enough to reach the shared understanding needed for the next useful phase.

## Process

1. Inspect the conversation, codebase, documentation, ADRs, and other project evidence first. Resolve factual questions from that evidence when practical instead of asking the user for facts the agent can find itself.
2. Call the Skill tool with `grilling` for material product, behavior, scope, interface, or tradeoff decisions that require the user's judgment.
3. Call the Skill tool with `domain-modeling` when ambiguity in domain concepts, terminology, entities, invariants, or relationships is itself material to the work.
4. Preserve important decisions when later contexts will need them. Reuse the work's existing durable location or follow the project's durable-state convention instead of creating a parallel one. Use local working state for detailed or provisional information that should survive contexts but does not belong in shared project documentation. If no convention exists, keep the clarification state in the simplest work-centered location that fits the work. Keep facts, decisions, assumptions, and unresolved points clearly distinguished. Save the current decision state, not a question-and-answer transcript.
