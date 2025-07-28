# Search Spaces
## Discrete Subspaces
### Constructing from a Dataframe

[`SubspaceDiscrete.from_dataframe`]() constructs a discrete subspace from a given dataframe.
By default, this method tries to infer the data column as as a [`NumericalDiscreteParameter`]() and uses [`CategoricalParameter`]() as fallback.
However, it is possible to change this behavior by using the optional `parameters` keyword.
This list informs `from_dataframe` about the parameters and the types of parameters that should be used.
In particular, it is necessary to provide such a list if there are non-numerical parameters that should not be interpreted as categorical parameters.

```python
import pandas as pd

df = pd.DataFrame(
    {
        "x0": [2, 3, 3],
        "x1": [5, 4, 6],
        "x2": [9, 7, 9],
    }
)
subspace = SubspaceDiscrete.from_dataframe(df)
```

```default
 Discrete Parameters
   Name                        Type  Num_Values Encoding
 0   x0  NumericalDiscreteParameter           2     None
 1   x1  NumericalDiscreteParameter           3     None
 2   x2  NumericalDiscreteParameter           2     None
```