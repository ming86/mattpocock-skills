---
name: visual-explanation
description: Make a mechanism, architecture, runtime flow, state relationship, code structure, or change easier to understand with a visual or text-visual representation. Use when the user asks to show, visualize, diagram, sketch, illustrate, or give a picture or ELI5-style explainer. Choose a form the current interface can display conveniently; prefer terminal-native representations in CLI coding environments.
---

# Visual Explanation

Make the important mechanism, structure, relationship, or change easier to see.

Choose the smallest representation that makes the key point clear to the intended reader. Visualization does not require graphics: spacing, indentation, arrows, trees, diffs, and compact tables can carry structure directly in text.

## Match the representation to the subject

Use the form that naturally exposes what matters:

- logic or an algorithm: pseudocode or a compact state sketch;
- runtime calls or control flow: an indented call tree or sequence sketch;
- file, module, component, or ownership structure: a shallow tree;
- a before-and-after structural change: a focused diff;
- data or state movement: arrows, a small flow diagram, or a sequence diagram;
- a compact comparison: a table when rows and columns make the relationship clearer;
- a dense spatial, interactive, or presentation-oriented concept: a richer diagram or artifact when simpler forms would hide the point.

Use several forms only when each reveals a different part of the explanation. Do not turn a simple question into a diagram collection.

## Fit the current interface

Prefer a representation the user can see directly where the conversation is happening.

In CLI coding agents and terminal-oriented VS Code workflows, prefer text-native forms such as trees, arrows, pseudocode, diffs, and tables. They remain visible in the transcript, copy cleanly, and do not require another viewer.

Use Mermaid or another rendered-markup format when the current surface renders it conveniently and the structure benefits from it. Raw diagram source is not an improvement when a clear text sketch would be easier to read.

Use HTML, images, or other external artifacts when the user asks for them or when richer rendering materially improves the explanation and the environment can display the result without adding unnecessary friction. If that viewing path is inconvenient or unavailable, use the best text-native representation instead.

## Match the explanation to the reader

Adjust prerequisite knowledge independently from the rendering medium.

For an ELI5 or beginner explanation, assume little prior knowledge, use concrete labels and a small number of visible steps, and introduce terminology only when it helps the mechanism make sense. Keep the explanation simple without making it childish or replacing the real mechanism with a misleading analogy.

For an experienced reader, preserve the technical distinctions that matter and remove explanatory scaffolding they do not need.

## Keep the visual focused

Show only the calls, files, states, components, relationships, or changes needed for the current point. Keep supporting prose close to the representation and brief enough that the visual structure remains the main aid to understanding.
