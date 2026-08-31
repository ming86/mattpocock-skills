---
name: workflow-guide
description: "Recognize explicit workflow skills that would help now or soon and suggest them early enough to be useful. Use throughout the task for clarification, experiments, long-running work, specs, task decomposition, implementation, review, conflict resolution, handoff, or input best supplied by another person."
---

# Workflow Guide

Use this guide throughout the work to recognize explicit workflow skills that are useful now or are likely to become useful soon. Suggest a workflow early enough for the user to choose it before the work reaches the phase it supports. Entering a workflow chooses a method for the current work; it does not turn additional work proposed by that method into agreed scope. Keep scope-expanding additions as proposals until the current direction includes them.

## Explicit workflows

- `grill-with-docs` — suggest before dependent planning or implementation when important uncertainty about the product, design, domain, or direction could change the work, project context can narrow the question, and the remaining answer depends on the user's input.
- `prototype` — suggest when an important design, behavior, UI, integration, or feasibility question would be easier or more reliable to answer with a small experiment than with more discussion or research.
- `wayfinder` — suggest when work is becoming large, uncertain, or likely to span contexts while important decisions, findings, dependencies, or open questions still need to survive context replacement and an ordinary plan is not yet enough.
- `to-spec` — suggest once the requirements and decisions that implementation needs to follow are clear enough that upcoming work would benefit from a spec it can find and rely on.
- `to-tickets` — suggest when a current plan or specification is ready to be executed across multiple independently understandable work units or sessions with real dependencies; keep tightly coupled reasoning together.
- `implement` — suggest when there is a well-scoped work item with a known outcome and it is ready to build rather than still needing requirements work.
- `implementation-review` — suggest when a bounded implementation specifically needs a focused review of requested behavior or repository integration, or when the user wants that review. A completed work unit does not by itself create another review phase.
- `resolving-merge-conflicts` — suggest when Git has stopped on merge or rebase conflicts that require understanding what each side was trying to preserve or change rather than simply choosing ours/theirs.
- `handoff` — suggest before work deliberately moves to another context, session, or agent when the next context will need live information that is not already saved in the project's working state.
- `to-questionnaire` — suggest when progress depends on input that another person or domain expert is best placed to provide, the missing input could block or significantly change the work, and neither the current user nor project research can supply it reliably.

Implicit analytical skills such as `research`, `grilling`, `diagnosing-bugs`, `domain-modeling`, and `codebase-design` route normally. `tdd` routes when test-first development is explicitly requested or project instructions call for it in the current work.
