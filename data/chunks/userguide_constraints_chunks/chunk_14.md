# Constraints
## Discrete Constraints
### DiscretePermutationInvarianceConstraint

Permutation invariance, enabled by the
[`DiscretePermutationInvarianceConstraint`]()
, is a property where combinations of values of multiple
parameters do not depend on their order due to some symmetry in the experiment.
Suppose we create a mixture containing up to three solvents, i.e. parameters
“Solvent_1”, “Solvent_2”, “Solvent_3”.
In this situation, all combinations from the following table would be equivalent,
hence the `SearchSpace` should effectively only contain one of them.

|    | Solvent_1    | Solvent_2    | Solvent_3    |
|----|--------------|--------------|--------------|
|  1 | Substance_43 | Substance_3  | Substance_12 |
|  2 | Substance_43 | Substance_12 | Substance_3  |
|  3 | Substance_3  | Substance_12 | Substance_43 |
|  4 | Substance_3  | Substance_43 | Substance_12 |
|  5 | Substance_12 | Substance_43 | Substance_3  |
|  6 | Substance_12 | Substance_3  | Substance_43 |

#### NOTE
Complex properties such as permutation invariance not only affect the search space but
should ideally also constrain the surrogate model. For instance, the kernels in a
Gaussian process can be made permutation-invariant to reflect this constraint, which
generally results in a better learning curve. Note that at this stage no
surrogate model provided by BayBE takes care of these invariances. This means the
invariance is ignored during model fitting and these models do not benefit
from a priori known constraints and invariances between parameters. However, generally,
the optimization will still work. We are in the process of enabling this as new feature,
but in the meantime the user can introduce their own
[custom surrogate model]()
to include these.

Let’s add to the mixture example the fact that not only the choice of substance but also
their relative mixture fractions are parameters, i.e. “Fraction_1”, “Fraction_2” and
“Fraction_3”.
This also implies that the solvent parameters depend on their corresponding
fraction being `> 0.0`, because in the case `== 0.0` the choice of solvent is
irrelevant. This models a scenario that allows “up to, but not necessarily,
three solvents”.

#### IMPORTANT
If some of the `parameters` of the `DiscretePermutationInvarianceConstraint` are
dependent on other parameters, we require that the dependencies are provided as a
`DiscreteDependenciesConstraint` to the `dependencies` argument of the
`DiscretePermutationInvarianceConstraint`. This
`DiscreteDependenciesConstraint` will not count towards the maximum limit of one
`DiscreteDependenciesConstraint` discussed [here](#ddc).

The `DiscretePermutationInvarianceConstraint` below applies to our example and
removes permutation-invariant combinations of solvents that have additional
dependencies as well:

```python
from baybe.constraints import (
    DiscretePermutationInvarianceConstraint,
    DiscreteDependenciesConstraint,
    ThresholdCondition,
)

DiscretePermutationInvarianceConstraint(
    parameters=["Solvent_1", "Solvent_2", "Solvent_3"],
    # `dependencies` is optional; it is only required if some of the permutation
    # invariant entries in `parameters` have dependencies on other parameters
    dependencies=DiscreteDependenciesConstraint(
        parameters=["Fraction_1", "Fraction_2", "Fraction_3"],
        conditions=[
            ThresholdCondition(threshold=0.0, operator=">"),
            ThresholdCondition(threshold=0.0, operator=">"),
            ThresholdCondition(threshold=0.0, operator=">"),
        ],
        affected_parameters=[["Solvent_1"], ["Solvent_2"], ["Solvent_3"]],
    ),
)
```

The usage of `DiscretePermutationInvarianceConstraint` is also part of the
[example on slot-based mixtures]().