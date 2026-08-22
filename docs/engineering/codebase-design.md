# Codebase Design

## What it does

`codebase-design` provides analytical vocabulary for reasoning about **modules**, **interfaces**, **depth**, **seams**, **adapters**, **leverage**, and **locality**. The goal is to put useful behavior behind interfaces that are small enough for callers and tests to understand without overriding the repository's established names for its actual modules and domain concepts.

Its supporting `DESIGN-IT-TWICE.md` procedure helps compare materially different interface designs before converging.

## When to reach for it

Use it when the shape of a module or interface is the design question, when a seam is difficult to place, or when tests are awkward because callers need to know too much about the implementation.

It can also act as vocabulary underneath another workflow such as architecture review or TDD.

## Common questions

**Does design-it-twice require parallel subagents?**

No. The useful mechanism is independent alternatives. The governing orchestration policy decides whether they are produced sequentially, in fresh contexts, or by separate workers.

**Is a new interface always desirable?**

No. A seam needs concrete leverage. If nothing meaningfully varies across it and it does not hide useful complexity, another abstraction can make the codebase shallower rather than deeper.

## It's working if

The chosen interface hides material complexity, concentrates change, gives callers a smaller surface to learn, and provides a meaningful seam for verification without introducing abstraction for its own sake.
