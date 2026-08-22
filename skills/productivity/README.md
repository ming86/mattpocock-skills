# Productivity

General workflow tools that are not code-specific.

## User-invoked

Reachable only when you type them (Claude Code: `disable-model-invocation: true`; Codex: `policy.allow_implicit_invocation: false` in `agents/openai.yaml`).

- **[grill-me](./grill-me/SKILL.md)**: Run a focused interview until the material ambiguity in a plan, design, decision, or idea is resolved.
- **[handoff](./handoff/SKILL.md)**: Compact useful context into a portable handoff so another executor or environment can continue.
- **[teach](./teach/SKILL.md)**: Teach a concept across sessions using the current directory as a stateful workspace.
- **[to-questionnaire](./to-questionnaire/SKILL.md)**: Turn missing input from another person into a questionnaire they can answer asynchronously or in a meeting.
- **[wait-what](./wait-what/SKILL.md)**: Re-explain a message that did not land, using the context the reader was missing.

## Model-invoked

Model- or user-reachable.

- **[grilling](./grilling/SKILL.md)**: Clarify material user-owned decisions using focused questions and evidence the agent can gather itself.
- **[writing-for-agents](./writing-for-agents/SKILL.md)**: Guidance for skills, agent instructions, and other documents primarily consumed by agents.
