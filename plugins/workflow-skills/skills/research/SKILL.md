---
name: research
description: "Investigate technical or project questions that materially depend on documentation, specifications, source code, APIs, repository evidence, or other primary sources instead of model memory. Use when existing evidence can answer the question without an experiment; separate facts from inference and preserve findings when later work will need them."
---

# Research

Use research when an engineering decision depends on facts that should come from documentation, specifications, source code, APIs, repository evidence, or other primary sources rather than model memory.

## Process

1. **Frame the question.** State the concrete fact, uncertainty, comparison, or decision the research needs to answer or inform. Avoid broad reading without a clear target.
2. **Choose the strongest available sources.** Prefer official documentation, specifications, source code, first-party APIs, release notes, repository history, and other sources that directly define, implement, or document the behavior or claim. Use secondary sources when they add useful interpretation or when no primary source exists, and keep that distinction visible.
3. **Collect only evidence relevant to the question or decision.** Follow a claim back far enough to verify it reliably, then stop. Do not turn focused research into an exhaustive literature review unless the task requires one.
4. **Separate evidence from inference.** Record what the source establishes, what follows by reasonable inference, and what remains uncertain. Include versions, dates, environment assumptions, or repository revisions when they materially affect the conclusion.
5. **Return the finding in the form the work needs.** A concise answer is enough when the result will be used immediately and is cheap to reconstruct. When findings are substantial, expensive to reproduce, or likely to matter after a context or session change, save them with the work. Reuse the work's existing durable location or follow the project's research or durable-state convention. Use local working state when detailed or provisional findings should persist but do not belong in shared project documentation. If no convention exists, use the simplest permitted work-centered location for a low-impact choice; do not silently establish a new shared source of truth when that choice is material. Preserve conclusions, evidence, versions, and remaining uncertainty rather than the investigation transcript.
6. **Link or cite the sources.** Keep enough source detail for another engineer or agent to verify important claims without repeating the whole investigation. A shared project document may already be the right home; local working state is useful when the findings are provisional or too detailed for project documentation. Moving local findings into shared documentation later is optional, not required.
