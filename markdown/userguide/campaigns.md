# Campaigns

When it comes to Bayesian optimization, campaigns emerge as an essential component.
They encompass a group of interconnected experiments that collectively aim to navigate
the search space and find an optimal solution. They take center stage in orchestrating
the iterative process of selecting, evaluating, and refining candidate solutions.
Thus, campaigns are an integral part of Bayesian optimization and, accordingly,
they also play a central role in BayBE.

The [`Campaign`]() class provides a structured framework for
defining and documenting an experimentation process.
It further serves as the primary interface for interacting with BayBE as a user
since it is responsible for handling experimental data, making recommendations, adding
measurements, and most other user-related tasks.

## Creating a Campaign

### Basic Creation

Creating a campaign requires specifying at least two pieces of information that
describe the underlying optimization problem at hand:

| Campaign Specification                     | BayBE Class                                              |
|--------------------------------------------|----------------------------------------------------------|
| What should be optimized in the campaign?  | `Objective` ([class]() / [user guide](objectives.md))    |
| Which experimental factors can be altered? | `SearchSpace` ([class]() / [user guide](searchspace.md)) |

Apart from this basic configuration, it is possible to further define the specific
optimization
`Recommender` ([class]()
/ [user guide](recommenders.md)) to be used.

```python
from baybe import Campaign

campaign = Campaign(
    searchspace=searchspace,  # Required
    objective=objective,  # Required
    recommender=recommender,  # Optional
)
```

### Creation From a JSON Config

Instead of using the default constructor, it is also possible to create a `Campaign`
from a JSON configuration string via
[`Campaign.from_config`]().
Herein, the expected JSON schema of the string should mirror the class
hierarchy of the objects nested in the corresponding campaign object.
The string can be easily validated using
[Campaign.validate_config]() without
instantiating the object, which skips the potentially costly search space creation step.
For more details and a full exemplary config, we refer to the corresponding
[example]().

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

### Candidate Control in Discrete Spaces

For discrete search spaces, campaigns provide additional control over how the candidate
set of recommendable points is built based on the trajectory the campaign has taken so
far. This is done by setting the following Boolean flags:

- `allow_recommending_already_measured`:  Controls whether points that have already been
  measured can be recommended.
- `allow_recommending_already_recommended`: Controls whether previously recommended points can
  be recommended again.
- `allow_recommending_pending_experiments`: Controls whether points marked as
  `pending_experiments` can be recommended (see [asynchronous
  workflows](async.md#pending-experiments)).

### Caching of Recommendations

The `Campaign` object caches the last batch of recommendations returned, in order to
avoid unnecessary computations for subsequent queries between which the status
of the campaign has not changed.
The cache is invalidated as soon as new measurements are added or a different
batch size is desired.
The latter is necessary because each batch is optimized for the specific number of
experiments requested (see note above).

<a id="am"></a>

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

## Acquisition Function Values

In some cases, you may want to examine the specific acquisition function values for a given set of candidates. Campaigns provide two straightforward methods for this purpose:

- `acquisition_values()`: Computes **individual** acquisition values for each candidate in the set, answering the question  *“What is the expected utility of running this experiment in isolation?”*
- `joint_acquisition_value()`: Computes the **joint** acquisition value for the entire candidate batch, answering the question  *“What is the overall expected utility of running this batch of experiments”?*

```python
rec = campaign.recommend(5)
acq_values = campaign.acquisition_values(rec)  # contains 5 numbers
joint_acq_value = campaign.joint_acquisition_value(rec)  # contains 1 number
```

By default, both methods use the acquisition function of the underlying recommender. However, you can also specify a custom acquisition function if needed:

```python
from baybe.acquisition import UCB, qPSTD

acq_values = campaign.acquisition_values(rec, UCB())
joint_acq_value = campaign.joint_acquisition_value(rec, qPSTD())
```

## Serialization

Like other BayBE objects, [`Campaigns`]() can be (de-)serialized
using their [`from_json`]()/
[`to_json`]() methods, which
allow to convert between Python objects and their corresponding representation in JSON
format:

```python
campaign_json = campaign.to_json()
reconstructed = Campaign.from_json(campaign_json)
assert campaign == reconstructed
```

General information on this topic can be found in our
[serialization user guide](serialization.md).
For campaigns, however, this possibility is particularly noteworthy as it enables
one of the most common workflows in this context –
persisting the current state of a campaign for long-term storage and continuing the
experimentation at a later point in time:

1. Get your campaign object
   * When initiating the workflow, create a new campaign object
   * When coming from the last step below, **deserialize** the existing campaign object
2. Add the latest measurement results
3. Get a recommendation
4. **Serialize** the campaign and store it somewhere
5. Run your (potentially lengthy) real-world experiments
6. Repeat

## Further Information

Campaigns are created as a first step in most of our
[examples]().
For more details on how to define campaigns for a specific use case, we thus propose
to have a look at the most suitable example.
