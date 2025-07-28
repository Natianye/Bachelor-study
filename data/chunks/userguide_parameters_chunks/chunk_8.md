# Parameters
## Discrete Parameters
### CustomDiscreteParameter

The `encoding` concept introduced above is generalized by the
[`CustomDiscreteParameter`]().
Here, the user is expected to provide their own descriptors for the encoding.

Take, for instance, a parameter that corresponds to the choice of a polymer.
Polymers are not well represented by the small molecule descriptors utilized in the
[`SubstanceParameter`]().
Still, one could provide experimental measurements or common metrics used to classify
polymers:

```python
import pandas as pd
from baybe.parameters import CustomDiscreteParameter

descriptors = pd.DataFrame(
    {
        "Glass_Transition_TempC": [20, -71, -39],
        "Weight_kDalton": [120, 32, 241],
    },
    index=["Polymer A", "Polymer B", "Polymer C"],  # put labels in the index
)

CustomDiscreteParameter(
    name="Polymer",
    data=descriptors,
    active_values=(  # optional, enforces that only Polymer A or C is recommended
        "Polymer A",
        "Polymer C",
    ),
    decorrelate=True,  # optional, uses default correlation threshold
)
```

With the [`CustomDiscreteParameter`](), you can also encode parameter labels that have
nothing to do with substances.
For example, a parameter corresponding to the choice of a vendor is typically not
easily encoded with standard means.
In BayBE’s framework, you can provide numbers corresponding e.g. to delivery time,
reliability or average price of the vendor to encode the labels via the
[`CustomDiscreteParameter`]().