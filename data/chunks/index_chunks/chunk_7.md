# BayBE — A Bayesian Back End for Design of Experiments
## ⚡ Quick Start
### The Optimization Loop

We can now construct a campaign object that brings all pieces of the puzzle together:

```python
from baybe import Campaign

campaign = Campaign(searchspace, objective, recommender)
```

With this object at hand, we can start our experimentation cycle.
In particular:

* We can ask BayBE to `recommend` new experiments.
* We can `add_measurements` for certain experimental settings to the campaign’s
  database.

Note that these two steps can be performed in any order.
In particular, available measurements can be submitted at any time and also several
times before querying the next recommendations.

```python
df = campaign.recommend(batch_size=3)
print(df)
```

```none
   Granularity  Pressure[bar]    Solvent
15      medium            1.0  Solvent D
10      coarse           10.0  Solvent C
29        fine            5.0  Solvent B
```

Note that the specific recommendations will depend on both the data
already fed to the campaign and the random number generator seed that is used.

After having conducted the corresponding experiments, we can add our measured
targets to the table and feed it back to the campaign:

```python
df["Yield"] = [79.8, 54.1, 59.4]
campaign.add_measurements(df)
```

With the newly arrived data, BayBE can produce a refined design for the next iteration.
This loop would typically continue until a desired target value has been achieved in
the experiment.