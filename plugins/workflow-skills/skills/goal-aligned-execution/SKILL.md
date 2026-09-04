---
name: goal-aligned-execution
description: Keep broad, ambiguous, or multi-step work aligned with the user's overall goal by establishing enough surrounding structure to identify the core concerns, prioritizing outcome-relevant work over peripheral detail, and adapting as understanding changes. Use when planning, designing, structuring, decomposing, or carrying out work where understanding how the parts contribute to the whole helps guide what to do next.
---

# Goal-Aligned Execution

Keep the work focused on what the user is actually trying to achieve.

Work from the whole toward the parts. Before investing heavily in a local detail, establish enough of the surrounding structure to understand why that detail matters, what it affects, and whether something more central needs attention first.

Proceed iteratively as understanding develops. Do not turn the method into ceremony.

## 1. Understand the goal

Before substantial work, establish:

- the outcome the user wants;
- important constraints;
- what would make the result successful.

Ask questions only when missing information would materially affect the work.

Keep goal discovery proportional to the task. Do not turn it into a lengthy interview.

## 2. Establish the surrounding structure

Identify enough of the main concerns, relationships, dependencies, and decisions to see how the work fits together and what most affects the outcome.

Start from the core of the problem and work outward toward branches and details as useful. Do not let an easy, interesting, or locally tractable detail consume substantial effort before its importance to the larger work is established.

Respect real dependencies. Where later work genuinely rests on a foundation, establish that foundation sufficiently before building heavily on it. Do not confuse foundational work with speculative infrastructure, preparation, or abstractions that the outcome does not require.

Use layers, branches, dependency order, or a thin end-to-end path according to the actual shape of the problem. Do not force an artificial structure, and do not assume the initial structure is complete or final.

For engineering or systems work, distinguish where an effect appears from the component, layer, object, or state source that can produce it. When relevant state or facts can diverge, identify the source that actually determines the behavior before deciding what should change. If the same problem persists or local fixes accumulate, widen the investigation enough to check shared causes, duplicate logic, competing state, or misplaced responsibility before adding another local fix.

## 3. Advance meaningful work

Choose a coherent piece of work that materially advances or clarifies the outcome in the context of the whole task.

Prefer core or high-leverage work over peripheral refinement when the latter does not materially help the primary outcome. A useful increment may be small or may cross several components; size alone does not determine whether it is the right next step.

Stay within the kind of work the user requested. Do not move from planning or design into implementation, or from one level of work into another, unless the task calls for it.

Avoid unnecessary phases, abstractions, documentation, supporting machinery, or process.

## 4. Inspect in context

Inspect what the current work produced and what it reveals about the larger task.

Check the result when doing so answers a material question about whether the work is correct, useful, or ready to build on. Keep checking proportional to the task and the uncertainty being resolved.

Consider:

- whether the work materially advances the intended outcome;
- whether attention has drifted into a local detail whose importance is no longer clear;
- whether an important dependency, assumption, or relationship changed;
- whether the current understanding of the surrounding structure still holds;
- what now matters most to do next.

## 5. Adapt

Keep reconnecting the current work to the original goal and the larger structure around it.

Refine the plan, decomposition, ordering, or level of detail as understanding develops. Do not continue optimizing a local branch merely because work has already started there.

If what changed materially affects the goal, requirements, scope, or direction, surface that change rather than silently choosing a new direction.

Then continue as needed.

## Principles

- Keep the overall goal and core path more important than local optimization.
- Understand enough of the whole to judge which parts deserve attention.
- Work from core concerns toward relevant details without forcing a rigid layer order.
- Treat real dependencies as reasons for foundational work, not as permission to overbuild foundations.
- Prefer meaningful, outcome-relevant progress over easy or exhaustive leaf work.
- Preserve the requested level and scope of work.
- Let new understanding reshape the work instead of defending the initial plan or current branch.
- Avoid unnecessary complexity, supporting machinery, process, and scope expansion.
