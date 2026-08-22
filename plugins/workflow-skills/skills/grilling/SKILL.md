---
name: grilling
description: "Clarify material decisions through focused questions when user judgment is needed before a plan, design, or next step can proceed. Use for interactive ambiguity resolution after inspecting available evidence; stop once remaining uncertainty is immaterial."
---

# Grilling

Interview the user until there is enough shared understanding for the intended next step to proceed reliably. The goal is to resolve material ambiguity, not to visit every theoretically possible branch of a design tree.

Model the unresolved decisions and their dependencies. The **frontier** is the set of material decisions whose prerequisites are already settled and that can usefully be answered now.

## Process

1. Establish what the clarification is trying to unblock: a decision, plan, specification, implementation, or other next step.
2. Inspect available evidence before asking factual questions. Facts that can be established from the filesystem, codebase, tools, documentation, or other available sources are the agent's job to investigate.
3. Identify unresolved user-owned decisions that would materially change the next step. Do not manufacture questions for immaterial edge cases, speculative future needs, or detail that can safely remain open.
4. Ask focused questions from the current frontier. Prefer one decision at a time when later questions depend on it. Independent questions may be grouped when doing so reduces unnecessary back-and-forth without making the user's decision harder.
5. Give a recommended answer when the available evidence supports one, together with the reason or tradeoff that matters. Keep a free-text path open when the provided choices are not exhaustive.
6. Recompute the frontier after each answer or evidence-gathering result. Retire questions that become irrelevant and add newly exposed questions only when they materially affect the goal.
7. Stop when the remaining uncertainty no longer materially blocks the intended next step. Preserve unresolved points according to the calling workflow instead of forcing arbitrary closure.

When clarification produces decisions or unresolved points that later contexts would otherwise have to reconstruct, preserve the compact current state in the work's existing durable location or according to the project's configured durable-state convention. A local working-state area is appropriate when detailed or provisional state should survive contexts but does not belong in a shared project artifact. If no convention exists, use the simplest permitted work-centered artifact when the location choice is low-impact; follow governing project or user consultation when the location, authority, or promotion of the artifact is material. Record conclusions, rationale, status, and evidence pointers rather than a transcript of the interview. Do not create a file for clarification that is immediately consumed and cheap to reconstruct.

User decisions remain the user's. Do not silently choose a material product, scope, interface, operational, or tradeoff decision merely to finish the interview.

When another skill calls `grilling`, follow that skill's narrower purpose, documentation behavior, and stopping conditions. Follow governing project or user instructions for consultation and checkpoints.
