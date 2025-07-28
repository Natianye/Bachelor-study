# Simulation
## Simulating a Single Experiment

The function [`simulate_experiment`]() is the most basic form of simulation.
It runs a single execution of a DoE loop for either a specific number of iteration or until the search space is fully observed.

For using this function, it is necessary to provide a [`campaign`](). Although technically not necessary, we advise to also always provide a lookup mechanisms since fake results will be produced if none is provided. It is possible to specify several additional parameters like the batch size, initial data or the number of DoE iterations that should be performed

```python
results = simulate_experiment(
    # Necessary
    campaign=campaign,
    # Technically optional but should always be set
    lookup=lookup,
    # Optional
    batch_size=batch_size,
    n_doe_iterations=n_doe_iterations,
    initial_data=initial_data,
    random_seed=random_seed,
    impute_mode=impute_mode,
    noise_percent=noise_percent,
)
```

This function returns a dataframe that contains the results. For details on the columns of this dataframe as well as the dataframes returned by the other functions discussed here, we refer to the documentation of the subpackage [here]().