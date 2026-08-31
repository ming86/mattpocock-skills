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
3. Carry forward validation guidance already required by the current work or existing project practice when later implementation needs it. Keep shared or end-to-end validation at the level where it actually applies. If preparing the spec reveals an additional validation step or other supporting work that would expand the current scope, keep it as a proposal or unresolved point rather than recording it as a requirement until it becomes part of the current direction.
4. Write the spec using the structure below, leaving out sections or details that add no useful information. Match the level of detail to the work. A spec organizes requirements and decisions; its sections do not create additional supporting work.
5. Store the spec where the project already keeps this kind of work so later work can find and rely on it. Reuse an existing tracker, documentation area, work-state location, shared spec, issue, or design document instead of creating a parallel one. A configured local working-state area is appropriate for a personal or provisional spec. If no convention exists, keep the spec in the simplest work-centered location that can serve as the reference for this work. A tracker is one option when it fits the project; another document may fit better.

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
