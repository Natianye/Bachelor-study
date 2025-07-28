# Serialization
## Deserialization from configuration strings
### Dataframe deserialization

When serializing BayBE objects, contained [`DataFrames`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame) are
automatically converted to a binary format in order to

1. ensure that the involved data types are exactly restored after completing the roundtrip and
2. decrease the size of the serialization string through compression.

From the user’s perspective, this has the disadvantage that the resulting JSON
representation is not human-readable, which can be a challenge when working
with configuration strings.

While you can manually work around this additional conversion step using our
`serialize_dataframe` and
`deserialize_dataframe` helpers,
a more elegant solution becomes apparent when noticing that [invoking alternative
constructors](#alternative-constructors) also works for non-BayBE objects.
In particular, this means you can resort to any dataframe constructor of your choice
(such as [`DataFrame.from_records`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_records.html#pandas.DataFrame.from_records))
when defining your configuration, instead of having to work with compressed formats:

```python
import pandas as pd
from baybe.searchspace.discrete import SubspaceDiscrete

subspace = SubspaceDiscrete.from_dataframe(
    pd.DataFrame.from_records(
        data=[[1, "a"], [2, "b"], [3, "c"]], columns=["Number", "Category"]
    )
)

subspace_json = """
{
    "constructor": "from_dataframe",
    "df": {
        "constructor": "from_records",
        "data": [[1, "a"], [2, "b"], [3, "c"]],
        "columns": ["Number", "Category"]
    }
}
"""
reconstructed = SubspaceDiscrete.from_json(subspace_json)

assert subspace == reconstructed
```