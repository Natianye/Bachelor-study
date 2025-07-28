# Simulation
## Simulating Transfer Learning

The function [`simulate_transfer_learning`]() partitions the search space into its tasks and simulates each task with the training data from the remaining tasks.

#### NOTE
Currently, this only supports discrete search spaces. See [`simulate_transfer_learning`]() for the reasons.

```python
task_param = TaskParameter(
    name="Cell Line",
    values=["Liver Cell", "Brain Cell", "Skin Cell"],
)
# Define searchspace using a task parameter
searchspace = SearchSpace.from_product(parameters=[param1, param2, task_param])

# Create a suitable campaign
campaign = Campaign(searchspace=searchspace, objective=objective)

# Create a lookup dataframe. Note that this needs to have a column labeled "Function"
# with values "F1" and "F2"
lookup = DataFrame(...)

results = simulate_transfer_learning(
    campaign=campaign,
    lookup=lookup,
    batch_size=BATCH_SIZE,
    n_doe_iterations=N_DOE_ITERATIONS,
    n_mc_iterations=N_MC_ITERATIONS,
)
```