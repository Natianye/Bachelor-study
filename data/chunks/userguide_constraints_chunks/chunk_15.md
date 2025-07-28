# Constraints
## Discrete Constraints
### DiscreteCardinalityConstraint

Like its [continuous cousin](), the
`DiscreteCardinalityConstraint` lets you control the
number of active parameters in your design. The construction works analogously:

```python
from baybe.constraints import DiscreteCardinalityConstraint

DiscreteCardinalityConstraint(
    parameters=["Fraction_1", "Fraction_2", "Fraction_3"],
    min_cardinality=1,  # defaults to 0
    max_cardinality=2,  # defaults to the number of affected parameters (here: 3)
)
```