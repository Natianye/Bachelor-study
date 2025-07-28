# Simulation
## The Lookup Mechanism
### Using a `Callable`

Using a `Callable` is the most general way to provide a lookup mechanism.
Any `Callable` is a suitable lookup as long as it accepts a dataframe containing parameter configurations and returns the corresponding target values.
More specifically:

- The input is expected to be a dataframe whose column names contain the parameter names and whose rows represent valid parameter configurations.
- The returned output must be a dataframe whose column names contain the target names and whose rows represent valid target values.
- The indices of the input and output dataframes must match.

An example might look like this:

```python
import pandas as pd

from baybe.parameters import NumericalContinuousParameter
from baybe.searchspace import SearchSpace
from baybe.targets import NumericalTarget

searchspace = SearchSpace.from_product(
    [
        NumericalContinuousParameter("p1", [0, 1]),
        NumericalContinuousParameter("p2", [-1, 1]),
    ]
)
objective = NumericalTarget("t1", "MAX").to_objective()


def lookup(df: pd.DataFrame) -> pd.DataFrame:
    """Map parameter configurations to target values."""
    return pd.DataFrame({"t1": df["p1"] ** 2}, index=df.index)


lookup(searchspace.continuous.sample_uniform(10))
```