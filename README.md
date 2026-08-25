# Workflow Skills

A focused set of engineering workflow skills for coding agents. The skills help clarify important decisions, gather evidence, preserve long-running work state, turn settled understanding into specs and work units, implement bounded changes, and check the results without imposing a second project-level orchestration policy.

This package is designed to complement whatever governing instructions, review agents, issue tracker, and engineering conventions a project already uses. It does not bundle or require a particular `AGENTS.md`, custom reviewer, worker topology, tracker, commit policy, or delivery workflow.

## What is included

The `workflow-skills` plugin currently contains 17 skills:

- `workflow-guide`: compact catalog for identifying relevant explicit workflow skills
- `grilling`: focused clarification of important decisions
- `grill-with-docs`: clarification grounded in repository and project evidence
- `research`: primary-source technical and project research
- `prototype`: smallest useful experiment for an important uncertainty
- `wayfinder`: durable overview for large, uncertain, or multi-session work
- `to-spec`: convert settled understanding into an implementation spec
- `to-tickets`: split work into clear units with real dependencies
- `implement`: execute one bounded work unit while preserving scope
- `implementation-review`: explicitly review a bounded implementation against the requested outcome and repository integration
- `diagnosing-bugs`: evidence-driven debugging and regression diagnosis
- `tdd`: focused red-green-refactor when test-first development is useful
- `domain-modeling`: sharpen durable domain vocabulary, relationships, and invariants
- `codebase-design`: reason about module boundaries, interfaces, dependencies, and testability
- `resolving-merge-conflicts`: reconcile in-progress Git conflicts from the intent behind both sides
- `handoff`: package live work state for a fresh session or agent
- `to-questionnaire`: ask an external decision-maker or domain expert for missing information

The skills are procedures, not mandatory stages. A clear small change can go directly to implementation. A large uncertain project may use clarification, research or prototypes, Wayfinder, a spec, tickets, and then bounded implementation. Use only the mechanisms that help the current work.

## Explicit workflow discovery

Several workflow skills are intentionally explicit-only, which can make their descriptions unavailable to normal model routing. The implicit `workflow-guide` closes that discoverability gap with a compact catalog of those workflows. Each catalog entry is a compressed routing summary of the target skill's own description; when a target description changes materially, review the guide entry too.

The guide identifies relevant explicit skills; project and user instructions decide whether and how to enter them. A root/worker project can add a small rule to its own `AGENTS.md`, for example:

```md
### Workflow skills

When available, the root agent should use the workflow guide to identify relevant explicit workflow skills. Before entering an explicit workflow, briefly recommend the relevant skill and ask the user.

Delegated workers should surface useful workflow needs to the root agent rather than prompting the user or expanding their assignment.
```

The plugin does not bundle an `AGENTS.md`; project and user instructions remain the governing source of orchestration policy.

## Durable working state

Coding-agent context is transient. When detailed findings, decisions, assumptions, evidence, or open questions would be expensive or unreliable to reconstruct after compaction or a fresh session, the skills may save that state outside the conversation. Persistence is useful when it preserves real value; it is not mandatory.

Persistence complements existing project documents and conventions; it does not replace them. Prefer files or records organized around the work rather than around the skill that produced them. First reuse the work's existing durable location or the project's tracker, documentation, or durable-state convention. Use a configured local working-state area, for example `.local/work/<work>/`, when detailed or provisional information should survive contexts but does not belong in shared project documentation. If no convention exists and the choice is low-impact, use the simplest permitted work-centered location. When creating a new shared location would be an important project decision, follow the project instructions rather than choosing one implicitly.

Keep durable state compact and current: preserve conclusions, status, rationale, and evidence pointers rather than transcripts or append-only diaries. A shared issue, spec, ADR, design document, or tracker may already be the right place for the current state; local working state may remain provisional. Moving local state into shared project documentation is one possible lifecycle, not a required one. If information is immediately consumed and cheap to reconstruct, leaving it transient is often better.

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

## Harness-specific skill metadata

The workflow instructions remain harness-neutral, but the package keeps additive metadata that a harness can use without changing workflow semantics. Codex reads each skill's `agents/openai.yaml` for presentation metadata and implicit-invocation policy. GitHub Copilot CLI and Claude Code understand `disable-model-invocation` in `SKILL.md`; selected explicit skills also use `argument-hint` when a short invocation hint improves the user-facing command experience.

The workflow-transition skills `grill-with-docs`, `prototype`, `wayfinder`, `to-spec`, `to-tickets`, and `implement`, plus `implementation-review`, `resolving-merge-conflicts`, `handoff`, and `to-questionnaire`, default to explicit invocation. The advisory `workflow-guide` plus analytical and support skills remain eligible for automatic selection. These adapters may control discovery and presentation, but must not choose models, workers, reviewers, permission escalation, or governing project policy.

`disable-model-invocation` is a Copilot/Claude extension rather than a field in the core Agent Skills specification. The canonical skills use that extension deliberately because both target harnesses consume it; other clients should ignore unknown frontmatter fields.

## Repository agent instructions

This source repository includes a root `AGENTS.md` with repository-specific maintenance guidance. It is for agents working on this repository and is not part of the installed workflow plugin. `CLAUDE.md` imports the same file for Claude Code so the repository guidance has one source of truth.

## Local development

Each harness can install or register a local checkout for testing. The source of truth remains `plugins/workflow-skills/`; do not maintain separate Codex, Copilot, and Claude copies of the skills.

`evals/routing-cases.yaml` is a lightweight, non-executable corpus of representative routing boundaries. It records which skill should semantically match a prompt and whether the current package policy permits implicit invocation; use it when changing trigger descriptions or reconsidering neighboring skill boundaries rather than treating it as a mandatory workflow test harness.

The plugin version is currently `0.2.12`. Bump it whenever a released plugin change should be visible to version-driven update mechanisms.

## Relationship to upstream

This project was derived from Matt Pocock's `skills` repository and substantially adapted. The product branch intentionally contains only the workflow package used here; the clean upstream line is retained separately as `upstream-main` for comparison and selective porting.

See [UPSTREAM.md](UPSTREAM.md) for lineage and synchronization details. The original MIT copyright and license notice are preserved in [LICENSE](LICENSE).
