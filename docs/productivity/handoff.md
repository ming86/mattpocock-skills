# Handoff

## What it does

`handoff` compacts the useful state of the current conversation into a portable Markdown document for another executor or environment. It writes the file to the operating system's temporary directory rather than adding a project artifact by default.

The value is portability. Durable specs, issues, ADRs, commits, diffs, and other existing sources are referenced rather than copied into the handoff.

## When to reach for it

Use it when the next executor cannot directly access the current context, for example:

- moving between agent harnesses;
- moving to a different repository or directory;
- handing work to a colleague;
- transferring a bounded side task to another environment.

Do not create a handoff merely because a planning or implementation phase ended. If the next executor already has the required durable project state, another summary may only duplicate information and drift.

## What to include

Capture only the live state another executor would otherwise miss:

- the current objective and bounded next task;
- material decisions, assumptions, and unresolved points that are not already durable elsewhere;
- relevant paths or URLs to specs, issues, commits, diffs, or other sources;
- important validation state or known limitations;
- suggested skills that may help the next executor.

Redact secrets and sensitive information.

## Common questions

**Is a handoff the same as durable project memory?**

No. A handoff is a transit document. Important state that multiple future contexts need should normally live in the repository, issue tracker, spec, or another established durable artifact.

**Should I paste existing specs and diffs into it?**

No. Point to the authoritative source instead. Copy only the task-local context that would otherwise be lost.

**What if the temporary file will not survive long enough?**

Move it to an appropriate durable location when the transfer requires that lifetime. The skill defaults to temp so one-off handoffs do not become repository clutter.

**How does this relate to `prototype` or `ask-matt`?**

A prototype may run in another context when isolation is useful, but it does not require a handoff if the executor can already read the relevant durable state. [`ask-matt`](../../skills/engineering/ask-matt/SKILL.md) routes by the work's actual need rather than through a fixed phase-boundary tree.

## It's working if

A fresh executor can start the bounded next task without asking for the conversation to be replayed, authoritative artifacts remain the single source of truth, and the handoff contains no secrets or unnecessary history.
