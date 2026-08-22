# When to Mock

Prefer the most realistic collaborator that still gives a focused and reliable test at reasonable cost. Mocks and fakes are tools for controlling dependencies; system boundaries are common places to use them, not the only valid places.

Common candidates include:

- External APIs such as payment or email providers
- Databases when a real or lightweight test database is disproportionately expensive
- Time, randomness, network failures, and other nondeterministic inputs
- File systems or operating-system interactions when a real substitute is impractical
- Narrow internal collaborators when controlling them meaningfully improves failure reproduction, speed, determinism, or coverage without making the test mainly assert implementation wiring

Be cautious about mocking your own classes, modules, or internal collaborators when doing so makes tests mirror the current call graph. Prefer real collaborators or a higher-level observable interface when that remains cheap and gives a more credible behavioral signal.

## Designing for controllable dependencies

When a dependency genuinely needs substitution, make the replacement point easy to control without exposing unnecessary implementation detail.

**1. Accept dependencies when substitution is useful**

Pass dependencies in rather than constructing them deep inside behavior that needs controlled testing:

```typescript
// Easy to substitute when needed
function processPayment(order, paymentClient) {
  return paymentClient.charge(order.total);
}

// Harder to control in a focused test
function processPayment(order) {
  const client = new StripeClient(process.env.STRIPE_KEY);
  return client.charge(order.total);
}
```

Do not add dependency injection mechanically when the dependency is stable, local, cheap, and already easy to exercise through the repository's normal tests.

**2. Prefer meaningful contracts over generic test hooks**

Specific operations often produce clearer contracts than one generic conditional mock:

```typescript
const api = {
  getUser: (id) => fetch(`/users/${id}`),
  getOrders: (userId) => fetch(`/users/${userId}/orders`),
  createOrder: (data) => fetch('/orders', { method: 'POST', body: data }),
};
```

Compared with a generic fetch wrapper, this can make test setup clearer and improve type safety. Preserve the repository's existing abstraction when it already communicates the contract well; do not create an SDK-style layer solely for mocking convenience.
