---
name: resolving-merge-conflicts
description: "Resolve an in-progress Git merge or rebase conflict by understanding what each side was trying to preserve or change from the code, history, tests, and related project context. Use when Git has stopped on conflicts that cannot be solved safely by choosing ours/theirs; report genuinely incompatible intent instead of inventing a compromise."
disable-model-invocation: true
---

# Resolving Merge Conflicts

Resolve conflicts as disagreements between changes made for reasons, not as blocks of text to delete until Git becomes clean.

Use this skill when a merge or rebase is already in progress and Git has stopped on conflicts. If the operation completed but the resulting code now behaves incorrectly, use a debugging workflow instead.

## Process

1. **Establish the operation and goal.** Inspect `git status`, the relevant history, and the conflicting files. Understand what is being merged or rebased and the intended outcome of the operation before editing conflict hunks.
2. **Recover what both sides were trying to preserve or change.** For each important conflict, trace the changes through the most direct available sources: commits and commit messages, surrounding diffs, tests, repository history, linked issues or pull requests, specifications, and nearby code. Identify the behavior, rules, and constraints each side was meant to preserve or change. Do not ask the user for facts the repository can establish directly.
3. **Compare the intent behind both sides.** Determine whether the intents are compatible, one side has replaced the other, or they are genuinely incompatible. Separate what the repository shows from what you are inferring.
4. **Resolve the behavior, not just the text.** Preserve compatible intent, rules, and relevant constraints. When one side has clearly replaced the other, retain the current intended behavior rather than mechanically preserving both texts. Do not invent new product behavior merely to make two incompatible changes coexist.
5. **Report important incompatibility.** If the repository history and surrounding context do not make clear which intent should win, leave that unresolved rather than silently choosing. Do the same when the choice would significantly change behavior, scope, compatibility, or architecture.
6. **Validate the result.** Use the smallest credible checks that establish the reconciled behavior: focused tests, typechecking, formatting, integration checks, or broader suites when project practice or consequences justify them. Pay particular attention to behavior that existed on either side before the conflict.
7. **Separate resolution mechanics from operation-level decisions.** The result of this skill is a reconciled worktree or index for the conflicted paths. Continuing a rebase, creating a commit, aborting the operation, or changing merge strategy are separate Git-workflow decisions.

For a large or multi-session conflict resolution, save important intent findings, unresolved tradeoffs, and useful references when losing them across context replacement would be expensive. Reuse the work's existing location and project conventions rather than creating a conflict-specific diary.

## Review standard

A good resolution should make it possible to explain, for every important conflict:

- what each side was trying to preserve or change;
- which code, history, tests, or project context showed that intent;
- how the resulting code preserves compatible intent or why one behavior replaced another;
- what validation showed that the reconciliation works;
- which unresolved issue, if any, still requires a project or user decision.
