# Constraints
## Continuous Constraints
### ContinuousCardinalityConstraint

The `ContinuousCardinalityConstraint` gives you a
tool to control the number of active factors (i.e. parameters that take a non-zero
value) in your designs. This comes handy, for example, when designing mixtures with a
limited number of components.

To create a constraint of this kind, simply specify the set of parameters on which the
constraint is to be imposed, together with the corresponding upper and lower cardinality
limits. For instance, the following constraint would ensure that there is always a
minimum of one and a maximum of two components in each parameter configuration:

```python
from baybe.constraints import ContinuousCardinalityConstraint

ContinuousCardinalityConstraint(
    parameters=["x_1", "x_2", "x_3"],
    min_cardinality=1,  # defaults to 0
    max_cardinality=2,  # defaults to the number of affected parameters (here: 3)
    relative_threshold=0.001,  # optional, defines the range of values considered active
)
```