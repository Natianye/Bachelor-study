# Getting Recommendations

The core functionality of BayBE is its ability to generate context-aware recommendations
for your experiments. This page covers the basics of the corresponding user interface,
assuming that a `SearchSpace` object and optional
`Objective` and measurement objects are already in place
(for more details, see the corresponding [search space](searchspace.md) /
[objective](objectives.md) user guides).

## The `recommend` Call

BayBE offers two entry points for requesting recommendations:

* <a id="stateless"></a>

  **Recommenders**<br />
  \\\\
  If a single (batch) recommendation is all you need, the most direct way to interact is
  to ask one of BayBE’s recommenders for it, by calling its
  `recommend()` method. To do so,
  simply pass all context information to the method call. This way, you interact with
  BayBE in a completely *stateless* way since all relevant components are explicitly
  provided at call time.

  For example, using the `BotorchRecommender`:
  ```python
  recommender = BotorchRecommender()
  recommendation = recommender.recommend(batch_size, searchspace, objective, measurements)
  ```
* <a id="stateful"></a>

  **Campaigns**<br />
  \\\\
  By contrast, if you plan to run an extended series of experiments where you feed newly
  arriving measurements back to BayBE and ask for a refined experimental design,
  creating a `Campaign` object that tracks the experimentation
  progress is a better choice. This offers *stateful* way of interaction where
  the context is fully maintained by the campaign object:
  ```python
  recommender = BotorchRecommender()
  campaign = Campaign(searchspace, objective, recommender)
  campaign.add_measurements(measurements)
  recommendation = campaign.recommend(batch_size)
  ```

  For more details, have a look at our [campaign user guide](campaigns.md).

## Excluding Configurations

When asking for recommendation, you often don’t want to consider all possible
combinations of parameter values (a.k.a. the full Cartesian product space) but you may
want to exclude certain configurations that are known to be infeasible or undesirable.
There are several ways to do this, including using BayBE’s sophisticated [constraint
machinery](constraints.md). Which approach is the right choice for you depends on
whether you want to exclude configurations *permanently* or (in-)activate them
*dynamically* during your experimentation cycle.

### Permanent Exclusion

Permanently excluding certain parameter configurations from the recommendation is
generally done by adjusting the `SearchSpace` object
accordingly, which defines the set of candidate configurations that will be considered.

BayBE provides several ways to achieve this, which we’ll illustrate by comparing against
the following “full” search space:

```python
searchspace_full = TaskParameter("p", ["A", "B", "C"]).to_searchspace()
```

Depending on the specific needs and complexity of the filtering operation, one approach
may be preferred over the other, but generally these mechanisms exist:

* Restricting individual parameter objects via `active_values`:
  ```python
  searchspace_reduced = TaskParameter(
      "p", ["A", "B", "C"], active_values=["A", "B"]
  ).to_searchspace()
  ```

  This is possible for all [label-like parameters](parameters.md#label-like).
* Specifying only a subset of configurations (discrete spaces only):
  ```python
  searchspace_reduced = SearchSpace.from_dataframe(
      pd.DataFrame({"p": ["A", "B"]}),
      parameters=[TaskParameter("p", ["A", "B", "C"])],
  )
  ```
* Filtering the search space using constraints:
  ```python
  searchspace_reduced = SearchSpace.from_product(
      parameters=[CategoricalParameter("p", ["A", "B", "C"])],
      constraints=[DiscreteExcludeConstraint(["p"], [SubSelectionCondition(["C"])])],
  )
  ```
* Using specialized constructors like
  `from_simplex()`.

### Dynamic Exclusion

Dynamic exclusion of candidates means to in-/exclude certain parameter configurations
while you are already in the middle of your experimentation process. Here,
we need to consider two different cases:

* **Recommenders**<br />
  \\\\
  Since recommender queries are [stateless]() with respect to the
  experimental context, you can easily adjust your search space object for each query
  as needed using any of the *permanent* exclusion methods. For example:
  ```python
  # Recommendation with full search space
  searchspace_full = CategoricalParameter("p", ["A", "B", "C"]).to_searchspace()
  recommender.recommend(batch_size, searchspace_full, objective, measurements)

  # Recommendation with reduced search space
  searchspace_reduced = TaskParameter(
      "p", ["A", "B", "C"], active_values=["A", "B"]
  ).to_searchspace()
  recommender.recommend(batch_size, searchspace_reduced, objective, measurements)
  ```
* **Campaigns**<br />
  \\\\
  Because the search space must be defined before a
  `Campaign` object can be created, a different approach is
  required for [stateful queries](). For this purpose,
  `Campaign`s provide a
  `toggle_discrete_candidates()` method that allows to
  dynamically enable or disable specific candidates while the campaign is running.
  The above example thus translates to:
  ```python
  campaign = Campaign(searchspace_full, objective, measurements)
  campaign.add_measurements(measurements)

  # Recommendation with full search space
  campaign.recommend(batch_size)

  # Exclude *matching* rows
  campaign.toggle_discrete_candidates(
      pd.DataFrame({"p": ["C"]}),
      exclude=True,
  )
  # Alternatively: Exclude *non-matching* rows
  campaign.toggle_discrete_candidates(
      pd.DataFrame({"p": ["A", "B"]}),
      complement=True,
      exclude=True,
  )

  # Recommend from reduced search space using altered candidate set
  campaign.recommend(batch_size)
  ```

  Note that you can alternatively toggle candidates by passing the appropriate
  `DiscreteConstraint` objects.
  For more details, see `toggle_discrete_candidates()`.
