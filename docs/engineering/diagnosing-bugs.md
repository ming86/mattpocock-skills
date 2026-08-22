# Diagnosing Bugs

## What it does

`diagnosing-bugs` provides an evidence-driven loop for difficult bugs and performance regressions. Its core idea is to obtain a signal that can distinguish the reported failure, use that signal to test plausible causes, fix the established cause, and preserve useful regression evidence.

The fork deliberately treats the loop as proportional. A small bug with an obvious failing test does not need a six-phase investigation, while an intermittent production regression may justify a reproduction harness, repeated measurements, or bisection.

## When to reach for it

Use it when straightforward inspection is not enough to identify the cause reliably, when several explanations remain plausible, or when a performance or intermittent failure needs measured evidence.

For a simple localized defect whose cause and validation are already clear, direct implementation may be enough.

## Common questions

**Do I need a perfect automated reproduction before forming a hypothesis?**

No. Prefer a credible feedback loop because it makes diagnosis less speculative, but do not turn the harness into a project of its own. If automation is impractical, use the best available evidence and state the reduced confidence.

**Does every bug need several hypotheses?**

No. Multiple falsifiable hypotheses are useful when the cause is uncertain. Direct evidence can make a single cause sufficiently established without manufacturing alternatives.

**Does the skill require a regression test or commit?**

No. Add a regression test when there is a correct observable seam and the test materially protects the behavior. Commits, pull requests, and review remain governed by project instructions.

## It's working if

The diagnosis is driven by evidence rather than a plausible story, the fix addresses the reported symptom, temporary instrumentation is cleaned up, and any remaining uncertainty is visible to the next engineer or agent.
