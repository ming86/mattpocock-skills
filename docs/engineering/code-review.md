## What it does

`code-review` reviews a bounded implementation along two independent axes:

- **Intent / Spec:** did the change implement the requested behavior, requirements, constraints, and scope?
- **Repository / Implementation:** is the change semantically correct and appropriate for this codebase and its actual integration environment?

Keeping the axes separate prevents technical polish from hiding a goal mismatch and prevents requirement compliance from hiding a poor implementation.

## When to reach for it

Type `/code-review`, or let the agent use it when a bounded change needs focused conformance review.

First establish an explicit review boundary such as a diff, commit range, branch, PR, or worktree state. Then use the strongest available source of intended behavior and the repository evidence needed to judge implementation quality.

## Independent evidence

The two axes stay independent in reasoning and reporting. If the governing orchestration policy chooses separate reviewers or fresh contexts, each reviewer can receive one axis; otherwise one reviewer can evaluate them sequentially. The skill itself does not decide whether to spawn reviewers.

The skill looks for substantive issues, not generic best-practice findings, cosmetic refactors, hypothetical hardening, or speculative future needs.

## Common questions

**Is this the same as an independent critic such as `rubber-duck`?**

No. This skill asks whether the bounded implementation matches its intent and fits the repository. A broader critic can separately ask whether the chosen plan or implementation is sensible, proportionate, unnecessarily complex, or based on a bad assumption.

**Does a pass on one axis cancel a failure on the other?**

No. The findings remain separate. Correct code that solves the wrong problem still fails Intent / Spec review.

## It's working if

- Every finding can be tied to the requested outcome or concrete repository evidence.
- The review boundary is explicit.
- The two axes remain distinguishable in the report.
- Cosmetic or hypothetical concerns do not drown out substantive defects.

## Where it fits

Use it after [`implement`](../../skills/engineering/implement/SKILL.md) when focused conformance review is useful. Governing project instructions decide whether additional independent review or runtime validation is required.