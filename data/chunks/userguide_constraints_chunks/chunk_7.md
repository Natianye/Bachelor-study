# Constraints
## Conditions
### SubSelectionCondition

In case a specific subset of values needs to be selected, it can be done with the
[`SubSelectionCondition`]():

```python
from baybe.constraints import SubSelectionCondition

SubSelectionCondition(  # will select two solvents identified by their labels
    selection=["Ethanol", "DMF"]
)
```