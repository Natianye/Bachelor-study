# BayBE — A Bayesian Back End for Design of Experiments
## ⚡ Quick Start
### Defining the Search Space

Next, we inform BayBE about the available “control knobs”, that is, the underlying
system parameters we can tune to optimize our targets. This also involves specifying
their values/ranges and other parameter-specific details.

For our example, we assume that we can control three parameters – `Granularity`,
`Pressure[bar]`, and `Solvent` – as follows:

```python
from baybe.parameters import (
    CategoricalParameter,
    NumericalDiscreteParameter,
    SubstanceParameter,
)

parameters = [
    CategoricalParameter(
        name="Granularity",
        values=["coarse", "medium", "fine"],
        encoding="OHE",  # one-hot encoding of categories
    ),
    NumericalDiscreteParameter(
        name="Pressure[bar]",
        values=[1, 5, 10],
        tolerance=0.2,  # allows experimental inaccuracies up to 0.2 when reading values
    ),
    SubstanceParameter(
        name="Solvent",
        data={
            "Solvent A": "COC",
            "Solvent B": "CCC",  # label-SMILES pairs
            "Solvent C": "O",
            "Solvent D": "CS(=O)C",
        },
        encoding="MORDRED",  # chemical encoding via scikit-fingerprints
    ),
]
```

For more parameter types and their details, see the
[parameters section](https://emdgroup.github.io/baybe/stable/userguide/parameters.html)
of the user guide.

Additionally, we can define a set of constraints to further specify allowed ranges and
relationships between our parameters. Details can be found in the
[constraints section](https://emdgroup.github.io/baybe/stable/userguide/constraints.html) of the user guide.
In this example, we assume no further constraints.

With the parameter definitions at hand, we can now create our
`SearchSpace` based on the Cartesian product of all possible parameter values:

```python
from baybe.searchspace import SearchSpace

searchspace = SearchSpace.from_product(parameters)
```

See the [search spaces section](https://emdgroup.github.io/baybe/stable/userguide/searchspace.html)
of our user guide for more information on the structure of search spaces
and alternative ways of construction.