---
name: diagnosing-bugs
description: "Diagnose bugs, regressions, intermittent failures, or performance problems whose cause is not known. Use when straightforward inspection is not enough and evidence is needed to distinguish competing explanations; use the smallest useful diagnostic loop and fix the cause only when fixing it is part of the requested work."
---

# Diagnosing Bugs

Use evidence to narrow bugs that straightforward inspection cannot resolve reliably. Match the depth of the investigation to the uncertainty and consequences instead of forcing every case through the same sequence at the same depth.

When exploring the codebase, use `CONTEXT.md`, ADRs, tests, logs, history, and nearby implementation as evidence when they are relevant.

## Protect sensitive debugging data

Redact secrets before showing commands, output, traces, headers, screenshots, or captured files. Prefer credentials in environment variables or existing secret stores rather than copying them into debugging files.

If useful evidence cannot be obtained safely or with the available access, say what is missing and why it matters.

## 1. Find a useful signal

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

If a reliable automated loop is not practical, use the best available evidence and state the reduced confidence. Ask for environment access, a redacted diagnostic file or output, or permission for temporary instrumentation only when it is genuinely needed.

## 2. Reproduce and narrow when useful

Confirm that the signal matches the user's reported symptom rather than a different failure. Reduce inputs, callers, configuration, timing, or data when doing so meaningfully shrinks the hypothesis space or produces a valuable regression case.

A minimal reproduction is useful evidence, not a gate. Do not block diagnosis on minimization when the existing reproduction is already precise enough to test causes.

## 3. Form testable hypotheses

When direct observations do not already make the cause clear, form multiple plausible hypotheses and rank them by the evidence available. Each hypothesis should predict an observation that would make it more or less likely.

Share the hypotheses when user knowledge or judgment could change the ranking. Do not create a user round-trip merely because this skill has reached a hypothesis step.

## 4. Test the differences that best separate the hypotheses

Choose probes that distinguish competing explanations with the least disruption. Prefer direct inspection, a debugger, a narrow log or trace, a controlled input/configuration change, or a focused comparison over broad instrumentation.

Change one important variable at a time when you need to know which change caused the result. Tag temporary instrumentation so it can be found and removed reliably.

For performance regressions, capture a before-change signal that can show whether the suspected cause actually explains the regression. Reuse an existing metric, profiler, or representative workflow when it is sufficient; add measurement machinery only when the current signal cannot answer the question.

## 5. Act once the cause is clear enough within the requested work

Once the evidence supports a cause, distinguish diagnosis from fixing the system. If fixing the bug is part of the requested work, implement the smallest coherent correction within scope. If the task asks only for diagnosis, report the cause, supporting evidence, confidence or remaining uncertainty, and the smallest credible correction without modifying the implementation.

If the findings show that an important requirement, architecture assumption, interface, or operational direction is wrong, treat that as a change in the problem definition rather than folding a redesign into the bug fix. Report the mismatch and its consequence clearly.

When fixing the bug is part of the requested work, preserve a regression check when it captures the real failure through a useful observable path and remains a maintainable signal. That check may be an existing workflow, test, reproduction, or measurement; choose the form that best represents the failure rather than creating a test by default.

## 6. Confirm the result and clean up

Before considering the task complete, confirm the result at the scope of the reported problem:

- the available observations support the root cause strongly enough for the task;
- when the bug was fixed, the original symptom no longer reproduces or the measured regression is corrected;
- when the bug was fixed, the focused regression signal passes when one exists;
- temporary debug instrumentation and disposable debug files are removed or intentionally retained in an existing location;
- unresolved uncertainty or validation limits are reported clearly.

For a substantial or multi-session investigation, preserve the current diagnostic state when repeating the work would be costly: confirmed observations, active or eliminated hypotheses, the root cause when known, evidence pointers, and remaining leads. Reuse the work's existing location or follow how the project normally saves ongoing diagnostic work. Use local working state when the investigation is provisional or too detailed for shared project documentation. If no convention exists, keep the diagnostic state in the simplest work-centered location that fits the investigation. Keep this state current rather than appending a chronological debugging transcript.

Preserve or share the root cause and supporting evidence when future work is likely to need them, using the project's normal way of saving ongoing work and updating the current work state when appropriate.
