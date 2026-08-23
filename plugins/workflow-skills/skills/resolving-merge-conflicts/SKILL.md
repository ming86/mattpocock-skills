---
name: resolving-merge-conflicts
description: "Resolve an in-progress Git merge or rebase conflict by recovering the intent, invariants, and relevant constraints behind both sides from repository evidence. Use when Git has stopped on conflicts that cannot be solved safely by choosing ours/theirs; report genuinely incompatible intent instead of inventing a compromise."
disable-model-invocation: true
---

# Resolving Merge Conflicts

Resolve conflicts as disagreements between changes made for reasons, not as blocks of text to delete until Git becomes clean.

Use this skill when a merge or rebase is already in progress and Git has stopped on conflicts. If the operation completed but the resulting code now behaves incorrectly, use a debugging workflow instead.

## Process

1. **Establish the operation and goal.** Inspect `git status`, the relevant history, and the conflicting files. Understand what is being merged or rebased and the intended outcome of the operation before editing conflict hunks.
2. **Recover the intent and invariants of both sides.** For each substantive conflict, trace the changes to the strongest available primary evidence: commits and commit messages, surrounding diffs, tests, repository history, linked issues or pull requests, specifications, and nearby code. Identify the behavior, invariants, and relevant constraints each side was meant to preserve or change. Do not ask the user for facts the repository can establish directly.
3. **Compare the intent behind both sides.** Determine whether the intents are compatible, one side supersedes the other, or they are genuinely incompatible. Distinguish established evidence from inference.
4. **Resolve the behavior, not just the text.** Preserve compatible intent, invariants, and relevant constraints. When one side is clearly superseded, retain the current intended behavior rather than mechanically preserving both texts. Do not invent new product behavior merely to make two incompatible changes coexist.
5. **Report important incompatibility.** If the evidence does not establish which intent should win, leave that intent unresolved rather than silently choosing. Do the same when the choice would materially change behavior, scope, compatibility, or architecture.
6. **Validate the result.** Use the smallest credible checks that establish the reconciled behavior: focused tests, typechecking, formatting, integration checks, or broader suites when project practice or consequences justify them. Pay particular attention to behavior that existed on either side before the conflict.
7. **Separate resolution mechanics from operation-level decisions.** The result of this skill is a reconciled worktree or index for the conflicted paths. Continuing a rebase, creating a commit, aborting the operation, or changing merge strategy are separate Git-workflow decisions.

For a large or multi-session conflict resolution, preserve important intent findings, unresolved tradeoffs, and evidence pointers when losing them across context replacement would be expensive. Reuse the work's existing durable location and project conventions rather than creating a conflict-specific diary.

## Review standard

A good resolution should make it possible to explain, for every material conflict:

- what each side was trying to preserve or change;
- which evidence established that intent;
- how the resulting code preserves compatible intent or why one behavior was superseded;
- what validation established that the reconciliation works;
- which material uncertainty, if any, still requires a project or user decision.
