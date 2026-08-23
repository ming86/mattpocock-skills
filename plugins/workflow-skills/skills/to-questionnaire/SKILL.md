---
name: to-questionnaire
description: "Turn missing decisions or facts owned by another person into a focused questionnaire. Use when the current user cannot responsibly supply the information, repository research cannot answer it, and progress depends on an external decision-maker or domain expert."
argument-hint: "Who should answer, and what do you need back?"
disable-model-invocation: true
---

# To Questionnaire

Use this skill when the missing information belongs to another person. The goal is to ask the right person efficiently, not to pressure the current user or the model into inventing an answer.

If repository evidence can establish the answer, research it. If the current user owns the decision, clarify it with them. If nobody knows yet and evidence must be created, use an experiment or prototype. Use a questionnaire when another identifiable person or role holds the needed judgment, facts, or domain knowledge.

## Clarify who should answer and what you need back

Do not interview the user about subject matter they have already established they cannot answer. Resolve what you can from existing context, then clarify only these two things when needed:

1. **Who should answer?** Establish the recipient or responsible role, their relevant expertise, and enough relationship/context to pitch the questionnaire appropriately.
2. **What must come back?** Identify the decisions, facts, constraints, or confirmations the work needs. Focus on what the user must be able to decide or do after receiving the response.

Ask these only when the current conversation or work artifacts do not already establish them.

## Draft the questionnaire

Create questions that target the gap between what the recipient knows and what the work needs.

- Put the highest-value questions first because an asynchronous response may be incomplete.
- Ask one idea per question. Split compound questions.
- Give enough context to answer well without reproducing the entire project history.
- Explain why a question matters only when that is likely to improve the answer.
- Make uncertainty safe: "I don't know," partial answers, caveats, and confidence levels can be useful evidence.
- Do not bias the recipient toward a preferred answer unless a real constraint or tradeoff must be stated.
- Do not invent deadlines, effort estimates, authority, or delivery channels that the user has not established.

## Artifact and authority

Produce the questionnaire in the requested delivery format when one is specified. Otherwise, create or return a Markdown draft appropriate for the work.

When a durable copy is useful, reuse the work's existing location or follow the project's documentation or durable-state convention. A local working-state location is appropriate for a provisional draft that should survive contexts without becoming shared project documentation. Do not silently make the questionnaire a new shared source of truth when that choice is material.

The questionnaire is a request for information, not the resulting project decision. When answers return, preserve their provenance and uncertainty; incorporate them into a spec, issue, model, or other source of truth only through the work's normal decision process.

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
