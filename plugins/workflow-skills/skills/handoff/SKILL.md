---
name: handoff
description: "Package the live state of ongoing work so a fresh agent or session can continue without reconstructing the conversation. Use when deliberately moving to a new context, session, or agent; point to existing specs, issues, work state, commits, and diffs instead of copying settled information."
argument-hint: "What should the next session or agent continue?"
disable-model-invocation: true
---

# Handoff

Create a compact handoff for the next context. Carry only the live information that still exists mainly in conversation or short-term context; do not replace the work's existing durable documents or state.

## Process

1. **Identify what the receiver should continue.** Use any user-supplied argument or current context to understand what the next session or agent is expected to do. Ask only if meaningfully different handoff targets remain plausible.
2. **Locate existing durable state.** Find the relevant spec, issue, plan, Wayfinder map, working-state document, commits, branch, diff, tests, and other useful or authoritative sources. Point to them instead of copying their contents.
3. **Capture only the live transition state.** Record information the next context would otherwise lose or have to reconstruct, such as:
   - what is currently in flight and why;
   - the exact next useful action or decision;
   - recent important discoveries not yet recorded elsewhere;
   - active assumptions, blockers, or unresolved tradeoffs;
   - current validation or failure state;
   - repository pointers needed to resume efficiently.
4. **Keep the handoff compact.** Preserve conclusions, status, rationale, and evidence pointers rather than the conversation transcript. Do not repeat settled requirements, design decisions, issue bodies, diffs, or research that already have durable homes.
5. **Put it somewhere the receiver can read.** Reuse an existing work-centered location or follow the project's durable-state convention when appropriate. A local or temporary file is suitable when the handoff is intentionally short-lived and should not become shared project documentation. Do not silently make the handoff a new shared source of truth when that choice is material.
6. **Treat the handoff as transition state.** Its live status can become stale as soon as the next context resumes work. After consumption, preserve any still-useful durable information through the work's normal state and retire, replace, or update the handoff when leaving it in place would mislead a later context. Do not create a cleanup protocol when the artifact is already ephemeral or its lifecycle is otherwise obvious.
7. **Redact sensitive material.** Do not copy credentials, API keys, passwords, private tokens, or unnecessary personal information into the handoff. Reference secure sources where appropriate instead.
8. **Point forward.** Mention next work, procedures, or skills when they would help the receiver resume. Distinguish established next steps from suggestions.

## Suggested structure

Use only the sections that carry useful transition state.

```markdown
# Handoff: <work>

## Continue with

<what the next context should accomplish or decide>

## Current state

<what is in flight, what changed recently, and where execution stopped>

## Next action

<the most useful immediate next step>

## Open / blocked

<material unresolved questions, assumptions, blockers, or tradeoffs>

## Validation state

<relevant checks already run, failures still present, or confidence gaps>

## References

- <spec / issue / work-state artifact / commit / branch / diff / file / external source>

## Relevant procedures

<only skills or procedures that are likely to help next, if any>
```

A successful handoff lets a fresh context recover momentum quickly without turning the handoff itself into a second copy of the project's durable state or leaving a stale transition snapshot that appears current later.
