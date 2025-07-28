# BayBE — A Bayesian Back End for Design of Experiments
## ⚡ Quick Start
### Optional: Defining the Optimization Strategy

As an optional step, we can specify details on how the optimization should be
conducted. If omitted, BayBE will choose a default setting.

For our example, we combine two recommenders via a so-called meta recommender named
`TwoPhaseMetaRecommender`:

1. In cases where no measurements have been made prior to the interaction with BayBE,
   a selection via `initial_recommender` is used.
2. As soon as the first measurements are available, we switch to `recommender`.

For more details on the different recommenders, their underlying algorithmic
details, and their configuration settings, see the
[recommenders section](https://emdgroup.github.io/baybe/stable/userguide/recommenders.html)
of the user guide.

```python
from baybe.recommenders import (
    BotorchRecommender,
    FPSRecommender,
    TwoPhaseMetaRecommender,
)

recommender = TwoPhaseMetaRecommender(
    initial_recommender=FPSRecommender(),  # farthest point sampling
    recommender=BotorchRecommender(),  # Bayesian model-based optimization
)
```