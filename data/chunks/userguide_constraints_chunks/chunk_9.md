# Constraints
## Discrete Constraints
### DiscreteExcludeConstraint

The [`DiscreteExcludeConstraint`]()
constraint simply removes a set of search space elements, according to its
specifications.

The following example would exclude entries where “Ethanol” and “DMF” are combined with
temperatures above 150, which might be due to their chemical instability at those
temperatures:

```python
from baybe.constraints import (
    DiscreteExcludeConstraint,
    ThresholdCondition,
    SubSelectionCondition,
)

DiscreteExcludeConstraint(
    parameters=["Temperature", "Solvent"],  # names of the affected parameters
    combiner="AND",  # specifies how the conditions are logically combined
    conditions=[  # requires one condition for each entry in parameters
        ThresholdCondition(threshold=150, operator=">"),
        SubSelectionCondition(selection=["Ethanol", "DMF"]),
    ],
)
```

A more detailed example can be found
[here]().