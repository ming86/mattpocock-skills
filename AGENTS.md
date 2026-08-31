# Repository agent instructions

## Purpose

This repository maintains a focused set of engineering workflow skills for coding agents. The skills complement project-level instructions and orchestration; they do not define a user's worker topology, reviewer policy, issue tracker, commit policy, delivery workflow, or who makes important project decisions.

## Source of truth

- `plugins/workflow-skills/` is the installable plugin maintained by this repository.
- Keep portable workflow behavior in each skill's `SKILL.md` and its local reference files.
- Harness-specific metadata may adapt discovery, presentation, or invocation controls, but must not create a separate implementation of a skill or change its workflow semantics.
- Repository marketplace files should point to that same plugin package.
- Keep repository-maintenance instructions at the repository level; do not add `AGENTS.md` or project orchestration policy inside the installable plugin.

## Change discipline

Keep changes proportional to the concrete problem being solved. Do not add workflow stages, abstractions, compatibility machinery, documentation, or validation merely for completeness.

Workflow methods should scale to the work they support. Let the task, project context, and actual consequences determine how much validation, verification, preflight work, benchmarking, review, rollout or rollback checking, compatibility checking, integrity checking, and other supporting process is useful. A skill invocation, document section, ticket boundary, or workflow transition does not by itself create another obligation. When an explicit scope boundary would prevent a likely expansion, state that boundary without enumerating hypothetical work that was never in play.

Treat engineering work as iterative. Plans, designs, findings, assumptions, and decisions reflect the current understanding and may change as implementation or investigation reveals more. Describe ordinary engineering state directly in terms of what is current, observed, chosen, changed, or still uncertain. Use language of proof or finality only when the work genuinely supports that stronger claim, and keep specialized technical terms when they carry a real domain distinction.

When changing a skill:

- preserve its responsibilities, stopping conditions, and intended scope;
- keep its description precise enough to distinguish neighboring skills before the body is loaded;
- prefer ordinary engineering language unless a specialized term carries a useful distinction;
- describe ordinary methodology primarily in terms of the behavior to pursue; reserve strong prohibitions for hard boundaries and recurring failure modes that need explicit suppression;
- when a skill depends on distinctions such as source findings, inference, assumptions, or user input, describe how those distinctions are determined rather than assuming the model can label them reliably;
- do not turn a useful technique into a mandatory project workflow;
- keep workflow-specific method, semantics, stopping conditions, and output meaning in the skill; leave surrounding orchestration and project workflow to project-level instructions. Express intrinsic boundaries in terms of what the skill does, produces, or leaves unresolved rather than restating external policy or adding defensive disclaimers.

If an explicit workflow skill's routing description changes enough to affect when it should be suggested, review its compressed entry in `workflow-guide` as well. When a change affects validation, review, persistence, or other supporting process, also inspect common skill compositions so a harmless local instruction does not multiply into repeated obligations across specs, tickets, implementation, review, and handoff.

Use `evals/routing-cases.yaml` when changing routing or invocation boundaries. Add or change cases when they protect a real semantic boundary; do not grow the corpus ceremonially.

## Harness compatibility

Keep the core skill behavior harness-neutral. Harness-specific metadata is additive and may differ where Codex, GitHub Copilot CLI, and Claude Code expose different controls.

When changing harness metadata, preserve the intended routing and invocation semantics rather than forcing identical fields to mean identical behavior. Keep package and marketplace versions synchronized when the installable plugin version changes.

## Upstream

`main` is the maintained product branch. `upstream-main` is a clean mirror of Matt Pocock's upstream `main` and should not be merged wholesale into the product branch.

Port useful upstream ideas selectively and adapt them to this repository's architecture. See `UPSTREAM.md` for the mirror and synchronization procedure.

## Validation

Validate what the change can realistically break. For relevant changes, check:

- skill frontmatter and harness sidecars parse;
- folder names, skill names, prompts, and invocation metadata remain coherent;
- routing cases when routing changed;
- package and marketplace versions when the plugin version changed;
- `git diff --check` and the worktree for unrelated changes.

Use broader validation only when the change justifies it.
