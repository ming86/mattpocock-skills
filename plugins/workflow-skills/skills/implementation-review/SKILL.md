---
name: implementation-review
description: "Review a bounded implementation against the requested outcome and the surrounding repository. Use only when explicitly asked to inspect a patch, pull request, or completed implementation for correctness, integration problems, regressions, unnecessary complexity, or missed requirements. This is not a broader critique of the underlying plan or approach."
disable-model-invocation: true
---

# Implementation Review

Review a bounded implementation without letting polished code hide a goal mismatch or a requirements checklist hide poor integration with the repository.

Keep two questions separate:

- **Intent / Spec:** Did the change implement the requested behavior, requirements, constraints, and scope?
- **Repository / Implementation:** Is the change correct and appropriate for this codebase, including its architecture, interfaces, conventions, and real integration behavior?

This is a focused implementation review, not a broader critique of the plan or approach. It assesses whether the bounded implementation matches its intended behavior and fits the repository; it does not answer whether the underlying plan or approach was the right one.

## 1. Identify the review boundary

Identify the exact change being reviewed: a diff against a commit, branch, tag, merge-base, PR, worktree state, or another explicit bounded surface. Confirm that the boundary resolves and contains the intended changes before drawing conclusions.

If the user did not specify a fixed point but the repository makes the intended boundary clear, use it and state what was reviewed. Ask only when meaningfully different boundaries remain plausible.

## 2. Identify the intent source

Identify the current requirements and decisions that define the requested behavior and scope. These may come from the current user request and current decisions, the originating spec or ticket, an agreed plan or requirements document, and other relevant task context. Account for later decisions or requirements that changed or replaced earlier ones.

Keep assumptions and unresolved points labeled as such. Do not invent requirements to make the review more exhaustive.

## 3. Read the relevant repository context

Read the relevant repository instructions, ADRs, coding or contribution guidance, nearby implementation patterns, tests, types, and interfaces needed to judge this change.

Repository conventions help judge whether the change fits the codebase; they are not a reason to flag every stylistic difference. Skip findings already enforced mechanically unless the change reveals an important problem that the tooling does not capture.

## 4. Review the axes independently

Keep the two axes independent in reasoning and reporting. Judge each against the sources and behavior relevant to that axis, and keep their findings distinct.

### Intent / Spec

Look for:

- requested behavior that is missing, partial, or incorrect;
- behavior or commitments added without support from the current scope;
- acceptance criteria that the implementation does not actually satisfy;
- tentative assumptions or incidental prototype details accidentally promoted into requirements;
- earlier requirements that were later changed or replaced but remain in the implementation.

For each finding, point to the relevant requirement or decision source when available.

### Repository / Implementation

Look for important issues in:

- correctness and important invariants;
- integration with surrounding modules and interfaces;
- regressions or realistic failure paths introduced by the change;
- architecture or dependency direction where the repository consistently uses a meaningful pattern;
- unnecessary complexity, indirection, duplication, or abstraction that meaningfully harms the implementation;
- when the contribution of complexity introduced by the reviewed change is unclear, use `simplify-by-ablation` to test what would actually be lost by removing or simplifying it, while staying within the current implementation and design boundary;
- performance, security, compatibility, or robustness only where the actual system assumptions make the concern relevant;
- runtime or integration assumptions that inspection alone cannot answer and whose uncertainty matters to the requested outcome;
- tests or checks changed with the implementation that do not actually bear on the requested behavior, cannot fail for a relevant wrong result, or mainly encode the implementation that was just written.

Do not manufacture generic best-practice findings, cosmetic refactors, hypothetical hardening, or speculative future needs.

## 5. Report without masking one axis with the other

Present findings under separate `Intent / Spec` and `Repository / Implementation` sections. For each important finding state:

- the issue;
- why it matters;
- severity or whether it blocks completion;
- the smallest credible correction, and when the finding depends on an unobserved runtime or integration assumption, the specific targeted check that would resolve that uncertainty.

If an axis has no important findings, say so explicitly. Do not merge the axes into a single score or allow a pass on one to cancel a failure on the other.

Review findings can remain in the current response when they will be acted on immediately. Save them only when they become follow-up work that later contexts need or otherwise change the effort's current state; reuse that work location rather than creating a separate review log.
