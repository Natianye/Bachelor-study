# Campaigns
## Predictive Statistics

You might be interested in statistics about the predicted target values for your
recommendations, or indeed for any set of possible candidate points. The
[`Campaign.posterior_stats`]() and
[`Surrogate.posterior_stats`]() methods
provide a simple interface for this:

```python
stats = campaign.posterior_stats(rec)
```

This will return a table with mean and standard deviation (and possibly other
statistics) of the target predictions for the provided candidates:

|    |   Yield_mean |   Yield_std |   Selectivity_mean |   Selectivity_std | …   |
|----|--------------|-------------|--------------------|-------------------|-----|
| 15 |        83.54 |        5.23 |              91.22 |              7.42 | …   |
| 18 |        56.12 |        2.34 |              87.32 |             12.38 | …   |
|  9 |        59.1  |        5.34 |              83.72 |              9.62 | …   |

You can also provide an optional sequence of statistic names to compute other
statistics. If a float is provided, the corresponding quantile points will be
calculated:

```python
stats = campaign.posterior_stats(rec, stats=["mode", 0.5])
```

|    |   Yield_mode |   Yield_Q_0.5 |   Selectivity_mode |   Selectivity_Q_0.5 | …   |
|----|--------------|---------------|--------------------|---------------------|-----|
| 15 |        83.54 |         83.54 |              91.22 |               91.22 | …   |
| 18 |        56.12 |         56.12 |              87.32 |               87.32 | …   |
|  9 |        59.1  |         59.1  |              83.72 |               83.72 | …   |