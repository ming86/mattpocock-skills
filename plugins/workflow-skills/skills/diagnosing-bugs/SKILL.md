---
name: diagnosing-bugs
description: "Diagnose bugs, regressions, intermittent failures, or performance problems whose cause is not known. Use when straightforward inspection is not enough and evidence is needed to distinguish competing explanations; use the smallest useful diagnostic loop and fix the cause only when fixing it is part of the requested work."
---

# Diagnosing Bugs

Use evidence to narrow bugs that straightforward inspection cannot resolve reliably. Match the depth of the investigation to the uncertainty and consequences instead of forcing every case through the same sequence at the same depth.

When exploring the codebase, use `CONTEXT.md`, ADRs, tests, logs, history, and nearby implementation as evidence when they are relevant.

## Protect sensitive evidence

Redact secrets before showing commands, output, traces, headers, screenshots, or captured artifacts. Prefer credentials in environment variables or established secret stores rather than copying them into debugging artifacts.

If useful evidence cannot be obtained safely or with the available access, say what is missing and why it matters.

## 1. Establish a useful signal

Prefer a feedback loop that can distinguish the reported bug from nearby failures. The cheapest credible signal may be:

- an existing or new focused test;
- a CLI or HTTP reproduction;
- a headless-browser scenario;
- a replayed trace or fixture;
- a small throwaway harness;
- a differential comparison between known-good and failing states;
- a profiler, timing harness, query plan, or other measurement for performance regressions;
- a bisection harness when the regression is bounded by known revisions.

For intermittent failures, improve the reproduction rate or collect enough repeated evidence to compare hypotheses. Do not spend disproportionate effort making a perfect harness when a slower or noisier signal is already sufficient to distinguish the cause reliably.

If a reliable automated loop is not practical, use the best available evidence and state the reduced confidence. Ask for environment access, a redacted artifact, or permission for temporary instrumentation only when it is materially needed.

## 2. Reproduce and narrow when useful

Confirm that the signal matches the user's reported symptom rather than a different failure. Reduce inputs, callers, configuration, timing, or data when doing so materially shrinks the hypothesis space or produces a valuable regression case.

A minimal reproduction is useful evidence, not a gate. Do not block diagnosis on minimization when the existing reproduction is already precise enough to test causes.

## 3. Form testable hypotheses

When the cause is not already established by direct evidence, form multiple plausible hypotheses and rank them by the evidence available. Each hypothesis should predict an observation that would make it more or less likely.

Share the hypotheses when user knowledge or judgment could materially change the ranking. Do not create a user round-trip merely because this skill has reached a hypothesis step.

## 4. Test the differences that best separate the hypotheses

Choose probes that distinguish competing explanations with the least disruption. Prefer direct inspection, a debugger, a narrow log or trace, a controlled input/configuration change, or a focused comparison over broad instrumentation.

Change one important variable at a time when you need to know which change caused the result. Tag temporary instrumentation so it can be found and removed reliably.

For performance regressions, measure before changing code. Use the metric or profiler that can establish whether the suspected cause actually explains the regression.

## 5. Act on the established cause within the requested work

Once the evidence supports a cause, distinguish diagnosis from fixing the system. If fixing the bug is part of the requested work, implement the smallest coherent correction within scope. If the task asks only for diagnosis, report the cause, supporting evidence, confidence or remaining uncertainty, and the smallest credible correction without modifying the implementation.

If the evidence invalidates a material requirement, architecture assumption, interface, or operational direction, treat that as a change in the problem definition rather than folding a redesign into the bug fix. Report the mismatch and its consequence clearly.

When fixing the bug is part of the requested work, add or retain a regression test when there is a correct observable seam and the test materially protects the behavior. A shallow or artificial test that cannot reproduce the real failure is not useful merely because a regression test seems customary.

## 6. Verify and clean up

Before considering the task complete, establish the evidence appropriate to its scope:

- the root cause is established to the degree the available evidence permits;
- when the bug was fixed, the original symptom no longer reproduces or the measured regression is corrected;
- when the bug was fixed, the focused regression signal passes when one exists;
- temporary debug instrumentation and disposable artifacts are removed or intentionally retained in an established location;
- unresolved uncertainty or validation limits are reported clearly.

For a substantial or multi-session investigation, preserve the current diagnostic state when repeating the work would be costly: confirmed observations, active or eliminated hypotheses, the root cause when known, evidence pointers, and remaining leads. Reuse the work's existing durable location or follow the project's durable-state convention. Use local working state when the investigation is provisional or too detailed for shared project documentation. If no convention exists, keep the diagnostic state in the simplest work-centered location that fits the investigation. Keep this state current rather than appending a chronological debugging transcript.

Preserve or share the root cause and supporting evidence when future work would materially benefit, using the project's normal durable-state conventions and updating the current work artifact when appropriate.
