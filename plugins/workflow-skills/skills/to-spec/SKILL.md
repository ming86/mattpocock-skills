---
name: to-spec
description: "Turn the current conversation and project context into an implementation specification that later work can find and rely on. Use when the requirements and decisions that shape implementation are clear enough to guide the work; keep assumptions and unresolved points visible as the understanding evolves."
disable-model-invocation: true
---

# To Spec

Turn the current understanding into a spec that later work can find and rely on. Record what is already known or decided rather than starting a second requirements interview.

Leave unresolved any question that still affects implementation and is not answered by the current requirements, project context, or user decisions.

## Process

1. Inspect the relevant repository state if needed. Check the project's existing vocabulary, ADRs, interfaces, conventions, and behavior.
2. Keep explicit requirements and decisions separate from what the current code, documentation, or other project sources show, from working assumptions, and from unresolved points. Preserve those distinctions so later work can tell what each statement is based on.
3. Decide whether later implementation needs validation guidance beyond the project's normal practices. When it does, start from the outcome or important uncertainty that later work needs to check and describe the narrowest useful scope. Prefer existing observable paths and checks; keep shared or end-to-end validation at the level where it can meaningfully show whether the outcome holds.
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

Include this section only when later work needs guidance beyond normal project practice. State the outcome, behavior, or important assumption that later work needs to check and the validation scope that is useful for this work. Prefer representative existing paths or checks when they are sufficient.

## Assumptions and Unresolved Points

Working assumptions or unresolved questions that still affect the work. Omit this section when there are none. Keep these items labeled as assumptions or unresolved points rather than requirements.

## Out of Scope

Boundaries that prevent likely misunderstanding or accidental expansion. Include supporting-process boundaries when they prevent a likely expansion of validation, benchmarking, rollout, migration, or similar work. Keep this section focused on boundaries that are actually relevant rather than enumerating hypothetical exclusions.

## Further Notes

Only additional context that later implementation or review actually needs.

</spec-template>
