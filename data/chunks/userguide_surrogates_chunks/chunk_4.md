# Surrogates
## Multi-Output Modeling
### Surrogate Replication

The simplest way to construct a multi-output surrogate is to replicate a given
single-output model architecture for each of the existing output dimensions.

To replicate a given surrogate, you can either call its
`replicate()` method or use the
[`CompositeSurrogate.from_replication()`]()
convenience constructor:

```python
from baybe.surrogates import CompositeSurrogate, GaussianProcessSurrogate

composite_a = GaussianProcessSurrogate().replicate()
composite_b = CompositeSurrogate.from_replication(GaussianProcessSurrogate())

assert composite_a == composite_b
```

However, there are very few cases where such an explicit conversion is required. Because
using a single-output surrogate model in a multi-output context would trivially fail, and
because BayBE cares deeply about its users’ lives, it automatically performs this conversion
for you behind the scenes:

<a id="auto-replication"></a>

The consequence of the above is that you can use the same model object regardless
of the modeling context and its multi-output capabilities.

There is *one* notable exception where an explicit replication may still make
sense: if you want to bypass the existing multi-output mechanics of a surrogate that is
inherently multi-output compatible.