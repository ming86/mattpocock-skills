---
name: writing-agent-instructions
description: Write, edit, or review reusable instructions that coding agents consume, including AGENTS.md, CLAUDE.md, skill instructions and descriptions, agent definitions, reusable prompts, and referenced instruction files. Use when improving how agent-facing instructions trigger, guide behavior, divide always-loaded from conditional context, avoid duplicate or stale rules, or state completion conditions clearly.
---

# Writing Agent Instructions

Write instructions to change agent behavior, not to document everything a human could know.

This skill covers the behavioral design of agent-facing instructions. Skill packaging, bundled resources, metadata schemas, and host-specific mechanics belong to the relevant skill-creation tooling.

## Put information where it is needed

Place material according to how broadly and how often the agent needs it.

Always-loaded instructions have the highest ongoing cost in context and attention, so keep them for behavior that must remain broadly available. Put branch-specific or task-specific guidance behind a skill, reference, or other conditional path when the agent only needs it in those situations.

Treat the project environment as information too. Do not restate facts the agent can cheaply and reliably read from source, configuration, directory structure, or tool output unless the instruction adds a non-obvious convention, rationale, boundary, or shortcut that materially changes the work, or repeated lookup would itself be materially costly or unreliable.

## Make routing text do real work

Descriptions, pointers, and other routing text determine whether the agent reaches conditional instructions.

State what the material is for and cover the distinct situations that should load it. Prefer one clear trigger for each genuinely different branch over several synonyms for the same case. Put the most discriminating language early enough to guide routing before generic wording dominates.

Keep invocation conditions in material that is available before invocation. Do not rely on a skill body or referenced file to explain when it should have been loaded.

## Write for executable behavior

State the behavior the agent should perform in direct terms. Use examples when they clarify the intended shape better than additional explanation.

For ordered work, make the end of a step clear enough that the agent can distinguish done from merely started. Use a concrete completion condition when premature completion would otherwise be plausible. Do not manufacture formal gates for work whose natural stopping point is already obvious.

Match specificity to the task. Fragile or highly constrained work may need exact instructions; variable work is better guided by principles, boundaries, and decision criteria that leave room for judgment.

## Keep each behavioral instruction in one primary place

Avoid maintaining the same behavioral rule independently in several instruction files. Duplication spends extra context, makes the repeated idea appear more important than intended, and makes later changes harder to keep consistent.

When several places need the same guidance, keep one primary source and point to it where practical. Repeat a short term or label only when the repetition helps the agent recognize the same established concept; do not repeat the full meaning merely for emphasis.

## Calibrate instructions to actual model behavior

Judge an instruction by whether it materially changes behavior relative to the models and environment that will consume it.

Remove explanation that the model already follows reliably when it adds no useful distinction. Keep concise instructions that suppress an observed failure mode even when the desired behavior seems obvious to a human reader.

Prefer stating the target behavior directly when that is sufficient. Explicit prohibitions remain appropriate for hard boundaries or recurring failure modes where naming the unwanted behavior improves compliance.

## Prune as well as add

Instruction sets accumulate residue when every observed failure adds another permanent rule. Periodically look for stale assumptions, duplicated meanings, superseded guidance, and instructions that no longer affect behavior.

Do not remove a rule only because it looks redundant in isolation. Consider why it exists and whether representative behavior still depends on it. When uncertainty matters, a small targeted comparison is more useful than debating the wording abstractly.
