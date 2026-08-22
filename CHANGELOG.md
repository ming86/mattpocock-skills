# Changelog

## 0.1.9 - 2026-08-22

- Repair semantic drift found by the repo-wide v3.8 language review while keeping the broader plain-language rewrite intact.
- Restore `material` where it acts as a routing, consultation, scope, or authority threshold rather than as stylistic wording.
- Keep research focused on evidence relevant to the current question or decision, and narrow its trigger back to questions that materially depend on primary evidence.
- Tighten `DESIGN-IT-TWICE` so alternative generation is user-requested or justified by a material interface decision that cannot be resolved reliably without comparison.
- Restore bug-fix authorization wording, merge-conflict invariants, and project/user authority wording where v3.8 had become too broad or too project-specific.
- Add negative routing cases for routine repository inspection and glossary lookup, plus a boundary case that prevents `codebase-design` from implying automatic alternative generation.

## 0.1.8 - 2026-08-22

- Rewrite all 16 skill entry files for clearer, more direct engineering language while preserving routing, authority, stopping conditions, and workflow behavior.
- Stop `codebase-design` from imposing a private design dialect: keep deep-module concepts available when useful while preserving ordinary repository terms such as service, API, boundary, and component.
- Simplify supporting TDD, prototype, domain-modeling, and codebase-design guidance where abstract wording or categorical vocabulary could steer models toward unnecessary formalism.
- Simplify user-facing Codex skill descriptions and prompts so harness metadata uses the same plain-language boundaries as the skills themselves.
- Keep the 16-skill set, explicit/implicit invocation policy, routing cases, persistence model, and orchestration boundaries unchanged.

## 0.1.7 - 2026-08-22

- Make inherited `codebase-design` and TDD testing guidance proportional: deep-module, seam, mock, and interface-testing rules remain strong heuristics rather than universal laws.
- Separate bug diagnosis from permission to modify the implementation; `diagnosing-bugs` now fixes only when the current task authorizes a correction and otherwise reports the established cause and smallest credible fix.
- Clarify that handoffs must be accessible to the receiving context and are transition snapshots whose stale live state should be retired, replaced, or updated after consumption when necessary.
- Allow ordinary staging/marking of resolved paths as part of an authorized merge-conflict resolution while keeping continue, commit, abort, and merge-strategy decisions under governing project/user authority.
- Remove the unused human-in-the-loop debugging shell template.
- Add a lightweight routing-case corpus for preserving semantic boundaries and explicit/implicit invocation intent without introducing a routing framework.
- Re-evaluate the explicit-only set and retain the v3.6 invocation policy unchanged for this consolidation release.

## 0.1.6 - 2026-08-22

- Add `resolving-merge-conflicts`, an explicit-only procedure for reconciling Git conflicts from the intent and evidence behind both sides without forcing abort/continue/commit policy.
- Add `handoff`, an explicit-only transition procedure that compacts only live session state and points to existing durable work artifacts rather than duplicating them.
- Add `to-questionnaire`, an explicit-only procedure for obtaining missing decisions or facts from the external person who owns them without manufacturing answers or interrogating the wrong user.
- Apply the existing persistence, artifact-location, authority, and consultation principles to all three additions.

## 0.1.5 - 2026-08-22

- Clarify that persistence complements existing project artifacts and conventions rather than replacing them.
- Let existing project sources of truth, durable-state conventions, and governing consultation determine artifact location and authority.
- Keep local working state as an option for detailed or provisional cross-context state, not a preferred destination.
- Reframe Wayfinder maps as durable orientation state that may live in shared project artifacts, trackers, work documents, or local state.
- Replace canonical-map wording with a primary orientation artifact or view to avoid implying that Wayfinder must create project truth.

## 0.1.4 - 2026-08-22

- Add value-driven persistence for working state that needs to survive context compaction, fresh sessions, or handoffs.
- Prefer work-centered artifacts and existing work locations over skill-specific files or parallel folder trees.
- Make Wayfinder normally establish or reuse durable current state while keeping other skills conditional and proportional.
- Preserve compressed conclusions, evidence, status, and open questions rather than transcripts or append-only agent diaries.
- Keep local working state provisional unless it is deliberately promoted into shared project truth.

## 0.1.3 - 2026-08-22

- Rename `code-review` to `implementation-review` so the skill is clearly narrower than broader independent criticism.
- Make `implementation-review` explicit-only across Codex, GitHub Copilot CLI, and Claude Code.
- Clarify that passing implementation review never satisfies or cancels a broader independent-review checkpoint configured by the project.

## 0.1.2 - 2026-08-22

- Refine all skill descriptions as routing metadata so harnesses can distinguish adjacent skills before loading their bodies.
- Add explicit trigger conditions and semantic boundaries without changing skill workflows or invocation policy.

## 0.1.1

- Restore additive harness metadata without coupling skill behavior to a harness.
- Add Codex `agents/openai.yaml` presentation metadata and implicit-invocation policy for every skill.
- Mark workflow-transition skills explicit-only for Copilot CLI and Claude Code with `disable-model-invocation`.

## 0.1.0

- Extract the adapted engineering workflow into one focused plugin.
- Package the skills using Agent Plugins 1.0.0.
- Add marketplace support for Codex, GitHub Copilot CLI, and Claude Code.
- Separate the maintained product branch from the clean `upstream-main` mirror.
