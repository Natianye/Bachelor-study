# Targets
Targets play a crucial role as the connection between observables measured in an
experiment and the machine learning core behind BayBE.
In general, it is expected that you create one [`Target`]()
object for each of your observables.
The way BayBE treats multiple targets is then controlled via the
[`Objective`](objectives.md).

## NumericalTarget

Besides the `name`, a [`NumericalTarget`]()
has the following attributes:

* **The optimization** `mode`: Specifies whether we want to minimize/maximize
  the target or whether we want to match a specific value.
* **Bounds**: Defines `bounds` that constrain the range of target values.
* **A** `transformation` **function**: When bounds are provided, this is
  used to map target values into the [0, 1] interval.

