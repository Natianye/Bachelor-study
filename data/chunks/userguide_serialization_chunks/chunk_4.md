# Serialization
## Deserialization from configuration strings
### Basic string assembly

Writing a configuration for a certain BayBE object in form of a serialization string is
easy:

1. Select your desired object class
2. Identify the arguments expected by one of its constructors (see also [here](#alternative-constructors))
3. Pack them into a JSON string that mirrors the constructor signature

Let’s have a more detailed look, for instance, at the serialization string from
the [above example](#json-serialization), this time assuming we wanted to assemble
the string manually.
For this purpose, we have a peek at the signature of the `__init__` method of
`CategoricalParameter`
and notice that it has two required arguments, `name` and `values`.
We specify these accordingly as separate fields in the JSON string:

```python
from baybe.parameters import CategoricalParameter

parameter_json = """
{
    "name": "Setting",
    "values": ["low", "high"]
}
"""
via_json = CategoricalParameter.from_json(parameter_json)
via_init = CategoricalParameter(name="Setting", values=["low", "high"])

assert via_json == via_init
```