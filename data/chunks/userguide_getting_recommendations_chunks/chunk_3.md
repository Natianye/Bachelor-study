# Getting Recommendations
## Excluding Configurations

When asking for recommendation, you often don’t want to consider all possible
combinations of parameter values (a.k.a. the full Cartesian product space) but you may
want to exclude certain configurations that are known to be infeasible or undesirable.
There are several ways to do this, including using BayBE’s sophisticated [constraint
machinery](constraints.md). Which approach is the right choice for you depends on
whether you want to exclude configurations *permanently* or (in-)activate them
*dynamically* during your experimentation cycle.