# Test-Driven Development

## What it does

`tdd` supplies a focused red-green-refactor loop for work where test-first development provides useful feedback. It emphasizes tests that can disagree with the implementation and observe behavior through a meaningful seam.

TDD is a technique in this fork, not a mandatory phase inside `implement`.

## When to reach for it

Use it when the requested behavior can be expressed cleanly through an observable interface and writing the test first will sharpen the requirement, protect a regression, or guide a small implementation slice.

Do not force it onto changes where another validation technique provides clearer or cheaper evidence.

## Common questions

**Do test seams need user approval before I write any test?**

Not routinely. Derive established seams from the spec, architecture, call sites, and existing tests. Consult the user when choosing among materially different seams would itself change architecture, scope, or what the test proves.

**Is refactoring forbidden during the loop?**

No. Refactor with the relevant tests green when the current slice exposes a concrete design problem. Avoid speculative refactoring that is unrelated to the behavior being developed.

**Does invoking `tdd` mean the whole feature must be test-first?**

No. Continue the loop only while it provides useful feedback.

## It's working if

Each red test expresses a real behavior, the smallest coherent implementation makes it green, refactoring preserves that behavior, and the resulting tests remain useful when internals change.
