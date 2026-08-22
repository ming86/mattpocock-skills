# Out-of-Scope Knowledge Base

Some repositories deliberately keep a `.out-of-scope/` directory as durable memory for rejected feature directions. Use this convention only when the repository already adopts it, or when the maintainer explicitly wants such a record. Triage does not create a rejection knowledge base by default.

The value of the convention is avoiding repeated reconsideration of a durable decision. Its cost is that temporary or context-specific rejections can become stale policy, so record only reasons that are likely to matter to a future maintainer or agent.

## Directory structure

When the convention is in use, prefer one file per rejected **concept**, not one file per issue:

```text
.out-of-scope/
├── dark-mode.md
├── plugin-system.md
└── graphql-api.md
```

## File content

A useful record states:

- the rejected capability or direction;
- the durable reason for the decision;
- constraints or architecture that make the reason understandable;
- prior requests when linking them materially helps deduplication.

Avoid recording temporary circumstances such as lack of time or current staffing as permanent scope decisions.

## When to consult it

If the repository already has `.out-of-scope/`, consult relevant entries during triage when a new request resembles a previously rejected concept. Match by meaning rather than keyword.

Surface the prior decision to the maintainer rather than treating it as immutable. The current request may reveal that the old reasoning no longer applies.

## When to write or update it

Write or update an entry only when all of these are true:

1. the maintainer has rejected an enhancement direction, not merely deferred it;
2. the repository uses this knowledge-base convention or the maintainer asks to adopt it;
3. preserving the reason has concrete future value, such as preventing likely repeated design work.

Do not record an issue here merely because it is closed as `wontfix`, and do not record requests that are already implemented. A closing comment is sufficient when the rejection reason is not worth making into durable project policy.

When an existing entry applies, update it only with information that remains useful. When the maintainer changes direction, revise or remove the stale record instead of preserving obsolete policy for historical completeness.
