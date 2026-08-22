---
name: tdd
description: Use a focused test-first red-green-refactor loop when test-driven development is appropriate for the behavior and repository.
---

# Test-Driven Development

TDD is a technique for discovering and protecting behavior through a short test-first loop. Use it when the requested work, repository practices, or uncertainty benefit from test-first execution. It is not a prerequisite for `implement` or for every code change.

When exploring the codebase, use the project's domain language and existing test conventions. Follow governing project instructions for user consultation, validation scope, review, and commits.

## What a useful test is

Tests should verify behavior through an observable interface rather than mirror implementation details. A good test can fail when the required behavior is wrong and remain valid when internals are refactored without changing that behavior.

See [tests.md](tests.md) for examples and [mocking.md](mocking.md) for mocking guidance.

## Choose the seam deliberately

A **seam** is the interface through which the test observes behavior. Prefer an existing public or integration boundary that represents the real behavior being changed.

Establish the relevant seam from the spec, ticket, repository architecture, existing tests, and call sites. If materially different seam choices would change architecture, scope, or what the test proves, surface that design decision according to the governing consultation rules. Do not require user confirmation for a routine seam that is already established by the codebase.

When the interface itself is the design question, use `codebase-design` as a vocabulary and reasoning reference.

## The loop

1. **Red.** Write one focused test that expresses the next behavior or regression case. Run it and establish that it fails for the expected reason.
2. **Green.** Make the smallest coherent implementation change that satisfies that test without speculatively implementing later cases.
3. **Refactor when useful.** With the relevant tests green, improve the implementation or test structure only when the current slice exposed a concrete design problem. Keep behavior unchanged and re-run the focused tests.
4. **Repeat.** Choose the next meaningful behavior slice only while test-first execution is still providing useful feedback.

Prefer vertical behavior slices over writing a large speculative batch of tests against imagined implementation structure.

## Avoid tests that cannot disagree with the code

Watch for:

- implementation-coupled tests that break on harmless refactors;
- tautological assertions that compute the expected result the same way as the implementation;
- mocks of internal collaborators that bypass the real behavior under test;
- broad snapshots or fixture construction that obscure the behavioral claim;
- test seams too shallow to reproduce the actual bug or requirement.

Stop using the TDD loop when another validation technique is a better fit for the remaining work. The objective is reliable behavior, not completion of a ritual.
