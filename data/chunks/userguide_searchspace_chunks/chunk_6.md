# Search Spaces
## Discrete Subspaces
### Representation of Data within Discrete Subspaces

Internally, discrete subspaces are represented by two dataframes, the *experimental* and the *computational* representation.

The experimental representation (`exp_rep`) contains all parameters as they were provided upon the construction of the search space and viewed by the experimenter. The computational representation (`comp_rep`) contains a representation of parameters that is actually used for the internal calculation.

In particular, the computational representation contains no more labels or constant columns. This happens e.g. for [`SubstanceParameter`]() or [`CategoricalParameter`](). Further, note that the shape of the computational representation can also change depending on the chosen encoding.

The following example demonstrates the difference:

```python
from baybe.parameters import NumericalDiscreteParameter, CategoricalParameter

speed = CategoricalParameter("Speed", values=["slow", "normal", "fast"], encoding="OHE")
temperature = NumericalDiscreteParameter(name="Temperature", values=[90, 105])

subspace = SubspaceDiscrete.from_product(parameters=[speed, temperature])
```

```default
  Experimental Representation
      Speed  Temperature
  0    slow         90.0
  1    slow        105.0
  2  normal         90.0
  3  normal        105.0
  4    fast         90.0
  5    fast        105.0

  Computational Representation
     Speed_slow  Speed_normal  Speed_fast  Temperature
  0           1             0           0         90.0
  1           1             0           0        105.0
  2           0             1           0         90.0
  3           0             1           0        105.0
  4           0             0           1         90.0
  5           0             0           1        105.0
```