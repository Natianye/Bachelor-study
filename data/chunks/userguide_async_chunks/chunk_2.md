# Asynchronous Workflows
## Marking Experiments as Pending

To avoid repeated recommendations in the above scenario, BayBE provides the
`pending_experiments` keyword. It is available wherever recommendations can be
requested, i.e. [`Campaign.recommend`]() or
[`RecommenderProtocol.recommend`]().

Akin to `measurements` or `recommendations`, `pending_experiments` is a dataframe in
[experimental representation](searchspace.md#data-representation).
In the following example, we get a set of recommendations, add results for half of them,
and start the next recommendation, marking the other half pending:

```python
from baybe.utils.dataframe import add_fake_measurements

# Get a set of 10 recommendation
rec = campaign.recommend(batch_size=10)

# Split recommendations into two parts
rec_finished = rec.iloc[:5]
rec_pending = rec.iloc[5:]

# Add target measurements to the finished part. Here we add fake results
add_fake_measurements(rec_finished, campaign.targets)
campaign.add_measurements(rec_finished)

# Get the next set of recommendations, incorporating the still unfinished experiments.
# These will not include the experiments marked as pending again.
rec_next = campaign.recommend(10, pending_experiments=rec_pending)
```