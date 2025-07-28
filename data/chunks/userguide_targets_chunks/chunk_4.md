# Targets
## NumericalTarget
### MATCH mode

If you want to match a desired value, the `TargetMode.MATCH` mode is the right choice.
In this mode, `bounds` are required and different transformations compared to `MIN`
and `MAX` modes are allowed.

Assume we want to instruct BayBE to match a value of 50 in a target.
We simply need to choose the bounds so that the midpoint is the desired value.
The spread of the bounds interval defines how fast the acceptability of a measurement
falls off away from the match value, also depending on the choice of `transformation`.

In the example below, `match_targetA` will treat all values < 45 and > 55 as
equally bad, while `match_targetB` is more forgiving in that it chooses a bell curve
transformation instead of a triangular one, and also uses a wider interval of bounds.
Both targets are configured such that the midpoint of `bounds` (in this case 50)
becomes the optimal value:

```python
from baybe.targets import NumericalTarget, TargetMode, TargetTransformation

match_targetA = NumericalTarget(
    name="Target_3A",
    mode=TargetMode.MATCH,
    bounds=(45, 55),  # mandatory in MATCH mode
    transformation=TargetTransformation.TRIANGULAR,  # optional, applied if bounds are not None
)
match_targetB = NumericalTarget(
    name="Target_3B",
    mode="MATCH",
    bounds=(0, 100),  # mandatory in MATCH mode
    transformation="BELL",  # can also be provided as TargetTransformation.BELL
)
```

Targets are used in nearly all [examples]().