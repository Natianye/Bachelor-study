# Objective

Optimization problems involve either a single target quantity of interest or several
(potentially conflicting) targets that need to be considered simultaneously. BayBE uses
the concept of an [`Objective`]() to allow the user to
control how these different types of scenarios are handled.

## SingleTargetObjective

The need to optimize a single [`Target`]() is the most basic
type of situation one can encounter in experimental design.
In this scenario, the fact that only one target shall be considered in the design is
communicated to BayBE by wrapping the target into a
[`SingleTargetObjective`]():

```python
from baybe.targets import NumericalTarget
from baybe.objectives import SingleTargetObjective

target = NumericalTarget(name="Yield", mode="MAX")
objective = SingleTargetObjective(target)
```

In fact, the role of the
[`SingleTargetObjective`]()
is to merely signal the absence of other [`Targets`]()
in the optimization problem.
Because this fairly trivial conversion step requires no additional user configuration,
we provide a convenience constructor for it:

## DesirabilityObjective

The [`DesirabilityObjective`]()
enables the combination of multiple targets via scalarization into a single numerical
value (commonly referred to as the *overall desirability*), a method also utilized in
classical DOE.

Besides the list of [`Targets`]()
to be scalarized, this objective type takes two
additional optional parameters that let us control its behavior:

* `weights`: Specifies the relative importance of the targets in the form of a
  sequence of positive numbers, one for each target considered.<br />
  \\\\
  **Note:**
  BayBE automatically normalizes the weights, so only their relative
  scales matter.
* `scalarizer`: Specifies the [scalarization function]()
  to be used for combining the normalized target values.
  The choices are `MEAN` and `GEOM_MEAN`, referring to the arithmetic and
  geometric mean, respectively.

The definitions of the `scalarizer`s are as follows, where $\{t_i\}$ enumerate the
**normalized** target measurements of single experiment and $\{w_i\}$ are the
corresponding target weights:

$$

\text{MEAN} &= \frac{1}{\sum w_i}\sum_{i} w_i \cdot t_i \\
\text{GEOM_MEAN} &= \left( \prod_i t_i^{w_i} \right)^{1/\sum w_i}
$$

In the example below, we consider three different targets (all associated with a
different goal) and give twice as much importance to the first target relative to each
of the other two:

```python
from baybe.targets import NumericalTarget
from baybe.objectives import DesirabilityObjective

target_1 = NumericalTarget(name="t_1", mode="MIN", bounds=(0, 100))
target_2 = NumericalTarget(name="t_2", mode="MIN", bounds=(0, 100))
target_3 = NumericalTarget(name="t_3", mode="MATCH", bounds=(40, 60))
objective = DesirabilityObjective(
    targets=[target_1, target_2, target_3],
    weights=[2.0, 1.0, 1.0],  # optional (by default, all weights are equal)
    scalarizer="GEOM_MEAN",  # optional
)
```

For a complete example demonstrating desirability mode, see [here]().

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
