# Constraints

Experimental campaigns often have naturally arising constraints on the parameters and
their combinations. Such constraints could for example be:

* When optimizing a mixture, the relative concentrations of the used ingredients must
  add up to 1.0.
* For chemical reactions, a reagent might be incompatible with high temperatures, hence
  these combinations must be excluded.
* Certain settings are dependent on other parameters, e.g. a set of parameters only
  becomes relevant if another parameter called `"Switch"` has the value `"on"`.

Similar to parameters, BayBE distinguishes two families of constraints, derived from the
abstract [`Constraint`]() class: discrete and
continuous constraints ([`DiscreteConstraint`](),
[`ContinuousConstraint`]()).
A constraint is called discrete/continuous if it operates on a set of exclusively
discrete/continuous parameters.