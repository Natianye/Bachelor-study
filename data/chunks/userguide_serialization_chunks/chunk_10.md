# Serialization
## Deserialization from configuration strings
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