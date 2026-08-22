---
name: grilling
description: "Clarify important decisions with focused questions when the next plan, design, or step depends on user judgment. Inspect available evidence first, ask only what the user needs to decide, and stop once the remaining uncertainty no longer blocks useful progress."
---

# Grilling

Ask the user only enough to reach the shared understanding needed for the next step. Resolve important ambiguity without exploring every possible branch of the problem.

Track unresolved decisions and their dependencies. Focus on decisions that are ready to answer now because their prerequisites are already settled.

## Process

1. Establish what the clarification is trying to unblock: a decision, plan, specification, implementation, or other next step.
2. Inspect available evidence before asking factual questions. Facts that can be established from the filesystem, codebase, tools, documentation, or other available sources are the agent's job to investigate.
3. Identify unresolved user-owned decisions that could meaningfully change the next step. Do not invent questions for minor edge cases, speculative future needs, or details that can safely remain open.
4. Ask focused questions that are ready to answer. Prefer one decision at a time when later questions depend on it. Group independent questions only when that reduces unnecessary back-and-forth without making the decision harder.
5. Give a recommended answer when the available evidence supports one, together with the reason or tradeoff that matters. Keep a free-text path open when the provided choices are not exhaustive.
6. Reassess the open decisions after each answer or new piece of evidence. Drop questions that no longer matter and add newly exposed questions only when they affect the goal.
7. Stop when the remaining uncertainty no longer blocks the intended next step in a meaningful way. Preserve unresolved points according to the calling workflow instead of forcing a decision.

When later contexts would otherwise have to reconstruct important decisions or open questions, preserve a compact summary in the work's existing durable location or follow the project's durable-state convention. Use local working state for detailed or provisional information that should survive contexts but does not belong in shared project documentation. If no convention exists, choose the simplest permitted work-centered location for a low-impact choice; consult the project or user when choosing a new location or source of truth would itself be important. Record conclusions, reasons, status, and evidence pointers rather than an interview transcript. Do not create a file for clarification that will be used immediately and is cheap to reconstruct.

User decisions remain the user's. Do not silently choose a material product, scope, interface, operational, or tradeoff decision merely to finish the interview.

When another skill calls `grilling`, follow that skill's narrower purpose, documentation behavior, and stopping conditions. Follow governing project or user instructions for consultation and checkpoints.
