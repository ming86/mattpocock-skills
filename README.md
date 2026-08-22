# Agent Engineering Skills

This is an adapted fork of [Matt Pocock's skills](https://github.com/mattpocock/skills). It keeps the useful engineering procedures while making them complementary to project-level agent policy such as `AGENTS.md`, rather than a second orchestration framework.

The upstream project and original skill set are MIT licensed. See [LICENSE](./LICENSE) and [FORK.md](./FORK.md) for the adaptation principles used here.

## What changed in this fork

The central rule is simple: project and user instructions own engineering policy; skills provide optional procedures for particular situations.

- Use process in proportion to the work. A small clear change should not need a spec, ticket graph, prototype, TDD cycle, and multiple review gates just because those tools exist.
- Preserve durable state when work must survive fresh agent contexts. Important decisions, constraints, dependencies, and unresolved points belong in project artifacts rather than only in conversation history.
- Decompose at meaningful behavior, ownership, dependency, and reasoning boundaries. Vertical slices are useful when they fit the work, not a universal rule.
- Prototype to resolve a concrete uncertainty. Disposable code is evidence, not automatically production code.
- Keep requirement status accurate. Do not silently turn guesses, examples, tentative preferences, or working assumptions into requirements.
- Let implementation surface invalidated assumptions instead of blindly preserving an obsolete plan.
- Separate focused implementation conformance review from broader independent criticism. A critic agent such as `rubber-duck` can complement `code-review` without being embedded inside it.

## Installation

Choose one installation model for a given agent so you do not end up with duplicate copies of the same skills.

### Claude Code

Add this fork as a marketplace, then install its plugin:

```text
/plugin marketplace add ming86/mattpocock-skills
/plugin install mattpocock-skills@ming86
```

The marketplace follows this repository, so updates come from the fork rather than the upstream official listing.

### Codex and other agents

```bash
npx skills@latest add ming86/mattpocock-skills
```

Pick the skills you actually want and the coding agents to install them on. `setup-matt-pocock-skills` is optional; install it only when a repository needs shared issue-tracker, triage-label, or domain-document configuration.

## Choosing a workflow

There is no mandatory main flow. Start from what the current work actually needs.

| Situation | Useful skill |
| --- | --- |
| Clear, bounded work ready to build | `implement`, or direct work if no skill adds value |
| Material product, scope, interface, or domain ambiguity | `grill-with-docs` |
| An executable experiment can answer an important question | `prototype` |
| Reasoning must survive several contexts and the route is still unclear | `wayfinder` |
| Settled decisions need a durable implementation description | `to-spec` |
| Work benefits from coherent dependency-aware execution units | `to-tickets` |
| A bounded change needs focused implementation conformance review | `code-review` |

These can compose when the task genuinely needs several of them. For example, a large uncertain effort may move through `wayfinder`, then `to-spec`, then `to-tickets`; a small feature may go directly to `implement`; a UI decision may use `prototype` and then return directly to the current plan.

The historical `ask-matt` router remains available for compatibility, but it now routes by task need instead of forcing every task through one fixed chain.

## Long-running agent work

The intended model for long-running work is not one conversation remembering the whole project. Durable state carries the project across bounded execution contexts:

```text
human intent
    |
    v
decisions and evidence
    |
    v
durable spec / map / work graph
    |
    +--> focused execution context
    +--> focused execution context
    +--> focused execution context
    |
    v
integrated repository state and verification
```

Fresh contexts are useful when they isolate reasoning, reduce irrelevant history, or allow independent work. They are harmful when decomposition cuts through tightly coupled reasoning. The governing agent policy decides when delegation, parallelism, checkpoints, and independent review are appropriate.

## Reference

### Engineering

**User-invoked**

- **[ask-matt](./skills/engineering/ask-matt/SKILL.md)**: Choose the smallest useful skill or workflow for the current situation.
- **[grill-with-docs](./skills/engineering/grill-with-docs/SKILL.md)**: Clarify material decisions and domain ambiguity while recording durable decisions when useful.
- **[triage](./skills/engineering/triage/SKILL.md)**: Move incoming issues through a triage workflow.
- **[improve-codebase-architecture](./skills/engineering/improve-codebase-architecture/SKILL.md)**: Survey a codebase for concrete architecture-improvement opportunities.
- **[setup-matt-pocock-skills](./skills/engineering/setup-matt-pocock-skills/SKILL.md)**: Optionally configure shared tracker, triage-label, and domain-document conventions.
- **[to-spec](./skills/engineering/to-spec/SKILL.md)**: Turn established conversation and project context into a durable implementation spec without reopening settled discussion.
- **[to-tickets](./skills/engineering/to-tickets/SKILL.md)**: Break established work into coherent dependency-aware units suited to focused execution contexts.
- **[implement](./skills/engineering/implement/SKILL.md)**: Implement bounded work while preserving scope and surfacing materially invalidated assumptions.
- **[wayfinder](./skills/engineering/wayfinder/SKILL.md)**: Externalize durable decision state for large, uncertain, or multi-session work whose route is not yet clear.

**Model-invoked**

- **[prototype](./skills/engineering/prototype/SKILL.md)**: Build the cheapest credible throwaway artifact that can answer one material design or feasibility question.
- **[diagnosing-bugs](./skills/engineering/diagnosing-bugs/SKILL.md)**: Use a disciplined evidence loop for difficult bugs and performance regressions.
- **[research](./skills/engineering/research/SKILL.md)**: Investigate a question against high-trust sources and preserve the evidence when later work needs it.
- **[tdd](./skills/engineering/tdd/SKILL.md)**: Use a red-green-refactor loop when test-first development fits the task and project.
- **[domain-modeling](./skills/engineering/domain-modeling/SKILL.md)**: Sharpen domain vocabulary, relationships, and durable domain decisions.
- **[codebase-design](./skills/engineering/codebase-design/SKILL.md)**: Reason about module depth, interfaces, seams, and codebase structure.
- **[code-review](./skills/engineering/code-review/SKILL.md)**: Review a bounded change independently for Intent / Spec and Repository / Implementation conformance.
- **[resolving-merge-conflicts](./skills/engineering/resolving-merge-conflicts/SKILL.md)**: Resolve an in-progress merge or rebase by tracing each side's intent.
- **[wizard](./skills/engineering/wizard/SKILL.md)**: Generate a human-operated procedure for steps the agent genuinely cannot perform itself.

### Productivity

**User-invoked**

- **[grill-me](./skills/productivity/grill-me/SKILL.md)**: Run a focused interview until the material ambiguity in a plan, design, decision, or idea is resolved.
- **[handoff](./skills/productivity/handoff/SKILL.md)**: Compact useful context into a portable handoff for another executor or environment.
- **[teach](./skills/productivity/teach/SKILL.md)**: Teach a concept across sessions using the current directory as a stateful workspace.
- **[to-questionnaire](./skills/productivity/to-questionnaire/SKILL.md)**: Turn missing input from another person into a questionnaire they can answer asynchronously.
- **[wait-what](./skills/productivity/wait-what/SKILL.md)**: Re-explain a message that did not land, using the context the reader was missing.

**Model-invoked**

- **[grilling](./skills/productivity/grilling/SKILL.md)**: Clarify material user-owned decisions using focused questions and environment evidence.
- **[writing-for-agents](./skills/productivity/writing-for-agents/SKILL.md)**: Guidance for skills, agent instructions, and other documents primarily consumed by agents.
