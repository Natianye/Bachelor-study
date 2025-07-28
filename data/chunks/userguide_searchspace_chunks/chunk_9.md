# Search Spaces
## Continuous Subspaces
### Constructing from a Dataframe

Similar to discrete subspaces, continuous spaces can also be constructed using [`SubspaceContinuous.from_dataframe`]().
However, when using this method to create a continuous space, it will create the smallest axis-aligned hyperrectangle-shaped continuous subspace that contains the points specified in the given dataframe.

```python
from baybe.parameters import NumericalContinuousParameter
from baybe.searchspace.continuous import SubspaceContinuous

points = pd.DataFrame(
    {
        "param1": [0, 1, 2],
        "param2": [-1, 0, 1],
    }
)
subspace = SubspaceContinuous.from_dataframe(df=points)
```

As for discrete subspaces, this method automatically infers the parameter types but can be provided with an optional list `parameters`.

```default
 Continuous Parameters
      Name                          Type  Lower_Bound  Upper_Bound
 0  param1  NumericalContinuousParameter          0.0          2.0
 1  param2  NumericalContinuousParameter         -1.0          1.0
```