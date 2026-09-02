---
name: simplify-by-ablation
description: "Simplify designs and implementations by testing which complexity materially contributes to the current solution. Use when asked to do an ablation pass, simplify overengineered work, remove unnecessary abstractions or design complexity, or determine whether layers, mechanisms, guards, supporting work, or other complexity earn their place."
---

# Simplify by Ablation

Evaluate questionable complexity by asking what would materially change if it were removed or simplified.

For an abstraction, layer, mechanism, guard, supporting artifact, or design commitment whose contribution is unclear, ask what concrete current requirement, behavior, constraint, or demonstrated benefit would be lost without it.

Prefer the simpler form when removing or simplifying something causes no material loss. Do not treat fewer components or less code as inherently better: keep complexity when its removal would lose required behavior, useful structure, a real boundary, necessary control, or another demonstrated benefit.

Judge contribution in the context of the whole solution. A component can be locally reasonable yet add more complexity, coupling, or ongoing obligation than the value it provides.

Do not use hypothetical future requirements to justify existing complexity unless there is a concrete current reason that flexibility matters. Apply the same reasoning to supporting machinery such as tests, validation, compatibility mechanisms, configurability, infrastructure, or process when their contribution is in question. Judge supporting work by the concrete function it is meant to serve; lack of an immediate runtime change alone does not show that it is unnecessary.

Follow the result rather than trying to remove something from every solution. An ablation pass may conclude that the existing complexity is justified.
