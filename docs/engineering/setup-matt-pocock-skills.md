## What it does

`setup-matt-pocock-skills` optionally establishes shared issue-tracker, triage-label, or domain-document conventions when several skills need them and the repository does not already provide suitable conventions.

The historical name is retained for compatibility. In this fork, setup is configuration rather than a prerequisite or an engineering-policy installer.

## When to reach for it

Type `/setup-matt-pocock-skills` when a repository lacks a clear durable location or convention needed by skills such as `to-spec`, `to-tickets`, `wayfinder`, `triage`, `domain-modeling`, or `grill-with-docs`.

If the project already has an issue tracker, planning-doc convention, domain docs, or triage workflow that those skills can use, no setup is required.

## Prefer what already exists

The skill inspects repository instructions and existing workflow artifacts before proposing configuration. It should reuse established project conventions rather than create parallel ones.

When configuration is genuinely needed, `docs/agents/` is a default location for small pointer documents such as tracker conventions, triage-label mappings, or domain-document layout. It is not mandatory when the repository already has a better home.

The skill must not add orchestration, review, testing, approval, or checkpoint policy to `AGENTS.md` or `CLAUDE.md` as part of setup.

## Common questions

**Do I need to run setup before using any engineering skill?**

No. Many skills need no shared configuration. Run setup only when multiple workflows need a durable convention that is currently missing or ambiguous.

**Will setup replace my existing tracker or docs structure?**

No. Existing suitable conventions take precedence.

## It's working if

- Setup is a no-op when the repository already has enough structure.
- New configuration exists only for real consumers.
- Agent-policy files remain focused on actual project policy rather than skill installation details.

## Where it fits

This is an optional repository configuration tool, not a chain step. [`ask-matt`](../../skills/engineering/ask-matt/SKILL.md) can help decide whether the current work needs it.