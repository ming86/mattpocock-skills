# Research

## What it does

`research` establishes technical or project facts from high-trust sources before those facts become assumptions in a design or implementation decision. It keeps source evidence, reasonable inference, and unresolved uncertainty distinct.

The fork does not require research to run in a background agent or to produce a repository file. Delegation and durable storage are decisions for the governing project workflow.

## When to reach for it

Use it when current documentation, APIs, specifications, source code, release notes, or repository evidence need to be checked before an engineering decision can be made reliably.

Do not invoke it for broad reading with no decision-relevant question unless the user actually asked for open-ended research.

## Common questions

**Does research always use a separate worker?**

No. The root orchestration policy decides whether research is done directly or delegated. The skill defines the evidence discipline, not the worker topology.

**Does every research result become a Markdown file?**

No. Return a concise finding when that is enough. Preserve a durable note only when later contexts or engineers need the evidence and use the repository's existing convention when one exists.

**Are secondary sources forbidden?**

No. Prefer the source that owns a claim when possible. Secondary sources can add useful interpretation or cover cases where no primary source exists, but keep their status visible.

## It's working if

The important claims can be traced to appropriate sources, versions or dates are captured when they matter, inference is not presented as fact, and the investigation stops once enough evidence exists for the decision it was meant to inform.
