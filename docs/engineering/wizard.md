# Wizard

## What it does

`wizard` generates an interactive shell procedure for steps that genuinely require a human, such as entering credentials, using a third-party dashboard, or confirming an irreversible migration step.

It turns a manual sequence into a repeatable, inspectable script while keeping secrets out of displayed output and requiring human confirmation at the relevant stages.

## When to reach for it

Use it when the agent cannot perform important steps itself and the human would otherwise have to follow a long, error-prone manual checklist.

Do not create a wizard for operations the agent can perform reliably with existing tools.

## Common questions

**Does the generated wizard belong in the repository?**

Not by default. It can be disposable for a one-off operation. If the user wants a repeatable project setup path, follow the repository's normal documentation, scope, and commit conventions before making it permanent.

**Should the agent run it end to end?**

No when it opens browsers, waits for human input, or performs user-owned actions. Validate the script statically and with shell tooling, then give the user the command to run it.

## It's working if

The human sees one clear stage at a time, secret values are captured safely, irreversible actions require confirmation, and every captured value reaches the destination established during planning.
