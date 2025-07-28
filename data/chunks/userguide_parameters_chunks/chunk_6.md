# Parameters
## Discrete Parameters
### CategoricalParameter

A [`CategoricalParameter`]() supports sets of strings as labels.
This is most suitable if the experimental choices cannot easily be translated into a
number.
Examples for this could be vendors like `("Vendor A", "Vendor B", "Vendor C")` or
post codes like `("PO16 7GZ", "GU16 7HF", "L1 8JQ")`.

Categorical parameters in BayBE can be encoded via integer or one-hot encoding.
For some cases, such basic forms of encoding make sense, e.g. if we had a parameter
for a setting with values
`("low", "medium", "high")`, an integer-encoding into values `(1, 2, 3)` would
be reasonable.

```python
from baybe.parameters import CategoricalParameter

CategoricalParameter(
    name="Intensity",
    values=("low", "medium", "high"),
    active_values=(
        "low",  # optional, only combinations with Intensity=low will be recommended
    ),
    encoding="INT",  # optional, uses integer encoding as described above
)
```

However, in other cases, these encodings would introduce undesired biases to the model.
Take, for instance, a parameter for a choice of solvents with values
`("Solvent A", "Solvent B", "Solvent C")`. Encoding these with `(1, 2, 3)` as
above would imply that “Solvent A” is more similar to “Solvent B” than to “Solvent C”,
simply because the number 1 is closer to 2 than to 3.
Hence, for an arbitrary set of labels, such an ordering cannot generally be assumed.
In the particular case of substances, it not even possible to describe the similarity
between labels by ordering along one single dimension.
For this reason, we also provide the [`SubstanceParameter`](), which encodes labels
corresponding to small molecules with chemical descriptors, capturing their similarities
much better and without the need for the user to think about ordering and similarity
in the first place.
This concept is generalized in the [`CustomDiscreteParameter`](), where the user can
provide their own custom set of descriptors for each label.