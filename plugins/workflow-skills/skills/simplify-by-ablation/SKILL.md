---
name: simplify-by-ablation
description: "Simplify designs and implementations by asking what materially changes when questionable complexity is removed or simplified. Use when asked to do an ablation pass, simplify overengineered work, remove unnecessary abstractions or design complexity, assess whether layers, mechanisms, guards, supporting work, or other complexity earn their place, or isolate which optimizations materially contribute."
---

# Simplify by Ablation

Evaluate questionable complexity by asking what materially changes if it is removed or simplified.

When the effect can be checked cheaply and directly, prefer a targeted ablation: remove or simplify one candidate and see what, if anything, materially changes. Otherwise, reason through the same counterfactual without manufacturing an experiment.

For an abstraction, layer, mechanism, guard, supporting work, or design commitment whose contribution is unclear, ask what concrete current requirement, behavior, constraint, or useful property would be lost without it.

Prefer the simpler form when removing or simplifying something causes no material loss. Do not treat fewer components or less code as inherently better: keep complexity when its removal would lose required behavior, useful structure, a real boundary, necessary control, or another material benefit.

Judge contribution in the context of the whole solution. A component can make sense locally yet add more complexity, coupling, or ongoing obligation than its role justifies.

For defensive machinery, judge its contribution against the realistic frequency and consequence of the failure it addresses, how easily the failure can be detected or repaired, and the ongoing complexity of automatic prevention or recovery. Theoretical possibility alone does not establish that added defensive machinery is worthwhile.

Do not use hypothetical future requirements to justify existing complexity unless there is a concrete current reason that flexibility matters. Apply the same reasoning to supporting machinery such as tests, validation, compatibility mechanisms, configurability, infrastructure, or process when their value is unclear. Judge supporting work by what it is meant to accomplish; the fact that removing it does not immediately change runtime behavior does not by itself make it unnecessary.

An ablation pass may justify keeping the existing complexity. Removal is not the goal.
