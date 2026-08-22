---
name: implement
description: "Implement a bounded unit of work whose scope and intended outcome are already established by a ticket, specification, or current plan. Use for execution rather than requirements discovery; preserve agreed scope, follow repository practices, validate proportionally, and surface material assumptions that implementation evidence invalidates."
disable-model-invocation: true
---

# Implement

Implement the bounded work described by the current spec, ticket, or approved plan.

## Process

1. Read the source work item and the relevant repository instructions before changing code. Preserve established requirements, decisions, constraints, and acceptance criteria without treating tentative assumptions as immutable facts.
2. Inspect enough surrounding code to follow existing architecture, vocabulary, interfaces, and validation practices. Prefer established project patterns when they fit the requested behavior.
3. Implement the most direct coherent solution within the current scope. Do not add unrelated cleanup, speculative abstractions, compatibility layers, defensive machinery, or future-facing configurability without a concrete need.
4. Validate the change using the repository's existing practices and the evidence appropriate to the consequences of the change. Use focused tests, typechecking, integration checks, TDD, full-suite runs, or other techniques when they materially improve confidence or are required by the project; none is mandatory merely because this skill is running.
5. If implementation evidence invalidates a material requirement, assumption, interface, architecture decision, or planned direction, do not silently redesign the work. Report the finding through the governing project or user-consultation path before making a materially different decision. When the work already has durable state and the finding will matter to later contexts, update that current state rather than leaving the old assumption in place.
6. Complete the bounded implementation and report what changed, what was validated, and any unresolved issue that matters to dependent work. Do not create an implementation diary; persist only material state that later work would otherwise need to reconstruct.

Do not independently decide that the work must be committed, merged, reviewed, or followed by another ticket. Those actions are controlled by the governing project instructions, orchestration policy, and current user authorization.

When the project configures a separate independent review policy, that policy remains authoritative for when and how review occurs; this skill does not replace or bypass it.