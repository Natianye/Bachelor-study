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