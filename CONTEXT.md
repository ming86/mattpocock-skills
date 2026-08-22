# Adapted Agent Skills

A collection of optional engineering and productivity procedures derived from Matt Pocock's skills. In this fork, project or user-level agent instructions remain authoritative for engineering policy; skills provide reusable procedures for particular situations.

## Language

**Governing agent policy**:
The project or user instructions that own scope, orchestration, delegation, consultation, checkpoints, validation, commits, and independent review. `AGENTS.md`, `CLAUDE.md`, or equivalent instructions can provide this policy. A workflow skill does not replace it.

**Durable project state**:
Information that later agent contexts or engineers must be able to recover without depending on conversation memory. It may live in repository documents, an issue tracker, specifications, tickets, ADRs, code, tests, or another established project artifact.

**Issue tracker**:
A tool or convention used to store tracked work, such as GitHub Issues, GitLab Issues, Jira, Linear, or local markdown. It is one possible home for durable project state, not a prerequisite for every skill.

**Work unit**:
A coherent bounded unit of execution, investigation, clarification, or prototyping with a meaningful outcome and enough focused context to be handled reliably. A work unit may be represented as an issue, ticket, local file, or another project artifact.

**Ticket**:
A durable representation of a work unit produced or consumed by a ticket-oriented workflow. `to-tickets` uses the term because the output is commonly placed in an issue tracker, but the underlying boundary is the work unit rather than the tracker object.

**Ready frontier**:
The set of work units whose genuine blockers are resolved. Units on the frontier may be executed independently or in parallel only when the governing agent policy and integration constraints permit it.

**Wayfinder map**:
A durable low-resolution index for a large or uncertain effort. It records the destination, established context, decisions, unresolved questions, dependencies, and important uncertainty that is not yet precise enough to become a separate work unit.

## Relationships

- The **Governing agent policy** controls how skills are used and how work is orchestrated.
- **Durable project state** lets fresh contexts recover decisions and progress without carrying the full prior conversation.
- An **Issue tracker** can hold **Tickets** and other durable artifacts, but local repository documents can serve the same persistence role.
- A **Ticket** represents a **Work unit**.
- Resolved dependencies determine the **Ready frontier**.
- A **Wayfinder map** can produce new **Work units** as uncertainty becomes precise enough to investigate or decide.

## Important distinctions

- Workflow skills are procedures, not mandatory gates.
- A fresh context is useful only when the work boundary is coherent; context isolation does not compensate for bad decomposition.
- Requirements and explicit decisions are not the same as discovered facts, working assumptions, or unresolved points.
- `code-review` checks bounded implementation conformance; broader independent criticism can remain a separate project-level review mechanism.
- `setup-matt-pocock-skills` is optional configuration for repositories that need shared tracker, triage-label, or domain-document conventions.