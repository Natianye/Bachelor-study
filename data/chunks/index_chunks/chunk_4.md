# BayBE — A Bayesian Back End for Design of Experiments
## ⚡ Quick Start
Let us consider a simple experiment where we control three parameters and want to
maximize a single target called `Yield`.

First, install BayBE into your Python environment:

```bash
pip install baybe
```

For more information on this step, see our
[detailed installation instructions]().

### Defining the Optimization Objective

In BayBE’s language, the `Yield` can be represented as a `NumericalTarget`,
which we wrap into a `SingleTargetObjective`:

```python
from baybe.targets import NumericalTarget
from baybe.objectives import SingleTargetObjective

target = NumericalTarget(
    name="Yield",
    mode="MAX",
)
objective = SingleTargetObjective(target=target)
```

In cases where we are confronted with multiple (potentially conflicting) targets,
the `ParetoObjective` or `DesirabilityObjective` can be used instead.
These allow to define additional settings, such as how the targets should be balanced.
For more details, see the
[objectives section](https://emdgroup.github.io/baybe/stable/userguide/objectives.html)
of the user guide.