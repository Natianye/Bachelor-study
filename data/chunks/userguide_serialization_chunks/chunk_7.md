# Serialization
## Deserialization from configuration strings
### The type field

Due to the leading design philosophy behind BayBE to provide its users easy access
to a broad range of tools, you typically have the choice between several modelling
alternatives when building your objects.
For example, when describing the degrees of freedom of your experimental campaign,
you can chose from several different [parameter types](parameters.md).

While this offers great flexibility, it comes with a challenge for deserialization
because you cannot know a priori which concrete object subclass is contained
in an incoming serialization string on the receiving end.
Instead, you oftentimes need to be able to process the incoming string dynamically.

For example, consider the following string, which perfectly mirrors the signatures of
both
`CategoricalParameter` and
`TaskParameter`:

```python
parameter_json = """
{
    "name": "Setting",
    "values": ["low", "high"]
}
"""
```

Unless you are aware of the specific purpose for which the string was created,
calling one of the classes’ constructors directly is impossible because you
simply do not know which one to chose.
A similar situation arises with [nested objects](#nested-objects) because resorting to
an explicit constructor call of a hand-selected subclass is only possible at the
highest level of the hierarchy, whereas the inner object types would remain unspecified.

The problem can be easily circumvented using an explicit subclass resolution
mechanism, i.e., by tagging the respective subclass in an additional `type` field that
holds the class’ name.
This allows to deserialize the object from the corresponding base class instead
(i.e., `Parameter` class in the example below),
mirroring the flexibility of specifying subtypes to your configuration file:

```python
from baybe.parameters.base import Parameter
from baybe.parameters import CategoricalParameter, TaskParameter

categorical_parameter = CategoricalParameter(name="Setting", values=["low", "high"])
categorical_parameter_json = """
{
    "type": "CategoricalParameter",
    "name": "Setting",
    "values": ["low", "high"]
}
"""
# NOTE: we can use `Parameter.from_json` instead of `CategoricalParameter.from_json`:
categorical_parameter_reconstructed = Parameter.from_json(categorical_parameter_json)
assert categorical_parameter == categorical_parameter_reconstructed

task_parameter = TaskParameter(name="Setting", values=["low", "high"])
task_parameter_json = """
{
    "type": "TaskParameter",
    "name": "Setting",
    "values": ["low", "high"]
}
"""
# NOTE: we can use `Parameter.from_json` instead of `TaskParameter.from_json`:
task_parameter_reconstructed = Parameter.from_json(task_parameter_json)
assert task_parameter == task_parameter_reconstructed
```

#### NOTE
When serializing an object that belongs to a class hierarchy, BayBE automatically
injects the `type` field into the serialization string to enable frictionless deserialization
at a later stage.