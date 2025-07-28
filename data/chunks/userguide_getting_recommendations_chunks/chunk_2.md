# Getting Recommendations

The core functionality of BayBE is its ability to generate context-aware recommendations
for your experiments. This page covers the basics of the corresponding user interface,
assuming that a `SearchSpace` object and optional
`Objective` and measurement objects are already in place

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