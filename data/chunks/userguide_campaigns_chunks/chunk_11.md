# Campaigns
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