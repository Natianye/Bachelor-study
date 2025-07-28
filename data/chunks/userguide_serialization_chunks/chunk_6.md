# Serialization
## Deserialization from configuration strings
### Automatic field conversion

BayBE classes apply converters to their inputs so that simpler attribute
representations can be passed.
Of course, these shortcuts can be analogously used inside a configuration string.

While the above holds generally true for all classes that have converters in place,
providing a few specific example may help to convey the concept:

* Since `Intervals` can be created *implicitly*,
  it is enough the specify their bound values directly:
  ```python
  from baybe.targets import NumericalTarget
  from baybe.utils.interval import Interval

  t1 = NumericalTarget(name="T", mode="MAX", bounds=Interval(0, 1))
  t2 = NumericalTarget(name="T", mode="MAX", bounds=(0, 1))
  t3 = NumericalTarget.from_json('{"name": "T", "mode": "MAX", "bounds": [0, 1]}')

  assert t1 == t2 == t3
  ```
* Conversion to enums happens automatically whenever needed;
  therefore, providing a raw string instead is sufficient:
  ```python
  from baybe.targets import NumericalTarget, TargetMode

  t1 = NumericalTarget(name="T", mode=TargetMode.MAX)
  t2 = NumericalTarget(name="T", mode="MAX")
  t3 = NumericalTarget.from_json('{"name": "T", "mode": "MAX"}')

  assert t1 == t2 == t3
  ```