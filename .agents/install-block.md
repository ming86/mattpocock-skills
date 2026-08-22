# The canonical install block

This file is the source of truth for install wording in this fork. Update it before copying install commands elsewhere.

This repository is an adapted fork of `mattpocock/skills`. Installing `mattpocock-skills` from Claude Code's official marketplace installs the upstream distribution, not this fork.

## Claude Code: this fork as a marketplace

Add this repository as a marketplace, then install its plugin:

<canonical-block name="claude-code">

```text
/plugin marketplace add ming86/mattpocock-skills
/plugin install mattpocock-skills@ming86
```

The marketplace follows this repository, so updates come from the fork rather than the upstream official listing.

</canonical-block>

The non-interactive CLI equivalents are:

```bash
claude plugin marketplace add ming86/mattpocock-skills
claude plugin install mattpocock-skills@ming86
```

## Codex and other agents: skills.sh

Use `skills.sh` to copy editable skill files from this fork:

<canonical-block name="skills-sh-whole-set">

```bash
npx skills@latest add ming86/mattpocock-skills
```

Pick the skills you actually want and the coding agents to install them on. `setup-matt-pocock-skills` is optional; install it only when a repository needs shared issue-tracker, triage-label, or domain-document configuration.

</canonical-block>

For one skill:

<canonical-block name="skills-sh-one-skill">

```bash
npx skills@latest add ming86/mattpocock-skills --skill=<name>
```

```bash
npx skills@latest update <name>
```

</canonical-block>

## Choose one installation model

The Claude Code plugin is a managed bundle from this repository. `skills.sh` writes editable skill files into the selected agent environment. Installing both can leave duplicate copies of the same skills, so normally choose one model for a given agent.

Human-facing pages under `docs/` do not include install commands because their publishing layer renders installation separately.