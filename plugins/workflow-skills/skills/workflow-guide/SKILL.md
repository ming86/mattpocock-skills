---
name: workflow-guide
description: "Recognize explicit workflow skills that would help now or soon and suggest them early enough to be useful. Use throughout the task for clarification, experiments, long-running work, specs, task decomposition, implementation, review, conflict resolution, handoff, or decisions owned by another person."
---

# Workflow Guide

Use this guide throughout the work to recognize explicit workflow skills that are useful now or are likely to become useful soon. Suggest a workflow early enough for the user to choose it before the work reaches the phase it supports.

## Explicit workflows

- `grill-with-docs` — suggest before dependent planning or implementation when unresolved product, design, or domain decisions could change what gets built, how it behaves, its interfaces, or the direction of the work, and the repository or project context can help the user decide.
- `prototype` — suggest when an important design, behavior, UI, integration, or feasibility question would be easier or more reliable to answer with a small experiment than with more discussion or research.
- `wayfinder` — suggest when work is becoming large, uncertain, or likely to span contexts while important decisions, findings, dependencies, or open questions still need to survive context replacement and an ordinary plan is not yet enough.
- `to-spec` — suggest once the requirements and decisions that implementation needs to follow are settled enough that upcoming work would benefit from a stable reference.
- `to-tickets` — suggest when a current plan or specification is ready to be executed across multiple independently understandable work units or sessions with real dependencies; keep tightly coupled reasoning together.
- `implement` — suggest when there is a clear work item with known scope and outcome and it is ready to build rather than still needing requirements work.
- `implementation-review` — suggest when an implementation is complete and a focused review of the requested outcome and repository integration would be useful before treating the work as finished.
- `resolving-merge-conflicts` — suggest when Git has stopped on merge or rebase conflicts that require understanding what each side was trying to preserve or change rather than simply choosing ours/theirs.
- `handoff` — suggest before work deliberately moves to another context, session, or agent when the next context will need live information that is not already saved in the project's working state.
- `to-questionnaire` — suggest when progress depends on facts or decisions owned by another person or domain expert that neither the current user nor repository research can responsibly supply.

Implicit analytical skills such as `research`, `grilling`, `diagnosing-bugs`, `tdd`, `domain-modeling`, and `codebase-design` route normally.
