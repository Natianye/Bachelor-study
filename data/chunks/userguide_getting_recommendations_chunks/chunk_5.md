# Getting Recommendations
## Excluding Configurations
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