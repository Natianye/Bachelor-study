# Parameters
## Discrete Parameters
### SubstanceParameter

Instead of `values`, this parameter accepts `data` in form of a dictionary. The
items correspond to pairs of labels and [SMILES](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system).
SMILES are string-based representations of molecular structures.
Based on these, BayBE can assign each label a set of molecular descriptors as encoding.

For instance, a parameter corresponding to a choice of solvents can be initialized with:

```python
from baybe.parameters import SubstanceParameter

SubstanceParameter(
    name="Solvent",
    data={
        "Water": "O",
        "1-Octanol": "CCCCCCCCO",
        "Toluene": "CC1=CC=CC=C1",
    },
    active_values=[  # optional, recommends only water and toluene as solvent
        "Water",
        "Toluene",
    ],
    encoding="MORDRED",  # optional
    decorrelate=0.7,  # optional
)
```

The `encoding` defines what kind of descriptors are calculated using the
[scikit-fingerprints](https://scikit-fingerprints.github.io/scikit-fingerprints/) package.
It can be specified either by passing the corresponding [`SubstanceEncoding`]() member
(click to see full list of options) or its string representation, e.g. use
[`SubstanceParameter.MORDRED`]()
or its string alias `"MORDRED"` to select the `MordredFingerprint`.

Here are examples of a few popular fingerprints:

* `ECFP`: Extended Connectivity FingerPrint,
  which is a circular topological fingerprint similar to Morgan fingerprint.
* `MORDRED`: Chemical descriptor based fingerprint.
* `RDKIT`: The RDKit fingerprint, which is based on hashing of molecular subgraphs.

You can customize the fingerprint computation by passing arguments of the corresponding
[scikit-fingerprints](https://scikit-fingerprints.github.io/scikit-fingerprints/) class to the `kwargs_fingerprint` argument the [`SubstanceParameter`]() constructor.
Similarly, for fingerprints requiring conformers,
the configuration options for conformer computation can be specified via `kwargs_conformer`.

```python
from baybe.parameters import SubstanceParameter

SubstanceParameter(
    name="Solvent",
    data={
        "Water": "O",
        "1-Octanol": "CCCCCCCCO",
        "Toluene": "CC1=CC=CC=C1",
    },
    encoding="ECFP",
    kwargs_fingerprint={
        "radius": 4,  # Set maximum radius of resulting subgraphs
        "fp_size": 1024,  # Change the number of computed bits
    },
)

```

These calculations will typically result in 500 to 1500 numbers per molecule.
To avoid detrimental effects on the surrogate model fit, we reduce the number of
descriptors via decorrelation before using them.
For instance, the `decorrelate` option in the example above specifies that only
descriptors with a correlation lower than 0.7 to any other descriptor will be kept.
This usually reduces the number of descriptors to 10-50, depending on the specific
items in `data`.

#### WARNING
The descriptors calculated for a [`SubstanceParameter`]() were developed to describe
small molecules and are not suitable for other substances. If you deal with large
molecules like polymers or arbitrary substance mixtures, we recommend to provide your
own descriptors via the [`CustomDiscreteParameter`]().

In the following example from an application you can see
the outcome for treating the solvent, base and ligand in a direct arylation reaction
optimization (from [Shields, B.J. et al.](https://doi.org/10.1038/s41586-021-03213-y)) with
different chemical encodings compared to one-hot and a random baseline:

![image](../examples/Backtesting/full_lookup_light.svg)![image](../examples/Backtesting/full_lookup_dark.svg)