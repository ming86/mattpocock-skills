---
name: research
description: "Investigate technical or project questions that depend on documentation, specifications, source code, APIs, repository history, or other primary sources rather than model memory. Use when existing sources can answer the question without an experiment; distinguish what the sources show from what is inferred and preserve findings when later work will need them."
---

# Research

Use research when the work depends on information that should come from documentation, specifications, source code, APIs, repository history, or other primary sources rather than model memory.

## Process

1. **Frame the question.** State the concrete uncertainty, comparison, behavior, or choice the research needs to answer or inform. Keep the research target specific enough to know when the question has been answered.
2. **Choose the strongest available sources.** Prefer official documentation, specifications, source code, first-party APIs, release notes, repository history, and other sources that directly define, implement, or document the behavior or claim. Use secondary sources when they add useful interpretation or when no primary source exists, and keep that distinction visible.
3. **Collect evidence relevant to the question.** Follow a claim back far enough to support it reliably, then stop when the research has enough support for the work at hand.
4. **Separate source findings from inference.** Record what each source directly shows or states, what follows by reasonable inference, and what remains uncertain. A source may show current behavior, documented intent, or historical context without showing all three. Include versions, dates, environment assumptions, or repository revisions when they affect the conclusion.
5. **Return the finding in the form the work needs.** A concise answer is enough when the result will be used immediately and is cheap to reconstruct. When findings are substantial, expensive to reproduce, or likely to matter after a context or session change, save them with the work. Reuse the work's existing location or follow how the project normally saves research findings. Use local working state when detailed or provisional findings should persist but do not belong in shared project documentation. If no convention exists, keep the findings in the simplest work-centered location that fits their expected use. Preserve conclusions, source support, versions, and remaining uncertainty rather than the investigation transcript.
6. **Link or cite the sources.** Keep enough source detail for another engineer or agent to check important claims without repeating the whole investigation. A shared project document may already be the right home; local working state is useful when the findings are provisional or too detailed for project documentation. Moving local findings into shared documentation later is optional, not required.
