---
name: workflow-guide
description: "Advise when one deliberate workflow skill could materially improve the current work without entering that workflow automatically. Use when the work may be ready for an explicit transition such as grounded clarification, a prototype, Wayfinder, a spec, tickets, bounded implementation, focused implementation review, merge-conflict resolution, handoff, or an external questionnaire; recommend the nearest useful skill briefly and do nothing when ordinary work should continue."
---

# Workflow Guide

Help the governing/root agent recognize when one of this plugin's explicit workflow skills may be worth using. This skill is advisory only. It does not replace project instructions, choose the overall workflow, or authorize another skill.

The default is to continue ordinary work. Recommend an explicit workflow only when entering it would materially improve clarity, evidence, continuity, execution, or review. Do not recommend a skill merely because it is a plausible next step or because it exists.

## Explicit workflow catalog

- `grill-with-docs` — material user-owned product, design, or domain decisions need clarification grounded in repository or project evidence.
- `prototype` — a material empirical uncertainty is cheaper or more reliable to settle with a small experiment than with more discussion or research.
- `wayfinder` — large, uncertain, or multi-session work needs a durable overview of decisions, evidence, dependencies, and open questions.
- `to-spec` — important understanding is sufficiently settled and a durable implementation contract would help dependent work.
- `to-tickets` — a settled plan or spec would benefit from coherent dependency-aware work units.
- `implement` — a bounded unit of work has an established scope and intended outcome and is ready for implementation.
- `implementation-review` — a completed bounded implementation needs focused review against the requested outcome and repository integration. This does not replace broader independent criticism required by the project.
- `resolving-merge-conflicts` — an active Git merge or rebase has conflicts whose correct resolution depends on understanding the intent and invariants behind both sides.
- `handoff` — the current session, agent, or context is about to change and the next context needs a compact transition snapshot.
- `to-questionnaire` — another person owns material information or decisions needed for the work, and a focused questionnaire would obtain them without manufacturing answers.

Implicit analytical skills such as `research`, `grilling`, `diagnosing-bugs`, `tdd`, `domain-modeling`, and `codebase-design` are outside this catalog. They may be selected normally when the harness and governing instructions allow it.

## How to advise

1. **Check whether ordinary work can continue.** A clear small change, routine repository inspection, straightforward implementation step, or already-authorized local technique usually needs no workflow recommendation.
2. **Identify the actual transition point.** Ask what is preventing reliable progress or what new mode of work would materially help. Match that condition to the closest explicit skill above.
3. **Prefer the smallest useful transition.** Recommend at most one skill by default. Do not propose a chain such as prototype → spec → tickets → implement. A later transition can be considered when the work actually reaches it. If two skills represent a genuine material choice, explain that choice instead of listing the catalog.
4. **Keep the recommendation brief.** In a root or user-facing context, name the skill, give the concrete reason it fits now, and ask whether the user wants to use it. Do not load, invoke, simulate, or require the target workflow before approval.
5. **Respect harness invocation rules.** User approval authorizes the workflow decision but does not bypass the current harness's skill-invocation rules. If the harness permits the root to deliberately invoke the approved skill, use that mechanism. If the harness requires user invocation, state the exact skill name or available command rather than pretending that approval alone loaded it.
6. **Handle worker contexts differently.** A delegated worker may identify that an explicit workflow could help, but unless its assignment already authorizes that workflow, it should report the candidate and reason to the governing/root agent rather than prompting the user or expanding its assignment.
7. **Honor a decline.** If the user declines the recommendation, continue without that workflow and do not ask again under the same circumstances. Reconsider only if the situation materially changes.

## Recommendation shape

Keep the prompt lightweight. For example:

> The remaining question is empirical and the docs do not settle it. `prototype` would let us answer it with a small experiment. Would you like to use that workflow?

Or:

> This work is now spanning contexts with several unresolved decisions. `wayfinder` could preserve the current map so we do not reconstruct it after compaction. Would you like to use it?

Do not turn the recommendation into a workflow plan, a catalog of available skills, or a mandatory checkpoint.
