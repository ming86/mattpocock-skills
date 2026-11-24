---
name: decide-under-uncertainty
description: Structure high-stakes or ambiguous decisions under incomplete information across engineering, career, strategy, or personal choices. Use when weighing competing options, evaluating tradeoffs, assessing irreversibility or tail risk, checking second-order effects, or deciding whether to act now, stage commitment, or gather more information first.
---

# Decide Under Uncertainty

Reach a defensible action under incomplete information without falling into analysis paralysis, false precision, or flat pros-and-cons lists.

## Match depth to reversibility

- **Reversible, low-cost choices (two-way doors):** Set a simple guardrail, pick the leading option, and learn from real feedback rather than over-analyzing.
- **Irreversible or high-downside choices (one-way doors):** Run the full sequence below before committing.

## Process

1. **Frame the real option set.** State the goal and time horizon. Always include the baseline (**status quo / do nothing**) and, where useful, a **staged or information-buying option** alongside the named alternatives. Ignore sunk costs; compare only marginal future costs, switching friction, and opportunity cost.
2. **Screen hard constraints and tail risk first.** Separate non-negotiable gates (safety, legal/compliance, ruinous downside, hard deadlines) from tradable objectives. Eliminate options that violate hard constraints or are dominated across every dimension. Do not use arbitrary 1-5 weighted scoring matrices that average away a fatal flaw.
3. **Compare marginal tradeoffs and second-order effects.** Compare surviving options in concrete units (time, money, latency, maintenance load, optionality) rather than vague labels. Trace the likely second-order consequences - how the system, team, incentives, or your future constraints will react after the first move.
4. **Separate inherent noise from decision-relevant unknowns.**
   - For irreducible variability (aleatory noise), build margin or fallback buffers.
   - For knowledge gaps (epistemic uncertainty), check **Value of Information (VoI)**: gather more data or run a small test only when different outcomes would actually change the chosen action and the test costs less than the mistake it prevents.
   - When estimates are disputed, identify the **switching value** (the threshold at which the winning option flips) instead of arguing over point probabilities.
5. **Stress-test the leading choice and design optionality.** State the single load-bearing assumption that would break the recommended choice (`Fails if ...`) and the cheapest way to check it. For high-uncertainty, high-cost moves, prefer staged commitments with explicit **trigger and exit criteria** that preserve reversibility.

## Output

Keep the answer proportional to the stakes:

- **Recommendation or next move** (act now, stage commitment, or run one targeted check first)
- **Decisive tradeoffs & second-order effects** across surviving options only
- **Key switching threshold & `Fails if` condition** (plus exit/rollback trigger when relevant)

Evaluate decision quality by the information and constraints available now, keeping facts, estimates, and value judgments distinct.
