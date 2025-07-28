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