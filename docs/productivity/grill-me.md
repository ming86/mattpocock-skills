## What it does

`grill-me` starts a focused clarification interview for a plan, design, decision, or idea without adding repository-specific documentation behavior.

It delegates to [`grilling`](../../skills/productivity/grilling/SKILL.md), whose goal is to resolve material ambiguity rather than exhaust every imaginable branch.

## When to reach for it

Type `/grill-me` when you want the agent to challenge and clarify your thinking but do not need the repository-aware behavior of [`grill-with-docs`](../../skills/engineering/grill-with-docs/SKILL.md).

It is useful for plans, designs, proposals, decisions, and other work where the important missing information is your judgment rather than a fact the agent can look up.

## Common questions

**Is it still a deep interview?**

It can be. Depth follows the material uncertainty in the subject. A genuinely ambiguous decision may require several rounds; a mostly settled plan may require only one or two questions.

**What is the difference from `grill-with-docs`?**

`grill-with-docs` also inspects repository evidence and can preserve useful decisions in project artifacts. `grill-me` is the simpler general-purpose entry point.

## It's working if

- Each question can change or clarify something that matters.
- Facts available to the agent are not turned into questions for you.
- The session ends when the intended next step is sufficiently clear.

## Where it fits

This is the user-invoked general wrapper around [`grilling`](../../skills/productivity/grilling/SKILL.md).