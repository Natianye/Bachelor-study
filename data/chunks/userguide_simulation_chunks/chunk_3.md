# Simulation
## The Lookup Mechanism

BayBE’s simulation package enables a wide range of use cases and can even be used for “oracle predictions”.
This is made possible through the flexible use of lookup mechanisms, which act as the loop-closing element of an optimization loop.

Lookups can be provided in a variety of ways, by using fixed data sets, analytical functions, or any other form of black-box callable.
In all cases, their role is the same: to retrieve target values for parameter configurations suggested by the recommendation engine.