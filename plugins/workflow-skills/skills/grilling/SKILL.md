---
name: grilling
description: "Clarify uncertainty with focused questions when the next plan, design, or step depends on input from the user. Ground the questions in current project context, resolve each uncertainty through the source best suited to answer it, and stop once the remaining uncertainty no longer changes or blocks useful progress."
---

# Grilling

Clarify only what is needed to move the work forward. Start from the next useful step and enough of the current task and system context to recognize which uncertainties could lead to different work.

Focus on unresolved questions whose plausible answers could change the work or unblock progress. Lower-impact uncertainty can remain open until it becomes relevant.

## Process

1. Establish what the clarification is trying to unblock: a plan, specification, implementation, direction, behavior, or other next step. Understand enough of the relevant task, code, system, and current direction to know which uncertainties could change that work.
2. Identify what is still unclear and what different plausible answers would change. Prioritize questions whose answers could change the work or unblock the next useful step.
3. Resolve each uncertainty through the source best suited to answer it:
   - inspect code, documentation, tools, runtime behavior, history, or other relevant project sources for current system behavior and context;
   - use engineering judgment for ordinary implementation choices that fit the current direction;
   - use an experiment or prototype when the answer has to be learned by trying something;
   - ask the user when their intent, priorities, acceptable behavior, tradeoffs, or direction determine how the work should proceed.
4. Use each source according to what it can actually show. Keep direct observations, reasonable inferences, working assumptions, and user choices distinguishable when later work depends on that distinction.
5. When useful questions depend on an interpretation of the existing system or intended direction that may not be shared with the user, make that understanding visible before going deeper.
6. Ask focused questions that are ready to answer. Prefer one question at a time when later questions depend on the answer. Group independent questions when that reduces unnecessary back-and-forth without making them harder to answer.
7. Give a recommended answer when the current context supports one, together with the reason or tradeoff that matters. Keep a free-text path open when the provided choices are not exhaustive.
8. Reassess after each answer or new finding. Retire questions that no longer affect the work and surface newly exposed questions when they could change or unblock what happens next.
9. Stop when the remaining uncertainty no longer changes or blocks useful progress. Preserve unresolved points according to the calling workflow rather than forcing closure.

When later contexts would otherwise have to reconstruct important conclusions or open questions, preserve a compact summary in the work's existing durable location or follow the project's durable-state convention. Use local working state for detailed or provisional information that should survive contexts but does not belong in shared project documentation. If no convention exists, use the simplest work-centered location that fits the clarification state. Record conclusions, reasons, status, and useful source references rather than an interview transcript. A separate clarification file is useful when later contexts need the state or reconstructing it would be costly.

Bring questions about the user's intent, priorities, acceptable behavior, tradeoffs, or direction back to the user when they affect how the work should proceed.

When another skill calls `grilling`, follow that skill's narrower purpose, documentation behavior, and stopping conditions.
