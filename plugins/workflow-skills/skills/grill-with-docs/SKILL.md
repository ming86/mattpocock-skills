---
name: grill-with-docs
description: "Clarify important product, design, or domain decisions using both repository evidence and user judgment. Use before dependent work when unresolved choices could change scope, behavior, interfaces, or direction; preserve decisions when later contexts will need them."
disable-model-invocation: true
---

# Grill With Docs

Use this skill when unresolved decisions or domain ambiguity could meaningfully affect the work. Ask only enough to reach the shared understanding needed for the next useful phase.

## Process

1. Inspect the conversation, codebase, documentation, ADRs, and other project evidence first. Resolve factual questions from that evidence when practical instead of asking the user for facts the agent can find itself.
2. Use `grilling` for material product, behavior, scope, interface, or tradeoff decisions that require the user's judgment.
3. Use `domain-modeling` when ambiguity in domain concepts, terminology, entities, invariants, or relationships is itself material to the work. Do not invoke it merely because the task has domain vocabulary.
4. Ask one focused question at a time when an answer materially changes subsequent work. Do not manufacture decisions or continue interviewing after the remaining uncertainty is immaterial.
5. Preserve important decisions when later contexts will need them. Reuse the work's existing durable location or follow the project's durable-state convention instead of creating a parallel one. Use local working state for detailed or provisional information that should survive contexts but does not belong in shared project documentation. If choosing a new location or source of truth is important, follow the project's consultation rules. Keep facts, decisions, assumptions, and unresolved points clearly distinguished. Save the current decision state, not a question-and-answer transcript.
6. Stop when enough is known for the next phase. Do not turn clarification into an open-ended requirements exercise or create files for information that will be used immediately and is cheap to reconstruct.

Follow the governing project or user instructions for consultation, checkpoints, documentation, and issue-tracker behavior.
