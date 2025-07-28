# Recommenders
## Pure Recommenders
### Sampling Recommenders

BayBE provides two recommenders that recommend by sampling form the search space:

* **[`RandomRecommender`]():**
  This recommender offers random recommendations for all types of search spaces.
  It is extensively used in backtesting examples, providing a valuable comparison.

* **[`FPSRecommender`]():**
  This recommender is only applicable for discrete search spaces, and recommends points
  based on farthest point sampling.