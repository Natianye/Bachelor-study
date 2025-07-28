# Search Spaces
## Discrete Subspaces
The `SubspaceDiscrete` contains all the discrete parameters of a `SearchSpace`. There are different ways of constructing this subspace.

### Building from the Product of Parameter Values

The method [`SearchSpace.from_product`]() constructs the full cartesian product of the provided parameters:

```python
from baybe.parameters import NumericalDiscreteParameter, CategoricalParameter
from baybe.searchspace import SubspaceDiscrete

parameters = [
    NumericalDiscreteParameter(name="x0", values=[1, 2, 3]),
    NumericalDiscreteParameter(name="x1", values=[4, 5, 6]),
    CategoricalParameter(name="Speed", values=["slow", "normal", "fast"]),
]
subspace = SubspaceDiscrete.from_product(parameters=parameters)
```

In this example, `subspace` has a total of 27 different parameter configuration.

```default
      x0   x1   Speed
 0   1.0  4.0    slow
 1   1.0  4.0  normal
 2   1.0  4.0    fast
 ..  ...  ...     ...
 24  3.0  6.0    slow
 25  3.0  6.0  normal
 26  3.0  6.0    fast

  [27 rows x 3 columns]
```