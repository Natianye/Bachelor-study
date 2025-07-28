# Constraints

### ThresholdCondition

For numerical parameters, we might want to select a certain range, which can be
achieved with a [`ThresholdCondition`]():

```python
from baybe.constraints import ThresholdCondition

ThresholdCondition(  # will select all values above 150
    threshold=150,
    operator=">",
)
```