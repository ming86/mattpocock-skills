# UI Prototype

Use this pattern when the uncertainty is visual or interaction design and concrete alternatives will answer it better than more verbal discussion.

## Keep the variants in realistic context

When practical, render alternatives inside the real page or surrounding application shell so density, navigation, data, and existing components constrain the design. Use a separate throwaway route only when there is no useful existing host.

Generate enough alternatives to expose meaningful tradeoffs. Two or three structurally different variants are often more useful than many cosmetic variations. The alternatives should disagree about layout, information hierarchy, or primary interaction rather than only color or copy.

A URL parameter or small temporary switcher can make comparison easy when the framework supports it. Keep prototype plumbing isolated and easy to remove.

## Use realistic data only when it matters

Reuse existing read paths or representative fixtures when they meaningfully affect the design question. Avoid wiring prototype variants to production mutations unless the interaction itself is what needs validation.

## Capture the result and remove prototype machinery

Stop once the comparison resolves the design question well enough for the next phase. Record the chosen direction and the evidence or feedback that mattered.

The production implementation should follow that validated direction under normal project constraints. Remove losing variants, temporary switchers, and prototype-only routes from the production path. Keep the prototype itself only when it remains useful as evidence.
