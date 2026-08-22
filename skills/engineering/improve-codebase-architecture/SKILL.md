---
name: improve-codebase-architecture
description: Survey a codebase for concrete deepening opportunities, present evidence-backed candidates, and explore the one the user chooses.
disable-model-invocation: true
---

# Improve Codebase Architecture

Surface architectural friction and propose **deepening opportunities**: refactors that turn shallow modules into deep ones. The aim is testability and AI-navigability.

This command is _informed_ by the project's domain model and built on a shared design vocabulary:

- Use `codebase-design` for the architecture vocabulary (**module**, **interface**, **depth**, **seam**, **adapter**, **leverage**, **locality**) and its principles (the deletion test, "the interface is the test surface", "one adapter = hypothetical seam, two = real"). Use that vocabulary when it sharpens the analysis while preserving the repository's established names for actual modules and domain concepts.
- Use the project's established domain vocabulary and architectural decision records when they exist. They are evidence about meaningful seams and prior tradeoffs, not a requirement to create `CONTEXT.md` or an ADR tree.

## Process

### 1. Explore

**Scope before you scan: YAGNI.** Deepening a module pays off by making future changes to it easier, so put extra weight on the parts of the codebase that have recently changed. Decide *where* to look before you look:

- If the user named a direction (a module, a subsystem, a pain point), take it, and skip the inference below.
- Otherwise, walk back a good stretch of the commit history (`git log --oneline`) to find the codebase's hot spots, the files and areas that keep coming up, and let those paths pull your attention first. If the changes are scattered with no clear hot spot, widen the net.

Read the relevant domain glossary, architecture notes, or ADRs when the project has them.

Explore the relevant codebase surface directly or through workers chosen by the governing orchestration policy. The skill needs credible findings, not a particular execution topology. Do not follow rigid heuristics; explore organically and note where you experience friction:

- Where does understanding one concept require bouncing between many small modules?
- Where are modules **shallow**, with an interface nearly as complex as the implementation?
- Where have pure functions been extracted just for testability, but the real bugs hide in how they're called (no **locality**)?
- Where do tightly-coupled modules leak across their seams?
- Which parts of the codebase are untested, or hard to test through their current interface?

Apply the **deletion test** to anything you suspect is shallow: would deleting it concentrate complexity, or just move it? A "yes, concentrates" is the signal you want.

### 2. Present the candidates

Present only candidates backed by concrete friction from the inspected code. For each candidate include:

- **Files or modules:** the affected surface;
- **Problem:** what makes the current structure hard to understand, change, or verify;
- **Proposed direction:** what would become deeper or move behind a clearer seam;
- **Expected benefit:** the concrete improvement in locality, leverage, testability, or navigability;
- **Confidence:** whether the evidence makes it a strong recommendation, worth exploring, or speculative.

Default to concise text when that communicates the candidates clearly. Use a temporary visual HTML report, Mermaid diagram, or before/after visualization only when the relationships are complex enough that the visual materially improves the decision. If you use the HTML scaffold in [HTML-REPORT.md](HTML-REPORT.md), keep it outside the repository unless the user explicitly wants a persistent artifact.

Do not design detailed interfaces for every candidate. Present the evidence first and ask the user which candidate, if any, is worth exploring further.

### 3. Grilling loop

Once the user picks a candidate, call the Skill tool with "grilling" to walk the decision tree with them: constraints, dependencies, the shape of the deepened module, what sits behind the seam, what tests survive.

Preserve durable domain or architecture decisions only when later work genuinely depends on them, using the repository's established documentation convention. `domain-modeling` can help when the domain vocabulary itself changed; do not create or update `CONTEXT.md` or ADRs merely because this skill is running.

- **A term or domain relationship materially changed?** Use the project's existing domain artifact when one exists and the change will matter later.
- **The user rejects a candidate for a durable, load-bearing reason?** Offer to record the reason only when doing so would prevent meaningful future rework; skip ephemeral reasons such as "not worth it right now."
- **Want to explore alternative interfaces for the deepened module?** Use `codebase-design` and its `DESIGN-IT-TWICE.md` procedure. The governing orchestration policy decides whether alternatives are generated sequentially or by independent workers.
