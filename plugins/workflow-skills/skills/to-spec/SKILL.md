---
name: to-spec
description: "Turn settled conversation and project context into a durable implementation specification. Use after material requirements and decisions are sufficiently resolved and later implementation needs a stable source of truth; preserve assumptions and unresolved points without reopening already-settled discussion."
disable-model-invocation: true
---

# To Spec

Synthesize the current understanding into a durable spec. This skill records what has already been established; it is not a second requirements interview.

If a material decision is still unresolved and the spec would have to invent an answer, surface that unresolved point instead of silently choosing. Follow the governing project or user instructions for whether that requires an immediate consultation or can remain explicitly unresolved.

## Process

1. Inspect the relevant repository state if needed. Use the project's established vocabulary, ADRs, interfaces, conventions, and existing behavior as evidence.
2. Separate what is actually known from what is merely inferred. Preserve the status of material information: explicit requirement or decision, discovered fact or constraint, working assumption, or unresolved point.
3. Identify verification seams appropriate to the change. Prefer existing observable boundaries when they provide useful confidence. Do not create new seams, test layers, or testing commitments solely to satisfy this template.
4. Write the spec using the structure below, omitting sections or details that add no useful information. Keep the amount of detail proportional to the work.
5. Publish or store the spec as durable work state using the effort's existing authoritative location or the project's configured tracker, documentation, or durable-state convention. Reuse an existing work location instead of scattering a parallel artifact elsewhere. A configured local working-state area is appropriate for a personal or provisional spec when that role is useful; an existing shared spec, issue, or design document may already be the intended source of truth. If no convention exists, use the simplest permitted work-centered artifact for a low-impact choice and follow governing consultation rules when choosing a new shared source of truth is material. Do not require a tracker when another durable artifact fits the work better.

<spec-template>

## Problem Statement

The problem or need being addressed, from the relevant user's or system's perspective.

## Desired Outcome

What should be true when the work succeeds, including important externally observable behavior.

## Scope and Requirements

The established requirements, constraints, and boundaries that materially shape the work. Use user stories only when they clarify actors, behavior, or value; do not manufacture an exhaustive list for its own sake.

## Implementation Decisions

Material implementation decisions already made or strongly established by repository evidence. Include relevant architecture, interfaces, schema or API contracts, interactions, and constraints. Avoid volatile file-by-file plans unless a path itself is a meaningful constraint.

If a prototype produced a compact artifact that expresses a validated decision more precisely than prose can, include only the decision-rich part and identify it as prototype-derived evidence.

## Verification

How the important behavior or assumptions will be validated, using existing project practices and the highest-value observable seams appropriate to the change. Distinguish required verification from optional ideas.

## Assumptions and Unresolved Points

Material working assumptions or unresolved decisions that remain relevant. Omit this section when there are none. Do not promote these items into requirements.

## Out of Scope

Material boundaries that prevent likely misunderstanding or accidental expansion. Do not enumerate hypothetical future work merely to make this section longer.

## Further Notes

Only additional context that materially helps later implementation or review.

</spec-template>
