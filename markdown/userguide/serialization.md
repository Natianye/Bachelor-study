# Serialization

BayBE is shipped with a sophisticated serialization engine that allows to unstructure
its objects into basic types and seamlessly reassemble them afterward.
This enables a variety of advanced workflows, such as:

* Persisting objects for later use
* Transmission and processing outside the Python ecosystem
* Interaction with APIs and databases
* Writing “configuration” files

Some of these workflows are demonstrated in the sections below.

<a id="json-serialization"></a>

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

## Deserialization from configuration strings

The workflow described [above](#json-serialization) most naturally applies to
situations where we start inside the Python ecosystem and want to make an object
leave the running session.
However, in many cases, we would like to kickstart the process from the other end and
rather specify a BayBE object **outside** Python for use in a later computation.
Common examples are when we wish to interact with an API or simply want to persist
a certain BayBE component in the form of a “configuration” file.

The following sections give an overview of the flexibilities that are offered for this
task. Of course, the underlying concepts can be mixed and matched arbitrarily.

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

### Using default values

Just like default values can be omitted when working in Python,
they can be omitted from the corresponding serialization string:

```python
from baybe.parameters import CategoricalParameter

p1 = CategoricalParameter(name="Setting", values=["low", "high"])
p2 = CategoricalParameter(name="Setting", values=["low", "high"], encoding="OHE")

p1_json = """
{
    "name": "Setting",
    "values": ["low", "high"]
}
"""
p2_json = """
{
    "name": "Setting",
    "values": ["low", "high"],
    "encoding": "OHE"
}
"""

p1_via_json = CategoricalParameter.from_json(p1_json)
p2_via_json = CategoricalParameter.from_json(p2_json)

assert p1 == p1_via_json == p2 == p2_via_json 
```

### Automatic field conversion

BayBE classes apply converters to their inputs so that simpler attribute
representations can be passed.
Of course, these shortcuts can be analogously used inside a configuration string.

While the above holds generally true for all classes that have converters in place,
providing a few specific example may help to convey the concept:

* Since `Intervals` can be created *implicitly*,
  it is enough the specify their bound values directly:
  ```python
  from baybe.targets import NumericalTarget
  from baybe.utils.interval import Interval

  t1 = NumericalTarget(name="T", mode="MAX", bounds=Interval(0, 1))
  t2 = NumericalTarget(name="T", mode="MAX", bounds=(0, 1))
  t3 = NumericalTarget.from_json('{"name": "T", "mode": "MAX", "bounds": [0, 1]}')

  assert t1 == t2 == t3
  ```
* Conversion to enums happens automatically whenever needed;
  therefore, providing a raw string instead is sufficient:
  ```python
  from baybe.targets import NumericalTarget, TargetMode

  t1 = NumericalTarget(name="T", mode=TargetMode.MAX)
  t2 = NumericalTarget(name="T", mode="MAX")
  t3 = NumericalTarget.from_json('{"name": "T", "mode": "MAX"}')

  assert t1 == t2 == t3
  ```

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

### Using abbreviations

Classes that have an `abbreviation` class variable defined can be conveniently
deserialized using the corresponding abbreviation string:

```python
from baybe.acquisition.base import AcquisitionFunction

acqf1 = AcquisitionFunction.from_json('{"type": "UpperConfidenceBound"}')
acqf2 = AcquisitionFunction.from_json('{"type": "UCB"}')

assert acqf1 == acqf2
```

<a id="nested-objects"></a>

### Nesting objects

BayBE objects typically appear as part of a larger object hierarchy.
For instance, a
`SearchSpace` can hold one or several
`Parameters`, just like an
`Objective` can hold one or several
`Targets`.
This hierarchical structure can be directly replicated in the serialization string:

```python
from baybe.objectives import DesirabilityObjective
from baybe.targets import NumericalTarget

objective = DesirabilityObjective(
    targets=[
        NumericalTarget(name="T1", mode="MAX", bounds=(-1, 1)),
        NumericalTarget(name="T2", mode="MIN", bounds=(0, 1)),
    ],
    weights=[0.1, 0.9],
    scalarizer="MEAN",
)

objective_json = """
{   
    "targets": [
        {
            "type": "NumericalTarget",
            "name": "T1",
            "mode": "MAX",
            "bounds": [-1.0, 1.0]
        }, 
        {
            "type": "NumericalTarget",
            "name": "T2",
            "mode": "MIN",
            "bounds": [0.0, 1.0]
        }
    ],
    "weights": [0.1, 0.9],
    "scalarizer": "MEAN"
}
"""

assert objective == DesirabilityObjective.from_json(objective_json)
```

<a id="alternative-constructors"></a>

### Invoking alternative constructors

Many BayBE classes offer additional routes of construction next to the default
mechanism via the class’ `__init__` method.
This offers convenient ways of object initialization alternative to specifying
an object’s attributes in their “canonical” form, which is often not the preferred
approach.

For instance, a search space is composed of two sub-components, a
[discrete subspace]()
and a [continuous subspace](),
which are accordingly expected by the
[`SearchSpace`]() constructor.
However, instead of providing the two components directly, most users would more
naturally invoke one of the alternative class methods available, such as
`SearchSpace.from_product` or
`SearchSpace.from_dataframe`.

Using a serialization string, the same alternative routes can be triggered via the
optional `constructor` field that allows specifying the initializer to be used for the
object creation step:

```python
from baybe.searchspace import SearchSpace
from baybe.parameters import CategoricalParameter, NumericalDiscreteParameter

searchspace = SearchSpace.from_product(
    parameters=[
        CategoricalParameter(name="Category", values=["low", "high"]),
        NumericalDiscreteParameter(name="Number", values=[1, 2, 3]),
    ]
)

searchspace_json = """
{
    "constructor": "from_product",
    "parameters": [
        {
            "type": "CategoricalParameter",
            "name": "Category",
            "values": ["low", "high"]
        },
        {
            "type": "NumericalDiscreteParameter",
            "name": "Number",
            "values": [1, 2, 3]
        }
    ]
}
"""

assert searchspace == SearchSpace.from_json(searchspace_json)
```

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
