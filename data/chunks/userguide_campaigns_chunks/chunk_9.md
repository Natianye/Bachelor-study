# Campaigns
## Adding Measurements

Available experimental data can be added at any time during the campaign lifecycle using
the [`add_measurements`]() method,
which expects a `DataFrame` containing the values of the used experimental parameters
and all corresponding target measurements.
If measurements are to be added immediately after a call to `recommend`,
this is most easily achieved by augmenting the  `DataFrame` returned from that call
with the respective target columns.

```python
rec["Target_max"] = [2, 4, 9]  # 3 values matching the batch_size of 3
campaign.add_measurements(rec)
new_rec = campaign.recommend(batch_size=5)
```

After adding the measurements, the corresponding `DataFrame` thus has the following
form:

|    | Categorical_1   | Categorical_2   |   Num_disc_1 |   Target_max |
|----|-----------------|-----------------|--------------|--------------|
| 15 | B               | good            |            1 |            2 |
| 18 | C               | bad             |            1 |            4 |
|  9 | B               | bad             |            1 |            9 |