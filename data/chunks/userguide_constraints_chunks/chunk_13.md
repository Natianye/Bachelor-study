# Constraints
## Discrete Constraints
### DiscreteDependenciesConstraint

A dependency is a situation where parameters depend on other parameters.
Let’s say an experimental setup has a parameter called `"Switch"`, which turns on
pieces of equipment that are optional.
This means the other parameters (called `affected_parameters`) are only relevant if
the switch parameter has the value `"on"`. If the switch is `"off"`, the affected
parameters are irrelevant.

You can specify such a dependency with the
[`DiscreteDependenciesConstraint`]()
, which requires:

1. A list `parameters` with the names of the parameters upon which others depend.
2. A list `conditions`, specifying the values of the corresponding entries in
   `parameters` that “activate” the dependent parameters.
3. A list of lists, each containing the `affected_parameters`, which become relevant
   only if the corresponding entry in `parameters` is active as specified by the
   entry in `conditions`.

Internally, BayBE drops elements from the `SearchSpace` where affected parameters are
irrelevant. Since in our example `"off"` is still a valid value for the switch, the
`SearchSpace` will still retain **one** configuration for that setting, showing arbitrary
values for the `affected_parameters` (which can be ignored).

<a id="ddc"></a>

#### IMPORTANT
BayBE requires that all dependencies are declared in a single
`DiscreteDependenciesConstraint`. Creating a `SearchSpace` from multiple
`DiscreteDependenciesConstraint`’s will throw a validation error.

In the example below, we mimic a situation where there are two switches and each switch
activates two other parameters that are only relevant if the first switch is `"on"` / the
second switch is set to `"right"`, respectively.

```python
from baybe.constraints import DiscreteDependenciesConstraint, SubSelectionCondition

DiscreteDependenciesConstraint(
    parameters=["Switch_1", "Switch_2"],  # the two parameters upon which others depend
    conditions=[
        SubSelectionCondition(
            # values of Switch_1 that activate the affected parameters
            selection=["on"]
        ),
        SubSelectionCondition(
            # values of Switch_2 that activate the affected parameters
            selection=["right"]
        ),
    ],
    affected_parameters=[
        ["Solvent", "Fraction"],  # parameters affected by Switch_1
        ["Frame_1", "Frame_2"],  # parameters affected by Switch_2
    ],
)
```

An end to end example can be found [here]().