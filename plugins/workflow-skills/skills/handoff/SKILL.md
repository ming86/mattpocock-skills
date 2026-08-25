---
name: handoff
description: "Package the live state of ongoing work so a fresh agent or session can continue without reconstructing the conversation. Use when deliberately moving to a new context, session, or agent; point to existing specs, issues, work state, commits, and diffs instead of copying settled information."
argument-hint: "What should the next session or agent continue?"
disable-model-invocation: true
---

# Handoff

Create a compact handoff for the next context. Carry only the live information that still exists mainly in conversation or short-term context; do not replace the project's existing work documents or saved state.

## Process

1. **Identify what the receiver should continue.** Use any user-supplied argument or current context to understand what the next session or agent is expected to do. Ask only if different plausible handoff targets would lead to different work.
2. **Locate existing project state.** Find the relevant spec, issue, plan, Wayfinder map, working-state document, commits, branch, diff, tests, and other useful current sources. Point to them instead of copying their contents.
3. **Capture only the live transition state.** Record information the next context would otherwise lose or have to reconstruct, such as:
   - what is currently in flight and why;
   - the exact next useful action or decision;
   - recent important discoveries not yet recorded elsewhere;
   - active assumptions, blockers, or unresolved tradeoffs;
   - current validation or failure state;
   - repository pointers needed to resume efficiently.
4. **Keep the handoff compact.** Preserve conclusions, current status, why important choices were made, and useful references rather than the conversation transcript. Do not repeat settled requirements, design decisions, issue bodies, diffs, or research that already live elsewhere.
5. **Put it somewhere the receiver can read.** Reuse an existing work-centered location or put it where the project normally keeps ongoing work when appropriate. A local or temporary file is suitable when the handoff is intentionally short-lived or provisional.
6. **Treat the handoff as transition state.** Its live status can become stale as soon as the next context resumes work. After it is used, move any information that still matters into the project's normal work state and retire, replace, or update the handoff when leaving it in place would mislead a later context. Do not create a cleanup protocol when the handoff is already temporary or its lifecycle is obvious.
7. **Redact sensitive material.** Do not copy credentials, API keys, passwords, private tokens, or unnecessary personal information into the handoff. Reference secure sources where appropriate instead.
8. **Point forward.** Mention next work, procedures, or skills when they would help the receiver resume. Distinguish the next steps the current work already calls for from optional suggestions.

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

<unresolved questions, assumptions, blockers, or tradeoffs the next context needs to continue>

## Validation state

<relevant checks already run, failures still present, or confidence gaps>

## References

- <spec / issue / work-state document / commit / branch / diff / file / external source>

## Relevant procedures

<only skills or procedures that are likely to help next, if any>
```

A successful handoff lets a fresh context recover momentum quickly without turning the handoff into a second copy of the project's saved state or leaving a stale snapshot that appears current later.
