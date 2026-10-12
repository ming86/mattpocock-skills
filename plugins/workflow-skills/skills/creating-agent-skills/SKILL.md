---
name: creating-agent-skills
description: Create new agent skills or substantially revise existing skills, including their workflow, structure, resources, metadata, and validation. Use for skill-level creation or redesign rather than focused wording edits to an already-correct skill.
metadata:
  short-description: Create or update an agent skill
---

# Creating Agent Skills

Based on OpenAI's `skill-creator`, adapted for portable agent skills and this repository's host compatibility.

Create skills that provide useful, non-obvious guidance without constraining unrelated work.

## Principles

- **Assume the agent is capable.** Include guidance that changes its decisions or improves execution, rather than generic advice, exhaustive examples, or repeated rules.
- **Preserve intent, scope, and authorization.** A skill supports the requested task without adding unrelated deliverables, dependencies, external actions, or project-level workflow. Approval for one operation does not authorize others; place permission checks near the actual side effect.
- **Choose the needed degree of freedom.** Describe normal methodology as behavior to pursue and criteria for choices. Reserve strict steps, scripts, and prohibitions for hard boundaries, important invariants, fragile workflows, or recurring failures where stronger steering demonstrably helps.
- **Keep discovery discriminating.** A description briefly identifies what the skill does and when it applies, including a meaningful exclusion when neighboring skills might otherwise trigger. Avoid catchall capability lists.
- **Disclose details progressively.** Keep purpose, essential workflow, and routing guidance in `SKILL.md`. Move substantial conditional detail to references read only when relevant. A small skill needs neither extra files nor a routing layer.
- **Keep corrections narrow.** For an observed failure, determine whether it needs clearer context, better selection criteria, a stronger workflow principle, or a true boundary; make the smallest change that addresses the failure. Do not turn isolated examples into universal requirements.

## Skill Structure

```text
skill-name/
├── SKILL.md                  # Required: YAML frontmatter and instructions
├── agents/openai.yaml         # Optional: host UI and invocation metadata
├── scripts/                   # Optional: deterministic or reusable operations
├── references/                # Optional: conditional documentation
└── assets/                    # Optional: files used in generated outputs
```

The required `SKILL.md` frontmatter supplies `name` and `description`. Preserve optional fields already used by the target host. This repository also uses `metadata`, `disable-model-invocation`, and `argument-hint`. Different hosts may express invocation controls differently; preserve intended behavior rather than forcing identical fields everywhere.

Use `scripts/` when repeated logic or deterministic execution materially improves reliability; test new or changed scripts. Use `references/` for task-specific schemas, workflows, or constraints needed only in particular situations. Link references and explain when to read them. Use `assets/` for output inputs such as templates, not agent instructions.

Avoid duplicated documentation, redundant placeholders, or auxiliary files unless packaging or the task requires them. Choose organization for actual needs rather than a universal template.

## Create or Update a Skill

Adapt the process to the task. A complex new skill may benefit from examples, planning, initialization, editing, and validation. A narrow update may need only a focused edit and relevant checks. Do not ask for examples when the request already gives enough context.

1. Determine the requests the skill should handle, its desired outcome, neighboring skills, and genuine constraints.
2. Choose supporting resources only where they provide a concrete benefit. Keep conditional detail out of the entrypoint when it would burden unrelated tasks.
3. For a new skill, use the initializer if it helps. Respect a specified location; for Codex otherwise use `${CODEX_HOME:-$HOME/.codex}/skills`.
4. Write instructions for another capable agent, preserving explicit choices, stopping conditions, and authorization boundaries.
5. Validate the resulting structure and changed scripts; test representative behavior when warranted.

### Naming and Initialization

Use lowercase letters, digits, and hyphens. Keep names under 64 characters, prefer short action-oriented names, and match the folder name.

```bash
scripts/init_skill.py my-skill --path "${CODEX_HOME:-$HOME/.codex}/skills"
scripts/init_skill.py my-skill --path ./skills --resources references
```

Create only useful directories; use `--examples` only for meaningful scaffolding and remove unfinished placeholders. Do not initialize an existing skill again.

### Host Metadata

`agents/openai.yaml` can contain UI descriptions and invocation policy. Read [references/openai_yaml.md](references/openai_yaml.md) before changing it.

```bash
scripts/generate_openai_yaml.py <path/to/skill-folder> --interface key=value
```

Preserve existing UI fields, host-specific metadata, policies, and dependencies unless deliberately changing them. In Codex, `policy.allow_implicit_invocation: false` allows explicit-only use; retain the existing invocation mode unless asked to change it. Other hosts may use different controls.

### Validation and Iteration

```bash
scripts/quick_validate.py <path/to/skill-folder>
```

Structural validation checks frontmatter, naming, and unfinished scaffold placeholders, not behavioral correctness. Inspect routing, reference discoverability, and metadata when applicable.

For complex or risky skills, consider independent forward-testing when delegation is available and authorized. Have an independent agent attempt a realistic request without supplying the intended answer or suspected flaw. Keep evaluation isolated and proportional; do not turn testing into a mandatory project workflow. Improve based on observed failures, choosing the smallest effective correction.
