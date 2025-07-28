# Search Spaces
## Continuous Subspaces

The `SubspaceContinuous` contains all the continuous parameters of a `SearchSpace`. There are different ways of constructing this subspace.

### Using Explicit Bounds

The [`SubspaceContinuous.from_bounds`]() method can be used to easily create a subspace representing a hyperrectangle.

```python
from baybe.searchspace import SubspaceContinuous

bounds = pd.DataFrame({"param1": [0, 1], "param2": [-1, 1]})
subspace = continuous = SubspaceContinuous.from_bounds(bounds)
```

```default
 Continuous Parameters
      Name                          Type  Lower_Bound  Upper_Bound
 0  param1  NumericalContinuousParameter          0.0          1.0
 1  param2  NumericalContinuousParameter         -1.0          1.0
```