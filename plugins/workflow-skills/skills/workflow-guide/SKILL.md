---
name: workflow-guide
description: "Recognize explicit workflow skills that would help the current or approaching work and surface them early enough to be useful. Use throughout the task for clarification, experiments, long-running work, specs, task decomposition, implementation, review, conflict resolution, handoff, or decisions owned by another person."
---

# Workflow Guide

Use this guide throughout the work to recognize explicit workflow skills that are relevant now or are becoming relevant. Suggest a workflow at the point where choosing it would be most useful, including before dependent work reaches the phase it is meant to support.

## Explicit workflows

- `grill-with-docs` — suggest before dependent planning or implementation when unresolved product, design, or domain decisions could materially change scope, behavior, interfaces, or direction and repository or project evidence can ground the user's judgment.
- `prototype` — suggest when a material design, behavior, UI, integration, or feasibility uncertainty remains and a small experiment can answer it more cheaply or reliably than further discussion or research.
- `wayfinder` — suggest when work is becoming large, uncertain, or likely to span contexts while important decisions, evidence, dependencies, or open questions still need to survive context replacement and an ordinary plan is not yet enough.
- `to-spec` — suggest once the requirements and decisions that materially shape implementation are settled enough that upcoming implementation would benefit from a durable reference.
- `to-tickets` — suggest when an established plan or specification is ready to be executed across multiple independently understandable work units or sessions with real dependencies; keep tightly coupled reasoning together.
- `implement` — suggest when a bounded unit of work has established scope and intended outcome and is ready for execution rather than requirements discovery.
- `implementation-review` — suggest when a bounded implementation is complete and focused review against the requested outcome and repository integration would be useful before treating that implementation as settled.
- `resolving-merge-conflicts` — suggest when Git has stopped on merge or rebase conflicts whose correct resolution depends on recovering the intent, invariants, or constraints behind both sides rather than choosing ours/theirs.
- `handoff` — suggest before work deliberately moves to another context, session, or agent when the next context will need live state that is not already captured in durable artifacts.
- `to-questionnaire` — suggest when progress depends on material facts or decisions owned by another person or domain expert that neither the current user nor repository research can responsibly supply.

Implicit analytical skills such as `research`, `grilling`, `diagnosing-bugs`, `tdd`, `domain-modeling`, and `codebase-design` route normally.
