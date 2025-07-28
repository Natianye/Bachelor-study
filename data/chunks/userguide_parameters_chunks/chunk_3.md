# Parameters

Parameters are fundamental for BayBE, as they configure the [`SearchSpace`]() and serve
as the direct link to the controllable variables in your experiment.
Before starting an iterative campaign, the user is required to specify the exact
parameters they can control and want to consider in their optimization.

BayBE distinguishes two parameter types, because they need to be treated very
differently under the hood: Discrete and continuous parameters.

## Continuous Parameters
### NumericalContinuousParameter

This is currently the only continuous parameter type BayBE supports.
It defines possible values from a numerical interval called
`bounds`, and thus has an infinite amount of possibilities.
Unless restrained by [`Constraint`]()s, BayBE will consider any possible parameter value
that lies within the chosen interval.

```python
from baybe.parameters import NumericalContinuousParameter

NumericalContinuousParameter(
    name="Temperature",
    bounds=(0, 100),
)
```