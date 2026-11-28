# Workflow Skills

A focused collection of 26 agent skills: 19 project workflow skills and 7 independent general-purpose skills covering research, reasoning, decision-making, execution, writing, visual explanation, and skill authoring. The workflow skills help clarify decisions, investigate open questions, preserve long-running state, produce specs and work units, implement bounded changes, and review results.

This package complements your project's existing governing instructions, review agents, issue tracker, commit policy, and delivery workflow. It ships without a bundled `AGENTS.md`, custom reviewer, worker topology, or mandatory orchestration policy.

## Install

### Codex

Install:

```bash
codex plugin marketplace add ming86/mattpocock-skills --ref main
codex plugin add workflow-skills@ming86-workflow
```

Inspect:

```bash
codex plugin marketplace list
codex plugin list
```

Update:

```bash
codex plugin marketplace upgrade ming86-workflow
codex plugin add workflow-skills@ming86-workflow
```

Remove:

```bash
codex plugin remove workflow-skills@ming86-workflow
codex plugin marketplace remove ming86-workflow
```

Codex namespaces plugin skills under the plugin name (for example, `workflow-skills:to-spec` and `workflow-skills:prototype`).

### GitHub Copilot CLI

Install:

```bash
copilot plugin marketplace add ming86/mattpocock-skills
copilot plugin install workflow-skills@ming86-workflow
```

Inspect and update:

```bash
copilot plugin list
copilot plugin marketplace update ming86-workflow
copilot plugin update workflow-skills
```

Remove:

```bash
copilot plugin uninstall workflow-skills
copilot plugin marketplace remove ming86-workflow
```

Run `/skills list` inside an interactive Copilot session to view skills contributed by installed plugins.

### Claude Code

Install:

```text
/plugin marketplace add ming86/mattpocock-skills
/plugin install workflow-skills@ming86-workflow
```

Update:

```text
/plugin marketplace update ming86-workflow
/plugin update workflow-skills@ming86-workflow
```

Remove:

```text
/plugin uninstall workflow-skills@ming86-workflow
/plugin marketplace remove ming86-workflow
```

Claude Code namespaces plugin skills (for example, `/workflow-skills:prototype` and `/workflow-skills:to-spec`). Run `/reload-plugins` if Claude Code prompts for a reload after installing or updating.

### Google Antigravity

Install:

```bash
agy plugin install https://github.com/ming86/mattpocock-skills
```

Inspect:

```bash
agy plugin list
```

Update:

```bash
agy plugin install https://github.com/ming86/mattpocock-skills
```

Remove:

```bash
agy plugin uninstall workflow-skills
```

Antigravity exposes installed plugin skills via `/<skill-name>` (for example, `/to-spec` and `/prototype`) and synchronizes installed plugins between the Antigravity App and Antigravity CLI.

## What is included

### Project workflow skills (19)

- `workflow-guide`: compact catalog for identifying relevant explicit workflow skills
- `grilling`: focused clarification of uncertainty that could change or block the work
- `grill-with-docs`: clarification grounded in project context and user input
- `research`: source-grounded investigation using evidence suited to the question, with concrete guidance for technical and engineering sources
- `prototype`: smallest useful experiment for an important uncertainty
- `wayfinder`: working overview that survives context changes for large, uncertain, or multi-session work
- `to-spec`: turn current understanding into an implementation spec
- `to-tickets`: split work into clear units with real dependencies
- `implement`: execute one bounded work unit while preserving scope
- `implementation-review`: explicitly review a bounded implementation against the requested outcome and repository integration
- `retro`: reflect on observed session friction and propose agent-environment improvements
- `diagnosing-bugs`: evidence-driven debugging and regression diagnosis
- `tdd`: focused red-green-refactor when test-first development is requested or project instructions call for it
- `domain-modeling`: clarify concepts, roles, relationships, and invariants in business processes, other problem domains, and software
- `codebase-design`: reason about module boundaries, interfaces, dependencies, and responsibility placement
- `simplify-by-ablation`: assess what would be lost by simplifying designs, implementations, plans, documents, or procedures
- `resolving-merge-conflicts`: reconcile in-progress Git conflicts from the intent behind both sides
- `handoff`: package live coding, research, writing, or other work state for a fresh session or agent
- `to-questionnaire`: ask another person or domain expert for input they are best placed to provide

### General-purpose skills (7)

These seven skills ship in the same plugin for convenience, trigger independently from their own descriptions, and stay outside `workflow-guide`:

- `decide-under-uncertainty`: structure high-stakes or ambiguous decisions under incomplete information using hard constraints, marginal tradeoffs, second-order effects, value of information, and reversibility
- `goal-aligned-execution`: keep broad, ambiguous, or multi-step work connected to the overall goal and surrounding structure
- `cognitive-clarity-editor`: write, revise, or polish text for clarity, readability, structure, and high signal-to-noise calibrated to medium, audience, and stakes
- `reason-from-first-principles`: reason beneath inherited framing from what is fundamental to the subject
- `writing-agent-instructions`: write and review reusable agent-facing instructions for effective routing, behavior, context use, and maintenance
- `visual-explanation`: make mechanisms, processes, concepts, arguments, timelines, comparisons, and software structure easier to see in the current interface
- `creating-agent-skills`: create and evolve agent skills using the OpenAI skill-creator foundation plus this project's steering refinements

