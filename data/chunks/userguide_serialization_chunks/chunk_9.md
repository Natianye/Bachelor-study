# Serialization
## Deserialization from configuration strings
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