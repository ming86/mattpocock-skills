---
name: diagnosing-bugs
description: Diagnose hard bugs and performance regressions with the smallest credible evidence loop, then fix the established cause and preserve a useful regression signal.
---

# Diagnosing Bugs

Use an evidence-driven loop for bugs that are not resolved reliably by straightforward inspection. Scale the procedure to the uncertainty and consequences of the bug rather than forcing every case through the same number of phases.

When exploring the codebase, use `CONTEXT.md`, ADRs, tests, logs, history, and nearby implementation as evidence when they are relevant. Follow governing project instructions for user consultation, temporary instrumentation, commits, review, and production-impacting actions.

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

## 3. Form falsifiable hypotheses

When the cause is not already established by direct evidence, form multiple plausible hypotheses and rank them by the evidence available. Each hypothesis should predict an observation that would make it more or less likely.

Share the hypotheses with the user when their domain knowledge could materially change the ranking or when the governing consultation rules call for a checkpoint. Do not create a user round-trip merely because this skill has reached a hypothesis step.

## 4. Test the highest-value distinctions

Choose probes that distinguish competing explanations with the least disruption. Prefer direct inspection, a debugger, a narrow log or trace, a controlled input/configuration change, or a focused comparison over broad instrumentation.

Change one material variable at a time when causal attribution depends on it. Tag temporary instrumentation so it can be found and removed reliably.

For performance regressions, measure before changing code. Use the metric or profiler that can establish whether the suspected cause actually explains the regression.

## 5. Fix the established cause

Once the evidence supports a cause, implement the smallest coherent correction within scope. If the evidence instead invalidates a material requirement, architecture assumption, interface, or operational direction, surface that finding through the governing root-agent or user-consultation path rather than silently redesigning the system.

Add or retain a regression test when there is a correct observable seam and the test materially protects the behavior. A shallow or artificial test that cannot reproduce the real failure is not useful merely because a regression test seems customary.

## 6. Verify and clean up

Before considering the diagnosis complete, establish the evidence appropriate to the bug:

- the original symptom no longer reproduces, or the measured regression is corrected;
- the focused regression signal passes when one exists;
- temporary debug instrumentation and disposable artifacts are removed or intentionally retained in an established location;
- unresolved uncertainty or validation limits are reported clearly.

Preserve the root cause and important evidence in the project's normal durable artifact when later engineers would benefit from it. If the project uses a commit or pull-request explanation, include the cause there when appropriate, but this skill does not require or authorize a commit by itself.
