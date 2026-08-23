# Logic or State Prototype

Use this pattern when the uncertainty is about state transitions, business rules, data shape, or an interface that becomes easier to judge with concrete scenarios.

The goal is evidence about the behavior or model, not reusable production code.

## Choose the smallest useful harness

A self-contained HTML page can be useful when a non-developer needs to click through scenarios, but it is only one option. A scratch script, REPL harness, focused executable example, or temporary test route may be cheaper when the question does not need a visual interface.

State the question visibly enough that someone evaluating the prototype knows what evidence to look for.

## Keep the model observable

Represent the relevant state and actions directly. Make it easy to exercise the happy path and the awkward cases that motivated the prototype. If a UI shell is used, keep the domain logic separate enough that the experiment is easy to reason about. Do not treat that prototype structure as a production architecture decision unless the experiment specifically validates it.

Useful scenarios include:

- the normal path;
- a boundary or ordering case that is hard to reason about on paper;
- an action that should be rejected or produce a distinctive state.

## Capture the result

Stop when the scenarios answer the question. Record the evidence and resulting decision when later work depends on it.

Production implementation may reuse an idea or small piece of code when that is genuinely appropriate, but do not assume prototype code should be lifted into the real module. Keep or discard the harness according to whether it remains useful as evidence.
