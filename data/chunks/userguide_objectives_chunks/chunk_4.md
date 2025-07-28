# Objective
## ParetoObjective

The [`ParetoObjective`]() can be used when the
goal is to find a set of solutions that represent optimal trade-offs among
multiple conflicting targets. Unlike the
[`DesirabilityObjective`](), this approach does not aggregate the
targets into a single scalar value but instead seeks to identify the Pareto front – the
set of *non-dominated* target configurations.

Identifying the Pareto front requires maintaining explicit models for each of the
targets involved. Accordingly, it requires to use acquisition functions capable of
processing vector-valued input, such as
`qLogNoisyExpectedHypervolumeImprovement`. This differs
from the [`DesirabilityObjective`](), which relies on a single
predictive model to describe the associated desirability values. However, the drawback
of the latter is that the exact trade-off between the targets must be specified *in
advance*, through explicit target weights. By contrast, the Pareto approach allows to
specify this trade-off *after* the experiments have been carried out, giving the user
the flexibly to adjust their preferences post-hoc – knowing that each of the obtained
points is optimal with respect to a particular preference model.

To set up a [`ParetoObjective`](), simply
specify the corresponding target objects:

```python
from baybe.targets import NumericalTarget
from baybe.objectives import ParetoObjective

target_1 = NumericalTarget(name="t_1", mode="MIN")
target_2 = NumericalTarget(name="t_2", mode="MAX")
objective = ParetoObjective(targets=[target_1, target_2])
```