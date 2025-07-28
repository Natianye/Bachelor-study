# Constraints
## Discrete Constraints

Discrete constraints currently do not affect the optimization process directly.
Instead, they act as a filter on the search space.
For instance, a search space created via [`from_product`]()
might include invalid combinations, which can be removed again by applying constraints.

Discrete constraints have in common that they operate on one or more parameters,
identified by the `parameters` member, which expects a list of parameter names as
strings.
All of these parameters must be present in the search space specification.