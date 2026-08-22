# Writing docs pages in this fork

Promoted skills in `skills/engineering/` and `skills/productivity/` have a corresponding human-facing page under `docs/<bucket>/<skill-name>.md`.

The docs page helps a reader decide whether and when to use the skill. It is not a second copy of `SKILL.md` and does not need to describe every implementation step.

## Update a page when behavior changes

When a promoted skill changes in a way that would make its existing page misleading, update the page in the same work. Preserve useful explanations and questions that remain accurate; remove upstream-specific claims, fixed workflows, mandatory gates, or publication links that no longer describe this fork.

A useful page normally answers:

- What problem does this skill solve?
- When is it useful, and when is it unnecessary?
- What is its defining constraint or stopping condition?
- What durable artifact or evidence does it produce, if any?
- Which neighboring skills are commonly confused with it?
- What does successful use look like?

Use headings that make those answers easy to find. Common sections such as `What it does`, `When to reach for it`, `Common questions`, `It's working if`, and `Where it fits` are useful when they add information, but they are not mandatory furniture.

## Links

These docs are maintained for the fork repository. Use repository-relative links for other files and skills in this repo. Do not send readers to `aihero.dev` for the behavior of an adapted skill, because that site documents upstream behavior that may differ from this fork.

## Installation

Do not copy install commands into every skill page. Keep the canonical fork installation in the top-level `README.md` and [.agents/install-block.md](./install-block.md).

## Style

Keep documentation proportional to the skill. Prefer concrete explanations of the mechanism and decision boundary over marketing language or exhaustive process narration.

Do not use em dashes in repository prose.