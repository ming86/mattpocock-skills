---
name: to-spec
description: "Turn the current conversation and project context into an implementation specification that later work can find and rely on. Use when the requirements and decisions that shape implementation are clear enough to guide the work; keep assumptions and unresolved points visible as the understanding evolves."
disable-model-invocation: true
---

# To Spec

Turn the current understanding into a spec that later work can find and rely on. Record what is already known or decided rather than starting a second requirements interview. Preserve the status of the source material: a useful idea from the agent is not a requirement merely because the spec records it.

Leave unresolved any question that still affects implementation and is not answered by the current requirements, project context, or user decisions.

## Process

1. Inspect the relevant repository state if needed. Check the project's existing vocabulary, ADRs, interfaces, conventions, and behavior.
2. Keep explicit requirements and decisions separate from what the current code, documentation, or other project sources show, from working assumptions, and from unresolved points. Preserve those distinctions so later work can tell what each statement is based on.
3. Carry forward validation already required by the current work or project practice, keeping shared or end-to-end checks at the level where they apply. Record any newly identified validation or supporting work under `Assumptions and Unresolved Points` as a proposal until accepted into scope.
4. Write the spec using the structure below, leaving out sections or details that add no useful information. Match detail to the work; spec sections organize requirements and decisions without creating extra supporting work.
5. Save the spec in the work's existing tracker, shared spec, issue, or design doc per project conventions without creating a parallel copy; use a configured local working-state area for a personal or provisional spec, or the simplest work-centered location when no convention exists.

<spec-template>

## Problem Statement

The problem or need being addressed, from the relevant user's or system's perspective.

## Desired Outcome

What should be true when the work succeeds, including important externally observable behavior.

## Scope and Requirements

The requirements, constraints, and boundaries that implementation needs to follow. Use user stories when they clarify actors, behavior, or value; an exhaustive list is unnecessary when it adds no useful information.

## Implementation Decisions

Implementation decisions already made, together with existing interfaces, constraints, or system behavior that the implementation needs to work with. Include relevant architecture, interfaces, schema or API contracts, interactions, and constraints. Describe existing repository behavior as a constraint when it matters to the work rather than presenting its existence alone as an intentional decision. Keep file-by-file detail only when a path itself is a meaningful constraint.

If a prototype produced a compact result that captures what the experiment showed more precisely than prose can, include the relevant result and the current conclusion it informed, and note that it came from the prototype.

## Validation (when needed)

Include this section when the current work or existing project practice already provides validation guidance that later work needs to carry forward. State the outcome, behavior, or important assumption to check and the relevant scope. Prefer representative existing paths or checks when they are sufficient. Do not turn an additional check into a new requirement here merely because it could increase confidence; keep such an addition as a proposal or unresolved point until it is accepted into the work.

## Assumptions and Unresolved Points

Working assumptions, unresolved questions, or proposed additions that still affect the work. Omit this section when there are none. Keep each item labeled by its current status rather than folding assumptions, unresolved points, or proposals into requirements.

## Out of Scope

Boundaries that prevent likely misunderstanding or accidental expansion. Include supporting-process boundaries when they prevent a likely expansion of validation, benchmarking, rollout, migration, or similar work. Keep this section focused on boundaries that are actually relevant rather than enumerating hypothetical exclusions.

## Further Notes

Only additional context that later implementation or review actually needs.

</spec-template>
