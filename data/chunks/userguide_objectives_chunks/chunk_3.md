# Objective
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