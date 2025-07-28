# Search Spaces

The term “search space” refers to the domain of possible values for the parameters that are being optimized during a campaign. A search space represents the space within which BayBE explores and searches for the optimal solution. It is implemented via the [`SearchSpace`]() class.

Note that a search space is not necessarily equal to the space of allowed measurements. That is, if configured properly, it is possible to add measurements to a campaign that are not part of the search space. For instance, a numerical parameter with values `1.0`, `2.0`, `5.0` will create a searchspace with these numbers, but you can also add measurements where the parameter has a value of e.g. `2.12`.

In BayBE, a search space is a union of two (potentially empty) subspaces. The [`SubspaceDiscrete`]() contains all discrete parameters, while the [`SubspaceContinuous`]() contains all continuous parameters.

Depending on which of the subspaces are non-empty, a `SearchSpace` has exactly one of the three [`SearchSpaceType`]()’s:

| `SubspaceDiscrete`   | `SubspaceContinuous`   | [`SearchSpaceType`]()            |
|----------------------|------------------------|----------------------------------|
| Non-empty            | Empty                  | [`SearchSpaceType.DISCRETE`]()   |
| Empty                | Non-Empty              | [`SearchSpaceType.CONTINUOUS`]() |
| Non-Empty            | Non-empty              | [`SearchSpaceType.HYBRID`]()     |