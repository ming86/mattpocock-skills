Skills are organized into bucket folders under `skills/`:

- `engineering/`: promoted skills for code and engineering work
- `productivity/`: promoted general workflow skills
- `misc/`: retained but not promoted
- `in-progress/`: experimental skills that are intentionally not shipped in the plugin
- `deprecated/`: no longer used

`AGENTS.md` is a symlink to this file, so these are the repository-local instructions for agents working on the fork.

Read [FORK.md](./FORK.md) before changing workflow behavior. The governing principle is that project or user-level agent instructions own engineering policy such as scope, orchestration, delegation, consultation, checkpoints, validation, commits, and independent review. Skills provide optional procedures and should not silently create a second policy layer.

## Promoted skill consistency

Every skill in `engineering/` or `productivity/` must have:

- an entry in the matching bucket `README.md`;
- an entry in the top-level `README.md`;
- an entry in `.claude-plugin/plugin.json`'s `skills` array;
- a human-facing page at `docs/<bucket>/<skill-name>.md`.

Skills in `misc/`, `in-progress/`, and `deprecated/` do not belong in the plugin manifest or top-level promoted-skill list and do not require a docs page.

When a promoted skill's behavior changes, update its descriptions and docs where the old behavior would otherwise mislead a reader. Keep docs concise and consistent with the current `SKILL.md`; do not reproduce the runbook verbatim. See [.agents/writing-docs.md](./.agents/writing-docs.md).

## Invocation metadata

Every promoted `SKILL.md` is either user-invoked (`disable-model-invocation: true` plus `policy.allow_implicit_invocation: false` in `agents/openai.yaml`) or model-invoked. Keep those two representations aligned. See [.agents/invocation.md](./.agents/invocation.md) when changing invocation behavior.

[`ask-matt`](./skills/engineering/ask-matt/SKILL.md) is retained as the compatibility router. When a user-reachable skill is added, removed, renamed, or changes how it fits with other workflows, update the router so it does not describe a stale flow.

## Distribution metadata

Install wording for this fork lives in [.agents/install-block.md](./.agents/install-block.md). Commands in the top-level README should match it.

The fork's Claude marketplace and plugin metadata live in `.claude-plugin/marketplace.json` and `.claude-plugin/plugin.json`. After changing either manifest, validate it with `claude plugin validate . --strict` when Claude Code is available.

Run `npm run check-plugin-version` after changing version metadata.

## Local skill links

`scripts/link-skills.sh` links skills into the local harness skill directories (`~/.claude/skills`, `~/.agents/skills`). Re-run it after adding, removing, or renaming a skill when local links need refreshing.

## Prose convention

Do not use em dashes in repository prose. Rewrite the sentence with a comma, colon, period, parentheses, or conjunction instead of mechanically substituting another character.