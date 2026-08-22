# Changelog

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
