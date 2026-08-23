---
name: wayfinder
description: "Keep decisions, evidence, dependencies, and open questions outside transient agent context for work that is large, uncertain, or likely to span sessions. Use when important reasoning must survive context replacement and the path is not yet clear enough for an ordinary plan."
disable-model-invocation: true
---

# Wayfinder

Use Wayfinder when important project reasoning must survive context replacement and the route to the desired outcome is not yet clear enough for a normal spec or implementation plan.

Wayfinding is not a mandatory planning phase. If the goal, important decisions, dependencies, and next work are already clear enough for a normal plan or implementation context, do not create a map.

## Purpose

The map is a durable overview of the work. It lets a fresh context recover important decisions, evidence, dependencies, and open work without reconstructing earlier conversations. A fresh context should be able to answer:

- What outcome are we trying to reach?
- What material decisions have already been made, and why?
- What facts or constraints have been established?
- What important questions remain unresolved?
- Which unresolved questions depend on others?
- What is currently ready to investigate or decide?

A Wayfinder map should normally persist because surviving context replacement is part of its purpose. Follow the project's existing conventions for where it lives and how authoritative it is. The map may be an existing planning document, tracker state, work document, or local working state. Reuse the work's existing overview instead of creating a parallel one. A configured local area such as `.local/` is appropriate when detailed or provisional information should survive contexts but does not belong in shared project documentation. If no convention exists, keep the map in the simplest work-centered location that can survive the intended context transitions.

Treat the map as maintained current state, not an append-only log. Update or remove superseded assumptions and questions as understanding changes. Preserve conclusions, status, rationale, and evidence pointers rather than discussion transcripts. Tracker-specific metadata and relationships can be useful when available but are not part of the core method.

## The map

Keep one primary overview of the effort when practical:

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

Keep detail near its source. The map is an overview and index, not a copy of every investigation or discussion.

## Work units

Each open work unit should resolve one coherent uncertainty: a decision, factual investigation, prototype question, domain clarification, or necessary enabling task. Size and split units at natural reasoning and dependency boundaries rather than an arbitrary token or session quota.

Useful modes include:

- **Research:** establish facts from documentation, APIs, repository evidence, or experiments.
- **Prototype:** create the cheapest credible artifact that can resolve a concrete design, behavior, UI, or feasibility question.
- **Clarification:** obtain user judgment on a material product, scope, interface, domain, or tradeoff decision.
- **Enabling task:** perform concrete work that is genuinely necessary before a decision can be made.

Do not create a ticket for uncertainty that is still too vague to state clearly. Keep it in the map until new evidence makes the question precise enough.

## Chart the map

1. Establish the destination from the current goal, established requirements, and relevant constraints. If materially different destinations remain plausible, keep them explicit rather than selecting one as settled.
2. Inspect existing project evidence before creating questions the repository can already answer.
3. Identify the first set of precise unresolved decisions or investigations and their genuine dependencies.
4. Record less-defined in-scope uncertainty without prematurely decomposing it.
5. Establish or update the primary overview using the work's existing durable location or the project's durable-state convention. Prefer an existing overview over creating a new one, and keep detailed research or experiment evidence near its source rather than copying it into the map. If no location is already established, use the simplest work-centered location that can serve as the current overview.
6. Stop charting when the known next questions are enough to proceed. Do not try to predict the complete task graph through unresolved uncertainty.

If this process reveals that the route is already clear and the remaining work fits ordinary planning, stop using Wayfinder; the map has served its purpose.

## Advance the map

For each selected open question:

1. Load the map and only the detailed context relevant to that question.
2. Resolve it using repository evidence, research, a prototype, or user consultation as appropriate.
3. Record the result with its actual status: established fact, explicit decision, working assumption, or unresolved issue.
4. Update dependencies and retire questions invalidated by the new result.
5. Turn newly clear uncertainty into a work unit only when doing so is useful.
6. Reassess whether the destination is clear enough to leave Wayfinder. Do not keep mapping once the remaining route can be captured more simply as a spec, plan, or tickets.
