# Contributing

Keep the installable product focused on workflow procedures that complement external project policy.

## Boundaries

A workflow skill may explain how to perform a bounded activity. It should not assume ownership of project-level decisions such as worker selection, subagent topology, checkpoints, commit or merge policy, release policy, destructive operations, or which independent reviewer a project uses.

Do not add a dependency on a particular `AGENTS.md`, custom agent, issue tracker, or coding-agent harness unless the behavior is isolated to a documented compatibility adapter. Portable skills should remain useful when installed by themselves.

Prefer evidence-driven, proportional procedures over mandatory ceremony. Add a stage, artifact, abstraction, validation step, or durable record only when it has a concrete role in the work the skill addresses.

## Plugin structure

The canonical plugin is `plugins/workflow-skills/`:

- root `plugin.json`: Agent Plugins 1.0.0 portable manifest
- `skills/`: canonical Agent Skills
- `.claude-plugin/plugin.json`: Claude Code compatibility manifest

Marketplace files are distribution adapters and must all point to that same plugin directory. Do not duplicate skill trees per harness.

When changing released behavior, keep the plugin version and all marketplace versions synchronized.

## Upstream

See `UPSTREAM.md`. Keep `upstream-main` as a clean mirror and port useful upstream changes selectively rather than merging the branch into `main`.
