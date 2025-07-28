# Constraints
## Continuous Constraints

#### WARNING
Not all surrogate models are able to treat continuous constraints. In such situations
the constraints are currently silently ignored.

### ContinuousLinearConstraint

The [`ContinuousLinearConstraint`]()
asserts that the following kind of equations are true (up to numerical rounding errors):

$$

\sum_{i} x_i \cdot c_i = \text{rhs} \\
\sum_{i} x_i \cdot c_i >= \text{rhs} \\
\sum_{i} x_i \cdot c_i <= \text{rhs}
$$

where $x_i$ is the value of the $i$’th parameter affected by the constraint,
$c_i$ is the coefficient for that parameter, and $\text{rhs}$ is a user-chosen number.
The (in)equality type is defined by the `operator` keyword.

As an example, let’s assume we have three parameters named `x_1`, `x_2` and
`x_3`, which describe the relative concentrations in a mixture campaign.
The constraint assuring that they always sum up to 1.0 would look like this:

```python
from baybe.constraints import ContinuousLinearConstraint

ContinuousLinearConstraint(
    parameters=["x_1", "x_2", "x_3"],  # these parameters must exist in the search space
    operator="=",
    coefficients=[1.0, 1.0, 1.0],
    rhs=1.0,
)
```

Let us amend the example from above and assume that there is always a fourth component
to the mixture that serves as a “filler”. In such a case, we might want to ensure that
the first three components only make up to 80% of the mixture.
The following constraint would achieve this:

```python
from baybe.constraints import ContinuousLinearConstraint

ContinuousLinearConstraint(
    parameters=["x_1", "x_2", "x_3"],
    operator="<=",
    coefficients=[1.0, 1.0, 1.0],
    rhs=0.8,
)
```

A more detailed example can be found
[here]().