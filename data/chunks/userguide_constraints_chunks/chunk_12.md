# Constraints
## Discrete Constraints
### DiscreteLinkedParametersConstraint

The [`DiscreteLinkedParametersConstraint`]()
is, in a sense, the opposite of the
[`DiscreteNoLabelDuplicatesConstraint`]().
It will ensure that **only** entries with duplicated labels are present.
This can be useful, for instance, in situations where we have one parameter but would
like to include it with several encodings:

```python
from baybe.parameters import SubstanceParameter
from baybe.constraints import DiscreteLinkedParametersConstraint

dict_solvents = {"Water": "O", "THF": "C1CCOC1", "Octanol": "CCCCCCCCO"}
solvent_encoding1 = SubstanceParameter(
    name="Solvent_RDKIT_enc",
    data=dict_solvents,
    encoding="RDKIT",
)
solvent_encoding2 = SubstanceParameter(
    name="Solvent_MORDRED_enc",
    data=dict_solvents,
    encoding="MORDRED",
)
DiscreteLinkedParametersConstraint(
    parameters=["Solvent_RDKIT_enc", "Solvent_MORDRED_enc"]
)
```

|    | Solvent_RDKIT_enc   | Solvent_MORDRED_enc   | With DiscreteLinkedParametersConstraint   |
|----|---------------------|-----------------------|-------------------------------------------|
|  1 | Water               | Water                 |                                           |
|  2 | THF                 | Water                 | would be excluded                         |
|  3 | Octanol             | Octanol               |                                           |