# Constraints
## Discrete Constraints
### DiscreteSumConstraint and DiscreteProductConstraint

[`DiscreteSumConstraint`]()
and [`DiscreteProductConstraint`]()
impose conditions on sums or products of numerical parameters.
[In the first example from `ContinuousLinearConstraint`](#clc), we
had three continuous parameters `x_1`, `x_2` and `x_3`, which needed to sum
up to 1.0.
If these parameters were instead discrete, the corresponding constraint would look like:

```python
from baybe.constraints import DiscreteSumConstraint, ThresholdCondition

DiscreteSumConstraint(
    parameters=["x_1", "x_2", "x_3"],
    condition=ThresholdCondition(  # set condition that should apply to the sum
        threshold=1.0,
        operator="=",
        tolerance=0.001,  # optional; here, everything between 0.999 and 1.001 would also be considered valid
    ),
)
```

An end to end example can be found [here]().