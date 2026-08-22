---
name: code-review
description: Review a bounded change along two independent axes: whether it matches the requested outcome and whether it is appropriate for the repository.
---

# Code Review

Review a bounded implementation without allowing technical polish to hide a goal mismatch, or requirement compliance to hide a poor repository integration.

Keep two questions separate:

- **Intent / Spec:** Did the change implement the requested behavior, requirements, constraints, and scope?
- **Repository / Implementation:** Is the change semantically correct and appropriate for this codebase, including its architecture, interfaces, conventions, and realistic integration behavior?

This skill is a focused implementation review. It does not replace broader independent criticism configured by the project. An independent reviewer such as `rubber-duck` may additionally examine whether the plan or implementation itself is sensible, proportionate, unnecessarily complex, based on bad assumptions, or drifting from the primary goal.

## 1. Establish the review boundary

Identify the exact change being reviewed: a diff against a commit, branch, tag, merge-base, PR, worktree state, or another explicit bounded surface. Verify that the boundary resolves and contains the intended changes before drawing conclusions.

If the user did not specify a fixed point but repository state makes the intended boundary clear, use it and state what was reviewed. Ask only when materially different boundaries remain plausible.

## 2. Identify the intent source

Use the strongest available source of requested behavior and scope, such as:

1. the originating spec or ticket;
2. an approved plan or requirements document;
3. the current user request and established decisions;
4. when no durable spec exists, the best available task context.

Preserve the actual status of assumptions and unresolved points. Do not invent requirements to make the review more exhaustive.

## 3. Identify repository evidence

Read the relevant repository instructions, ADRs, coding or contribution guidance, nearby implementation patterns, tests, types, and interfaces needed to judge this change.

Repository conventions are evidence, not an excuse to flag every stylistic difference. Skip findings already enforced mechanically unless the change demonstrates a substantive problem that the tooling does not capture.

## 4. Review the axes independently

When independent subagent contexts are available and proportionate to the change, use separate fresh contexts for the two axes so one conclusion does not anchor the other. Otherwise review them sequentially while keeping the evidence and findings distinct.

### Intent / Spec

Look for:

- requested behavior that is missing, partial, or incorrect;
- behavior or commitments added without support from the current scope;
- acceptance criteria that are not actually established by the implementation;
- tentative assumptions or prototype artifacts accidentally promoted into requirements;
- obsolete or superseded requirements preserved in the implementation.

For each finding, point to the relevant requirement or decision source when available.

### Repository / Implementation

Look for substantive issues in:

- semantic correctness and invariants;
- integration with surrounding modules and interfaces;
- regressions or realistic failure paths introduced by the change;
- architecture or dependency direction where the repository establishes a meaningful pattern;
- unnecessary complexity, indirection, duplication, or abstraction that materially harms the implementation;
- performance, security, compatibility, or robustness only where the actual system assumptions make the concern relevant;
- runtime or integration assumptions that inspection alone cannot establish and need targeted validation.

Do not manufacture generic best-practice findings, cosmetic refactors, hypothetical hardening, or speculative future needs.

## 5. Report without masking one axis with the other

Present findings under separate `Intent / Spec` and `Repository / Implementation` sections. For each substantive finding state:

- the issue;
- why it matters;
- severity or whether it blocks completion;
- the smallest credible correction or validation needed.

If an axis has no substantive findings, say so explicitly. Do not merge the axes into a single score or allow a pass on one to cancel a failure on the other.

Follow the governing project instructions for whether another independent review is required, who owns fixes, and what validation or checkpoint follows.