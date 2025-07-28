# Utilities
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