# Resolving Merge Conflicts

## What it does

`resolving-merge-conflicts` recovers the intent behind both sides of an in-progress merge or rebase and uses that evidence to resolve compatible changes coherently.

The skill does not treat completion of the Git operation as automatic authorization. Aborting, continuing, staging, and committing remain governed by the current task and project instructions.

## When to reach for it

Use it when conflict markers represent overlapping changes whose intended behavior needs to be reconstructed from history, issues, plans, tests, or surrounding code.

Mechanical conflicts whose correct resolution is already obvious may not need the full procedure.

## Common questions

**Should the agent always preserve both sides?**

Only when both intents remain compatible with the current direction. Superseded behavior should not survive merely because it appears on one side of the conflict.

**What if the two sides encode incompatible product or architecture decisions?**

If the governing direction does not resolve the choice, surface it through the project's consultation process rather than inventing a decision to finish the merge.

**Does the skill automatically commit the resolution?**

No. It validates the resolved state, while completion and delivery actions remain under project policy and user authorization.

## It's working if

The resolved tree reflects the current intended behavior, material incompatibilities are visible rather than guessed away, and the relevant validation establishes that the merge did not introduce a regression.
