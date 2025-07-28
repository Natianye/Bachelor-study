# Simulation
## Simulating Multiple Scenarios

The function [`simulate_scenarios`]() allows to specify multiple simulation settings at once.
Instead of a single campaign, this function expects a dictionary of campaigns, mapping scenario identifiers to `Campaign` objects.
In addition to the keyword arguments available for `simulate_experiment`, this function has two different keywords available:

1. `n_mc_iterations`: This can be used to perform multiple Monte Carlo runs with a single call. Multiple Monte Carlo runs are always advised to average out the effect of random effects such as the initial starting data.
2. `initial_data`: This can be used to provide a list of dataframe, where each dataframe is then used as initial data for an independent run. That is, the function performs one optimization loop per dataframe in this list.

Note that these two keywords are mutually exclusive.

```python
lookup = ...  # some reasonable lookup, e.g. a Callable
campaign1 = Campaign(...)
campaign2 = Campaign(...)
scenarios = {"Campaign 1": campaign1, "Campaign 2": campaign2}

results = simulate_scenarios(
    scenarios=scenarios,
    lookup=lookup,
    batch_size=batch_size,
    n_doe_iterations=n_doe_iterations,
    n_mc_iterations=n_mc_iterations,
)
```