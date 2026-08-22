---
name: wayfinder
description: Externalize the durable decision state for work that is too large, uncertain, or multi-session to navigate reliably in one transient agent context.
---

# Wayfinder

Use Wayfinder when important project reasoning must survive context replacement and the route to the desired outcome is not yet sufficiently clear for direct specification or implementation.

Wayfinding is not a mandatory planning phase. If the goal, important decisions, dependencies, and next work are already clear enough for a normal plan or implementation context, do not create a map.

## Purpose

The map is durable project memory for the decisions that shape later work. It should let a fresh context answer:

- What outcome are we trying to reach?
- What material decisions have already been made, and why?
- What facts or constraints have been established?
- What important questions remain unresolved?
- Which unresolved questions depend on others?
- What is currently ready to investigate or decide?

The durable state belongs in the project's configured issue tracker or documentation convention. Tracker-specific labels, assignment mechanics, native dependencies, and issue relationships are useful when available but are not part of the core method.

## The map

Keep one canonical low-resolution artifact for the effort:

```markdown
## Destination

<the outcome that ends this wayfinding effort: for example a decision-ready design, an implementation-ready spec, or enough evidence to choose a direction>

## Established context

<material facts, constraints, standing project instructions, and links to source evidence that later contexts must not lose>

## Decisions so far

- <decision>: <short rationale or evidence pointer>

## Open questions

- <question>: <dependencies or status if useful>

## Not yet clear enough to decide

<important in-scope uncertainty that is visible but cannot yet be phrased as a precise decision or investigation>

## Out of scope

<only material boundaries that prevent accidental expansion>
```

Keep detail near its source. The map is an index and orientation aid, not a duplicate of every investigation or discussion.

## Work units

Each open work unit should resolve one coherent uncertainty: a decision, factual investigation, prototype question, domain clarification, or necessary enabling task. Size and split units at natural reasoning and dependency boundaries rather than an arbitrary token or session quota.

Useful modes include:

- **Research:** establish facts from documentation, APIs, repository evidence, or experiments.
- **Prototype:** create the cheapest credible artifact that can resolve a concrete design, behavior, UI, or feasibility question.
- **Clarification:** obtain user judgment on a material product, scope, interface, domain, or tradeoff decision.
- **Enabling task:** perform concrete work that is genuinely necessary before a decision can be made.

Do not create a ticket for uncertainty that is still too vague to state meaningfully. Keep it in the map until upstream evidence makes the question precise enough.

## Chart the map

1. Establish the destination from the current goal and governing instructions. Ask the user only when materially different destinations remain plausible.
2. Inspect existing project evidence before creating questions the repository can already answer.
3. Identify the first set of precise unresolved decisions or investigations and their genuine dependencies.
4. Record less-defined in-scope uncertainty without prematurely decomposing it.
5. Publish the map and actionable work units using the project's durable-state convention.
6. Stop charting when the known frontier is sufficient. Do not try to predict the complete task graph through unresolved uncertainty.

If this process reveals that the route is already clear and the remaining work fits ordinary planning, stop using Wayfinder and hand off to that simpler workflow.

## Advance the map

For each selected open question:

1. Load the map and only the detailed context relevant to that question.
2. Resolve it using repository evidence, research, a prototype, or user consultation as appropriate.
3. Record the result with its actual status: established fact, explicit decision, working assumption, or unresolved issue.
4. Update dependencies and retire questions invalidated by the new result.
5. Promote newly precise uncertainty into work units only when it is now useful to do so.
6. Re-evaluate whether the destination is clear enough to leave Wayfinder. Do not continue mapping after the remaining route can be captured more simply as a spec, plan, or tickets.

Independent work units may be handled in fresh or parallel contexts when the governing orchestration policy permits it. The project-level agent instructions remain authoritative for delegation, user checkpoints, claims/assignment, review, and execution.