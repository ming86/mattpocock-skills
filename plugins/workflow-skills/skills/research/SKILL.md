---
name: research
description: "Investigate technical or project questions that materially depend on documentation, specifications, source code, APIs, repository evidence, or other primary sources rather than model memory. Use when evidence can resolve the uncertainty without building an experiment; distinguish established facts from inference and preserve findings when later work needs them."
---

# Research

Use research when an engineering decision depends on facts that should be established from documentation, specifications, source code, APIs, repository evidence, or other primary sources rather than guessed from model memory.

Follow the governing project instructions for delegation and context management. Research can be performed directly or delegated according to the governing project or harness policy; this skill does not require a background agent.

## Process

1. **Frame the question.** State the concrete fact, uncertainty, comparison, or decision the research needs to inform. Avoid broad reading without a decision-relevant target.
2. **Choose the strongest available sources.** Prefer official documentation, specifications, source code, first-party APIs, release notes, repository history, and other sources that own the claim. Use secondary sources when they add useful interpretation or when no primary source exists, and keep that distinction visible.
3. **Collect only decision-relevant evidence.** Follow a claim back far enough to establish it reliably, then stop. Do not turn research into an exhaustive literature review unless the task actually requires one.
4. **Separate evidence from inference.** Record what the source establishes, what follows by reasonable inference, and what remains uncertain. Include versions, dates, environment assumptions, or repository revisions when they materially affect the conclusion.
5. **Return the finding in the form the current work needs.** A concise answer may be enough when the result is immediately consumed and cheap to reconstruct. When findings are substantial, expensive to reproduce, or likely to matter after a context or session boundary, persist them as work-centered state. Reuse an existing work location first; otherwise use the project's configured local working-state or research location, or the simplest permitted work-centered local artifact when no convention exists. Preserve conclusions, evidence, versions, and remaining uncertainty rather than the investigation transcript.
6. **Link or cite the sources.** Preserve enough source detail for another engineer or agent to verify the important claims without repeating the whole investigation. Promote findings into shared project documentation only when they belong there; a local working artifact may remain provisional.
