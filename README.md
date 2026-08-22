# Workflow Skills

A focused set of engineering workflow skills for coding agents. The skills help clarify material decisions, gather evidence, externalize long-running project state, turn settled understanding into specs and work units, implement bounded changes, and validate them without imposing a second project-level orchestration policy.

This package is designed to complement whatever governing instructions, review agents, issue tracker, and engineering conventions a project already uses. It does not bundle or require a particular `AGENTS.md`, custom reviewer, worker topology, tracker, commit policy, or delivery workflow.

## What is included

The `workflow-skills` plugin currently contains 13 skills:

- `grilling`: focused clarification of material decisions
- `grill-with-docs`: clarification grounded in repository and project evidence
- `research`: primary-source technical and project research
- `prototype`: smallest useful experiment for a material uncertainty
- `wayfinder`: durable decision state for large, uncertain, or multi-session work
- `to-spec`: convert settled understanding into an implementation spec
- `to-tickets`: decompose work into coherent dependency-aware units
- `implement`: execute one bounded work unit while preserving scope
- `code-review`: review intent/spec conformance separately from repository integration
- `diagnosing-bugs`: evidence-driven debugging and regression diagnosis
- `tdd`: focused red-green-refactor when test-first development is useful
- `domain-modeling`: sharpen durable domain vocabulary, relationships, and invariants
- `codebase-design`: reason about module interfaces, seams, depth, and testability

The skills are procedures, not mandatory stages. A clear small change can go directly to implementation. A large uncertain project may use clarification, research or prototypes, Wayfinder, a spec, tickets, and then bounded implementation. Use only the mechanisms that help the current work.

## Plugin layout

The canonical package follows Agent Plugins 1.0.0:

```text
plugins/workflow-skills/
├── plugin.json
├── skills/
│   ├── grilling/
│   ├── grill-with-docs/
│   ├── research/
│   └── ...
├── .claude-plugin/
│   └── plugin.json
└── LICENSE
```

`plugin.json` and `skills/` are the portable core. `.claude-plugin/plugin.json` is a small Claude Code compatibility manifest. Repository-level marketplace catalogs adapt the same plugin package to Codex, GitHub Copilot CLI, and Claude Code without duplicating the skills.

## Install with Codex

Register this repository as a marketplace, then install the plugin:

```bash
codex plugin marketplace add ming86/mattpocock-skills --ref main
codex plugin add workflow-skills@ming86-workflow
```

Inspect the installation with:

```bash
codex plugin marketplace list
codex plugin list
```

To refresh the marketplace and reinstall the current plugin version:

```bash
codex plugin marketplace upgrade ming86-workflow
codex plugin add workflow-skills@ming86-workflow
```

To remove it:

```bash
codex plugin remove workflow-skills@ming86-workflow
codex plugin marketplace remove ming86-workflow
```

Codex namespaces plugin skills with the plugin name. In the CLI skill picker, expect names such as `workflow-skills:to-spec` and `workflow-skills:prototype`.

## Install with GitHub Copilot CLI

```bash
copilot plugin marketplace add ming86/mattpocock-skills
copilot plugin install workflow-skills@ming86-workflow
```

Inspect or update it with:

```bash
copilot plugin list
copilot plugin marketplace update ming86-workflow
copilot plugin update workflow-skills
```

Remove it with:

```bash
copilot plugin uninstall workflow-skills
copilot plugin marketplace remove ming86-workflow
```

Inside an interactive Copilot session, `/skills list` shows the skills contributed by installed plugins.

## Install with Claude Code

In Claude Code:

```text
/plugin marketplace add ming86/mattpocock-skills
/plugin install workflow-skills@ming86-workflow
```

Plugin skills are namespaced, for example:

```text
/workflow-skills:prototype
/workflow-skills:to-spec
```

Update with:

```text
/plugin marketplace update ming86-workflow
/plugin update workflow-skills@ming86-workflow
```

Remove with:

```text
/plugin uninstall workflow-skills@ming86-workflow
/plugin marketplace remove ming86-workflow
```

Run `/reload-plugins` if Claude Code tells you a reload is required after an install or update.

## Local development

Each harness can install or register a local checkout for testing. The source of truth remains `plugins/workflow-skills/`; do not maintain separate Codex, Copilot, and Claude copies of the skills.

The plugin version is currently `0.1.0`. Bump it whenever a released plugin change should be visible to version-driven update mechanisms.

## Relationship to upstream

This project was derived from Matt Pocock's `skills` repository and substantially adapted. The product branch intentionally contains only the workflow package used here; the clean upstream line is retained separately as `upstream-main` for comparison and selective porting.

See [UPSTREAM.md](UPSTREAM.md) for lineage and synchronization details. The original MIT copyright and license notice are preserved in [LICENSE](LICENSE).
