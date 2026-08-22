# Issue tracker: Local Markdown

Issues and specs for this repo live as markdown files in `.scratch/`.

## Conventions

- One feature per directory: `.scratch/<feature-slug>/`
- The spec is `.scratch/<feature-slug>/spec.md`
- Implementation issues are one file per ticket at `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, numbered from `01`, never a single combined tickets file
- Triage state is recorded as a `Status:` line near the top of each issue file (see `triage-labels.md` for the role strings)
- Comments and conversation history append to the bottom of the file under a `## Comments` heading

## When a skill says "publish to the issue tracker"

Create a new file under `.scratch/<feature-slug>/` (creating the directory if needed).

## When a skill says "fetch the relevant ticket"

Read the file at the referenced path. The user will normally pass the path or the issue number directly.

## Wayfinding storage

When the project chooses local Markdown for durable Wayfinder state:

- **Map:** keep one `map.md` for the effort using the current Wayfinder sections such as Destination, Established context, Decisions so far, Open questions, Not yet clear enough to decide, and Out of scope.
- **Work units:** use one file per precise research, prototype, clarification, or enabling unit when separate files materially help independent execution or dependency tracking. Small efforts can keep open questions directly in the map.
- **Dependencies:** record genuine blockers explicitly when separate units depend on one another, for example a `Blocked by: 01, 03` line when numbered issue files are the local convention.
- **Ready frontier:** ready means genuine blockers are resolved. File numbering or listing order does not decide execution order; the governing orchestration policy does.
- **Results:** record the outcome near the work unit or source evidence and update the canonical map with material decisions, facts, and newly exposed questions. Do not require a gist, assignment state, or other tracker emulation unless the project actually uses it.