Shared methods such as `research`, `domain-modeling`, `simplify-by-ablation`, `visual-explanation`, and `handoff` retain concrete engineering guidance where it applies and also work on non-coding or mixed tasks without assuming a repository exists.

## How the workflows operate

Use only the procedures that help the current task. A clear small change can move straight to `implement`, while a large uncertain project can chain clarification, research or prototypes, `wayfinder`, `to-spec`, `to-tickets`, and bounded implementation.

Process weight scales to the task. Skills carry forward only the validation and checks your project already requires, keeping shared or end-to-end verification at the level where it applies. Specs, tickets, and document sections organize execution without creating extra obligations; newly discovered work stays as a proposal until you explicitly adopt it into scope. As investigation or implementation advances, skills update plans, specs, and assumptions to reflect current understanding.

## Explicit workflow discovery

Eleven workflow skills are explicit-only so they never hijack routine tasks, which hides their descriptions from automatic model routing. The implicit `workflow-guide` closes that gap with a compact catalog summarizing each target skill's routing conditions. Whenever a target skill's description changes enough to alter when it should be suggested, update its `workflow-guide` entry as well.

`workflow-guide` identifies relevant explicit skills while your project and user instructions govern whether and how to enter them. A root/worker project can add a brief rule to its own `AGENTS.md`:

```md
### Workflow skills

When available, the root agent should use the workflow guide to identify relevant explicit workflow skills. Before entering an explicit workflow, briefly recommend the relevant skill and ask the user.

Delegated workers should surface useful workflow needs to the root agent rather than prompting the user or expanding their assignment.
```

## Saved working state

Coding-agent context is transient. Save state outside the conversation when detailed findings, decisions, assumptions, source pointers, or open questions would be costly or unreliable to reconstruct after compaction or a fresh session. Leave information transient when it is immediately consumed and cheap to rebuild.

Organize saved state around the work itself following three priorities:

1. Reuse the work's existing shared location first (an issue, spec, ADR, design document, or tracker) according to project conventions.
2. Store provisional or session-specific detail under a local working-state area such as `.local/work/<work>/`, or the simplest permitted work-centered path when no convention exists and impact is low.
3. Follow project instructions before creating a new shared documentation location.

Keep saved state compact and current by recording conclusions, status, rationale, and source pointers while omitting raw transcripts or append-only diaries. Promote local working state into shared project docs only when it belongs there permanently.

## Plugin layout and harness metadata

The package follows Agent Plugins 1.0.0:

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

`plugin.json` and `skills/` form the portable core, `.claude-plugin/plugin.json` provides Claude Code compatibility, `.antigravity-plugin/plugin.json` adapts the repository root for Google Antigravity, and repository-level marketplace catalogs adapt the same package to Codex, GitHub Copilot CLI, and Claude Code without duplicating skill files.

Skill instructions remain harness-neutral, accompanied by additive metadata that controls discovery and presentation without altering workflow semantics (or choosing models, workers, reviewers, permission escalation, or governing policy):

- **Codex** reads each skill's `agents/openai.yaml` for display metadata and implicit-invocation policy.
- **GitHub Copilot CLI, Claude Code, and Google Antigravity** read `disable-model-invocation` in `SKILL.md`; Copilot CLI and Claude Code also read optional `argument-hint`.
- **Invocation defaults**: Eleven workflows default to explicit invocation (`grill-with-docs`, `prototype`, `wayfinder`, `to-spec`, `to-tickets`, `implement`, `implementation-review`, `resolving-merge-conflicts`, `handoff`, `retro`, and `to-questionnaire`). `workflow-guide` and all remaining analytical, support, and general-purpose skills trigger automatically from their descriptions. `tdd` activates only when test-first development is explicitly requested or called for by project instructions.

## Local development

Each harness can install or register a local checkout for testing. Keep `plugins/workflow-skills/` as the single source of truth across Codex, Copilot CLI, Claude Code, and Google Antigravity.

- **Repository instructions**: The root `AGENTS.md` (imported by `CLAUDE.md` for Claude Code) governs maintenance of this source repository and is excluded from the installed plugin.
- **Routing reference**: `evals/routing-cases.yaml` lists sample prompts, expected skill matches, and implicit-invocation rules. Consult it when editing trigger descriptions or adjusting boundaries between neighboring skills.
- **Versioning**: The plugin version is currently `0.2.45`. Bump it whenever a released change should be visible to version-driven updates.

## Relationship to upstream

This repository was derived from Matt Pocock's `skills` repository and substantially adapted. The `main` branch contains only this workflow package, while `upstream-main` preserves the clean upstream line for comparison and selective porting.

See [UPSTREAM.md](UPSTREAM.md) for lineage and synchronization details. The original MIT copyright and license notice remain in [LICENSE](LICENSE).
