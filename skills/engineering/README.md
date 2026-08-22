# Engineering

Composable procedures for engineering work. Project and user instructions remain authoritative for scope, orchestration, delegation, consultation, checkpoints, validation, commits, and independent review.

There is no mandatory sequence. Use a skill when its procedure solves a concrete problem in the current work.

## User-invoked

Reachable only when you type them (Claude Code: `disable-model-invocation: true`; Codex: `policy.allow_implicit_invocation: false` in `agents/openai.yaml`).

- **[ask-matt](./ask-matt/SKILL.md)**: Choose the smallest useful skill or workflow for the current situation.
- **[grill-with-docs](./grill-with-docs/SKILL.md)**: Clarify material decisions and domain ambiguity while recording durable decisions when useful.
- **[triage](./triage/SKILL.md)**: Move incoming issues through a triage workflow.
- **[improve-codebase-architecture](./improve-codebase-architecture/SKILL.md)**: Survey a codebase for concrete architecture-improvement opportunities.
- **[setup-matt-pocock-skills](./setup-matt-pocock-skills/SKILL.md)**: Optionally configure shared tracker, triage-label, and domain-document conventions when the repository lacks them.
- **[to-spec](./to-spec/SKILL.md)**: Turn established conversation and project context into a durable implementation spec without reopening settled discussion.
- **[to-tickets](./to-tickets/SKILL.md)**: Break established work into coherent dependency-aware units suited to focused execution contexts.
- **[implement](./implement/SKILL.md)**: Implement bounded work while preserving scope and surfacing materially invalidated assumptions.
- **[wayfinder](./wayfinder/SKILL.md)**: Externalize durable decision state for large, uncertain, or multi-session work whose route is not yet clear.

## Model-invoked

Model- or user-reachable.

- **[prototype](./prototype/SKILL.md)**: Build the cheapest credible throwaway artifact that can answer one material design or feasibility question.
- **[diagnosing-bugs](./diagnosing-bugs/SKILL.md)**: Use a disciplined evidence loop for difficult bugs and performance regressions.
- **[research](./research/SKILL.md)**: Investigate a question against high-trust sources and preserve the evidence when later work needs it.
- **[tdd](./tdd/SKILL.md)**: Use a red-green-refactor loop when test-first development fits the task and project.
- **[domain-modeling](./domain-modeling/SKILL.md)**: Sharpen domain vocabulary, relationships, and durable domain decisions.
- **[codebase-design](./codebase-design/SKILL.md)**: Reason about module depth, interfaces, seams, and codebase structure.
- **[code-review](./code-review/SKILL.md)**: Review a bounded change independently for Intent / Spec and Repository / Implementation conformance.
- **[resolving-merge-conflicts](./resolving-merge-conflicts/SKILL.md)**: Resolve an in-progress merge or rebase by tracing each side's intent.
- **[wizard](./wizard/SKILL.md)**: Generate a human-operated procedure for steps the agent genuinely cannot perform itself.
