# Active Learning
## Local Uncertainty Reduction

In BayBE, there are two types of acquisition function that can be chosen to search for
the points with the highest predicted model uncertainty:

- [`PosteriorStandardDeviation`]() (`PSTD`)
  / [`qPosteriorStandardDeviation`]() (`qPSTD`)
- [`UpperConfidenceBound`]() (`UCB`) /
  [`qUpperConfidenceBound`]() (`qUCB`)
  with high `beta`:<br />
  \\\\
  Increasing values of `beta` effectively eliminate the effect of the posterior mean on
  the acquisition value, yielding a selection of points driven primarily by the
  posterior variance. However, we generally recommend to use this acquisition function
  only if a small exploratory component is desired – otherwise, the
  [`qPosteriorStandardDeviation`]()
  acquisition function is what you are looking for.