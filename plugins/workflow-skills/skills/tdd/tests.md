# Good and Bad Tests

## Strong behavioral tests

Prefer tests that check behavior users or callers care about through a stable observable interface.

```typescript
// GOOD: Tests observable behavior
test("user can checkout with valid cart", async () => {
  const cart = createCart();
  cart.add(product);
  const result = await checkout(cart, paymentMethod);
  expect(result.status).toBe("confirmed");
});
```

Useful characteristics include:

- Tests behavior users or callers care about
- Uses a stable public or integration interface when that interface exposes the relevant behavior
- Survives harmless internal refactors
- Describes WHAT is protected more than HOW it happens
- Keeps each test focused on one clear behavioral claim; multiple assertions are fine when they jointly check that claim

Lower-level tests can still be appropriate when they protect an important invariant, algorithm, parser, performance property, failure mode, or other behavior that would be expensive or unclear to check only through a broader interface.

## Fragile implementation-detail tests

Tests become suspicious when they primarily encode incidental structure rather than the behavior that structure exists to provide.

```typescript
// FRAGILE: Tests current wiring rather than payment behavior
test("checkout calls paymentService.process", async () => {
  const mockPayment = jest.mock(paymentService);
  await checkout(cart, payment);
  expect(mockPayment.process).toHaveBeenCalledWith(cart.total);
});
```

Red flags include:

- Mocking internal collaborators merely to assert the current call graph
- Testing private methods without an important invariant that justifies the narrower test surface
- Asserting call counts/order when callers do not depend on that ordering
- Breaking on a harmless refactor with no corresponding behavior change
- Test names that describe incidental HOW rather than protected WHAT

Prefer checking through the normal interface when it credibly exposes the result:

```typescript
// GOOD: Checks through the normal interface
test("parseConfig preserves the declared output directory", () => {
  const config = parseConfig("output = ./dist");
  expect(config.outputDir).toBe("./dist");
});
```

Direct inspection of storage, events, logs, or another lower-level surface is not automatically wrong. Use it when that surface is itself the behavior being protected or when the normal interface cannot show the property without excessive setup. Make the reason clear so the test does not accidentally become an implementation-coupled substitute for a simpler behavioral check.

**Tautological tests**: Expected value restates the implementation, so the test passes by construction.

```typescript
// BAD: Expected value is recomputed the way the code computes it
test("calculateTotal sums line items", () => {
  const items = [{ price: 10 }, { price: 5 }];
  const expected = items.reduce((sum, i) => sum + i.price, 0);
  expect(calculateTotal(items)).toBe(expected);
});

// GOOD: Expected value is an independent, known literal
test("calculateTotal sums line items", () => {
  expect(calculateTotal([{ price: 10 }, { price: 5 }])).toBe(15);
});
```
