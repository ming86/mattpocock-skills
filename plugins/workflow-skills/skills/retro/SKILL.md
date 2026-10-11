---
name: retro
description: Review the current or an accessible past coding session and propose evidence-backed improvements to the agent's working environment. Use when the user asks for a session retrospective, not to review a patch or diagnose one bug.
disable-model-invocation: true
---

# Retro

Review a coding session to find concrete ways the agent's working environment could support future work better. This is an optional, user-requested retrospective, not a step every task needs.

## Review the session

Use the current conversation and its available records by default. If the user names another session, use that session's primary record, such as an available transcript or supplied log. If evidence for the selected session is partial, state the limit and keep the review within what the evidence supports. If no evidence for the selected session is available, say the retrospective cannot be completed from the available records and stop; do not review another session instead. Do not guess at events or create session-history infrastructure.

Look for session-grounded friction in areas such as:

- finding relevant files, project context, or dependencies;
- getting information or access needed to do the work;
- repeated or unnecessarily costly tool calls;
- instructions or documentation that were unclear, stale, duplicated, or did not affect behavior;
- errors or user corrections that suggest a useful change to the agent's environment.

Consider changes to navigation, available context, tools, instructions, documentation, or checks when the session supports them. For a possible check or standard, connect it to an observed failure and account for the project's existing practices. A missing general lint or CI setup is not a finding on its own.

## Present proposals

Every proposal must point to a specific event or error in the session record. Separate what the record shows from an inferred contributing cause and from the proposed change. Describe the likely benefit and meaningful effort or tradeoff, and prioritize candidates by their likely value. Keep the proposal proportionate to the evidence and the project; do not add candidates just to cover every category.

Return only actionable proposals. If the session provides no clear reason to change the environment, say that no useful improvement surfaced. Do not edit files, create tickets, or turn proposals into requirements as part of this retrospective. Return the proposals and stop; any selected proposal can be handled as separate follow-up work.
