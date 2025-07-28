# Asynchronous Workflows
## Adding Partial Results

A *partial result* is possible if you have multiple targets, but only measured the
outcome for some of those. This is a common occurrence, especially if the different
target measurements correspond to experiments that differ in complexity or duration.

As a simple example, consider a campaign with medical background aimed at creating a
drug formulation. Typically, there are quick initial analytics performed on the
formulation, followed by *in vitro* experiments followed by mouse *in vivo* experiments.
Without the ability to use partial measurements, you would have to wait until the slow
mouse experiment for a given recommendation is measured until you could utilize any of
the other (faster) experimental outcomes for that recommendation. Furthermore, if the fast
measurements are already unpromising, the slower target measurements are possibly never
performed at all.

In BayBE, you can leverage results even if they are only partial. This is indicated
by setting the corresponding target measurement value to NaN. There are several ways to indicate this, e.g.:

* [`numpy.nan`](https://numpy.org/doc/stable/reference/constants.html#numpy.nan)
* [`pandas.NA`](https://pandas.pydata.org/docs/reference/api/pandas.NA.html#pandas.NA)
* `None`
* `float("nan")`

Let us consider this 3-batch of recommendations, assuming
we need to measure “Target_1”, “Target_2” and “Target_3”:

```python
import numpy as np
import pandas as pd

rec = campaign.recommend(batch_size=3)
# Resetting the index to have easier access via .loc later
measurements = rec.reset_index(drop=True)

# Add measurement results
measurements.loc[0, "Target_1"] = 10.3
measurements.loc[0, "Target_2"] = 0.5
measurements.loc[0, "Target_3"] = 11.1

measurements.loc[1, "Target_1"] = 7.1
measurements.loc[1, "Target_2"] = np.nan  # not measured yet
measurements.loc[1, "Target_3"] = 12.2

measurements.loc[2, "Target_1"] = 11.4
measurements.loc[2, "Target_2"] = pd.NA  # not measured yet
measurements.loc[2, "Target_3"] = None  # not measured yet

measurements

# Proceed with campaign.add_measurements ...
```

| Param_1   |   Param_2 | …   |   Target_1 |   Target_2 |   Target_3 |
|-----------|-----------|-----|------------|------------|------------|
| on        |       1.1 | …   |       10.3 |        0.5 |       11.1 |
| on        |       3.8 | …   |        7.1 |      nan   |       12.2 |
| off       |       2.9 | …   |       11.4 |      nan   |      nan   |

Internally, the incomplete rows are dropped when fitting a surrogate model for each
target. If you use an unsupported surrogate model, an error will be thrown at runtime.