# Recommenders
## Meta Recommenders

In analogy to meta studies, meta recommenders are wrappers that operate on a sequence
of pure recommenders and determine when to switch between them according to different
logics. BayBE offers three distinct kinds of meta recommenders.

* The
  [`TwoPhaseMetaRecommender`]()
  employs two distinct recommenders and switches between them at a certain specified
  point, controlled by the `switch_after` attribute. This is useful e.g. if you want a
  different recommender for the initial recommendation when there is no data yet
  available. This simple example would recommend randomly for the first batch and switch
  to a Bayesian recommender as soon as measurements have been ingested:

```python
from baybe.recommenders import (
    BotorchRecommender,
    TwoPhaseMetaRecommender,
    RandomRecommender,
)

recommender = TwoPhaseMetaRecommender(
    initial_recommender=RandomRecommender(), recommender=BotorchRecommender()
)
```

* The **[`SequentialMetaRecommender`]()**
  introduces a simple yet versatile approach by utilizing a predefined list of
  recommenders. By specifying the desired behavior using the `mode` attribute, it is
  possible to flexibly determine the meta recommender’s response when it exhausts the
  available recommenders. The possible choices are to either raise an error, re-use the
  last recommender or re-start at the beginning of the sequence.
* Similar to the `SequentialMetaRecommender`, the
  **[`StreamingSequentialMetaRecommender`]()**
  enables the utilization of *arbitrary* iterables to select recommender.

  #### WARNING
  Due to the arbitrary nature of iterables that can be used, (de-)serializability cannot
  be guaranteed. As a consequence, using a `StreamingSequentialMetaRecommender` results
  in an error if you attempt to serialize the corresponding object or higher-level
  objects containing it.