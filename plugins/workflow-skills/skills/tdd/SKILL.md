---
name: tdd
description: "Apply a focused red-green-refactor loop when test-first development is explicitly requested or project instructions call for it in the current work. Use the method to shape and protect behavior within that chosen workflow rather than treating TDD as the default companion to code changes."
---

# Test-Driven Development

TDD is a technique for discovering and protecting behavior through a short test-first loop. Use it when the user has requested test-first development or project instructions call for it in the current work. Within that chosen workflow, keep the loop focused on behavior the work actually needs to deliver.

When exploring the codebase, use the project's domain language and existing test conventions.

## What a useful test is

Tests should check behavior through an observable interface rather than mirror implementation details. A good test can fail when the required behavior is wrong and remain valid when internals are refactored without changing that behavior.

See [tests.md](tests.md) for examples and [mocking.md](mocking.md) for mocking guidance.

## Choose what the test should observe

Prefer an existing public, integration, or other stable interface that exposes the real behavior being changed. In testing literature this kind of replaceable or observable point is sometimes called a **seam**; use the repository's normal term when it is clearer.

Choose the test surface from the spec, ticket, repository architecture, existing tests, and call sites. If different choices would change architecture, scope, or what the test can tell you, treat the test surface as a design decision rather than choosing it solely for testing convenience.

When the interface itself is the design question, use `codebase-design` for design guidance.

## The loop

1. **Red.** Write one focused test that expresses the next behavior or regression case. Run it and confirm that it fails for the expected reason.
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
- test surfaces too narrow to reproduce the actual bug or requirement.

Stop using the TDD loop when another way of checking the remaining work is a better fit. The objective is reliable behavior, not completion of a ritual.
