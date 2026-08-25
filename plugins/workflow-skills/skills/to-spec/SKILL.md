---
name: to-spec
description: "Turn settled conversation and project context into a stable implementation specification. Use when the requirements and decisions that shape implementation are clear enough and later work needs a reliable reference; preserve assumptions and unresolved points without reopening settled discussion."
disable-model-invocation: true
---

# To Spec

Turn the current understanding into a stable spec. Record what is already known or decided; do not start a second requirements interview.

If a decision is still unresolved and the spec would have to invent an answer, mark it unresolved instead of silently choosing.

## Process

1. Inspect the relevant repository state if needed. Check the project's existing vocabulary, ADRs, interfaces, conventions, and behavior.
2. Separate requirements and known facts from assumptions and unresolved points. Keep those distinctions clear in the spec.
3. Identify verification seams appropriate to the change. Prefer existing observable boundaries when they provide useful confidence. Do not create new seams, test layers, or testing commitments solely to satisfy this template.
4. Write the spec using the structure below, leaving out sections or details that add no useful information. Match the level of detail to the work.
5. Store the spec where the project already keeps this kind of work. Reuse an existing tracker, documentation area, work-state location, shared spec, issue, or design document instead of creating a parallel one. A configured local working-state area is appropriate for a personal or provisional spec. If no convention exists, keep the spec in the simplest work-centered location that can serve as a stable reference. Do not require a tracker when another document fits the work better.

<spec-template>

## Problem Statement

The problem or need being addressed, from the relevant user's or system's perspective.

## Desired Outcome

What should be true when the work succeeds, including important externally observable behavior.

## Scope and Requirements

The requirements, constraints, and boundaries that shape the work. Use user stories only when they clarify actors, behavior, or value; do not manufacture an exhaustive list for its own sake.

## Implementation Decisions

Implementation decisions already made or clearly reflected in the repository. Include relevant architecture, interfaces, schema or API contracts, interactions, and constraints. Avoid volatile file-by-file plans unless a path itself is a meaningful constraint.

If a prototype produced a compact result that captures a validated decision more precisely than prose can, include only the decision-rich part and note that it came from the prototype.

## Verification

How the important behavior or assumptions will be checked, using existing project practices and the most useful observable interfaces or outcomes for the change. Distinguish required verification from optional ideas.

## Assumptions and Unresolved Points

Working assumptions or unresolved decisions that still affect the work. Omit this section when there are none. Do not turn these items into requirements.

## Out of Scope

Boundaries that prevent likely misunderstanding or accidental expansion. Do not enumerate hypothetical future work merely to make this section longer.

## Further Notes

Only additional context that helps later implementation or review.

</spec-template>
