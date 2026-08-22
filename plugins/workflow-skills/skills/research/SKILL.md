---
name: research
description: Investigate a technical or project question against high-trust primary sources, distinguish evidence from inference, and preserve durable findings when later work needs them.
---

# Research

Use research when an engineering decision depends on facts that should be established from documentation, specifications, source code, APIs, repository evidence, or other primary sources rather than guessed from model memory.

Follow the governing project instructions for delegation and context management. Research can be performed directly or delegated according to the governing project or harness policy; this skill does not require a background agent.

## Process

1. **Frame the question.** State the concrete fact, uncertainty, comparison, or decision the research needs to inform. Avoid broad reading without a decision-relevant target.
2. **Choose the strongest available sources.** Prefer official documentation, specifications, source code, first-party APIs, release notes, repository history, and other sources that own the claim. Use secondary sources when they add useful interpretation or when no primary source exists, and keep that distinction visible.
3. **Collect only decision-relevant evidence.** Follow a claim back far enough to establish it reliably, then stop. Do not turn research into an exhaustive literature review unless the task actually requires one.
4. **Separate evidence from inference.** Record what the source establishes, what follows by reasonable inference, and what remains uncertain. Include versions, dates, environment assumptions, or repository revisions when they materially affect the conclusion.
5. **Return the finding in the form the current work needs.** A concise answer may be enough for the current context. When later contexts or engineers need the evidence, save it in the repository's established research or planning location, or another durable artifact chosen by governing project conventions. Do not create a Markdown file merely because this skill is running.
6. **Link or cite the sources.** Preserve enough source detail for another engineer or agent to verify the important claims without repeating the whole investigation.
