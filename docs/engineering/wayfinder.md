## What it does

`wayfinder` externalizes durable decision state when an effort is too large, uncertain, or multi-session to navigate reliably in one transient agent context.

It is for route-finding, not for adding a planning phase to work that is already clear.

## When to reach for it

Type `/wayfinder` when important project reasoning must survive context replacement and the route from the current state to the desired outcome is still materially unclear.

If the remaining work can already be captured as a normal plan, spec, or coherent implementation task, use the simpler workflow instead.

## The map is durable memory

A useful map keeps the low-resolution state a fresh context needs:

- the destination;
- established facts and constraints;
- decisions already made and their rationale;
- open questions and genuine dependencies;
- important uncertainty that is visible but not yet precise enough to become a work unit;
- material scope boundaries.

Detailed evidence stays near its source. The map is an index and orientation aid rather than a duplicate of every investigation.

Work units resolve coherent uncertainties through research, prototyping, clarification, or genuinely necessary enabling work. Do not predict the whole graph through unresolved uncertainty.

## Common questions

**Is this just `to-tickets` for a bigger project?**

No. `to-tickets` decomposes sufficiently established work for execution. Wayfinder is used earlier, when important decisions and even parts of the route are not yet clear enough to decompose reliably.

**Does every question need its own issue?**

No. Use the project's durable convention. Keep vague uncertainty in the map until it becomes precise enough that a separate work unit is useful.

## It's working if

- A fresh context can recover the project's current decision state without reading the entire conversation history.
- New work units emerge as uncertainty becomes precise rather than being guessed up front.
- Wayfinding stops once a simpler planning or execution artifact can carry the remaining route.

## Where it fits

Wayfinder can eventually hand off to [`to-spec`](../../skills/engineering/to-spec/SKILL.md), [`to-tickets`](../../skills/engineering/to-tickets/SKILL.md), or direct planning when the route becomes clear.