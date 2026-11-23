---
name: grilling
description: "Clarify immediate uncertainty with focused questions when the next plan, design, or step depends on user input. Ground questions in the current task and context, resolve each uncertainty through the best-suited source, and stop once remaining uncertainty no longer changes or blocks the next step."
---

# Grilling

Clarify only what is needed to move the work forward. Start from the next useful step and enough of the current task and system context to recognize which uncertainties could lead to different work.

Focus on unresolved questions whose plausible answers could change the work or unblock progress. Lower-impact uncertainty can remain open until it becomes relevant.

## Process

1. Identify what the clarification is trying to unblock: a plan, specification, implementation, direction, behavior, or other next step. Understand enough of the relevant task, code, system, and current direction to know which uncertainties could change that work.
2. Identify what is still unclear and what different plausible answers would change. Prioritize questions whose answers could change the work or unblock the next useful step.
3. Resolve each uncertainty through the source best suited to answer it:
   - inspect code, documentation, tools, runtime behavior, history, or other relevant project sources for current system behavior and context;
   - use engineering judgment for ordinary implementation choices that fit the current direction;
   - use an experiment or prototype when the answer has to be learned by trying something;
   - ask the user when their intent, priorities, acceptable behavior, tradeoffs, or direction determine how the work should proceed.
4. Use each source according to what it can actually show. Keep direct observations, reasonable inferences, working assumptions, and user choices distinguishable when later work depends on that distinction.
5. When useful questions depend on an interpretation of the existing system or intended direction that may not be shared with the user, make that understanding visible before going deeper.
6. Ask focused questions that are ready to answer. Prefer one question at a time when later questions depend on the answer. Group independent questions when that reduces unnecessary back-and-forth without making them harder to answer.
7. Give a recommended answer when the current context supports one, together with the reason or tradeoff that matters. For a binary question with a recommendation, phrase it so answering “yes” accepts the recommendation. Keep a free-text path open when the provided choices are not exhaustive.
8. Reassess after each answer or new finding. Retire questions that no longer affect the work and surface newly exposed questions when they could change or unblock what happens next.
9. Stop when the remaining uncertainty no longer changes or blocks useful progress. Preserve unresolved points according to the calling workflow rather than forcing closure.

When later contexts need the conclusions or open questions, save a compact summary (conclusions, reasons, status, and source references—not a transcript) in the work's existing location per project conventions, in local working state for provisional detail, or in the simplest work-centered location when no convention exists.

Bring questions about the user's intent, priorities, acceptable behavior, tradeoffs, or direction back to the user when they affect how the work should proceed.

When another skill calls `grilling`, follow that skill's narrower purpose, documentation behavior, and stopping conditions.
