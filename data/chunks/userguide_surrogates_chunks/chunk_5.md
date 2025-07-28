# Surrogates
## Multi-Output Modeling
### Composite Surrogates

An alternative to surrogate replication is to manually assemble your
`CompositeSurrogate`. This can be useful if you want
to

* use the same model architecture but with different settings for each output or
* use different architectures for the outputs to begin with.

```python
from baybe.surrogates import (
    CompositeSurrogate,
    GaussianProcessSurrogate,
    RandomForestSurrogate,
)

surrogate = CompositeSurrogate(
    {
        "target_a": GaussianProcessSurrogate(),
        "target_b": RandomForestSurrogate(),
    }
)
```

A noticeable difference to the replication approach is that manual assembly requires
the exact set of target variables to be known at the time the object is created.