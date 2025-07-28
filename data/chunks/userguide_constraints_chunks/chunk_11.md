# Constraints
## Discrete Constraints
### DiscreteNoLabelDuplicatesConstraint

Sometimes, duplicated labels in several parameters are undesirable.
Consider an example with two solvents that describe different mixture
components.
These might have the exact same or overlapping sets of possible values, e.g.
`["Water", "THF", "Octanol"]`.
It would not necessarily be reasonable to allow values in which both solvents show the
same label/component.
We can exclude such occurrences with the
[`DiscreteNoLabelDuplicatesConstraint`]():

```python
from baybe.constraints import DiscreteNoLabelDuplicatesConstraint

DiscreteNoLabelDuplicatesConstraint(parameters=["Solvent_1", "Solvent_2"])
```

Without this constraint, combinations like below would be possible:

|    | Solvent_1   | Solvent_2   | With DiscreteNoLabelDuplicatesConstraint   |
|----|-------------|-------------|--------------------------------------------|
|  1 | Water       | Water       | would be excluded                          |
|  2 | THF         | Water       |                                            |
|  3 | Octanol     | Octanol     | would be excluded                          |

The usage of `DiscreteNoLabelDuplicatesConstraint` is part of the
[example on slot-based mixtures]().