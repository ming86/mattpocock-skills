---
name: to-questionnaire
description: "Turn needed input from another person or domain expert into a focused questionnaire. Use when progress depends on information, expertise, context, or judgment that the current user and project sources cannot supply reliably."
argument-hint: "Who should answer, and what do you need back?"
disable-model-invocation: true
---

# To Questionnaire

Use this skill when another identifiable person or role is best placed to provide input the work needs. Route other uncertainty through project research, user clarification, engineering judgment, or an experiment as appropriate.

## Clarify who should answer and what you need back

When the current user has already established that they cannot supply the subject matter, focus clarification on these two things when they are not already clear:

1. **Who should answer?** Establish the recipient or responsible role, their relevant expertise, and enough relationship/context to pitch the questionnaire appropriately.
2. **What must come back?** Identify the information, constraints, confirmations, choices, or judgment the work needs. Focus on what the user must be able to decide or do after receiving the response.

Use the current conversation and work artifacts to answer these where possible.

## Draft the questionnaire

Create questions that target the gap between what the recipient knows and what the work needs.

- Put the highest-value questions first because an asynchronous response may be incomplete.
- Ask one idea per question. Split compound questions.
- Give enough context to answer well without reproducing the entire project history.
- Explain why a question matters when that is likely to improve the answer.
- Make uncertainty safe: "I don't know," partial answers, caveats, and confidence levels can be useful input.
- Present constraints and tradeoffs neutrally so the recipient can answer without being steered toward a preferred result.
- Use only deadlines, decision roles, and delivery channels already established by the user or project context.

## Questionnaire and answers

Produce the questionnaire in the requested delivery format when one is specified. Otherwise, create or return a Markdown draft appropriate for the work.

When a durable copy is useful, reuse the work's existing location or follow the project's documentation or durable-state convention. A local working-state location is appropriate for a provisional draft that should survive contexts without becoming shared project documentation.

The questionnaire requests input; it does not itself settle the resulting project direction. When answers return, keep track of who supplied them and any uncertainty. Treat the answers as sourced input until the relevant spec, issue, model, or other project state incorporates them.

## Suggested structure

Use only the sections that help the recipient answer.

```markdown
# <Questionnaire title>

**Purpose:** <why this information is needed and what decision or work depends on it>

**For:** <recipient or role>

## Context

<short orientation needed to answer accurately>

## Questions

### 1. <single focused question>

<optional: why this matters, only when useful>

> Answer:

### 2. <single focused question>

> Answer:

## Anything else?

<optional catch-all for important context the questionnaire failed to ask about>
```
