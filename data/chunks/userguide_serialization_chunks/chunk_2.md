# Serialization

BayBE is shipped with a sophisticated serialization engine that allows to unstructure
its objects into basic types and seamlessly reassemble them afterward.
This enables a variety of advanced workflows, such as:

* Persisting objects for later use
* Transmission and processing outside the Python ecosystem
* Interaction with APIs and databases
* Writing “configuration” files

Some of these workflows are demonstrated in the sections below.

## JSON (de-)serialization

Most BayBE objects can be conveniently serialized into an equivalent JSON
representation by calling their
`to_json` method.
The obtained JSON string can then be deserialized via the
`from_json` method
of the corresponding class, which yields an “equivalent copy” of the original object.

For example:

```python
from baybe.parameters import CategoricalParameter

parameter = CategoricalParameter(name="Setting", values=["low", "high"])
json_string = parameter.to_json()
reconstructed = CategoricalParameter.from_json(json_string)
assert parameter == reconstructed
```

This form of roundtrip serialization can be used, for instance, to persist objects
for long-term storage, but it also provides an easy way to “move” existing objects
between Python sessions by executing the deserializing step in a different context
than the serialization step.