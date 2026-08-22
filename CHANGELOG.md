# Changelog

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
