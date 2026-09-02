---
name: simplify-by-ablation
description: "Simplify designs and implementations by testing which complexity materially contributes to the current solution. Use when asked to do an ablation pass, simplify overengineered work, remove unnecessary abstractions or design complexity, determine whether layers, mechanisms, guards, supporting work, or other complexity earn their place, or isolate which optimizations materially contribute to a result."
---

# Simplify by Ablation

Evaluate questionable complexity by testing what materially changes if it is removed or simplified.

When the contribution can be checked cheaply and directly, prefer a targeted ablation: remove or simplify one candidate and observe whether the relevant behavior, property, or metric materially changes. Otherwise, reason through the same counterfactual without manufacturing an experiment.

For an abstraction, layer, mechanism, guard, supporting artifact, or design commitment whose contribution is unclear, ask what concrete current requirement, behavior, constraint, or demonstrated benefit would be lost without it.

Prefer the simpler form when removing or simplifying something causes no material loss. Do not treat fewer components or less code as inherently better: keep complexity when its removal would lose required behavior, useful structure, a real boundary, necessary control, or another demonstrated benefit.

Judge contribution in the context of the whole solution. A component can be locally reasonable yet add more complexity, coupling, or ongoing obligation than the value it provides.

For defensive machinery, judge its contribution against the realistic frequency and consequence of the failure it addresses, how easily the failure can be detected or repaired, and the ongoing complexity of automatic prevention or recovery. Theoretical possibility alone does not establish that permanent defensive machinery is worthwhile.

Do not use hypothetical future requirements to justify existing complexity unless there is a concrete current reason that flexibility matters. Apply the same reasoning to supporting machinery such as tests, validation, compatibility mechanisms, configurability, infrastructure, or process when their contribution is in question. Judge supporting work by the concrete function it is meant to serve; lack of an immediate runtime change alone does not show that it is unnecessary.

Follow the result rather than trying to remove something from every solution. An ablation pass may conclude that the existing complexity is justified.
