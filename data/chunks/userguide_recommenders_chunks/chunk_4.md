# Recommenders
## Pure Recommenders
### Bayesian Recommenders

The Bayesian recommenders in BayBE are built on the foundation of the
[`BayesianRecommender`]()
class, offering an array of possibilities with internal surrogate models and support
for various acquisition functions.

* The **[`BotorchRecommender`]()**
  is a powerful recommender based on BoTorch’s optimization engine that can be applied
  to all kinds of search spaces. In continuous spaces, its `sequential_continuous` flag
  allows to choose between greedy sequential optimization and batch optimization as the
  underlying point generation mode. In discrete/hybrid spaces, sequential greedy
  selection is the only available mode and is thus activated automatically.

  Note that the recommender performs a brute-force search when applied to hybrid search
  spaces, as it does gradient-based optimization in the continuous part of the space
  while exhaustively evaluating configurations of the discrete subspace. You can customize this
  behavior to only sample a certain percentage of the discrete subspace via the
  `sampling_percentage`
  argument and to choose different sampling algorithms via the
  `hybrid_sampler`
  argument.

  The gradient-based optimization part can also further be controlled by the
  `n_restarts` and
  `n_raw_samples`
  arguments. For details, please refer
  to [BotorchRecommender]().
* The **[`NaiveHybridSpaceRecommender`]()**
  can be applied to all search spaces, but is intended to be used in hybrid spaces.
  This recommender combines individual recommenders for the continuous and the discrete
  subspaces. It independently optimizes each subspace and consolidates the best results
  to generate a candidate for the original hybrid space.