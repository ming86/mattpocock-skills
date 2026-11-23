---
name: grill-with-docs
description: "Clarify important product, design, domain, or direction questions using project context and user input. Use before dependent work when unresolved questions could change scope, behavior, interfaces, or direction; preserve the resulting state when later contexts will need it."
disable-model-invocation: true
---

# Grill With Docs

Use this skill when important uncertainty remains and project context can narrow the questions before the user needs to weigh in. Build enough understanding of the current system and task to know which questions are actually relevant.

## Process

1. Inspect the conversation, codebase, documentation, ADRs, runtime information, and other relevant project sources first. Use them to understand the current system and task, and keep what those sources directly show separate from conclusions about intent, requirements, or direction.
2. Use `grilling` when important uncertainty remains and resolving it depends on the user's intent, priorities, acceptable behavior, tradeoffs, or direction.
3. Use `domain-modeling` when unclear domain concepts, terminology, entities, rules, or relationships are preventing the work from being understood or the right questions from being asked.
4. Preserve the resulting state when later contexts need it—reusing the work's existing location per project conventions, local working state for provisional detail, or the simplest work-centered location when no convention exists. Keep project findings, user decisions, working assumptions, and unresolved points distinct, saving current state rather than a Q&A transcript.
