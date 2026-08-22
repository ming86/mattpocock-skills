---
name: workflow-guide
description: "Advise when the current work has reached a material transition where one explicit workflow skill may help. Use to identify and briefly recommend the nearest deliberate workflow for clarification, empirical uncertainty, long-running work, planning, implementation, review, conflict resolution, handoff, or an external decision owner. Do nothing when ordinary work can continue."
---

# Workflow Guide

Recognize whether one explicit workflow skill is worth proposing. This skill is advisory only: it does not choose the overall workflow or authorize another skill.

The default is to continue ordinary work. Recommend a transition only when it would materially improve the work.

## Explicit workflows

- `grill-with-docs` — material product, design, or domain decisions need user judgment grounded in repository or project evidence before dependent work proceeds.
- `prototype` — a design, behavior, UI, integration, or feasibility question materially affects the work and a small experiment can answer it more cheaply or reliably than more discussion or research.
- `wayfinder` — large, uncertain, or multi-session work needs decisions, evidence, dependencies, and open questions to survive context replacement because an ordinary plan is not yet enough.
- `to-spec` — requirements and decisions that materially shape implementation are settled enough, and later implementation needs a durable reference.
- `to-tickets` — a plan or spec is large enough to benefit from clear dependency-aware work units; keep tightly coupled reasoning together.
- `implement` — a bounded unit of work has established scope and intended outcome and is ready for execution rather than requirements discovery.
- `implementation-review` — a completed bounded implementation needs focused review for correctness, repository integration, regressions, unnecessary complexity, or missed requirements; not broader critique of the plan or approach.
- `resolving-merge-conflicts` — an in-progress Git merge or rebase has conflicts that cannot be resolved safely by choosing ours/theirs and require recovering the intent, invariants, and relevant constraints behind both sides.
- `handoff` — work is deliberately moving to a new context, session, or agent and the next context needs the live state without duplicating settled specs, issues, commits, or other durable artifacts.
- `to-questionnaire` — the current user cannot responsibly supply needed facts or decisions, repository research cannot answer them, and another person or domain expert owns the answer.

This guide advises only on the explicit workflows above. Implicit analytical skills such as `research`, `grilling`, `diagnosing-bugs`, `tdd`, `domain-modeling`, and `codebase-design` route normally.

## How to advise

1. **Prefer ordinary work.** If the work can continue reliably without a workflow transition, recommend nothing.
2. **Match the actual transition.** Choose the nearest explicit skill for what is blocking or materially changing the work. Recommend at most one; do not propose workflow chains.
3. **Ask before entering it.** In a root or user-facing context, name the skill, give the concrete reason it fits now, and ask whether to use it. Do not load, invoke, or simulate the target workflow before approval.
4. **Follow the harness after approval.** If the harness requires user invocation, state the skill name or available command. Do not treat approval alone as invocation.
5. **Workers escalate.** Unless already authorized, delegated workers report a useful workflow transition to the root rather than prompting the user or expanding their assignment.
6. **Honor a decline.** Continue normally and do not ask again unless circumstances materially change.

## Recommendation

Keep it brief:

> `<skill>` fits here because <concrete reason>. Would you like to use it?

Do not turn the recommendation into a workflow plan, skill catalog, or mandatory checkpoint.
