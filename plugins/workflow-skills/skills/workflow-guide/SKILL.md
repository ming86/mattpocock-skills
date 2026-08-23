---
name: workflow-guide
description: "Identify relevant explicit workflow skills for the current work. Use when deciding among the plugin's explicit workflows for clarification, experiments, long-running work, specs, task decomposition, implementation, review, conflict resolution, handoff, or decisions owned by another person."
---

# Workflow Guide

Use this guide to identify explicit workflow skills that fit the current situation.

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

Implicit analytical skills such as `research`, `grilling`, `diagnosing-bugs`, `tdd`, `domain-modeling`, and `codebase-design` route normally.
