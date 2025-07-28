# Parameters
## Discrete Parameters
A discrete parameter has a finite set of possible values that can be recommended.
These values can be numeric or label-like (i.e. strings) and are transformed
internally before being ingested by the surrogate model.

### NumericalDiscreteParameter

This is the right type for parameters that have numerical values.
We support sets with equidistant values like `(1, 2, 3, 4, 5)` but also unevenly
spaced sets of numbers like `(0.2, 1.0, 2.0, 5.0, 10.0, 50.0)`.

```python
from baybe.parameters import NumericalDiscreteParameter

NumericalDiscreteParameter(
    name="Temperature",
    # you can also use np.arange or similar to provide values
    values=(0, 10, 20, 30, 40, 50),
)
```