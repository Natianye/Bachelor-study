# Targets
## NumericalTarget
### MIN and MAX mode

Here are two examples for simple maximization and minimization targets:

```python
from baybe.targets import NumericalTarget, TargetMode, TargetTransformation

max_target = NumericalTarget(
    name="Target_1",
    mode=TargetMode.MAX,  # can also be provided as string "MAX"
)

min_target = NumericalTarget(
    name="Target_2",
    mode="MIN",  # can also be provided as TargetMode.MIN
    bounds=(0, 100),  # optional
    transformation=TargetTransformation.LINEAR,  # optional, will be applied if bounds are not None
)
```