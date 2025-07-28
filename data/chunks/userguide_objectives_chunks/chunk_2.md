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