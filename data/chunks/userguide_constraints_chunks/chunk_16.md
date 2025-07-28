# Constraints
## Discrete Constraints
### DiscreteCustomConstraint

With a [`DiscreteCustomConstraint`]()
constraint, you can specify a completely custom filter:

```python
import pandas as pd
import numpy as np
from baybe.constraints import DiscreteCustomConstraint


def custom_filter(df: pd.DataFrame) -> pd.Series:  # this signature is required
    """
    In this example, we exclude entries where the square root of the
    temperature times the cubed pressure are larger than 5.6.
    """
    mask_good = np.sqrt(df["Temperature"]) * np.power(df["Pressure"], 3) <= 5.6

    return mask_good


DiscreteCustomConstraint(
    parameters=[  # the custom function will have access to these variables
        "Pressure",
        "Temperature",
    ],
    validator=custom_filter,
)
```

Find a detailed example [here]().

#### WARNING
Due to the arbitrary nature of code and dependencies that can be used in the
`DiscreteCustomConstraint`, (de-)serializability cannot be guaranteed. As a consequence,
using a `DiscreteCustomConstraint` results in an error if you attempt to serialize
the corresponding object or higher-level objects containing it.