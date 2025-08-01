# Utilities

BayBE comes with a set of useful functions that can make your life easier in certain
scenarios.

## Search Space Memory Estimation

In search spaces that have discrete parts, the memory needed to store the respective
data can become excessively large as the number of points grows with the amount of
possible combinations arising form all discrete parameter values.

The [`SearchSpace.estimate_product_space_size`]()
and [`SubspaceDiscrete.estimate_product_space_size`]()
utilities allow estimating the memory needed to represent the discrete subspace.
They return a [`MemorySize`]() object that
contains some relevant estimates:

```python
import numpy as np

from baybe.parameters import NumericalDiscreteParameter
from baybe.searchspace import SearchSpace

# This creates 10 parameters with 20 values each.
# The resulting space would have 20^10 entries, requiring around 745 TB of memory for
# both experimental and computational representation of the search space.
parameters = [
    NumericalDiscreteParameter(name=f"p{k + 1}", values=np.linspace(0, 100, 20))
    for k in range(10)
]

# Estimate the required memory for such a space
mem_estimate = SearchSpace.estimate_product_space_size(parameters)

# Print quantities of interest
print("Experimental Representation")
print(f"Estimated size: {mem_estimate.exp_rep_human_readable}")
print(f"Estimated size in Bytes: {mem_estimate.exp_rep_bytes}")
print(f"Expected data frame shape: {mem_estimate.exp_rep_shape}")

print("Computational Representation")
print(f"Estimated size: {mem_estimate.comp_rep_human_readable}")
print(f"Estimated size in Bytes: {mem_estimate.comp_rep_bytes}")
print(f"Expected data frame shape: {mem_estimate.comp_rep_shape}")
```

## Reproducibility

In some scenarios, for instance when testing your code setup, it can be useful to fix
the random seeds for all relevant engines to generate reproducible results. BayBE offers
the [`set_random_seed`]() utility for this purpose:

```python
from baybe.utils.random import set_random_seed

# Set the global random seed for all relevant engines
set_random_seed(1337)

# Assuming we have a prepared campaign
campaign.recommend(5)
```

Setting the global random seed can be undesirable if there are other packages in your
setup that might unintentionally be influenced by this. For this, BayBE offers
[`temporary_seed`]():

```python
from baybe.utils.random import temporary_seed

# Set the random seed for all relevant engines temporarily within the context
with temporary_seed(1337):
    campaign.recommend(5)
```

## Adding Fake Target Measurements and Parameter Noise

When creating test scripts, it is often useful to try the recommendation loop for a few
iterations. However, this requires some arbitrary target measurements to be set. Instead
of coming up with a custom logic every time, you can use the
[`add_fake_measurements`]() utility to add fake target
measurements and the [`add_parameter_noise`]()
utility to add artificial parameter noise:

```python
from baybe.utils.dataframe import add_fake_measurements, add_parameter_noise

# Get recommendations
recommendations = campaign.recommend(5)

# Add fake target measurements and artificial parameter noise to the recommendations.
# The utilities modify the dataframes inplace.
measurements = recommendations.copy()
add_fake_measurements(measurements, campaign.targets)
add_parameter_noise(measurements, campaign.parameters)

# Now continue the loop, e.g. by adding the measurements...
```
