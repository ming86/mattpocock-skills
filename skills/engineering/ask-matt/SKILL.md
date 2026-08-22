---
name: ask-matt
description: Choose the smallest useful skill or workflow for the current situation instead of forcing every task through one fixed pipeline.
disable-model-invocation: true
---

# Workflow Guide

This skill keeps the historical `ask-matt` name for compatibility. Its job is to route the current work to the smallest useful procedure.

There is no mandatory main flow. Start from the actual uncertainty, scale, and state of the work. Follow the governing project or user instructions for orchestration, consultation, checkpoints, validation, commits, and independent review.

## Choose by need

| Situation | Reach for |
| --- | --- |
| The task is clear, bounded, and ready to build | `implement`, or work directly when no skill adds value |
| Material product, scope, interface, or domain decisions are unresolved | `grill-with-docs` |
| A concrete experiment can answer an important question more cheaply than discussion | `prototype` |
| Important reasoning must survive multiple contexts and the route is still unclear | `wayfinder` |
| The important decisions are settled and a durable implementation description would help | `to-spec` |
| The work benefits from multiple coherent, dependency-aware execution units | `to-tickets` |
| A bounded implementation needs focused conformance review | `code-review` |

These choices compose when the work genuinely needs more than one of them. Do not invoke a skill merely because it would be the next box in a nominal workflow.

## Common paths

### Small, clear change

`implement`

If the request and repository already make the outcome clear, do not manufacture a specification, ticket graph, or clarification phase.

### Ambiguous feature

`grill-with-docs` -> optional `prototype` -> `to-spec` or `implement`

Clarify only the decisions that materially affect the next phase. Prototype only questions that benefit from executable evidence. Create a spec when durable alignment will help later execution or review.

### Large or foggy effort

`wayfinder` -> `to-spec` -> optional `to-tickets` -> bounded implementation

Use `wayfinder` to externalize durable decision state while the route is still unclear. Leave it once the remaining route can be expressed more simply. Use `to-tickets` only when decomposition, dependencies, separate contexts, or parallel execution provide real value.

### Existing spec or tickets

Start from the durable artifact that already exists. Do not recreate upstream phases just to satisfy a flow. Implement ready work in coherent contexts and let the governing orchestration policy decide delegation, parallelism, integration, checkpoints, and review.

## Context and durable state

Do not optimize for one unbroken context window. Preserve information according to its useful lifetime:

- Keep transient exploration local when it will not matter later.
- Record material decisions, constraints, dependencies, and unresolved points when later contexts need them.
- Use fresh contexts at meaningful reasoning or ownership boundaries when isolation improves reliability.
- Keep detailed evidence near its source and use durable artifacts as pointers rather than copying the entire history into every work item.

`handoff` is useful when state must cross a harness, directory, colleague, or other boundary that cannot directly access the existing context. Do not create a handoff merely because a phase changed if the next executor already has the required durable sources.

## Other engineering tools

- `triage`: turn incoming, not-yet-shaped issues into actionable work when triage is actually needed.
- `diagnosing-bugs`: use a disciplined evidence loop for bugs that are not resolved by straightforward inspection.
- `improve-codebase-architecture`: inspect for concrete architecture improvements when codebase health is itself the task; do not run maintenance merely because feature work exists.
- `tdd`: use test-first red-green-refactor when it is appropriate to the behavior, project practices, and governing instructions. It is a technique, not a universal gate inside `implement`.
- `domain-modeling`: sharpen domain vocabulary and relationships when the model itself is ambiguous or changing.
- `codebase-design`: reason about module boundaries, interfaces, seams, and depth when code structure is the design question.
- `research`: establish facts from high-trust sources when external or repository evidence is needed before a decision.
- `resolving-merge-conflicts`: resolve an in-progress merge or rebase by intent.
- `wizard`: prepare a human-operated procedure when necessary steps genuinely cannot be performed by the agent.

## Productivity tools

- `grill-me`: focused clarification without repository documentation behavior.
- `grilling`: the reusable interview primitive behind the grill skills.
- `handoff`: compact useful state for a different executor or environment.
- `to-questionnaire`: collect missing decisions or facts from another person asynchronously.
- `wait-what`: re-explain a message that did not land.
- `teach`: maintain a stateful learning workflow across sessions.
- `writing-for-agents`: guidance for documents intended primarily for agents.

## Setup

`setup-matt-pocock-skills` remains available for repositories that want shared issue-tracker, triage-label, or domain-document conventions. It is configuration, not a prerequisite for using every engineering skill. Prefer existing project conventions when they already provide the needed durable state.