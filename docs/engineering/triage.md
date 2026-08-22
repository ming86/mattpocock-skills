# Triage

## What it does

`triage` helps a maintainer move incoming issues and external pull requests through the repository's configured triage roles. It gathers evidence, recommends a state, verifies claims when useful, clarifies material gaps, and writes an agent-ready brief when the work is ready for delegation.

The tracker state machine is deliberate triage behavior. Broader engineering policy, durable documentation, and issue-closing authority remain subject to the repository's conventions and maintainer direction. Public AI-disclosure wording is likewise a repository policy rather than a hard-coded skill requirement.

## When to reach for it

Use it when a project has an established issue-tracker triage workflow and incoming requests need classification, verification, clarification, or an execution brief.

If the project does not use the configured roles or labels, establish the needed conventions first rather than guessing them.

## Common questions

**Does triage always run a grilling and domain-modeling session?**

No. Clarify only when material ambiguity prevents a reliable state or brief. Use domain modeling only when the domain vocabulary or relationships are themselves part of the ambiguity.

**Does every rejected enhancement go into `.out-of-scope/`?**

No. Consult that knowledge base when the repository already uses it. Record a rejected direction only when the convention is established and the durable reason has concrete future value, or when the maintainer asks for it.

**Does an old rejection permanently block a new issue?**

No. Treat prior decisions as evidence. Surface them to the maintainer so changed constraints or direction can be recognized.

## It's working if

The maintainer can see the evidence behind the recommended state, resolved information is not re-asked, agent-ready work has verifiable acceptance criteria, and triage does not create durable policy or documentation that the project did not ask for.
