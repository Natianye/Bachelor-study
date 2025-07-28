# Active Learning
## Global Uncertainty Reduction

BayBE also offers the
[`qNegIntegratedPosteriorVariance`]()
(`qNIPV`), which integrates
the posterior variance over the entire search space.
Choosing candidates based on this acquisition function is tantamount to selecting the
set of points resulting in the largest reduction of global uncertainty when added to
the already existing experimental design.

Because of its ability to quantify uncertainty on a global scale, this approach is often
superior to using a point-based uncertainty criterion as acquisition function.
However, due to its computational complexity, it can be prohibitive to integrate over
the entire search space. For this reason, we offer the option to sub-sample parts of it,
configurable via the constructor:

```python
from baybe.acquisition import qNIPV
from baybe.utils.sampling_algorithms import DiscreteSamplingMethod

# Will integrate over the entire search space
qNIPV()

# Will integrate over 50% of the search space, randomly sampled
qNIPV(sampling_fraction=0.5)

# Will integrate over 250 points, chosen by farthest point sampling
# Both lines are equivalent
qNIPV(sampling_n_points=250, sampling_method="FPS")
qNIPV(sampling_n_points=250, sampling_method=DiscreteSamplingMethod.FPS)
```