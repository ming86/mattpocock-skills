---
name: setup-matt-pocock-skills
description: "Optionally configure shared issue-tracker, triage-label, and domain-document conventions when the repository does not already provide suitable ones."
disable-model-invocation: true
---

# Setup Workflow Skills

This skill keeps the historical `setup-matt-pocock-skills` name for compatibility.

Use it when several workflow skills need a shared durable convention and the repository does not already make that convention clear. It is not a prerequisite for every engineering skill, and it must not install a second engineering policy on top of the repository's existing `AGENTS.md`, `CLAUDE.md`, or equivalent instructions.

## Process

### 1. Inspect existing conventions

Read the repository instructions and the artifacts relevant to the skills the user actually intends to use. Useful evidence may include:

- `AGENTS.md`, `CLAUDE.md`, contribution docs, and project-local workflow instructions;
- existing GitHub, GitLab, Jira, Linear, or other issue-tracker usage;
- local planning or task directories;
- existing `CONTEXT.md`, glossary, ADR, architecture, or domain-document conventions;
- existing triage labels if the `triage` skill is in use;
- monorepo structure when it materially affects where durable domain documentation belongs.

Prefer established project conventions over creating parallel ones.

### 2. Determine whether setup is needed

Configure only the shared state that has a concrete consumer:

- **Issue tracker or task storage:** useful when `to-spec`, `to-tickets`, `wayfinder`, `triage`, or another workflow needs a durable place to publish artifacts and the project does not already make that destination clear.
- **Triage labels:** useful only when `triage` is installed and the project wants tracker labels for its states.
- **Domain documents:** useful when `domain-modeling` or `grill-with-docs` will maintain durable domain vocabulary or ADRs and no suitable project convention already exists.

If the repository already supplies the necessary conventions, report that no setup is required and stop. Do not rewrite configuration merely to normalize it to this skill's preferred layout.

### 3. Resolve only material choices

Establish factual repository state from evidence. Ask the user only when a material choice remains, such as which of multiple active trackers should receive new work or whether a project with several established documentation locations wants one of them to be canonical.

Recommend the simplest option consistent with existing project practice. Local markdown remains a valid choice when no external tracker is desired.

### 4. Write minimal durable configuration

When configuration is needed, use `docs/agents/` by default unless the repository already has a better location. Write only the files that have actual consumers:

- `docs/agents/issue-tracker.md` for tracker or task-storage conventions;
- `docs/agents/triage-labels.md` when `triage` uses shared label mappings;
- `docs/agents/domain.md` when domain-document location or consumer rules need to be made explicit.

The seed templates in this skill folder can be used as starting points:

- [issue-tracker-github.md](./issue-tracker-github.md)
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md)
- [issue-tracker-local.md](./issue-tracker-local.md)
- [triage-labels.md](./triage-labels.md)
- [domain.md](./domain.md)

For another tracker, record the project's actual workflow directly rather than forcing it into one of these templates.

### 5. Keep agent-policy files narrow

Do not add orchestration, delegation, review, testing, checkpoint, approval, or other engineering policy to `AGENTS.md` or `CLAUDE.md` as part of setup.

If the relevant agent-policy file needs to point agents at the new configuration, propose the smallest useful pointer and follow the repository's normal rules for editing that file. Do not create a new policy file merely because this skill exists, and do not duplicate information that agents can already discover reliably.

### 6. Report the resulting convention

State what was configured, where it lives, and which installed skills will consume it. Mention that these files can be edited directly when the project's workflow changes; re-running setup is optional.