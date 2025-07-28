# Simulation
## The Lookup Mechanism
### Using a Dataframe

When dealing with discrete search spaces, it is also possible to provide the lookup values in a tabular representation using a dataframe.
To be a valid lookup, the dataframe must have columns corresponding to all parameters and targets in the modeled domain.

An example might look as follows:

```python
import pandas as pd

from baybe.parameters import NumericalDiscreteParameter
from baybe.searchspace import SearchSpace
from baybe.targets import NumericalTarget

searchspace = SearchSpace.from_product(
    [
        NumericalDiscreteParameter("p1", [0, 1, 2, 3]),
        NumericalDiscreteParameter("p2", [1, 10, 100, 1000]),
    ]
)
objective = NumericalTarget("t", "MAX").to_objective()

lookup = pd.DataFrame.from_records(
    [
        {"p1": 0, "p2": 100, "t": 23},
        {"p1": 2, "p2": 10, "t": 5},
        {"p1": 3, "p2": 1000, "t": 56},
    ]
)
```