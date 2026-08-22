---
name: resolving-merge-conflicts
description: "Use when you need to understand and resolve an in-progress git merge or rebase conflict without losing either side's intent."
---

# Resolving Merge Conflicts

Resolve conflicts from the intent that produced each side, not by mechanically choosing ours or theirs.

Follow the governing project and user instructions for whether the merge or rebase should be completed, aborted, staged, committed, or paused for consultation. This skill provides the resolution procedure; it does not authorize delivery actions by itself.

## Process

1. **Establish the current state.** Inspect the merge or rebase status, conflicting files, relevant history, and the exact operation in progress. Do not assume that completing the operation is still the desired outcome when the surrounding task says otherwise.

2. **Find the primary sources.** For each substantive conflict, understand why both sides changed. Read the relevant commits, issues, pull requests, plans, tests, or nearby code needed to recover intent.

3. **Resolve compatible intent.** Preserve both sides when they can coexist coherently. Where the intents are incompatible and the current task or repository evidence clearly establishes which one governs, resolve accordingly without inventing new behavior.

4. **Surface material choices.** If an incompatible conflict represents a material product, behavior, architecture, compatibility, or operational decision that cannot be resolved from established direction, stop that path and use the governing consultation process. Do not make a new material decision merely to finish the merge.

5. **Validate the resolved state.** Run the focused checks that establish the merge did not break the affected behavior. Expand validation only when project practice or the consequences of the change justify it.

6. **Finish only when authorized.** Continue the merge or rebase, stage files, create commits, or abort the operation only when those actions are part of the requested scope and permitted by governing project instructions. Report any unresolved choice or validation gap before dependent work continues.
