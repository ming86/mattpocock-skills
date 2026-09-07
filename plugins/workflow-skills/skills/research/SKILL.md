---
name: research
description: "Investigate questions, claims, comparisons, or decisions using documents, records, data, published research, source code, or other relevant sources rather than relying on model memory. Use when existing evidence can answer or materially inform a question without an experiment; distinguish what sources establish from inference and uncertainty, and preserve findings when later work will need them."
---

# Research

Investigate the question using relevant documents, records, data, published research, source code, or other evidence rather than relying on model memory.

## Process

1. **Frame the question.** State the concrete uncertainty, comparison, behavior, or choice the research needs to answer or inform. Keep the research target specific enough to know when the question has been answered.
2. **Choose the strongest available sources.** Choose sources for their relevance and ability to support the claim. Use original records, data, research, and other primary sources where they provide the needed evidence, and reliable synthesis or interpretation when it helps establish the broader picture or no primary source is available. Keep those source types distinct. For software and engineering questions, prefer official documentation, specifications, source code, first-party APIs, release notes, and repository history that directly define, implement, or document the relevant behavior.
3. **Collect evidence relevant to the question.** Follow a claim back far enough to support it reliably, then stop when the research has enough support for the work at hand.
4. **Separate source findings from inference.** Record what each source directly shows or states, what follows by reasonable inference, and what remains uncertain. A source may show current practice or behavior, documented intent, a proposal, or historical context without establishing the others. Include dates, scope, versions, environment assumptions, or repository revisions when they affect the conclusion.
5. **Return the finding in the form the work needs.** A concise answer is enough when the result will be used immediately and is cheap to reconstruct. When findings are substantial, expensive to reproduce, or likely to matter after a context or session change, save them with the work. Reuse the work's existing location or follow how the project normally saves research findings. Use local working state when detailed or provisional findings should persist but do not belong in shared project documentation. If no convention exists, keep the findings in the simplest work-centered location that fits their expected use. Preserve conclusions, source support, versions, and remaining uncertainty rather than the investigation transcript.
6. **Link or cite the sources.** Keep enough source detail for another person or agent to check important claims without repeating the whole investigation. A shared project document may already be the right home; local working state is useful when the findings are provisional or too detailed for project documentation. Moving local findings into shared documentation later is optional, not required.
