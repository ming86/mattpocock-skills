---
name: to-spec
description: "Turn settled conversation and project context into a durable implementation specification. Use when important requirements and decisions are clear enough and later implementation needs a stable reference; preserve assumptions and unresolved points without reopening settled discussion."
disable-model-invocation: true
---

# To Spec

Turn the current understanding into a durable spec. Record what is already established; do not start a second requirements interview.

If a material decision is still unresolved and the spec would have to invent an answer, report that unresolved point instead of silently choosing. Follow the governing project or user instructions for whether that requires an immediate consultation or can remain explicitly unresolved.

## Process

1. Inspect the relevant repository state if needed. Use the project's established vocabulary, ADRs, interfaces, conventions, and existing behavior as evidence.
2. Separate what is actually known from what is merely inferred. Preserve the status of material information: explicit requirement or decision, discovered fact or constraint, working assumption, or unresolved point.
3. Identify verification seams appropriate to the change. Prefer existing observable boundaries when they provide useful confidence. Do not create new seams, test layers, or testing commitments solely to satisfy this template.
4. Write the spec using the structure below, leaving out sections or details that add no useful information. Match the level of detail to the work.
5. Store the spec in the work's existing authoritative location or follow the project's tracker, documentation, or durable-state convention. Reuse an existing work location instead of creating a parallel one. A configured local working-state area is appropriate for a personal or provisional spec; an existing shared spec, issue, or design document may already be the source of truth. If no convention exists, use the simplest permitted work-centered location for a low-impact choice and consult the project or user before choosing a new shared source of truth. Do not require a tracker when another durable document fits the work better.

<spec-template>

## Problem Statement

The problem or need being addressed, from the relevant user's or system's perspective.

## Desired Outcome

What should be true when the work succeeds, including important externally observable behavior.

## Scope and Requirements

The established requirements, constraints, and boundaries that meaningfully shape the work. Use user stories only when they clarify actors, behavior, or value; do not manufacture an exhaustive list for its own sake.

## Implementation Decisions

Material implementation decisions already made or strongly established by repository evidence. Include relevant architecture, interfaces, schema or API contracts, interactions, and constraints. Avoid volatile file-by-file plans unless a path itself is a meaningful constraint.

If a prototype produced a compact artifact that expresses a validated decision more precisely than prose can, include only the decision-rich part and identify it as prototype-derived evidence.

## Verification

How the important behavior or assumptions will be checked, using existing project practices and the most useful observable interfaces or outcomes for the change. Distinguish required verification from optional ideas.

## Assumptions and Unresolved Points

Material working assumptions or unresolved decisions that remain relevant. Omit this section when there are none. Do not turn these items into requirements.

## Out of Scope

Material boundaries that prevent likely misunderstanding or accidental expansion. Do not enumerate hypothetical future work merely to make this section longer.

## Further Notes

Only additional context that materially helps later implementation or review.

</spec-template>
