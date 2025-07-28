# Campaigns
## Getting Recommendations
### Basics

To obtain a recommendation for the next batch of experiments, we can query the
campaign via the [`recommend`]() method.
It expects a parameter `batch_size` that specifies the desired number of
experiments to be conducted.

```python
rec = campaign.recommend(batch_size=3)
```

Calling the function returns a `DataFrame` with `batch_size` many rows, each
representing a particular parameter configuration from the campaign’s search space.
Thus, the following might be a `DataFrame` returned by `recommend` in a search space
with the three parameters `Categorical_1`, `Categorical_2` and `Num_disc_1`:

|    | Categorical_1   | Categorical_2   |   Num_disc_1 |
|----|-----------------|-----------------|--------------|
| 15 | B               | good            |            1 |
| 18 | C               | bad             |            1 |
|  9 | B               | bad             |            1 |